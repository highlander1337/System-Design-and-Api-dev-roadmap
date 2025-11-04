import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from dateutil.relativedelta import relativedelta


# =======================================
#              UTILITIES
# =======================================

def parse_decimal(s):
    """Convert string with comma or dot decimal separator to float."""
    if pd.isna(s):
        return 0.0
    if isinstance(s, (int, float)):
        return float(s)
    s = str(s).replace(',', '.').strip()
    try:
        return float(s)
    except ValueError:
        return 0.0


# =======================================
#              DATA LOADING
# =======================================

def load_data(filepath: str = "ledger.csv") -> pd.DataFrame:
    """Load ledger data and normalize columns."""
    df = pd.read_csv(filepath, sep=None, engine="python")  # Auto-detect separator
    df.columns = df.columns.str.strip().str.upper()  # Normalize header names

    expected_cols = ['MONTH', 'TYPE', 'DESCRIPTION', 'VALUE', 'DATE']
    missing_cols = [col for col in expected_cols if col not in df.columns]
    if missing_cols:
        raise ValueError(f"❌ Missing expected columns: {missing_cols}")

    df['VALUE'] = df['VALUE'].apply(parse_decimal)
    df['DATE'] = pd.to_datetime(df['DATE'], errors='coerce')
    df['MONTH'] = pd.to_datetime(df['MONTH'], errors='coerce')
    df = df.dropna(subset=['DATE', 'MONTH'])
    return df


# =======================================
#             DATA PROCESSING
# =======================================

def aggregate_monthly(df: pd.DataFrame) -> pd.DataFrame:
    """Aggregate ledger entries per month and compute totals."""
    df['MONTH'] = df['DATE'].dt.to_period('M').dt.to_timestamp()
    df_agg = df.groupby(['MONTH', 'TYPE'])['VALUE'].sum().unstack(fill_value=0)

    # Ensure all relevant columns exist
    for col in ['FIXED_COST', 'VARIABLE_COST', 'INCOME']:
        if col not in df_agg.columns:
            df_agg[col] = 0.0

    df_agg['TOTAL_EXPENSES'] = df_agg['FIXED_COST'] + df_agg['VARIABLE_COST']
    df_agg = df_agg.reset_index()
    return df_agg


def calculate_equilibrium(df_agg: pd.DataFrame) -> pd.DataFrame:
    """Compute cumulative income and expenses to identify financial equilibrium."""
    df_agg = df_agg.copy()
    df_agg['CUM_NET_INCOME'] = df_agg['INCOME'].cumsum() - df_agg['TOTAL_EXPENSES'].cumsum()
    df_agg['CUM_FUTURE_EXPENSES'] = df_agg['TOTAL_EXPENSES'][::-1].cumsum()[::-1]
    df_agg['EQUILIBRIUM_BALANCE'] = df_agg['CUM_NET_INCOME'] - df_agg['CUM_FUTURE_EXPENSES']
    return df_agg


# =======================================
#             DISPLAY FUNCTIONS
# =======================================

def display_projection_table(df_agg: pd.DataFrame):
    """Display the financial equilibrium projection table."""
    print("\n📊 Financial Equilibrium Projection Table:")
    print(df_agg[['MONTH', 'TOTAL_EXPENSES', 'INCOME', 'EQUILIBRIUM_BALANCE']])


def plot_projection(df_agg: pd.DataFrame):
    """Plot income vs expenses and show the equilibrium evolution over time."""
    months = pd.to_datetime(df_agg['MONTH'])
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), sharex=True)

    # Chart 1: Equilibrium trajectory
    ax1.plot(months, df_agg['EQUILIBRIUM_BALANCE'], color='black', marker='o', label='Equilibrium Balance')
    ax1.axhline(0, color='gray', linestyle='--', linewidth=1)
    ax1.set_ylabel('Value')
    ax1.set_title('Financial Equilibrium Over Time')
    ax1.legend()
    ax1.grid(True)

    # Chart 2: Cumulative comparison
    ax2.plot(months, df_agg['CUM_NET_INCOME'], color='green', marker='o', label='Cumulative Net Income')
    ax2.plot(months, df_agg['CUM_FUTURE_EXPENSES'], color='red', marker='o', label='Cumulative Future Expenses')

    ax2.fill_between(months, df_agg['CUM_NET_INCOME'], df_agg['CUM_FUTURE_EXPENSES'],
                     where=(df_agg['CUM_NET_INCOME'] > df_agg['CUM_FUTURE_EXPENSES']),
                     color='green', alpha=0.2)
    ax2.fill_between(months, df_agg['CUM_NET_INCOME'], df_agg['CUM_FUTURE_EXPENSES'],
                     where=(df_agg['CUM_NET_INCOME'] <= df_agg['CUM_FUTURE_EXPENSES']),
                     color='red', alpha=0.2)

    ax2.set_xlabel('Month')
    ax2.set_ylabel('Cumulative Value')
    ax2.set_title('Cumulative Net Income vs Future Expenses')
    ax2.legend()
    ax2.grid(True)

    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_cost_distribution(df: pd.DataFrame):
    """Plot two pie charts:
       1. Fixed vs Variable Costs (overall)
       2. Cost breakdown by unique descriptions (e.g. 'BOLETO FIES', 'B3 INVESTMENTS')
    """
    # Filter only costs (exclude INCOME)
    cost_df = df[df['TYPE'].isin(['FIXED_COST', 'VARIABLE_COST'])]

    # 1️⃣ Aggregate totals by TYPE (Fixed vs Variable)
    type_sums = cost_df.groupby('TYPE')['VALUE'].sum().reindex(['FIXED_COST', 'VARIABLE_COST']).fillna(0)

    # 2️⃣ Aggregate totals by DESCRIPTION (individual cost items)
    desc_sums = cost_df.groupby('DESCRIPTION')['VALUE'].sum().sort_values(ascending=False)

    # ----- Plot side-by-side pies -----
    fig, axes = plt.subplots(1, 2, figsize=(14, 7))

    # Pie 1: Fixed vs Variable Costs
    axes[0].pie(
        type_sums,
        labels=type_sums.index.str.replace('_', ' ').str.title(),
        autopct='%1.1f%%',
        startangle=90,
        colors=['#FF9999', '#66B3FF']
    )
    axes[0].set_title('Fixed vs Variable Costs')

    # Pie 2: Cost Distribution by Description
    axes[1].pie(
        desc_sums,
        labels=desc_sums.index,
        autopct='%1.1f%%',
        startangle=90,
        colors=plt.cm.tab20.colors
    )
    axes[1].set_title('Cost Breakdown by Description')

    plt.tight_layout()
    plt.show()



# =======================================
#               DATA ENTRY
# =======================================

def add_entry(df: pd.DataFrame, entry_type: str):
    """Add a new ledger entry interactively, supporting repetition."""
    try:
        description = input("Enter a short description: ").strip()
        value = float(input(f"Enter {entry_type.replace('_', ' ').lower()} value: ").strip())
        date_str = input("Enter date (YYYY-MM-DD): ").strip()
        repeat_times = int(input("Repeat for how many months (including this one)? ").strip())

        date = datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        print("❌ Invalid input. Entry not added.")
        return df

    # Generate repeated monthly entries
    entries = []
    for i in range(repeat_times):
        entry_date = date + relativedelta(months=i)
        entries.append({
            'MONTH': entry_date.replace(day=1),
            'TYPE': entry_type,
            'DESCRIPTION': description,
            'VALUE': value,
            'DATE': entry_date
        })

    new_rows = pd.DataFrame(entries)
    df = pd.concat([df, new_rows], ignore_index=True)
    print(f"✅ Added {repeat_times} entry(ies) for {entry_type.replace('_', ' ').capitalize()}.")
    return df


# =======================================
#                MENU
# =======================================

def show_menu():
    """Display main program menu."""
    print("\n====== 💰 Financial Ledger Menu ======")
    print("1. Add new fixed cost")
    print("2. Add new variable cost")
    print("3. Add new salary/income")
    print("4. Show equilibrium projection table and plot")
    print("5. Show cost distribution (pie charts)")
    print("6. Save ledger")
    print("7. Exit without saving")
    print("======================================")


def main():
    """Main interactive loop."""
    try:
        df = load_data()
        print("✅ Ledger loaded successfully.")
    except FileNotFoundError:
        print("⚠️ No ledger file found. Starting a new one.")
        df = pd.DataFrame(columns=['MONTH', 'TYPE', 'DESCRIPTION', 'VALUE', 'DATE'])
    except Exception as e:
        print(f"❌ Error loading ledger: {e}")
        df = pd.DataFrame(columns=['MONTH', 'TYPE', 'DESCRIPTION', 'VALUE', 'DATE'])

    while True:
        show_menu()
        choice = input("Select an option: ").strip()

        if choice == "1":
            df = add_entry(df, "FIXED_COST")
        elif choice == "2":
            df = add_entry(df, "VARIABLE_COST")
        elif choice == "3":
            df = add_entry(df, "INCOME")
        elif choice == "4":
            if df.empty:
                print("⚠️ No data to process.")
                continue
            df_agg = aggregate_monthly(df)
            df_agg = calculate_equilibrium(df_agg)
            display_projection_table(df_agg)
            plot_projection(df_agg)
        elif choice == "5":
            if df.empty:
                print("⚠️ No data to process.")
                continue
            plot_cost_distribution(df)
        elif choice == "6":
            df.to_csv("ledger.csv", sep=',', index=False)
            print("💾 Ledger saved.")
        elif choice == "7":
            print("Exiting without saving.")
            break
        else:
            print("❌ Invalid option. Try again.")


# =======================================
#            ENTRY POINT
# =======================================
if __name__ == "__main__":
    main()

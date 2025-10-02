using System;
using System.Net.Mail;
using System.Runtime.InteropServices;
using System.Globalization;

namespace FinalQuiz
{
    // Enum to represent the result of product management actions
    enum ProductActionResult
    {
        Successful,    // Action completed successfully
        NotFound,      // Product not found in the system
        LowStock,      // Not enough stock or invalid (negative) quantity
        AlreadyExists  // Product already exists in the system
    }

    class Inventory
    {
        // Parallel lists to store product data
        List<string> products_name = new List<string>();   // Product names
        List<float> products_price = new List<float>();    // Product prices
        List<float> products_quantity = new List<float>(); // Product quantities

        // Check if a product exists by name
        public bool ProductExists(string product)
        {
            return products_name.Contains(product);
        }

        // Add a new product if it does not already exist
        public ProductActionResult AddNewProduct(string product, float price, float quantity)
        {
            if (ProductExists(product))
            {
                // Prevent duplicate products
                return ProductActionResult.AlreadyExists;
            }
            products_name.Add(product);
            products_price.Add(price);
            products_quantity.Add(quantity);
            return ProductActionResult.Successful;
        }

        // Remove a product by name if it exists
        public ProductActionResult RemoveProduct(string product)
        {
            int index = products_name.IndexOf(product);
            if (ProductExists(product))
            {
                // Remove product data from all lists
                products_name.RemoveAt(index);
                products_price.RemoveAt(index);
                products_quantity.RemoveAt(index);
                return ProductActionResult.Successful;
            }
            return ProductActionResult.NotFound;
        }

        // Return a list of all products with formatted details
        public List<string> ListAllProducts()
        {
            List<string> productList = new List<string>();
            for (int i = 0; i < products_name.Count; i++)
            {
                // Always use dot as decimal separator for price and quantity
                string productInfo = $"Product: {products_name[i]}, Price: {products_price[i].ToString(CultureInfo.InvariantCulture)}, Quantity: {products_quantity[i].ToString(CultureInfo.InvariantCulture)}";
                productList.Add(productInfo);
            }
            return productList;
        }

        // Print all products to the console
        public void PrintAllProducts()
        {
            foreach (var product in ListAllProducts())
            {
                Console.WriteLine(product);
            }
        }

        // Update the quantity of a product (private to prevent unintended use)
        // Returns LowStock if new quantity is negative
        private ProductActionResult UpdateQuantity(string product, float newQuantity)
        {
            int index = products_name.IndexOf(product);
            if (ProductExists(product))
            {
                if (newQuantity < 0)
                {
                    // Prevent negative stock
                    return ProductActionResult.LowStock;
                }
                products_quantity[index] = newQuantity;
                return ProductActionResult.Successful;
            }
            return ProductActionResult.NotFound;
        }

        // Get the quantity of a product, or -1 if not found
        private float GetQuantity(string product)
        {
            int index = products_name.IndexOf(product);
            if (ProductExists(product))
            {
                return products_quantity[index];
            }
            return -1;
        }

        // Sell a product: reduce quantity if enough stock and valid input
        // Returns LowStock if not enough stock or negative input
        public ProductActionResult SellProduct(string product, float quantitySold)
        {
            if (quantitySold < 0)
            {
                // Prevent negative sales
                return ProductActionResult.LowStock;
            }
            float currentQuantity = GetQuantity(product);
            if (!ProductExists(product))
            {
                return ProductActionResult.NotFound;
            }
            if (currentQuantity < quantitySold)
            {
                // Not enough stock to sell
                return ProductActionResult.LowStock;
            }
            var updateResult = UpdateQuantity(product, currentQuantity - quantitySold);
            return updateResult;
        }

        // Restock a product: increase quantity if valid input
        // Returns LowStock if negative input
        public ProductActionResult RestockProduct(string product, float quantityToAdd)
        {
            if (quantityToAdd < 0)
            {
                // Prevent negative restock
                return ProductActionResult.LowStock;
            }
            if (ProductExists(product))
            {
                float currentQuantity = GetQuantity(product);
                var updateResult = UpdateQuantity(product, currentQuantity + quantityToAdd);
                return updateResult;
            }
            return ProductActionResult.NotFound;
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            // Example usage of the product management system
            Inventory inventory = new Inventory();

            // Main menu loop for the product management system
            while (true)
            {
                // Display menu options
                Console.WriteLine("\nProduct Management System");
                Console.WriteLine("1. Add New Product");
                Console.WriteLine("2. Remove Product");
                Console.WriteLine("3. List All Products");
                Console.WriteLine("4. Update Product Quantity");
                Console.WriteLine("5. Sell Product");
                Console.WriteLine("6. Restock Product");
                Console.WriteLine("7. Exit");
                Console.Write("Choose an option: ");
                string? choice = Console.ReadLine();

                // Handle user selection
                switch (choice)
                {
                    case "1":
                        // Add new product flow
                        Console.Write("Enter product name: ");
                        string? nameInput = Console.ReadLine();
                        if (string.IsNullOrEmpty(nameInput))
                        {
                            Console.WriteLine("Invalid product name.");
                            break;
                        }
                        if (inventory.ProductExists(nameInput))
                        {
                            Console.WriteLine("Product already exists.");
                            break;
                        }
                        string name = nameInput;
                        Console.Write("Enter product price: ");
                        string? priceInput = Console.ReadLine();
                        float price;
                        if (string.IsNullOrEmpty(priceInput) || !float.TryParse(priceInput, NumberStyles.Float, CultureInfo.InvariantCulture, out price))
                        {
                            Console.WriteLine("Invalid product price.");
                            break;
                        }
                        Console.Write("Enter product quantity: ");
                        string? quantityInput = Console.ReadLine();
                        float quantity;
                        if (string.IsNullOrEmpty(quantityInput) || !float.TryParse(quantityInput, NumberStyles.Float, CultureInfo.InvariantCulture, out quantity))
                        {
                            Console.WriteLine("Invalid product quantity.");
                            break;
                        }
                        var addResult = inventory.AddNewProduct(name, price, quantity);
                        if (addResult == ProductActionResult.Successful)
                        {
                            Console.WriteLine("Product added successfully.");
                        }
                        else
                        {
                            Console.WriteLine("Failed to add product.");
                        }
                        break;
                    case "2":
                        // Remove product flow
                        Console.Write("Enter product name to remove: ");
                        string? removeNameInput = Console.ReadLine();
                        if (string.IsNullOrEmpty(removeNameInput))
                        {
                            Console.WriteLine("Invalid product name.");
                            break;
                        }
                        string removeName = removeNameInput;
                        var removeResult = inventory.RemoveProduct(removeName);
                        if (removeResult == ProductActionResult.Successful)
                        {
                            Console.WriteLine("Product removed successfully.");
                        }
                        else
                        {
                            Console.WriteLine("Product not found.");
                        }
                        break;
                    case "3":
                        // List all products
                        inventory.PrintAllProducts();
                        break;
                    case "4":
                        // Update product quantity flow
                        Console.Write("Enter product name to update quantity: ");
                        string? updateNameInput = Console.ReadLine();
                        if (string.IsNullOrEmpty(updateNameInput))
                        {
                            Console.WriteLine("Invalid product name.");
                            break;
                        }
                        string updateName = updateNameInput;
                        Console.Write("Enter new quantity: ");
                        string? newQuantityInput = Console.ReadLine();
                        if (string.IsNullOrEmpty(newQuantityInput))
                        {
                            Console.WriteLine("Invalid quantity.");
                            break;
                        }
                        float newQuantity = float.Parse(newQuantityInput, CultureInfo.InvariantCulture);
                        // Use reflection to call the private UpdateQuantity method
                        var updateMethod = typeof(Inventory).GetMethod("UpdateQuantity", System.Reflection.BindingFlags.NonPublic | System.Reflection.BindingFlags.Instance);
                        if (updateMethod != null)
                        {
                            var result = updateMethod.Invoke(inventory, new object[] { updateName, newQuantity });
                            if (result is ProductActionResult updateResult)
                            {
                                if (updateResult == ProductActionResult.Successful)
                                {
                                    Console.WriteLine("Quantity updated successfully.");
                                }
                                else if (updateResult == ProductActionResult.LowStock)
                                {
                                    Console.WriteLine("Invalid quantity (negative value).");
                                }
                                else
                                {
                                    Console.WriteLine("Product not found.");
                                }
                            }
                            else
                            {
                                Console.WriteLine("Failed to update quantity.");
                            }
                        }
                        else
                        {
                            Console.WriteLine("Update method not found.");
                        }
                        break;
                    case "5":
                        // Sell product flow
                        Console.Write("Enter product name to sell: ");
                        string? sellNameInput = Console.ReadLine();
                        if (string.IsNullOrEmpty(sellNameInput))
                        {
                            Console.WriteLine("Invalid product name.");
                            break;
                        }
                        string sellName = sellNameInput;
                        Console.Write("Enter quantity to sell: ");
                        string? sellQuantityInput = Console.ReadLine();
                        if (string.IsNullOrEmpty(sellQuantityInput))
                        {
                            Console.WriteLine("Invalid quantity.");
                            break;
                        }
                        float sellQuantity = float.Parse(sellQuantityInput, CultureInfo.InvariantCulture);
                        var sellResult = inventory.SellProduct(sellName, sellQuantity);
                        if (sellResult == ProductActionResult.Successful)
                        {
                            Console.WriteLine("Product sold successfully.");
                        }
                        else if (sellResult == ProductActionResult.LowStock)
                        {
                            Console.WriteLine("Insufficient quantity.");
                        }
                        else if (sellResult == ProductActionResult.NotFound)
                        {
                            Console.WriteLine("Product not found.");
                        }
                        break;
                    case "6":
                        // Restock product flow
                        Console.Write("Enter product name to restock: ");
                        string? restockNameInput = Console.ReadLine();
                        if (string.IsNullOrEmpty(restockNameInput))
                        {
                            Console.WriteLine("Invalid product name.");
                            break;
                        }
                        string restockName = restockNameInput;
                        Console.Write("Enter quantity to add: ");
                        string? restockQuantityInput = Console.ReadLine();
                        if (string.IsNullOrEmpty(restockQuantityInput))
                        {
                            Console.WriteLine("Invalid quantity.");
                            break;
                        }
                        float restockQuantity = float.Parse(restockQuantityInput, CultureInfo.InvariantCulture);
                        var restockResult = inventory.RestockProduct(restockName, restockQuantity);
                        if (restockResult == ProductActionResult.Successful)
                        {
                            Console.WriteLine("Product restocked successfully.");
                        }
                        else
                        {
                            Console.WriteLine("Product not found.");
                        }
                        break;
                    case "7":
                        // Exit the program
                        return;
                    default:
                        Console.WriteLine("Invalid option. Please try again.");
                        break;
                }
            }
        }
    }
}

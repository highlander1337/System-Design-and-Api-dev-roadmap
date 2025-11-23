using System;
using System.Linq;
using System.Collections.Generic;

class LibraryManager
{
	private class Book
	{
		public string Title { get; set; } = string.Empty;
		public bool IsCheckedOut { get; set; } = false;
	}

	static Book[] books = new Book[5];
	static int borrowedCount = 0;
	const int MaxBorrow = 3;

	static LibraryManager()
	{
		for (int i = 0; i < books.Length; i++)
			books[i] = new Book();
	}

	static void Main()
	{
		Console.WriteLine("Library Management System");

		while (true)
		{
			Console.WriteLine();
			Console.WriteLine("Choose an action:");
			Console.WriteLine("1) Add a book");
			Console.WriteLine("2) Remove a book");
			Console.WriteLine("3) Display books");
			Console.WriteLine("4) Search for a book");
			Console.WriteLine("5) Borrow a book");
			Console.WriteLine("6) Check in a book");
			Console.WriteLine("7) Exit");
			Console.Write("Choice (1-7): ");
			var input = Console.ReadLine();

			if (string.IsNullOrWhiteSpace(input) || !int.TryParse(input.Trim(), out var choice))
			{
				Console.WriteLine("Please enter a valid number between 1 and 7.");
				continue;
			}

			switch (choice)
			{
				case 1:
					AddBook();
					break;
				case 2:
					RemoveBook();
					break;
				case 3:
					DisplayBooks();
					break;
				case 4:
					SearchBook();
					break;
				case 5:
					BorrowBook();
					break;
				case 6:
					CheckInBook();
					break;
				case 7:
					Console.WriteLine("Goodbye!");
					return;
				default:
					Console.WriteLine("Invalid choice. Please select a number between 1 and 7.");
					break;
			}
		}
	}

	static void AddBook()
	{
		if (IsCollectionFull())
		{
			Console.WriteLine("The library is full. No more books can be added.");
			return;
		}

		Console.Write("Enter the title of the book to add: ");
		var newBook = Console.ReadLine()?.Trim();
		if (string.IsNullOrWhiteSpace(newBook))
		{
			Console.WriteLine("Invalid title. Nothing was added.");
			return;
		}

		if (IndexOfBook(newBook) >= 0)
		{
			Console.WriteLine("A book with that title already exists (case-insensitive). Nothing was added.");
			return;
		}

		var emptyIndex = Array.FindIndex(books, b => string.IsNullOrWhiteSpace(b.Title));
		if (emptyIndex < 0)
		{
			Console.WriteLine("Unexpected: no empty slot found.");
			return;
		}

		books[emptyIndex].Title = newBook;
		books[emptyIndex].IsCheckedOut = false;
		Console.WriteLine($"Added '{newBook}' to slot {emptyIndex + 1}.");
	}

	static void RemoveBook()
	{
		if (IsCollectionEmpty())
		{
			Console.WriteLine("There are no books to remove.");
			return;
		}
		// Show indexed list of all books for user to pick from
		var availableIndices = new List<int>();
		Console.WriteLine("Select a book to remove:");
		for (int i = 0, display = 1; i < books.Length; i++)
		{
			if (!string.IsNullOrWhiteSpace(books[i].Title))
			{
				Console.WriteLine($"{display}) {books[i].Title} (slot {i + 1}) - {(books[i].IsCheckedOut ? "Checked out" : "Available")}");
				availableIndices.Add(i);
				display++;
			}
		}

		if (availableIndices.Count == 0)
		{
			Console.WriteLine("No books available to remove.");
			return;
		}

		Console.Write($"Choose a number (1-{availableIndices.Count}): ");
		var input = Console.ReadLine();
		if (!int.TryParse(input?.Trim(), out var choice) || choice < 1 || choice > availableIndices.Count)
		{
			Console.WriteLine("Invalid selection.");
			return;
		}

		var idx = availableIndices[choice - 1];
		var removedTitle = books[idx].Title;

		// If book was checked out, decrement borrowed count so counts stay consistent
		if (books[idx].IsCheckedOut)
		{
			books[idx].IsCheckedOut = false;
			if (borrowedCount > 0) borrowedCount--;
		}

		books[idx].Title = string.Empty;
		Console.WriteLine($"Removed '{removedTitle}' from slot {idx + 1}.");
	}

	static void SearchBook()
	{
		Console.Write("Enter the title to search for: ");
		var q = Console.ReadLine()?.Trim();
		if (string.IsNullOrWhiteSpace(q))
		{
			Console.WriteLine("Invalid title.");
			return;
		}

		var idx = IndexOfBook(q);
		if (idx < 0)
		{
			Console.WriteLine("The book is not in the collection.");
			return;
		}

		if (books[idx].IsCheckedOut)
			Console.WriteLine($"'{books[idx].Title}' is in the collection but currently checked out.");
		else
			Console.WriteLine($"'{books[idx].Title}' is available in the collection.");
	}

	static void BorrowBook()
	{
		if (IsCollectionEmpty())
		{
			Console.WriteLine("There are no books to borrow.");
			return;
		}

		if (borrowedCount >= MaxBorrow)
		{
			Console.WriteLine($"You have reached the borrowing limit ({MaxBorrow}). Return a book before borrowing another.");
			return;
		}
		// Show indexed list of currently available (not checked out) books
		var availableToBorrow = new List<int>();
		Console.WriteLine("Select a book to borrow:");
		for (int i = 0, display = 1; i < books.Length; i++)
		{
			if (!string.IsNullOrWhiteSpace(books[i].Title) && !books[i].IsCheckedOut)
			{
				Console.WriteLine($"{display}) {books[i].Title} (slot {i + 1})");
				availableToBorrow.Add(i);
				display++;
			}
		}

		if (availableToBorrow.Count == 0)
		{
			Console.WriteLine("No available books to borrow.");
			return;
		}

		Console.Write($"Choose a number (1-{availableToBorrow.Count}): ");
		var input = Console.ReadLine();
		if (!int.TryParse(input?.Trim(), out var choice) || choice < 1 || choice > availableToBorrow.Count)
		{
			Console.WriteLine("Invalid selection.");
			return;
		}

		var idx = availableToBorrow[choice - 1];
		books[idx].IsCheckedOut = true;
		borrowedCount++;
		Console.WriteLine($"You have borrowed '{books[idx].Title}'. ({borrowedCount}/{MaxBorrow} borrowed)");
	}

	static void CheckInBook()
	{
		var checkedOutIndices = new List<int>();
		Console.WriteLine("Select a book to check in:");
		for (int i = 0, display = 1; i < books.Length; i++)
		{
			if (!string.IsNullOrWhiteSpace(books[i].Title) && books[i].IsCheckedOut)
			{
				Console.WriteLine($"{display}) {books[i].Title} (slot {i + 1})");
				checkedOutIndices.Add(i);
				display++;
			}
		}

		if (checkedOutIndices.Count == 0)
		{
			Console.WriteLine("No books are currently checked out.");
			return;
		}

		Console.Write($"Choose a number (1-{checkedOutIndices.Count}): ");
		var input = Console.ReadLine();
		if (!int.TryParse(input?.Trim(), out var choice) || choice < 1 || choice > checkedOutIndices.Count)
		{
			Console.WriteLine("Invalid selection.");
			return;
		}

		var idx = checkedOutIndices[choice - 1];
		books[idx].IsCheckedOut = false;
		if (borrowedCount > 0) borrowedCount--;
		Console.WriteLine($"You have checked in '{books[idx].Title}'. ({borrowedCount}/{MaxBorrow} borrowed)");
	}

	static void DisplayBooks()
	{
		Console.WriteLine();
		Console.WriteLine("Available books:");
		var any = false;
		for (int i = 0; i < books.Length; i++)
		{
			if (!string.IsNullOrWhiteSpace(books[i].Title))
			{
				var status = books[i].IsCheckedOut ? "Checked out" : "Available";
				Console.WriteLine($"- {books[i].Title} (slot {i + 1}) - {status}");
				any = true;
			}
		}

		if (!any) Console.WriteLine("(No books available)");
		Console.WriteLine();
	}

	static bool IsCollectionFull()
	{
		return books.All(b => !string.IsNullOrWhiteSpace(b.Title));
	}

	static bool IsCollectionEmpty()
	{
		return books.All(b => string.IsNullOrWhiteSpace(b.Title));
	}

	static int IndexOfBook(string title)
	{
		if (title == null) return -1;
		for (int i = 0; i < books.Length; i++)
		{
			if (!string.IsNullOrWhiteSpace(books[i].Title) && string.Equals(books[i].Title, title, StringComparison.OrdinalIgnoreCase))
				return i;
		}

		return -1;
	}
}

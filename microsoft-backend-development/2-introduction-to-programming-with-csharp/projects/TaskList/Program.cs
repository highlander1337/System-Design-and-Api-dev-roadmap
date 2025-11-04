
using System.Net.NetworkInformation;
using System.Security.Cryptography.X509Certificates;

public class ToDoList
{
    static int NUMBER_OF_TASKS = 10;

    // Array to store tasks
    public static string[] tasks = new string[NUMBER_OF_TASKS];

    // Array to store task statuses
    public static bool[] taskStatuses = new bool[NUMBER_OF_TASKS];

    // Counter to keep track of the number of tasks
    public static int taskCount = 0;

    // Menu options
    public static string[] menuOptions =
    [
        "Add Task",
        "View Tasks",
        "Mark Task as Completed",
        "Exit"
    ];  

    ///<summary>
    /// Adds a new task to the to-do list. If the list is full, it notifies the user.
    /// if the input is empty, it prompts the user that the description cannot be empty.
    ///</summary>
    public static void AddTask()
    {
        // Check if the task list is full
        if (taskCount >= NUMBER_OF_TASKS)
        {
            Console.WriteLine("Task list is full. Cannot add more tasks.");
            return;
        }
        // Prompt the user to enter a new task
        Console.Write("Enter the task description: ");
        string? input = Console.ReadLine();
        string task = input ?? string.Empty;

        // Check if the input is empty
        if (task.Trim() == string.Empty)
        {
            Console.WriteLine("Task description cannot be empty.");
            return;
        }

        // Add the new task to the array and increment the task count
        tasks[taskCount] = task;
        taskCount++;
        Console.WriteLine("Task added successfully.");
    }

    public static void ViewTasks()
    {
        // Check if there are no tasks
        if (taskCount == 0)
        {
            Console.WriteLine("No tasks in the to-do list.");
            return;
        }

        // Print all tasks in the list
        Console.WriteLine("To-Do List:");
        for (int i = 0; i < taskCount; i++)
        {
            if(taskStatuses[i])
            {
                Console.WriteLine($"{i + 1}. {tasks[i]} (Completed)");
                continue;
            }
            Console.WriteLine($"{i + 1}. {tasks[i]}");
        }
    }

    public static void MarkAsCompleted()
    {
        // Prompt the user to enter the task number to mark as completed
        Console.Write("Enter the task number to mark as completed: ");
        string? input = Console.ReadLine();
        
        // Validate the input
        int taskNumber;
        bool validInput = int.TryParse(input, out taskNumber); // Try to parse the input to an integer
        if (!validInput || taskNumber < 1 || taskNumber > taskCount)
        {
            Console.WriteLine("Invalid task number.");
            return;
        }

        // Mark the specified task as completed
        taskStatuses[taskNumber - 1] = true;
        Console.WriteLine($"Task {taskNumber} marked as completed.");
    }

    public static void Main(string[] args)
    {
        while (true)
        {
            int count = 0;
            Console.WriteLine("\nTo-Do List Menu:");

            foreach (var option in menuOptions)
            {
                count++;
                Console.WriteLine($"{count}. " + option);
            }

            Console.Write($"Choose an option (1-{menuOptions.Length}): ");

            string? choiceInput = Console.ReadLine();
            int choice;

            if (!int.TryParse(choiceInput, out choice))
            {
                Console.WriteLine($"Invalid input. Please enter a number between 1 and {menuOptions.Length}.");
                continue;
            }

            switch (choice)
            {
                case 1:
                    AddTask();
                    break;
                case 2:
                    ViewTasks();
                    break;
                case 3:
                    MarkAsCompleted();
                    break;
                case 4:
                    Console.WriteLine("Exiting the program.");
                    return;
                default:
                    break;
            }
        }
    }
}
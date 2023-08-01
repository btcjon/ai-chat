I have updated the README in our Noteable notebook with the latest information about our project. Here is the updated content:

# SimpleAIChat Framework

In this project, we are using the SimpleAIChat framework to build our application. This framework provides a simplified interface for interacting with OpenAI's ChatGPT model. It includes features such as session management, system prompts, and the ability to extend the model's capabilities with custom 'tools'.

## Key Features of SimpleAIChat

1. **Session Management**: SimpleAIChat handles session management, allowing us to maintain context between different messages in a conversation.

2. **System Prompts**: We can use system prompts to guide the model's behavior. For example, we can instruct the model to behave like a certain character or to follow certain rules.

3. **Tools**: Tools are custom functions that the model can decide to use. This allows us to extend the model's capabilities beyond what is possible with just the chat AI. For example, we can create a tool that allows the model to retrieve recent information from the internet.

## How We Are Using SimpleAIChat

We are using SimpleAIChat as the foundation for our application. We have added a Google Search tool to the framework, which allows the model to perform web searches. This tool is implemented in a similar way to the default Wikipedia tool provided by the framework.

In addition to the Google Search tool, we are also using the framework's session management feature to maintain context between messages. This allows us to have more natural and coherent conversations with the model.

We are also using system prompts to guide the model's behavior. For example, we have instructed the model to behave like a project manager and an advisor, switching between these roles as needed.

## Dos and Don'ts

When using SimpleAIChat, there are a few key principles to keep in mind:

- **Do decompose problems before resolving**: Before trying to solve a problem, it's important to break it down into smaller, more manageable parts. This can make the problem easier to understand and solve.

- **Do perform tasks step-by-step**: When implementing a feature or solving a problem, it's important to take it one step at a time. This can help prevent mistakes and make the process more manageable.

- **Don't rely on historical best practices**: SimpleAIChat allows users to specify system prompts, which can be more effective than relying on historical best practices. It's important to experiment with different prompts to find what works best.

- **Don't ignore potential security issues**: While SimpleAIChat implements some sensible security defaults, it's important to be aware of potential security issues and take steps to mitigate them.

## Updates

We have made several updates to our application to improve its functionality and usability. These updates include:

- **Google Search Tool**: We have updated our Google Search tool to be asynchronous, allowing it to perform web searches without blocking the rest of the application. This makes our application more responsive and efficient.

- **Additional Queries**: We have added the ability to specify additional queries that can trigger the use of a tool. This allows us to customize the behavior of our application to better meet our needs.

- **Code Refactoring**: We have refactored our code to improve its readability and maintainability. This includes following best practices for asynchronous programming and making our code more modular.

- **Documentation**: We have updated our documentation to provide more detailed information about our application and how to use it. This includes information about our updates and how they improve our application.


## Handling Functions and Function Calling

The simpleaichat framework is designed to handle functions and function calling in a flexible and efficient manner. Here's how it works:

Defining Functions: You can define your own functions and add them to the framework. These functions can perform a variety of tasks, such as performing a Google search, fetching data from a database, or any other task that you need for your project. The functions should be defined in a way that they can be called with a single argument, which is the user's input.

Adding Functions to the Framework: Once you've defined your functions, you can add them to the framework by passing them as a list to the tools parameter when creating an AIChat or AsyncAIChat instance. For example:

from simpleaichat import AsyncAIChat
from my_tools import my_function

ai = AsyncAIChat(api_key='my-api-key', tools=[my_function])
Function Selection: When the AI receives a user's input, it will select a function to call based on the input and the docstrings of the functions. The AI uses the OpenAI Codex model to understand the user's input and select the most appropriate function. The function's docstring should provide a clear and concise description of what the function does, as this will help the AI to select it when appropriate.

Function Calling: Once the AI has selected a function, it will call the function with the user's input as the argument. The function should return a dictionary with a context key, which contains the information retrieved by the function. This information will be used by the AI to generate a response to the user's input.

Error Handling: If an error occurs while calling a function, the AI will catch the error and generate a response indicating that an error occurred. This allows the chat to continue even if a function fails.

This approach allows the simpleaichat framework to handle a wide variety of tasks and provide dynamic and interactive responses to the user's input.

## notebook updates

You can view the updated README in our Noteable notebook [here](https://app.noteable.io/f/4a69c260-f3e1-44cd-980b-98bac5f37de9?cellID=97097d89-56fa-4f73-ad7d-6d2dc1f9b6e1).
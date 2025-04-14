# Gen-AI-Chatboot--Python
## Overview

This project implements a conversational chatbot powered by Google's Generative AI (GenAI) API. It allows users to interact with a large language model (LLM) to ask questions, generate text, and engage in natural language conversations. This project serves as a basic framework for building more advanced AI-powered chatbot applications.

## Key Features

* **Integration with Google GenAI API:** Leverages the power of Google's state-of-the-art language models.
* **Simple Conversational Interface:** Provides a basic command-line or interactive interface for users to chat.
* **Customizable Prompts:** Allows for easy modification of prompts to guide the model's responses.
* **Basic Error Handling:** Includes rudimentary error handling for API interactions.
* **Extensible Architecture:** Designed to be easily expanded with more features and functionalities.

## Prerequisites

Before you begin, ensure you have the following installed and configured:

* **Python 3.7+:** Download and install the latest version of Python from [https://www.python.org/downloads/](https://www.python.org/downloads/).
* **pip:** Python package installer (usually included with Python installations).
* **Google Cloud Project:** You need a Google Cloud Project with the Generative Language API enabled.
* **API Key:** Obtain an API key for the Generative Language API from your Google Cloud Project. Refer to the [Google Cloud documentation](https://cloud.google.com/docs/authentication/api-keys) for instructions on creating and managing API keys.
* **`google-generativeai` Python Library:** Install this library using pip (see Installation section).

## Installation

1.  **Install the required Python library:**
    ```bash
    pip install google-generativeai
    ```

2.  **Set up your API Key:**
    There are a few ways to provide your API key. Choose the method that best suits your needs:

    * **Environment Variable (Recommended for security):**
        ```bash
        export GOOGLE_API_KEY="YOUR_API_KEY"  # On Linux/macOS
        set GOOGLE_API_KEY="YOUR_API_KEY"     # On Windows
        ```
        Replace `"YOUR_API_KEY"` with your actual API key.

    * **Directly in the code (Not recommended for production):**
        You can directly assign your API key in your Python script:
        ```python
        import google.generativeai as genai

        genai.configure(api_key="YOUR_API_KEY")
        ```
        **Warning:** Avoid hardcoding your API key in your code, especially if you plan to share or version control your project.

    * **Using `.env` file (Recommended for development):**
        Create a `.env` file in your project's root directory and add your API key:
        ```
        GOOGLE_API_KEY=YOUR_API_KEY
        ```
        Then, in your Python script, load the environment variable (you might need to install the `python-dotenv` library: `pip install python-dotenv`):
        ```python
        from dotenv import load_dotenv
        import os
        import google.generativeai as genai

        load_dotenv()
        api_key = os.getenv("GOOGLE_API_KEY")
        genai.configure(api_key=api_key)
        ```
        ## Author
      **Bikram Chai**
      python Developer | Full Stack Developer | # www.linkedin.com/in/bikram-chai-a215582a8

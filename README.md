# Chatbot with Conversational Retrieval and Gradio UI

This project implements an AI-powered chatbot that provides answers based on a dataset of questions and answers. The chatbot leverages the `LangChain` library for conversational AI and vector-based retrieval using `Qdrant` to answer queries by referencing a knowledge base. It also integrates a simple user interface using `Gradio` to facilitate interaction.

## Features

- **Conversational Retrieval**: The chatbot uses LangChain's `ConversationalRetrievalChain` to retrieve relevant context from a knowledge base and generate helpful, contextually relevant responses.
- **Question Answering (QA)**: The system combines stored Q&A pairs in a CSV file to generate answers to customer support queries.
- **Real-Time Chat Interface**: A Gradio-based web interface allows for interactive conversations with the bot.
- **Source Documentation**: The chatbot provides the source documents used to generate the response.

## Prerequisites

Before you run the project, ensure you have the following installed:

- Python 3.8 or higher
- `pip` for installing Python packages

### Required Python Libraries

The following Python libraries are required for the project:

1. **LangChain**: A framework to build language model-powered applications.
2. **Gradio**: A UI library for creating interactive web interfaces.
3. **Pandas**: For working with CSV data.
4. **Qdrant**: A vector database to store and search document embeddings.
5. **OpenAI API**: Required to use OpenAI's models for language generation.

### Installation

1. Clone the repository:

    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2. Install the dependencies:

    ```bash
    pip install langchain gradio pandas openai qdrant-client
    ```

## Setup

### 1. Prepare Your Data

The chatbot expects a CSV file (`query_response_base.csv`) containing questions and answers. Ensure the file is in the same directory as the script. The CSV file should have two columns: `Question` and `Answer`. Example:

| Question                    | Answer                             |
|-----------------------------|------------------------------------|
| What is your return policy?  | Our return policy lasts 30 days.   |
| Do you offer free shipping?  | Yes, we offer free shipping.      |

### 2. Running the Chatbot

Once you've set up the environment and prepared your data, you can run the chatbot interface using the following command:

```bash
python chatbot.py



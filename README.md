## THIS IS A DRAFT OF THE README BEFORE IMPLEMETATION


# MemoryAI

MemoryAI is a personal AI assistant web application that leverages vector search and Retrieval-Augmented Generation (RAG) techniques to provide contextual responses based on user data. The application supports efficient retrieval of information from various personal data sources by converting them into vector embeddings and storing them in a MongoDB vector database.

## Features

- **Vector Search:** Utilizes advanced vector search algorithms for efficient information retrieval.
- **Retrieval-Augmented Generation (RAG):** Combines information retrieval with AI-generated responses for contextual and personalized interactions.
- **Data Integration:** Supports multiple data formats (JSON, PDF, TXT) and integrates with personal data sources like autobiography entries and calendar events to enhance the assistant's capabilities.

## Tech Stack

- **Python:** Core programming language for developing scripts and backend logic.
- **MongoDB:** Vector database for storing and retrieving embeddings efficiently.
- **Vector Search Libraries:** Libraries such as `Faiss` or `Annoy` for creating and querying vector indices.
- **Natural Language Processing (NLP):** Tools like `spaCy`, `transformers`, or `GPT` for embedding creation and AI responses.
- **Node.js:** Backend web framework for building the server-side logic and API endpoints.
- **React & JavaScript:** Frontend framework and scripting language for creating dynamic user interfaces and interactive features.

## Setup Instructions

### Prerequisites

- Python 3.7+
- Node.js and npm
- MongoDB (with vector storage capabilities)
- NLP libraries: `spaCy`, `transformers`
- Vector search libraries: `faiss` or `annoy`
- PDF parsing libraries: `PyPDF2` or `pdfminer`
- JSON and TXT file handling libraries

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/MemoryAI.git
    cd MemoryAI
    ```

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Install the required Node.js packages for the frontend:

    ```bash
    cd frontend
    npm install
    ```

4. Set up MongoDB with vector storage:

    - Follow the instructions in the [MongoDB Vector Search Setup](https://example.com/vector-search-setup) to configure your MongoDB instance.

5. Set up environment variables:

    - `MONGO_URI`: MongoDB connection string.
    - `EMBEDDING_MODEL`: Path or name of the embedding model to use.
    - `RAG_MODEL`: Path or name of the RAG model for generating responses.

    Example:

    ```bash
    export MONGO_URI="mongodb+srv://username:password@cluster.mongodb.net/memoryai?retryWrites=true&w=majority"
    export EMBEDDING_MODEL="sentence-transformers/all-MiniLM-L6-v2"
    export RAG_MODEL="facebook/bart-large"
    ```

6. Run the backend server:

    ```bash
    python app.py
    ```

7. Run the frontend development server:

    ```bash
    cd frontend
    npm start
    ```

8. Access the web application at `http://localhost:3000` for the frontend and `http://localhost:5000` for the backend.

## Usage

### Adding Data

1. **Upload Files:** Users can upload JSON, PDF, or TXT files through the web interface. The files will be converted into vector embeddings and stored in the MongoDB vector database.
2. **Personal Data Integration:** Users can connect their autobiography or calendar data to the assistant, enhancing its ability to provide personalized responses.

### Querying Data

- Users can ask questions or make requests through the web interface, and the AI assistant will respond using a combination of retrieved data and generated text, based on the integrated personal information.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or suggestions, please reach out to [mingikang31@gmail.com](mailto:mingikang31@gmail.com).

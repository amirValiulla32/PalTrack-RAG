from langchain.chains import RetrievalQA
from langchain_community.llms import Ollama  # Updated import
from langchain_community.vectorstores import FAISS  # Updated import
from langchain_community.embeddings import HuggingFaceEmbeddings  # Updated import

# Load FAISS vector database (Allow FAISS deserialization)
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vector_db = FAISS.load_local("faiss_index", embedding_model, allow_dangerous_deserialization=True)  # Fixed security warning

# Use Mistral with Ollama
llm = Ollama(model="mistral")

# Create RAG pipeline
qa = RetrievalQA.from_chain_type(
    llm=llm, 
    retriever=vector_db.as_retriever(),
    chain_type="stuff"  # Ensures all retrieved docs are used in response
)

def chat_with_bot(query):
    """
    Queries the chatbot and returns an accurate Palestine-related response.
    """
    system_prompt = (
        "You are an AI assistant focused on Palestinian history and human rights. "
        "Use only retrieved knowledge from FAISS to generate your answer. "
        "Do not hallucinate or make up facts. Cite sources when possible."
    )

    response = qa.run(f"{system_prompt}\n\nUser: {query}")
    return response

# Run chatbot in terminal
if __name__ == "__main__":
    print("✅ Chatbot is running! Type 'exit' to quit.")
    while True:
        user_input = input("\nAsk me anything about Palestine: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        response = chat_with_bot(user_input)
        print("\n💬 Chatbot:", response, "\n")

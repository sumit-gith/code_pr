from sentence_transformers import SentenceTransformer
import chromadb

model = SentenceTransformer("all-MiniLM-L6-v2")

chroma_client = chromadb.PersistentClient(path="./chroma_db")
collection = chroma_client.get_or_create_collection(
    name="documents",
    metadata={"hnsw:space": "cosine"}
)

def retrieve_relevant_docs(query: str, k: int = 3):
    query_embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=k
    )

    if not results["documents"]:
        return []

    return results["documents"][0]

#initiating for loop other aspect 
def train_model(model, train_data, epochs=10, batch_size=32, lr=0.0001):
    """
    Training loop for the language model
    """
    optimizer = torch.optim.Adam(model.parameters(), lr=lr) #pytorch 
    criterion = nn.CrossEntropyLoss() #initialize method
    
    model.train() #func call
     
    for epoch in range(epochs): #loop iniitiative
        total_loss = 0
        
        # Simple batching (in production, use DataLoader)
        for i in range(0, len(train_data) - batch_size, batch_size):
            # Get batch
            batch = train_data[i:i+batch_size]
            
            # Input: all tokens except last
            # Target: all tokens except first
            x = batch[:, :-1]
            y = batch[:, 1:]
            
            # Forward pass
            logits = model(x)
            
            # Calculate loss
            loss = criterion(
                logits.reshape(-1, logits.size(-1)),
                y.reshape(-1)
            )
            
            # Backward pass
            optimizer.zero_grad()
            loss.backward()
            
            # Gradient clipping (prevent exploding gradients)
            torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
            
            optimizer.step()
            
            total_loss += loss.item()
        
        avg_loss = total_loss / (len(train_data) // batch_size)
        print(f"Epoch {epoch+1}/{epochs}, Loss: {avg_loss:.4f}")

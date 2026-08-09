from src.rag import RAG


def main():
    rag = RAG()
    print("RAG System Ready!")

    while True:
        query = input("\nAsk Question: ")
        if query.lower() == "exit":
            break
        response = rag.ask(query)
        print("\nAnswer:\n")
        print(response)

if __name__ == "__main__":
    main()
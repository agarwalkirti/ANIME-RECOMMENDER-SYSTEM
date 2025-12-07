from langchain_groq import ChatGroq
from langchain_core.runnables import RunnablePassthrough
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain
from src.prompt_template import get_anime_prompt


class AnimeRecommender:
    def __init__(self, retriever, api_key: str, model_name: str):
        # Use Groq LLM # temperature=0 no creativeness to get clear answer. No answer fabrication
        self.llm = ChatGroq(api_key=api_key, model=model_name, temperature=0)

        # Load prompt
        self.prompt = get_anime_prompt()

        # The document-combining chain
        self.combine_docs_chain = create_stuff_documents_chain(
            llm=self.llm,
            prompt=self.prompt
        )
        question_answer_chain = self.combine_docs_chain

        # Build the retrieval chain
        self.qa_chain = create_retrieval_chain(retriever,question_answer_chain)

    def get_recommendation(self, query: str):
        response = self.qa_chain.invoke({"input": query})
        return response["answer"]


from langchain_groq import ChatGroq
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from src.prompt_template import get_anime_prompt


class AnimeRecommender:
    def __init__(self, retriever, api_key: str, model_name: str):
        # LLM
        self.llm = ChatGroq(
            api_key=api_key,
            model=model_name,
            temperature=0
        )

        # Prompt
        self.prompt = get_anime_prompt()

        # LCEL retrieval + generation chain
        self.chain = (
            {
                "context": retriever,               # retrieved docs
                "input": RunnablePassthrough(),  # user query
            }
            | self.prompt
            | self.llm
            | StrOutputParser()
        )

    def get_recommendation(self, query: str) -> str:
        return self.chain.invoke(query)


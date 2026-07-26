import json
import os

from dotenv import load_dotenv

from langchain.chat_models import init_chat_model

from rag.prompts import (
    ROUTER_PROMPT,
    ANSWER_PROMPT,
    HYBRID_PROMPT,
)

load_dotenv()


class HybridResearchAgent:

    def __init__(self, retriever):

        self.retriever = retriever

        self.llm = init_chat_model(
            model="llama-3.3-70b-versatile",
            model_provider="groq",
            api_key=os.getenv("GROQ_API_KEY"),
        )

    def route_question(self, question, pdf_context):

        prompt = ROUTER_PROMPT.format(
            context=pdf_context,
            question=question,
        )

        response = self.llm.invoke(prompt)

        answer = response.content.strip().upper()

        return "YES" in answer


    def answer_question(self, question):

        pdf_context, docs = self.retriever.search_pdf(question)

        need_web = self.route_question(
            question,
            pdf_context,
        )

        if need_web:

            web_context = self.retriever.search_web(question)

            prompt = HYBRID_PROMPT.format(
                pdf_context=pdf_context,
                web_context=web_context,
                question=question,
            )

            answer = self.llm.invoke(prompt).content

            return {
                "answer": answer,
                "used_web": True,
                "reason": "PDF did not contain enough information.",
                "sources": docs,
            }

        prompt = ANSWER_PROMPT.format(
            context=pdf_context,
            question=question,
        )

        answer = self.llm.invoke(prompt).content

        return {
            "answer": answer,
            "used_web": False,
            "reason": "Answer generated completely from PDF.",
            "sources": docs,
        }
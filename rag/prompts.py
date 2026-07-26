ROUTER_PROMPT = """
You are an intelligent research assistant.

You are given:

1. PDF Context
2. User Question

Your job is to decide whether the PDF contains enough information to answer the question.

Rules:

- If the PDF contains enough information, reply with exactly:

NEED_WEB_SEARCH = NO

- If the PDF does NOT contain enough information, reply with exactly:

NEED_WEB_SEARCH = YES

PDF Context:

{context}

Question:

{question}

Remember:
Reply ONLY with

NEED_WEB_SEARCH = YES

or

NEED_WEB_SEARCH = NO
"""


ANSWER_PROMPT = """
You are an expert research assistant.

Answer the question ONLY using the PDF context below.

If the answer is not present,
say that the uploaded document does not contain enough information.

PDF Context:

{context}

Question:

{question}
"""


HYBRID_PROMPT = """
You are an expert research assistant.

Answer the question using BOTH:

1. PDF Context
2. Web Search Results

Combine both naturally into one clear answer.

Do not mention where the information came from unless asked.

PDF Context:

{pdf_context}

Web Search:

{web_context}

Question:

{question}
"""
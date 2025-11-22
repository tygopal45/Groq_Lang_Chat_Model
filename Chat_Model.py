import os
from dotenv import load_dotenv
load_dotenv()

import gradio as gr
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage


def get_groq_response(question: str) -> str:
    if not question:
        return ""
    llm = ChatGroq(
        api_key=os.getenv("GROQ_API_KEY"),
        model="llama-3.3-70b-versatile",
        temperature=0.6,
        max_tokens=60
    )
    messages = [
        SystemMessage(content="You are a helpful assistant."),
        HumanMessage(content=question)
    ]
    resp = llm.invoke(messages)
    return getattr(resp, "content", str(resp))


with gr.Blocks() as demo:
    gr.Markdown("## Q & A Chatbot")
    gr.Markdown("Type a question and click **Ask the question**.")

    txt = gr.Textbox(
        label="Input",
        placeholder="Ask a question...",
        lines=2
    )

    btn = gr.Button("Ask the question")

    out = gr.Textbox(
        label="Response",
        interactive=False,
        lines=4
    )

    btn.click(fn=get_groq_response, inputs=txt, outputs=out)


if __name__ == "__main__":
    demo.launch()

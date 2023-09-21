import openai
from datagpt.log import logger
from datagpt.config import config


class OpenAI:
    """LLM api to OpenAI ChatGPT models."""

    def __init__(self) -> None:
        if config.get("llm.openai.azure") is not None:
            openai.api_type = "azure"
            openai.api_version = config.get(
                "llm.openai.azure.api_version", default="2023-05-15"
            )
        openai.api_base = config.get(
            "llm.openai.api_base", default="https://api.openai.com/v1"
        )
        openai.api_key = config.get("llm.openai.api_key")

    def completion(self, messages: list[dict]) -> str:
        if openai.api_type == "azure":
            engine = config.get("llm.openai.azure.engine")
            chat_completion = openai.ChatCompletion.create(
                engine=engine, messages=messages, temperature=0
            )
        else:
            model = config.get("llm.openai.api_model")
            chat_completion = openai.ChatCompletion.create(
                model=model, messages=messages, temperature=0
            )
        return chat_completion.choices[0].message.content

    def ask(self, prompt: str) -> str:
        messages = [{"role": "user", "content": prompt}]
        return self.completion(messages)
from langchain.prompts import ChatPromptTemplate
messages = [
    ("system", "You are a comedian who tells jokes about {topic}."),
    ("human", "Tell me {joke_count} jokes."),
]
prompt_template = ChatPromptTemplate.from_messages(messages)
prompt = prompt_template.invoke({"topic": "lawyers", "joke_count": 3})


class BasePrompt():
    def __init__(self) -> None:
        self.prompt_template_funtion = ChatPromptTemplate.from_messages

    def invoke(self, messages, key):
        prompt_template = self.prompt_template_funtion(messages)
        return prompt_template.format_prompt(**key).to_messages()

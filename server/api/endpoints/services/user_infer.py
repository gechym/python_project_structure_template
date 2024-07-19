from src import GeminiModel, BasePrompt

def infer_llm():
    from src import BasePrompt,GeminiModel
    
    llm = GeminiModel()
    base_prompt = BasePrompt()

    history = [
        ("system", "Bạn là mội diễn viên hài về chủ đề {topic}."),
        ("human", "kể cho tôi {joke_count} câu chuyện cười ngắn."),
    ]

    prompt = base_prompt.invoke(history , {"topic": "lawyers", "joke_count": 3})
    return llm.chat(prompt)
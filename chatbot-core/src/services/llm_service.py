import os
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain


llm = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    temperature=0.7,
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

# Memory to track conversation
memory = ConversationBufferMemory(return_messages=True)
conversation = ConversationChain(llm=llm, memory=memory)

def classify_intent(message: str) -> str:
    messages = [
        SystemMessage(content="Classify the user's message into one of these intents: 'mental_health', 'greeting', 'unrelated'. Respond only with the intent name."),
        HumanMessage(content=message)
    ]
    try:
        response = llm(messages)
        return response.content.strip().lower()
    except Exception as e:
        return "unrelated"  # Fallback intent if LLM fails

def generate_response(message: str, custom_prompt: str = None) -> str:
    intent = classify_intent(message)

    if intent == "unrelated":
        return "I'm here to support your mental well-being. If there's anything you'd like to share or talk about, I'm here for you."

    # Use default or injected system prompt
    system_prompt = custom_prompt or (
        "You are a kind and supportive mental health assistant trained to help users "
        "manage stress, anxiety, or emotional struggles. Always respond with compassion, "
        "hope, and practical suggestions."
    )

    try:
        chat = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=message)
        ]
        response = llm(chat)
        memory.save_context({"input": message}, {"output": response.content})
        return response.content.strip()
    except Exception as e:
        return "I'm having trouble understanding right now. Please try again in a moment or rephrase your message."


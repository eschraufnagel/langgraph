from pprint import pprint
from langchain_core.messages import AIMessage, HumanMessage
from langchain_openai import ChatOpenAI

messages = [AIMessage(content=f"So you said you were researching American football teams?", name="Model")]
messages.append(HumanMessage(content=f"Yes, that's right.",name="Eric"))
messages.append(AIMessage(content=f"Great, what would you like to learn about.", name="Model"))
messages.append(HumanMessage(content=f"I want to learn about the best stadium to watch a football game.", name="Eric"))

for m in messages:
    m.pretty_print()

llm = ChatOpenAI(model="gpt-4o")
result = llm.invoke(messages)
type(result)
pprint(result)
from typing import TypedDict, Annotated
from langchain_core.messages import AnyMessage
from langgraph.graph.message import add_messages
from langchain_core.messages import AIMessage, HumanMessage

# Use the add_messages reducer to append messages to state (otherwise it will override state with each new message)
class MessagesState(TypedDict):
    messages: Annotated[list[AnyMessage], add_messages]

# Initial state
initial_messages = [AIMessage(content="Hello! How can I assist you?", name="Model"),
                    HumanMessage(content="I'm looking for information on NFL teams.", name="Eric")
                   ]

# New message to add
new_message = AIMessage(content="Sure, I can help with that. What specifically are you interested in?", name="Model")

# Test
output = add_messages(initial_messages , new_message)
print(output)
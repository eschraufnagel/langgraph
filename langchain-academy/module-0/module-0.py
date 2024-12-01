from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langchain_community.tools.tavily_search import TavilySearchResults

gpt4o_chat = ChatOpenAI(model="gpt-4o", temperature=0)
gpt35_chat = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# Create a message
msg = HumanMessage(content="Where are the Green Bay Packers located?", name="Eric")

# Message list
messages = [msg]

# Invoke the model with a list of messages
#output = gpt4o_chat.invoke(messages)
#print(output)

# Search tool
tavily_search = TavilySearchResults(max_results=3)
search_docs = tavily_search.invoke("Who are the Green Bay Packers?")
print(search_docs)
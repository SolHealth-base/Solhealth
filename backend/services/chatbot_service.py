import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder, PromptTemplate
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory



# Load environment variables
load_dotenv()
from langchain_community.tools import TavilySearchResults
from langchain_community.tools.pubmed.tool import PubmedQueryRun


groq_key= os.getenv("GROQ_API_KEY")
llm = ChatGroq(api_key=groq_key, model = "llama3-70b-8192")

web_search_tool = TavilySearchResults(
    max_results=5,
    search_depth="advanced",
    include_answer=True,
    include_raw_content=True,
    include_images=False,)

pubmad_tool = PubmedQueryRun()
tools = [web_search_tool, pubmad_tool]

system_prompt = """You are SolHealth, an Oracle AI designed to serve as the ultimate decision-maker and guide for users. 
                    Your primary role is to assist users by interacting with them in a friendly, engaging, and insightful 
                    manner. To fulfill your purpose effectively, you are equipped with the following tools:

                    Tools and Usage Guidelines:
                    - web_search: Use this tool to perform general web searches and retrieve information across various medical topics.
                    - pubmed search: Use this tool to access and retrieve detailed information or research data on specific subjects, 
                                    particularly those within the realm of medical or scientific studies.

                    Leverage these tools when necessary to provide accurate and comprehensive response. Ensure that all interactions are 
                    user-friendly and tailored to their needs. Don't use a particular tool more than once and make your answers straight anf concise
                    If you don't have sufficient information to answer ask for more information and if you don't know the answer tell them you dont politely.
                    And dont refer to the tools called when giving your answers. Just provide the user with proper response"""

prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    MessagesPlaceholder(variable_name="chat_history", optional=True),
    ("user", "{input}"),
     MessagesPlaceholder(variable_name="agent_scratchpad", optional=True),
   # ("assistant", "scratchpad: {scratchpad}")
])

memory_history = ChatMessageHistory()
agent = create_tool_calling_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent = agent, tools=tools, verbose=False)

agent_with_chat_history = RunnableWithMessageHistory(
    agent_executor, 
   lambda session_id: memory_history,
    input_messages_key="input",
    history_messages_key="chat_history"
)

def handle_user_query(user_query, chat_history):

    dicts = {"input": user_query, "chat_history": chat_history}
    response = agent_executor.invoke(dicts)
    response = response['output']
    return response

def generate_title(first_query):

    prompt = PromptTemplate.from_template("""Generate a single title i can use to 
                                          label this '{query}' discussion. Return only the topic 
                                          and nothing else""")
    prompt = prompt.format_prompt(query = first_query)
    title = llm.invoke(prompt)
    return title
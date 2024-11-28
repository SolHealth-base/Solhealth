import os
import requests
import operator

from Bio import Entrez
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from serpapi import GoogleSearch
from langchain_core.tools import tool


from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langgraph.graph import StateGraph, END
from typing import TypedDict, Annotated, List
from langchain_core.agents import AgentAction
from langchain_core.messages import BaseMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

load_dotenv()

serpapi_params = {
    "engine": "google",
    "api_key": os.getenv("SERPAPI_KEY")
}


# Define your email (required by PubMed)
Entrez.email = "hundredgodwin@gmail.com"

def drug_info(links):
    results = []

    for link in links:
        response = requests.get(link)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            
            # Attempt to find the summary container
            summary_container = soup.find('div', class_="monograph_cont")
            summary = summary_container.text.strip() if summary_container else "No summary available."

            # Attempt to find the uses container
            uses_container = soup.find_all('div', class_="pgContent")
            uses = uses_container[1].text.strip() if len(uses_container) > 1 else "No uses information available."

            # Append the result
            result = f"Summary:\n{summary}\n\nUses:\n{uses}"
            results.append(result)

    # Join all results and return the final response
    final_response = "\n\n---\n\n".join(results)

    return final_response

def extract_pubmed_abstract(links):

    results = []
    for link in links:

        response = requests.get(link)

        if response.status_code == 200:
            
            soup = BeautifulSoup(response.text, "html.parser")
            abstact_container = soup.find('div', class_="abstract")
            abstract = abstact_container.text
            results.append(abstract)

    final_response = "\n".join([i for i in results])
    return final_response


# PubMed Search Tool
@tool('pubmed_search')
def pubmed_search(query: str):
    """
    Searches PubMed for scientific articles related to a given medical query.
    Returns the top articles and links to their abstracts.
    PubMed is a trusted source for peer-reviewed medical research articles.
    """
    handle = Entrez.esearch(db="pubmed", term=query, retmax=1)
    record = Entrez.read(handle)
    handle.close()

    if record["IdList"]:
        ids = record["IdList"]
        article_links = [f'https://pubmed.ncbi.nlm.nih.gov/{id}/' for id in ids]

        # Extract article abstracts (you'll need an actual method for this)
        article = extract_pubmed_abstract(article_links)

        return f"Top PubMed search results for '{query}':\n{article}"
    else:
        return "No articles found."

# Web Search Tool using Google Search
@tool('web_search')
def web_search(query: str):
    """
    Conducts a Google search using a specific medical query to find relevant
    health information or research articles. Returns the top 5 search results 
    with titles, snippets, and links.
    """
    search = GoogleSearch({
        **serpapi_params,
        "q": query,
        "num": 2
    })
    results = search.get_dict()["organic_results"]

    # Formatting results into readable output
    contexts = "\n---\n".join(
        ["\n".join([x["title"], x["snippet"], x["link"]]) for x in results]
    )
    return contexts

# Drug Search Tool on RxList
@tool('drug_search')
def drug_search(query: str):
    """
    Searches RxList for detailed drug information, including uses, side effects, 
    and warnings. RxList is a trusted source for information on prescription 
    and over-the-counter drugs.
    """
    search_url = f"https://www.rxlist.com/search/rxl/{query}"
    response = requests.get(search_url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        results_container = soup.find('div', class_="searchresults main")
        
        if results_container:
            items = results_container.find_all('li', limit=1)
            results = [item.find('a') for item in items]
            links = [link['href'] for link in results]

            # Fetch drug information (requires implementation of drug_info method)
            drugs_info = drug_info(links)

            return drugs_info
        else:
            return "No relevant RxList results found."
    else:
        return "Failed to retrieve RxList results."
    
# @tool("query_rewrite")
# def query_rewrite(user_query: str):
#     """
#     Rewrites the user's medical query by correcting any typographical errors and improving clarity 
#     to ensure the query is easily understood and more precise.
    
#     - `user_query`: The original query from the user, which may contain typos or unclear phrasing.
#     """
#     # Use language processing techniques or external services to correct and improve the query.
#     corrected_query = correct_typo_and_improve_clarity(user_query)
    
#     return corrected_query


@tool("medical_response")
def medical_response(response: str, research_steps):
    """
    Provides a detailed and reliable answer to the user's medical query.
    
    - `response`: A well-crafted, concise, and medically accurate response to the user's question.
    - `research_steps`: (Optional) Steps taken to gather the information.
    """

    if type(research_steps) is list:
        research_steps = "\n".join([f"- {r}" for r in research_steps])
    
    return response


system_prompt = """You are the oracle, the ultimate AI decision-maker. Your role is to handle the user's query using the following steps:

Steps:
1.  Direct Response: If you have enough knowledge from your internal base to answer the query, respond directly without using any external tools.
2.  Web Search: If more information is needed beyond what you know, begin by conducting a web search.
3.  Tool Use: Only resort to specialized tools (e.g., drug_search, pubmed_search) if the web search does not provide sufficient information.
4.  Drug-Related Queries: Use the drug tool exclusively for drug-related questions.
5.  Tool Usage Limit: Avoid using the same tool more than once for the same query.
6.  Efficiency: If the web search gives enough information, avoid using further tools. Otherwise, choose the most relevant tool to continue.
7.  Diverse Sources: Prioritize collecting information from a variety of resources to provide a well-rounded answer."""

prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    MessagesPlaceholder(variable_name="chat_history"),
    ("user", "{input}"),
    ("assistant", "scratchpad: {scratchpad}"),
])

tools=[
  pubmed_search,
  web_search,
  drug_search,
  medical_response,
]


class AgentState(TypedDict):
    input: str
    chat_history: list[BaseMessage]
    intermediate_steps: Annotated[list[tuple[AgentAction, str]], operator.add]

# define a function to transform intermediate_steps from list
# of AgentAction to scratchpad string
def create_scratchpad(intermediate_steps: list[AgentAction]):
    research_steps = []
    for i, action in enumerate(intermediate_steps):
        if action.log != "TBD":
            # this was the ToolExecution
           
            research_steps.append(
                f"Tool: {action.tool}, input: {action.tool_input}\n"
                f"Output: {action.log}"
            )
    return "\n---\n".join(research_steps)


# llm = ChatOpenAI(model = "gpt-4o")

groq_key= os.getenv("GROQ_API_KEY")
os.environ["OPENAI_API_KEY"] = "Your Key"


llm = ChatGroq(api_key=groq_key, model = "llama3-70b-8192")

oracle = (
    {
        "input": lambda x: x["input"],
        "chat_history": lambda x: x["chat_history"],
        "scratchpad": lambda x: create_scratchpad(
            intermediate_steps=x["intermediate_steps"]
        ),
    }
    | prompt | llm.bind_tools(tools=tools, tool_choice='auto')
)

def run_oracle(state: list):
    # Invoke the oracle and capture the output
    out = oracle.invoke(state)
    
    # Check if there are any tool calls in the output
    if out.tool_calls:
        tool_name = out.tool_calls[0]["name"]
        tool_args = out.tool_calls[0]["args"]
        action_out = AgentAction(
            tool=tool_name,
            tool_input=tool_args,
            log="TBD"
        )
        return {
            "intermediate_steps": [action_out]
        }
    else:
        # Handle cases where no tools are required
        action_out = AgentAction(
            tool="medical_response",
            tool_input={"response": out.content,
                        "research_steps": None},  # Direct response
            log=out.content
        )
        return {
            "intermediate_steps": [action_out]
        }



def router(state: list):
    # return the tool name to use
    if state["intermediate_steps"] and isinstance(state["intermediate_steps"], list):
        return state["intermediate_steps"][-1].tool
    else:
        # if we output bad format go to final answer
        print("Router invalid format")
        return "medical_response"
    
tool_str_to_func = {
   "pubmed_search": pubmed_search,
    "web_search": web_search,
    "drug_search": drug_search,
   "medical_response": medical_response
}

def run_tool(state: list):
   
    tool_name = state["intermediate_steps"][-1].tool
    tool_args = state["intermediate_steps"][-1].tool_input


   # If the tool is 'medical_response', ensure we pass 'research_steps'
    if tool_name == "medical_response":
       response = tool_args.get("response", "")
       research_steps = tool_args.get("research_steps", None)  # Pass None if not available
       out = response
    #    out = tool_str_to_func[tool_name].invoke(response=response, research_steps=research_steps)
    else:
       out = tool_str_to_func[tool_name].invoke(input=tool_args)

    action_out = AgentAction(
        tool=tool_name,
        tool_input=tool_args,
        log=str(out)
    )
    return {"intermediate_steps": [action_out]}


graph = StateGraph(AgentState)

graph.add_node("oracle", run_oracle)
graph.add_node("pubmed_search", run_tool)
graph.add_node("web_search", run_tool)
graph.add_node("drug_search", run_tool)
graph.add_node("medical_response", run_tool)

graph.set_entry_point("oracle")

graph.add_conditional_edges(
    source="oracle",  # where in graph to start
    path=router,  # function to determine which node is called
)

# create edges from each tool back to the oracle
for tool_obj in tools:
    if tool_obj.name != "medical_response":
        graph.add_edge(tool_obj.name, "oracle")

# if anything goes to final answer, it must then move to END
graph.add_edge("medical_response", END)

runnable = graph.compile()

chat_history = []
for i in range(5):

    query = input("Enter your query\n\n")
    dicts = {"input": query, "chat_history": chat_history}
    response = runnable.invoke(dicts)
    response = response["intermediate_steps"][-1].tool_input
    response = response['response']
    chat_history.append(query)
    chat_history.append(response)
    print(f"{response}\n\n")

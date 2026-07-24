from typing import TypedDict

from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_groq import ChatGroq
from langgraph.graph import StateGraph, START, END

load_dotenv()  
llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0)

class State(TypedDict):
    topic: str      
    research: str   
    draft: str      
    final: str      


def _ask(role_system: str, user: str) -> str:
    """Run one LLM call as a given role. This is the whole 'agent' -- a role + a call."""
    reply = llm.invoke([SystemMessage(content=role_system), HumanMessage(content=user)])
    return reply.content.strip()


# --- Three agents, three system prompts --------------------------------------
def researcher(state: State) -> dict:
    """Agent 1: gather a few crisp facts about the topic."""
    system = (
        "You are a Researcher. Given a topic, list 3 short factual bullet points "
        "a writer could use. Bullets only, no intro."
    )
    research = _ask(system, f"Topic: {state['topic']}")
    print("\n[researcher] produced notes:\n" + research)
    return {"research": research}


def writer(state: State) -> dict:
    """Agent 2: turn the researcher's notes into a short paragraph."""
    system = (
        "You are a Writer. Using ONLY the research notes provided, write one "
        "engaging paragraph (3-4 sentences) for a general audience."
    )
    draft = _ask(system, f"Topic: {state['topic']}\n\nResearch notes:\n{state['research']}")
    print("\n[writer] produced a draft:\n" + draft)
    return {"draft": draft}


def editor(state: State) -> dict:
    """Agent 3: tighten the writer's draft into a final version."""
    system = (
        "You are an Editor. Improve clarity and flow of the draft. Fix any awkward "
        "wording. Return ONLY the polished paragraph."
    )
    final = _ask(system, state["draft"])
    print("\n[editor] produced the final:\n" + final)
    return {"final": final}


def build_pipeline():
    """Wire the three agents into a straight line. This IS the sequential pattern."""
    g = StateGraph(State)
    g.add_node("researcher", researcher)
    g.add_node("writer", writer)
    g.add_node("editor", editor)

    g.add_edge(START, "researcher")    
    g.add_edge("researcher", "writer")  
    g.add_edge("writer", "editor")      
    g.add_edge("editor", END)         
    return g.compile()

def main() -> None:
    print("=" * 66)
    print("Sequential agents: researcher -> writer -> editor")
    print("=" * 66)

    pipeline = build_pipeline()
    topic = "why Python is popular for AI"
    result = pipeline.invoke({"topic": topic, "research": "", "draft": "", "final": ""})


    print(
        "=========================Final Output===================================="
    )
    print(result)


if __name__ == "__main__":
    main()



import os
from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage

load_dotenv()
MODEL = "llama-3.1-8b-instant"

@tool
def multiply(a: int, b: int) -> int:
    """Multiply two integers and return the exact result."""
    return a * b


@tool
def add(a: int, b: int) -> int:
    """Add two integers and return the exact result."""
    return a + b


TOOLS = [multiply, add]
TOOL_MAP = {t.name: t for t in TOOLS}


def run_loop(model, question):
    """Drive model -> tool -> model until the model stops asking for tools."""
    messages = [HumanMessage(content=question)]
    step = 0
    while True:
        step += 1
        ai = model.invoke(messages)         # the model's turn
        messages.append(ai)

        if not ai.tool_calls:               # no tool requested -> we're done
            print(f"  [step {step}] model gave the final answer")
            return ai.content

        # The model asked for one or more tools. Run each and feed results back.
        for call in ai.tool_calls:
            result = TOOL_MAP[call["name"]].invoke(call["args"])
            print(f"  [step {step}] ran {call['name']}({call['args']}) -> {result}")
            # ToolMessage MUST quote tool_call_id so the model matches Q to A.
            messages.append(ToolMessage(content=str(result), tool_call_id=call["id"]))


    
    def invoke(self, messages):
        already_used_a_tool = any(isinstance(m, ToolMessage) for m in messages)
        if not already_used_a_tool:
            # Pretend the model decided to call multiply(6, 7).
            return AIMessage(
                content="",
                tool_calls=[{"name": "multiply", "args": {"a": 6, "b": 7},
                             "id": "call_offline_1"}],
            )
        # It has the tool result now -- read it back and answer.
        last_result = [m for m in messages if isinstance(m, ToolMessage)][-1].content
        return AIMessage(content=f"The answer is {last_result}.")


if os.getenv("GROQ_API_KEY"):
    from langchain_groq import ChatGroq
    model = ChatGroq(model=MODEL, temperature=0).bind_tools(TOOLS)
    question = "What is 6 times 7, then add 100 to that?"
    print(f"Using real Groq model.\nQ: {question}")


answer = run_loop(model, question)
print(f"\nFinal answer: {answer}")
print("\nThat model -> tool -> model loop is exactly what the database project runs.")
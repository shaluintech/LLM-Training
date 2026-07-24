"""
 Module 04: Parallel agents (fan-out / fan-in)

Sometimes several agents should look at the SAME input independently and at the
same time -- like sending a draft to three reviewers at once:

                  +--> [fact-checker] --+
   [dispatch] ----+--> [seo-expert] ----+---> [aggregate] --> END
                  +--> [tone-expert] ---+

Two LangGraph mechanics make this work:
  1. FAN-OUT: add an edge from one node to SEVERAL nodes -> they run in parallel.
  2. FAN-IN with a REDUCER: each specialist appends to a shared list. A plain state
     key would OVERWRITE (last writer wins); `Annotated[list, add]` ACCUMULATES, so
     all three notes survive. (You met reducers on Day 24.)

The `aggregate` node has three incoming edges, so LangGraph waits for ALL three
specialists to finish before running it -- that's the "fan-in".

Run it (needs a free GROQ_API_KEY in a .env file next to this script):
    python parallel_agents.py
"""


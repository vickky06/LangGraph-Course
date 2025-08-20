"""Graph workflow implementation."""
from typing import Dict, Any, cast
from langgraph.graph import StateGraph, MessagesState
from langgraph.graph.state import CompiledStateGraph
from langchain_core.messages import AIMessage
from .constants import GraphNodes, LAST

def should_continue(state: MessagesState) -> str:
    """Determine if the agent should continue processing.
    
    Args:
        state: Current message state
        
    Returns:
        Next node to transition to
    """
    last_message = state["messages"][LAST]
    if not isinstance(last_message, AIMessage) or not getattr(last_message, "tool_calls", None):
        return GraphNodes.END
    return GraphNodes.ACT

def create_graph(
    run_agent_reasoning: Any, 
    tool_node: Any
) -> CompiledStateGraph[MessagesState, None, MessagesState, MessagesState]:
    """Create the agent workflow graph.
    
    Args:
        run_agent_reasoning: Agent reasoning function
        tool_node: Tool execution node
        
    Returns:
        Compiled graph
    """
    flow = StateGraph(MessagesState)

    def end_node(state: MessagesState) -> MessagesState:
        """End node that returns the final state."""
        return state

    # Add nodes
    flow.add_node(GraphNodes.AGENT_REASON, run_agent_reasoning)
    flow.set_entry_point(GraphNodes.AGENT_REASON)
    flow.add_node(GraphNodes.ACT, tool_node)
    flow.add_node(GraphNodes.END, end_node)

    # Add edges
    flow.add_conditional_edges(
        GraphNodes.AGENT_REASON, 
        should_continue, 
        {
            GraphNodes.END: GraphNodes.END,
            GraphNodes.ACT: GraphNodes.ACT
        }
    )
    flow.add_edge(GraphNodes.ACT, GraphNodes.AGENT_REASON)

    app = flow.compile()
    return app

def save_graph_visualization(graph: Any, output_path: str = "flow.png") -> None:
    """Save a visualization of the graph.
    
    Args:
        graph: Compiled graph
        output_path: Path to save the visualization
    """
    try:
        try:
            if hasattr(graph, "get_graph"):
                # Try to save as PNG first
                png_bytes = graph.get_graph().draw_mermaid_png( max_retries=5, retry_delay=2.0)
                with open(output_path, "wb") as f:
                    f.write(png_bytes)
        except Exception as e:
            ascii = graph.get_graph().print_ascii()
            print(f"Warning: Could not save graph as PNG: {str(e)}")
            print(ascii)
            
    except Exception as e:

        print(f"Warning: Could not generate graph visualization: {str(e)}")
        print("This is non-critical, the graph will still work.")

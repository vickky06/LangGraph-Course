"""
Main entry point for the LangGraph Course project.
Can be run using 'poetry run start'
"""
from src.agents.nodes import AgentNode
from src.llm.implementations import GenAI_LLMManager
from src.graph.flow import create_graph, save_graph_visualization
from src.agents.nodes import AgentNode
from src.llm.implementations import GenAI_LLMManager
from langchain_core.messages import HumanMessage  # pyright: ignore[reportMissingImports]
from src.config.settings import ConfigKey, get_config

def create_visualization(graph):
    """Create a visualization of the graph."""
    try:
        save_graph_visualization(graph, "flow.png")
    except Exception as viz_error:
        print(f"Note: Graph visualization failed: {str(viz_error)}")
        print("This is non-critical, continuing with execution...")
    
def graph_main():
    """Main entry point for the LangGraph Course project."""
    try:
        # Initialize agent and create graph
        agent = AgentNode(llm_type=GenAI_LLMManager)
        graph = create_graph(agent.run_agent_reasoning, agent.tool_node)
        return graph
        
    except Exception as e:
        print(f"Error initializing project: {str(e)}")
        return None

if __name__ == "__main__":
    graph = graph_main()
    question = "What is the temperature in Tokyo? List it and then triple it, then take the tripled value, multiply it with 7, use the value as year, and tell me a historical event from that year."
    if graph:
        # Example usage of the graph
        result = graph.invoke({"messages": [HumanMessage(content=question)]})
        if get_config(ConfigKey.VISUALIZE_GRAPH):
            create_visualization(graph)
        print("Graph execution result:", result["messages"][-1].content)
    else:
        print("Failed to initialize the graph.")    


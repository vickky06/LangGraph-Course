"""
Main entry point for the LangGraph Course project.
Can be run using 'poetry run start'
"""
from src.agents.nodes import AgentNode
from src.llm.implementations import GenAI_LLMManager
from src.graph.flow import create_graph, save_graph_visualization
from src.agents.nodes import AgentNode
from src.llm.implementations import GenAI_LLMManager
from langchain_core.messages import HumanMessage


    
def graph_main():
    """Main entry point for the LangGraph Course project."""
    try:
        # Initialize agent and create graph
        agent = AgentNode(llm_type=GenAI_LLMManager)
        graph = create_graph(agent.run_agent_reasoning, agent.tool_node)
        
        # Try to generate visualization (non-critical)
        # try:
        #     save_graph_visualization(graph, "flow.png")
        # except Exception as viz_error:
        #     print(f"Note: Graph visualization failed: {str(viz_error)}")
        #     print("This is non-critical, continuing with execution...")
        
        # print("LangGraph Course project initialized successfully.")
        return graph
        
    except Exception as e:
        print(f"Error initializing project: {str(e)}")
        return None

if __name__ == "__main__":
    graph = graph_main()
    if graph:
        # Example usage of the graph
        result = graph.invoke({"messages": [HumanMessage(content="What is tripple of 5?")]})
        print("Graph execution result:", result)
    else:
        print("Failed to initialize the graph.")    


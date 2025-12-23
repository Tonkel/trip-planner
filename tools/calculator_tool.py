from langchain_core.tools import tool

#This is all you need for a simple tool. Once the agent calls the tool it will automatically know which parameters to pass in.

class CalculatorTool:

    #use the @tool decorator to define the tool and make it available to the agent
    @tool("Make a calculation")
    def calculate(operation: str) -> float:
        """Useful to perform any mathematical calculations, like sum, minus, multiplication, division, etc. The input to this tool should be a mathematical expression, a couple examples are `200*7` or `5000/2*10.`"""
        try:
            return eval(operation)
        except Exception as e:
            return f"Error: {str(e)}"
        
    def tools():
        return [CalculatorTool.calculate]
        
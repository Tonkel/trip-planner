from langchain_core.tools import tool
from pydantic import BaseModel, Field

#This is unnecessary for simple tools, but it is a good practice for more complex tools, you can use the BaseModel class to define the input parameters

#this is a pydantic model that defines the input parameters for the tool

#A pydantic model: is a class that defines the input parameters for the tool. It is used to validate the input parameters and to generate the input schema for the tool.
class CalculatorInput(BaseModel):
    operation: str = Field(..., description="The mathematical expression to evaluate. Example: `200*7` or `5000/2*10.`")
    factor: float = Field(..., description="The factor to multiply the result by. Example: `2`")

#use the @tool decorator with the args_schema parameter pointing to the pydantic model.
@tool("perform a calculation", args_schema=CalculatorInput, return_direct=True)
def perform_calculation(operation: str, factor: float) -> str:
    """
    Performs a specific mathematical operation and multiplies the result by the givenfactor.

    Parameters:
    -operation (str) A string representing a mathematical operation (e.g., "10 + 5").
    -factor (float) A number to multiply the result by (e.g., 2).

    Returns: A string representing the result of the calculation.
    """

    #pertform the calculation and return the result
    try: 
        result = eval(operation) * factor
        return f"The result of {operation} multiplied by {factor} is {result}"
    except Exception as e:
        return f"Error: {str(e)}"


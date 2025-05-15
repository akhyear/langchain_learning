from langchain_core.runnables import RunnableMap

# Define transformations
def uppercase_name(data: dict) -> str:
    return data["name"].upper()

def double_age(data: dict) -> int:
    return data["age"] * 2

# RunnableMap: map inputs to these transformations
runnable = RunnableMap({
    "NAME_IN_CAPS": uppercase_name,
    "AGE_DOUBLED": double_age
})

# Input
input_data = {"name": "Rafin", "age": 21}

# Run the map
output = runnable.invoke(input_data)

print(output)

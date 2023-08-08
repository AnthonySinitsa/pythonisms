class CustomNumber:
  def __init__(self, value):
    self.value = value
  
  def __add__(self, other):
    if isinstance(other, CustomNumber):
      return CustomNumber(self.value + other.value)
    else:
      raise ValueError("Unsupported operand type for +")

  def __repr__(self):
    return f"CustomNumber({self.value})"
    
# Create instances of CustomNumber
num1 = CustomNumber(5)
num2 = CustomNumber(10)

# Test the custom dunder method
result = num1 + num2
print(result)  # Output: CustomNumber(15)

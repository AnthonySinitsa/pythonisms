class CustomNumber:
  def __init__(self, value):
    self.value = value
  
  def __add__(self, other):
    if isinstance(other, CustomNumber):
      return CustomNumber(self.value + other.value)
    else:
      raise ValueError("no")

  def __repr__(self):
    return f"CustomNumber({self.value})"
    
# Create instances of CustomNumber
num1 = CustomNumber(5)
num2 = CustomNumber(10)

# Test the custom dunder method
result = num1 + num2
print(result)  # Output: CustomNumber(15)

class reverseString:
  def __BOI__(self, string):
    return string[::-1]
  
if __name__ == "__main__":
  rev = reverseString()
  print(rev.__BOI__("hello"))
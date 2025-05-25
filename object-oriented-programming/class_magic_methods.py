class CompleteClass:
    """
    A class demonstrating all major Python magic methods with documentation.
    This serves as a learning reference for Python's special methods.
    """
    
    def __new__(cls, *args, **kwargs):
        """
        Called to create a new instance of the class. 
        Rarely overridden except for metaclasses or immutable types.
        """
        print("__new__ called - instance creation")
        instance = super().__new__(cls)
        return instance
    
    def __init__(self, value):
        """
        Called after instance creation for initialization.
        This is where most instance setup happens.
        """
        print("__init__ called - instance initialization")
        self.value = value
        self.items = []
    
    def __del__(self):
        """Called when instance is about to be destroyed (garbage collected)."""
        print(f"__del__ called - instance with value {self.value} is being destroyed")
    
    # Representation methods
    def __str__(self):
        """Called by str() and print() to get user-friendly string representation."""
        return f"CompleteClass instance (value={self.value})"
    
    def __repr__(self):
        """Called by repr() to get unambiguous string representation."""
        return f"CompleteClass({self.value!r})"
    
    def __format__(self, format_spec):
        """Called by format() and f-strings for custom formatting."""
        return f"Formatted: {self.value:{format_spec}}"
    
    def __bytes__(self):
        """Called by bytes() to get byte representation."""
        return str(self.value).encode('utf-8')
    
    # Comparison methods
    def __eq__(self, other):
        """Called for == operator."""
        return self.value == other.value
    
    def __ne__(self, other):
        """Called for != operator."""
        return not (self == other)
    
    def __lt__(self, other):
        """Called for < operator."""
        return self.value < other.value
    
    def __le__(self, other):
        """Called for <= operator."""
        return self.value <= other.value
    
    def __gt__(self, other):
        """Called for > operator."""
        return self.value > other.value
    
    def __ge__(self, other):
        """Called for >= operator."""
        return self.value >= other.value
    
    # Arithmetic operations
    def __add__(self, other):
        """Called for + operator."""
        return CompleteClass(self.value + other.value)
    
    def __sub__(self, other):
        """Called for - operator."""
        return CompleteClass(self.value - other.value)
    
    def __mul__(self, other):
        """Called for * operator."""
        return CompleteClass(self.value * other.value)
    
    def __truediv__(self, other):
        """Called for / operator."""
        return CompleteClass(self.value / other.value)
    
    def __floordiv__(self, other):
        """Called for // operator."""
        return CompleteClass(self.value // other.value)
    
    def __mod__(self, other):
        """Called for % operator."""
        return CompleteClass(self.value % other.value)
    
    def __pow__(self, power, modulo=None):
        """Called for ** operator."""
        return CompleteClass(pow(self.value, power.value, modulo))
    
    # Reflected arithmetic operations
    def __radd__(self, other):
        """Called when + operator with reflected operands."""
        return self.__add__(other)
    
    def __rsub__(self, other):
        """Called when - operator with reflected operands."""
        return CompleteClass(other.value - self.value)
    
    # In-place arithmetic operations
    def __iadd__(self, other):
        """Called for += operator."""
        self.value += other.value
        return self
    
    def __isub__(self, other):
        """Called for -= operator."""
        self.value -= other.value
        return self
    
    # Unary operators
    def __neg__(self):
        """Called for unary - operator."""
        return CompleteClass(-self.value)
    
    def __pos__(self):
        """Called for unary + operator."""
        return CompleteClass(+self.value)
    
    def __abs__(self):
        """Called by abs() built-in."""
        return CompleteClass(abs(self.value))
    
    def __invert__(self):
        """Called for ~ operator."""
        return CompleteClass(~self.value)
    
    # Type conversion
    def __int__(self):
        """Called by int() built-in."""
        return int(self.value)
    
    def __float__(self):
        """Called by float() built-in."""
        return float(self.value)
    
    def __bool__(self):
        """Called by bool() built-in and truth value testing."""
        return bool(self.value)
    
    def __complex__(self):
        """Called by complex() built-in."""
        return complex(self.value)
    
    # Container methods
    def __len__(self):
        """Called by len() built-in."""
        return len(self.items)
    
    def __getitem__(self, key):
        """Called for getting item with self[key]."""
        return self.items[key]
    
    def __setitem__(self, key, value):
        """Called for setting item with self[key] = value."""
        self.items[key] = value
    
    def __delitem__(self, key):
        """Called for deleting item with del self[key]."""
        del self.items[key]
    
    def __contains__(self, item):
        """Called for 'in' operator."""
        return item in self.items
    
    def __iter__(self):
        """Called when iterating over container."""
        return iter(self.items)
    
    def __reversed__(self):
        """Called by reversed() built-in."""
        return reversed(self.items)
    
    # Context managers
    def __enter__(self):
        """Called when entering 'with' block."""
        print("Entering context")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Called when exiting 'with' block."""
        print("Exiting context")
        if exc_type:
            print(f"Exception occurred: {exc_val}")
        return False  # Don't suppress exceptions
    
    # Callable objects
    def __call__(self, *args, **kwargs):
        """Called when instance is called like a function."""
        print(f"Instance called with args: {args}, kwargs: {kwargs}")
        return sum(args) + self.value
    
    # Attribute access
    def __getattr__(self, name):
        """Called when attribute not found through normal lookup."""
        print(f"Getting undefined attribute {name!r}")
        return f"DEFAULT_{name.upper()}"
    
    def __setattr__(self, name, value):
        """Called when setting any attribute."""
        print(f"Setting attribute {name!r} to {value!r}")
        super().__setattr__(name, value)
    
    def __delattr__(self, name):
        """Called when deleting an attribute."""
        print(f"Deleting attribute {name!r}")
        super().__delattr__(name)
    
    # Descriptor protocol
    def __get__(self, instance, owner):
        """Descriptor protocol: getting attribute."""
        print(f"Descriptor __get__ called with instance={instance}, owner={owner}")
        return self
    
    def __set__(self, instance, value):
        """Descriptor protocol: setting attribute."""
        print(f"Descriptor __set__ called with instance={instance}, value={value}")
    
    # Numeric type conversion
    def __index__(self):
        """Called when object is used in slice expression."""
        return int(self.value)
    
    # Asynchronous support
    async def __aiter__(self):
        """Asynchronous iterator protocol."""
        for item in self.items:
            yield item
    
    async def __anext__(self):
        """Asynchronous iterator protocol."""
        # Implementation would go here
        pass
    
    async def __aenter__(self):
        """Asynchronous context manager entry."""
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Asynchronous context manager exit."""
        pass


# Demonstration of usage
if __name__ == "__main__":
    print("=== Creating instances ===")
    obj1 = CompleteClass(10)
    obj2 = CompleteClass(20)
    
    print("\n=== String representation ===")
    print(str(obj1))
    print(repr(obj1))
    print(f"Formatted: {obj1:05d}")
    
    print("\n=== Comparisons ===")
    print(obj1 == obj2)
    print(obj1 < obj2)
    
    print("\n=== Arithmetic operations ===")
    obj3 = obj1 + obj2
    print(obj3.value)
    
    print("\n=== Container operations ===")
    obj1.items = [1, 2, 3]
    print(len(obj1))
    print(2 in obj1)
    
    print("\n=== Context manager ===")
    with obj1 as o:
        print("Inside context")
    
    print("\n=== Callable ===")
    print(obj1(5, 6, 7))
    
    print("\n=== Attribute access ===")
    print(obj1.undefined_attr)
    obj1.new_attr = 42
    del obj1.new_attr
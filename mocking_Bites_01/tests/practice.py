class FakeObject:
    def __init__(self):
        self.greet_has_been_called = False

    def greet(self, name):
        self.greet_has_been_called = True
        assert name == "Liam"
        return "Hello, Kay!"

fake_object = FakeObject()

def test1():
    assert fake_object.greet_has_been_called == False
    assert fake_object.greet("Kay") == "Hello, Kay!"
    assert fake_object.greet_has_been_called == True
    #fake_object.greet("Henry") # Raises an error

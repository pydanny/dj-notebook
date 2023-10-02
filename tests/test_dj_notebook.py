from dj_notebook import activate


def test_thing():
    plus = activate("test_harness")
    # TODO capture STDOUT and assert on it
    assert plus.print() is None

from dj_notebook.shell_plus import DiagramClass

def test_namify():
    """
    Test the `namify` method of the `DiagramClass`.
    
    Checks if the `namify` method correctly converts the class 
    name and its module into a format that replaces dots with underscores. 
    Test covers three scenarios:
    1. Built-in classes (e.g., `str`).
    2. Custom classes (e.g., `DiagramClass`).
    3. Nested classes (e.g., `OuterClass.InnerClass`).

    TODO: Maybe add scenarios of periods included in naming to
    test conversion
    """
    # Create an instance of DiagramClass - include a sample class
    diagram = DiagramClass(str)
    
    # Test built-in class
    assert diagram.namify(str) == "builtins_str"
    
    # Test custom class
    assert diagram.namify(DiagramClass) == "dj_notebook_shell_plus_DiagramClass"
    
    # Test nested class
    class OuterClass:
        class InnerClass:
            pass
    assert diagram.namify(OuterClass.InnerClass) == "tests_test_dj_notebook_InnerClass"

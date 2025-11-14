"""Example usage of launcher.py

This demonstrates how to import launcher and pass your functions to launcher.run().
"""
import launcher


def example():
    print("Example function ran!")
    print("This is the example.")


def foobar(bravo):
    print("Foobar function ran!")
    print(f"Bravo is: {bravo}")
    print("This is foobar.")


if __name__ == "__main__":
    # Use launcher.defer() to pass arguments - no lambda needed!
    launcher.run(
        example,
        launcher.defer(foobar, "Test Argument")
    )

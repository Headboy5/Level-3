#!/usr/bin/env python3
"""Simple function launcher: present a GUI picker to run one of several functions.

Usage:
    import launcher
    
    def example():
        print("example ran")
    
    def foobar(arg):
        print(f"foobar ran with {arg}")
    
    # Use launcher.defer() to pass functions with arguments:
    launcher.run(
        example,
        launcher.defer(foobar, "Test Argument"),
        launcher.defer(foobar, arg="Keyword Argument")
    )

This will open a dialog with buttons for each function; clicking one executes it.
"""
from __future__ import annotations
import sys
from typing import Callable, Any
from functools import partial

try:
    from PySide6 import QtWidgets
except ImportError:
    QtWidgets = None  # type: ignore


class DeferredCall:
    """Wrapper that defers function execution and preserves the function name."""
    def __init__(self, func: Callable, *args, **kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self.__name__ = getattr(func, "__name__", str(func))
    
    def __call__(self):
        return self.func(*self.args, **self.kwargs)


def defer(func: Callable, *args, **kwargs) -> DeferredCall:
    """Defer a function call with arguments.
    
    Args:
        func: The function to call
        *args: Positional arguments to pass
        **kwargs: Keyword arguments to pass
    
    Returns:
        A DeferredCall object that will execute the function when called
    
    Example:
        launcher.run(
            example,
            launcher.defer(foobar, "argument")
        )
    """
    return DeferredCall(func, *args, **kwargs)


class FunctionPicker(QtWidgets.QDialog):
    """Dialog that displays a button for each function; clicking runs it and closes."""

    def __init__(self, entries: list[tuple[str, Callable]], parent=None):
        super().__init__(parent)
        self.setWindowTitle("Choose a function to run")
        self.entries = entries
        self.resize(400, 200)

        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(QtWidgets.QLabel("Click a button to run that function:"))

        for name, func in entries:
            btn = QtWidgets.QPushButton(name)
            btn.clicked.connect(lambda checked=False, f=func: self._run_and_close(f))
            layout.addWidget(btn)

        cancel = QtWidgets.QPushButton("Cancel")
        cancel.clicked.connect(self.reject)
        layout.addWidget(cancel)

    def _run_and_close(self, func: Callable):
        try:
            func()
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"Function raised an exception:\n{e}")
        self.accept()


def _normalize_entry(item: Any) -> tuple[str, Callable]:
    """Convert various input formats to (name, callable) tuple."""
    # If it's a DeferredCall, extract name and callable
    if isinstance(item, DeferredCall):
        return item.__name__, item
    
    # If it's already a callable (function, lambda, partial)
    if callable(item):
        name = getattr(item, "__name__", str(item))
        return name, item
    
    # If it's a tuple: (func, args, kwargs) or (name, func, args, kwargs)
    if isinstance(item, tuple):
        if len(item) == 3:
            # (func, args, kwargs)
            func, args, kwargs = item
            name = getattr(func, "__name__", str(func))
            return name, partial(func, *args, **kwargs)
        elif len(item) == 4:
            # (name, func, args, kwargs)
            name, func, args, kwargs = item
            return name, partial(func, *args, **kwargs)
    
    raise ValueError(f"Invalid entry format: {item}")


def run(*functions: Any) -> None:
    """Open a GUI dialog to pick and run one of the provided functions.
    
    Args:
        *functions: one or more items, each can be:
            - A callable with no required args (function)
            - A DeferredCall from launcher.defer()
            - A tuple: (func, args, kwargs) where args is tuple, kwargs is dict
            - A tuple: (name, func, args, kwargs) for custom button labels
    
    Examples:
        launcher.run(func1, func2)  # no-arg functions
        launcher.run(launcher.defer(func, "arg"))  # with arguments
        launcher.run((func, ("arg",), {}))  # tuple format
        launcher.run(("Custom Name", func, ("arg",), {"key": "val"}))
    """
    if not functions:
        print("No functions provided to launcher.run()")
        return

    try:
        entries = [_normalize_entry(f) for f in functions]
    except ValueError as e:
        print(f"Error processing functions: {e}")
        return

    if QtWidgets is None:
        print("PySide6 not available; falling back to CLI picker.")
        _run_cli(entries)
        return

    app = QtWidgets.QApplication.instance()
    if app is None:
        app = QtWidgets.QApplication(sys.argv)

    picker = FunctionPicker(entries)
    picker.exec()


def _run_cli(entries: list[tuple[str, Callable]]) -> None:
    """Fallback CLI picker if PySide6 is not installed."""
    print("Select a function to run:")
    for i, (name, _) in enumerate(entries, start=1):
        print(f"  {i}. {name}")
    try:
        choice = int(input("Enter number: "))
        if 1 <= choice <= len(entries):
            _, func = entries[choice - 1]
            func()
        else:
            print("Invalid choice.")
    except (ValueError, KeyboardInterrupt):
        print("Cancelled.")


if __name__ == "__main__":
    # Simple test if run directly
    def test_a():
        print("Test A executed!")

    def test_b():
        print("Test B executed!")

    run(test_a, test_b)

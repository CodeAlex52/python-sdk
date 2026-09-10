"""Tests for context parameter detection."""

from mcp.server.mcpserver import Context
from mcp.server.mcpserver.utilities.context_injection import find_context_parameter


def test_return_annotation_is_ignored() -> None:
    def fn(value: int) -> Context: ...

    assert find_context_parameter(fn) is None


def test_optional_return_annotation_is_ignored() -> None:
    def fn(value: int) -> Context | None: ...

    assert find_context_parameter(fn) is None


def test_context_parameter_is_found() -> None:
    def fn(ctx: Context, value: int) -> int: ...

    assert find_context_parameter(fn) == "ctx"


def test_optional_context_parameter_is_found() -> None:
    def fn(ctx: Context | None) -> int: ...

    assert find_context_parameter(fn) == "ctx"

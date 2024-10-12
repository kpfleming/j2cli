from __future__ import annotations

from typing import TYPE_CHECKING

from . import (
    FilePairFactory,
    render_env,
)


if TYPE_CHECKING:  # pragma: no cover
    import pathlib


def test_short_option(
    make_file_pair: FilePairFactory,
    tmp_path: pathlib.Path,
) -> None:
    files = make_file_pair("{{ a }}", "", "json")
    out_file = tmp_path / "j2-out"
    assert "" == render_env(files, ["-o", str(out_file)], env={"a": "123"})
    assert "123" == out_file.read_text()


def test_long_option(
    make_file_pair: FilePairFactory,
    tmp_path: pathlib.Path,
) -> None:
    files = make_file_pair("{{ a }}", "", "json")
    out_file = tmp_path / "j2-out"
    assert "" == render_env(files, ["--output-file", str(out_file)], env={"a": "123"})
    assert "123" == out_file.read_text()

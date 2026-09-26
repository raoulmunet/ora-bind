from __future__ import annotations
from dataclasses import dataclass, asdict
import re

@dataclass(frozen=True)
class BindValue:
    name: str
    literal: str
    kind: str
    def to_dict(self): return asdict(self)

@dataclass(frozen=True)
class BindResult:
    sql: str
    binds: list[BindValue]

_LITERAL = re.compile(
    r"""(?P<date>\bDATE\s+'(?:''|[^'])*')|(?P<string>'(?:''|[^'])*')|(?P<number>(?<![\w$#.:])[-+]?\d+(?:\.\d+)?(?![\w$#]))""",
    re.I | re.X,
)

def convert_literals(sql: str) -> BindResult:
    binds: list[BindValue] = []
    out: list[str] = []
    i = 0
    line_comment = False
    block_comment = False
    while i < len(sql):
        if line_comment:
            out.append(sql[i])
            if sql[i] == "\n": line_comment = False
            i += 1; continue
        if block_comment:
            if sql.startswith("*/", i):
                out.append("*/"); i += 2; block_comment = False
            else:
                out.append(sql[i]); i += 1
            continue
        if sql.startswith("--", i):
            out.append("--"); i += 2; line_comment = True; continue
        if sql.startswith("/*", i):
            out.append("/*"); i += 2; block_comment = True; continue
        m = _LITERAL.match(sql, i)
        if not m:
            out.append(sql[i]); i += 1; continue
        literal = m.group(0)
        kind = "date" if m.group("date") else "string" if m.group("string") else "number"
        name = f":b{len(binds)+1}"
        binds.append(BindValue(name, literal, kind))
        out.append(name)
        i = m.end()
    return BindResult("".join(out), binds)

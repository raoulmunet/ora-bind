from __future__ import annotations
import argparse, json, sys
from pathlib import Path
from .core import convert_literals

def main(argv=None):
    p=argparse.ArgumentParser(description="Convert Oracle SQL literals to bind variables.")
    p.add_argument("source")
    p.add_argument("--format",choices=("text","json"),default="text")
    a=p.parse_args(argv)
    sql=sys.stdin.read() if a.source=="-" else Path(a.source).read_text(encoding="utf-8")
    r=convert_literals(sql)
    if a.format=="json":
        print(json.dumps({"sql":r.sql,"binds":[b.to_dict() for b in r.binds]},indent=2))
    else:
        print(r.sql.rstrip())
        if r.binds:
            print("\nBinds:")
            for b in r.binds: print(f"{b.name} = {b.literal} [{b.kind}]")
    return 0
if __name__=="__main__": raise SystemExit(main())

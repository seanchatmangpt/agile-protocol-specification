#!/usr/bin/env python3
"""Re-run the engineering-standards adoption projections for this repository.

The manifest (engineering-standards.json) and the project profile
(semantic/engineering-standards-profile.ttl) are rendered by the vendored,
blob-pinned root generator semantic/generators/render-repository-adoption.py
over the invocation parameters pinned in tools/verify.py. The AGENTS.md
root-binding header (everything up to the first ``---`` rule) is rendered from
that manifest by tools/verify.py:render_adoption_header. The local constitution
below the rule is handwritten and preserved byte-for-byte.

  --check  exit 1 and list every projection that differs from its renderer
  --write  rewrite the projections in place (never touches the handwritten body)
"""
from __future__ import annotations

import argparse
import importlib.util
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]


def load_verify():
    spec = importlib.util.spec_from_file_location("aps_verify_render", REPO / "tools/verify.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def projections(verify, root: Path) -> dict[str, bytes]:
    failures: list[str] = []
    generator = verify.load_adoption_generator(root, failures, "render")
    if generator is None:
        raise SystemExit("REFUSED: " + "; ".join(failures))
    manifest = verify.expected_adoption_manifest(generator)
    agents_path = root / verify.ADOPTION_CONSTITUTION
    current = agents_path.read_text() if agents_path.is_file() else ""
    if current.startswith("# Engineering Standards Root Binding\n") and "\n---\n" in current:
        body = current.split("\n---\n", 1)[1]
    else:
        body = "\n" + current
    return {
        verify.ADOPTION_MANIFEST: verify.expected_adoption_manifest_bytes(generator),
        verify.ADOPTION_PROFILE: verify.expected_adoption_profile(generator).encode(),
        verify.ADOPTION_CONSTITUTION: (verify.render_adoption_header(manifest) + body).encode(),
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--write", action="store_true")
    parser.add_argument("--root", type=Path, default=REPO)
    args = parser.parse_args(argv)
    verify = load_verify()
    root = args.root.resolve()
    stale = []
    for rel, data in projections(verify, root).items():
        path = root / rel
        if not path.is_file() or path.read_bytes() != data:
            stale.append(rel)
            if args.write:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(data)
    if args.check and stale:
        for rel in stale:
            print(f"STALE projection: {rel}", file=sys.stderr)
        return 1
    print(("rewrote " if args.write else "current: ") + (", ".join(stale) if args.write else "all projections"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Archive the four existing source builds; these are not Homebrew bottles."""
import hashlib
import io
import json
import os
from pathlib import Path
import subprocess
import tarfile

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "releases/local-builds-2026-10-09"
PACKAGES = [("deno", "2.9.7"), ("llvm", "23.1.2"),
            ("rust", "1.99.0"), ("zig@0.16", "0.16.0")]


def package(name, version):
    source = Path("/usr/local/Cellar") / name / version
    receipt = json.loads((source / "INSTALL_RECEIPT.json").read_text())
    assert receipt["arch"] == "x86_64", "Unexpected architecture"
    assert not receipt["built_as_bottle"], "This script is for ordinary source builds"
    receipt["source"].pop("path", None)  # Omit the builder's personal cache path.
    archive = OUT / f"{name}-{version}.macos15-x86_64.local-build.tar.gz"
    partial = archive.with_suffix(archive.suffix + ".partial")
    prefix = f"{name}/{version}"

    def normalize(info):
        if info.name == prefix + "/INSTALL_RECEIPT.json":
            return None
        info.uid = info.gid = 0
        info.uname = info.gname = ""
        assert not info.name.startswith("/"), "Absolute archive path"
        if info.issym() or info.islnk():
            assert not os.path.isabs(info.linkname), "Absolute archive link"
        return info

    with tarfile.open(partial, "w:gz", compresslevel=1) as tar:
        tar.add(source, arcname=prefix, filter=normalize)
        data = (json.dumps(receipt, indent=2) + "\n").encode()
        info = tarfile.TarInfo(prefix + "/INSTALL_RECEIPT.json")
        info.size = len(data)
        info.mode = 0o644
        tar.addfile(info, io.BytesIO(data))
    subprocess.run(["gzip", "-t", str(partial)], check=True)
    with tarfile.open(partial) as tar:
        members = tar.getnames()
        assert prefix + "/INSTALL_RECEIPT.json" in members
        assert any("LICENSE" in n or "COPYING" in n for n in members)
        assert prefix + "/.brew/" + name + ".rb" in members
    partial.replace(archive)
    with archive.open("rb") as f:
        digest = hashlib.file_digest(f, "sha256").hexdigest()
    print(f"Verified {archive.name}: {archive.stat().st_size} bytes", flush=True)
    return {"name": name, "version": version, "asset": archive.name,
            "sha256": digest, "bytes": archive.stat().st_size,
            "built_as_bottle": False, "built_on": receipt["built_on"],
            "compiler": receipt["compiler"],
            "runtime_dependencies": receipt["runtime_dependencies"]}


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    packages = [package(n, v) for n, v in PACKAGES]
    manifest = {"release": "local-builds-2026-10-09",
                "status": "experimental-local-build-archives-not-bottles",
                "architecture": "x86_64", "prefix": "/usr/local",
                "verification": "archive integrity and source-machine smoke tests only",
                "packages": packages}
    (OUT / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    (OUT / "SHA256SUMS").write_text("".join(
        f"{p['sha256']}  {p['asset']}\n" for p in packages))


if __name__ == "__main__":
    main()

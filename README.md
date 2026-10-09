# Homebrew bottles for Intel Macs

Community-maintained Homebrew bottles for Intel Macs.

## Available build archives

[Experimental local builds — 2026-10-09](https://github.com/daubas/homebrew-intel-macos/releases/tag/local-builds-2026-10-09)

- Deno 2.9.7
- LLVM 23.1.2
- Rust 1.99.0
- Zig 0.16.0 (`zig@0.16`)

These are archives of existing local source installations, **not standard Homebrew bottles**. There are currently no installable formulae in this tap; `brew install daubas/intel-macos/deno` is not available yet.

The archives preserve the installed files, license files, Homebrew receipt, and original formula. The receipt's personal source-cache path and archive owner names have been omitted. Each archive has a SHA-256 checksum. Build metadata and original formula snapshots are also recorded in [`builds/2026-10-09`](builds/2026-10-09).

## Verified environment

- Intel (`x86_64`), Kaby Lake CPU
- macOS 15.7.9 Sequoia
- Standard Homebrew prefix: `/usr/local`
- Homebrew 7.0.9; Xcode 26.3

Archive integrity and basic functionality were checked on the source machine: Deno evaluation, LLVM C compilation/execution, Rust compilation/execution, and a Zig unit test all passed. Clean-machine installation, relocation, and compatibility with other Intel CPUs or macOS versions have not been verified. Binaries may retain source-build paths.

## Dependencies

The archives do not bundle every Homebrew dependency. The manifest records the runtime dependencies and versions observed during installation. In particular, Rust links to LLVM 23; Zig links to LLVM 21 and LLD 21. These archives must not be blindly extracted over an existing Homebrew installation.

## Standard bottle publication

Future installable formulae will live under `Formula/`. To produce standard bottles:

1. Build each maintained formula with `brew install --build-bottle` on the target Intel macOS environment.
2. Package with `brew bottle`, retaining its platform tag, checksum, and relocation metadata.
3. Verify installation and package tests in a clean compatible environment.
4. Publish archives to GitHub Releases and commit the corresponding bottle definitions.

Each new version requires its own build and verification. Ordinary source installations are not represented as validated Homebrew bottles.

This is an independent community tap and is not affiliated with Homebrew. Included software retains its upstream licenses; see the license files inside each archive.

## References

- [Creating and maintaining a tap](https://docs.brew.sh/How-to-Create-and-Maintain-a-Tap)
- [Bottles](https://docs.brew.sh/Bottles)
- [Support tiers](https://docs.brew.sh/Support-Tiers)

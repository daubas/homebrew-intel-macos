# Homebrew bottles for Intel Macs

Community-maintained Homebrew bottles for Intel Macs.

## Status

This tap is being prepared. No formulae or bottles have been published yet.

The first planned package is Deno, followed by LLVM and Rust as build and testing capacity allows.

## Initial target

- Intel (`x86_64`) Macs running macOS 15 Sequoia
- Standard Homebrew prefix: `/usr/local`
- Compatibility is limited to environments verified for each published bottle

This is an independent community tap and is not affiliated with Homebrew.

## Planned installation

Once the Deno formula and its bottle are published:

```sh
brew install daubas/intel-macos/deno
```

You can add the tap now, but there are currently no packages to install:

```sh
brew tap daubas/intel-macos
```

## Publishing approach

1. Maintain formulae under `Formula/`, with upstream sources, checksums, dependencies, tests, and license declarations.
2. Build on an Intel macOS environment using `brew install --build-bottle`.
3. Package using `brew bottle` and retain its platform tag, checksum, and relocation metadata.
4. Verify installation and package tests in a clean compatible environment.
5. Publish bottle archives to GitHub Releases and commit the matching bottle definitions.

Ordinary local source installations are not treated as validated, distributable bottles. Each new package version requires a fresh build and verification.

## References

- [Homebrew: Creating and maintaining a tap](https://docs.brew.sh/How-to-Create-and-Maintain-a-Tap)
- [Homebrew: Bottles](https://docs.brew.sh/Bottles)
- [Homebrew: Support tiers](https://docs.brew.sh/Support-Tiers)

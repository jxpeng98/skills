---
name: rust-windows-cross-build
description: "Cross-build Rust applications on Apple Silicon macOS for Windows x64 MSVC, then validate the artifacts in a Parallels Windows 11 Arm guest. Use for this build-and-test loop; not as proof of native x64 hardware behavior."
---

# Rust Windows Cross Build

Use `x86_64-pc-windows-msvc` by default for ordinary Windows x64 releases. Read
`references/workflow.md` for setup commands, Parallels routes, validation tiers,
and architecture-sensitive cases.

1. Confirm the Mac is Apple Silicon, identify the Cargo workspace and expected
   Windows artifacts, and inspect `Cargo.toml`, `Cargo.lock`, `.cargo/config*`,
   `build.rs`, native dependencies, code generators, and packaging steps.
2. Reuse installed Rust, LLVM, cargo-xwin, and Parallels tooling. Ask before
   installing global tools or accepting the Microsoft SDK licence.
3. Run the project's macOS checks for portable logic, then cross-build the
   Windows release with cargo-xwin. A successful build is not a runtime pass.
4. Inspect each deliverable as PE/COFF x86-64 and collect required DLLs,
   resources, configuration, migrations, and installer files.
5. Run the packaged result inside Windows 11 Arm in Parallels, manually or with
   `prlctl` when available. Exercise startup, core workflows, persistence,
   networking, updates, failure paths, and clean-machine dependencies that
   matter to the application.
6. Add a hosted native Windows x64 CI run only when emulation cannot answer a
   release-critical question, such as drivers, CPU-specific code, JITs,
   anti-cheat, low-level installers, native plug-ins, or performance.

Report commands run, artifact paths and hashes, guest OS/build, checks passed or
failed, and residual risk. When applicable, say: "Validated on Windows 11 Arm
with x64 emulation; native Windows x64 hardware was not verified." Never claim
byte-identical output, native x64 certification, signing, or publishing without
separate evidence and authorization.

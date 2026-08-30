# Apple Silicon to Windows x64 workflow

## What this validates

`x86_64-pc-windows-msvc` produces Windows x64 PE/COFF artifacts. On Apple
Silicon, Parallels runs a Windows 11 Arm guest; Windows then runs the x64
artifact through its built-in x64 emulation. This is a real Windows API,
filesystem, registry, installer, and runtime check, but not a native x64 CPU or
driver check.

The Rust target itself is Tier 1 with host tools. Rust does not officially
support building that MSVC target from a non-Windows host; cargo-xwin supplies
that third-party cross-compilation path. Keep both facts visible when reporting
support or diagnosing native dependencies.

Use the lowest validation tier that answers the release question:

1. macOS host tests plus a Windows cross-build and PE inspection;
2. Windows 11 Arm guest execution under x64 emulation;
3. hosted native Windows x64 CI for architecture-sensitive or release-critical
   behavior. A physical Windows machine is not required.

## Preflight

Inspect before installing or changing anything:

```bash
uname -m
rustc -vV
cargo metadata --no-deps --format-version 1
rustup target list --installed
command -v clang
command -v cargo-xwin
command -v prlctl
```

Expect `arm64` from `uname -m`. Look for target-specific features, `build.rs`
scripts, C/C++ or assembly crates, bundled executables, generated code, and
runtime DLLs. Build-time tools must run on macOS; target libraries and final
applications must match Windows x64.

If tools are missing and the user authorizes machine-wide changes, the usual
setup is:

```bash
brew install llvm
rustup target add x86_64-pc-windows-msvc
cargo install --locked cargo-xwin
```

cargo-xwin downloads Microsoft CRT and Windows SDK material and requires
acceptance of Microsoft's licence. LLVM also covers clang/lld needs; native
CMake dependencies may additionally need Ninja. Install only what the project
actually requires.

## Build on macOS

Run the repository's own checks first. For a conventional workspace, a useful
fallback is:

```bash
cargo test --workspace --all-targets
cargo xwin build --workspace --release --target x86_64-pc-windows-msvc
```

When Windows test targets compile cleanly, build them without pretending they
ran on macOS:

```bash
cargo xwin test --workspace --no-run --target x86_64-pc-windows-msvc
```

The normal output root is:

```text
target/x86_64-pc-windows-msvc/release/
```

Inspect the final `.exe` and `.dll` files with what is already installed:

```bash
file target/x86_64-pc-windows-msvc/release/<app>.exe
llvm-readobj --file-headers target/x86_64-pc-windows-msvc/release/<app>.exe
```

`file` should identify a PE32+ x86-64 Windows executable. Use `llvm-readobj`
only when available. Record a SHA-256 hash for the exact package sent to the
guest:

```bash
shasum -a 256 <artifact-or-archive>
```

Do not test a lone `.exe` when the release normally includes DLLs, WebView or
other runtimes, resources, migrations, configuration, or an installer. Test the
same package users receive.

## Move the package into Parallels

Use a configured Parallels shared folder or another existing transfer route.
Do not assume a fixed `\\Mac\\Home` path: confirm the share name in File Explorer.
For tests affected by network-share paths, file locking, permissions, update
replacement, or long paths, copy the package to a local Windows directory first.

In the guest, record the Windows version and package hash, then run the relevant
CLI or GUI smoke path. A small PowerShell check can include:

```powershell
Get-CimInstance Win32_OperatingSystem |
  Select-Object Caption, Version, BuildNumber, OSArchitecture
Get-FileHash C:\path\to\package.zip -Algorithm SHA256
& C:\path\to\app.exe --version
$LASTEXITCODE
```

Adapt the command to the application. For GUI software, verify launch, first-run
state, windows and menus, file open/save, clipboard or tray behavior, networking,
restart persistence, uninstall/update behavior, and one meaningful failure path.
Use a clean VM snapshot when missing dependencies or installer behavior matters.

## Optional `prlctl` route

Prefer manual guest testing when Parallels CLI access is unavailable. Pro and
Business editions can expose `prlctl`; `prlctl exec` also requires Parallels
Tools in the guest. Confirm syntax with the installed version, then use the
shortest route:

```bash
prlctl list --all
prlctl start "<vm-name>"
prlctl exec "<vm-name>" powershell.exe -NoProfile -ExecutionPolicy Bypass -File "C:\\path\\to\\smoke.ps1"
```

Put multi-step guest checks in a shared `.ps1` file instead of building a long,
fragile quoted command. Do not place passwords on the command line.

## When the guest is not enough

Require a native Windows x64 CI job for kernel drivers, custom services with
architecture-specific binaries, anti-cheat, CPU feature detection, hand-written
assembly, JIT or SIMD correctness, native plug-in ecosystems, low-level
installer custom actions, hardware integration, or x64 performance claims.
Parallels also has graphics and nested-virtualization limits, so do not use it to
certify those paths.

For ordinary Rust GUI, CLI, HTTP, database, filesystem, registry, notification,
clipboard, tray, or WebView applications, the guest is a strong day-to-day
Windows compatibility check. Report the environment honestly rather than
turning that confidence into a guarantee.

## Primary references

- Rust target support: <https://doc.rust-lang.org/rustc/platform-support/windows-msvc.html>
- cargo-xwin usage and prerequisites: <https://github.com/rust-cross/cargo-xwin>
- Microsoft x86/x64 emulation on Arm: <https://learn.microsoft.com/windows/arm/apps-on-arm-x86-emulation>
- Microsoft Windows 11 on Apple silicon options: <https://support.microsoft.com/windows/experience/platform-variants/options-for-using-windows-11-with-mac-computers-with-apple-m1-m2-and-m3-chips>
- Parallels Windows 11 Arm installation: <https://kb.parallels.com/125375>
- Parallels shared folders: <https://docs.parallels.com/landing/pdfm-ug/v19-en-us/parallels-desktop-for-mac-19-users-guide/use-windows-on-your-mac/setting-how-windows-works-with-macos/sharing-items-between-macos-and-windows/sharing-files-and-folders>

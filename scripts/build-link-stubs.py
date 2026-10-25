#!/usr/bin/env python3
"""Archive the bootstrap no-op hooks for the kernel link."""
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
source = ROOT / 'kits/sheng/LinkStubs.c'
out = ROOT / 'build/link-stubs'
out.mkdir(parents=True, exist_ok=True)
obj, archive = out / 'LinkStubs.o', out / 'libLinkStubs.a'
subprocess.run(['xcrun', '--sdk', 'iphoneos', 'clang', '-arch', 'arm64', '-mkernel', '-miphoneos-version-min=17.0',
                '-Os', '-Wall', '-Werror', '-c', source, '-o', obj], check=True)
archive.unlink(missing_ok=True)
subprocess.run(['xcrun', 'ar', 'rcs', archive, obj], check=True)
print(archive)

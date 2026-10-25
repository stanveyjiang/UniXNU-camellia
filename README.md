# UniXNU camellia

Device repository for the Redmi Note 10 5G (`camellia`, MediaTek MT6833).

This repository is a bring-up configuration. It contains the Camellia bootstrap
defconfig, iPadOS target identity, prelink roots and device package needed by the
current XNU early-boot work. It does not claim a bootable userland.

The current configuration intentionally disables SM8550/Sheng storage, display,
input, GPU, Wi-Fi and power components. Camellia hardware integration lives in
`uefi-camellia`, the native UFS work and the device diagnostics maintained under
`/home/jiangshihao/unixnu`.

Build the kernel from a UniXNU checkout:

```sh
./unixnu defconfig camellia_bootstrap_defconfig -D ../UniXNU-camellia
./unixnu fetch xnu libplatform libdispatch AvailabilityVersions libpthread \
  corecrypto-2023 IOStorageFamily -D ../UniXNU-camellia
./unixnu build kernel -D ../UniXNU-camellia
```

The generated kernel is prelinked against the shared iPad7,1 iPadOS 17.7.11
target. That Apple image identity is separate from the MT6833 hardware profile.

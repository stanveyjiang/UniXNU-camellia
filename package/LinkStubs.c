// SPDX-License-Identifier: BSD-2-Clause-Patent
// Weak bootstrap definitions for components intentionally omitted from the
// camellia minimal kernel. Strong definitions from later archive steps replace
// them in the final link.

#include <stdint.h>

#define STUB __attribute__((weak))

void native_legacy_display_probe(void);
STUB void native_legacy_display_probe(void)
{
}

void mockfs_mountroot(void);
STUB void mockfs_mountroot(void)
{
}

STUB void *mockfs_vfsops[1];
STUB void *mockfs_vnodeop_opv_desc[1];

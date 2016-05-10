# Common HSF Tools

This is a collection of tools used within the context of the HEP
Software Foundation (HSF).

## create_project
The tool create_project creates a template CMake project. The created project
contains the standard use patterns for small CMake projects, plus support for
Doxygen and CPack. Further documentation is provided within the created
package itself inside the README.md.

## hsf_get_platform and hsf_platform_compatibility
These tools provide a way to derive and assemble the used platform
(architecture, operating system, compiler, build type) into the standard HSF form.
More details can be found int he corresponding HSF note.

#--- CMake Config Files -----------------------------------------------
# - Use CMake's module to help generating relocatable config files
include(CMakePackageConfigHelpers)

# - Versioning
write_basic_package_version_file(
  ${CMAKE_CURRENT_BINARY_DIR}/HSFTEMPLATEConfigVersion.cmake
  VERSION ${HSFTEMPLATE_VERSION}
  COMPATIBILITY SameMajorVersion)

# - Install time config and target files
configure_package_config_file(${CMAKE_CURRENT_LIST_DIR}/HSFTEMPLATEConfig.cmake.in
  "${PROJECT_BINARY_DIR}/HSFTEMPLATEConfig.cmake"
  INSTALL_DESTINATION "${CMAKE_INSTALL_LIBDIR}/cmake/HSFTEMPLATE"
  PATH_VARS
    CMAKE_INSTALL_BINDIR
    CMAKE_INSTALL_INCLUDEDIR
    CMAKE_INSTALL_LIBDIR
  )

# - install and export
install(FILES
  "${PROJECT_BINARY_DIR}/HSFTEMPLATEConfigVersion.cmake"
  "${PROJECT_BINARY_DIR}/HSFTEMPLATEConfig.cmake"
  DESTINATION "${CMAKE_INSTALL_LIBDIR}/cmake/HSFTEMPLATE"
  )
install(EXPORT HSFTEMPLATETargets
  NAMESPACE HSFTEMPLATE::
  DESTINATION "${CMAKE_INSTALL_LIBDIR}/cmake/HSFTEMPLATE"
  )

#--- Pkg-Config File --------------------------------------------------
# - Derive relative pcfile -> prefix path to make pkg-config file
#   relocatable
file(RELATIVE_PATH HSFTEMPLATE_PCFILEDIR_TO_PREFIX
  "${CMAKE_INSTALL_FULL_LIBDIR}/pkgconfig"
  "${CMAKE_INSTALL_PREFIX}"
  )
configure_file("${CMAKE_CURRENT_LIST_DIR}/HSFTEMPLATE.pc.in"
  "${PROJECT_BINARY_DIR}/HSFTEMPLATE.pc"
  @ONLY
  )
install(FILES "${PROJECT_BINARY_DIR}/HSFTEMPLATE.pc"
  DESTINATION "${CMAKE_INSTALL_LIBDIR}/pkgconfig"
  )

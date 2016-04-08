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


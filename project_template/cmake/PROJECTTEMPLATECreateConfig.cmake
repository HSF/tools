# - Use CMake's module to help generating relocatable config files
include(CMakePackageConfigHelpers)

# - Versioning
write_basic_package_version_file(
  ${CMAKE_CURRENT_BINARY_DIR}/PROJECTTEMPLATEConfigVersion.cmake
  VERSION ${PROJECTTEMPLATE_VERSION}
  COMPATIBILITY SameMajorVersion)

# - Install time config and target files
configure_package_config_file(${CMAKE_CURRENT_LIST_DIR}/PROJECTTEMPLATEConfig.cmake.in
  "${PROJECT_BINARY_DIR}/PROJECTTEMPLATEConfig.cmake"
  INSTALL_DESTINATION "${CMAKE_INSTALL_LIBDIR}/cmake/PROJECTTEMPLATE"
  PATH_VARS
    CMAKE_INSTALL_BINDIR
    CMAKE_INSTALL_INCLUDEDIR
    CMAKE_INSTALL_LIBDIR
  )

# - install and export
install(FILES
  "${PROJECT_BINARY_DIR}/PROJECTTEMPLATEConfigVersion.cmake"
  "${PROJECT_BINARY_DIR}/PROJECTTEMPLATEConfig.cmake"
  DESTINATION "${CMAKE_INSTALL_LIBDIR}/cmake/PROJECTTEMPLATE"
  )
install(EXPORT PROJECTTEMPLATETargets
  NAMESPACE PROJECTTEMPLATE::
  DESTINATION "${CMAKE_INSTALL_LIBDIR}/cmake/PROJECTTEMPLATE"
  )


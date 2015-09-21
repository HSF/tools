include(CMakePackageConfigHelpers)
configure_file(cmake/HSFTEMPLATEConfig.cmake.in "${PROJECT_BINARY_DIR}/HSFTEMPLATEConfig.cmake" @ONLY)
write_basic_package_version_file(${CMAKE_CURRENT_BINARY_DIR}/HSFTEMPLATEConfigVersion.cmake
                                 VERSION ${HSFTEMPLATE_VERSION}
                                 COMPATIBILITY SameMajorVersion )

install(FILES ${CMAKE_CURRENT_BINARY_DIR}/HSFTEMPLATEConfig.cmake
              ${CMAKE_CURRENT_BINARY_DIR}/HSFTEMPLATEConfigVersion.cmake
        DESTINATION ${CMAKE_INSTALL_PREFIX}/cmake )

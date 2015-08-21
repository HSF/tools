cmake_minimum_required(VERSION 2.8)

project(HSFTEMPLATE)
set( HSFTEMPLATE_VERSION_MAJOR 0 )
set( HSFTEMPLATE_VERSION_MINOR 1 )
set( HSFTEMPLATE_VERSION_PATCH 0 )
set( HSFTEMPLATE_VERSION "${HSFTEMPLATE_VERSION_MAJOR}.${HSFTEMPLATE_VERSION_MINOR}" )

set(CMAKE_BUILD_TYPE Release)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

#--- enable unit testing capabilities ------------------
include(CTest)

#--- subdirectories ------------------------------------
add_subdirectory(subpackage)

#--- target for Doxygen documentation ------------------
find_package(Doxygen)
if(DOXYGEN_FOUND)
  configure_file(${CMAKE_CURRENT_SOURCE_DIR}/doc/Doxyfile.in
                 ${CMAKE_CURRENT_BINARY_DIR}/Doxyfile @ONLY
                )
  add_custom_target(doc
  ${DOXYGEN_EXECUTABLE} ${CMAKE_CURRENT_BINARY_DIR}/Doxyfile
  WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
  COMMENT "Generating API documentation with Doxygen" VERBATIM
  )
  install( DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/doxygen DESTINATION doxygen OPTIONAL)
endif(DOXYGEN_FOUND)

#--- targets for CMake infrastructure ------------------
include(CMakePackageConfigHelpers)

configure_file(HSFTEMPLATEConfig.cmake.in "${PROJECT_BINARY_DIR}/HSFTEMPLATEConfig.cmake" @ONLY)
write_basic_package_version_file(${CMAKE_CURRENT_BINARY_DIR}/HSFTEMPLATEConfigVersion.cmake
                                 VERSION ${HSFTEMPLATE_VERSION}
                                 COMPATIBILITY SameMajorVersion )

install(FILES ${CMAKE_CURRENT_BINARY_DIR}/HSFTEMPLATEConfig.cmake
              ${CMAKE_CURRENT_BINARY_DIR}/HSFTEMPLATEConfigVersion.cmake
        DESTINATION ${CMAKE_INSTALL_PREFIX}/cmake )

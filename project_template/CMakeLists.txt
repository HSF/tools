cmake_minimum_required(VERSION 2.8)

project(HSFTEMPLATE)
set( HSFTEMPLATE_VERSION_MAJOR 0 )
set( HSFTEMPLATE_VERSION_MINOR 1 )
set( HSFTEMPLATE_VERSION_PATCH 0 )
set( HSFTEMPLATE_VERSION "${HSFTEMPLATE_VERSION_MAJOR}.${HSFTEMPLATE_VERSION_MINOR}" )

set(CMAKE_BUILD_TYPE Release)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

#--- Declare options -----------------------------------------------------------
option(HSFTEMPLATE_documentation "Whether or not to create doxygen doc target.")

#--- enable unit testing capabilities ------------------------------------------
include(CTest)

#--- enable CPack --------------------------------------------------------------
include(cmake/HSFTEMPLATECPack.cmake)

#--- target for Doxygen documentation ------------------------------------------
if(HSFTEMPLATE_documentation)
  include(cmake/HSFTEMPLATEDoxygen.cmake)
endif()

#--- add version files ---------------------------------------------------------
configure_file(${CMAKE_CURRENT_SOURCE_DIR}/HSFTEMPLATEVersion.h
               ${CMAKE_CURRENT_BINARY_DIR}/HSFTEMPLATEVersion.h )
install(FILES ${CMAKE_CURRENT_BINARY_DIR}/HSFTEMPLATEVersion.h
        DESTINATION ${CMAKE_INSTALL_PREFIX}/include/HSFTEMPLATE )

#--- add CMake infrastructure --------------------------------------------------
include(cmake/HSFTEMPLATECreateConfig.cmake)

#--- add license files ---------------------------------------------------------
install(FILES ${CMAKE_CURRENT_SOURCE_DIR}/LICENSE
              ${CMAKE_CURRENT_SOURCE_DIR}/NOTICE
        DESTINATION ${CMAKE_INSTALL_PREFIX})

#--- project specific subdirectories -------------------------------------------
add_subdirectory(HSFSUBPACKAGE)

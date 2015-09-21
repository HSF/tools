set(CPACK_PACKAGE_DESCRIPTION "HSFTEMPLATE Project")
set(CPACK_PACKAGE_DESCRIPTION_SUMMARY "HSFTEMPLATE Project")
set(CPACK_PACKAGE_VENDOR "HEP Software Foundation")
set(CPACK_PACKAGE_VERSION ${HSFTEMPLATE_VERSION})
set(CPACK_PACKAGE_VERSION_MAJOR ${HSFTEMPLATE_MAJOR_VERSION})
set(CPACK_PACKAGE_VERSION_MINOR ${HSFTEMPLATE_MINOR_VERSION})
set(CPACK_PACKAGE_VERSION_PATCH ${HSFTEMPLATE_PATCH_VERSION})

set(CPACK_PACKAGE_DESCRIPTION_FILE "${CMAKE_SOURCE_DIR}/README.md")
set(CPACK_RESOURCE_FILE_LICENSE "${CMAKE_SOURCE_DIR}/LICENSE")
set(CPACK_RESOURCE_FILE_README "${CMAKE_SOURCE_DIR}/README.md")

#--- source package settings ---------------------------------------------------
set(CPACK_SOURCE_IGNORE_FILES
    ${PROJECT_BINARY_DIR}
    "~$"
    "/.git/"
    "/\\\\\\\\.git/"
    "/#"
)
set(CPACK_SOURCE_STRIP_FILES "")

#--- translate buildtype -------------------------------------------------------
string( TOLOWER "${CMAKE_BUILD_TYPE}" buildtype_lower )
if(buildtype_lower STREQUAL "release")
  set(HSF_BUILDTYPE "opt")
elseif(buildtype_lower STREQUAL "debug")
  set(HSF_BUILDTYPE "dbg")
elseif(buildtype_lower STREQUAL "relwithbebinfo")
  set(HSF_BUILDTYPE "owd")
endif()


#--- use HSF platform name -----------------------------------------------------
execute_process(
  COMMAND hsf_get_platform.py --buildtype ${HSF_BUILDTYPE}
  OUTPUT_VARIABLE HSF_PLATFORM OUTPUT_STRIP_TRAILING_WHITESPACE)


set(CPACK_PACKAGE_RELOCATABLE True)
set(CPACK_PACKAGE_INSTALL_DIRECTORY "HSFTEMPLATE_${HSFTEMPLATE_VERSION}")
set(CPACK_PACKAGE_FILE_NAME "HSFTEMPLATE_${HSFTEMPLATE_VERSION}_${HSF_PLATFORM}")

include(CPack)

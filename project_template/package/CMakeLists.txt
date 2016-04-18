# List sources for target
# - Note that we include headers. CMake will resolve dependencies on headers
#   correctly, but they will not show up in IDEs like Xcode if they are not
#   listed in the files for a target
set(examplelibrary_SOURCES
  include/HSFTEMPLATE/Example.h
  src/Example.cpp
  )

## create a library target
add_library(examplelibrary SHARED ${examplelibrary_SOURCES})

# - Define its header interface when building and when installed
# (i.e. used by a third party)
target_include_directories(examplelibrary
  PUBLIC
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
    $<INSTALL_INTERFACE:${CMAKE_INSTALL_INCLUDEDIR}>
    )

## if needed, link against "someexternal"
## which has been included with find_package(someexternal)
#target_link_libraries(examplelibrary ${someexternal_LIBRARIES})

# - Install the example library into the install time library directory
# The EXPORT name is used so that we can "export" the target for
# use by client projects
install(TARGETS examplelibrary
  EXPORT HSFTEMPLATETargets
  DESTINATION ${CMAKE_INSTALL_LIBDIR}
  )

## install the headers
install(DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/include/HSFTEMPLATE
  DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}
  )

## handling of test executables
add_subdirectory(tests)

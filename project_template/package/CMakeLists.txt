## add include directory
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/include)

## select all source files
file(GLOB sources ${CMAKE_CURRENT_SOURCE_DIR}/src/*.cpp)

## create a library target
add_library(examplelibrary SHARED ${sources})

## if needed, link against "someexternal"
## which has been included with find_package(someexternal)
#target_link_libraries(examplelibrary ${someexternal_LIBRARIES})

## install the example library into lib/
install(TARGETS examplelibrary DESTINATION lib)

## install the headers
install(DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/include/HSFTEMPLATE DESTINATION include)

## handling of test executables
add_subdirectory(tests)

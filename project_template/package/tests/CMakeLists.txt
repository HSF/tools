# Find gtest or fail
# NOTE: GTest recommends that it be vendored into the project rather
# than used from the system!
find_package(GTest REQUIRED)

## handling of test executables
## here a generic example for creating one executable per .cpp is shown
file(GLOB tests RELATIVE ${CMAKE_CURRENT_SOURCE_DIR} *.cpp)
message(${tests})
foreach( sourcefile ${tests} )
  string( REPLACE ".cpp" "" name ${sourcefile} )
  add_executable( ${name} ${sourcefile} )
  target_link_libraries( ${name} examplelibrary  ${GTEST_LIBRARIES})
  add_test(NAME ${name} COMMAND ${name})
endforeach()

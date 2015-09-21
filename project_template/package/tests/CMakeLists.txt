find_package(GTest)

## handling of test executables
## here a generic example for creating one executable per .cpp is shown
file(GLOB tests RELATIVE ${CMAKE_CURRENT_SOURCE_DIR} *.cpp)
message(${tests})
foreach( sourcefile ${tests} )
  string( REPLACE ".cpp" "" name ${sourcefile} )
  add_executable( ${name} ${sourcefile} )
  target_link_libraries( ${name} examplelibrary  ${GTEST_LIBRARIES})
  install(TARGETS ${name} DESTINATION bin)
  add_test(NAME ${name} COMMAND ${name})
endforeach( sourcefile ${tests} )

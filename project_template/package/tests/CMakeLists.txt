# Find gtest or fail
# NOTE: GTest recommends that it be vendored into the project rather
# than used from the system!
find_package(GTest REQUIRED)

# - handling of test executables
# Here a generic example for creating an executable then defining it as a
# test to CTest
# 1. Create executable
add_executable(test_example test_example.cpp)

# 2. Link it to the librayr being tested, plus the unit test library(ies)
target_link_libraries(test_example examplelibrary ${GTEST_LIBRARIES})

# 3. Add the test program as a command to be run as a test
# Note: NAME is what will be shown in CTest, COMMAND is what will be run
#       CMake knows that text_example is a CMake target, and knows where
#       the resultant executable is. Things like PATH and so on do not need
#       to be set.
add_test(NAME testExampleClass COMMAND test_example)


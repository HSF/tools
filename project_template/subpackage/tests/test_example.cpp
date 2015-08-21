// gtest
#include "gtest/gtest.h"

// project specific include
#include "example/Example.h"

using namespace HSFTEMPLATE;

TEST(Example, DoesThings) {
  auto e = Example();
  EXPECT_EQ(0,e.get());

  e = Example(10);
  EXPECT_EQ(10,e.get());

  e.set(12);
  EXPECT_EQ(12,e.get());
}

int main(int argc, char **argv) {
  ::testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}

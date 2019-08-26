#include <gtest/gtest.h>
#include "counter.hpp"

TEST(counter_tests, canConstructWithDefaultArguements)
{
    Counter c = Counter();
    Counter c1 = Counter();
}

TEST(counter_tests, canConstruct)
{
    Counter c1 = Counter();
    Counter c2 = Counter(14);
    Counter c3 = Counter(0, 2);
    Counter c4 = Counter(10, 4);
}

TEST(counter_tests, canConstructWithOneDefaultArguement)
{
    Counter c = Counter(10);
    Counter c1 = Counter(5);
    Counter c2 = Counter(11);
}
TEST(counter_tests, canIncrementCount)
{
    Counter c = Counter();
    for(int i = 0; i < 100; ++i)
    {
        c.up();
    }

    EXPECT_GT(c.display(), 0);
}

TEST(counter_tests, doesNotDecrementCountIfNegative)
{
    Counter c = Counter(-10);
    for(int i = 0; i < 100; ++i)
    {
        c.down();
    }

    EXPECT_EQ(c.display(), -10);
}

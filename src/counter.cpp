#include "counter.hpp"

Counter::Counter(int new_count, int new_step)
:count(new_count), step(new_step)
{}

Counter::~Counter()
{}

void Counter::up()
{
    count += step;
}

void Counter::down()
{
    if(count > 0)
    {
        count -= step;
    }
}

void Counter::reset_count(int other_count)
{
    count = other_count;
}

void Counter::reset_step(int other_step)
{
    step = other_step;
}

int Counter::display()
{
    return count;
}

void Counter::operator ++()
{
	count++;
}

void Counter::operator --()
{
	count--;
}


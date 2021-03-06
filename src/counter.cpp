#include "counter.hpp"

Counter::Counter(int new_count, int new_step)
:count(new_count), step(new_step)
{}

Counter::~Counter()
{}

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
	count += step;
}

void Counter::operator --()
{
	count-= step;
}

void Counter::operator ++(int)
{
	count += step;
}

void Counter::operator --(int)
{
	count -= step;
}

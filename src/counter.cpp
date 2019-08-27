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

void Counter::reset_count()
{
    count = 0;
}

void Counter::reset_step(int reset_step)
{
    step = reset_step;
}

int Counter::display()
{
    return count;
}

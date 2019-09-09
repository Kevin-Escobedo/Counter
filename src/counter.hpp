class Counter
{
private:
    int count;
    int step;
public:
    Counter(int new_count = 0, int new_step = 1);
    ~Counter();
    void up();
    void down();
    int display();
    void reset_count(int other_count = 0);
    void reset_step(int other_step = 1);
    void operator ++();
    void operator --();
};

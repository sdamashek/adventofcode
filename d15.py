inp = """Disc #1 has 5 positions; at time=0, it is at position 2.
Disc #2 has 13 positions; at time=0, it is at position 7.
Disc #3 has 17 positions; at time=0, it is at position 10.
Disc #4 has 3 positions; at time=0, it is at position 2.
Disc #5 has 19 positions; at time=0, it is at position 9.
Disc #6 has 7 positions; at time=0, it is at position 0."""

time = 0
while True:
    if (time+2+1) % 5 == 0 and (time+7+2) % 13 == 0 and (time + 3 + 10) % 17 == 0 and (time + 4 + 2) % 3 == 0 and (time + 5 + 9) % 19 == 0 and (time + 6) % 7 == 0 and (time + 7) % 11 == 0:
        print(time)
        break
    time += 1

import time
import sys


def ft_progress(lst):
    toolbar_width = 20
    length = len(lst)
    temp = int(length / toolbar_width)
    start = time.time()
    cnt = 0
    for i in lst:
        eta = (time.time() - start) * (length / (i + 1) - 1)
        msg = "ETA: {:.2f}s [ {}%][{:<}] {}/{} | elapsed time {:.2f}s".format(
                eta, int((i + 1) / length * 100),
                "=" * cnt + ">" + " " * (toolbar_width - cnt),
                i + 1, length, time.time() - start)
        sys.stdout.write(msg)
        sys.stdout.flush()
        if i != length:
            sys.stdout.write('\b' * len(msg))
        if i % temp == 0:
            cnt += 1
        yield i
    sys.stdout.write("\n")

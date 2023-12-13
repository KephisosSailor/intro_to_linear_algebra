# p10 22
import matplotlib.pyplot as plt
import numpy as np

def main():
    u_x = [0, 3]
    u_y = [0, 1]
    v_x = [0, 1]
    v_y = [0, 3]
    w_x = [0, 2]
    w_y = [0, 4]

    plt.plot(u_x, u_y, v_x, v_y, w_x, w_y, marker = "o")

    plt.axis([0, 6, 0, 6])

    # scatter
    dot_x = []
    dot_y = []
    for a in np.arange(0, 1, 0.05):
        for b in np.arange(0, 1, 0.05):
            if (a + b) > 1:
                continue
            for c in np.arange(0, 1, 0.05):
                if (a + b + c) > 1:
                    continue
                dot_x.append(a * u_x[1] + b * v_x[1] + c * w_x[1])
                dot_y.append(a * u_y[1] + b * v_y[1] + c * w_y[1])

    plt.scatter(dot_x, dot_y, cmap="g", alpha=0.3)

    plt.show()

if __name__ == '__main__':
    main()
import numpy as np
import matplotlib.pyplot as plt


def generate_lorenz_key():

    # ==========================================================
    # LORENZ CHAOTIC KEY GENERATOR USING X, Y AND Z
    # ==========================================================

    # Standard Lorenz Parameters
    sigma = 10
    rho = 28
    beta = 8 / 3

    dt = 0.01
    iterations = 1000

    # ----------------------------------------------------------
    # User Input
    # ----------------------------------------------------------

    print("=" * 70)
    print("        LORENZ CHAOTIC KEY GENERATOR")
    print("     (Using X, Y and Z with XOR)")
    print("=" * 70)

    x = float(input("Enter Initial x : "))
    y = float(input("Enter Initial y : "))
    z = float(input("Enter Initial z : "))

    print("\nStandard Lorenz Parameters")
    print(f"Sigma = {sigma}")
    print(f"Rho   = {rho}")
    print(f"Beta  = {beta:.4f}")

    # ----------------------------------------------------------
    # Generate Lorenz Sequence
    # ----------------------------------------------------------

    X = []
    Y = []
    Z = []

    for i in range(iterations):

        dx = sigma * (y - x)
        dy = x * (rho - z) - y
        dz = x * y - beta * z

        x += dx * dt
        y += dy * dt
        z += dz * dt

        X.append(x)
        Y.append(y)
        Z.append(z)

    # ----------------------------------------------------------
    # Generate Binary Key
    # ----------------------------------------------------------

    binary_key = []

    print("\n")
    print("=" * 90)
    print("FIRST 20 GENERATED BITS")
    print("=" * 90)

    print("{:<5} {:<10} {:<10} {:<10} {:<8} {:<8} {:<8} {:<8}".format(
        "Itr", "Frac(X)", "Frac(Y)", "Frac(Z)",
        "BitX", "BitY", "BitZ", "Final"))

    for i in range(iterations):

        fx = abs(X[i]) % 1
        fy = abs(Y[i]) % 1
        fz = abs(Z[i]) % 1

        bit_x = 1 if fx > 0.5 else 0
        bit_y = 1 if fy > 0.5 else 0
        bit_z = 1 if fz > 0.5 else 0

        final_bit = bit_x ^ bit_y ^ bit_z

        binary_key.append(str(final_bit))

        if i < 20:

            print("{:<5} {:<10.4f} {:<10.4f} {:<10.4f} {:<8} {:<8} {:<8} {:<8}".format(
                i + 1,
                fx,
                fy,
                fz,
                bit_x,
                bit_y,
                bit_z,
                final_bit
            ))

    binary_key = "".join(binary_key)

    # ----------------------------------------------------------
    # Display Final Binary Key
    # ----------------------------------------------------------

    print("\n")
    print("=" * 70)
    print("FINAL CHAOTIC BINARY KEY")
    print("=" * 70)

    print(binary_key)

    print("\nKey Length :", len(binary_key), "bits")

    print("\nFirst 64 Bits")
    print(binary_key[:64])

    # ----------------------------------------------------------
    # Lorenz Time Series (Separate Subplots)
    # ----------------------------------------------------------

    fig, ax = plt.subplots(3, 1, figsize=(12, 8), sharex=True)

    ax[0].plot(X, color="blue")
    ax[0].set_title("Lorenz X(t)")
    ax[0].set_ylabel("X")
    ax[0].grid(True)

    ax[1].plot(Y, color="green")
    ax[1].set_title("Lorenz Y(t)")
    ax[1].set_ylabel("Y")
    ax[1].grid(True)

    ax[2].plot(Z, color="red")
    ax[2].set_title("Lorenz Z(t)")
    ax[2].set_xlabel("Iteration")
    ax[2].set_ylabel("Z")
    ax[2].grid(True)

    plt.tight_layout()
    plt.show()

    # ----------------------------------------------------------
    # Bifurcation Diagram
    # ----------------------------------------------------------

    rho_values = np.linspace(0, 50, 250)

    plt.figure(figsize=(10, 6))

    for rho in rho_values:

        x = 0.1
        y = 0.2
        z = 0.3

        z_points = []

        for i in range(2500):

            dx = sigma * (y - x)
            dy = x * (rho - z) - y
            dz = x * y - beta * z

            x += dx * dt
            y += dy * dt
            z += dz * dt

            if i > 2200:
                z_points.append(z)

        plt.plot([rho] * len(z_points),
                 z_points,
                 ',k',
                 alpha=0.25)

    plt.title("Lorenz Bifurcation Diagram")
    plt.xlabel("Control Parameter (ρ)")
    plt.ylabel("Steady-State Z")
    plt.grid(True)

    plt.show()

    # ----------------------------------------------------------
    # Return Generated Key
    # ----------------------------------------------------------

    return binary_key


# ==========================================================
# Execute only if lorenz.py is run directly
# ==========================================================

if __name__ == "__main__":
    generate_lorenz_key()
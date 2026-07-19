import random


def run_bb84(alice_bits):

    print("\n" + "=" * 90)
    print("                    BB84 QUANTUM KEY DISTRIBUTION")
    print("=" * 90)

    n = len(alice_bits)

    # --------------------------------------------------
    # Random Basis Generation
    # --------------------------------------------------

    alice_bases = [random.choice(['+', '×']) for _ in range(n)]
    bob_bases = [random.choice(['+', '×']) for _ in range(n)]

    # --------------------------------------------------
    # Bob Measures the Incoming Qubits
    # --------------------------------------------------

    bob_bits = []

    for i in range(n):

        # Same Basis → Correct Bit
        if alice_bases[i] == bob_bases[i]:
            bob_bits.append(alice_bits[i])

        # Different Basis → Random Measurement
        else:
            bob_bits.append(str(random.randint(0, 1)))

    # --------------------------------------------------
    # Sifting Process
    # --------------------------------------------------

    sifted_alice = []
    sifted_bob = []

    keep_count = 0
    discard_count = 0

    print("\n")
    print("=" * 100)
    print("SIFTING PROCESS")
    print("=" * 100)

    print("{:<10} {:<12} {:<14} {:<14} {:<12} {:<12}".format(
        "Position",
        "Alice Bit",
        "Alice Basis",
        "Bob Basis",
        "Bob Bit",
        "Status"
    ))

    print("-" * 100)

    for i in range(n):

        if alice_bases[i] == bob_bases[i]:

            status = "KEEP"

            sifted_alice.append(alice_bits[i])
            sifted_bob.append(bob_bits[i])

            keep_count += 1

        else:

            status = "DISCARD"

            discard_count += 1

        print("{:<10} {:<12} {:<14} {:<14} {:<12} {:<12}".format(
            i + 1,
            alice_bits[i],
            alice_bases[i],
            bob_bases[i],
            bob_bits[i],
            status
        ))

    sifted_alice = "".join(sifted_alice)
    sifted_bob = "".join(sifted_bob)

    # --------------------------------------------------
    # Final Result
    # --------------------------------------------------

    print("\n")
    print("=" * 100)
    print("FINAL RESULT AFTER SIFTING")
    print("=" * 100)

    print("\nOriginal Alice Key")
    print("-" * 100)
    print(alice_bits)

    print("\nSifted Alice Key")
    print("-" * 100)
    print(sifted_alice)

    print("\nSifted Bob Key")
    print("-" * 100)
    print(sifted_bob)

    print("\n")
    print("=" * 100)
    print("KEY STATISTICS")
    print("=" * 100)

    print(f"Original Length : {len(alice_bits)} bits")
    print(f"Sifted Length   : {len(sifted_alice)} bits")
    print(f"Discarded Bits  : {discard_count} bits")
    print(f"Kept Bits       : {keep_count} bits")

    print("\nKeys Match :", sifted_alice == sifted_bob)

    return {
        "alice_key": sifted_alice,
        "bob_key": sifted_bob,
        "original_length": len(alice_bits),
        "sifted_length": len(sifted_alice),
        "discarded_bits": discard_count,
        "kept_bits": keep_count
    }
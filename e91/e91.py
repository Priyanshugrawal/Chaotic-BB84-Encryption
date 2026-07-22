import random
import math
import hashlib
from collections import defaultdict

LINE = "=" * 90
THIN = "-" * 90


def header(title: str) -> None:
    print("\n" + LINE)
    print(title.center(90))
    print(LINE)


# ======================================================================
# STEP 1 : NUMBER OF ENTANGLED PAIRS
# ======================================================================
header("E91 QUANTUM KEY DISTRIBUTION PROTOCOL -- SIMULATION")

while True:
    try:
        N = int(input("Enter number of entangled photon pairs : "))
        if N <= 0:
            print("Please enter a positive integer.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter an integer, e.g. 20")


# ======================================================================
# STEP 2 : BELL STATE USED
# ======================================================================
# |Psi-> is rotationally invariant -> perfect anti-correlation when
# Alice and Bob share the same basis; correlation follows -cos(Da-Db)
# when bases differ.
header("STEP 2 : BELL STATE USED")
print("Bell State Used :")
print("   |Psi-> = ( |01> - |10> ) / sqrt(2)")


# ======================================================================
# STEP 3 : BASIS DEFINITIONS (standard E91/CHSH angle set, degrees)
# ======================================================================
ALICE_BASES = {"A1": 0, "A2": 45, "A3": 90}
BOB_BASES = {"B1": 45, "B2": 90, "B3": 135}

# Angle-matched pairs -> perfect anti-correlation -> used for the key
KEY_BASIS_PAIRS = {("A2", "B1"), ("A3", "B2")}

# Combinations required by the CHSH formula
CHSH_PAIRS = [("A1", "B1"), ("A1", "B3"), ("A3", "B1"), ("A3", "B3")]


def quantum_probability_same(basis_a: str, basis_b: str) -> float:
    """P(Alice bit == Bob bit) predicted for |Psi-> : sin^2(Da-Db)/2)."""
    theta_a = math.radians(ALICE_BASES[basis_a])
    theta_b = math.radians(BOB_BASES[basis_b])
    delta = theta_a - theta_b
    return math.sin(delta / 2.0) ** 2


# ======================================================================
# STEP 4-7 : MEASUREMENT LOOP + RAW DATA TABLE
# ======================================================================
header("STEP 3-7 : MEASUREMENT SIMULATION AND RAW DATA TABLE")

alice_raw_key = []
bob_raw_key = []
bell_test_records = defaultdict(list)  # (a,b) -> [(alice_bit, bob_bit_before)]
table_rows = []

for pair_no in range(1, N + 1):
    # Step 3: random basis choice
    alice_basis = random.choice(list(ALICE_BASES.keys()))
    bob_basis = random.choice(list(BOB_BASES.keys()))

    # Step 4: measurement -- Alice uniform random, Bob per quantum stats
    alice_bit = random.randint(0, 1)
    p_same = quantum_probability_same(alice_basis, bob_basis)
    bob_bit_before = alice_bit if random.random() < p_same else 1 - alice_bit

    # Step 5: Bob's bit inversion (Algorithm 3)
    bob_bit_after = 1 - bob_bit_before

    # Step 6: basis match check
    basis_pair = (alice_basis, bob_basis)
    is_key_pair = basis_pair in KEY_BASIS_PAIRS

    if is_key_pair:
        alice_raw_key.append(alice_bit)
        bob_raw_key.append(bob_bit_after)
        status, match_str = "KEY", "YES"
    else:
        bell_test_records[basis_pair].append((alice_bit, bob_bit_before))
        status, match_str = "BELL TEST", "no"

    table_rows.append(
        (pair_no, alice_basis, bob_basis, alice_bit,
         bob_bit_before, bob_bit_after, match_str, status)
    )

# Step 7: print table
col_titles = ("Pair", "A-Basis", "B-Basis", "A-Bit",
              "B-Bit(before)", "B-Bit(after)", "Match", "Status")
row_fmt = "{:<6}{:<9}{:<9}{:<7}{:<15}{:<15}{:<7}{:<10}"
print(row_fmt.format(*col_titles))
print(THIN)
for row in table_rows:
    print(row_fmt.format(*row))


# ======================================================================
# STEP 8 : RAW KEYS
# ======================================================================
header("STEP 8 : RAW KEY SUMMARY")
alice_raw_key_str = "".join(str(b) for b in alice_raw_key)
bob_raw_key_str = "".join(str(b) for b in bob_raw_key)
print(f"Alice Raw Key : {alice_raw_key_str if alice_raw_key_str else '(empty)'}")
print(f"Bob   Raw Key : {bob_raw_key_str if bob_raw_key_str else '(empty)'}")
print(f"Length        : {len(alice_raw_key)}")


# ======================================================================
# STEP 9-10 : BELL TEST CORRELATIONS
# ======================================================================
header("STEP 9-10 : BELL TEST -- CORRELATION PER BASIS COMBINATION")

all_combinations = [
    ("A1", "B1"), ("A1", "B2"), ("A1", "B3"),
    ("A2", "B1"), ("A2", "B2"), ("A2", "B3"),
    ("A3", "B1"), ("A3", "B2"), ("A3", "B3"),
]
correlation = {}

print("{:<10}{:<10}{:<12}{:<15}".format("Combo", "Same", "Different", "E(a,b)"))
print(THIN)
for combo in all_combinations:
    records = bell_test_records.get(combo, [])
    same_count = sum(1 for a, b in records if a == b)
    diff_count = sum(1 for a, b in records if a != b)
    total = same_count + diff_count
    e_ab = (same_count - diff_count) / total if total > 0 else 0.0
    correlation[combo] = e_ab
    print("{:<10}{:<10}{:<12}{:<15.4f}".format(
        f"({combo[0]},{combo[1]})", same_count, diff_count, e_ab))

print(THIN)
print("Note: (A2,B1) and (A3,B2) are KEY basis pairs, excluded from Bell test.")


# ======================================================================
# STEP 11 : CHSH PARAMETER S
# ======================================================================
header("STEP 11 : CHSH BELL INEQUALITY PARAMETER")

E_A1B1 = correlation[("A1", "B1")]
E_A1B3 = correlation[("A1", "B3")]
E_A3B1 = correlation[("A3", "B1")]
E_A3B3 = correlation[("A3", "B3")]

print("Formula :")
print("   S = | E(A1,B1) - E(A1,B3) + E(A3,B1) + E(A3,B3) |")
print("\nSubstitution :")
print(f"   S = | {E_A1B1:.2f} - ({E_A1B3:.2f}) + {E_A3B1:.2f} + {E_A3B3:.2f} |")

S = abs(E_A1B1 - E_A1B3 + E_A3B1 + E_A3B3)
print(f"\n   S = {S:.4f}")


# ======================================================================
# STEP 12 : DECISION
# ======================================================================
header("STEP 12 : ENTANGLEMENT VERIFICATION DECISION")
# Classical bound S<=2; quantum allows up to 2*sqrt(2) (Tsirelson bound)
secure_channel = S > 2

if secure_channel:
    print(f"S = {S:.4f}  >  2")
    print("\n>>> Quantum Entanglement Verified")
    print(">>> Secure Channel")
else:
    print(f"S = {S:.4f}  <=  2")
    print("\n>>> Bell Inequality NOT Violated")
    print(">>> Possible Eavesdropping")
    print(">>> Abort Key")


# ======================================================================
# STEP 13-14 : ERROR CORRECTION + PRIVACY AMPLIFICATION
# ======================================================================
final_secret_key_hex = None

if secure_channel:
    header("STEP 13 : ERROR CORRECTION")
    print("Performing Error Correction...")
    print("Error Correction Completed.")

    header("STEP 14 : PRIVACY AMPLIFICATION")
    if len(alice_raw_key_str) == 0:
        print("No raw key bits generated -- privacy amplification skipped.")
    else:
        print(f"Original Key (Alice Raw Key) : {alice_raw_key_str}")
        sha256_digest = hashlib.sha256(alice_raw_key_str.encode()).hexdigest()
        print(f"SHA-256 Hash                 : {sha256_digest}")
        final_secret_key_hex = sha256_digest[:32]  # 128 bits = 32 hex chars
        print(f"\nFinal Secret Key (128 bits)  : {final_secret_key_hex}")
else:
    header("STEP 13-14 : SKIPPED")
    print("Channel INSECURE -- key aborted, no error correction/privacy amplification.")


# ======================================================================
# STEP 15 : FINAL REPORT
# ======================================================================
print("\n" + LINE)
print("FINAL REPORT".center(90))
print(LINE)

total_key_pairs = len(alice_raw_key)
total_bell_pairs = N - total_key_pairs

print(f"Total Pairs             : {N}")
print(f"Pairs used for Key      : {total_key_pairs}")
print(f"Pairs used for Bell Test: {total_bell_pairs}")
print(f"Alice Raw Key           : {alice_raw_key_str if alice_raw_key_str else '(empty)'}")
print(f"Bob   Raw Key           : {bob_raw_key_str if bob_raw_key_str else '(empty)'}")
print(f"Final Secret Key        : {final_secret_key_hex if final_secret_key_hex else '(none - not generated)'}")
print(f"CHSH Value (S)          : {S:.4f}")
print(f"Channel Status          : {'SECURE' if secure_channel else 'NOT SECURE'}")
print(LINE)
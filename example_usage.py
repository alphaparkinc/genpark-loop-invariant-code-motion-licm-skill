from client import LoopInvariantCodeMotion

def main():
    print("=== Testing Loop-Invariant Code Motion (LICM) ===")
    licm = LoopInvariantCodeMotion()

    loop = [
        ("t1", "ADD", "width", "height"),
        ("i", "ADD", "i", 1),
        ("t2", "MUL", "t1", 4)
    ]
    outside = {"width", "height"}

    hoisted, rem = licm.hoist(loop, outside)
    print(f"Hoisted {len(hoisted)} instructions to loop preheader:")
    for h in hoisted:
        print("  [HOISTED]", h)
    print(f"Remaining {len(rem)} loop body instructions:")
    for r in rem:
        print("  [LOOP]", r)

    assert len(hoisted) == 2
    assert len(rem) == 1
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()

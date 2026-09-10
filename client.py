class LoopInvariantCodeMotion:
    """
    Loop-Invariant Code Motion (LICM).
    Identifies instructions in a loop whose operands are either constants or defined
    outside the loop, and hoists them to loop preheader.
    """
    def hoist(self, loop_body, outside_defs):
        invariant_instructions = []
        available_defs = set(outside_defs)

        changed = True
        remaining = list(loop_body)
        while changed:
            changed = False
            still_remaining = []
            for instr in remaining:
                dest, op, s1, s2 = instr
                s1_inv = isinstance(s1, int) or s1 in available_defs
                s2_inv = isinstance(s2, int) or s2 in available_defs
                if s1_inv and s2_inv:
                    invariant_instructions.append(instr)
                    available_defs.add(dest)
                    changed = True
                else:
                    still_remaining.append(instr)
            remaining = still_remaining

        return invariant_instructions, remaining

import re


def parse(data):
    rules, parts = data.split("\n\n")
    rules_dict = {}
    for line in rules.splitlines():
        line = line.split("{")
        workflow = line[0]
        rule_list = line[1].strip("}").split(",")
        rules_dict[workflow] = rule_list

    part_list = []
    for line in parts.splitlines():
        part = line.strip("\{\}").split(",")
        part_list.append(part)
    return rules_dict, part_list


def accepted(conds, workflow, rules_dict):
    if workflow == "R":
        return 0
    if workflow == "A":
        total = 1
        for mn, mx in conds.values():
            total *= mx - mn + 1
        return total

    total = 0
    for check in rules_dict[workflow]:
        if "<" in check or ">" in check:
            rule, new_workflow = check.split(":")
            var, value = re.split(">|<", rule)
            value = int(value)
            mn_old, mx_old = conds[var]

            if "<" in check:
                mn = mn_old
                mx = min(mx_old, value) - 1

                mn_else = mx + 1
                mx_else = mx_old
            else:
                mn = max(mn_old, value) + 1
                mx = mx_old

                mn_else = mn_old
                mx_else = mn - 1
            if mn <= mx:
                copy = dict(conds)
                copy[var] = (mn, mx)
                total += accepted(copy, new_workflow, rules_dict)
            if mn_else <= mx_else:
                conds = dict(conds)
                conds[var] = (mn_else, mx_else)
        else:
            total += accepted(conds, check, rules_dict)
    return total


def part1():
    with open("inputs/day19inp.txt", "r") as file:
        data = file.read()
    rules_dict, part_list = parse(data)
    total = 0
    x, m, a, s = 0, 0, 0, 0
    for part in part_list:
        init = "\n".join(part)
        d = {}
        exec(init, d)
        x, m, a, s = d["x"], d["m"], d["a"], d["s"]
        workflow = "in"
        while workflow != "A" and workflow != "R":
            for idx, check in enumerate(rules_dict[workflow]):
                if idx == len(rules_dict[workflow]) - 1:
                    workflow = check
                else:
                    rule, new_workflow = check.split(":")
                    if eval(rule):
                        workflow = new_workflow
                        break
        total += x + m + a + s if workflow == "A" else 0
    return total


def part2():
    with open("inputs/day19inp.txt", "r") as file:
        data = file.read()
    rules_dict, _ = parse(data)
    no_cond = {var: (1, 4000) for var in "xmas"}
    return accepted(no_cond, "in", rules_dict)


if __name__ == "__main__":
    print(part1())
    print(part2())

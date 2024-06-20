from dataclasses import dataclass
from itertools import product
from string import ascii_lowercase
from typing import Union, Optional


@dataclass
class Node:
    data: Union[int, str]
    left: Optional['Node'] = None
    right: Optional['Node'] = None

    @property
    def is_leaf(self):
        return self.left is None and self.right is None

    @property
    def is_constant(self):
        return self.is_leaf and isinstance(self.data, int)

    def evaluate_tree(self, subs: Optional[dict] = None):
        if self.is_leaf:
            if isinstance(self.data, int):
                return self.data
            return subs[self.data]

        left_parsed = self.left.evaluate_tree(subs)
        right_parsed = self.right.evaluate_tree(subs)
        if self.data == "+":
            return left_parsed + right_parsed
        elif self.data == "*":
            return left_parsed * right_parsed
        elif self.data == "/":
            if left_parsed * right_parsed < 0:
                return -(abs(left_parsed) // abs(right_parsed))
            return abs(left_parsed) // abs(right_parsed)
        else:
            return left_parsed % right_parsed

    def get_tree_symbols(self):
        if self.is_leaf:
            if isinstance(self.data, int):
                return set()
            return {self.data}

        return self.left.get_tree_symbols() | self.right.get_tree_symbols()

    def assign_node(self, other_node):
        self.data = other_node.data
        self.left = other_node.left
        self.right = other_node.right

    def assign_leaf(self, value):
        self.data = value
        self.left = self.right = None

    def copy(self):
        if self.is_leaf:
            return Node(self.data)

        return Node(self.data, self.left.copy(), self.right.copy())

    def simplify(self):
        # simplify the tree as much as possible
        if self.is_leaf:
            return

        self.left.simplify()
        self.right.simplify()

        if self.data == "+":
            if self.left.data == 0:
                self.assign_node(self.right)
            elif self.right.data == 0:
                self.assign_node(self.left)
            elif self.left.is_constant and self.right.is_constant:
                self.assign_leaf(self.left.data + self.right.data)
            elif self.left.is_constant and self.right.data == "+":
                if self.right.left.is_constant:
                    self.left.data += self.right.left.data
                    self.right.assign_node(self.right.right)
                elif self.right.right.is_constant:
                    self.left.data += self.right.right.data
                    self.right.assign_node(self.right.left)
            elif self.right.is_constant and self.left.data == "+":
                if self.left.left.is_constant:
                    self.right.data += self.left.left.data
                    self.left.assign_node(self.left.right)
                elif self.left.right.is_constant:
                    self.right.data += self.left.right.data
                    self.left.assign_node(self.left.left)

        elif self.data == "*":
            if self.left.data == 0 or self.right.data == 0:
                self.assign_leaf(0)
            elif self.left.data == 1:
                self.assign_node(self.right)
            elif self.right.data == 1:
                self.assign_node(self.left)

        elif self.data == "%":
            # we know that everything is taking mod 26
            if self.left.is_constant:
                self.assign_leaf(self.left.data % 26)
            elif self.left.data == "+":
                if self.left.left.data == "*" and (self.left.left.left.data == 26 or self.left.left.right.data == 26):
                    mn, mx = self.left.right.get_min_max()
                    if -26 < mn <= mx < 26:
                        self.assign_node(self.left.right)
                elif self.left.right.data == "*" and (self.left.right.left.data == 26 or self.left.right.right.data == 26):
                    mn, mx = self.left.left.get_min_max()
                    if -26 < mn <= mx < 26:
                        self.assign_node(self.left.left)
                else:
                    mn, mx = self.left.get_min_max()
                    if -26 < mn <= mx < 26:
                        self.assign_node(self.left)
            else:
                mn, mx = self.left.get_min_max()
                if -26 < mn <= mx < 26:
                    self.assign_node(self.left)

        else:
            # we know that we only divide by 26
            if self.is_constant:
                self.assign_leaf(self.left.data // 26)
            elif self.left.data == "+":
                if self.left.left.data == "*" and (self.left.left.left.data == 26 or self.left.left.right.data == 26):
                    mn, mx = self.left.right.get_min_max()
                    if -26 < mn <= mx < 26:
                        if self.left.left.left.data == 26:
                            self.assign_node(self.left.left.right)
                        else:
                            self.assign_node(self.left.left.left)
                elif self.left.right.data == "*" and (self.left.right.left.data == 26 or self.left.right.right.data == 26):
                    mn, mx = self.left.left.get_min_max()
                    if -26 < mn <= mx < 26:
                        if self.left.right.left.data == 26:
                            self.assign_node(self.left.right.right)
                        else:
                            self.assign_node(self.left.right.left)
                else:
                    mn, mx = self.left.get_min_max()
                    if -26 < mn <= mx < 26:
                        self.assign_leaf(0)
            else:
                mn, mx = self.left.get_min_max()
                if -26 < mn <= mx < 26:
                    self.assign_leaf(0)

    def get_min_max(self):
        # get minimal and maximal possible values of the tree
        if self.is_leaf:
            if self.is_constant:
                return self.data, self.data
            else:
                return 1, 9

        min_left, max_left = self.left.get_min_max()
        min_right, max_right = self.right.get_min_max()
        if self.data == "+":
            return min_left + min_right, max_left + max_right
        if self.data == "*":
            mn = min(min_left * min_right, min_left * max_right, max_left * min_right, max_left * max_right)
            mx = max(min_left * min_right, min_left * max_right, max_left * min_right, max_left * max_right)
            return mn, mx
        if self.data == "/":
            return min_left // self.right.data, max_left // self.right.data
        if self.data == "%":
            return min_left % self.right.data, max_left % self.right.data


def main(filename):
    instructions = []
    with open(filename) as input_file:
        for line in input_file:
            parts = line.strip().split()
            if parts[0] in ["mod", "div"]:
                if parts[0] == "div" and parts[2] == "1":
                    # dividing by one doesn't do anything
                    continue
                assert parts[2] == "26"
            instructions.append(tuple(parts))

    pool = [
        (
            (Node(0), Node(0), Node(0), Node(0)),  # initial values for w, x, y, z
            0,  # variable index (we will call the 14 variables a-n)
            (),  # conditions
        ),
    ]
    for inst in instructions:
        for values, *_ in pool:
            for val in values:
                val.simplify()

        target_index = "wxyz".index(inst[1])
        if inst[0] == "inp":
            pool = [
                (
                    values[:target_index] + (Node(ascii_lowercase[variable_index]),) + values[target_index + 1:],
                    variable_index + 1,
                    conditions,
                )
                for values, variable_index, conditions in pool
            ]
        else:
            if inst[0] == "eql":
                pool_tmp = []
                for values, variable_index, conditions in pool:
                    target_value = values[target_index]
                    if inst[2] in "wxyz":
                        other_index = "wxyz".index(inst[2])
                        other_value = values[other_index]
                    else:
                        other_value = Node(int(inst[2]))
                    free_symbols = target_value.get_tree_symbols() | other_value.get_tree_symbols()
                    if free_symbols:
                        free_symbols = sorted(free_symbols)
                        equal_count = 0
                        non_equal_count = 0
                        for symbol_values in product(range(1, 10), repeat=len(free_symbols)):
                            subs = dict(zip(free_symbols, symbol_values))

                            target_value_replaced = target_value.evaluate_tree(subs)
                            other_value_replaced = other_value.evaluate_tree(subs)
                            if target_value_replaced == other_value_replaced:
                                equal_count += 1
                            else:
                                non_equal_count += 1
                        if equal_count == 0:
                            assert non_equal_count != 0
                            pool_tmp.append(
                                (
                                    values[:target_index] + (Node(0),) + values[target_index + 1:],
                                    variable_index,
                                    conditions,
                                )
                            )
                        elif non_equal_count == 0:
                            pool_tmp.append(
                                (
                                    values[:target_index] + (Node(1),) + values[target_index + 1:],
                                    variable_index, conditions,
                                )
                            )
                        else:
                            # we should check whether any old condition and new condition contradict,
                            # but we find the solution without checking, so we skip the check.
                            pool_tmp.append(
                                (
                                    values[:target_index] + (Node(1),) + values[target_index + 1:],
                                    variable_index,
                                    conditions + ((target_value.copy(), "==", other_value.copy()),),
                                )
                            )
                            pool_tmp.append(
                                (
                                    values[:target_index] + (Node(0),) + values[target_index + 1:],
                                    variable_index,
                                    conditions + ((target_value.copy(), "!=", other_value.copy()),),
                                )
                            )
                    else:
                        target_value_replaced = target_value.evaluate_tree()
                        other_value_replaced = other_value.evaluate_tree()
                        new_value = int(target_value_replaced == other_value_replaced)
                        pool_tmp.append(
                            (
                                values[:target_index] + (Node(new_value),) + values[target_index + 1:],
                                variable_index,
                                conditions,
                            )
                        )
                pool = pool_tmp
            else:
                operation_symbol = {
                    "add": "+",
                    "mul": "*",
                    "div": "/",
                    "mod": "%",
                }[inst[0]]
                pool_tmp = []
                for values, variable_index, conditions in pool:
                    target_value = values[target_index].copy()
                    if inst[2] in "wxyz":
                        other_index = "wxyz".index(inst[2])
                        other_value = values[other_index].copy()
                    else:
                        other_value = Node(int(inst[2]))
                    new_value = Node(operation_symbol, target_value, other_value)
                    pool_tmp.append(
                        (
                            values[:target_index] + (new_value,) + values[target_index + 1:],
                            variable_index,
                            conditions,
                        )
                    )
                pool = pool_tmp

    result_part_1 = None
    result_part_2 = None
    for i, (values, _, conditions) in enumerate(pool):
        expr = values[-1]  # z expression
        expr.simplify()

        mn, mx = values[-1].get_min_max()
        if mn > 0 or mx < 0:
            # z cannot be zero
            continue

        assert expr.data == 0  # turns out that we only encounter the case where z is already zero
        min_sol = {}
        max_sol = {}
        for cond in conditions:
            assert cond[1] == "=="  # turns out we only encounter equality conditions
            condition_vars = cond[0].get_tree_symbols() | cond[2].get_tree_symbols()
            assert len(condition_vars) == 2  # turns out that only two variables are involved in each condition
            assert not condition_vars.intersection(min_sol)  # turns out that all conditions are indipendent
            condition_vars = sorted(condition_vars)
            found = False
            for a in range(9, 0, -1):
                if found:
                    break
                for b in range(1, 10):
                    subs = {condition_vars[0]: a, condition_vars[1]: b}
                    if cond[0].evaluate_tree(subs) == cond[2].evaluate_tree(subs):
                        max_sol.update(subs)
                        found = True
                        break
            found = False
            for a in range(1, 10):
                if found:
                    break
                for b in range(1, 10):
                    subs = {condition_vars[0]: a, condition_vars[1]: b}
                    if cond[0].evaluate_tree(subs) == cond[2].evaluate_tree(subs):
                        min_sol.update(subs)
                        found = True
                        break
        min_sol_int = int("".join(str(n) for v, n in sorted(min_sol.items())))
        max_sol_int = int("".join(str(n) for v, n in sorted(max_sol.items())))
        if result_part_1 is None or max_sol_int > result_part_1:
            result_part_1 = max_sol_int
        if result_part_2 is None or min_sol_int < result_part_2:
            result_part_2 = min_sol_int

    print(f"part 1: {result_part_1}")
    print(f"part 2: {result_part_2}")


if __name__ == "__main__":
    for input_filename in [
        "input.txt"
    ]:
        print(f"-- {input_filename} --")
        main(input_filename)

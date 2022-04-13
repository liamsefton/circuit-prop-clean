func_dict = {}
def prob_or(a, b):
    return a + b - a * b

def prob_and(a, b):
    return a * b

def prob_xor(a, b):
    return a - 2 * a * b + b 

def output_cell_one(pin_dict):
    return prob_or(prob_and(prob_and(pin_dict["A"], prob_xor((1 - pin_dict["B"]), (1 - prob_or(pin_dict["C"], (1 - pin_dict["D"]))))), prob_xor(prob_xor((1 - pin_dict["E"]), pin_dict["F"]), pin_dict["G"])), (1 - pin_dict["H"]))

func_dict["cell_one"] = output_cell_one

def output_cell_two(pin_dict):
    return prob_and(prob_and(prob_and(prob_and(prob_and(prob_and(prob_and(pin_dict["A"], pin_dict["B"]), pin_dict["C"]), pin_dict["D"]), pin_dict["E"]), pin_dict["F"]), pin_dict["G"]), pin_dict["H"])

func_dict["cell_two"] = output_cell_two

def output_cell_three(pin_dict):
    return prob_xor(prob_xor(prob_xor(prob_xor(prob_xor(prob_xor(prob_xor((1 - pin_dict["A"]), (1 - pin_dict["B"])), (1 - pin_dict["C"])), (1 - pin_dict["D"])), (1 - pin_dict["E"])), (1 - pin_dict["F"])), (1 - pin_dict["G"])), (1 - pin_dict["H"]))

func_dict["cell_three"] = output_cell_three


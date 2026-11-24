GREEN = "\033[38;2;34;197;94m"
RED = "\033[38;2;239;68;68m"
RESET = "\033[0m"
import shutil
class Alan:
    '''
        Alan (TUrIng) is the TUI manager, whose job is to display the bias and wieghts,
        for model improvment. 
    '''
    def __init__(self, init_bias, init_weights):
        self.init_bias = init_bias
        self.init_weights = init_weights.copy()
        self.models = {}

    def update_terminal(self, model_name, weights, bias):
        self.models[model_name] = (weights, bias)
        frames = []

        for model_name, (weights, bias) in self.models.items():
            header = f"{model_name}\n{'Parameter':<12}{'Initial':>12}{'Current':>12}{'Change':>12}"
            frame = f"{header}\n{self._build_weights(weights)}\n{self._build_bias(bias)}\n"
            frames.append(frame)

        joined_frame = "\n".join(frames)
        print(f"\033[H\033[J{joined_frame}", end="", flush=True)
        
    def display_results(self, correct, wrong):
        pass

    def _build_weights(self, weights) -> str:
        rows = []
        for i, weight in enumerate(weights):
            rows.append(self._build_row(f"Weight {i}", self.init_weights[i], weight))
        return "\n".join(rows)

    def _build_bias(self, bias):
        return self._build_row("Bias", self.init_bias, bias)

    def _build_row(self, name, initial, current):
        difference = current - initial
        color = RESET
        if difference > 0:
            color = GREEN
        elif difference < 0:
            color = RED
        return (
            f"{name:<12}{initial:>12.4f}{current:>12.4f}"
            f"{color}{difference:>+12.4f}{RESET}"
        )
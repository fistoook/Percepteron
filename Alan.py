GREEN = "\033[38;2;34;197;94m"
RED = "\033[38;2;239;68;68m"
RESET = "\033[0m"
import shutil
class Alan:
    def __init__(self, models):
        self.init_model_values = {}
        self.updating_model_values = {}

        self.initialize_dictionaries(models)

    def initialize_dictionaries(self, models):
        for model in models:
            name = model.get_name()

            self.init_model_values[name] = (
                model.get_input_weights().copy(), 
                model.get_bias()
            )
            
            self.updating_model_values[name] = (0,0)
        
    def update_terminal(self, model_name, weights, bias):
        self.updating_model_values[model_name] = (weights, bias)

        frames = []

        header = f"{model_name}\n{'Parameter':<12}{'Initial':>12}{'Current':>12}{'Change':>12}"
        frame = f"{header}\n{self._build_weights(model_name)}\n{self._build_bias(model_name)}\n"
        frames.append(frame)

        joined_frame = "\n".join(frames)
        print(f"\033[H\033[J{joined_frame}", end="", flush=True)

    def display_results(self, model_name, loss, accuracy):
        print(
            f"\n{'─' * 36}\n"
            f" {model_name} — results\n"
            f"{'─' * 36}\n"
            f"{'Accuracy':<18}{GREEN}{accuracy:>17.2%}{RESET}\n"
            f"{'Loss':<18}{RED}{loss:>18.4f}{RESET}\n"
            f"{'─' * 36}",
            flush=True
        )

    def _build_weights(self, model_name) -> str:
        weights = self.updating_model_values[model_name][0]
        init_weights = self.init_model_values[model_name][0]

        rows = []
        for i, weight in enumerate(weights):
            rows.append(self._build_row(f"Weight {i}", init_weights[i], weight))
            
        return "\n".join(rows)

    def _build_bias(self, model_name):
        bias = self.updating_model_values[model_name][1]
        init_bias = self.init_model_values[model_name][1]

        return self._build_row("Bias", init_bias, bias)

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
class EarlyStoppingHelper:
    def __init__(self, model, early_stopping_rounds):
        self.last_round = None
        self.model = model
        self.best_round = None
        self.best_loss = None
        self.best_state_dict = None
        self.early_stopping_rounds = early_stopping_rounds

    def step(self, loss):
        self.last_round = self.last_round + 1 if self.last_round is not None else 0
        if self.best_loss is None or loss < self.best_loss:
            self.best_loss = loss
            self.best_state_dict = self.model.state_dict().copy()
            self.best_round = self.last_round
        if self.last_round >= self.best_round + self.early_stopping_rounds:
            print("Early stopping")
            print(f"Best loss: {self.best_loss} at round {self.best_round}")
            self.model.load_state_dict(self.best_state_dict)
            return True
        else:
            return False

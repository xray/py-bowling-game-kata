STRIKE_VALUE = 10
SPARE_VALUE = 10

class Score:
    def __init__(self):
        self.score = 0

    def calculate(self, score_card):
        for _ in range(10):
            if self.is_strike(score_card[0]):
                self.score += STRIKE_VALUE + score_card[1] + score_card[2]
                self.remove_values(score_card, 1)

            elif self.is_spare(score_card[0], score_card[1]):
                self.score += SPARE_VALUE + score_card[2]
                self.remove_values(score_card, 2)

            else:
                self.score += score_card[0] + score_card[1]
                self.remove_values(score_card, 2)

        return self.score

    def is_strike(self, value):
        return value == 10

    def is_spare(self, value1, value2):
        return value1 + value2 == 10

    def remove_values(self, score_card, number_of_values):
        for _ in range(number_of_values):
            score_card.pop(0)

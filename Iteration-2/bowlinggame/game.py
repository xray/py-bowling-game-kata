class Score:
    def __init__(self):
        self.score = 0

    def calculate(self, score_card):
        for _ in range(10):
            print(score_card)
            if score_card[0] == 10:
                self.score += score_card[0] + score_card[1] + score_card[2]
                score_card.pop(0)

            elif score_card[0] + score_card[1] == 10:
                self.score += score_card[0] + score_card[1] + score_card[2]
                score_card.pop(0)
                score_card.pop(0)

            else:
                self.score += score_card[0] + score_card[1]
                score_card.pop(0)
                score_card.pop(0)

        return self.score

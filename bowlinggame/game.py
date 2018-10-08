ROLL_ONE = 0
ROLL_TWO = 1
ROLL_THREE = 2
STRIKE = 10


class Score:
    def __init__(self):
        self.score = 0

    def get_roll_total(self, frame_rolls):
        roll_total = 0
        for roll_index, rolls in enumerate(frame_rolls):
            roll_total += frame_rolls[roll_index]
        return roll_total

    def get_strike_additional_points(self, game, frame_number, next_frame):
        if next_frame[ROLL_ONE] == 10:
            if frame_number == 8:
                return 10 + next_frame[ROLL_TWO]
            else:
                frame_after_next = game[frame_number + 2]
                return 10 + frame_after_next[ROLL_ONE]
        else:
            return next_frame[ROLL_ONE] + next_frame[ROLL_TWO]

    def check_if_strike_or_spare(self, game, frame, frame_number):
        if frame[ROLL_ONE] == STRIKE:
            return self.get_strike_additional_points(game, frame_number, game[frame_number + 1])
        else:
            next_frame = game[frame_number + 1]
            return next_frame[ROLL_ONE]

    def score_frame(self, full_game, current_frame_number):
        frame = full_game[current_frame_number]

        if self.get_roll_total(frame) < 10:
            return self.get_roll_total(frame)
        elif current_frame_number == 9:
            return frame[ROLL_ONE] + frame[ROLL_TWO] + frame[ROLL_THREE]
        else:
            extra_points = self.check_if_strike_or_spare(full_game, frame, current_frame_number)
            return frame[ROLL_ONE] + frame[ROLL_TWO] + extra_points

    def calculate(self, game):
        for current_frame_number, current_frame_points in enumerate(game):
            self.score += self.score_frame(game, current_frame_number)
        return self.score

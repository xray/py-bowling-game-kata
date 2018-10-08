from bowlinggame.game import Score


def gen_all_x_except_y_frame(number_to_set, frame_to_change, arr=[]):
    game = []
    for frame in range(10):
        if frame == (frame_to_change - 1):
            game.append(arr)
        else:
            if frame == 9:
                if number_to_set == 10:
                    game.append([number_to_set, number_to_set, number_to_set])
                else:
                    game.append([number_to_set, number_to_set, 0])
            elif number_to_set == 10:
                game.append([number_to_set, 0])
            else:
                game.append([number_to_set, number_to_set])
    return game


def test_gutter_game():
    new_score = Score()
    assert new_score.calculate(gen_all_x_except_y_frame(0, 0)) == 0


def test_all_ones_game():
    new_score = Score()
    assert new_score.calculate(gen_all_x_except_y_frame(1, 0)) == 20


def test_spare_in_frame_one_zeros():
    new_score = Score()
    assert new_score.calculate(gen_all_x_except_y_frame(0, 1, [1, 9])) == 10


def test_spare_in_frame_one_ones():
    new_score = Score()
    assert new_score.calculate(gen_all_x_except_y_frame(1, 1, [1, 9])) == 29


def test_strike_in_frame_one_ones():
    new_score = Score()
    assert new_score.calculate(gen_all_x_except_y_frame(1, 1, [10, 0])) == 30


def test_various_game():
    rolls = [[6, 3], [6, 4], [6, 2], [4, 6], [10, 0], [10, 0], [3, 2], [5, 5], [4, 3], [3, 1, 0]]
    new_score = Score()
    assert new_score.calculate(rolls) == 121


def test_all_strikes_except_last_frame():
    new_score = Score()
    assert new_score.calculate(gen_all_x_except_y_frame(10, 10, [0, 0, 0])) == 240


def test_last_frame_spare():
    new_score = Score()
    assert new_score.calculate(gen_all_x_except_y_frame(0, 10, [9, 1, 9])) == 19


def test_last_frame_strikes():
    new_score = Score()
    assert new_score.calculate(gen_all_x_except_y_frame(0, 10, [10, 10, 10])) == 30


def test_all_strikes():
    new_score = Score()
    assert new_score.calculate(gen_all_x_except_y_frame(10, 10, [10, 10, 10])) == 300

from bowlinggame.game import Score


def test_gutter_game():
    new_score = Score()
    score_card = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert new_score.calculate(score_card) == 0


def test_frame_total_nine_or_under():
    new_score = Score()
    score_card = [4, 2, 5, 3, 1, 6, 7, 1, 8, 1, 4, 5, 9, 0, 5, 3, 6, 3, 1, 3]
    assert new_score.calculate(score_card) == 77


def test_spare_in_first_frame_five_in_second():
    new_score = Score()
    score_card = [9, 1, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert new_score.calculate(score_card) == 20


def test_strike_in_first_frame_five_and_two_in_second():
    new_score = Score()
    score_card = [10, 5, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert new_score.calculate(score_card) == 24


def test_perfect_game():
    new_score = Score()
    score_card = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    assert new_score.calculate(score_card) == 300


def test_typical_game():
    new_score = Score()
    score_card = [6, 3, 6, 4, 6, 2, 4, 6, 10, 10, 3, 2, 5, 5, 4, 3, 3, 1]
    assert new_score.calculate(score_card) == 121

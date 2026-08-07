from scoring import calculate_score, classify_lead


def run_tests():
    score = calculate_score(
        budget=2500,
        timeline="ASAP",
        decision_maker="yes"
    )

    assert score == 10
    assert classify_lead(score) == "Hot"


    score = calculate_score(
        budget=1000,
        timeline="three months",
        decision_maker="unknown"
    )

    assert score == 6
    assert classify_lead(score) == "Warm"


    score = calculate_score(
        budget=0,
        timeline="sometime next year",
        decision_maker="no"
    )

    assert score == 2
    assert classify_lead(score) == "Cold"

    print("All scoring tests passed!")


run_tests()
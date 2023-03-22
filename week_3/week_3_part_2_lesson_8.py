expected_result = 11
actual_result = 15
def test_input_text(expected_result, actual_result):
    assert expected_result == actual_result, f"expected {expected_result}, got {actual_result}"

test_input_text(expected_result, actual_result)
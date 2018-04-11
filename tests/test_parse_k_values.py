from admixture_amigo import parse_k_values

def test_parse_k_values():
    result = parse_k_values('1,2')
    assert result == [1, 2]

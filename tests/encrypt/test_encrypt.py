import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("hagnarok", "7")

    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(159, 2)

    result = encrypt_message("hagnarok", 10)
    assert result == "korangah"

    result = encrypt_message("hagnarok", 5)
    assert result == "angah_kor"

    result = encrypt_message("hagnarok", 3)
    assert result == "gah_koran"

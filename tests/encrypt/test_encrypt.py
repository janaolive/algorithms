# from challenges.challenge_encrypt_message import encrypt_message
import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    assert encrypt_message('AABBCC', 3) == 'BAA_CCB'
    assert encrypt_message('ABBCCA', 4) == 'AC_CBBA'
    assert encrypt_message('AABBCC', -1) == 'CCBBAA'

    with pytest.raises(TypeError, match='tipo inválido para message'):
        encrypt_message(3, 3)

    with pytest.raises(TypeError) as encryptError:
        encrypt_message('AABBCC', 'a')
    assert encryptError.type is TypeError
    assert encryptError.value.args[0] == 'tipo inválido para key'

# Рассчитать хеш (h). Проверить, что хеш совпадает с рассчитанным командой crc32
from checkers import checkout, getout

dz_2 = "/home/user/Autotests/Home_Work_2/"


def test_7z_h():
    crc32_hash = getout(f'cd {dz_2}; crc32 checkers.py').upper()
    assert checkout(f'cd {dz_2}; 7z h checkers.py', crc32_hash), "test_h FAIL"
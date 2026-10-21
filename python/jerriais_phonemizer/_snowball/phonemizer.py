# Generated from jerriais-phonemizer.sbl by Snowball 3.1.1 - https://snowballstem.org/

from .basestemmer import BaseStemmer
from .among import Among


class Phonemizer(BaseStemmer):
    '''
    This class implements the stemming algorithm defined by a snowball script.
    Generated from jerriais-phonemizer.sbl by Snowball 3.1.1 - https://snowballstem.org/
    '''

    g_i_any = "iîï"
    g_y_any = "yŷ"
    g_soft_vowels = {"e", "i", "y", "è", "é", "ê", "ë", "î", "ï", "ŷ"}

    g_vowels = {"a", "e", "i", "o", "u", "y", "à", "â", "è", "é", "ê", "ë", "î", "ï", "ô", "ö", "ù", "û", "ü", "ŷ"}

    g_consonants = {"b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z", "ç"}

    g_vowels_without_y = {"a", "e", "i", "o", "u", "à", "â", "è", "é", "ê", "ë", "î", "ï", "ô", "ö", "ù", "û", "ü"}

    g_accepted_characters = {" ", "'", "-", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "à", "â", "ç", "è", "é", "ê", "ë", "î", "ï", "ô", "ö", "ù", "û", "ü", "ŷ"}

    g_ipa_consonants = {"b", "d", "f", "h", "k", "l", "m", "n", "p", "r", "s", "t", "v", "z", "ð", "ɡ", "ɲ", "ʃ", "ʒ"}

    g_ipa_oral_vowels = {"a", "e", "i", "j", "o", "u", "w", "y", "œ", "ɑ", "ɔ", "ɛ", "ɪ"}

    g_ipa_nasal_vowels = {"e", "o", "ø", "ɑ", "ɔ", "ɛ", "̃"}

    g_ipa_vowels = {"a", "e", "i", "j", "o", "u", "w", "y", "ø", "œ", "ɑ", "ɔ", "ɛ", "ɪ", "ː", "̃"}

    S_separator = ""
    B_must_liaise = False
    B_may_liaise = False

    def __r_liaison(self):
        self.bra = self.cursor
        among_var = self.find_among(Phonemizer.a_0)
        if among_var == 0:
            return False
        self.ket = self.cursor
        if self.cursor < self.limit:
            return False
        self.slice_from(Phonemizer.as_0[among_var - 1])
        return True

    def __r_liaison_set_phrases(self):
        self.bra = self.cursor
        among_var = self.find_among(Phonemizer.a_1)
        if among_var == 0:
            return False
        self.ket = self.cursor
        self.slice_from(Phonemizer.as_1[among_var - 1])
        return True

    def __r_silent_nt(self):
        v_1 = self.cursor
        try:
            if self.B_must_liaise:
                raise lab0()
            self.limit_backward = self.cursor
            self.cursor = self.limit
            self.ket = self.cursor
            if not self.eq_s_b("nt"):
                raise lab0()
            self.bra = self.cursor
            if self.cursor <= self.limit_backward or self.current[self.cursor - 1] != "e":
                raise lab0()
            self.cursor -= 1
            v_2 = self.limit - self.cursor
            try:
                if self.find_among_b(Phonemizer.a_2) == 0:
                    raise lab1()
                if self.cursor > self.limit_backward:
                    raise lab1()
                raise lab0()
            except lab1: pass
            self.cursor = self.limit - v_2
            self.slice_del()
            self.cursor = self.limit_backward
        except lab0: pass
        self.cursor = v_1
        return True

    def __r_remove_h(self):
        while True:
            v_1 = self.cursor
            try:
                self.bra = self.cursor
                if not self.eq_s("hu"):
                    raise lab0()
                self.ket = self.cursor
                while True:
                    try:
                        if self.cursor == self.limit or self.current[self.cursor] != "e":
                            raise lab1()
                        self.cursor += 1
                        break
                    except lab1: pass
                    if self.cursor == self.limit or self.current[self.cursor] != "i":
                        raise lab0()
                    self.cursor += 1
                    break
                self.slice_from("w")
                break
            except lab0: pass
            self.cursor = v_1
            self.bra = self.cursor
            break
        if self.cursor == self.limit or self.current[self.cursor] != "h":
            return False
        self.cursor += 1
        self.ket = self.cursor
        self.slice_del()
        return True

    def __r_silent_h(self):
        v_1 = self.cursor
        self.bra = self.cursor
        if self.cursor == self.limit or self.current[self.cursor] != "h":
            return False
        self.cursor += 1
        self.ket = self.cursor
        self.cursor = v_1
        v_2 = self.cursor
        among_var = self.find_among(Phonemizer.a_3)
        if among_var == 0:
            return False
        if among_var == 1:
            if self.cursor < self.limit:
                return False
        self.cursor = v_2
        return True

    def __r_oralize(self):
        v_1 = self.cursor
        while True:
            try:
                if not self.in_grouping(Phonemizer.g_vowels):
                    raise lab0()
                break
            except lab0: pass
            if self.cursor == self.limit or self.current[self.cursor] != "'":
                return False
            self.cursor += 1
            break
        self.cursor = v_1
        return True

    def __r_not_double_consonant(self):
        v_1 = self.cursor
        if not self.in_grouping(Phonemizer.g_consonants):
            return False
        while True:
            try:
                if not self.in_grouping(Phonemizer.g_vowels):
                    raise lab0()
                break
            except lab0: pass
            try:
                if not self.eq_s("li"):
                    raise lab0()
                break
            except lab0: pass
            if not self.eq_s("ly"):
                return False
            break
        self.cursor = v_1
        v_2 = self.cursor
        try:
            v_3 = self.cursor
            if self.cursor == self.limit or self.current[self.cursor] != "x":
                raise lab0()
            self.cursor += 1
            self.cursor = v_3
            return False
        except lab0: pass
        self.cursor = v_2
        return True

    def __r_delete_silent_e(self):
        v_1 = self.cursor
        try:
            self.bra = self.cursor
            if self.cursor == self.limit or self.current[self.cursor] != "e":
                self.cursor = v_1
                raise lab0()
            self.cursor += 1
            self.ket = self.cursor
            v_2 = self.cursor
            while True:
                v_3 = self.cursor
                try:
                    if self.cursor == self.limit or self.current[self.cursor] != "o":
                        raise lab1()
                    self.cursor += 1
                    break
                except lab1: pass
                self.cursor = v_3
                try:
                    if self.cursor == self.limit or self.current[self.cursor] != "ô":
                        raise lab1()
                    self.cursor += 1
                    break
                except lab1: pass
                self.cursor = v_3
                try:
                    if self.cursor == self.limit or self.current[self.cursor] != "a":
                        raise lab1()
                    self.cursor += 1
                    break
                except lab1: pass
                self.cursor = v_3
                try:
                    if self.cursor == self.limit or self.current[self.cursor] != "â":
                        raise lab1()
                    self.cursor += 1
                    break
                except lab1: pass
                self.cursor = v_3
                try:
                    if not self.__r_not_double_consonant():
                        raise lab1()
                    break
                except lab1: pass
                self.cursor = v_3
                if not self.eq_s("fr"):
                    self.cursor = v_1
                    raise lab0()
                break
            self.cursor = v_2
            self.slice_del()
        except lab0: pass
        return True

    def __r_consonant_phoneme(self):
        self.bra = self.cursor
        among_var = self.find_among(Phonemizer.a_4)
        if among_var == 0:
            return False
        self.ket = self.cursor
        if among_var == 1:
            self.slice_from("b")
        elif among_var == 2:
            self.slice_from("s")
        elif among_var == 3:
            while True:
                v_1 = self.cursor
                try:
                    v_2 = self.cursor
                    if not self.in_grouping(Phonemizer.g_soft_vowels):
                        raise lab0()
                    self.cursor = v_2
                    self.slice_from("s")
                    self.__r_delete_silent_e()
                    break
                except lab0: pass
                self.cursor = v_1
                self.slice_from("k")
                break
        elif among_var == 4:
            while True:
                v_3 = self.cursor
                try:
                    v_4 = self.cursor
                    if not self.in_grouping(Phonemizer.g_soft_vowels):
                        raise lab0()
                    self.cursor = v_4
                    self.slice_from("ks")
                    self.__r_delete_silent_e()
                    break
                except lab0: pass
                self.cursor = v_3
                self.slice_from("k")
                break
        elif among_var == 5:
            self.slice_from("ss")
        elif among_var == 6:
            self.slice_from("ʃ")
        elif among_var == 7:
            self.slice_from("kr")
        elif among_var == 8:
            self.slice_from("d")
        elif among_var == 9:
            self.slice_from("ʤ")
        elif among_var == 10:
            self.slice_from("f")
        elif among_var == 11:
            while True:
                v_5 = self.cursor
                try:
                    v_6 = self.cursor
                    if not self.in_grouping(Phonemizer.g_soft_vowels):
                        raise lab0()
                    self.cursor = v_6
                    self.slice_from("ʒ")
                    self.__r_delete_silent_e()
                    break
                except lab0: pass
                self.cursor = v_5
                self.slice_from("ɡ")
                break
        elif among_var == 12:
            self.slice_from("ʒʒ")
            self.__r_delete_silent_e()
        elif among_var == 13:
            while True:
                v_7 = self.cursor
                try:
                    v_8 = self.cursor
                    while True:
                        try:
                            if not self.in_grouping(Phonemizer.g_soft_vowels):
                                raise lab1()
                            break
                        except lab1: pass
                        if self.cursor == self.limit or self.current[self.cursor] != "'":
                            raise lab0()
                        self.cursor += 1
                        break
                    self.cursor = v_8
                    self.slice_from("ɡ")
                    break
                except lab0: pass
                self.cursor = v_7
                self.slice_from("ɡy")
                break
        elif among_var == 14:
            self.slice_from("ɡ")
        elif among_var == 15:
            self.slice_from("ʒ")
        elif among_var == 16:
            self.slice_from("l")
        elif among_var == 17:
            self.slice_from("ll")
        elif among_var == 18:
            self.slice_from("ji")
        elif among_var == 19:
            self.slice_from("m")
        elif among_var == 20:
            self.slice_from("n")
        elif among_var == 21:
            self.slice_from("ɲ")
        elif among_var == 22:
            self.slice_from("p")
        elif among_var == 23:
            self.slice_from("k")
            self.__r_delete_silent_e()
        elif among_var == 24:
            self.slice_from("r")
        elif among_var == 25:
            while True:
                v_9 = self.cursor
                try:
                    v_10 = self.cursor
                    if not self.in_grouping(Phonemizer.g_vowels):
                        raise lab0()
                    self.cursor = v_10
                    v_11 = self.limit - self.cursor
                    if self.cursor <= self.limit_backward or self.current[self.cursor - 1] != "s":
                        raise lab0()
                    self.cursor -= 1
                    v_12 = self.limit - self.cursor
                    try:
                        if self.cursor <= self.limit_backward or self.current[self.cursor - 1] != "ː":
                            self.cursor = self.limit - v_12
                            raise lab1()
                        self.cursor -= 1
                    except lab1: pass
                    if not self.in_grouping_b(Phonemizer.g_ipa_oral_vowels):
                        raise lab0()
                    self.cursor = self.limit - v_11
                    self.slice_from("z")
                    break
                except lab0: pass
                self.cursor = v_9
                self.slice_from("s")
                break
        elif among_var == 26:
            while True:
                v_13 = self.cursor
                try:
                    v_14 = self.cursor
                    if not self.in_grouping(Phonemizer.g_soft_vowels):
                        raise lab0()
                    self.cursor = v_14
                    self.slice_from("s")
                    break
                except lab0: pass
                self.cursor = v_13
                self.slice_from("sk")
                break
        elif among_var == 27:
            self.slice_from("t")
        elif among_var == 28:
            self.slice_from("ʧ")
        elif among_var == 29:
            self.slice_from("ð")
        elif among_var == 30:
            self.slice_from("z")
        elif among_var == 31:
            self.slice_del()
        return True

    def __r_vowel_phoneme(self):
        self.bra = self.cursor
        among_var = self.find_among(Phonemizer.a_5)
        if among_var == 0:
            return False
        self.ket = self.cursor
        if among_var == 1:
            self.slice_from("a")
        elif among_var == 2:
            self.slice_from("ɛ")
        elif among_var == 3:
            self.slice_from("e")
        elif among_var == 4:
            while True:
                v_1 = self.cursor
                try:
                    v_2 = self.cursor
                    if not self.in_grouping(Phonemizer.g_vowels_without_y):
                        raise lab0()
                    self.cursor = v_2
                    v_3 = self.limit - self.cursor
                    if self.cursor <= self.limit_backward or self.current[self.cursor - 1] != "i":
                        raise lab0()
                    self.cursor -= 1
                    if not self.in_grouping_b(Phonemizer.g_ipa_consonants):
                        raise lab0()
                    self.cursor = self.limit - v_3
                    self.slice_from("j")
                    break
                except lab0: pass
                self.cursor = v_1
                self.slice_from("i")
                break
        elif among_var == 5:
            while True:
                v_4 = self.cursor
                try:
                    v_5 = self.cursor
                    if not self.in_grouping(Phonemizer.g_vowels_without_y):
                        raise lab0()
                    self.cursor = v_5
                    self.slice_from("j")
                    break
                except lab0: pass
                self.cursor = v_4
                self.slice_from("i")
                break
        elif among_var == 6:
            self.slice_from("ɔ")
        elif among_var == 7:
            self.slice_from("y")
        elif among_var == 8:
            self.slice_from("ɑː")
        elif among_var == 9:
            self.slice_from("eːi")
        elif among_var == 10:
            self.slice_from("iː")
        elif among_var == 11:
            self.slice_from("oːu")
        elif among_var == 12:
            self.slice_from("yː")
        elif among_var == 13:
            while True:
                v_6 = self.cursor
                try:
                    while True:
                        v_7 = self.cursor
                        try:
                            if self.cursor == self.limit or self.current[self.cursor] != "n":
                                raise lab1()
                            self.cursor += 1
                            self.ket = self.cursor
                            break
                        except lab1: pass
                        self.cursor = v_7
                        v_8 = self.cursor
                        if not self.__r_oralize():
                            raise lab0()
                        self.cursor = v_8
                        break
                    self.slice_from("an")
                    self.__r_delete_silent_e()
                    break
                except lab0: pass
                self.cursor = v_6
                self.slice_from("ɑ̃")
                break
        elif among_var == 14:
            while True:
                v_9 = self.cursor
                try:
                    while True:
                        v_10 = self.cursor
                        try:
                            if self.cursor == self.limit or self.current[self.cursor] != "n":
                                raise lab1()
                            self.cursor += 1
                            self.ket = self.cursor
                            break
                        except lab1: pass
                        self.cursor = v_10
                        v_11 = self.cursor
                        if not self.__r_oralize():
                            raise lab0()
                        self.cursor = v_11
                        break
                    self.slice_from("ɛn")
                    self.__r_delete_silent_e()
                    break
                except lab0: pass
                self.cursor = v_9
                self.slice_from("ɛ̃")
                break
        elif among_var == 15:
            while True:
                v_12 = self.cursor
                try:
                    v_13 = self.cursor
                    while True:
                        v_14 = self.cursor
                        try:
                            if not self.__r_oralize():
                                raise lab1()
                            break
                        except lab1: pass
                        self.cursor = v_14
                        if self.cursor == self.limit or self.current[self.cursor] != "r":
                            raise lab0()
                        self.cursor += 1
                        break
                    self.cursor = v_13
                    self.slice_from("ɑ̃t")
                    self.__r_delete_silent_e()
                    break
                except lab0: pass
                self.cursor = v_12
                self.slice_from("ɑ̃")
                break
        elif among_var == 16:
            self.slice_from("ɑ̃ʧ")
        elif among_var == 17:
            while True:
                v_15 = self.cursor
                try:
                    v_16 = self.cursor
                    if not self.__r_oralize():
                        raise lab0()
                    self.cursor = v_16
                    self.slice_from("ɑ̃n")
                    break
                except lab0: pass
                self.cursor = v_15
                self.slice_from("ɑ̃")
                break
        elif among_var == 18:
            self.slice_from("ɛn")
        elif among_var == 19:
            while True:
                v_17 = self.cursor
                try:
                    while True:
                        v_18 = self.cursor
                        try:
                            if self.cursor == self.limit or self.current[self.cursor] != "m":
                                raise lab1()
                            self.cursor += 1
                            self.ket = self.cursor
                            break
                        except lab1: pass
                        self.cursor = v_18
                        v_19 = self.cursor
                        if not self.__r_oralize():
                            raise lab0()
                        self.cursor = v_19
                        break
                    self.slice_from("ɛm")
                    break
                except lab0: pass
                self.cursor = v_17
                self.slice_from("ɑ̃")
                break
        elif among_var == 20:
            while True:
                v_20 = self.cursor
                try:
                    while True:
                        v_21 = self.cursor
                        try:
                            if self.cursor == self.limit or self.current[self.cursor] != "n":
                                raise lab1()
                            self.cursor += 1
                            self.ket = self.cursor
                            break
                        except lab1: pass
                        self.cursor = v_21
                        v_22 = self.cursor
                        if not self.__r_oralize():
                            raise lab0()
                        self.cursor = v_22
                        break
                    self.slice_from("ɪn")
                    self.__r_delete_silent_e()
                    break
                except lab0: pass
                self.cursor = v_20
                self.slice_from("ẽ")
                break
        elif among_var == 21:
            self.slice_from("ẽː")
        elif among_var == 22:
            while True:
                v_23 = self.cursor
                try:
                    while True:
                        v_24 = self.cursor
                        try:
                            if self.cursor == self.limit or self.current[self.cursor] != "n":
                                raise lab1()
                            self.cursor += 1
                            self.ket = self.cursor
                            break
                        except lab1: pass
                        self.cursor = v_24
                        v_25 = self.cursor
                        if not self.__r_oralize():
                            raise lab0()
                        self.cursor = v_25
                        break
                    self.slice_from("ɔn")
                    self.__r_delete_silent_e()
                    break
                except lab0: pass
                self.cursor = v_23
                self.slice_from("õ")
                v_26 = self.cursor
                try:
                    self.bra = self.cursor
                    if self.cursor == self.limit or self.current[self.cursor] != "h":
                        self.cursor = v_26
                        raise lab0()
                    self.cursor += 1
                    self.ket = self.cursor
                    self.slice_from("n")
                except lab0: pass
                break
        elif among_var == 23:
            self.slice_from("õː")
        elif among_var == 24:
            while True:
                v_27 = self.cursor
                try:
                    while True:
                        v_28 = self.cursor
                        try:
                            if self.cursor == self.limit or self.current[self.cursor] != "m":
                                raise lab1()
                            self.cursor += 1
                            self.ket = self.cursor
                            break
                        except lab1: pass
                        self.cursor = v_28
                        v_29 = self.cursor
                        if not self.__r_oralize():
                            raise lab0()
                        self.cursor = v_29
                        break
                    self.slice_from("ɔm")
                    break
                except lab0: pass
                self.cursor = v_27
                self.slice_from("õ")
                break
        elif among_var == 25:
            while True:
                v_30 = self.cursor
                try:
                    while True:
                        v_31 = self.cursor
                        try:
                            if self.cursor == self.limit or self.current[self.cursor] != "n":
                                raise lab1()
                            self.cursor += 1
                            self.ket = self.cursor
                            break
                        except lab1: pass
                        self.cursor = v_31
                        v_32 = self.cursor
                        if not self.__r_oralize():
                            raise lab0()
                        self.cursor = v_32
                        break
                    self.slice_from("yn")
                    break
                except lab0: pass
                self.cursor = v_30
                self.slice_from("ø̃")
                break
        elif among_var == 26:
            while True:
                v_33 = self.cursor
                try:
                    while True:
                        v_34 = self.cursor
                        try:
                            if self.cursor == self.limit or self.current[self.cursor] != "m":
                                raise lab1()
                            self.cursor += 1
                            self.ket = self.cursor
                            break
                        except lab1: pass
                        self.cursor = v_34
                        v_35 = self.cursor
                        if not self.__r_oralize():
                            raise lab0()
                        self.cursor = v_35
                        break
                    self.slice_from("ym")
                    break
                except lab0: pass
                self.cursor = v_33
                self.slice_from("ø̃")
                break
        elif among_var == 27:
            while True:
                v_36 = self.cursor
                try:
                    v_37 = self.cursor
                    while True:
                        try:
                            if not self.eq_s("th"):
                                raise lab1()
                            break
                        except lab1: pass
                        try:
                            if self.cursor == self.limit or self.current[self.cursor] != "m":
                                raise lab1()
                            self.cursor += 1
                            break
                        except lab1: pass
                        if not self.eq_s("ch"):
                            raise lab0()
                        break
                    self.cursor = v_37
                    self.slice_from("ɛ")
                    break
                except lab0: pass
                self.cursor = v_36
                self.slice_from("ei")
                break
        elif among_var == 28:
            self.slice_from("ou")
        elif among_var == 29:
            self.slice_from("ui")
        elif among_var == 30:
            self.slice_from("wœ")
        elif among_var == 31:
            self.slice_from("uiː")
        elif among_var == 32:
            self.slice_from("uẽː")
        elif among_var == 33:
            self.slice_from("ji")
        elif among_var == 34:
            self.slice_from("eːji")
        elif among_var == 35:
            self.slice_from("ɛː")
        elif among_var == 36:
            self.slice_from("œ")
        elif among_var == 37:
            self.slice_from("œː")
        elif among_var == 38:
            self.slice_from("uː")
        elif among_var == 39:
            while True:
                v_38 = self.cursor
                try:
                    v_39 = self.limit - self.cursor
                    while True:
                        try:
                            if not self.eq_s_b("ou"):
                                raise lab1()
                            break
                        except lab1: pass
                        if not self.eq_s_b("où"):
                            raise lab0()
                        break
                    while True:
                        try:
                            if self.cursor > self.limit_backward:
                                raise lab1()
                            break
                        except lab1: pass
                        try:
                            if not self.in_grouping_b(Phonemizer.g_ipa_consonants):
                                raise lab1()
                            break
                        except lab1: pass
                        v_40 = self.limit - self.cursor
                        try:
                            if self.cursor <= self.limit_backward or self.current[self.cursor - 1] != "ː":
                                self.cursor = self.limit - v_40
                                raise lab1()
                            self.cursor -= 1
                        except lab1: pass
                        if not self.in_grouping_b(Phonemizer.g_ipa_nasal_vowels):
                            raise lab0()
                        break
                    self.cursor = self.limit - v_39
                    v_41 = self.cursor
                    while True:
                        try:
                            if not self.in_grouping(Phonemizer.g_vowels):
                                raise lab1()
                            break
                        except lab1: pass
                        if self.cursor == self.limit or self.current[self.cursor] != "'":
                            raise lab0()
                        self.cursor += 1
                        break
                    self.cursor = v_41
                    self.slice_from("w")
                    break
                except lab0: pass
                self.cursor = v_38
                self.slice_from("u")
                break
        elif among_var == 40:
            while True:
                v_42 = self.cursor
                try:
                    v_43 = self.cursor
                    if not self.in_grouping(Phonemizer.g_vowels):
                        raise lab0()
                    self.cursor = v_43
                    self.slice_from("w")
                    break
                except lab0: pass
                self.cursor = v_42
                self.slice_from("u")
                break
        elif among_var == 41:
            self.slice_from("ɑːj")
            v_44 = self.cursor
            try:
                self.bra = self.cursor
                if not self.eq_s("'l"):
                    self.cursor = v_44
                    raise lab0()
                self.ket = self.cursor
                self.slice_from("j")
            except lab0: pass
        elif among_var == 42:
            self.slice_from("ɑl")
        elif among_var == 43:
            self.slice_from("ej")
        elif among_var == 44:
            self.slice_from("eːjj")
        elif among_var == 45:
            while True:
                v_45 = self.cursor
                try:
                    v_46 = self.limit - self.cursor
                    if not self.eq_s_b("ill"):
                        raise lab0()
                    v_47 = self.limit - self.cursor
                    try:
                        if self.cursor <= self.limit_backward or self.current[self.cursor - 1] != "ː":
                            self.cursor = self.limit - v_47
                            raise lab1()
                        self.cursor -= 1
                    except lab1: pass
                    if not self.in_grouping_b(Phonemizer.g_ipa_vowels):
                        raise lab0()
                    self.cursor = self.limit - v_46
                    self.slice_from("j")
                    break
                except lab0: pass
                self.cursor = v_45
                self.slice_from("ij")
                break
        else:
            while True:
                v_48 = self.cursor
                try:
                    v_49 = self.limit - self.cursor
                    if not self.eq_s_b("ill'"):
                        raise lab0()
                    v_50 = self.limit - self.cursor
                    try:
                        if self.cursor <= self.limit_backward or self.current[self.cursor - 1] != "ː":
                            self.cursor = self.limit - v_50
                            raise lab1()
                        self.cursor -= 1
                    except lab1: pass
                    if not self.in_grouping_b(Phonemizer.g_ipa_vowels):
                        raise lab0()
                    self.cursor = self.limit - v_49
                    self.slice_from("jj")
                    break
                except lab0: pass
                self.cursor = v_48
                self.slice_from("ijj")
                break
        return True

    def __r_word_final(self):
        self.bra = self.cursor
        among_var = self.find_among(Phonemizer.a_6)
        if among_var == 0:
            return False
        v_1 = self.cursor
        try:
            if self.cursor == self.limit or self.current[self.cursor] != "s":
                self.cursor = v_1
                raise lab0()
            self.cursor += 1
        except lab0: pass
        self.ket = self.cursor
        if self.cursor < self.limit:
            return False
        if among_var == 1:
            self.slice_from("e")
        elif among_var == 2:
            self.slice_from("ɛ̃")
        elif among_var == 3:
            self.slice_from("eːi")
        elif among_var == 4:
            self.slice_from("ɛ")
        elif among_var == 5:
            self.slice_from("ɛː")
        elif among_var == 6:
            self.slice_from("ou")
        elif among_var == 7:
            self.slice_from("oːu")
        elif among_var == 8:
            self.slice_from("jou")
        elif among_var == 9:
            self.slice_from("joːu")
        elif among_var == 10:
            self.slice_from("œː")
        elif among_var == 11:
            self.slice_from("œːz")
        elif among_var == 12:
            self.slice_from("eː")
        elif among_var == 13:
            self.slice_from("ei")
            v_2 = self.cursor
            try:
                if not self.B_must_liaise:
                    self.cursor = v_2
                    raise lab0()
                self.insert(self.cursor, self.cursor, "t")
            except lab0: pass
        elif among_var == 14:
            self.slice_from("ei")
        elif among_var == 15:
            self.slice_from("ejɛ̃")
        elif among_var == 16:
            self.slice_from("e")
            v_3 = self.cursor
            try:
                if not self.B_must_liaise:
                    self.cursor = v_3
                    raise lab0()
                self.insert(self.cursor, self.cursor, "z")
            except lab0: pass
        elif among_var == 17:
            self.slice_from("e")
            v_4 = self.cursor
            try:
                if not self.B_must_liaise:
                    self.cursor = v_4
                    raise lab0()
                self.insert(self.cursor, self.cursor, "t")
            except lab0: pass
        elif among_var == 18:
            if not self.B_must_liaise:
                return False
            self.slice_from("t")
        elif among_var == 19:
            self.slice_from("eje")
        elif among_var == 20:
            self.slice_from("ɛn")
        elif among_var == 21:
            while True:
                v_5 = self.cursor
                try:
                    v_6 = self.limit - self.cursor
                    while True:
                        try:
                            if not self.eq_s_b("ien"):
                                raise lab1()
                            break
                        except lab1: pass
                        if not self.eq_s_b("ïen"):
                            raise lab0()
                        break
                    if not self.in_grouping_b(Phonemizer.g_ipa_consonants):
                        raise lab0()
                    self.cursor = self.limit - v_6
                    self.slice_from("yɛ̃")
                    break
                except lab0: pass
                self.cursor = v_5
                self.slice_from("iɛ̃")
                break
        elif among_var == 22:
            while True:
                v_7 = self.cursor
                try:
                    v_8 = self.limit - self.cursor
                    while True:
                        try:
                            if not self.eq_s_b("ienne"):
                                raise lab1()
                            break
                        except lab1: pass
                        if not self.eq_s_b("ïenne"):
                            raise lab0()
                        break
                    if not self.in_grouping_b(Phonemizer.g_ipa_consonants):
                        raise lab0()
                    self.cursor = self.limit - v_8
                    self.slice_from("yɛn")
                    break
                except lab0: pass
                self.cursor = v_7
                self.slice_from("iɛn")
                break
        elif among_var == 23:
            self.slice_from("ɪn")
        elif among_var == 24:
            self.slice_from("iː")
        elif among_var == 25:
            self.slice_from("yː")
        elif among_var == 26:
            self.slice_from("iː")
            v_9 = self.cursor
            try:
                if not self.B_must_liaise:
                    self.cursor = v_9
                    raise lab0()
                self.insert(self.cursor, self.cursor, "z")
            except lab0: pass
        elif among_var == 27:
            self.slice_from("o")
        elif among_var == 28:
            self.slice_from("uː")
        elif among_var == 29:
            self.slice_from("i")
        elif among_var == 30:
            self.slice_del()
        elif among_var == 31:
            self.slice_from("ɡ")
        elif among_var == 32:
            self.slice_from("ɛne")
        elif among_var == 33:
            self.slice_from("mɑ̃")
        elif among_var == 34:
            self.slice_from("mɑ̃t")
        elif among_var == 35:
            self.slice_from("il")
        elif among_var == 36:
            self.slice_from("ɑːl")
        elif among_var == 37:
            self.slice_from("k")
        elif among_var == 38:
            self.slice_from("ʒ")
        elif among_var == 39:
            self.slice_from("ɑ̃")
        else:
            while True:
                try:
                    if not self.B_must_liaise:
                        raise lab0()
                    break
                except lab0: pass
                self.slice_del()
                break
        return True

    def __r_pre_word(self):
        self.bra = self.cursor
        among_var = self.find_among(Phonemizer.a_7)
        if among_var == 0:
            return False
        self.ket = self.cursor
        if among_var == 1:
            self.slice_from("ʒ")
        elif among_var == 2:
            self.slice_from("t")
        elif among_var == 3:
            self.slice_from("s")
        elif among_var == 4:
            self.slice_from("l")
        elif among_var == 5:
            self.slice_from("li")
        elif among_var == 6:
            self.slice_from("d")
        elif among_var == 7:
            self.slice_from("m")
        elif among_var == 8:
            self.slice_from("n")
        elif among_var == 9:
            self.slice_from("k")
        elif among_var == 10:
            while True:
                v_1 = self.cursor
                try:
                    v_2 = self.cursor
                    if not self.eq_s("ou"):
                        raise lab0()
                    if not self.in_grouping(Phonemizer.g_vowels):
                        raise lab0()
                    self.cursor = v_2
                    self.slice_from("t")
                    break
                except lab0: pass
                self.cursor = v_1
                self.slice_from("tw")
                break
        elif among_var == 11:
            self.slice_from("ʃ")
        else:
            self.slice_from("j")
        return True

    def __r_single_letter(self):
        self.bra = self.cursor
        among_var = self.find_among(Phonemizer.a_8)
        if among_var == 0:
            return False
        self.ket = self.cursor
        if self.cursor < self.limit:
            return False
        if among_var > 0:
            self.slice_from(Phonemizer.as_8[among_var - 1])
        return True

    def __r_exceptions(self):
        while True:
            v_1 = self.cursor
            try:
                while True:
                    try:
                        if not self.B_must_liaise:
                            raise lab1()
                        break
                    except lab1: pass
                    if not self.B_may_liaise:
                        raise lab0()
                    break
                if not self.__r_liaison():
                    raise lab0()
                break
            except lab0: pass
            self.cursor = v_1
            try:
                self.bra = self.cursor
                among_var = self.find_among(Phonemizer.a_9)
                if among_var == 0:
                    raise lab0()
                self.ket = self.cursor
                if self.cursor < self.limit:
                    raise lab0()
                self.slice_from(Phonemizer.as_9[among_var - 1])
                break
            except lab0: pass
            self.cursor = v_1
            self.bra = self.cursor
            among_var = self.find_among(Phonemizer.a_10)
            if among_var == 0:
                return False
            self.ket = self.cursor
            if among_var == 1:
                while True:
                    v_2 = self.cursor
                    try:
                        if self.cursor < self.limit:
                            raise lab0()
                        self.slice_from("ɡy")
                        break
                    except lab0: pass
                    self.cursor = v_2
                    self.slice_from("ɡyj")
                    break
            elif among_var == 2:
                v_3 = self.cursor
                try:
                    if self.cursor == self.limit or self.current[self.cursor] != "s":
                        self.cursor = v_3
                        raise lab0()
                    self.cursor += 1
                    self.ket = self.cursor
                except lab0: pass
                while True:
                    v_4 = self.cursor
                    try:
                        if self.cursor < self.limit:
                            raise lab0()
                        self.slice_from("vẽː")
                        break
                    except lab0: pass
                    self.cursor = v_4
                    self.slice_from("vẽːt")
                    break
            elif among_var == 3:
                self.slice_from("vil")
            elif among_var == 4:
                self.slice_from("mil")
            elif among_var == 5:
                self.slice_from("bibjotɛk")
            elif among_var == 6:
                self.slice_from("ipɔtɛk")
            elif among_var == 7:
                self.slice_from("eːizimɑ̃")
            elif among_var == 8:
                self.slice_from("sɛt")
            elif among_var == 9:
                self.slice_from("kɔr")
            elif among_var == 10:
                self.slice_from("jɛtɔ")
            elif among_var == 11:
                self.slice_from("biɡɛs")
            elif among_var == 12:
                self.slice_from("õɡɑ̃n")
            elif among_var == 13:
                self.slice_from("õɡɑ̃")
            elif among_var == 14:
                self.slice_from("ɡlis")
            elif among_var == 15:
                self.slice_from("ɡlin")
            elif among_var == 16:
                self.slice_from("ɡlyʒ")
            elif among_var == 17:
                self.slice_from("ʒneːi")
            elif among_var == 18:
                self.slice_from("ʒnu")
            elif among_var == 19:
                self.slice_from("ʒnwɔ")
            else:
                self.slice_from("ʒniʃ")
            break
        return True

    def __r_word_initial(self):
        v_1 = self.cursor
        try:
            if not self.__r_silent_h():
                self.cursor = v_1
                raise lab0()
            if not self.__r_remove_h():
                self.cursor = v_1
                raise lab0()
        except lab0: pass
        while True:
            v_2 = self.cursor
            try:
                self.bra = self.cursor
                if not self.eq_s("th"):
                    raise lab0()
                self.ket = self.cursor
                self.slice_from("t")
                break
            except lab0: pass
            self.cursor = v_2
            try:
                self.bra = self.cursor
                v_3 = self.cursor
                try:
                    if self.cursor == self.limit or self.current[self.cursor] != "l":
                        self.cursor = v_3
                        raise lab1()
                    self.cursor += 1
                except lab1: pass
                while True:
                    try:
                        if self.cursor == self.limit or self.current[self.cursor] != "y":
                            raise lab1()
                        self.cursor += 1
                        break
                    except lab1: pass
                    if self.cursor == self.limit or self.current[self.cursor] != "i":
                        raise lab0()
                    self.cursor += 1
                    break
                self.ket = self.cursor
                v_4 = self.cursor
                if not self.in_grouping(Phonemizer.g_vowels):
                    raise lab0()
                self.cursor = v_4
                self.slice_from("j")
                break
            except lab0: pass
            self.cursor = v_2
            self.bra = self.cursor
            while True:
                try:
                    if not self.eq_s("ex"):
                        raise lab0()
                    break
                except lab0: pass
                if not self.eq_s("x-"):
                    return False
                break
            v_5 = self.cursor
            try:
                if self.cursor == self.limit or self.current[self.cursor] != "c":
                    self.cursor = v_5
                    raise lab0()
                self.cursor += 1
                v_6 = self.cursor
                if not self.in_grouping(Phonemizer.g_soft_vowels):
                    self.cursor = v_5
                    raise lab0()
                self.cursor = v_6
            except lab0: pass
            self.ket = self.cursor
            self.slice_from("ɛks")
            break
        return True

    def __r_silent_l(self):
        while True:
            v_1 = self.cursor
            try:
                v_2 = self.cursor
                if self.find_among(Phonemizer.a_11) == 0:
                    raise lab0()
                if self.cursor == self.limit or self.current[self.cursor] != "l":
                    raise lab0()
                self.cursor += 1
                while True:
                    try:
                        if not self.in_grouping(Phonemizer.g_y_any):
                            raise lab1()
                        break
                    except lab1: pass
                    if not self.in_grouping(Phonemizer.g_i_any):
                        raise lab0()
                    break
                self.cursor = v_2
                if not self.__r_consonant_phoneme():
                    raise lab0()
                while True:
                    v_3 = self.cursor
                    try:
                        self.bra = self.cursor
                        if self.cursor == self.limit or self.current[self.cursor] != "l":
                            raise lab1()
                        self.cursor += 1
                        if not self.in_grouping(Phonemizer.g_y_any):
                            raise lab1()
                        v_4 = self.cursor
                        try:
                            if not self.in_grouping(Phonemizer.g_i_any):
                                self.cursor = v_4
                                raise lab2()
                        except lab2: pass
                        self.ket = self.cursor
                        self.slice_from("ji")
                        break
                    except lab1: pass
                    self.cursor = v_3
                    self.bra = self.cursor
                    if self.cursor == self.limit or self.current[self.cursor] != "l":
                        raise lab0()
                    self.cursor += 1
                    if not self.in_grouping(Phonemizer.g_i_any):
                        raise lab0()
                    self.ket = self.cursor
                    self.slice_from("j")
                    break
                break
            except lab0: pass
            self.cursor = v_1
            try:
                v_5 = self.cursor
                if not self.in_grouping(Phonemizer.g_consonants):
                    raise lab0()
                if not self.eq_s("l'ye"):
                    raise lab0()
                self.cursor = v_5
                if not self.__r_consonant_phoneme():
                    raise lab0()
                self.bra = self.cursor
                if not self.eq_s("l'ye"):
                    raise lab0()
                self.ket = self.cursor
                self.slice_from("j")
                break
            except lab0: pass
            self.cursor = v_1
            self.bra = self.cursor
            if not self.eq_s("'l"):
                return False
            while True:
                try:
                    if self.cursor == self.limit or self.current[self.cursor] != "y":
                        raise lab0()
                    self.cursor += 1
                    break
                except lab0: pass
                if self.cursor == self.limit or self.current[self.cursor] != "i":
                    return False
                self.cursor += 1
                break
            self.ket = self.cursor
            v_6 = self.cursor
            if not self.in_grouping(Phonemizer.g_vowels):
                return False
            self.cursor = v_6
            self.slice_from("j")
            break
        return True

    def __r_mid_word_exceptions(self):
        while True:
            v_1 = self.cursor
            try:
                if not self.__r_silent_l():
                    raise lab0()
                break
            except lab0: pass
            self.cursor = v_1
            self.bra = self.cursor
            among_var = self.find_among(Phonemizer.a_12)
            if among_var == 0:
                return False
            self.ket = self.cursor
            if among_var == 1:
                self.slice_from("tɑ̃")
            elif among_var == 2:
                self.slice_from("fɑ̃m")
            elif among_var == 3:
                self.slice_from("lm")
            elif among_var == 4:
                self.slice_from("sjõ")
            elif among_var == 5:
                self.slice_from("aks")
            elif among_var == 6:
                self.slice_from("ɔsk")
            elif among_var == 7:
                self.slice_from("bɑːk")
            elif among_var == 8:
                self.slice_from("huk")
            elif among_var == 9:
                self.slice_from("bɑːt")
            else:
                while True:
                    v_2 = self.cursor
                    try:
                        v_3 = self.cursor
                        if self.cursor == self.limit or self.current[self.cursor] != "i":
                            raise lab0()
                        self.cursor += 1
                        if not self.in_grouping(Phonemizer.g_vowels):
                            raise lab0()
                        self.cursor = v_3
                        if self.cursor == self.limit or self.current[self.cursor] != "i":
                            raise lab0()
                        self.cursor += 1
                        self.ket = self.cursor
                        self.slice_from("ʒj")
                        break
                    except lab0: pass
                    self.cursor = v_2
                    self.slice_from("ʒl")
                    break
            break
        return True

    def __r_exceptions_with_hyphens(self):
        v_1 = self.cursor
        try:
            while True:
                v_2 = self.cursor
                try:
                    while True:
                        v_3 = self.cursor
                        try:
                            self.bra = self.cursor
                            if not self.eq_s("-s"):
                                raise lab2()
                            while True:
                                try:
                                    if self.cursor == self.limit or self.current[self.cursor] != "-":
                                        raise lab3()
                                    self.cursor += 1
                                    break
                                except lab3: pass
                                if self.cursor == self.limit or self.current[self.cursor] != "'":
                                    raise lab2()
                                self.cursor += 1
                                break
                            self.ket = self.cursor
                            self.cursor = v_3
                            break
                        except lab2: pass
                        self.cursor = v_3
                        if self.cursor >= self.limit:
                            raise lab1()
                        self.cursor += 1
                    self.slice_from("ze-")
                    continue
                except lab1: pass
                self.cursor = v_2
                break
        except lab0: pass
        self.cursor = v_1
        while True:
            v_4 = self.cursor
            try:
                self.bra = self.cursor
                among_var = self.find_among(Phonemizer.a_13)
                if among_var == 0:
                    raise lab0()
                self.ket = self.cursor
                self.slice_from(Phonemizer.as_13[among_var - 1])
                break
            except lab0: pass
            self.cursor = v_4
            v_5 = self.cursor
            while True:
                v_7 = self.cursor
                try:
                    self.bra = self.cursor
                    among_var = self.find_among(Phonemizer.a_14)
                    if among_var == 0:
                        raise lab0()
                    self.ket = self.cursor
                    if self.cursor < self.limit:
                        raise lab0()
                    if among_var == 1:
                        self.slice_from("ti")
                    elif among_var == 2:
                        self.slice_from("tal")
                    elif among_var == 3:
                        self.slice_from("jœn")
                    elif among_var == 4:
                        self.slice_from("jœnjɛm")
                    elif among_var == 5:
                        while True:
                            v_8 = self.cursor
                            try:
                                while True:
                                    try:
                                        if not self.B_must_liaise:
                                            raise lab2()
                                        break
                                    except lab2: pass
                                    if not self.B_may_liaise:
                                        raise lab1()
                                    break
                                self.slice_from("tɑ̃n")
                                break
                            except lab1: pass
                            self.cursor = v_8
                            self.slice_from("tɑ̃")
                            break
                    elif among_var == 6:
                        self.B_must_liaise = True
                        self.slice_from("i")
                    elif among_var == 7:
                        self.B_must_liaise = True
                        self.slice_from("al")
                    elif among_var == 8:
                        while True:
                            v_9 = self.cursor
                            try:
                                while True:
                                    try:
                                        if not self.B_must_liaise:
                                            raise lab2()
                                        break
                                    except lab2: pass
                                    if not self.B_may_liaise:
                                        raise lab1()
                                    break
                                self.slice_from("uz")
                                break
                            except lab1: pass
                            self.cursor = v_9
                            self.slice_from("u")
                            break
                        self.B_must_liaise = True
                    elif among_var == 9:
                        while True:
                            v_10 = self.cursor
                            try:
                                while True:
                                    try:
                                        if not self.B_must_liaise:
                                            raise lab2()
                                        break
                                    except lab2: pass
                                    if not self.B_may_liaise:
                                        raise lab1()
                                    break
                                self.slice_from("woz")
                                break
                            except lab1: pass
                            self.cursor = v_10
                            self.slice_from("wo")
                            break
                        self.B_must_liaise = True
                    else:
                        while True:
                            v_11 = self.cursor
                            try:
                                while True:
                                    try:
                                        if not self.B_must_liaise:
                                            raise lab2()
                                        break
                                    except lab2: pass
                                    if not self.B_may_liaise:
                                        raise lab1()
                                    break
                                self.slice_from("ɑ̃n")
                                break
                            except lab1: pass
                            self.cursor = v_11
                            self.slice_from("ɑ̃")
                            break
                        self.B_must_liaise = True
                    self.cursor = v_7
                    break
                except lab0: pass
                self.cursor = v_7
                if self.cursor >= self.limit:
                    return False
                self.cursor += 1
            v_6 = self.limit - self.cursor
            self.limit = self.cursor
            self.cursor = v_5
            self.__r_phonemize_word_with_hyphens()
            self.limit += v_6
            self.B_must_liaise = False
            self.cursor = self.limit
            break
        return True

    def __r_phoneme(self):
        while True:
            v_1 = self.cursor
            try:
                if not self.__r_word_final():
                    raise lab0()
                break
            except lab0: pass
            self.cursor = v_1
            try:
                if not self.__r_mid_word_exceptions():
                    raise lab0()
                break
            except lab0: pass
            self.cursor = v_1
            try:
                if not self.__r_vowel_phoneme():
                    raise lab0()
                break
            except lab0: pass
            self.cursor = v_1
            if not self.__r_consonant_phoneme():
                return False
            break
        return True

    def __r_phonemize_word(self):
        while True:
            v_1 = self.cursor
            try:
                if not self.__r_single_letter():
                    raise lab0()
                break
            except lab0: pass
            self.cursor = v_1
            while True:
                v_2 = self.cursor
                try:
                    while True:
                        v_3 = self.cursor
                        try:
                            if not self.__r_exceptions():
                                raise lab1()
                            break
                        except lab1: pass
                        self.cursor = v_3
                        if not self.__r_pre_word():
                            raise lab0()
                        break
                    continue
                except lab0: pass
                self.cursor = v_2
                break
            self.__r_silent_nt()
            v_4 = self.cursor
            try:
                if not self.__r_word_initial():
                    self.cursor = v_4
                    raise lab0()
            except lab0: pass
            while True:
                v_5 = self.cursor
                try:
                    if not self.__r_phoneme():
                        raise lab0()
                    continue
                except lab0: pass
                self.cursor = v_5
                break
            break
        return True

    def __r_phonemize_word_with_hyphens(self):
        while True:
            v_1 = self.cursor
            try:
                if not self.__r_exceptions_with_hyphens():
                    raise lab0()
                break
            except lab0: pass
            self.cursor = v_1
            while True:
                v_2 = self.cursor
                try:
                    v_3 = self.cursor
                    while True:
                        try:
                            while True:
                                v_5 = self.cursor
                                try:
                                    if self.cursor == self.limit or self.current[self.cursor] != "-":
                                        raise lab2()
                                    self.cursor += 1
                                    self.cursor = v_5
                                    break
                                except lab2: pass
                                self.cursor = v_5
                                if self.cursor >= self.limit:
                                    raise lab1()
                                self.cursor += 1
                            break
                        except lab1: pass
                        self.cursor = self.limit
                        break
                    v_4 = self.limit - self.cursor
                    self.limit = self.cursor
                    self.cursor = v_3
                    self.__r_phonemize_word()
                    self.limit += v_4
                    while True:
                        v_6 = self.cursor
                        try:
                            self.bra = self.cursor
                            self.cursor = v_6
                            break
                        except lab1: pass
                        self.cursor = v_6
                        if self.cursor >= self.limit:
                            raise lab0()
                        self.cursor += 1
                    if self.cursor == self.limit or self.current[self.cursor] != "-":
                        raise lab0()
                    self.cursor += 1
                    self.ket = self.cursor
                    self.slice_from(" ")
                    continue
                except lab0: pass
                self.cursor = v_2
                break
            break
        return True

    def __r_word_end(self):
        while True:
            try:
                while True:
                    v_1 = self.cursor
                    try:
                        if self.cursor == self.limit or self.current[self.cursor] != " ":
                            raise lab1()
                        self.cursor += 1
                        self.cursor = v_1
                        break
                    except lab1: pass
                    self.cursor = v_1
                    if self.cursor >= self.limit:
                        raise lab0()
                    self.cursor += 1
                break
            except lab0: pass
            self.cursor = self.limit
            break
        return True

    def __r_test_liaison(self):
        self.B_may_liaise = False
        v_1 = self.cursor
        try:
            if self.cursor == self.limit or self.current[self.cursor] != " ":
                raise lab0()
            self.cursor += 1
            while True:
                try:
                    if not self.in_grouping(Phonemizer.g_vowels):
                        raise lab1()
                    break
                except lab1: pass
                v_2 = self.cursor
                self.__r_word_end()
                v_3 = self.limit - self.cursor
                self.limit = self.cursor
                self.cursor = v_2
                if not self.__r_silent_h():
                    self.limit += v_3
                    raise lab0()
                self.limit += v_3
                break
            self.B_may_liaise = True
        except lab0: pass
        self.cursor = v_1
        return True

    def set_separator(self):
        self.bra = self.cursor
        self.cursor = self.limit
        self.ket = self.cursor
        self.S_separator = self.slice_to()
        return True

    def phonemize(self):
        v_1 = self.cursor
        try:
            while True:
                v_2 = self.cursor
                try:
                    while True:
                        v_3 = self.cursor
                        try:
                            try:
                                if not self.in_grouping(Phonemizer.g_accepted_characters):
                                    raise lab3()
                                raise lab2()
                            except lab3: pass
                            self.cursor = v_3
                            break
                        except lab2: pass
                        self.cursor = v_3
                        if self.cursor >= self.limit:
                            raise lab1()
                        self.cursor += 1
                    self.bra = self.cursor
                    if self.cursor >= self.limit:
                        raise lab1()
                    self.cursor += 1
                    self.ket = self.cursor
                    self.slice_from(" ")
                    continue
                except lab1: pass
                self.cursor = v_2
                break
        except lab0: pass
        self.cursor = v_1
        try:
            v_4 = self.cursor
            try:
                self.bra = self.cursor
                if self.cursor == self.limit or self.current[self.cursor] != " ":
                    raise lab1()
                self.cursor += 1
                self.ket = self.cursor
                self.slice_del()
            except lab1: pass
            self.cursor = v_4
            v_5 = self.cursor
            try:
                while True:
                    v_6 = self.cursor
                    try:
                        while True:
                            try:
                                if self.cursor == self.limit or self.current[self.cursor] != " ":
                                    raise lab3()
                                self.cursor += 1
                                break
                            except lab3: pass
                            if self.cursor >= self.limit:
                                raise lab2()
                            self.cursor += 1
                        self.bra = self.cursor
                        while True:
                            v_7 = self.cursor
                            try:
                                v_8 = self.cursor
                                try:
                                    while True:
                                        try:
                                            if self.cursor == self.limit or self.current[self.cursor] != " ":
                                                raise lab5()
                                            self.cursor += 1
                                            break
                                        except lab5: pass
                                        if self.cursor == self.limit or self.current[self.cursor] != "-":
                                            raise lab4()
                                        self.cursor += 1
                                        break
                                    raise lab3()
                                except lab4: pass
                                self.cursor = v_8
                                self.cursor = v_7
                                break
                            except lab3: pass
                            self.cursor = v_7
                            if self.cursor >= self.limit:
                                raise lab2()
                            self.cursor += 1
                        self.ket = self.cursor
                        self.slice_del()
                        continue
                    except lab2: pass
                    self.cursor = v_6
                    break
            except lab1: pass
            self.cursor = v_5
            v_9 = self.cursor
            try:
                if self.cursor > (len(self.current) - 1):
                    raise lab1()
                self.cursor = (len(self.current) - 1)
                self.bra = self.cursor
                if self.cursor == self.limit or self.current[self.cursor] != " ":
                    raise lab1()
                self.cursor += 1
                self.ket = self.cursor
                self.slice_del()
            except lab1: pass
            self.cursor = v_9
        except lab0: pass
        v_10 = self.cursor
        try:
            while True:
                v_11 = self.cursor
                try:
                    v_12 = self.cursor
                    try:
                        if not self.__r_liaison_set_phrases():
                            self.cursor = v_12
                            raise lab2()
                    except lab2: pass
                    v_13 = self.cursor
                    self.__r_word_end()
                    self.__r_test_liaison()
                    v_14 = self.limit - self.cursor
                    self.limit = self.cursor
                    self.cursor = v_13
                    self.__r_phonemize_word_with_hyphens()
                    self.limit += v_14
                    while True:
                        try:
                            if self.cursor == self.limit or self.current[self.cursor] != " ":
                                raise lab2()
                            self.cursor += 1
                            break
                        except lab2: pass
                        if self.cursor >= self.limit:
                            raise lab1()
                        self.cursor += 1
                    continue
                except lab1: pass
                self.cursor = v_11
                break
        except lab0: pass
        self.cursor = v_10
        v_15 = BaseStemmer()
        v_15.copy_from(self)
        self.current = self.S_separator
        self.cursor = 0
        self.limit = len(self.current)
        v_15_f = True
        try:
            if len(self.current) <= 0:
                raise lab0()
            v_15_f = False
        except lab0: pass
        self.S_separator = self.current
        super().copy_from(v_15)
        if v_15_f:
            return False
        while True:
            v_16 = self.cursor
            try:
                if self.cursor >= self.limit:
                    raise lab0()
                self.cursor += 1
                if self.cursor >= self.limit:
                    raise lab0()
                while True:
                    v_17 = self.cursor
                    try:
                        if self.cursor == self.limit or self.current[self.cursor] != " ":
                            raise lab1()
                        self.cursor += 1
                        break
                    except lab1: pass
                    self.cursor = v_17
                    try:
                        v_18 = self.cursor
                        while True:
                            try:
                                if self.cursor == self.limit or self.current[self.cursor] != "ː":
                                    raise lab2()
                                self.cursor += 1
                                break
                            except lab2: pass
                            if self.cursor == self.limit or self.current[self.cursor] != "̃":
                                raise lab1()
                            self.cursor += 1
                            break
                        self.cursor = v_18
                        break
                    except lab1: pass
                    self.cursor = v_17
                    self.insert(self.cursor, self.cursor, self.S_separator)
                    break
                continue
            except lab0: pass
            self.cursor = v_16
            break
        return True

    a_0 = [
        Among("ch't", -1, 15),
        Among("ches", -1, 16),
        Among("des", -1, 4),
        Among("deux", -1, 17),
        Among("dgiêx", -1, 20),
        Among("en", -1, 5),
        Among("huit", -1, 23),
        Among("les", -1, 3),
        Among("lus", -1, 10),
        Among("mes", -1, 7),
        Among("neuf", -1, 24),
        Among("nos", -1, 11),
        Among("nouos", -1, 13),
        Among("ous", -1, 6),
        Among("sept", -1, 22),
        Among("ses", -1, 9),
        Among("siêx", -1, 19),
        Among("tes", -1, 8),
        Among("trais", -1, 18),
        Among("un", -1, 1),
        Among("vos", -1, 12),
        Among("vouos", -1, 14),
        Among("vîngt", -1, 21),
        Among("ès", -1, 2)
    ]
    as_0 = ("ø̃n", "ɛz", "lɛz", "dɛz", "ɑ̃n", "uz", "mɛz", "tɛz", "sɛz", "lyz", "noz", "voz", "nwoz", "vwoz", "ʃt", "ʃɛz", "dœz", "trez", "sjeːiz", "ʤieːiz", "vẽːt", "sɛt", "wit", "nœv")

    a_1 = [
        Among("ch'est en tchi", -1, 8),
        Among("d'mains en mains", -1, 6),
        Among("d'pus en pus", -1, 5),
        Among("d'temps en temps", -1, 3),
        Among("est avis", -1, 10),
        Among("m'est avis", -1, 9),
        Among("pus en pus", -1, 4),
        Among("pus à co", -1, 1),
        Among("temps en temps", -1, 2),
        Among("tout à fait", -1, 7)
    ]
    as_1 = ("pyz a ko", "tɑ̃z ɑ̃ tɑ̃", "dtɑ̃z ɑ̃ tɑ̃", "pyz ɑ̃ py", "dpyz ɑ̃ py", "dmɛ̃z ɑ̃ mɛ̃", "tut a fei", "ʃet ɑ̃ ʧi", "met avi", "et avi")

    a_2 = [
        Among("acc", -1, -1),
        Among("vînc", -1, -1),
        Among("innoc", -1, -1),
        Among("înnoc", -1, -1),
        Among("réc", -1, -1),
        Among("d", -1, -1),
        Among("ad", 5, -1),
        Among("accid", 5, -1),
        Among("încid", 5, -1),
        Among("résid", 5, -1),
        Among("présid", 9, -1),
        Among("vice-présid", 10, -1),
        Among("êvid", 5, -1),
        Among("tchiând", 5, -1),
        Among("ard", 5, -1),
        Among("prud", 5, -1),
        Among("împrud", 15, -1),
        Among("précéd", 5, -1),
        Among("ag", -1, -1),
        Among("îndig", -1, -1),
        Among("întellig", -1, -1),
        Among("contig", -1, -1),
        Among("néglyig", -1, -1),
        Among("arg", -1, -1),
        Among("vif-arg", 23, -1),
        Among("viv-arg", 23, -1),
        Among("urg", -1, -1),
        Among("sèrg", -1, -1),
        Among("rég", -1, -1),
        Among("entrég", 28, -1),
        Among("ch", -1, -1),
        Among("pouor-ch", 30, -1),
        Among("vînch", 30, -1),
        Among("înnoch", 30, -1),
        Among("path", -1, -1),
        Among("appath", 34, -1),
        Among("transpath", 34, -1),
        Among("contchuth", -1, -1),
        Among("difféth", -1, -1),
        Among("îndifféth", 38, -1),
        Among("dévthai", -1, -1),
        Among("pouôrrai", -1, -1),
        Among("pâci", -1, -1),
        Among("împâci", 42, -1),
        Among("cli", -1, -1),
        Among("înconvéni", -1, -1),
        Among("ori", -1, -1),
        Among("împâti", -1, -1),
        Among("l", -1, -1),
        Among("r'l", 48, -1),
        Among("tal", 48, -1),
        Among("êtchival", 48, -1),
        Among("excell", 48, -1),
        Among("êtchipoll", 48, -1),
        Among("dol", 48, -1),
        Among("îndol", 54, -1),
        Among("viol", 48, -1),
        Among("însol", 48, -1),
        Among("èrl", 48, -1),
        Among("opul", 48, -1),
        Among("l'opul", 59, -1),
        Among("grand'm", -1, -1),
        Among("sèl'm", -1, -1),
        Among("eunanînm'm", -1, -1),
        Among("légitînm'm", -1, -1),
        Among("anonŷnm'm", -1, -1),
        Among("alîngn'm", -1, -1),
        Among("envithonn'm", -1, -1),
        Among("l'envithonn'm", 67, -1),
        Among("touônn'm", -1, -1),
        Among("bénîn'm", -1, -1),
        Among("sup'm", -1, -1),
        Among("cliut'm", -1, -1),
        Among("assiqu'm", -1, -1),
        Among("trébuqu'm", -1, -1),
        Among("assèqu'm", -1, -1),
        Among("affêqu'm", -1, -1),
        Among("médicam", -1, -1),
        Among("prédicam", -1, -1),
        Among("testam", -1, -1),
        Among("rapacem", -1, -1),
        Among("propicem", -1, -1),
        Among("finnancem", -1, -1),
        Among("couaincem", -1, -1),
        Among("coincem", -1, -1),
        Among("innocem", -1, -1),
        Among("înnocem", -1, -1),
        Among("atrocem", -1, -1),
        Among("atchiêscem", -1, -1),
        Among("exaucem", -1, -1),
        Among("naïcem", -1, -1),
        Among("raidem", -1, -1),
        Among("solidem", -1, -1),
        Among("tînmidem", -1, -1),
        Among("rapidem", -1, -1),
        Among("stupidem", -1, -1),
        Among("întrépidem", -1, -1),
        Among("vividem", -1, -1),
        Among("c'mandem", -1, -1),
        Among("quémandem", -1, -1),
        Among("amendem", -1, -1),
        Among("fondem", -1, -1),
        Among("s'gondem", -1, -1),
        Among("rondem", -1, -1),
        Among("codem", -1, -1),
        Among("c'modem", -1, -1),
        Among("quémodem", -1, -1),
        Among("mal-quémodem", 106, -1),
        Among("couardem", -1, -1),
        Among("caudem", -1, -1),
        Among("rudem", -1, -1),
        Among("tchièdem", -1, -1),
        Among("vièdem", -1, -1),
        Among("êtouffem", -1, -1),
        Among("caûffem", -1, -1),
        Among("êcaûffem", 114, -1),
        Among("engagem", -1, -1),
        Among("dêgagem", -1, -1),
        Among("encouothagem", -1, -1),
        Among("dêcouothagem", -1, -1),
        Among("soulagem", -1, -1),
        Among("dêdommagem", -1, -1),
        Among("dêmênagem", -1, -1),
        Among("sagem", -1, -1),
        Among("néglyigem", -1, -1),
        Among("changem", -1, -1),
        Among("arrangem", -1, -1),
        Among("êtrangem", -1, -1),
        Among("dêrangem", -1, -1),
        Among("bouogem", -1, -1),
        Among("louogem", -1, -1),
        Among("largem", -1, -1),
        Among("jugem", -1, -1),
        Among("enâgem", -1, -1),
        Among("pliaichem", -1, -1),
        Among("empliaichem", 134, -1),
        Among("rempliaichem", 135, -1),
        Among("dêpliaichem", 134, -1),
        Among("rappraichem", -1, -1),
        Among("cichem", -1, -1),
        Among("richem", -1, -1),
        Among("ap'tichem", -1, -1),
        Among("clioutichem", -1, -1),
        Among("lanchem", -1, -1),
        Among("franchem", -1, -1),
        Among("tanchem", -1, -1),
        Among("avanchem", -1, -1),
        Among("c'menchem", -1, -1),
        Among("quémenchem", -1, -1),
        Among("r'quémenchem", 148, -1),
        Among("èrquémenchem", 148, -1),
        Among("pînchem", -1, -1),
        Among("grînchem", -1, -1),
        Among("accouochem", -1, -1),
        Among("douochem", -1, -1),
        Among("cauchem", -1, -1),
        Among("gauchem", -1, -1),
        Among("chuchem", -1, -1),
        Among("dêbouchem", -1, -1),
        Among("attouchem", -1, -1),
        Among("suchem", -1, -1),
        Among("rapièchem", -1, -1),
        Among("empêchem", -1, -1),
        Among("fraîchem", -1, -1),
        Among("vaûchem", -1, -1),
        Among("amathem", -1, -1),
        Among("suicidaithem", -1, -1),
        Among("s'gondaithem", -1, -1),
        Among("vuldgaithem", -1, -1),
        Among("téméthaithem", -1, -1),
        Among("cliaithem", -1, -1),
        Among("spectatchulaithem", -1, -1),
        Among("populaithem", -1, -1),
        Among("primaithem", -1, -1),
        Among("prînmaithem", -1, -1),
        Among("ordinnaithem", -1, -1),
        Among("extraordinnaithem", 175, -1),
        Among("prélînminnaithem", -1, -1),
        Among("provisionnaithem", -1, -1),
        Among("dêbouonnaithem", -1, -1),
        Among("honoraithem", -1, -1),
        Among("contraithem", -1, -1),
        Among("nécessaithem", -1, -1),
        Among("militaithem", -1, -1),
        Among("solitaithem", -1, -1),
        Among("mâjoritaithem", -1, -1),
        Among("boltaithem", -1, -1),
        Among("volantaithem", -1, -1),
        Among("învolontaithem", -1, -1),
        Among("provisouaithem", -1, -1),
        Among("oblyigatouaithem", -1, -1),
        Among("méthitouaithem", -1, -1),
        Among("dêchithem", -1, -1),
        Among("chavithem", -1, -1),
        Among("dêfidguthem", -1, -1),
        Among("juthem", -1, -1),
        Among("puthem", -1, -1),
        Among("suthem", -1, -1),
        Among("sîncéthem", -1, -1),
        Among("transféthem", -1, -1),
        Among("rapaciéthem", -1, -1),
        Among("fonciéthem", -1, -1),
        Among("mênagiéthem", -1, -1),
        Among("ligiéthem", -1, -1),
        Among("chiéthem", -1, -1),
        Among("carnachiéthem", 204, -1),
        Among("entchiéthem", 204, -1),
        Among("hospitaliéthem", -1, -1),
        Among("spectacliéthem", -1, -1),
        Among("fanmiliéthem", -1, -1),
        Among("sîndguliéthem", -1, -1),
        Among("rédguliéthem", -1, -1),
        Among("irrédguliéthem", 211, -1),
        Among("partitchuliéthem", -1, -1),
        Among("sétchuliéthem", -1, -1),
        Among("preunmiéthem", -1, -1),
        Among("manniéthem", -1, -1),
        Among("dèrniéthem", -1, -1),
        Among("rantcheuniéthem", -1, -1),
        Among("améthem", -1, -1),
        Among("prospéthem", -1, -1),
        Among("sévéthem", -1, -1),
        Among("seûthem", -1, -1),
        Among("laiem", -1, -1),
        Among("paiem", -1, -1),
        Among("graiem", -1, -1),
        Among("vraiem", -1, -1),
        Among("couaiem", -1, -1),
        Among("euniem", -1, -1),
        Among("priem", -1, -1),
        Among("aîsiem", -1, -1),
        Among("gliobalem", -1, -1),
        Among("globalem", -1, -1),
        Among("grammaticalem", -1, -1),
        Among("granmaticalem", -1, -1),
        Among("prodigalem", -1, -1),
        Among("légalem", -1, -1),
        Among("illégalem", 236, -1),
        Among("êgalem", -1, -1),
        Among("commèrcialem", -1, -1),
        Among("conmèrcialem", -1, -1),
        Among("spécialem", -1, -1),
        Among("espécialem", 241, -1),
        Among("mondialem", -1, -1),
        Among("cordgialem", -1, -1),
        Among("territorialem", -1, -1),
        Among("împartialem", -1, -1),
        Among("malem", -1, -1),
        Among("normalem", 247, -1),
        Among("méd'cinnalem", -1, -1),
        Among("finnalem", -1, -1),
        Among("machinnalem", -1, -1),
        Among("nonminnalem", -1, -1),
        Among("înfèrnalem", -1, -1),
        Among("prîncipalem", -1, -1),
        Among("moralem", -1, -1),
        Among("arbitralem", -1, -1),
        Among("centralem", -1, -1),
        Among("thiâtralem", -1, -1),
        Among("libéralem", -1, -1),
        Among("généralem", -1, -1),
        Among("latéralem", -1, -1),
        Among("littéralem", -1, -1),
        Among("salem", -1, -1),
        Among("tressalem", 263, -1),
        Among("fatalem", -1, -1),
        Among("digitalem", -1, -1),
        Among("horizontalem", -1, -1),
        Among("totalem", -1, -1),
        Among("brutalem", -1, -1),
        Among("louoyalem", -1, -1),
        Among("dêlouoyalem", 270, -1),
        Among("rouoyalem", -1, -1),
        Among("idéalem", -1, -1),
        Among("habilem", -1, -1),
        Among("facilem", -1, -1),
        Among("difficilem", -1, -1),
        Among("utilem", -1, -1),
        Among("civilem", -1, -1),
        Among("êmèrvilem", -1, -1),
        Among("êvilem", -1, -1),
        Among("amouochellem", -1, -1),
        Among("enchorchellem", -1, -1),
        Among("senchorchellem", 282, -1),
        Among("pathellem", -1, -1),
        Among("natuthellem", -1, -1),
        Among("structuthellem", -1, -1),
        Among("officiellem", -1, -1),
        Among("artificiellem", -1, -1),
        Among("supèrficiellem", -1, -1),
        Among("riellem", -1, -1),
        Among("îndustriellem", 290, -1),
        Among("confidentiellem", -1, -1),
        Among("providentiellem", -1, -1),
        Among("essentiellem", -1, -1),
        Among("originnellem", -1, -1),
        Among("crînminnellem", -1, -1),
        Among("rêsinnellem", -1, -1),
        Among("traditionnellem", -1, -1),
        Among("additionnellem", -1, -1),
        Among("conditionnellem", -1, -1),
        Among("întentionnellem", -1, -1),
        Among("exceptionnellem", -1, -1),
        Among("constitutionnellem", -1, -1),
        Among("solonnellem", -1, -1),
        Among("pèrsonnellem", -1, -1),
        Among("împèrsonnellem", 305, -1),
        Among("journellem", -1, -1),
        Among("patèrnellem", -1, -1),
        Among("êtèrnellem", -1, -1),
        Among("naturellem", -1, -1),
        Among("tellem", -1, -1),
        Among("accidentellem", 311, -1),
        Among("mortellem", 311, -1),
        Among("graduellem", -1, -1),
        Among("îndividuellem", -1, -1),
        Among("annuellem", -1, -1),
        Among("continnuellem", -1, -1),
        Among("cruellem", -1, -1),
        Among("mensuellem", -1, -1),
        Among("usuellem", -1, -1),
        Among("câsuellem", -1, -1),
        Among("actuellem", -1, -1),
        Among("întellectuellem", -1, -1),
        Among("ponctuellem", -1, -1),
        Among("habituellem", -1, -1),
        Among("spirituellem", -1, -1),
        Among("êventuellem", -1, -1),
        Among("mutuellem", -1, -1),
        Among("pèrpétuellem", -1, -1),
        Among("sexuellem", -1, -1),
        Among("nivellem", -1, -1),
        Among("nouvellem", -1, -1),
        Among("rêellem", -1, -1),
        Among("habillem", -1, -1),
        Among("patheillem", -1, -1),
        Among("embrouoillem", -1, -1),
        Among("catouoillem", -1, -1),
        Among("follem", -1, -1),
        Among("nullem", -1, -1),
        Among("scêllem", -1, -1),
        Among("êffrédolem", -1, -1),
        Among("êmiolem", -1, -1),
        Among("endgeulem", -1, -1),
        Among("seulem", -1, -1),
        Among("riditchulem", -1, -1),
        Among("bostchulem", -1, -1),
        Among("boulem", -1, -1),
        Among("êboulem", 347, -1),
        Among("coulem", -1, -1),
        Among("pâlem", -1, -1),
        Among("fidèlem", -1, -1),
        Among("înfidèlem", 351, -1),
        Among("bêlem", -1, -1),
        Among("drôlem", -1, -1),
        Among("enrôlem", -1, -1),
        Among("rouôlem", -1, -1),
        Among("êcrouôlem", 356, -1),
        Among("brûlem", -1, -1),
        Among("sublînmem", -1, -1),
        Among("întînmem", -1, -1),
        Among("quatrièmem", -1, -1),
        Among("traîsièmem", -1, -1),
        Among("neuvièmem", -1, -1),
        Among("deuxièmem", -1, -1),
        Among("seizièmem", -1, -1),
        Among("tchînzièmem", -1, -1),
        Among("quatorzièmem", -1, -1),
        Among("bliêmem", -1, -1),
        Among("extrêmem", -1, -1),
        Among("renseignem", -1, -1),
        Among("grouongnem", -1, -1),
        Among("dîngnem", -1, -1),
        Among("soudainem", -1, -1),
        Among("préchainem", -1, -1),
        Among("sainem", -1, -1),
        Among("cèrtainem", -1, -1),
        Among("încèrtainem", 376, -1),
        Among("hautainem", -1, -1),
        Among("vainem", -1, -1),
        Among("plieinem", -1, -1),
        Among("dreinem", -1, -1),
        Among("séreinem", -1, -1),
        Among("anciennem", -1, -1),
        Among("chrêtchiennem", -1, -1),
        Among("mouoyennem", -1, -1),
        Among("finnem", -1, -1),
        Among("raffinnem", 386, -1),
        Among("dêraichinnem", -1, -1),
        Among("tabouothinnem", -1, -1),
        Among("achéthinnem", -1, -1),
        Among("cajelinnem", -1, -1),
        Among("ouillinnem", -1, -1),
        Among("êminnem", -1, -1),
        Among("chagrinnem", -1, -1),
        Among("împèrtinnem", -1, -1),
        Among("piétinnem", -1, -1),
        Among("abandonnem", -1, -1),
        Among("bourdonnem", -1, -1),
        Among("êbourgeonnem", -1, -1),
        Among("endgèrdgichonnem", -1, -1),
        Among("envithonnem", -1, -1),
        Among("approvisionnem", -1, -1),
        Among("fonctionnem", -1, -1),
        Among("râtionnem", -1, -1),
        Among("stâtionnem", -1, -1),
        Among("tourbillonnem", -1, -1),
        Among("bouoillonnem", -1, -1),
        Among("ronnem", -1, -1),
        Among("gronnem", 408, -1),
        Among("couronnem", 408, -1),
        Among("raisonnem", -1, -1),
        Among("dêraisonnem", 411, -1),
        Among("frissonnem", -1, -1),
        Among("rêsonnem", -1, -1),
        Among("assaîsonnem", -1, -1),
        Among("empouaîsonnem", -1, -1),
        Among("tâtonnem", -1, -1),
        Among("êtonnem", -1, -1),
        Among("bouonnem", -1, -1),
        Among("autcheunem", -1, -1),
        Among("enchifrènem", -1, -1),
        Among("appartènem", -1, -1),
        Among("justènem", -1, -1),
        Among("vènem", -1, -1),
        Among("êvénem", -1, -1),
        Among("tapem", -1, -1),
        Among("êcappem", -1, -1),
        Among("achoppem", -1, -1),
        Among("dêveloppem", -1, -1),
        Among("attroupem", -1, -1),
        Among("barbarem", -1, -1),
        Among("rarem", -1, -1),
        Among("encôffrem", -1, -1),
        Among("bizarrem", -1, -1),
        Among("èrrem", -1, -1),
        Among("entèrrem", 435, -1),
        Among("dêtèrrem", 435, -1),
        Among("pouôrrem", -1, -1),
        Among("seûrem", -1, -1),
        Among("êcrasem", -1, -1),
        Among("grégeaisem", -1, -1),
        Among("emmalaisem", -1, -1),
        Among("seurnouaisem", -1, -1),
        Among("sournouaisem", -1, -1),
        Among("matouaisem", -1, -1),
        Among("courtouaisem", -1, -1),
        Among("mauvaisem", -1, -1),
        Among("îndécisem", -1, -1),
        Among("dêdgisem", -1, -1),
        Among("extchisem", -1, -1),
        Among("pansem", -1, -1),
        Among("récensem", -1, -1),
        Among("bonassem", -1, -1),
        Among("dêgourdissem", -1, -1),
        Among("êtourdissem", -1, -1),
        Among("tréfissem", -1, -1),
        Among("clièrgissem", -1, -1),
        Among("rêclièrgissem", 457, -1),
        Among("affranchissem", -1, -1),
        Among("adouochissem", -1, -1),
        Among("radouochissem", 460, -1),
        Among("dueurchissem", -1, -1),
        Among("endueurchissem", 462, -1),
        Among("accourchissem", -1, -1),
        Among("raccourchissem", 464, -1),
        Among("haûchissem", -1, -1),
        Among("dgéthissem", -1, -1),
        Among("r'dgéthissem", 467, -1),
        Among("èrdgéthissem", 467, -1),
        Among("enchiéthissem", -1, -1),
        Among("renchiéthissem", 470, -1),
        Among("péthissem", -1, -1),
        Among("ensev'lissem", -1, -1),
        Among("vieillissem", -1, -1),
        Among("abolissem", -1, -1),
        Among("vômissem", -1, -1),
        Among("bannissem", -1, -1),
        Among("êvannissem", -1, -1),
        Among("finnissem", -1, -1),
        Among("dgèrnissem", -1, -1),
        Among("breunissem", -1, -1),
        Among("dêdgèrpissem", -1, -1),
        Among("assoupissem", -1, -1),
        Among("pouôrrissem", -1, -1),
        Among("appaûvrissem", -1, -1),
        Among("saisissem", -1, -1),
        Among("êlouaîssissem", -1, -1),
        Among("êlaîsissem", -1, -1),
        Among("avèrtissem", -1, -1),
        Among("divèrtissem", -1, -1),
        Among("convèrtissem", -1, -1),
        Among("assujettissem", -1, -1),
        Among("abrutissem", -1, -1),
        Among("êtablyissem", -1, -1),
        Among("rêtablyissem", 494, -1),
        Among("affaiblyissem", -1, -1),
        Among("accomplyissem", -1, -1),
        Among("faussem", -1, -1),
        Among("dêlâssem", -1, -1),
        Among("dêpâssem", -1, -1),
        Among("chanceusem", -1, -1),
        Among("malchanceusem", 501, -1),
        Among("couothageusem", -1, -1),
        Among("outrageusem", -1, -1),
        Among("avantageusem", -1, -1),
        Among("savantageusem", 505, -1),
        Among("couôtageusem", -1, -1),
        Among("ravageusem", -1, -1),
        Among("foudgeusem", -1, -1),
        Among("clyîncheusem", -1, -1),
        Among("pièrcheusem", -1, -1),
        Among("haînitcheusem", -1, -1),
        Among("vigouotheusem", -1, -1),
        Among("amouotheusem", -1, -1),
        Among("malheutheusem", -1, -1),
        Among("beinheutheusem", -1, -1),
        Among("malaûtchoeutheusem", -1, -1),
        Among("génétheusem", -1, -1),
        Among("heûtheusem", -1, -1),
        Among("peûtheusem", -1, -1),
        Among("avathicieusem", -1, -1),
        Among("licieusem", -1, -1),
        Among("avaricieusem", -1, -1),
        Among("vicieusem", -1, -1),
        Among("consciencieusem", -1, -1),
        Among("silencieusem", -1, -1),
        Among("soucieusem", -1, -1),
        Among("grâcieusem", -1, -1),
        Among("disgrâcieusem", 528, -1),
        Among("précieusem", -1, -1),
        Among("précaûcieusem", -1, -1),
        Among("mélodieusem", -1, -1),
        Among("mînséthicordieusem", -1, -1),
        Among("contagieusem", -1, -1),
        Among("r'ligieusem", -1, -1),
        Among("èrligieusem", -1, -1),
        Among("prestigieusem", -1, -1),
        Among("futhieusem", -1, -1),
        Among("tchuthieusem", -1, -1),
        Among("înjuthieusem", -1, -1),
        Among("înféthieusem", -1, -1),
        Among("séthieusem", -1, -1),
        Among("mystéthieusem", -1, -1),
        Among("oublieusem", -1, -1),
        Among("dgiâblieusem", -1, -1),
        Among("anglieusem", -1, -1),
        Among("batilieusem", -1, -1),
        Among("înginnieusem", -1, -1),
        Among("pieusem", -1, -1),
        Among("glorieusem", -1, -1),
        Among("îndustrieusem", -1, -1),
        Among("ambitieusem", -1, -1),
        Among("minnutieusem", -1, -1),
        Among("scandaleusem", -1, -1),
        Among("mielleusem", -1, -1),
        Among("tcherelleusem", -1, -1),
        Among("ordgilleusem", -1, -1),
        Among("catouoilleusem", -1, -1),
        Among("gaspilleusem", -1, -1),
        Among("roupilleusem", -1, -1),
        Among("frauduleusem", -1, -1),
        Among("mithatchuleusem", -1, -1),
        Among("scrupuleusem", -1, -1),
        Among("brâleusem", -1, -1),
        Among("fanmeusem", -1, -1),
        Among("ranclieunmeusem", -1, -1),
        Among("gliunmeusem", -1, -1),
        Among("chicangneusem", -1, -1),
        Among("èrgouongneusem", -1, -1),
        Among("souongneusem", -1, -1),
        Among("r'tchîngneusem", -1, -1),
        Among("èrtchîngneusem", -1, -1),
        Among("leunminneusem", -1, -1),
        Among("rapinneusem", -1, -1),
        Among("ruinneusem", -1, -1),
        Among("chap'ronneusem", -1, -1),
        Among("soupçonneusem", -1, -1),
        Among("sgorneusem", -1, -1),
        Among("rantcheuneusem", -1, -1),
        Among("haîneusem", -1, -1),
        Among("peîneusem", -1, -1),
        Among("trompeusem", -1, -1),
        Among("râpeusem", -1, -1),
        Among("dangereusem", -1, -1),
        Among("affreusem", -1, -1),
        Among("âffreusem", -1, -1),
        Among("dgiântreusem", -1, -1),
        Among("dgiâtreusem", -1, -1),
        Among("malaûc'seusem", -1, -1),
        Among("penseusem", -1, -1),
        Among("ponseusem", -1, -1),
        Among("graîsseusem", -1, -1),
        Among("pouaîsseusem", -1, -1),
        Among("bliâseusem", -1, -1),
        Among("vâseusem", -1, -1),
        Among("briteusem", -1, -1),
        Among("nécessiteusem", -1, -1),
        Among("ardgumenteusem", -1, -1),
        Among("honteusem", -1, -1),
        Among("tchînteusem", -1, -1),
        Among("cliuteusem", -1, -1),
        Among("affectueusem", -1, -1),
        Among("respectueusem", -1, -1),
        Among("irrespectueusem", 603, -1),
        Among("vèrtueusem", -1, -1),
        Among("majestueusem", -1, -1),
        Among("nèrveusem", -1, -1),
        Among("jouaiyeusem", -1, -1),
        Among("briyeusem", -1, -1),
        Among("souoyeusem", -1, -1),
        Among("dêbouaîsem", -1, -1),
        Among("crouaîsem", -1, -1),
        Among("seûsem", -1, -1),
        Among("licatem", -1, -1),
        Among("înmédiatem", -1, -1),
        Among("îngratem", -1, -1),
        Among("parfaitem", -1, -1),
        Among("împarfaitem", 617, -1),
        Among("adraitem", -1, -1),
        Among("maladraitem", 619, -1),
        Among("traitem", -1, -1),
        Among("distraitem", 621, -1),
        Among("êtraitem", 621, -1),
        Among("subitem", -1, -1),
        Among("excitem", -1, -1),
        Among("enditem", -1, -1),
        Among("discréditem", -1, -1),
        Among("p'titem", -1, -1),
        Among("gratuitem", -1, -1),
        Among("vitem", -1, -1),
        Among("êcantem", -1, -1),
        Among("senchantem", -1, -1),
        Among("transpliantem", -1, -1),
        Among("lentem", -1, -1),
        Among("consentem", -1, -1),
        Among("présentem", -1, -1),
        Among("contentem", -1, -1),
        Among("malcontentem", 637, -1),
        Among("saintem", -1, -1),
        Among("appouaintem", -1, -1),
        Among("sappouaintem", 640, -1),
        Among("appointem", -1, -1),
        Among("sappointem", 642, -1),
        Among("sîntem", -1, -1),
        Among("chuchotem", -1, -1),
        Among("promptem", -1, -1),
        Among("battem", -1, -1),
        Among("abattem", 647, -1),
        Among("douochettem", -1, -1),
        Among("nettem", -1, -1),
        Among("douochottem", -1, -1),
        Among("frottem", -1, -1),
        Among("sottem", -1, -1),
        Among("brutem", -1, -1),
        Among("compliètem", -1, -1),
        Among("încompliètem", 655, -1),
        Among("discrètem", -1, -1),
        Among("îndiscrètem", 657, -1),
        Among("adrètem", -1, -1),
        Among("bein-gn-adrètem", 659, -1),
        Among("s'grètem", -1, -1),
        Among("bêtem", -1, -1),
        Among("honnêtem", -1, -1),
        Among("malhonnêtem", 663, -1),
        Among("emboêtem", -1, -1),
        Among("tempêtem", -1, -1),
        Among("agîtem", -1, -1),
        Among("couôtem", -1, -1),
        Among("longuem", -1, -1),
        Among("runguem", -1, -1),
        Among("snoguem", -1, -1),
        Among("tchoeuthuem", -1, -1),
        Among("r'muem", -1, -1),
        Among("èrmuem", -1, -1),
        Among("sécouem", -1, -1),
        Among("sengouem", -1, -1),
        Among("dêvouem", -1, -1),
        Among("secquem", -1, -1),
        Among("mangnifiquem", -1, -1),
        Among("magiquem", -1, -1),
        Among("tragiquem", -1, -1),
        Among("logiquem", -1, -1),
        Among("biologiquem", 682, -1),
        Among("sŷmpathiquem", -1, -1),
        Among("conmiquem", -1, -1),
        Among("anémiquem", -1, -1),
        Among("mécaniquem", -1, -1),
        Among("techniquem", -1, -1),
        Among("tyranniquem", -1, -1),
        Among("chroniquem", -1, -1),
        Among("euniquem", -1, -1),
        Among("hygiéniquem", -1, -1),
        Among("microscopiquem", -1, -1),
        Among("typiquem", -1, -1),
        Among("théoriquem", -1, -1),
        Among("hystériquem", -1, -1),
        Among("phŷsiquem", -1, -1),
        Among("dramatiquem", -1, -1),
        Among("diplomatiquem", -1, -1),
        Among("automatiquem", -1, -1),
        Among("systématiquem", -1, -1),
        Among("aristocratiquem", -1, -1),
        Among("pratiquem", -1, -1),
        Among("critiquem", -1, -1),
        Among("identiquem", -1, -1),
        Among("hypnotiquem", -1, -1),
        Among("artistiquem", -1, -1),
        Among("prophétiquem", -1, -1),
        Among("mangnétiquem", -1, -1),
        Among("phonétiquem", -1, -1),
        Among("génétiquem", -1, -1),
        Among("publyiquem", -1, -1),
        Among("êtanquem", -1, -1),
        Among("rembèrquem", -1, -1),
        Among("renvèrquem", -1, -1),
        Among("empouquem", -1, -1),
        Among("affêquem", -1, -1),
        Among("tuem", -1, -1),
        Among("lavem", -1, -1),
        Among("bravem", -1, -1),
        Among("êvasivem", -1, -1),
        Among("offensivem", -1, -1),
        Among("pensivem", -1, -1),
        Among("successivem", -1, -1),
        Among("excessivem", -1, -1),
        Among("progressivem", -1, -1),
        Among("împressivem", -1, -1),
        Among("mâssivem", -1, -1),
        Among("ouaîsivem", -1, -1),
        Among("r'lativem", -1, -1),
        Among("èrlativem", -1, -1),
        Among("décorativem", -1, -1),
        Among("adminnistrativem", -1, -1),
        Among("activem", -1, -1),
        Among("respectivem", -1, -1),
        Among("addictivem", -1, -1),
        Among("înstînctivem", -1, -1),
        Among("productivem", -1, -1),
        Among("prînmitivem", -1, -1),
        Among("définnitivem", -1, -1),
        Among("positivem", -1, -1),
        Among("attentivem", -1, -1),
        Among("craintivem", -1, -1),
        Among("bontivem", -1, -1),
        Among("fautivem", -1, -1),
        Among("chétivem", -1, -1),
        Among("vivem", -1, -1),
        Among("mouvem", -1, -1),
        Among("adgèvem", -1, -1),
        Among("souôlèvem", -1, -1),
        Among("dêgrèvem", -1, -1),
        Among("naïvem", -1, -1),
        Among("trantchil'yem", -1, -1),
        Among("gréem", -1, -1),
        Among("chim", -1, -1),
        Among("expéthim", -1, -1),
        Among("îndéfinnim", -1, -1),
        Among("pim", -1, -1),
        Among("expérim", -1, -1),
        Among("quâsim", -1, -1),
        Among("gentim", -1, -1),
        Among("sentim", -1, -1),
        Among("pressentim", 762, -1),
        Among("îndépendamm", -1, -1),
        Among("abondamm", -1, -1),
        Among("accordamm", -1, -1),
        Among("extravagamm", -1, -1),
        Among("convaintchamm", -1, -1),
        Among("chotchamm", -1, -1),
        Among("mêchamm", -1, -1),
        Among("couothamm", -1, -1),
        Among("întoléthamm", -1, -1),
        Among("rasseûthamm", -1, -1),
        Among("nochalamm", -1, -1),
        Among("vaillamm", -1, -1),
        Among("brillamm", -1, -1),
        Among("r'pugnamm", -1, -1),
        Among("èrpugnamm", -1, -1),
        Among("êtonnamm", -1, -1),
        Among("b'samm", -1, -1),
        Among("suffisamm", -1, -1),
        Among("rafraîchissamm", -1, -1),
        Among("împuissamm", -1, -1),
        Among("piêssamm", -1, -1),
        Among("întérêssamm", -1, -1),
        Among("r'connaîssamm", -1, -1),
        Among("èrconnaîssamm", -1, -1),
        Among("pésamm", -1, -1),
        Among("pliaîsamm", -1, -1),
        Among("compliaîsamm", 789, -1),
        Among("exorbitamm", -1, -1),
        Among("notamm", -1, -1),
        Among("constamm", -1, -1),
        Among("savamm", -1, -1),
        Among("récemm", -1, -1),
        Among("êvidemm", -1, -1),
        Among("ardemm", -1, -1),
        Among("prudemm", -1, -1),
        Among("împrudemm", 798, -1),
        Among("oblyigemm", -1, -1),
        Among("néglyigemm", -1, -1),
        Among("appathemm", -1, -1),
        Among("difféthemm", -1, -1),
        Among("pâciemm", -1, -1),
        Among("împâciemm", 804, -1),
        Among("înconvéniemm", -1, -1),
        Among("împâtiemm", -1, -1),
        Among("excellemm", -1, -1),
        Among("îndolemm", -1, -1),
        Among("violemm", -1, -1),
        Among("încompétemm", -1, -1),
        Among("conséquemm", -1, -1),
        Among("comm", -1, -1),
        Among("coumm", -1, -1),
        Among("ronflianm", -1, -1),
        Among("fronm", -1, -1),
        Among("jeunm", -1, -1),
        Among("tempéthânm", -1, -1),
        Among("vraînm", -1, -1),
        Among("régînm", -1, -1),
        Among("chînm", -1, -1),
        Among("pînm", -1, -1),
        Among("mom", -1, -1),
        Among("sèrm", -1, -1),
        Among("ardgum", -1, -1),
        Among("dotchum", -1, -1),
        Among("jum", -1, -1),
        Among("absolum", -1, -1),
        Among("monum", -1, -1),
        Among("înstrum", -1, -1),
        Among("tempêthâm", -1, -1),
        Among("absorbém", -1, -1),
        Among("supèrbém", -1, -1),
        Among("parfondém", -1, -1),
        Among("bombardém", -1, -1),
        Among("bûsardém", -1, -1),
        Among("dêbordém", -1, -1),
        Among("gourdém", -1, -1),
        Among("sourdém", -1, -1),
        Among("dêgorgém", -1, -1),
        Among("dêchèrgém", -1, -1),
        Among("r'tèrgém", -1, -1),
        Among("èrtèrgém", -1, -1),
        Among("raccourchém", -1, -1),
        Among("bèrchém", -1, -1),
        Among("bitchém", -1, -1),
        Among("sembèrtchém", -1, -1),
        Among("probabliém", -1, -1),
        Among("împrobabliém", 848, -1),
        Among("irrévocabliém", -1, -1),
        Among("vendabliém", -1, -1),
        Among("dommageabliém", -1, -1),
        Among("néglyigeabliém", -1, -1),
        Among("affabliém", -1, -1),
        Among("irrempliaichabliém", -1, -1),
        Among("innexplyitchabliém", -1, -1),
        Among("ristchabliém", -1, -1),
        Among("îns'pathabliém", -1, -1),
        Among("compathabliém", -1, -1),
        Among("încompathabliém", 859, -1),
        Among("irrépathabliém", -1, -1),
        Among("însépathabliém", -1, -1),
        Among("admithabliém", -1, -1),
        Among("sithabliém", -1, -1),
        Among("înd'sithabliém", 864, -1),
        Among("honothabliém", -1, -1),
        Among("adouothabliém", -1, -1),
        Among("m'suthabliém", -1, -1),
        Among("considéthabliém", -1, -1),
        Among("transféthabliém", -1, -1),
        Among("préféthabliém", -1, -1),
        Among("toléthabliém", -1, -1),
        Among("vénéthabliém", -1, -1),
        Among("mînséthabliém", -1, -1),
        Among("sociabliém", -1, -1),
        Among("fiabliém", -1, -1),
        Among("irrémédgiabliém", -1, -1),
        Among("pitchiabliém", -1, -1),
        Among("înnoubliabliém", -1, -1),
        Among("pliabliém", -1, -1),
        Among("vâliabliém", -1, -1),
        Among("criabliém", -1, -1),
        Among("êffriabliém", -1, -1),
        Among("agriabliém", -1, -1),
        Among("sagriabliém", 884, -1),
        Among("vâriabliém", -1, -1),
        Among("învâriabliém", 886, -1),
        Among("înconsolabliém", -1, -1),
        Among("aimabliém", -1, -1),
        Among("conv'nabliém", -1, -1),
        Among("comprannabliém", -1, -1),
        Among("încomprannabliém", 891, -1),
        Among("înstannabliém", -1, -1),
        Among("abominnabliém", -1, -1),
        Among("întèrminnabliém", -1, -1),
        Among("împardonnabliém", -1, -1),
        Among("raisonnabliém", -1, -1),
        Among("dêraisonnabliém", 897, -1),
        Among("însténabliém", -1, -1),
        Among("capabliém", -1, -1),
        Among("coupabliém", -1, -1),
        Among("dêchiffrabliém", -1, -1),
        Among("adorabliém", -1, -1),
        Among("mémorabliém", -1, -1),
        Among("honorabliém", -1, -1),
        Among("shonorabliém", 905, -1),
        Among("favorabliém", -1, -1),
        Among("vénérabliém", -1, -1),
        Among("prédisabliém", -1, -1),
        Among("împrédisabliém", 909, -1),
        Among("îndispensabliém", -1, -1),
        Among("responsabliém", -1, -1),
        Among("irresponsabliém", 912, -1),
        Among("îndgéthissabliém", -1, -1),
        Among("péthissabliém", -1, -1),
        Among("pâssabliém", -1, -1),
        Among("connaîssabliém", -1, -1),
        Among("r'connaîssabliém", 917, -1),
        Among("èrconnaîssabliém", 917, -1),
        Among("dêconnaîssabliém", 917, -1),
        Among("mêconnaîssabliém", 917, -1),
        Among("haïssabliém", -1, -1),
        Among("extchûsabliém", -1, -1),
        Among("innextchûsabliém", 923, -1),
        Among("întranslatabliém", -1, -1),
        Among("respectabliém", -1, -1),
        Among("împrédictabliém", -1, -1),
        Among("seûthetabliém", -1, -1),
        Among("souhaitabliém", -1, -1),
        Among("însouhaitabliém", 929, -1),
        Among("traitabliém", -1, -1),
        Among("véthitabliém", -1, -1),
        Among("charitabliém", -1, -1),
        Among("irritabliém", -1, -1),
        Among("êvitabliém", -1, -1),
        Among("êpouvantabliém", -1, -1),
        Among("lamentabliém", -1, -1),
        Among("présentabliém", -1, -1),
        Among("notabliém", -1, -1),
        Among("acceptabliém", -1, -1),
        Among("îndomptabliém", -1, -1),
        Among("confortabliém", -1, -1),
        Among("însupportabliém", -1, -1),
        Among("dêtestabliém", -1, -1),
        Among("înstabliém", -1, -1),
        Among("ajustabliém", -1, -1),
        Among("r'grettabliém", -1, -1),
        Among("èrgrettabliém", -1, -1),
        Among("louabliém", -1, -1),
        Among("r'mèrquabliém", -1, -1),
        Among("èrmèrquabliém", -1, -1),
        Among("prouvabliém", -1, -1),
        Among("trouvabliém", -1, -1),
        Among("întrouvabliém", 953, -1),
        Among("încriyabliém", -1, -1),
        Among("împrononçabliém", -1, -1),
        Among("fouaibliém", -1, -1),
        Among("crédibliém", -1, -1),
        Among("încorrigibliém", -1, -1),
        Among("niêthibliém", -1, -1),
        Among("înfaillibliém", -1, -1),
        Among("pénibliém", -1, -1),
        Among("tèrribliém", -1, -1),
        Among("hôrribliém", -1, -1),
        Among("paisibliém", -1, -1),
        Among("risibliém", -1, -1),
        Among("întraduisibliém", -1, -1),
        Among("visibliém", -1, -1),
        Among("învisibliém", 968, -1),
        Among("sensibliém", -1, -1),
        Among("accessibliém", -1, -1),
        Among("innaccessibliém", 971, -1),
        Among("împôssibliém", -1, -1),
        Among("illiêsibliém", -1, -1),
        Among("niêsibliém", -1, -1),
        Among("irresistibliém", -1, -1),
        Among("trembliém", -1, -1),
        Among("assembliém", -1, -1),
        Among("rassembliém", 978, -1),
        Among("humbliém", -1, -1),
        Among("nobliém", -1, -1),
        Among("ameubliém", -1, -1),
        Among("doubliém", -1, -1),
        Among("troubliém", -1, -1),
        Among("accâbliém", -1, -1),
        Among("dgiâbliém", -1, -1),
        Among("cliém", -1, -1),
        Among("soûffliém", -1, -1),
        Among("sûffliém", -1, -1),
        Among("ronfliém", -1, -1),
        Among("êtrangliém", -1, -1),
        Among("aveugliém", -1, -1),
        Among("règliém", -1, -1),
        Among("tripliém", -1, -1),
        Among("înmpliém", -1, -1),
        Among("sîmpliém", -1, -1),
        Among("suppliém", -1, -1),
        Among("dêpeupliém", -1, -1),
        Among("accoupliém", -1, -1),
        Among("soupliém", -1, -1),
        Among("supplém", -1, -1),
        Among("parlém", -1, -1),
        Among("heurlém", -1, -1),
        Among("êlém", -1, -1),
        Among("calmém", -1, -1),
        Among("armém", -1, -1),
        Among("têtouongném", -1, -1),
        Among("îndîngném", -1, -1),
        Among("rêsinném", -1, -1),
        Among("orném", -1, -1),
        Among("ajourném", -1, -1),
        Among("discèrném", -1, -1),
        Among("gouvèrném", -1, -1),
        Among("dêlabrém", -1, -1),
        Among("librém", -1, -1),
        Among("sombrém", -1, -1),
        Among("sobrém", -1, -1),
        Among("ludgubrém", -1, -1),
        Among("tendrém", -1, -1),
        Among("maîndrém", -1, -1),
        Among("poudrém", -1, -1),
        Among("gouffrém", -1, -1),
        Among("boufrém", -1, -1),
        Among("maigrém", -1, -1),
        Among("bigrém", -1, -1),
        Among("bougrém", -1, -1),
        Among("allègrém", -1, -1),
        Among("întègrém", -1, -1),
        Among("proprém", -1, -1),
        Among("malproprém", 1029, -1),
        Among("sâprém", -1, -1),
        Among("dgiântrém", -1, -1),
        Among("fotrém", -1, -1),
        Among("scouotrém", -1, -1),
        Among("bistrém", -1, -1),
        Among("tristrém", -1, -1),
        Among("boustrém", -1, -1),
        Among("frustrém", -1, -1),
        Among("enregîstrém", -1, -1),
        Among("autrém", -1, -1),
        Among("foutrém", -1, -1),
        Among("dgiâtrém", -1, -1),
        Among("marâtrém", -1, -1),
        Among("traîtrém", -1, -1),
        Among("pauvrém", -1, -1),
        Among("remboursém", -1, -1),
        Among("dêboursém", -1, -1),
        Among("divèrsém", -1, -1),
        Among("pèrvèrsém", -1, -1),
        Among("aheuqu'tém", -1, -1),
        Among("exactém", -1, -1),
        Among("directém", -1, -1),
        Among("îndirectém", 1052, -1),
        Among("correctém", -1, -1),
        Among("încorrectém", 1054, -1),
        Among("strictém", -1, -1),
        Among("distînctém", -1, -1),
        Among("abruptém", -1, -1),
        Among("appartém", -1, -1),
        Among("départém", -1, -1),
        Among("fortém", -1, -1),
        Among("emportém", -1, -1),
        Among("mêportém", -1, -1),
        Among("avouortém", -1, -1),
        Among("apèrtém", -1, -1),
        Among("ouvèrtém", -1, -1),
        Among("vastém", -1, -1),
        Among("modestém", -1, -1),
        Among("lestém", -1, -1),
        Among("célestém", 1069, -1),
        Among("tristém", -1, -1),
        Among("robustém", -1, -1),
        Among("justém", -1, -1),
        Among("înjustém", 1073, -1),
        Among("quém", -1, -1),
        Among("embèrquém", 1075, -1),
        Among("sembèrquém", 1076, -1),
        Among("dêbèrquém", 1075, -1),
        Among("presquém", 1075, -1),
        Among("fisquém", 1075, -1),
        Among("brusquém", 1075, -1),
        Among("ênèrvém", -1, -1),
        Among("dêlobêm", -1, -1),
        Among("décidêm", -1, -1),
        Among("dêvèrgondêm", -1, -1),
        Among("dêmodêm", -1, -1),
        Among("dêmathêm", -1, -1),
        Among("s'pathêm", -1, -1),
        Among("sépathêm", -1, -1),
        Among("affaithêm", -1, -1),
        Among("dênatuthêm", -1, -1),
        Among("délibéthêm", -1, -1),
        Among("modéthêm", -1, -1),
        Among("viciêm", -1, -1),
        Among("dêrégliêm", -1, -1),
        Among("compliêm", -1, -1),
        Among("dêliêm", -1, -1),
        Among("naûmiêm", -1, -1),
        Among("manniêm", -1, -1),
        Among("fèrmêm", -1, -1),
        Among("dêtèrminnêm", -1, -1),
        Among("sareunêm", -1, -1),
        Among("avrônêm", -1, -1),
        Among("capêm", -1, -1),
        Among("rupêm", -1, -1),
        Among("tupêm", -1, -1),
        Among("râpêm", -1, -1),
        Among("sagrêm", -1, -1),
        Among("cârrêm", -1, -1),
        Among("malavisêm", -1, -1),
        Among("censêm", -1, -1),
        Among("posêm", -1, -1),
        Among("êvassêm", -1, -1),
        Among("exprêssêm", -1, -1),
        Among("rusêm", -1, -1),
        Among("sappouaintêm", -1, -1),
        Among("sappointêm", -1, -1),
        Among("dêhontêm", -1, -1),
        Among("affrontêm", -1, -1),
        Among("estchîntêm", -1, -1),
        Among("hagotêm", -1, -1),
        Among("dêroutêm", -1, -1),
        Among("êffathuêm", -1, -1),
        Among("envitouêm", -1, -1),
        Among("dêvouêm", -1, -1),
        Among("agravêm", -1, -1),
        Among("dêpravêm", -1, -1),
        Among("privêm", -1, -1),
        Among("vraîm", -1, -1),
        Among("hardîm", -1, -1),
        Among("bragîm", -1, -1),
        Among("complyitchîm", -1, -1),
        Among("polîm", -1, -1),
        Among("malpolîm", 1133, -1),
        Among("r'frouangnîm", -1, -1),
        Among("èrfrouangnîm", -1, -1),
        Among("compartîm", -1, -1),
        Among("assortîm", -1, -1),
        Among("sexîm", -1, -1),
        Among("complyîm", -1, -1),
        Among("mannyîm", -1, -1),
        Among("jouôm", -1, -1),
        Among("innattendûm", -1, -1),
        Among("îndeûm", -1, -1),
        Among("aidgûm", -1, -1),
        Among("fichûm", -1, -1),
        Among("irrésolûm", -1, -1),
        Among("rêsolûm", -1, -1),
        Among("goulûm", -1, -1),
        Among("pèrman", -1, -1),
        Among("prominn", -1, -1),
        Among("êminn", -1, -1),
        Among("continn", -1, -1),
        Among("împèrtinn", -1, -1),
        Among("tchèrp", -1, -1),
        Among("sèrp", -1, -1),
        Among("torr", -1, -1),
        Among("s", -1, -1),
        Among("abs", 1158, -1),
        Among("ass", 1158, -1),
        Among("prés", 1158, -1),
        Among("pénit", -1, -1),
        Among("cont", -1, -1),
        Among("malcont", 1163, -1),
        Among("încompét", -1, -1),
        Among("ongu", -1, -1),
        Among("conséqu", -1, -1),
        Among("v", -1, -1),
        Among("l'v", 1168, -1),
        Among("daiv", 1168, -1),
        Among("peuv", 1168, -1),
        Among("couv", 1168, -1),
        Among("souv", 1168, -1),
        Among("êv", 1168, -1),
        Among("l'êv", 1174, -1)
    ]

    a_3 = [
        Among("habi", -1, -1),
        Among("haleine", -1, -1),
        Among("halenée", -1, -1),
        Among("haoulouoge", -1, -1),
        Among("harias", -1, -1),
        Among("harmonium", -1, -1),
        Among("hasias", -1, -1),
        Among("hathias", -1, -1),
        Among("hav'non", -1, -1),
        Among("hav'thon", -1, -1),
        Among("haîmpettes", -1, -1),
        Among("haûsîn", -1, -1),
        Among("heu", -1, 1),
        Among("heunmeu", 12, -1),
        Among("heunmid", 12, -1),
        Among("heur", 12, 1),
        Among("heure", 15, -1),
        Among("heuth", 12, -1),
        Among("heûre", -1, -1),
        Among("heûs", -1, -1),
        Among("heûth", -1, -1),
        Among("hie", -1, -1),
        Among("hiouppe", -1, -1),
        Among("hippo", -1, -1),
        Among("hiron", -1, -1),
        Among("his", -1, -1),
        Among("hiv", -1, -1),
        Among("hiè", -1, -1),
        Among("homicide", -1, -1),
        Among("homm'thie", -1, -1),
        Among("hommage", -1, -1),
        Among("homme", -1, 1),
        Among("hommes", 31, 1),
        Among("honmage", -1, -1),
        Among("honmasse", -1, -1),
        Among("honme", -1, 1),
        Among("honneu", -1, 1),
        Among("honnête", -1, -1),
        Among("honor", -1, -1),
        Among("horiz", -1, -1),
        Among("hortic", -1, -1),
        Among("hospi", -1, -1),
        Among("houa", -1, -1),
        Among("houe", -1, -1),
        Among("houi", -1, -1),
        Among("houo", -1, -1),
        Among("houp'sé", -1, -1),
        Among("houyie", -1, -1),
        Among("houé", -1, -1),
        Among("houê", -1, -1),
        Among("houî", -1, -1),
        Among("houô", -1, -1),
        Among("hue", -1, -1),
        Among("hufer", -1, -1),
        Among("hui", -1, -1),
        Among("hum", -1, -1),
        Among("hus", -1, -1),
        Among("hy", -1, -1),
        Among("hâcou", -1, -1),
        Among("hâsard", -1, -1),
        Among("hâsi", -1, -1),
        Among("hâsîn", -1, -1),
        Among("hèrb", -1, -1),
        Among("hèrch", -1, -1),
        Among("hèrmi", -1, -1),
        Among("hèrs", -1, -1),
        Among("hébreu", -1, -1),
        Among("hélas", -1, -1),
        Among("héliotrope", -1, -1),
        Among("hélièr", -1, -1),
        Among("hélyi", -1, -1),
        Among("hémorragie", -1, -1),
        Among("hérode", -1, -1),
        Among("héré", -1, -1),
        Among("hési", -1, -1),
        Among("héthache", -1, -1),
        Among("héthi", -1, -1),
        Among("hétho", -1, -1),
        Among("héthèque", -1, -1),
        Among("hîndou", -1, -1),
        Among("hînmeu", -1, -1),
        Among("hîs", -1, -1),
        Among("hît", -1, -1),
        Among("hôlou", -1, -1),
        Among("hôpit", -1, -1),
        Among("hôrr", -1, -1),
        Among("hôte", -1, 1),
        Among("hôtel", 86, -1),
        Among("hûs", -1, -1),
        Among("hŷ", -1, -1)
    ]

    a_4 = [
        Among("'", -1, 31),
        Among("b", -1, 1),
        Among("bb", 1, 1),
        Among("c", -1, 3),
        Among("c'c", 3, 5),
        Among("cc", 3, 4),
        Among("ce'", 3, 2),
        Among("ch", 3, 6),
        Among("chr", 7, 7),
        Among("cqu", 3, 23),
        Among("d", -1, 8),
        Among("dd", 10, 8),
        Among("dg", 10, 9),
        Among("f", -1, 10),
        Among("ff", 13, 10),
        Among("g", -1, 11),
        Among("g'g", 15, 12),
        Among("gn", 15, 21),
        Among("gu", 15, 13),
        Among("gue", 18, 14),
        Among("h", -1, -1),
        Among("j", -1, 15),
        Among("k", -1, -1),
        Among("l", -1, 16),
        Among("l'l", 23, 17),
        Among("l'ye", 23, 16),
        Among("ll", 23, 16),
        Among("lyi", 23, 18),
        Among("m", -1, 19),
        Among("mm", 28, 19),
        Among("n", -1, 20),
        Among("nn", 30, 20),
        Among("p", -1, 22),
        Among("ph", 32, 10),
        Among("pp", 32, 22),
        Among("qu", -1, 23),
        Among("r", -1, 24),
        Among("rr", 36, 24),
        Among("s", -1, 25),
        Among("sc", 38, 26),
        Among("ss", 38, 2),
        Among("t", -1, 27),
        Among("tch", 41, 28),
        Among("th", 41, 29),
        Among("tt", 41, 27),
        Among("v", -1, -1),
        Among("w", -1, -1),
        Among("x", -1, 30),
        Among("z", -1, 30),
        Among("ç", -1, 2)
    ]

    a_5 = [
        Among("a", -1, 1),
        Among("ai", 0, 27),
        Among("aill", 1, 41),
        Among("aill'", 2, 42),
        Among("ain", 1, 14),
        Among("an", 0, 13),
        Among("ant", 5, 15),
        Among("antch", 6, 16),
        Among("au", 0, 28),
        Among("ayi", 0, 34),
        Among("aî", 0, 9),
        Among("aû", 0, 11),
        Among("e", -1, 2),
        Among("eau", 12, 28),
        Among("ei", 12, 2),
        Among("eill", 14, 43),
        Among("eill'l", 15, 44),
        Among("ein", 14, 14),
        Among("em", 12, 19),
        Among("en", 12, 17),
        Among("enn'", 19, 18),
        Among("enne", 19, 18),
        Among("ent", 19, 15),
        Among("entch", 22, 16),
        Among("eu", 12, 36),
        Among("eî", 12, 35),
        Among("eû", 12, 37),
        Among("i", -1, 4),
        Among("ill", 27, 45),
        Among("ill'l", 28, 46),
        Among("in", 27, 20),
        Among("o", -1, 6),
        Among("oeu", 31, 36),
        Among("om", 31, 24),
        Among("on", 31, 22),
        Among("ou", 31, 39),
        Among("où", 31, 39),
        Among("oû", 31, 38),
        Among("u", -1, 7),
        Among("ueu", 38, 30),
        Among("ui", 38, 29),
        Among("um", 38, 26),
        Among("un", 38, 25),
        Among("uî", 38, 31),
        Among("uîn", 43, 32),
        Among("y", -1, 5),
        Among("yi", 45, 33),
        Among("à", -1, 1),
        Among("â", -1, 8),
        Among("è", -1, 2),
        Among("é", -1, 2),
        Among("ée", 50, 3),
        Among("ê", -1, 9),
        Among("ë", -1, 2),
        Among("ëm", 53, 19),
        Among("ën", 53, 17),
        Among("ënne", 55, 18),
        Among("î", -1, 10),
        Among("în", 57, 21),
        Among("ï", -1, 5),
        Among("ô", -1, 11),
        Among("ôn", 60, 23),
        Among("öu", -1, 40),
        Among("ù", -1, 7),
        Among("û", -1, 12),
        Among("ü", -1, 7),
        Among("ŷ", -1, 10)
    ]

    a_6 = [
        Among("ai", -1, 1),
        Among("aie", 0, 14),
        Among("aient", 1, 13),
        Among("aille", 0, 36),
        Among("aim", 0, 2),
        Among("ait", 0, 13),
        Among("anc", -1, 39),
        Among("au", -1, 6),
        Among("aue", 7, 7),
        Among("aus", 7, 6),
        Among("aux", 7, 7),
        Among("aye", -1, 3),
        Among("aî", -1, 5),
        Among("aîs", 12, 5),
        Among("aïen", -1, 15),
        Among("b", -1, 40),
        Among("c", -1, 37),
        Among("cq", 16, 37),
        Among("d", -1, 40),
        Among("e", -1, 30),
        Among("eaux", 19, 7),
        Among("ement", 19, 33),
        Among("emente", 21, 34),
        Among("enne", 19, 20),
        Among("enner", 23, 32),
        Among("ennez", 23, 32),
        Among("ent", 19, 18),
        Among("er", 19, 1),
        Among("est", 19, 17),
        Among("et", 19, 4),
        Among("ets", 29, 4),
        Among("eue", 19, 10),
        Among("euse", 19, 11),
        Among("eux", 19, 10),
        Among("eyen", 19, 15),
        Among("ez", 19, 16),
        Among("g", -1, 40),
        Among("g'", 36, 38),
        Among("gue", 36, 31),
        Among("h", -1, 40),
        Among("id", -1, 24),
        Among("ids", 40, 24),
        Among("ie", -1, 24),
        Among("ieau", 42, 8),
        Among("ieaux", 43, 9),
        Among("ien", 42, 21),
        Among("ienne", 45, 22),
        Among("ille", -1, 35),
        Among("inne", -1, 23),
        Among("is", -1, 24),
        Among("it", -1, 24),
        Among("its", 50, 24),
        Among("ix", -1, 24),
        Among("iz", -1, 26),
        Among("j", -1, 40),
        Among("m", -1, 40),
        Among("ment", 55, 33),
        Among("mente", 56, 34),
        Among("n", -1, 40),
        Among("o", -1, 27),
        Among("oue", 59, 28),
        Among("p", -1, 40),
        Among("q", -1, 37),
        Among("s", -1, 40),
        Among("t", -1, 40),
        Among("ue", -1, 25),
        Among("v", -1, 40),
        Among("w", -1, 40),
        Among("x", -1, 40),
        Among("ye", -1, 29),
        Among("z", -1, 40),
        Among("ée", -1, 12),
        Among("éer", 71, 19),
        Among("és", -1, 16),
        Among("ët", -1, 4),
        Among("ëts", 74, 4),
        Among("ïen", -1, 21),
        Among("ïenne", 76, 22)
    ]

    a_7 = [
        Among("ch'", -1, 11),
        Among("d'", -1, 6),
        Among("j'", -1, 1),
        Among("l'", -1, 4),
        Among("li'", -1, 5),
        Among("m'", -1, 7),
        Among("n'", -1, 8),
        Among("qu'", -1, 9),
        Among("s'", -1, 3),
        Among("t'", -1, 2),
        Among("tu'", -1, 10),
        Among("y'", -1, 12)
    ]

    a_8 = [
        Among("a", -1, 1),
        Among("b", -1, 2),
        Among("c", -1, 3),
        Among("d", -1, 4),
        Among("e", -1, 5),
        Among("f", -1, 6),
        Among("g", -1, 7),
        Among("h", -1, 8),
        Among("i", -1, -1),
        Among("j", -1, 9),
        Among("k", -1, 10),
        Among("l", -1, 11),
        Among("m", -1, 12),
        Among("n", -1, 13),
        Among("o", -1, 14),
        Among("p", -1, 15),
        Among("q", -1, 16),
        Among("r", -1, 17),
        Among("s", -1, 18),
        Among("t", -1, 19),
        Among("u", -1, 20),
        Among("v", -1, 21),
        Among("w", -1, 22),
        Among("x", -1, 23),
        Among("y", -1, 24),
        Among("z", -1, 25)
    ]
    as_8 = ("a", "be", "se", "de", "œ", "ɛf", "ʒe", "ɔʃ", "ʒi", "ka", "ɛl", "ɛm", "ɛn", "ɔ", "pe", "ky", "ɛr", "ɛs", "te", "y", "ve", "dyblj ve", "ɛks", "i", "zɛd")

    a_9 = [
        Among("'tions", -1, 36),
        Among("ces", -1, 16),
        Among("ch't", -1, 18),
        Among("ch't'", 2, 18),
        Among("ches", -1, 17),
        Among("d's", -1, 4),
        Among("des", -1, 2),
        Among("es", -1, 20),
        Among("eus", -1, 27),
        Among("eut", -1, 27),
        Among("eûdrent", -1, 30),
        Among("eûdres", -1, 30),
        Among("eûnmes", -1, 28),
        Among("eûsse", -1, 31),
        Among("eûssent", 13, 31),
        Among("eûssiez", -1, 34),
        Among("eûssions", -1, 32),
        Among("eûssyiz", -1, 33),
        Among("eûtent", -1, 29),
        Among("eûtes", -1, 29),
        Among("hie", -1, 25),
        Among("icho", -1, 26),
        Among("il", -1, 19),
        Among("l's", -1, 3),
        Among("les", -1, 1),
        Among("m'n", -1, 5),
        Among("m's", -1, 7),
        Among("m'th", -1, 8),
        Among("mes", -1, 9),
        Among("mén", -1, 6),
        Among("n'n", -1, 15),
        Among("neuf", -1, 22),
        Among("ours", -1, 37),
        Among("s'n", -1, 13),
        Among("ses", -1, 16),
        Among("sén", -1, 14),
        Among("t'n", -1, 10),
        Among("tes", -1, 12),
        Among("tén", -1, 11),
        Among("x", -1, 23),
        Among("y", -1, 24),
        Among("ès", -1, 21),
        Among("étions", -1, 35)
    ]
    as_9 = ("le", "de", "lz", "dz", "mn", "mɛn", "mz", "mð", "mɛ", "tn", "tɛn", "tɛ", "sn", "sɛn", "nn", "se", "ʃe", "ʃt", "il", "e", "ɛ", "nœ", "ɛks", "i", "iː", "iko", "y", "yːm", "yːt", "yːdr", "yːs", "yːsjõ", "yːsji", "yːsje", "ɛtjõ", "tjõ", "urs")

    a_10 = [
        Among("aîsiement", -1, 7),
        Among("bibliothèque", -1, 5),
        Among("biguesse", -1, 11),
        Among("corps", -1, 9),
        Among("g'lice", -1, 14),
        Among("g'linne", -1, 15),
        Among("g'luge", -1, 16),
        Among("g'niche", -1, 20),
        Among("g'nou", -1, 18),
        Among("g'nouo", 8, 19),
        Among("g'nêt", -1, 17),
        Among("guy", -1, 1),
        Among("hypothèque", -1, 6),
        Among("jétho", -1, 10),
        Among("mille", -1, 4),
        Among("onguenn", -1, 12),
        Among("onguent", -1, 13),
        Among("sept", -1, 8),
        Among("ville", -1, 3),
        Among("vîngt", -1, 2)
    ]

    a_11 = [
        Among("b", -1, 1),
        Among("bb", 0, 1),
        Among("c", -1, 1),
        Among("cc", 2, 1),
        Among("f", -1, 1),
        Among("ff", 4, 1),
        Among("g", -1, 1),
        Among("p", -1, 1),
        Among("pp", 7, 1)
    ]

    a_12 = [
        Among("ax", -1, 5),
        Among("bike", -1, 7),
        Among("bâpt", -1, 9),
        Among("femm", -1, 2),
        Among("g'l", -1, 10),
        Among("hook", -1, 8),
        Among("llem", -1, 3),
        Among("osc", -1, 6),
        Among("temps", -1, 1),
        Among("tion", -1, 4)
    ]

    a_13 = [
        Among("deux-trais", -1, 3),
        Among("p't-êt'", -1, 2),
        Among("p't-être", -1, 1),
        Among("pe't-êt'", -1, 2),
        Among("pe't-être", -1, 1)
    ]
    as_13 = ("pteːtr", "pteːt", "dœztre")

    a_14 = [
        Among("-alle", -1, 7),
        Among("-en", -1, 10),
        Among("-i'", -1, 6),
        Among("-ieune", -1, 3),
        Among("-ieunième", -1, 4),
        Among("-ouos", -1, 9),
        Among("-ous", -1, 8),
        Among("-t-alle", -1, 2),
        Among("-t-en", -1, 5),
        Among("-t-i'", -1, 1),
        Among("-y", -1, 6)
    ]


class lab0(BaseException): pass


class lab1(BaseException): pass


class lab2(BaseException): pass


class lab3(BaseException): pass


class lab4(BaseException): pass


class lab5(BaseException): pass

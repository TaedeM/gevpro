import cdb
import wordsearch


class TestCDB:
    def test_adjectives_1(self):
        adjectives = list(cdb.get_adjectives('cdb-sample.xml'))
        assert len(adjectives) == 132
        assert set(adjectives) == {
            '', 'steriel', 'romantisch', 'opgemaakt', 'aanstaande',
            'vleselijk', 'beter', 'ijzig', 'praktisch', 'vlezig', 'onzijdig',
            'tweeslachtig', 'lam', 'flauw', 'glashelder', 'ontrouw',
            'onvruchtbaar', 'disponibel', 'uit', 'kapot', 'centraal', 'lekker',
            'ongebonden', 'onnatuurlijk', 'gevestigd', 'gewijd', 'stekelig',
            'gewoon', 'zat', 'onbeperkt', 'ver', 'heilzaam', 'glazig',
            'onbuigbaar', 'ongewoon', 'ongemakkelijk', 'bijzonder', 'gesloten',
            'rein', 'proper', 'onhoudbaar', 'vruchtbaar', 'naar', 'dol',
            'geraffineerd', 'bezet', 'finaal', 'lokaal', 'pittig',
            'beschikbaar', 'polair', 'bezeten', 'vrij', 'heerlijk', 'algemeen',
            'werelds', 'wrang', 'zindelijk', 'gekleurd', 'beroerd', 'gaar',
            'zuiver', 'berekend', 'plastisch', 'goed', 'progressief',
            'verplicht', 'hysterisch', 'scheef', 'verward', 'driftig',
            'solide', 'temporeel', 'raak', 'onfeilbaar', 'traag', 'vervallen',
            'fenomenaal', 'onwaarschijnlijk', 'link', 'respectabel', 'best',
            'historisch', 'handig', 'week', 'ongelijk', 'verzadigd',
            'verbonden', 'genadig', 'broos', 'links', 'ecologisch',
            'rekkelijk', 'gedekt', 'overjarig', 'kokend', 'onbeschaafd',
            'plaatselijk', 'onbedekt', 'nietig', 'onbekwaam', 'nodig', 'down',
            'krampachtig', 'klein', 'makkelijk', 'redelijk', 'ellendig',
            'gezwollen', 'gering', 'vet', 'publiek', 'alleenstaand',
            'statisch', 'intiem', 'abnormaal', 'simpel', 'verdacht',
            'verdraaid', 'rijk', 'rechteloos', 'rot', 'slijmerig',
            'onaanzienlijk', 'stroef', 'elektrisch', 'onontwikkeld', 'afkerig',
            'solidair', 'automatisch', 'vergevensgezind', 'speculatief'}


class TestWordSearch:
    def test_wordsearch_1(self):
        words = list(wordsearch.solve('puzzle1.txt', 'words.json'))
        assert len(words) == 2
        assert set(words) == {'KLAK', 'MELK'}

    def test_wordsearch_2(self):
        words = list(wordsearch.solve('puzzle2.txt', 'words.json'))
        assert len(words) == 27
        assert set(words) == {
            'OVER', 'VIER', 'RAIO', 'NFWO', 'KAAS', 'GETROFFEN', 'NEGEN',
            'TIEN', 'ZONNEBRIL', 'BRIL', 'GALMEN', 'GALM', 'MENISCUS',
            'NAGALMEN', 'BABYUITZET', 'BABY', 'UITZET', 'OMNIBUS', 'STIL',
            'STILTE', 'AFFAIRE', 'FAIR', 'ZEKER', 'HERSENS', 'EDEL', 'EDELE',
            'BEDSTEDE'}

    def test_advanced_wordsearch_1(self):
        words = list(wordsearch.solve('puzzle1.txt', 'words.json', 'True'))
        assert len(words) == 9
        assert set(words) == {
            'KALK', 'INAS', 'KLAK', 'KOFFIE', 'MELK', 'KLEM', 'SINAS',
            'WATER', 'CASSIS'
        }

    def test_advanced_wordsearch_2(self):
        words = list(wordsearch.solve('puzzle2.txt', 'words.json', 'True'))
        assert len(words) == 32
        assert set(words) == {
            'NEER', 'BABYUITZET', 'GALMEN', 'RAIO', 'SLEE', 'VIER', 'NFWO',
            'NAGALMEN', 'OMNIBUS', 'STIL', 'EDEL', 'KAAS', 'GALM', 'ZEKER', 
            'GETROFFEN', 'OVER', 'NEGEN', 'AFFAIRE', 'FAIR', 'HERSENS', 
            'RITS', 'FORT', 'BRIL', 'MENISCUS', 'BABY', 'ZONNEBRIL', 
            'EDELE', 'TIEN', 'BEDSTEDE', 'KLEI', 'STILTE', 'UITZET'
        }
        
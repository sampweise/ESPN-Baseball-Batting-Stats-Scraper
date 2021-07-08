class Team_Names:
    Teams = {
    'KC'  : '/kc',
    'CHW' : '/chw',
    'CLE' : '/cle',
    'DET' : '/det',
    'MIN' : '/min',
    'BAL' : '/bal',
    'BOS' : '/bos',
    'NYY' : '/nyy',
    'TB'  : '/tb',
    'TOR' : '/tor',
    'HOU' : '/hou',
    'LAA' : '/laa',
    'OAK' : '/oak',
    'SEA' : '/sea',
    'TEX' : '/tex',
    'ATL' : '/atl',
    'MIA' : '/mia',
    'NYM' : '/nym',
    'PHI' : '/phi',
    'WSH' : '/wsh',
    'CHC' : '/chc',
    'CIN' : '/cin',
    'MIL' : '/mil',
    'PIT' : '/pit',
    'STL' : '/stl',
    'ARI' : '/ari',
    'COL' : '/col',
    'LAD' : '/lad',
    'SD' : '/sd',
    'SF' : '/sf',
    }

    @staticmethod
    def check_names(name):
        for check in Team_Names.Teams:
            if (name == check):
                return True
        return False

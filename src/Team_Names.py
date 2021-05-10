class Team_Names:
    Teams = {
    'KC'  : '/kc',
    'CHW' : '/chw',
    'CLE' : '/cle',
    'DET' : '/det',
    'MIN' : '/min'
    }

    @staticmethod
    def check_names(name):
        for check in Team_Names.Teams:
            if (name == check):
                return True
        return False
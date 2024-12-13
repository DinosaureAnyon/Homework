file = 'NISPUF17.csv'


def chickenpox_by_sex(file):
    df = pd.read_csv(file, sep=',')
    count_male = len(df.query('(HAD_CPOX <= 2) and (SEX == 1) and (P_NUMPCV > 0)').dropna(
        subset=['HAD_CPOX', 'SEX', 'P_NUMPCV']))
    count_male_not_sick = len(df.query('(HAD_CPOX == 2) and (SEX == 1) and (P_NUMPCV > 0)').dropna(
        subset=['HAD_CPOX', 'SEX', 'P_NUMPCV']))
    count_female = len(df.query('(HAD_CPOX <= 2) and (SEX == 2) and (P_NUMPCV > 0)').dropna(
        subset=['HAD_CPOX', 'SEX', 'P_NUMPCV']))
    count_female_not_sick = len(df.query('(HAD_CPOX == 2) and (SEX == 2) and (P_NUMPCV > 0)').dropna(
        subset=['HAD_CPOX', 'SEX', 'P_NUMPCV']))
    vaccine_effectiveness = {'male': round(count_male_not_sick/count_male, 2),
                             'female': round(count_female_not_sick/count_female, 2)}
    print(vaccine_effectiveness)


chickenpox_by_sex(file)
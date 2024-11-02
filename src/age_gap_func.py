
def age_gap_func(dating_df) :
    
    # age_gap_func의 내부 함수
    def age_func(x) :
        if x['age'] == -99 :
            return -99
        elif x['age_o'] == -99 :
            return -99
        elif x['gender'] == 'female' :
            return x['age_o'] - x['age']
        else :
            return x['age'] - x['age_o']
    
    dating_df['age_gap'] = dating_df.apply(age_func, axis = 1)
    # 저 나이차가 음 , 양 수 판단 후 새 컬럼 추가
    dating_df['age_gap_dir']=dating_df['age_gap'].apply(lambda x:'positive' if x>0 else 'negative' if x < 0 else 'zero') # 두번째 if 는 else negative 소속 if
     # age_gap에 절대 값 씌움
    dating_df['age_gap']=abs(dating_df['age_gap'])
    
    return dating_df         

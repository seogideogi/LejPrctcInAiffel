
def race_func(dating_df) :
    
    dating_df['same_race']=(dating_df['race'] == dating_df['race_o'] ).astype('int') # 위 True , False 인티저로 바꾸기
    # 0을 -1 로 변환하자
    dating_df['same_race'] = dating_df['same_race'].replace({ 0 : -1})
    # 위 다시 계산
    dating_df['same_race_point']=dating_df['same_race'] * dating_df['importance_same_race']
    
    return dating_df      

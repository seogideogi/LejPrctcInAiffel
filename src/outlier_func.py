
def outlier_func( dating_df ) :
    # ~score~ 컬럼은 모두 10 기준으로 데이터 변경
    # dating_df['o_score_attractive'] = dating_df['o_score_attractive'].apply(lambda x:10 if x> 10 else x )
    
    o_score = []
    i_score = []
    
    for i in dating_df.columns :
        if i.startswith('o_score'):
            o_score.append(i)
        elif i.startswith('i_score'):
            i_score.append(i)
    
    ## 넣어 준것 적용 하기
    for i in o_score :
        dating_df[i] = dating_df[i].apply(lambda x:10 if x> 10 else x )
        
    for i in i_score :
        dating_df[i] = dating_df[i].apply(lambda x:10 if x> 10 else x )
    
    return dating_df

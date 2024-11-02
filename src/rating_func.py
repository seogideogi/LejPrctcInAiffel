
def rating_func(dating_df) :
    
    # 컬럼 이름 모으기
    o_important = []
    o_score = []
    i_important = []
    i_score = []

    for i in dating_df.columns :
        if i.startswith('o_important') :
            o_important.append(i)
        elif i.startswith('o_score') :
            o_score.append(i) 
        elif i.startswith('i_important') :
            i_important.append(i)
        elif i.startswith('i_score') :
            i_score.append(i)
    
    # 중요치 않아서 0을 준 경우. -99로 대체하기
    dating_df[o_important] = dating_df[o_important].replace({ 0 : -99})
    dating_df[i_important] = dating_df[i_important].replace({ 0 : -99})
    
    # rating_func 내부 함수
    def rating(data, important , score) :
        if data[score] == -99 :
            return -99
        elif data[important] == -99 :
            return -99
        else :
            return data[important] * data[score]
    
    #### ####  for loop 돌면서 rating 적용 하기 전 추가 될 컬럼 이름 리스트 지정하기 () editplus  등에서 한꺼번에 바꾸기 해
    o_rating = ['o_rating_attractive',
     'o_rating_sincere',
     'o_rating_intelligence',
     'o_rating_funny',
     'o_rating_ambitious',
     'o_rating_shared_interests']

    i_rating = [
       'i_rating_attractive',
     'i_rating_sincere',
     'i_rating_intellicence',
     'i_rating_funny',
     'i_rating_ambtition',
     'i_rating_shared_interests'   
    ]
    
    ####  for loop 돌면서 rating 적용 하기
    for i, j, k in zip(o_important, o_score, o_rating) :
        dating_df[k] = dating_df.apply(lambda x : rating(x, i, j) , axis = 1)
        
    ### 나의 평가에도 적용 해 주기
    ####  for loop 돌면서 rating 적용 하기
    for i, j, k in zip(i_important, i_score, i_rating) :
        dating_df[k] = dating_df.apply(lambda x : rating(x, i, j) , axis = 1)
    
    ## 평균 구하되, -99 제외 되도록 하기
    dating_df ['o_rating_total'] = dating_df[o_rating].apply(lambda x : x[x > 0].mean(), axis=1 )
    dating_df ['i_rating_total'] = dating_df[i_rating].apply(lambda x : x[x > 0].mean(), axis=1 )

    ## 조합평균 적용
    dating_df['rating_mean'] = 2 * dating_df['o_rating_total'] * dating_df['i_rating_total'] / (dating_df['o_rating_total'] + dating_df['i_rating_total'])
    
    return dating_df    

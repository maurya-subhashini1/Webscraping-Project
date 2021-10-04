from task_1 import sracp_movie
from task_2 import group_by_year
import pprint


import json
scrape_top_list=sracp_movie()
dec_arg=group_by_year(scrape_top_list)
def group_by_decade(movie):
    movie_iedec={}
    list1=[]
    for index in movie:
        Mod=index%10
        decade=index-Mod
        if decade not in list1:
            list1.append(decade)
    list1.sort()
    for i in list1:
        movie_iedec[i]=[]
    for i in movie_iedec:
        dec10=i+9
        for x in movie:
            if x <=dec10 and x>=i:
                for v in movie[x]:
                    movie_iedec[i].append(v)
    with open("movie.json","w")as h:
        json.dump(movie_iedec,h,indent=5)
    return movie_iedec
group_by_decade(dec_arg)

import json
import facebook
import requests

def get_basic_info(graph):


    profile = graph.get_object('me',fields='first_name,last_name,location,link,email')	

    print(json.dumps(profile, indent=5))

def get_all_posts(graph):

    posts = graph.request('/me/posts')
    count=1
    while "paging" in posts: 
        print("length of the dictionary",len(posts))
        print("length of the data part",len(posts['data']))
        for post in posts["data"]:
            print(count,"\n")
            if "message" in post:
                print(post["message"])
            print("time :  ",post["created_time"])
            print("id   :",post["id"],"\n\n")
            count=count+1

        #post2=graph.request(posts["paging"]["next"])
        posts=requests.get(posts["paging"]["next"]).json()
        
    print("end of posts")
        

def authentication():
    
    f = open("token.txt", "r")
    f1=[]
    for x in f:
        f1.append(x.rstrip())
    token=f1[0]
    graph = facebook.GraphAPI(token)
    return graph
    
def main():

    graph=authentication()
    
    #get_basic_info(graph)
    get_all_posts(graph)



if __name__ == '__main__':

    main()
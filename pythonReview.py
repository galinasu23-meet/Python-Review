

def create_youtube_video(title, description, hashtag):
	video = {"title":title, "description":description, "likes":0, "dislikes": 0, "comments": {}, "hashtag":hashtag }
	return video

def like(vid):
	if "likes" in vid:
			vid["likes"]+=1
	return vid

def dislike(vid):
	if "dislikes" in vid:
		vid["dislikes"]+=1
	return vid

def add_comment(youtubevideo, username, comment_text):
	youtubevideo["comments"][username]= "comment_text"
	return youtubevideo

newvideo = create_youtube_video("Guys I Just Got Kidnapped!!!", "PLS SEND HELP",["#kidnapping", "sad", "#help", "#sendhelp", "#viral" ])
add_comment(newvideo,"gali","same broooo")
for i in range(495):
	like(newvideo)

newvideo2 = create_youtube_video("kidnapping tutorial!!", "learn the best ways to Kidnap",["#kidnapping", "happy", "#tips", "#sendlove", "#viral" ])
add_comment(newvideo,"gali","same broooo")
for i in range(630):
	like(newvideo2)

def similarity_to_video (a,b):
	counter = 0
	for i in a:
		if a[i]==b[i]:
			counter +=1
	precent = counter/len(b)
	print ("the precent of similarity of", a["title"], "and",  b["title"], "is", precent* 100.0)
similarity_to_video (newvideo,newvideo2)



print (newvideo["likes"],newvideo2["likes"])




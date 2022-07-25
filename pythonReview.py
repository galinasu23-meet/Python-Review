

def create_youtube_video(title,description):
	video = {"title":title, "description":description, "likes":0, "dislikes": 0, "comments": {}}
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

newvideo = create_youtube_video("Guys I Just Got Kidnapped!!!", "PLS SEND HELP")
add_comment(newvideo,"gali","same broooo")
for i in range(495):
	like(newvideo)

print (newvideo["likes"])




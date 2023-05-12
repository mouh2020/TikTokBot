base_xpath = "/html/body/div[2]/div[2]/div[2]/div[1]/"

def video_author_xpath(video_number) :
    return f"{base_xpath}div[{video_number}]/div/div[1]/div[1]/a[2]/h3"
def video_caption_xpath(video_number) : 
    return f"{base_xpath}div[{video_number}]/div/div[1]/div[2]/div/div[2]/div"
def video_music_xpath(video_number) : 
    return f"{base_xpath}div[{video_number}]/div/div[1]/h4/a"
def follow_author_button_xpath(video_number) : 
    return f"{base_xpath}div[{video_number}]/div/div[1]/button"
def search_field_xpath() :
    return "/html/body/div[2]/div[1]/div/div[2]/div/form/input"
def follow_user_button_xpath() : 
    return "/html/body/div[2]/div[2]/div[2]/div/div[1]/div[1]/div[2]/div/div[1]/button"
def user_username_xpath():
    return "/html/body/div[2]/div[2]/div[2]/div/div[1]/div[1]/div[2]/h2"
def user_name_xpath() : 
    return "/html/body/div[2]/div[2]/div[2]/div/div[1]/div[1]/div[2]/h1"
def like_video_xpath() : 
    return "g:nth-child(1) > g > .png:nth-child(3) path"
def comment_video_xpath():
    return "/html/body/div[2]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[1]/div[4]/div/button[2]/span/div/div/svg"
    

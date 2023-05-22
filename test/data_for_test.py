from yt_concate.model.yt import YT
from yt_concate.model.found import Found

# 5 URL list
sample_url = ['https://www.youtube.com/watch?v=_QNBdW8ZPB4',
              'https://www.youtube.com/watch?v=_zRP8CyTerY',
              'https://www.youtube.com/watch?v=_SB7h2kB6Eg',
              'https://www.youtube.com/watch?v=7ROkCm4T_Lk',
              'https://www.youtube.com/watch?v=Zd7s5A9Xdok',
              ]

# 3 YT object list
yt_list = [YT('https://www.youtube.com/watch?v=QlI0bxcIAeQ'),
           YT('https://www.youtube.com/watch?v=Ez0EX3mKRBQ'),
           YT('https://www.youtube.com/watch?v=ttwDb1PWrD0'),
           ]

# 3 videos' captions in below by 2 layers dictionary
caption_list = {'_QNBdW8ZPB4.en.srt': {'listen to that': '00:07:58,560 --> 00:08:04,790', 'you gotta see this ready': '00:00:06,480 --> 00:00:10,790', 'wait for it': '00:00:10,800 --> 00:00:17,269', "there's a little wing on the roof": '00:00:17,279 --> 00:00:19,269', 'how freaking cool is that all right': '00:00:19,279 --> 00:00:20,870', "round here there's a secret button here": '00:00:20,880 --> 00:00:23,990', "and you've got to push the front of it": '00:00:24,000 --> 00:00:25,589', "look look how that's embedded ready": '00:00:25,599 --> 00:00:29,589', 'door goes out': '00:00:29,599 --> 00:00:35,670', 'now you have wings': '00:00:35,680 --> 00:00:37,990', 'on the top of your car how cool is this': '00:00:38,000 --> 00:00:39,990', 'this is the brand new': '00:00:40,000 --> 00:00:41,990', 'buick': '00:00:42,000 --> 00:00:43,030', "wildcat and i'm going to show you the": '00:00:43,040 --> 00:00:44,630', 'coolest features': '00:00:44,640 --> 00:00:46,410', '[Music]': '00:09:07,670 --> 00:09:15,030', 'wild cat here it is on the back why is': '00:00:58,160 --> 00:01:00,709', 'it called wildcat this name is reserved': '00:01:00,719 --> 00:01:04,229', 'for buicks concept cars these are the': '00:01:04,239 --> 00:01:07,109', 'cars that show the future of buick so': '00:01:07,119 --> 00:01:10,070', 'all of the cool design features that': '00:01:10,080 --> 00:01:12,390', "we're going to see in the real": '00:01:12,400 --> 00:01:13,510', "production cars coming out so i'm going": '00:01:13,520 --> 00:01:15,030', 'to show you a few of those first of all': '00:01:15,040 --> 00:01:16,870', 'right here look at this this is a brand': '00:01:16,880 --> 00:01:18,950', 'new buick logo the circle is gone the': '00:01:18,960 --> 00:01:22,550', 'like classic shield cutting through is': '00:01:22,560 --> 00:01:24,550', 'gone this is actually going to come out': '00:01:24,560 --> 00:01:26,950', 'in real buicks in 2023. i say real': '00:01:26,960 --> 00:01:30,550', "buicks like this isn't a real": '00:01:30,560 --> 00:01:32,469', "it's a real car like we're going to": '00:01:32,479 --> 00:01:34,149', 'drive it in a minute but you know what i': '00:01:34,159 --> 00:01:35,590', 'mean actual production models right': '00:01:35,600 --> 00:01:37,510', 'around here i absolutely love this look': '00:01:37,520 --> 00:01:40,230', 'at this look at these tail lights how': '00:01:40,240 --> 00:01:42,230', 'they go all the way': '00:01:42,240 --> 00:01:44,230', 'up the back': '00:01:44,240 --> 00:01:46,149', 'of the rear windscreen i have never seen': '00:01:46,159 --> 00:01:48,950', 'that before i absolutely love that okay': '00:01:48,960 --> 00:01:51,590', 'now around here another favorite feature': '00:01:51,600 --> 00:01:53,990', 'of mine check out these wheels look at': '00:01:54,000 --> 00:01:56,469', 'this how freaking cool do they look 18': '00:01:56,479 --> 00:01:59,830', 'spoke 22 inch wheels and here look': '00:01:59,840 --> 00:02:05,590', 'you got a little': '00:02:05,600 --> 00:02:07,270', 'surprise wheels are spinning spinning': '00:02:07,280 --> 00:02:09,749', 'see this is the kind of detail the go-to': '00:02:09,759 --> 00:02:11,910', 'guys when it comes to design they have': '00:02:11,920 --> 00:02:14,309', 'custom made tires and the tread even the': '00:02:14,319 --> 00:02:17,190', 'tread like these marks you see here': '00:02:17,200 --> 00:02:19,430', "that's designed": '00:02:19,440 --> 00:02:21,190', 'like they could have made that design': '00:02:21,200 --> 00:02:22,790', "anything but they're like nope we want": '00:02:22,800 --> 00:02:24,390', "this one so that's the kind of detail": '00:02:24,400 --> 00:02:26,390', 'that goes into a concept car like this': '00:02:26,400 --> 00:02:28,550', "and they're going right what do we want": '00:02:28,560 --> 00:02:30,229', "for the future of buick let's put it all": '00:02:30,239 --> 00:02:32,070', 'in this car now around the front again': '00:02:32,080 --> 00:02:34,550', "you've got the coolest headlights here": '00:02:34,560 --> 00:02:37,190', 'and': '00:04:07,760 --> 00:04:12,149', 'i love the way that these light up as': '00:02:37,920 --> 00:02:40,630', 'you approach the car and when you lock': '00:02:40,640 --> 00:02:43,190', "the car we're going to show you that in": '00:02:43,200 --> 00:02:44,710', 'the shade just to show you how special': '00:02:44,720 --> 00:02:46,630', 'that light sequence is love okay now': '00:02:46,640 --> 00:02:49,270', 'around here this front grille here is': '00:02:49,280 --> 00:02:51,589', "also another design feature we're gonna": '00:02:51,599 --> 00:02:53,830', 'see on production model buicks in future': '00:02:53,840 --> 00:02:56,790', 'so look out for that okay guys so': '00:02:56,800 --> 00:02:59,509', "here's the deal this is the first time": '00:02:59,519 --> 00:03:01,350', 'we are featuring a buick on the supercar': '00:03:01,360 --> 00:03:03,509', 'blondie channel what is buick just': '00:03:03,519 --> 00:03:05,750', "really quickly it's a premium car brand": '00:03:05,760 --> 00:03:08,309', 'under gm and their goal is to become': '00:03:08,319 --> 00:03:10,949', 'fully electric by 2030. this is a full': '00:03:10,959 --> 00:03:14,869', 'ev': '00:03:14,879 --> 00:03:15,910', "concept and you've got this as well look": '00:03:15,920 --> 00:03:18,390', 'something called ultra cruise now this': '00:03:18,400 --> 00:03:21,350', 'is a level two autonomous driving system': '00:03:21,360 --> 00:03:24,390', "that they're going to be rolling out": '00:03:24,400 --> 00:03:26,149', 'which basically means that you can drive': '00:03:26,159 --> 00:03:29,430', 'this car on say like 98': '00:03:29,440 --> 00:03:32,949', 'of roads around america you know with': '00:03:32,959 --> 00:03:35,509', "like autonomous systems that aren't as": '00:03:35,519 --> 00:03:37,910', 'great you can be hands-free on the road': '00:03:37,920 --> 00:03:41,350', 'but only on highways as soon as you take': '00:03:41,360 --> 00:03:43,350', 'that road off the highway it kind of': '00:03:43,360 --> 00:03:44,949', "paddocks it's like where are we it": '00:03:44,959 --> 00:03:47,110', 'freaks out this one is not going to do': '00:03:47,120 --> 00:03:48,869', 'that so this one will go through all': '00:03:48,879 --> 00:03:50,390', 'your suburbs etc so this is going to be': '00:03:50,400 --> 00:03:52,229', 'rolled out in buick cars in a few years': '00:03:52,239 --> 00:03:55,110', 'time and of course because buick is on': '00:03:55,120 --> 00:03:56,869', "the gm you're going to see some of the": '00:03:56,879 --> 00:03:58,470', 'same technology rolled out in their': '00:03:58,480 --> 00:04:01,110', "other brands right let's go in let's see": '00:04:01,120 --> 00:04:04,229', 'the interior so again we push here': '00:04:04,239 --> 00:04:07,750', "the interior is revealed and i've been": '00:04:12,159 --> 00:04:14,869', "told i'm the only person outside of gm": '00:04:14,879 --> 00:04:17,590', 'to be allowed to sit in this and': '00:04:17,600 --> 00:04:19,110', 'actually drive it which is so fantastic': '00:04:19,120 --> 00:04:21,670', 'thank you guys so much all right now': '00:04:21,680 --> 00:04:23,189', 'come check this out here we have': '00:04:23,199 --> 00:04:25,830', 'the incredible interior i just love how': '00:04:25,840 --> 00:04:27,830', 'long this door is as well just look at': '00:04:27,840 --> 00:04:30,070', "the size of this thing incredible you've": '00:04:30,080 --> 00:04:32,550', 'got your side camera view here as well': '00:04:32,560 --> 00:04:35,110', 'so that corresponds to this camera here': '00:04:35,120 --> 00:04:37,670', "there's just so much space": '00:04:37,680 --> 00:04:39,749', 'because of course this is an ev now': '00:04:39,759 --> 00:04:41,749', 'right': '00:04:41,759 --> 00:04:42,390', "so you don't need all of this": '00:04:42,400 --> 00:04:45,030', 'kind of center': '00:04:45,040 --> 00:04:46,469', 'block between you and the passenger seat': '00:04:46,479 --> 00:04:48,710', 'so this is all open this is floating and': '00:04:48,720 --> 00:04:51,110', 'then all of this here is floating as': '00:04:51,120 --> 00:04:53,030', 'well you see you can put your hand': '00:04:53,040 --> 00:04:54,790', "behind here there's all this space here": '00:04:54,800 --> 00:04:56,629', "in the back now what's cool is this is": '00:04:56,639 --> 00:04:59,189', "what we're going to see in future buicks": '00:04:59,199 --> 00:05:01,909', 'this whole new redesigned screen look': '00:05:01,919 --> 00:05:04,150', "it's a curved screen it's quite long": '00:05:04,160 --> 00:05:06,390', 'and this right here': '00:05:06,400 --> 00:05:08,870', 'is going to be taken pretty much from': '00:05:08,880 --> 00:05:11,110', 'this car and put in buick models so': '00:05:11,120 --> 00:05:13,749', "that's quite cool to see and then here": '00:05:13,759 --> 00:05:15,670', "you've got this beautiful center console": '00:05:15,680 --> 00:05:18,150', 'stretching all the way from the front': '00:05:18,160 --> 00:05:20,950', 'into the back there and then these seats': '00:05:20,960 --> 00:05:24,629', 'as you can see here these are like': '00:05:24,639 --> 00:05:26,310', 'floating do you see that': '00:05:26,320 --> 00:05:28,230', 'everything in the interior is about': '00:05:28,240 --> 00:05:30,350', 'floating these kind of materials of': '00:05:30,360 --> 00:05:33,270', "course they're looking into being more": '00:05:33,280 --> 00:05:35,189', 'sustainable in future so this is': '00:05:35,199 --> 00:05:36,710', 'actually from old yarn so recycled yarn': '00:05:36,720 --> 00:05:39,590', "that they've done this fabric and up": '00:05:39,600 --> 00:05:41,749', "here you've got a little easter egg look": '00:05:41,759 --> 00:05:43,830', 'at this': '00:05:43,840 --> 00:05:44,870', 'a little wild cat up here just to remind': '00:05:44,880 --> 00:05:47,830', "you what you're in i really like this": '00:05:47,840 --> 00:05:49,749', 'this is acrylic': '00:05:49,759 --> 00:05:51,189', 'and it just makes it look a little bit': '00:05:51,199 --> 00:05:52,629', 'futuristic all these acrylic features': '00:05:52,639 --> 00:05:54,629', 'here quite a thin steering wheel which': '00:05:54,639 --> 00:05:56,870', 'is cool and when you move it': '00:05:56,880 --> 00:05:59,189', 'the center badge stays stationary what': '00:05:59,199 --> 00:06:02,870', 'do you guys think in the interior': '00:06:02,880 --> 00:06:04,469', 'alright we have a special guest': '00:06:04,479 --> 00:06:06,469', 'sharon from australia actually come in': '00:06:06,479 --> 00:06:08,710', 'come in aussie buddies sharon is the': '00:06:08,720 --> 00:06:11,189', 'executive director of design at buick': '00:06:11,199 --> 00:06:13,830', "and gmc and we're going to talk about": '00:06:13,840 --> 00:06:16,309', "the interior com come around let's have": '00:06:16,319 --> 00:06:18,070', "a look i haven't said anything about the": '00:06:18,080 --> 00:06:19,830', 'color yet so why did you guys choose the': '00:06:19,840 --> 00:06:22,150', "green and the white and what's going on": '00:06:22,160 --> 00:06:24,309', 'so what i love about this interior is': '00:06:24,319 --> 00:06:27,110', 'the fact that there are so many elements': '00:06:27,120 --> 00:06:29,350', "that that float we've got": '00:06:29,360 --> 00:06:31,270', 'a panel that floats the seats that are': '00:06:31,280 --> 00:06:33,189', "floating this beautiful console that's": '00:06:33,199 --> 00:06:35,670', 'floating and the color and trim really': '00:06:35,680 --> 00:06:37,990', 'does speak to': '00:06:38,000 --> 00:06:39,590', 'emphasizing those floating elements so': '00:06:39,600 --> 00:06:41,830', 'everything in white really speaks to': '00:06:41,840 --> 00:06:43,510', "everything that's floating it's grounded": '00:06:43,520 --> 00:06:45,749', "with this really rich green that we've": '00:06:45,759 --> 00:06:47,909', "called legato green yeah it's beautiful": '00:06:47,919 --> 00:06:49,990', "it's gorgeous it's like a forest yeah i": '00:06:50,000 --> 00:06:52,469', "mean it's really rich it's beautiful": '00:06:52,479 --> 00:06:54,469', "it's deep and actually in photography it": '00:06:54,479 --> 00:06:56,309', "doesn't show up so well but in person": '00:06:56,319 --> 00:06:59,510', "it's just an exquisite green and the": '00:06:59,520 --> 00:07:02,550', 'exterior color which is this very deep': '00:07:02,560 --> 00:07:06,230', 'metallic mid-value gray really does': '00:07:06,240 --> 00:07:08,870', 'highlight all of the beautiful': '00:07:08,880 --> 00:07:11,110', "custom aluminum work so it's just": '00:07:11,120 --> 00:07:13,589', 'stunning so these bits is here as well': '00:07:13,599 --> 00:07:15,909', 'sharing the acrylic why use that': '00:07:15,919 --> 00:07:18,790', 'so again you know the design team paid a': '00:07:18,800 --> 00:07:21,189', 'lot of attention to detail': '00:07:21,199 --> 00:07:23,270', 'all the elements have been designed and': '00:07:23,280 --> 00:07:25,270', 'the acrylic was just another way to': '00:07:25,280 --> 00:07:27,589', 'bring in': '00:07:27,599 --> 00:07:28,790', "an element that's really rich and really": '00:07:28,800 --> 00:07:30,790', "beautiful and deep all right we're going": '00:07:30,800 --> 00:07:32,469', "to see this in motion now there's": '00:07:32,479 --> 00:07:33,830', 'something special about seeing concept': '00:07:33,840 --> 00:07:35,510', "cars drive that's what we're going to do": '00:07:35,520 --> 00:07:37,749', 'now look at this this is how you close': '00:07:37,759 --> 00:07:39,270', 'the door from the inside with this': '00:07:39,280 --> 00:07:41,270', 'little button here all right ready here': '00:07:41,280 --> 00:07:44,309', 'we go': '00:07:44,319 --> 00:07:53,830', "sounds quite cool doesn't it": '00:07:53,840 --> 00:07:58,550', 'hey hey': '00:08:04,800 --> 00:08:07,270', 'oh look at this': '00:08:07,280 --> 00:08:09,110', 'how cool does this look and look at all': '00:08:09,120 --> 00:08:11,270', 'these lights here in the center console': '00:08:11,280 --> 00:08:13,029', 'all of this lights up': '00:08:13,039 --> 00:08:14,629', 'oh': '00:08:14,639 --> 00:08:15,510', "i love concept cars why can't they just": '00:08:15,520 --> 00:08:17,510', 'come to life': '00:08:17,520 --> 00:08:18,869', 'why': '00:08:18,879 --> 00:08:20,150', "and look look how i'm turning the wheel": '00:08:20,160 --> 00:08:21,749', 'in this stay center': '00:08:21,759 --> 00:08:28,790', 'here we go here we go here we go': '00:08:28,800 --> 00:08:30,550', 'listen to that sound': '00:08:30,560 --> 00:08:34,709', 'oh what do you guys reckon': '00:08:34,719 --> 00:08:37,909', 'and there we go one of the fastest': '00:08:37,919 --> 00:08:40,070', "drives i've ever done": '00:08:40,080 --> 00:08:42,310', 'just want to say a massive thank you to': '00:08:42,320 --> 00:08:44,630', 'buick for organizing this i am so lucky': '00:08:44,640 --> 00:08:47,990', 'to get my hands on this and to show you': '00:08:48,000 --> 00:08:50,310', "guys on this channel really it's": '00:08:50,320 --> 00:08:52,710', 'incredible so a massive thank you to you': '00:08:52,720 --> 00:08:54,710', "guys and that's it make sure you like": '00:08:54,720 --> 00:08:56,630', 'the video subscribe to the channel and': '00:08:56,640 --> 00:08:58,710', "uh we'll see you next time we've got": '00:08:58,720 --> 00:09:00,790', 'some crazy stuff happening': '00:09:00,800 --> 00:09:02,630', "bye i'm out": '00:09:02,640 --> 00:09:07,660', 'you': '00:09:15,040 --> 00:09:17,120'},
'_SB7h2kB6Eg.en.srt': {"i'm here at a top secret location to see": '00:00:00,160 --> 00:00:03,750', 'a car that the world has never seen': '00:00:03,760 --> 00:00:05,590', 'before': '00:00:05,600 --> 00:00:09,430', 'okay all right all right come on in': '00:00:09,440 --> 00:00:20,550', 'go': '00:00:20,560 --> 00:00:26,550', 'you think it only exists online it': '00:00:26,560 --> 00:00:28,550', "doesn't": '00:00:28,560 --> 00:00:38,150', 'okay': '00:00:50,399 --> 00:00:57,750', 'all right': '00:00:45,680 --> 00:00:50,389', 'side view': '00:00:57,760 --> 00:01:09,350', 'that might give you a hint': '00:01:09,360 --> 00:01:15,429', "don't look in there it gives too much": '00:01:15,439 --> 00:01:16,950', 'away': '00:01:16,960 --> 00:01:22,310', 'where do you want to look from front': '00:01:22,320 --> 00:01:24,149', 'yeah': '00:09:54,000 --> 00:09:54,870', "holy ah this is the first time i'm": '00:01:26,479 --> 00:01:29,270', 'seeing it in real life you guys': '00:01:29,280 --> 00:01:31,670', "same as you we're getting this moment": '00:01:31,680 --> 00:01:33,510', 'together': '00:01:33,520 --> 00:01:34,710', 'by the way': '00:01:34,720 --> 00:01:36,310', 'welcome to the supercar vlog': '00:01:36,320 --> 00:01:39,190', 'subscribe': '00:01:39,200 --> 00:01:42,069', 'ready': '00:01:42,079 --> 00:01:43,590', 'oh': '00:01:43,600 --> 00:01:45,670', 'wow what oh my goodness': '00:01:45,680 --> 00:01:49,670', 'oh what': '00:01:49,680 --> 00:01:52,850', '[Music]': '00:10:24,470 --> 00:10:38,470', 'oh my god you guys': '00:01:54,399 --> 00:01:56,709', 'oh my god': '00:02:09,759 --> 00:02:11,750', 'we got to get this thing off the truck': '00:01:59,360 --> 00:02:00,550', 'so you can see what i see': '00:02:00,560 --> 00:02:02,630', 'this is madness': '00:02:02,640 --> 00:02:09,749', 'what': '00:02:11,760 --> 00:02:14,790', 'holy moly': '00:02:14,800 --> 00:02:18,550', "i'm glad i wore my fancy shoes for this": '00:02:18,560 --> 00:02:20,550', 'shoot': '00:02:20,560 --> 00:02:23,270', 'although nothing can on stage this car': '00:02:23,280 --> 00:02:31,990', 'look at that y line on the back': '00:02:32,000 --> 00:02:38,390', 'holy mackerel what are you guys reckon': '00:02:38,400 --> 00:02:41,910', 'is that worth the trip or what this car': '00:02:41,920 --> 00:02:44,150', 'is so delicate': '00:02:44,160 --> 00:02:45,830', "it's going to take a whole team to get": '00:02:45,840 --> 00:02:47,190', 'it off the truck so we can have a better': '00:02:47,200 --> 00:02:48,630', 'look at it but just look at that beast': '00:02:48,640 --> 00:02:52,710', "wow you guys this if you haven't": '00:02:52,720 --> 00:02:55,270', 'recognized it is the lambo v12 vision': '00:02:55,280 --> 00:02:59,589', 'gran turismo': '00:02:59,599 --> 00:03:27,589', 'look how careful they have to be guys': '00:03:27,599 --> 00:03:29,990', 'it comes off 10 centimeters at a time': '00:03:30,000 --> 00:03:32,789', 'you have to keep moving all of these': '00:03:32,799 --> 00:03:34,949', 'boards': '00:03:34,959 --> 00:03:37,509', 'it is super low to the ground': '00:03:37,519 --> 00:03:41,270', "there's only one of these in the world": '00:03:41,280 --> 00:03:42,789', 'so': '00:03:42,799 --> 00:03:44,949', 'i should be super super careful': '00:03:44,959 --> 00:03:47,750', 'obviously': '00:03:47,760 --> 00:03:51,589', 'every few seconds something needs to be': '00:03:51,599 --> 00:03:53,509', 'moved': '00:03:53,519 --> 00:03:54,949', 'when we were starting to film with this': '00:03:54,959 --> 00:03:56,550', "we said okay let's get off the truck": '00:03:56,560 --> 00:03:57,990', 'they said okay see you in one hour': '00:03:58,000 --> 00:04:01,830', "look it hasn't been an hour but it's": '00:04:01,840 --> 00:04:03,350', 'been a good 30 minutes to get it off': '00:04:03,360 --> 00:04:05,030', 'safely': '00:04:05,040 --> 00:04:20,710', "that's a way to get a workout ditch the": '00:04:20,720 --> 00:04:22,550', "gym push off the world's coolest car": '00:04:22,560 --> 00:04:30,570', '[Applause]': '00:04:30,580 --> 00:04:30,850', 'very well done here it is in real life': '00:04:34,160 --> 00:04:36,710', 'you can actually drive this car in the': '00:04:36,720 --> 00:04:39,110', 'game gran turismo but on this channel we': '00:04:39,120 --> 00:04:41,830', 'get to see it in real life': '00:04:41,840 --> 00:04:44,310', 'all right is this not the coolest car': '00:04:44,320 --> 00:04:46,150', "you've ever seen so this is the lambo": '00:04:46,160 --> 00:04:49,670', 'v12': '00:04:49,680 --> 00:04:51,189', 'vision gran turismo': '00:04:51,199 --> 00:04:54,700', "it's called that because it was actually": '00:05:07,840 --> 00:05:09,270', 'made for the game gran turismo the': '00:05:09,280 --> 00:05:12,390', 'ultimate championships in 2019. this is': '00:05:12,400 --> 00:05:15,350', 'of course a concept so this is the only': '00:05:15,360 --> 00:05:17,110', 'one in the world and lamborghini has': '00:05:17,120 --> 00:05:19,350', 'been so awesome': '00:05:19,360 --> 00:05:21,670', 'to actually bring it out for our channel': '00:05:21,680 --> 00:05:24,070', 'today on the supercar blondie channel': '00:05:24,080 --> 00:05:25,510', "thank you so much guys all right let's": '00:05:25,520 --> 00:05:27,110', 'have a look i love these tail lights': '00:05:27,120 --> 00:05:29,590', "isn't that fantastic": '00:05:29,600 --> 00:05:31,270', 'with the': '00:05:31,280 --> 00:05:32,629', 'why lamborghini line': '00:05:32,639 --> 00:05:35,510', "it's just so prominent it takes up the": '00:05:35,520 --> 00:05:37,510', 'whole back wing i love that and then': '00:05:37,520 --> 00:05:40,629', "what i also love you've got these": '00:05:40,639 --> 00:05:42,790', 'hexagonal exhaust tips here but what i': '00:05:42,800 --> 00:05:44,950', 'love is this whole pipe runs all the way': '00:05:44,960 --> 00:05:47,749', 'through and you can see that': '00:05:47,759 --> 00:05:49,510', 'into': '00:05:49,520 --> 00:05:50,870', 'what is': '00:05:50,880 --> 00:05:52,390', 'a naturally aspirated v12 so you see': '00:05:52,400 --> 00:05:55,350', 'this right here': '00:05:55,360 --> 00:05:57,270', 'this': '00:05:57,280 --> 00:05:58,309', 'stands for super capacitor so this drive': '00:05:58,319 --> 00:06:01,350', 'train': '00:06:01,360 --> 00:06:02,390', 'is based on': '00:06:02,400 --> 00:06:04,150', 'the cyan': '00:06:04,160 --> 00:06:05,510', 'so it has the same drivetrain as that': '00:06:05,520 --> 00:06:07,749', 'car that car however is real like you': '00:06:07,759 --> 00:06:10,710', 'can actually drive that car there are 63': '00:06:10,720 --> 00:06:12,710', "of them being produced i've got a video": '00:06:12,720 --> 00:06:14,469', 'coming out on that car as well so make': '00:06:14,479 --> 00:06:16,230', 'sure you subscribe hit it right now guys': '00:06:16,240 --> 00:06:18,150', 'you have to do it i know some of you': '00:06:18,160 --> 00:06:19,990', 'watching right now are not subscribed go': '00:06:20,000 --> 00:06:22,070', 'do it': '00:06:22,080 --> 00:06:23,029', 'do it right now that one is going to be': '00:06:23,039 --> 00:06:24,870', 'on my channel really soon these fenders': '00:06:24,880 --> 00:06:26,950', "here you see how they're separated from": '00:06:26,960 --> 00:06:28,469', 'the body and this is floating': '00:06:28,479 --> 00:06:31,430', 'that is awesome': '00:06:31,440 --> 00:06:33,590', "love love love and as you can see it's a": '00:06:33,600 --> 00:06:35,670', "one seater so the driver's straight in": '00:06:35,680 --> 00:06:37,909', 'the middle there': '00:06:37,919 --> 00:06:39,670', 'and what is also super cool like he just': '00:06:39,680 --> 00:06:41,670', "has a like there's just a head he": '00:06:41,680 --> 00:06:43,990', "doesn't have a body it's just a head and": '00:06:44,000 --> 00:06:46,390', 'then that head is looking at this really': '00:06:46,400 --> 00:06:48,550', "cool digital display everything's being": '00:06:48,560 --> 00:06:50,710', 'projected onto this like glass section': '00:06:50,720 --> 00:06:53,830', "here in the middle you've got the": '00:06:53,840 --> 00:06:55,270', 'special racing suspension': '00:06:55,280 --> 00:07:00,629', "this is so freaking insane isn't that": '00:07:00,639 --> 00:07:02,870', 'you can see all the way through the side': '00:07:02,880 --> 00:07:04,870', "of the car here and then you've got this": '00:07:04,880 --> 00:07:06,710', 'super low front lip all that made out of': '00:07:06,720 --> 00:07:09,909', 'carbon fiber 63 you might be wondering': '00:07:09,919 --> 00:07:13,029', 'why in the world is there a 63 on it': '00:07:13,039 --> 00:07:15,350', 'that is': '00:07:15,360 --> 00:07:16,469', 'to celebrate 63 years since lamborghini': '00:07:16,479 --> 00:07:19,510', 'was founded so this came out 63 years': '00:07:19,520 --> 00:07:21,589', "later which was in 2019 and you've got a": '00:07:21,599 --> 00:07:25,189', 'rose gold tow hook the reason why it was': '00:07:25,199 --> 00:07:27,510', 'made as a one-seater is because of': '00:07:27,520 --> 00:07:29,270', 'course in the game': '00:07:29,280 --> 00:07:31,029', "it's just you driving right you never": '00:07:31,039 --> 00:07:33,110', 'have a passenger with you': '00:07:33,120 --> 00:07:46,020', 'and this actually opens': '00:07:49,520 --> 00:07:52,070', 'like a jet fighter so the whole canopy': '00:07:52,080 --> 00:07:54,309', "opens which is super cool and you've got": '00:07:54,319 --> 00:07:57,029', 'the': '00:07:57,039 --> 00:07:57,749', 'petrol that goes in here the benzene': '00:07:57,759 --> 00:08:00,309', "you've got these beautiful rose gold": '00:08:00,319 --> 00:08:02,150', 'accents here and': '00:08:02,160 --> 00:08:04,309', "on the wheel don't you just love this": '00:08:04,319 --> 00:08:05,830', 'this is beautiful': '00:08:05,840 --> 00:08:16,410', "all right guys let's talk to meteor the": '00:08:24,639 --> 00:08:26,390', "head of design here at lamborghini he's": '00:08:26,400 --> 00:08:28,390', 'responsible for this beast ready': '00:08:28,400 --> 00:08:32,149', 'this is meet you everyone head of': '00:08:32,159 --> 00:08:33,670', "designer at lamborghini uh he's spent": '00:08:33,680 --> 00:08:35,750', 'the last hour just doing little tiny': '00:08:35,760 --> 00:08:37,829', "droplets all over the car it's a fitting": '00:08:37,839 --> 00:08:39,909', 'effect yeah you see that yeah see that': '00:08:39,919 --> 00:08:42,709', 'was part of the design right i think': '00:08:42,719 --> 00:08:44,470', "it's fresh uh paint yeah": '00:08:44,480 --> 00:08:47,110', 'come around the back here mitchell i': '00:08:47,120 --> 00:08:48,790', 'love this white table tail light here': '00:08:48,800 --> 00:08:50,790', 'this is incredible that was the most': '00:08:50,800 --> 00:08:52,470', 'important design theme yeah from the': '00:08:52,480 --> 00:08:54,310', 'beginning yeah because you know when we': '00:08:54,320 --> 00:08:56,310', "were asked uh let's collaborate with": '00:08:56,320 --> 00:08:58,790', 'gran turismo yeah you know basically for': '00:08:58,800 --> 00:09:01,110', 'two weeks my team was not stoppable they': '00:09:01,120 --> 00:09:03,030', 'were disappearing and then you know': '00:09:03,040 --> 00:09:04,949', 'coming back with a million ideas but': '00:09:04,959 --> 00:09:07,430', 'that y shape was from the beginning': '00:09:07,440 --> 00:09:09,430', 'because i had to be there i had to be': '00:09:09,440 --> 00:09:10,790', 'there because we said we need to design': '00:09:10,800 --> 00:09:12,870', 'it also in this perspective yes because': '00:09:12,880 --> 00:09:14,949', 'you know in the game it is used like': '00:09:14,959 --> 00:09:16,389', "this that's why that's so true": '00:09:16,399 --> 00:09:18,870', 'and these exhaust tips meteor': '00:09:18,880 --> 00:09:21,590', "where'd you grab those from": '00:09:21,600 --> 00:09:23,430', 'you know to make the process faster and': '00:09:23,440 --> 00:09:25,670', 'to also save some money because': '00:09:25,680 --> 00:09:27,430', 'designers are also efficient people yeah': '00:09:27,440 --> 00:09:29,670', 'we took the aventador s exos five double': '00:09:29,680 --> 00:09:32,389', "them and we have it here so that's": '00:09:32,399 --> 00:09:34,710', "awesome you know it's super cool for me": '00:09:34,720 --> 00:09:36,470', 'this kind this car is also a design': '00:09:36,480 --> 00:09:39,110', 'strategy it is kind of following the': '00:09:39,120 --> 00:09:41,590', 'idea of the taps millennium yeah but we': '00:09:41,600 --> 00:09:43,350', 'wanted to get it even more crazy yeah': '00:09:43,360 --> 00:09:45,269', 'because with the tesla was the': '00:09:45,279 --> 00:09:46,710', 'electrical concept yeah and here the v12': '00:09:46,720 --> 00:09:49,269', 'yeah hybrid okay so which one do you': '00:09:49,279 --> 00:09:51,430', 'like better design-wise the next one': '00:09:51,440 --> 00:09:53,990', "where's the latest one if i tell you no": '00:09:54,880 --> 00:09:57,030', 'politically correct you know the design': '00:09:57,040 --> 00:09:58,790', 'of the other cars maybe then uh you know': '00:09:58,800 --> 00:10:00,630', 'disappointing': '00:10:00,640 --> 00:10:02,829', "yeah they have their own camera they're": '00:10:02,839 --> 00:10:04,069', "very different yes i think that's it": '00:10:04,079 --> 00:10:06,310', 'guys massive thank you to lamborghini': '00:10:06,320 --> 00:10:08,150', 'for bringing this out today for us and': '00:10:08,160 --> 00:10:10,630', "michie the head of design and we've had": '00:10:10,640 --> 00:10:12,710', 'like a close-up look at this incredible': '00:10:12,720 --> 00:10:15,590', 'car otherwise you would only see it in': '00:10:15,600 --> 00:10:17,670', "the game we'll see you next time bye": '00:10:17,680 --> 00:10:19,269', "love ya i'm out": '00:10:19,279 --> 00:10:24,460', 'i': '00:10:38,480 --> 00:10:40,560'},
'_zRP8CyTerY.en.srt': {'enemies at the back this is what you': '00:00:00,240 --> 00:00:01,990', "deploy look it's armed": '00:00:02,000 --> 00:00:04,070', 'and it has tacks let me grab them for': '00:01:42,720 --> 00:01:46,069', 'you': '00:04:18,639 --> 00:04:20,720', '[Music]': '00:04:14,400 --> 00:04:18,629', 'look at this': '00:00:22,000 --> 00:00:28,550', 'and around here check this out': '00:00:28,560 --> 00:00:36,790', "isn't this ridiculous guys this is a": '00:00:36,800 --> 00:00:38,869', 'real james bond car from': '00:00:38,879 --> 00:00:41,110', 'tomorrow never dies came out in 1997 let': '00:00:41,120 --> 00:00:44,470', 'me show you look': '00:00:44,480 --> 00:00:46,470', "there's no one driving it the driver is": '00:00:46,480 --> 00:00:49,590', 'actually in the back': '00:00:49,600 --> 00:00:50,869', 'this is christian hey look how cool this': '00:00:50,879 --> 00:00:53,029', 'setup is': '00:00:53,039 --> 00:00:53,910', 'he actually drives the car from the back': '00:00:53,920 --> 00:00:56,830', 'seat': '00:00:56,840 --> 00:00:58,470', "look i'll show you in here as well oh": '00:00:58,480 --> 00:01:00,229', 'look the bullet holes': '00:01:00,239 --> 00:01:01,830', 'got to have some bullet holes on the car': '00:01:01,840 --> 00:01:03,670', 'and then here': '00:01:03,680 --> 00:01:05,109', 'you can see the pedals have been': '00:01:05,119 --> 00:01:06,310', 'elongated to go all the way back': '00:01:06,320 --> 00:01:09,109', "to the rear seats so we've got the": '00:01:09,119 --> 00:01:12,149', 'normal brake here this one in the middle': '00:01:12,159 --> 00:01:14,630', 'normal brake': '00:01:14,640 --> 00:01:15,670', "we've got the accelerator and then we've": '00:01:15,680 --> 00:01:17,830', 'got this as well now this allows you to': '00:01:17,840 --> 00:01:20,390', 'break just the back': '00:01:20,400 --> 00:01:21,749', "wheels they've actually installed extra": '00:01:21,759 --> 00:01:23,670', 'brakes here': '00:01:23,680 --> 00:01:25,510', 'so at about 30 kilometers an hour if you': '00:01:25,520 --> 00:01:27,670', 'need to quickly drift around the corner': '00:01:27,680 --> 00:01:30,069', 'as james bond would you slam on that': '00:01:30,079 --> 00:01:32,230', 'break that extra one and off it goes': '00:01:32,240 --> 00:01:34,870', 'now around here you just get even cooler': '00:01:34,880 --> 00:01:37,910', 'all right enemies at the back this is': '00:01:37,920 --> 00:01:40,310', "what you deploy look it's armed": '00:01:40,320 --> 00:01:42,710', "actually that's right and look at this": '00:01:50,159 --> 00:01:54,789', "it's got double 07 printed on them so": '00:01:54,799 --> 00:01:57,590', 'you just pop these in here': '00:01:57,600 --> 00:01:59,910', 'yeah and then they deploy': '00:01:59,920 --> 00:02:05,670', 'like drive over that your tyres are done': '00:02:05,680 --> 00:02:12,869', 'this is the setup again so you can see': '00:02:12,879 --> 00:02:14,470', 'it in better detail': '00:02:14,480 --> 00:02:16,070', 'christian is the actual stunt driver for': '00:02:16,080 --> 00:02:18,869', 'james bond like a christian': '00:02:18,879 --> 00:02:22,710', 'what bmw did was they actually delivered': '00:02:22,720 --> 00:02:26,150', 'this seven series to the studio with all': '00:02:26,160 --> 00:02:29,430', 'of this set up in the back so they': '00:02:29,440 --> 00:02:31,110', 'actually had to': '00:02:31,120 --> 00:02:32,390', 'make sure that the car was able to drive': '00:02:32,400 --> 00:02:34,710', 'from the back seat': '00:02:34,720 --> 00:02:36,630', 'before they even delivered the car and': '00:02:36,640 --> 00:02:38,150', 'they made three of these with all of the': '00:02:38,160 --> 00:02:40,150', 'features and everything': '00:02:40,160 --> 00:02:41,509', 'um so bmw delivered it with that': '00:02:41,519 --> 00:02:44,390', 'capability but then the studio added all': '00:02:44,400 --> 00:02:46,550', 'of these cool james bond features': '00:02:46,560 --> 00:02:48,470', 'to the front seat so you can take a look': '00:02:48,480 --> 00:02:58,710', 'oh my goodness': '00:02:58,720 --> 00:03:02,550', 'and then you come around here': '00:03:02,560 --> 00:03:05,360', "open up the boot you've got these tanks": '00:03:07,280 --> 00:03:11,750', 'so these actually power all of the the': '00:03:11,760 --> 00:03:14,070', 'gadgets that come in and out in and out': '00:03:14,080 --> 00:03:16,830', 'so': '00:03:16,840 --> 00:03:18,390', "that's what's hidden in the trunk and": '00:03:18,400 --> 00:03:21,830', "that's about it that's all the features": '00:03:21,840 --> 00:03:23,750', 'and cool stuff we found it here': '00:03:23,760 --> 00:03:25,830', 'look how hard he has to concentrate': '00:03:25,840 --> 00:03:27,270', "you're trying to back it up": '00:03:27,280 --> 00:03:29,110', 'he only has this screen': '00:03:29,120 --> 00:03:35,110', "and look you've got cameras here too": '00:03:35,120 --> 00:03:44,830', 'guys': '00:03:44,840 --> 00:03:58,830', 'uh': '00:03:58,840 --> 00:04:04,390', 'give us a quick thumbs up subscribe to': '00:04:04,400 --> 00:04:06,470', 'the supercar bonnie family we have cool': '00:04:06,480 --> 00:04:08,229', "stuff to show you right i'm out": '00:04:08,239 --> 00:04:12,830', 'bye': '00:04:12,840 --> 00:04:14,390'},}


yt_list2 = [YT('https://www.youtube.com/watch?v=_QNBdW8ZPB4'),
           YT('https://www.youtube.com/watch?v=_SB7h2kB6Eg'),
           YT('https://www.youtube.com/watch?v=_zRP8CyTerY'),
           ]

# add captions in each YT object
yt_list2[0].captions = caption_list['_QNBdW8ZPB4.en.srt']
yt_list2[1].captions = caption_list['_SB7h2kB6Eg.en.srt']
yt_list2[2].captions = caption_list['_zRP8CyTerY.en.srt']

f1 = Found(yt_list2[0], "the incredible interior i just love how", "00:04:25,840 --> 00:04:27,830")
f2 = Found(yt_list2[0], "the size of this thing incredible you've", "00:04:30,080 --> 00:04:32,550")
f3 = Found(yt_list2[0], "incredible so a massive thank you to you", "00:08:52,720 --> 00:08:54,710")
f4 = Found(yt_list2[1], "this is incredible that was the most", "00:08:50,800 --> 00:08:52,470")
f5 = Found(yt_list2[1], "like a close-up look at this incredible", "00:10:12,720 --> 00:10:15,590")

found = [f1, f2, f3, f4, f5]

image bg hotel_hw = "mod_assets/places/hotel_hw.png"

label act2_ch1:
 stop music fadeout 2.0
 scene black
 with dissolve_scene_full
 show intro_logo:
  menu_logo_move_b
 show menu_particles_b:
  xpos 640
  ycenter 510
  time 1.920
 show text("{size=100}{color=#6debab}{b}Arc 2, Chapter 3{/b}{/size}{/color}\n{size=60}Starting from zero{/size}\n{size=60}and the mysterious orange haired girl.{/size}"):
  yalign 0.8
 with Dissolve(1.0)
 pause 4.0
 scene bg mc_lr
 with dissolve_scene_full 
 "Monika and Natsuki finally resolved their problems..."
 $ perspective = "mc"
 call perspective_window
 "Now, more problems ahead of me. Mio being the main one."
 "How am I supposed to tell her I don't want her to be in my house?"
 "I'm still waiting for Sayori's confirmation too."
 "But now I have some time to think about her. And not in the romantic way."
 "Where did Mio come from? Why did I think it was a good idea to invite her to the club?"
 "And more importantly... Why is she behaving very flirty when she is around me?"
 "Almost as suspicious as Kotonoha."
 play sound cellphone
 "Finally, Sayori is calling."
 mc "Yeah? Sayori?"
 s "{i}Hello [player]!~{/i}"
 mc "Hello Sayori, what are you doing?"
 s "{i}I just finished my homework~{/i}"
 s "{i}What about you?{/i}"
 mc "Literally waiting for your answer."
 s "{i}Ehehe~{/i}"
 s "{i}So, about your question...{/i}"
 mc "Yeah?"
 s "{i}Can I go to your place to talk about it?{/i}"
 mc "Oh... Yeah, go for it."
 s "{i}Soooo, see you soon!{/i}"
 mc "See you Sayori."
 "With that, Sayori hangs up."
 "Ohhh man... I didn't tell her what time she'll be coming at!"
 "I think I'm gonna text her."
 mc "{i}Hello Sayori, I just wanted to ask how long do I have to wait for you.{/i}"
 "While I wait for Sayori's answer, I think I'm going to take a nap or something..."
 "I'm actually really tired and even if I woke up early today, I can't help feeling sleepy when I'm bored."
 "Sleepy and lazily walking, I make my way to my bedroom."
 scene black with wipeleft
 scene bg bedroom with wipeleft
 mc "{i}*sigh*{/i}"
 "Well... Now I can finally take a well deserved nap..."
 "I take my shoes out, then I lie down on the bed."
 "I'm glad that finally they've made up their problems..."
 "And now, the difficult part starts: writing a happy story to all of them."
 "What would I do to make 5 girls happy? It's not like they all like the same..."
 "And I actually really would want to invite Monika to go out somewhere."
 "But I don't think I know what I will say to her..."
 "I mean: how I will invite her..."
 "To be honest I'm kind of scared for what's coming. Will I write a better future for this world?"
 "I really want to do that, but just going with the flow is not something that fits with me at all."
 "Well... I think I can do better."
 "Now, time to sleep for a little bit."
 scene black with dissolve_scene_full
 "..."
 "Finally... Now I can--"
 play sound cellphone
 mc "Ugh..."
 "Well... That must be Sayori..."
 "Opening my eyes, I take my phone from the drawer."
 scene bg bedroom with dissolve_scene_full
 mc "{i}*yawn*{/i}"
 mc "Huh... It's a message from Sayori..."
 mc "{i}*Sorry, I fell asleep... Ehehe...*{/i}"
 mc "{i}*I'm going to your home right now, so we can talk about that.*{/i}"
 "Heh... Sayori falling asleep... I'm glad to know anything has changed so far."
 "Well, if Sayori is coming over then I should go get some clean clothing."
 "I get up from the bed, taking my dark shirt and pants. Once I'm dressed, I go down to the living room."
 scene black with wipeleft
 scene bg mc_lr with wipeleft
 play sound doorbell
 "Just as I get to the living room, I hear the doorbell's sound."
 mc "Yeah! I'm coming already!"
 scene black with wipeleft
 scene bg mc_hw with wipeleft
 "I reach the door, watching Sayori's thin shape behind."
 play music tsayori_c
 show sayori 1ba at t11 zorder 1
 s "Hello [player]~"
 mc "Hey Sayori, how you doing?"
 s 2bl "{i}*yawn*{/i} I'm still kinda sleepy but... I'm alright!"
 mc "Have you done Math's assignment for tomorrow?"
 s 2bx "Yeah! I have already~"
 mc "Nice, because I haven't."
 s 3bq "I can help you with that if you want, [player]."
 mc "Oh actually I don't need help, but it's just a lot of stuff, you know?"
 s 3br "Ehehe... Yeah, I know."
 mc "Well, then come in. Mio isn't here at the moment."
 show sayori 4br at h11 zorder 1
 s "Okay~"
 "Cheerfully smiling, Sayori walks to the living room."
 scene black with wipeleft
 scene bg mc_lr with wipeleft
 "Sayori sits on the couch, doing the same myself."
 show sayori 1bx at t11 zorder 1
 s "Soooo... [player]..."
 s 2bb "I've been thinking about that Mio thing, and..."
 mc "And?"
 s 2bj "Naomi is actually right! Mio is a very cute person!"
 s "Why would you ask me something like that?"
 mc "Because of Monika."
 s 3bb "Eh? Monika?"
 mc "Yeah. Look, if I tell her that Mio is staying at my home, what do you think her opinion will be?"
 s 3bh "Well... I guess you're right, but--"
 mc "Plus, Mio came without even letting me know! What am I supposed to do with her?"
 s 1bh "Try to getting to know her a little bit better?"
 mc "You're not getting my point... What I mean is, Mio can't stay here to sleep because it's not what I want."
 mc "Mio might be cute and all, but she's literally invading my home without asking me first."
 s 1bf "..."
 "Sayori doesn't say anything, she's just staring at me like kind of thinking."
 "I mean I really don't want to bother her with this, but I don't want Mio in my house either."
 "It's somewhat creepy that Mio knows where I live at..."
 "Hesitating, Sayori looks away."
 s 2bf "Well... Okay [player]..."
 mc "Are you sure?"
 s "Yeah... It's not like I hate her."
 mc "Phew... Thanks Sayori, I really--"
 show sayori 2bj at h11 zorder 1
 s "But there will be a a condition!"
 mc "Sure! What is it?"
 s 4bj "You won't be a meanie to Mio anymore! And if you do, I will be very pissed at you!"
 mc "..."
 "If this is the only way I'll be able to take Mio out of my place, then..."
 mc "{i}*sigh*{/i}"
 mc "Alright then, I promise. I won't be a meanie to Mio from now on."
 mc "And if I do, you'll be very pissed at me."
 s 4br "Yaaaay!~"
 s 1ba "Then okay, Mio can stay in my home!"
 mc "You're the best, Sayori."
 s "Ehehe~"
 play sound closet_open
 "While Sayori laughs, the door opens as Mio comes in smiling."
 show sayori 1ba at t21 zorder 1
 show mio 1ba at l22 zorder 2
 mi "Hello [player]!~ I'm back and I've--"
 mi 2bc "Oh? Sayori?"
 show sayori 2bx at h21 zorder 1
 s "Hello~"
 mi 3bg "O-oh! Um... Hello."
 mi 3bl "Can I know what are you guys doing here alone?"
 s 1ba "We were talking about stuff."
 mi 1bg "Ah, I see."
 mi 8bf "Well, you can stay for dinner Sayori! I'm gonna cook something delicious~"
 s 4bx "Oh, we can call the others too!"
 mc "Hey wait, why are you guys organizing a dinner in my place?"
 s 5ba "Oh... Sorry... Ehehe..."
 mi 6ba "Oh come on [player]! Let's do something tonight!"
 mc "We have school tomorrow."
 mi 5be "Does that mean we can't have fun?"
 mc "{i}*sigh*{/i}"
 mi "Sooooo?"
 stop music fadeout 2.0
 s 3bx "Come on [player], it'll be much fun!"
 "Why do they keep insisting with that? I mean, I want to do that, but..."
 "Something is kind of stopping me, I can't tell what it is though..."
 play music nday fadein 2.0
 "Is it the fact that both Mio and Monika are gonna be here? What will I say to Monika that Mio wants to stay at my home?"
 "Sayori will take her to her house, but still..."
 "Well, it will be the first step to actually spend time with Monika now that I think about it."
 "Alright, I think I can accept that."
 mc "Fine, let's do something for dinner today and let's invite everyone."
 $ s_name = "Mio & Sayo"
 show sayori 4br at h21 zorder 1
 show mio 5by at h22 zorder 2
 s "Yaaaay!~"
 $ s_name = "Sayori"
 mc "Well, let's call for them then."
 mi 1bl "Tehehe... [player]... We have to think of something to eat..."
 s 1bx "Yeah, I agree with Mio~"
 mc "Alright, what are we having for dinner then?"
 mi 3be "Some pasta with meatballs!~"
 mc "Uhhhh... Mio, but--"
 s 2br "Yaaaay!~ It'll be so delicious!"
 mc "Girls!"
 $ s_name = "Mio & Sayo"
 show sayori 1bb at h21 zorder 1
 show mio 3bc at h22 zorder 2
 s "Huh?!"
 mc "You guys are forgetting that Monika doesn't eat meat!"
 s 2bb "..."
 "Sayori and Mio remains silent while staring at me, it seems they actually didn't think that Monika doesn't eat meat."
 $ s_name = "Sayori"
 s 5bb "Ehehe... N-now that's correct..."
 mi 7bi "Oh no, how could I miss that? I've already bought everything..."
 s 2bl "Somehow I-I forgot that too..."
 mc "Well, I think we should ask her then..."
 mi 5bd  "Ask her what?"
 mc "What would she wants to eat."
 mi "Oh! Um... Then would you call her?"
 mc "Yeah, I'm on it. You guys go to take a seat to the living room."
 "Mio and Sayori nods, then I go to the kitchen."
 scene black with wipeleft
 scene bg kitchen with wipeleft
 "I take my phone out of my pocket to call Monika. I just expect she's not busy with homework or anything..."
 window hide(None)
 window auto
 pause 2.0
 $ m_name = "???"
 m "{i}Hello?{/i}"
 mc "Hey Monika, what are you doing?"
 m "{i}Ehhh... I'm not Monika, [player]...{/i}"
 mc "Kotonoha?"
 m "{i}Yeah, "
 $ m_name = "Kotonoha"
 extend "it's me.{/i}"
 mc "What? Where's Monika?"
 m "{i}Ah, she went out for some stuff to make the homework.{/i}"
 mc "Huh..."
 m "{i}Yeah. Why? Did you want to talk to her?{/i}"
 mc "Yeah, I did."
 m "{i}Well, maybe you might want to stop by my place, we're about to start our assignments...{/i}"
 mc "{i}*sigh*{/i}"
 m "Well... I'm gonna tell Mio and Sayori about that."
 m "{i}Oh... Okay then.{/i}"
 mc "Alright, see you in a while Kotonoha,"
 m "{i}Yes! See you [player]~{/i}"
 $ m_name = "Monika"
 "Saying nothing else, Kotonoha hangs up."
 "As I said... She's actually busy with homework..."
 "Maybe she can enjoy herself tonight if we go to have dinner to Kotonoha's home."
 "I put my phone in my pocket again, heading back to the living room."
 scene black with wipeleft
 scene bg mc_lr with wipeleft
 "Mio and Sayori are sitting on the couch, they seems to be having a nice time."
 "Sayori actually really likes Mio, doesn't she?"
 "Yeah... It makes sense, it's Sayori after all."
 show mio 1ba at t11 zorder 1
 mi "[player]~"
 show mio 1ba at t21 zorder 1
 show sayori 1ba at t22 zorder 2
 s "So... What did Monika say?"
 mc "Ah... Well, she's about to start her homework, and Kotonoha took the call."
 show sayori 2bk at s22 zorder 2
 s "Oh... So, no dinner for tonight..."
 "Looking sad, Sayori sighs and stares down."
 mc "Sayori... I would highly appreciate it if you let me finish my statement..."
 show sayori 3bl at t22 zorder 2
 s 3bl "Ehehe... O-okay [player]..."
 mc "Thanks. Kotonoha took the call AND she said that we can go to the hotel."
 s 2bm "Ooohhh!"
 s "So we all can spend more time together!"
 "Sayori happily jumps as I said that Kotonoha told me we can go to her hotel."
 "And yeah, we can actually spend more time together!"
 "--not to mention that I can spend more time with Monika."
 mc "Alright you all, we're leaving in 5 minutes, get ready!"
 $ s_name = "Sayo & Mio"
 show sayori 1bx at t21 zorder 1
 show mio 1be at t22 zorder 2
 s "Okaaay!~"
 $ s_name = "Sayori"
 s "I'll be right back then!~"
 show sayori at rhide
 hide sayori
 show mio 1ba at t11 zorder 1
 "With that, Sayori goes out of my house. Probably going to hers."
 "As Sayori leaves, Mio stands herself up from the couch."
 mi 2bd "So... [player]..."
 mc "Yeah?"
 play music hb
 $ currentpos = get_pos(channel="music")
 $ audio.nday = "<from " + str(currentpos) + " loop 0>../eheart-music/Daytime_g.ogg"
 stop music fadeout 2.0
 $ renpy.music.play(audio.nday, fadein=2.0, channel="music_bg2")
 show noise at noisefade(1) zorder 5
 show layer master at heartbeat
 mi "Why?"
 $ gtext = glitchtext(4)
 $ mi_name = "[gtext]"
 show mio dark at i11 zorder 1
 pause 0.2
 show screen tear(20, 0.1, 0.1, 0, 40)
 pause 0.25
 play sound glitchsay
 hide screen tear
 show mio 1bd at t11 zorder 1
 pause 0.26
 mc "Uh? Why what?"
 mi "Why can't you remember?"
 $ gtext = glitchtext(25)
 $ style.say_dialogue = style.edited
 mc "{cps=*2}[gtext]{nw}"
 $ style.say_dialogue = style.normal
 mi "Why can't you realize how much I love you?!"
 $ style.say_dialogue = style.edited
 mc "{cps=*2}[gtext]{nw}"
 show mio dark at t11 zorder 1
 show screen tear(20, 0.1, 0.1, 0, 40)
 pause 0.25
 play sound glitchsay
 hide screen tear
 show mio dark at t11 zorder 1
 pause 0.27
 mi "{cps=5}Why don't you come with me instead of her?!"
 "[gtext]"
 "[gtext]"
 show screen tear(20, 0.1, 0.1, 0, 40)
 pause 0.25
 play sound glitchsay
 hide screen tear
 mi "{cps=5}Just love me! Love me and I will make you the happiest man alive!"
 show mio dark at face
 mi "{cps=5}Ignore that freaking bragger... Ignore them all and just come with me..."
 mi "{cps=5}Freak Monika... LOVE ME!"
 stop music_bg2
 hide mio dark
 show mio 1bd at t11 zorder 1
 hide noise
 hide vignette
 show layer master
 scene black
 stop music
 play sound fall
 $ style.say_dialogue = style.normal
 $ audio.nday = "<loop 0>eheart-music/Daytime.ogg"
 "..."
 $ s_name = "???"
 s "{alpha=.5}[player]{/alpha}!"
 "Eehh?"
 "W-what happened? Why am I on the floor?"
 "I can't move my body, scream either..."
 s "{alpha=.7}[player]{/alpha}!"
 s "{alpha=.7}What happened to him?{/alpha}"
 s "{alpha=.7}I don't know! I was talking to him, but he suddenly passed out!{/alpha}"
 s "{alpha=07}Oh no! [player]! Please wake up!{/alpha}"
 "Huh? Sayori? Is that Sayori's voice?"
 s "Call an ambulance, Mio! W-we can't let him die!"
 "I can't hear anything but Sayori's weeping."
 "I barely remember... Why am I here? Wasn't I supposed to be talking to Mio?"
 "For Sayori's sake I got to try to wake up..."
 scene bg mc_lr with dissolve_scene_full
 $ s_name = "Sayori"
 s "[player]!"
 "As I open my eyes, I find myself lying on the floor."
 "Said that, Sayori comes running to me, hugging me while crying."
 show sayori 4bw at face
 with Dissolve(1.5)
 s "[player], you are fine! I-I thought you were gonna die!"
 mc "Hooooh... N-no, Sayori, don't worry. I-I'm okay..."
 s 3bu "Are you sure?"
 mc "Yeah... I guess so..."
 "Sayori lets me go of her grip, standing myself up from the floor."
 $ mi_name = "Mio"
 show sayori 4bu at t21 zorder 1
 with None
 show mio 1bj at t22 zorder 2
 mi "[player], why did you faint out? I was so scared!"
 mi 3bi "You even began to say weird random things!"
 mc "Huh?"
 show sayori 1bk at t21 zorder 2
 "I was talking to Mio, but I'm not that sure what we were talking about though..."
 "I lost track of time out of the blue."
 mi 4bh "Are you okay, [player]? I wouldn't want you to be hurt or anything!"
 mc "Ehh... Yeah, everything is okay now."
 s 3bh "Are you sure?"
 mc "Yeah."
 s "{i}*sigh*{/i}"
 s 2bd "Okay [player]... So, we can go now!"
 play music nday fadein 2.0
 show sayori at rhide
 hide sayori
 show mio 6bg at t11 zorder 1
 "Kind of sadly smiling, Sayori slowly walks to the front door."
 "Meanwhile Mio comes to me, she then hugs my arm."
 show mio 6bg at face with Dissolve(1.5)
 mi "Mmmm~"
 mi 5bl "Thankfully you're alright, [player]!~"
 mi 3bf "Don't scare me like that again, okay?"
 mc "Uh... Yeah? Now, stop hugging my arm like that."
 mi 2bx "Uhuhu~ For real, you're the cutest one I've ever met!"
 mi 1ba "Let's go~"
 show mio 1ba at t11
 show mio at rhide
 hide mio
# pause 1.0
 "Mio goes to the front door, humming and smiling."
 mc "What was that...?"
 "I still can't figure out what happened to me... Basically it wasn't me at all!"
 "What were we talking about?"
 "This is getting creepier each day..."
 mc "{i}*sigh*{/i}"
 "I think I'm becoming crazy..."
 "I just have to see how things flows from now on."
 "For now, I just want to get leaving, head to Kotonoha's and spend time with Monika."
 "She'll be busy with homework, and it would be a nice chance to get closer to her."
 "Finding  the motivation, I step out, Sayori and Mio waiting for me outside."
 scene black with wipeleft
 scene bg house with wipeleft
 show sayori 1ba at t11 zorder 1
 s "Hey [player]~"
 mc "Huh?"
 s 2bx "Can we go to the mall real quick in our way to Kotonoha's?"
 mc "Eh? What for?"
 s "Mio wants to buy something."
 show sayori 2bx at t21 zorder 1
 show mio 1be at t22 zorder 2
 mi "Yes! It would be wrong if we get there without a gift, don't you think so?"
 mc "Hm..."
 mc "Yeah, that makes sense. Let's go then, the city is quite close to her home."
 $ s_name = "Sayo & Mio"
 show sayori 2bx at h21 zorder 1
 show mio 1bx at h22 zorder 2
 s "Yes!"
 $ s_name = "Sayori"
 "Mio, Sayori and I begin to make our way to the city, so we can go to the mall. I'm not that sure what Mio would get, but well."
 "I think she just wants to be cute and take a gift to them."
 scene black with wipeleft
 scene bg st with wipeleft
 "Walking a couple of blocks, we reach Kotonoha's hotel. Unfortunately this isn't our destination.."
 show mio 1ba at t21 zorder 2
 mi "[player], Sayori, what should we get them?"
 show sayori 2ba at t22 zorder 1
 s "Ummm... I don't know..."
 s 2bx "What about a cake?"
 mi 2be "A cake? Hm... What do you think, [player]?"
 "Sayori and Mio stares at me, waiting for me to respond."
 mc "Yeah, I think a cake would be a nice present to be honest."
 mi 4bx "Uhuhu~ That's what I thought!"
 show sayori 4br at h22 zorder 1
 s "Yaaaay, we're gonna have cake!"
 mi 8be "Then let's go! There's a nice bakery a few blocks ahead!"
 s 2br "Come on [player], come on! I want to see Monika and Kotonoha's faces when they see the cake!"
 "Saying nothing else, Sayori takes my hand and drags me. Mio laughs as she sees that."
 scene black with wipeleft
 scene bg city with wipeleft
 "We've gotten to the city and I can say that there are lots of people everywhere."
 "I mean that's why it's a city. Duh [player]..."
 "Whatever, we're walking around, Mio is having a conversation with Sayori."
 "Well... Actually I think Mio is not that bad of a person..."
 "And if Sayori thinks I'm being a 'meanie' to her... I think I should really do it."
 show sayori 1ba at t11 zorder 1
 s "Oh look, there's Monika!"
 "As Sayori said, Monika is just stepping out of the bakery, holding a plastic bag containing buns."
 s "Hey Monika!~"
 "Monika looks around to see who's called for her, finding us. Sayori waves her left hand."
 show sayori 1ba at t21 zorder 1
 show monika mp1_c at t22 zorder 2
 m "Oh... "
 extend mp2_e "Hey guys!"
 s 2bc "We didn't expect you to be here."
 show sayori 2bk at s21 zorder 1
 s "Awwwww, that ruined our plans..."
 m mp3_l "Ahaha... Your plans?"
 show sayori 2bk at t31 zorder 1
 show monika mp3_l at t32 zorder 2
 show mio 1ba at t33 zorder 3
 mi "Yes! We are going to get a cake!"
 m "Um... I don't get what plans are you guys talking about..."
 mc "Well, I called to you, but Kotonoha replied. She said you went out to get materials for your homework."
 m mp3_b "Oh! Not really, I've come to get buns!"
 "Monika raises that plastic bag."
 s 2bc "Buns?"
 m mp3_k "Yeah, these are a gift to her~"
 mi 3bc "A gift? What are you gifting her that for?"
 m mp1_a "Just to show how much I care about her~"
 mi 8bc "Oh... I see..."
 m mp2_a "So... Yeah."
 mc "Um... We came because Mio wanted to take you girls a cake."
 s 4bx "We're all gonna have dinner together!"
 m mp3_n  "Oh... But, we got school tomorrow..."
 mi 1be "That doesn't mean we can't have fun~"
 m mp2_n "Ahaha... Fair enough..."
 m mp1_b "So, are you gonna buy that cake here?"
 mi 3be "Yes! This is my favorite bakery after all."
 m mp2_b "Oh... That's great."
 "Mio stares at me."
 mi 4bf "Hey [player], wanna come with us?"
 mc "Actually I'm gonna wait right here with Monika."
 s 2bx "Come on [player], let's go!~"
 stop music fadeout 2.0
 mc "I'm gonna wait here with Monika, so we all can go together."
 show sayori at rhide
 hide sayori
 show mio at rhide
 hide mio
 show monika mp2_b at t11 zorder 1
 "Sayori nods, cheerfully dragging Mio inside."
 play music tmonika_b fadein 2.0
 m mp2_e "So... [player]..."
 mc "Yeah?"
 m mp3_l "What does Sayori mean by saying 'we'are all gonna have dinner together'?"
 mc "Oh... Well, she actually came up with that idea. They thought of pasta with meatballs but..."
 m mp2_e "Sayori forgot I don't eat meat, did she?"
 mc "Yeah. So did Mio."
 m mp2_c "Um... "
 extend mp3_d "I have never spoken to Mio..."
 m "There's no way she can knows I don't eat meat."
 mc "Well, she said 'how did I miss that?', so..."
 m mp1_c "Hm..."
 m "That's {i}very{/i} suspicious... Isn't it?"
 mc "Yeah... You're right..."
 m "Whatever... "
 extend mp1_b "So, what is Mio gonna cook for us?"
 mc "Well, um... I don't know... That's why I called you."
 m mp2_l "Ahaha... [player], you already know I'm vegetarian..."
 mc "Yeah, I know but... I'm not, Monika."
 mc "I should learn some veggie dishes, shouldn't I?"
 m mp3_k "Heh... That would be quite helpful to be honest~"
 mc "Alright, I might need some of your help to do so."
 show monika mp4_k at h11 zorder 1
 m "Sure! I can teach you my favorite dishes!"
 mc "Great!"
 m mp2_m "And, um..."
 m mp2_n "Did you come across Mio or something? Why is she here?"
 "God... I knew it was time to reach this point..."
 "Well, it's not like I don't have that resolved now."
 mc "Eh, actually she..."
 m "She...?"
 mc "Well, as you should already know, she came to my house without even letting me know."
 m mp1_n "Yeah."
 mc "So, we were about to leave my home and she said that..."
 mc "--she is gonna stay with me at my place."
 m mp2_n "Eh? B-but... [player]..."
 mc "But don't worry. Sayori is gonna help me with that."
 m mp2_g "Oh? How is she gonna help you?"
 "Monika making sure Sayori and Mio are not leaving the bakery, comes slightly close to me."
 show monika mp1_g at face zorder 1
 with Dissolve(0.5)
 mc "I asked Sayori if she's down to help me hosting her, and she agreed."
 m mp1_e "Oh! That's a relief..."
 mc "But she asked something in return."
 m mp2_d "What? Really?"
 "Monika is surprised to hear that Sayori actually really did that. I'm surprised myself too..."
 mc "Yeah."
 m mp3_n "And... What did she ask you to do?"
 mc "She's asked me to stop being mean to Mio, and um... That's it."
 m mp2_n "Oh... I see..."
 mc "Yeah. I'm gonna try to not being mean to her, but... I don't think I could let myself to trust Mio."
 m mp2_g "I understand you, [player]. "
 extend mp2_e "I don't trust her either."
 mc "Well I think we've spoken enough about her. How are you feeling now that everything is okay?"
 show monika mp2_e at t11 zorder 1
 with None
 m "I'm certainly more relaxed now!"
 m mp1_b "Actually we're gonna go shopping on Saturday~"
 mc "'We'?"
 m mp2_b "Yep. Natsuki, Kotonoha and me."
 mc "Oh... But, what about the others?"
 m mp3_b "We're gonna talk about that tomorrow during the club, and if they want to go, then that's it!"
 mc "Nice. Can I go this time?"
 show monika mp3_k at h11 zorder 1
 m "Sure! Why not?"
 mc "Kotonoha also told us you're gonna do your homework."
 m mp2_l "Ahaha... Actually I don't have homework today."
 mc "So... Why did you tell her that?"
 m mp2_a "I just thought it'd make sense."
 mc "Heh... Alright then."
 m mp2_b "Oh! I've come up with something to eat!"
 mc "What is it?"
 m mp3_b "How about an eggplant lasagna?"
 mc "Eggplant lasagna? How do you cook that?"
 m mp3_n "Um... With eggplant? That's why it's called \"eggplant lasagna\"... Ahaha..."
 mc "Huh... Yeah, I guess you got me there."
 m mp2_b "It's okay! But even so, you're kind of silly."
 mc "Hahaha, yeah I think I am."
 "Stepping out of the bakery, Sayori and Mio comes to us."
 show monika mp2_b at t31 zorder 1
 show mio 2be at t32 zorder 2
 mi "We're back!"
 show sayori 1br at t33 zorder 3
 s "And we've bought the best cake!"
 "Sayori takes the cake showing it to us."
 "It's a circular chocolate cake with chocolate syrup spreaded above."
 s 2bx "Do you guys think Kotonoha will like it?"
 m mp2_k "Yeah! I've spoken to her a lot lately and she's said that she really loves chocolate!"
 mi 5bx "Uhuhu~"
 mi 4ba "{i}I knew it.{/i}"
 mc "Uh? Did you say something, Mio?"
 mi 1ba "Oh, it's nothing [player]. It's nothing."
 mc "Hm... Okay, I see."
 show sayori 1br at h33 zorder 1
 s "So, What are we waiting for? Let's get going already!"
 show sayori at rhide
 hide sayori
 show mio at rhide
 hide mio
 show monika mp2_a at t11 zorder 1
 "With that, Sayori and Mio walks back to Kotonoha and Monika's place, letting me and Monika behind."
 m mp1_b "It's nice to be back, isn't it?"
 mc "Yeah, indeed it is."
 m mp3_k "Come on [player], let's catch them up!"
 "I nod and we both walk back."
 "Hopefully today is gonna be a great day."
 scene black with wipeleft
 scene bg st with wipeleft
 show orange zorder 10:
  alpha 0.1
 with wipeleft
 "As we approach the hotel, the usual scene greets us: cars traveling around, people walking, couples enjoying themselves..."
 stop music fadeout 2.0
 "One day Monika and I are gonna be part of that group."
 "Sayori and Mio are having a conversation, and it seems they are enjoying themselves."
 "Meanwhile we are just walking next to each other, and Monika has a really cute smile in her face."
 "Watching her smiling like this is the most relieving thing I have ever seen."
 "I'm kind of nervous about things though... Will I make it good this time? Will I manage to make them all happy?"
 "It's not like I think I can't but... I don't know, something kind of got me concerned."
 play music confession fadein 2.0
 show monika mp1_d at t11 zorder 1
 m "[player]? Are you okay?"
 "Monika stares at me, I think she asked me something but I didn't hear it."
 mc "Oh, sorry I was thinking about something."
 m mp2_d "What is it?"
 mc "I'm kind of worried... What if I don't do it well?"
 m mp2_c "Uh? Do what?"
 mc "Give this world a good ending to you all."
 mc "It's like the biggest responsibility I've carried on my back so far."
 m mp2_e "Well... If that's what you want, I bet you'll make it just good."
 m mp3_e "You brought us back after all."
 mc "Yeah... And that's why I don't want to fail."
 mc "If I really want to give you guys a good ending, I'll have to give it my best. I don't think I could stand losing any of you."
 m mp1_e "[player]..."
 "Monika stops walking, next she takes my hand."
 m mp3_g "Why are you this insecure about yourself?"
 mc "Because I don't want to commit mistakes..."
 mc "I don't want to lose anyone this time... I don't want anyone to be left behind..."
 m mp2_g "If that's what you want, then everything will be okay."
 m "Trust me, [player]..."
 m mp1_k "From now on, we won't lose those we love anymore!"
 m "Just like you don't wanna leave us behind... I don't wanna let you do everything while I'm just sitting there waiting for you to solve everything."
 m "I'll be right here with you."
 mc "..."
 m mp1_b "Just stay with us and we won't fail you either."
 mc "Alright..."
 m mp2_k "Just take my hand and we'll make it up to all of them."
 m mp2_b "Are you gonna let me help you with your struggles?"
 mc "I... Um..."
 "I don't know what to say..."
 "This is... kind of sudden of her to say that..."
 "She's said that before, but still it felt different..."
 "I think that I'm worrying for making them all happy, but I'm not considering this."
 "I mean, I'm not considering that Monika also wants to help, and I'm just declining her proposal."
 "Probably that's the very first step to have everyone smiling everyday: taking care of my own concerns as well."
 m mp2_a "And well?"
 "Monika's eyes brights as the sun hits her cute emerald green pupils."
 "Looking to the front, I don't see Mio nor Sayori around. Probably they've already arrived to the hotel."
 "This is the perfect time... To say her how I feel about her..."
 "--that I want her to be the one I want to be with."
 mc "Monika..."
 "I hold her hands as I stare at her eyes."
 m mp1_n "Oh? Y-yeah?"
 mc "Alright. I'm gonna accept your help if that's what you want."
 mc "And also... I want to tell you something..."
 "Slightly tightening my grip to her hands, I take a deep breath."
 mc "Look... I've always liked you since \"that\" happened in the other world, but I kind of said: why someone like her would like me back?"
 mc "\"She's out of my league\"."
 mc "Until I knew that you were feeling really alone in this world."
 mc "That you really wanted to be with someone."
 m mp2_o "[player]..."
 mc "I still don't know who you were trying to reach, but it felt like it was me."
 mc "But I've taken my choice now, this time with no regrets."
 m mp2_d "Ah--"
 "Holding her in an embrace, I stare at Monika."
 show monika mp2_d at face
 with Dissolve(1.5)
 mc "Would you..."
 m "Y-yeah?"
 mc "Would you... date me?"
 m mp3_f "Oh... Um..."
 "I knew it... This wasn't the best moment to ask her that..."
 "But... How could I miss this chance? What if she actually says \"yes\"?"
 m mp2_g "[player]..."
 "Monika's face is blushing so badly, making this the most cute moment we'll have."
 "Even if she declines, I'm gonna remember this until she accepts me as her boyfriend."
 "This time for real."
 m mp3_n "I-I would want that too..."
 m "I truly do..."
 m mp2_n "But I prefer to wait a little bit more... until we had known each other a little bit more..."
 "Still blushing, Monika looks away."
 m "I... I just want you to know that I truly do love you..."
 m mp1_l "And nothing would make me the happiest girl than hearing you say those words to me..."
 m "D-don't get me wrong! I'm so happy right now!"
 m mp3_e "Finally hearing those words going out of your mouth are truly the best I've ever heard you say this time."
 m "You know, since we haven't had enough time to know us a little bit better because of Natsuki and that stuff."
 mc "Yeah..."
 m mp1_f "I'm not saying that I don't accept your confession. I... really want to be your girlfriend..."
 m "I even call you my boyfriend even when you haven't asked me for that yet..."
 m mp2_g "But now that you just said it, I... Kind of feel doubtful..."
 m mp3_k "Just give me some days to get to know you better..."
 mc "Yeah... Understood..."
 m "Don't be sad, [player]."
 m mp1_e "This is not a denial... "
 extend mp3_b "It's more like a \"wait for me\"."
 mc "I think you're right though."
 m mp2_j "Ahaha!~"
 "Monika hugs me back, tightening her hug as I pat her head."
 m "Mmmm~"
 "Slowly letting go of me, Monika kisses my cheek still holding my hand."
 stop music fadeout 2.0
 show monika mp1_b at t11 zorder 1
 m "Come on! We still have things to do!"
 mc "Yeah... Let's go..."
 "Freeing my hand from hers, she hugs my arm and rests her head on my shoulder."
 show monika at thide
 hide monika
 m "Let's go!~"
 "With that, we both walk to the hotel."
 scene black with wipeleft
 scene bg st with wipeleft
 show orange zorder 10:
  alpha 0.2
 with wipeleft
 ""
 $ MainMenu(confirm=False)()
































label act2_ch3_preending:
 scene black with wipeleft
 scene bg club_day with wipeleft
 "Mio has gone out with her backpack while we're just finishing up to clean the clubroom."
 "It was a pretty good day, I actually enjoyed to hang out with everyone today."
 if persistent.h_scene == True:
  "Also... I can't believe Monika and I did do... 'that'..."
 elif persistent.h_scene == False and persistent.monika_date == True:
  "I'm glad Monika and I finally had an actual date as a couple."
 "This is what I was really looking for.... Watch their smiles everyday..."
 "Hear their laughs everyday..."
 "I'm really happy now, and I think everyone is too."
 "Mio was being somewhat down since me and Monika became a couple, but overall... I'm glad she finally came with us."
 "Despite everything she has done, I kind of missed her."
 play music stay_alive fadein 2.0
 mi "Hello guys! I'm back~"
 mc "Eh?"
 "Mio's mood has changed out of the blue? She wasn't even looking happy..."
 kt "Mio...?"
 "Mio doesn't respond, it's almost like her face is lifeless."
 mi "You see everyone... This wasn't what I wanted, but if I have no choice then... I can't let you all to be around [player]. {b}MY{/b} [player]."
 play sound slide
 $ m_name = "Everyone"
 m "What?!"
 $ m_name = "Monika"
 "Mio has taken a gun out of her backpack, pulling the slide backwards and spotting at us."
 scene mi_gun with Dissolve(2.0)
 mc "Mio! What are you doing!"
 mi "I'm protecting what deserves me!"
 mc "What?! What are you even talking about?!"
 mi "About {b}YOU{/b}, [player]!"
 "Mio walks to Monika, but I block her way."
 mi "[player], move! T-this is because I love you!"
 mc "And I said that I wanna be WITH Monika!"
 mc "She's MY girlfriend now, and if you want to hurt her, you must hurt me first."
 "She's trying to push me away, but she's not as strong as Natsuki."
 m "M-Mio... I..."
 $ style.say_dialogue = style.edited
 mi "{cps=3.5}YOU SHUT UP!{/cps}"
 call gun_effects
 $ style.say_dialogue = style.normal
 "Mio shoots to the floor, making everyone to kneel down."
 mc "M-Mio! Put that thing down!"
 mi "I just..."
 mi "[player], please... Don't make it harder..."
 mc "You are making it harder! Do you think I will hang out with you if you kill MY girlfriend!"
 mi "..."
 "Monika slowly walks to Mio and--"
 m "Mio! This isn't you! I know what you are feeling, I also felt the way you do now!"
 m "You... You don't wanna do this... It's the obsession talking!"
 mi "Shut up..."
 m "And also, do you think that killing us would resolve anything? Because it won't!"
 mi "Shut up..."
 m "[player] has chosen this, and--"
 mi "{b}I SAID SHUT UP!{/b}"
 call gun_effects
 call gun_effects
 m "Nnngh---"
 play sound fall
 kt "N-no! Monika!"
 mi "Don't help her!"
 call gun_effects
 kt "...!"
 mc "What?!"
 "The unconscious Monika's corpse falls just behind me, everyone screams as Mio still holds the gun."
 y "M-Mio... Please... D-drop the gun and we'll talk about this..."
 mi "You freaking bookworm, {i}SHUT UP!{/b}"
 call gun_effects
 call gun_effects
 call gun_effects
 "Mio spotted at Yuri and shot at her three times, but she ran away and got in to the closet."
 play sound mag_load
 "Distracted loading the gun, Kotonoha rushes at Mio. Since she's taller than her, Kotonoha reaches her before she pulls the slide again."
 scene mi_gunb with dissolve_cg
 "Taking a chair to charge towards Mio, Kotonoha quickly hits her hand with it, making Mio to drop the gun."
 "As Mio dropped the gun, Kotonoha tackles her and Mio fells to the ground. Kicking away the gun, Kotonoha yells--"
 kt "R-run, Sayori! Natsuki! I-I'll restrain her while you girls run away!"
 s "N-no! We won't lea--"
 kt "I SAID RUN!"
 "Kind of surprised, Sayori and Natsuki ran out of the classroom."
 mi "Kotonoha... Y-You're gonna die too!"
 "I run as fast as I can, but Mio managed to set herself free from Kotonoha's grip, kicking her to the left, quickly going to gather her gun."
 play sound slide
 "Seeing that Mio has already gotten back her gun, Kotonoha tries to dodge the shot--"
 call gun_effects
 call gun_effects
 kt "Nnngh--"
 $ style.say_dialogue = style.edited
 mi "AHAHAHAHAHAHA!"
 $ style.say_dialogue = style.normal
 mc "Kotonoha!"
 kt "I-it's okay [player]... That second bullet only brushed me..."
 mi "Ahaha... You're  as agile as I remember..."
 mc "'As I remember?' What do you mean?"
 kt "It's nothing [player], we--"
 mi "You're so cute Kotonoha... You know something? I'm not gonna kill you."
 "Taking down the gun, Mio slowly walks to Kotonoha, who is still trying to recover herself."
 mc "Mio, leave her alone!"
 "Angered, I walk as fast as I can, but Mio spots at me."
 mi "Don't move [player]~ You wouldn't want Kotonoha to get hurted, would you?"
 mc "Gh--"
 "Damn... I have to do something to keep Kotonoha safe..."
 "She will die if I don't do anything!"
 "But she will die if I do something..."
 "Alright [player]... You can't let Kotonoha nor Monika die..."
 "You can't also let the fear of Monika dying take you to become crazy..."
 "I have to handle this carefully or she will shoot Kotonoha out!"
 "But also I have to protect Yuri!"
 "Fuck..."
 "What do I do...?"
 mi "Kneel to me, Kotonoha~"
 kt "Huh?! I won't--"
 call gun_effects
 mi "I said kneel to me!"
 kt "..."
 mc "Kotonoha, no!"
 "Kotonoha stares at me with tears in her eyes, almost about to cry."
 ""
 $ MainMenu(confirm=False)()

  #######################################################################################
label idk:
  mi "Uhuhu~"
  mi "So, [player]... Were you talking about me with Kotonoha?"
  mc "Huh?!"
  "What? How did she know that!"
  "What if Monika is right? What if Mio is self-aware and she's hiding something from us?"
  mi "I knew it!"
  mi "Do you remember our deal, don't you?"
  mc "..."
  mi "What? You won't respond me?"
  mi "Even when I discovered it?"
  mi "Wow [player], you got to hate me so much, don't you?"
  mc "...no?"
  mi "Yeah, let's assume you don't. Why did you do that again? Don't I deserve some love?"
  mc "Meh."
  mi "'Meh'? What is that supposed to mean?"
  mc "Mio I told you already, I wanna be with Monika! What part am I not being clear in??"
  mi "Well, I understand that. But like, eh, I would want you to try with me, you know..."
  "Mio comes close to me, she then ties my necktie."
  "Next, she whispers something to my ear."
  mi "{i}Monika doesn't deserve you.{/i}"
  "She kisses my cheek and goes to the window cheerfully. Just after having the window open, she sits on the desk."
  scene mi_desk1a with dissolve_cg
  mi "[player], come here~"
  "With a smug expression, Mio asks me to come closer."
  "I take a loooong sigh before bringing myself to do that."
  mc "Right."
  "Slowly making my way towards her, I reach up the dena she's sitting on."
  mi "So, as part of the deal we had, I want you to kneel before me and apologize."
  mc "Eh?! I'm not gonna do that in any circumstance!"
  mi "Uhuhu~"
  mi "So, are you gonna break our deal?"
  mc "Yes, I will."
  mi "Oh... So that's how it is..."
  mi "Well, if you don't, I'll tell Monika that you tried to rape me."
  mc "Yeah, because she would trust anything you tell her."
  scene mi_desk1b with dissolve_cg
  mi "We have become very close friends~"
  mi "You wouldn't want her to think you're a rapist..."
  mi "--someone who takes advantage of an innocent and defenseless girl..."
  mi "Or even the Principal, what would my dad--"
  mc "Your... What?"
  mi "Ahem..."
  mi "I mean... What would the Principal think of you? Are you going to ruin your reputation because you're just breaking our deal?"
  mi "--or even Kotonoha... it's a shame she likes you, but you don't even notice her."
  mc "Kotonoha doesn't love me. Well, as far I know."
  mi "Uhuhu~"
  mi "I know it all, [player]. Kotonoha loves you, just so you know it as well."
  scene black
  with dissolve_scene_full
  show text("{size=100}{color=#6debab}{b}Meanwhile in{/b}{/size}{/color}\n{size=60}Kotonoha's classroom.{/size}"):
    yalign 0.5
  with dissolve_scene_full
  pause 2.0
  scene bg kt_classroom with dissolve_scene_full
  $ perspective = "kotonoha"
  call perspective_window
  "..."

label gun_effects:
 play sound gunshot
 show white zorder 4:
  alpha 0.8
  linear 0.25 alpha 0.0
 pause 0.3

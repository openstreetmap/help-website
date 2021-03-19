+++
type = "question"
title = "Cant use editcap"
description = '''Hi, first of all: I m sorry for my english. I have the latest wireshark version 1.6.2 The Problem: When i try to open my xxx.eth file with wireshark, it shows me this error: &quot;This application has requested the Runtime to terminate it in an unusual way.&quot; The File is about 38 MB and should not be too ...'''
date = "2011-09-10T04:43:00Z"
lastmod = "2011-09-10T07:03:00Z"
weight = 6246
keywords = [ "editcap" ]
aliases = [ "/questions/6246" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Cant use editcap](/questions/6246/cant-use-editcap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6246-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6246-score" class="post-score" title="current number of votes">0</div><span id="post-6246-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, first of all: I m sorry for my english.</p><p>I have the latest wireshark version 1.6.2 The Problem: When i try to open my xxx.eth file with wireshark, it shows me this error: "This application has requested the Runtime to terminate it in an unusual way." The File is about 38 MB and should not be too big, wireshark already worked with 200 mb nd bigger files. I searched in different forums nd tried to use <em>editcap</em>. But when i doubleclick on editcap, a black dos window opens and closes so fast, that i cant read anything. I really dont know much about this stuff :/ can somebody help me pls? For example i found the follwing command in a forum</p><p>editcap -c 100000 &lt;yourbigfile&gt; &lt;outfile&gt;</p><p>but how do i use it? where can i command it, editcap doesnt even open, so i could be able to command anything!</p><p>Thanks :)</p><p>PS: if someone wants to answer in german, no prob :)</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-editcap" rel="tag" title="see questions tagged &#39;editcap&#39;">editcap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Sep '11, 04:43</strong></p><img src="https://secure.gravatar.com/avatar/2702888710c56c44fed545933abaa674?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="weltbeobachter&#39;s gravatar image" /><p><span>weltbeobachter</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="weltbeobachter has no accepted answers">0%</span></p></div></div><div id="comments-container-6246" class="comments-container"></div><div id="comment-tools-6246" class="comment-tools"></div><div class="clear"></div><div id="comment-6246-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6247"></span>

<div id="answer-container-6247" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6247-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6247-score" class="post-score" title="current number of votes">2</div><span id="post-6247-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You should run editcap from a command line window, since it is a command line tool - if you double click it from the explorer it will exit right away, after showing some usage details.</p><p>So start cmd.exe (I think it is called "Eingabeaufforderung" in a german Windows Start Menu, but I'm not sure), change into the Wireshark installation directory (usually "C:\programme\Wireshark") and run editcap. That should work, and show you all the options it has.</p><p>Now, in your command line window, change to the directory where the trace is, and call editcap with it's full path (or, if you prefer to run it anywhere without the path you could add the Wireshark installation directory to your system path variable if you know how to do that).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Sep '11, 04:52</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>10 Sep '11, 04:53</strong> </span></p></div></div><div id="comments-container-6247" class="comments-container"><span id="6249"></span><div id="comment-6249" class="comment"><div id="post-6249-score" class="comment-score"></div><div class="comment-text"><p>Wow, that was very fast! Thank You! I followed Your instructions, but i m sorry i didnt understand the last chapter :/</p><p>Maybe You can help me, when i provide more details... I can see now all the options of editcap. The istallation directory was right, and the path of the file, i want to split up, is: C:usersXXXXXspeed.eth</p><p>Is it posssible, that You show me, what i must write into that dos wondow now?</p><p>Thanks again :)</p></div><div id="comment-6249-info" class="comment-info"><span class="comment-age">(10 Sep '11, 05:17)</span> <span class="comment-user userinfo">weltbeobachter</span></div></div><span id="6250"></span><div id="comment-6250" class="comment"><div id="post-6250-score" class="comment-score"></div><div class="comment-text"><p>it is "C:usersXXXXXspeed .eth"</p></div><div id="comment-6250-info" class="comment-info"><span class="comment-age">(10 Sep '11, 05:19)</span> <span class="comment-user userinfo">weltbeobachter</span></div></div><span id="6251"></span><div id="comment-6251" class="comment"><div id="post-6251-score" class="comment-score"></div><div class="comment-text"><p>damn it, it doest show the / sign xD</p></div><div id="comment-6251-info" class="comment-info"><span class="comment-age">(10 Sep '11, 05:19)</span> <span class="comment-user userinfo">weltbeobachter</span></div></div><span id="6252"></span><div id="comment-6252" class="comment"><div id="post-6252-score" class="comment-score">1</div><div class="comment-text"><p>yeah, you need to put double \ in there to see them.</p><p>Try something like this:</p><p>c:\programme\wireshark\editcap -c 100000 -F libpcap c:\usersXXXXXspeed.eth c:\tracefile.pcap</p><p>which will cut it into files of 100000 packets each, saving them in the libpcap format.</p></div><div id="comment-6252-info" class="comment-info"><span class="comment-age">(10 Sep '11, 06:31)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="6254"></span><div id="comment-6254" class="comment"><div id="post-6254-score" class="comment-score"></div><div class="comment-text"><p>It worked! Thanks a LOT!</p></div><div id="comment-6254-info" class="comment-info"><span class="comment-age">(10 Sep '11, 07:03)</span> <span class="comment-user userinfo">weltbeobachter</span></div></div></div><div id="comment-tools-6247" class="comment-tools"></div><div class="clear"></div><div id="comment-6247-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


+++
type = "question"
title = "TCP streams in video capture"
description = '''i am taking capture while i am watching video from youtube. i see lots of tcp streams i really wonder why there is lots of streams? is one video one stream?  thanks.'''
date = "2016-05-11T05:43:00Z"
lastmod = "2016-05-11T07:31:00Z"
weight = 52429
keywords = [ "tcp.stream", "youtube", "tcp", "wireshark" ]
aliases = [ "/questions/52429" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [TCP streams in video capture](/questions/52429/tcp-streams-in-video-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52429-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>i am taking capture while i am watching video from youtube. i see lots of tcp streams i really wonder why there is lots of streams? is one video one stream?<br />
</p><p>thanks.</p></div><div id="question-tags" class="tags-container tags">tcp.stream youtube tcp wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 May '16, 05:43</strong></p><img src="https://secure.gravatar.com/avatar/a2097107eecb9ea2f8282e67c8020de0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kutlant&#39;s gravatar image" /><p>kutlant<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kutlant has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-52429" class="comments-container"></div><div id="comment-tools-52429" class="comment-tools"></div><div class="clear"></div><div id="comment-52429-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="52433"></span>

<div id="answer-container-52433" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52433-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Your best bet would probably be to close youtube (and any other apps), restart your capture, and then look at the the streams that get started after you open up youtube and start up a video. You can find the beginning of these streams if you filter or search on TCP SYNs (tcp.flags.syn == 1). You will then have a better idea of what is related to your youtube usage.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 May '16, 07:31</strong></p><img src="https://secure.gravatar.com/avatar/ba1199f4d360c53a6cc8aa6aa5da37c8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ryber&#39;s gravatar image" /><p>ryber<br />
<span class="score" title="146 reputation points">146</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ryber has one accepted answer">16%</span></p></div></div><div id="comments-container-52433" class="comments-container"><span id="52441"></span><div id="comment-52441" class="comment"><div id="post-52441-score" class="comment-score"></div><div class="comment-text"><p>thank you it really helps my observation. But the thing i dont understand, i am opening a video and start capturing packets. while this i see lots of streams which has different destination ip or same dest ip with first stream. what ignites this streams to start?</p></div><div id="comment-52441-info" class="comment-info"><span class="comment-age">(11 May '16, 11:59)</span> kutlant</div></div><span id="52442"></span><div id="comment-52442" class="comment"><div id="post-52442-score" class="comment-score">1</div><div class="comment-text"><p>What exactly means "lots"? When you open a web page, it may contain a lot of components which aren't necessarily stored at the same server (IP address) like the basic html text of the page, so your browser may easily have to open tens of tcp sessions to be able to rendering the page completely. And it rarely closes these sessions immediately after fetching the data, as reuse of already open sessions saves resources.</p><p>So you need to look which of the sessions remain open but actually transfer no data (except, in some cases, keepalives) and which keep transferring large bursts of data, or just transfer the biggest volume, and that one would be the video one (due to video advertising, you may have two big-volume sessions in the capture).</p></div><div id="comment-52442-info" class="comment-info"><span class="comment-age">(11 May '16, 12:48)</span> sindy</div></div><span id="52627"></span><div id="comment-52627" class="comment"><div id="post-52627-score" class="comment-score">1</div><div class="comment-text"><p>I agree with Sindy. If you are using firefox, you can hit F12 to get a developer console. If you go to the network tab, you can see every individual HTTP connection it makes in the course of loading the page. I have never used this with Youtube, but it is usually very helpful. There is also an Inspector tab that you can use to examine different elements of the page, which might also help.</p><p>If the requests are plain HTTP, you will be able to see what they are for in the packet capture. If they are encrypted over SSL, you won't be able to see much, but you will be able to see the server cert, which may point you to what the request is for.</p></div><div id="comment-52627-info" class="comment-info"><span class="comment-age">(16 May '16, 09:50)</span> ryber</div></div><span id="52672"></span><div id="comment-52672" class="comment"><div id="post-52672-score" class="comment-score"></div><div class="comment-text"><p>thank you very much i really understand how stuff works</p></div><div id="comment-52672-info" class="comment-info"><span class="comment-age">(17 May '16, 06:46)</span> kutlant</div></div></div><div id="comment-tools-52433" class="comment-tools"></div><div class="clear"></div><div id="comment-52433-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


+++
type = "question"
title = "Problems to find rtmp"
description = '''I can&#x27;t meet the URL to download a video, i could like to know how see the rtmp for this link http://www.alfaconcursos.com.br/cursos/detalhe/329/caixa_economica_federal_caixa.html how i can see the paramenters by this movie with wireshark? i am trying to down with rtmpdump... any idea?'''
date = "2013-11-07T15:16:00Z"
lastmod = "2013-11-07T15:32:00Z"
weight = 26738
keywords = [ "rtmp", "wireshark" ]
aliases = [ "/questions/26738" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Problems to find rtmp](/questions/26738/problems-to-find-rtmp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26738-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I can't meet the URL to download a video, i could like to know how see the rtmp for this link <a href="http://www.alfaconcursos.com.br/cursos/detalhe/329/caixa_economica_federal_caixa.html">http://www.alfaconcursos.com.br/cursos/detalhe/329/caixa_economica_federal_caixa.html</a></p><p>how i can see the paramenters by this movie with wireshark? i am trying to down with rtmpdump... any idea?</p></div><div id="question-tags" class="tags-container tags">rtmp wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Nov '13, 15:16</strong></p><img src="https://secure.gravatar.com/avatar/dbf5776259deb8ecf86a6e3102892143?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sm86&#39;s gravatar image" /><p>Sm86<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sm86 has no accepted answers">0%</span></p></div></div><div id="comments-container-26738" class="comments-container"></div><div id="comment-tools-26738" class="comment-tools"></div><div class="clear"></div><div id="comment-26738-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26739"></span>

<div id="answer-container-26739" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26739-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>There is no cleartext RTMP involved. There is a flash player (JW player) embedded that 'might' use RTMPS (RTMP over SSL), as the <strong>whole communication is encrypted, as soon as the video plays</strong>. Unless you have further debugging tools for that flash player (JW player) or you have access to the server private keys, you won't be able to decrypt the data and thus your won't be able to dissect RTMP (if it is used at all - you simply can't tell because of the encryption).</p><p>However: If you look at the source code of the page, you'll find some Javascript code that refers to RTMPS, so chances are that its being used.</p><p>So, to answer your question:</p><blockquote><p>i could like to know how see the rtmp for this link</p></blockquote><p>unless you can decrypt the traffic somehow (debugging the player or access to the keys), you won't be able to know anything about 'the rtmp for this link'</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Nov '13, 15:32</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-26739" class="comments-container"><span id="26747"></span><div id="comment-26747" class="comment"><div id="post-26747-score" class="comment-score"></div><div class="comment-text"><p>Well, i have the SecurityToken key, to acess the server and download the movie but i need always the correct link. I am amateur in this so, if you have some idea to down this, i could try...</p></div><div id="comment-26747-info" class="comment-info"><span class="comment-age">(07 Nov '13, 15:54)</span> Sm86</div></div><span id="26749"></span><div id="comment-26749" class="comment"><div id="post-26749-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Well, i have the SecurityToken key, to acess the server</p></blockquote><p>What do you mean? You can log into that server (www.alfaconcursos.com.br) via RDP or ssh and have admin access?</p><p>Even if so, that won't help you, as the video is downloaded from 187.103.38.22 (www.51a31bcacc912.streamlock.net)</p></div><div id="comment-26749-info" class="comment-info"><span class="comment-age">(07 Nov '13, 15:56)</span> Kurt Knochner ♦</div></div><span id="26751"></span><div id="comment-26751" class="comment"><div id="post-26751-score" class="comment-score"></div><div class="comment-text"><p>I'm sorry, maybe my english is a little bad. But i am not admin that site...</p><p>I bought this course, and some videos are protected and others not so much. With rtmpdump I got some videos, after I discovered the tokensecurety. But now, I can't find the correct link. it's down from this site: <span>rtmps://51a31bcacc912.streamlock.net/alfaconcursos2s</span> but i need the second parament like "mp4:200/....."</p></div><div id="comment-26751-info" class="comment-info"><span class="comment-age">(07 Nov '13, 16:44)</span> Sm86</div></div><span id="26752"></span><div id="comment-26752" class="comment"><div id="post-26752-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I bought this course, <strong>and some videos are protected</strong> and others not so much.</p></blockquote><p>Well, I guess there is a good reason why they are protected !??!</p><blockquote><p>it's down from this site: <span>rtmps://51a31bcacc912.streamlock.net/alfaconcursos2s</span> but i need the second parament like "mp4:200/....."</p></blockquote><p>As you can't decrypt the traffic, you will <strong>not be able</strong> to find that link/parameter.</p><p>I guess the encryption is there to prevent people from doing exactly that.</p></div><div id="comment-26752-info" class="comment-info"><span class="comment-age">(07 Nov '13, 16:51)</span> Kurt Knochner ♦</div></div><span id="26757"></span><div id="comment-26757" class="comment"><div id="post-26757-score" class="comment-score"></div><div class="comment-text"><p>I guess they have good reasons to do it. As I have also good to take down this limit. The reason is to protect their interests and mine is to be able to study anywhere. I want to study in the mobile phone during the day, when I have free time and the platform does not allow. In this case I must seek to meet, after all I paid for it. =( By the way If i did, i come back to talk about... Anyway, thanks so much!</p></div><div id="comment-26757-info" class="comment-info"><span class="comment-age">(07 Nov '13, 17:10)</span> Sm86</div></div><span id="26760"></span><div id="comment-26760" class="comment not_top_scorer"><div id="post-26760-score" class="comment-score"></div><div class="comment-text"><blockquote><p>In this case I must seek to meet, after all I paid for it.</p></blockquote><p>well, then have a look at a video download helper plugin for your browser: <a href="https://www.google.com/?q=firefox+video+downloader">https://www.google.com/?q=firefox+video+downloader</a></p></div><div id="comment-26760-info" class="comment-info"><span class="comment-age">(07 Nov '13, 17:22)</span> Kurt Knochner ♦</div></div><span id="26766"></span><div id="comment-26766" class="comment not_top_scorer"><div id="post-26766-score" class="comment-score"></div><div class="comment-text"><p>I tryed but nothing. I am search some similar way...</p></div><div id="comment-26766-info" class="comment-info"><span class="comment-age">(07 Nov '13, 20:47)</span> Sm86</div></div><span id="26772"></span><div id="comment-26772" class="comment not_top_scorer"><div id="post-26772-score" class="comment-score"></div><div class="comment-text"><p><a href="https://www.google.com/?q=jwplayer+save+video">Ya old buddy google has some hints</a> ;-)</p></div><div id="comment-26772-info" class="comment-info"><span class="comment-age">(08 Nov '13, 04:37)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-26739" class="comment-tools"><span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a></div><div class="clear"></div><div id="comment-26739-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


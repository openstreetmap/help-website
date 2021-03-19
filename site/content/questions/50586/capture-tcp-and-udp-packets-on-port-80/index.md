+++
type = "question"
title = "Capture TCP and UDP packets on port 80"
description = '''can you capture TCP and UDP packets on port 80? i saw the filter command tcp.port == 80 || udp.port == 80 but thats just an or so i changed it to &quot;and&quot; with tcp.port == 80 &amp;amp;&amp;amp; udp.port == 80 but that didnt do much of anything. any help would be nice thank you'''
date = "2016-02-29T13:55:00Z"
lastmod = "2016-02-29T16:21:00Z"
weight = 50586
keywords = [ "capture", "udp", "tcp" ]
aliases = [ "/questions/50586" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Capture TCP and UDP packets on port 80](/questions/50586/capture-tcp-and-udp-packets-on-port-80)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50586-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>can you capture TCP and UDP packets on port 80? i saw the filter command tcp.port == 80 || udp.port == 80 but thats just an or so i changed it to "and" with tcp.port == 80 &amp;&amp; udp.port == 80 but that didnt do much of anything. any help would be nice thank you</p></div><div id="question-tags" class="tags-container tags">capture udp tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Feb '16, 13:55</strong></p><img src="https://secure.gravatar.com/avatar/4e0df0968118e28c9e48374dbbd124f5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cadel546&#39;s gravatar image" /><p>cadel546<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cadel546 has no accepted answers">0%</span></p></div></div><div id="comments-container-50586" class="comments-container"></div><div id="comment-tools-50586" class="comment-tools"></div><div class="clear"></div><div id="comment-50586-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="50591"></span>

<div id="answer-container-50591" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50591-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>You original display filter was correct.</p><p>With both the capture and display filters you are specifying what packets you want to see/capture. With the display filter "tcp.port == 80 || udp.port == 80" you are looking for packets which are TCP or UDP ports 80.</p><p>With the display filter "tcp.port == 80 &amp;&amp; udp.port == 80" you are looking for traffic which is TCP and UDP port 80 however a packet cannot be both TCP and UDP at the same time (without complicated encapsulation that's out of scope of this thread anyway).</p><p>Luke</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Feb '16, 16:21</strong></p><img src="https://secure.gravatar.com/avatar/6ab3787b37488d06770b0e81aa9a0bc6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sludge3000&#39;s gravatar image" /><p>sludge3000<br />
<span class="score" title="61 reputation points">61</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sludge3000 has one accepted answer">50%</span></p></div></div><div id="comments-container-50591" class="comments-container"><span id="50592"></span><div id="comment-50592" class="comment"><div id="post-50592-score" class="comment-score"></div><div class="comment-text"><p>That's what I needed to know. I had an idea but I wasn't sure thank you so much</p></div><div id="comment-50592-info" class="comment-info"><span class="comment-age">(29 Feb '16, 16:27)</span> cadel546</div></div></div><div id="comment-tools-50591" class="comment-tools"></div><div class="clear"></div><div id="comment-50591-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="50587"></span>

<div id="answer-container-50587" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50587-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Those filters are display filters. If you are trying to filter during a capture, you need to provide the correct filter:</p><p>port 80</p><p>If you want to filter all HTTP traffic, then it would be</p><p>port 80 or port 8080</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Feb '16, 14:34</strong></p><img src="https://secure.gravatar.com/avatar/d9cf592a79eafbc3b2a8b3f38cf38362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amato_C&#39;s gravatar image" /><p>Amato_C<br />
<span class="score" title="1098 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amato_C has 15 accepted answers">14%</span></p></div></div><div id="comments-container-50587" class="comments-container"><span id="50588"></span><div id="comment-50588" class="comment"><div id="post-50588-score" class="comment-score"></div><div class="comment-text"><p>Yeah I forgot to mention that just display filters is fine. But even when I write udp &amp;&amp; TCP in the display filter is not showing anything so I'm wondering if there's anything wrong with my wireshark installation or something</p></div><div id="comment-50588-info" class="comment-info"><span class="comment-age">(29 Feb '16, 14:40)</span> cadel546</div></div><span id="50589"></span><div id="comment-50589" class="comment"><div id="post-50589-score" class="comment-score"></div><div class="comment-text"><p>I was thinking because you can only listen to one thing at a time on the same port?? Yeah..I don't really know</p></div><div id="comment-50589-info" class="comment-info"><span class="comment-age">(29 Feb '16, 15:18)</span> cadel546</div></div></div><div id="comment-tools-50587" class="comment-tools"></div><div class="clear"></div><div id="comment-50587-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


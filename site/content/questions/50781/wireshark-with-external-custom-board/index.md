+++
type = "question"
title = "Wireshark with external custom board"
description = '''Hi, we are planning to use Wireshark to display Wi-Fi packets which are captured by external Wi-Fi sniffer board. The board itself has USB connection which is recognized as COM PORT on the PC. Can someone help us how to start? Thanks.'''
date = "2016-03-09T04:47:00Z"
lastmod = "2016-03-09T05:30:00Z"
weight = 50781
keywords = [ "wifi", "board", "custom" ]
aliases = [ "/questions/50781" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark with external custom board](/questions/50781/wireshark-with-external-custom-board)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50781-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50781-score" class="post-score" title="current number of votes">0</div><span id="post-50781-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>we are planning to use Wireshark to display Wi-Fi packets which are captured by external Wi-Fi sniffer board. The board itself has USB connection which is recognized as COM PORT on the PC. Can someone help us how to start? Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wifi" rel="tag" title="see questions tagged &#39;wifi&#39;">wifi</span> <span class="post-tag tag-link-board" rel="tag" title="see questions tagged &#39;board&#39;">board</span> <span class="post-tag tag-link-custom" rel="tag" title="see questions tagged &#39;custom&#39;">custom</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Mar '16, 04:47</strong></p><img src="https://secure.gravatar.com/avatar/ecb035afa09278098406c9e3e0c8f802?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lhend&#39;s gravatar image" /><p><span>lhend</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lhend has no accepted answers">0%</span></p></div></div><div id="comments-container-50781" class="comments-container"><span id="50782"></span><div id="comment-50782" class="comment"><div id="post-50782-score" class="comment-score"></div><div class="comment-text"><p>The first thing I would ask myself before even obtaining such a board is what transmission speed of the "serial port" its USB part supports. While currently supported WiFi aerial bitrates are in tens of Mbps, USB2.0 has a maximum bitrate of 480 Mbps which actually means about 280 Mbps, but this mode usually doesn't come together with the serial ("com") port model, so you may find yourself limited to 12 Mbps theoretical rate which effectively means about 8.</p><p>Unless you can download the data faster than you capture them, you'd have to have a lot of RAM on the board and still its size would set a limit to your captures' size/duration.</p><p>If the board's USB interface could behave as a gigabit Ethernet over USB 3.0, that would be a completely different story - no bottleneck and much simpler software interface as you could feed such a GbE interface with the frames captured on WiFi augmented with a simple encapsulation header and capture them using the standard libpcap/WinPcap, rather than deploying the extcap model.</p></div><div id="comment-50782-info" class="comment-info"><span class="comment-age">(09 Mar '16, 05:11)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-50781" class="comment-tools"></div><div class="clear"></div><div id="comment-50781-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50783"></span>

<div id="answer-container-50783" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50783-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50783-score" class="post-score" title="current number of votes">0</div><span id="post-50783-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You'll likely have to look at writing an extcap plugin. extcap allows an external capturing process to feed the captured traffic into Wireshark.</p><p>There's the original SharkFest presentation about extcap <a href="https://sharkfest.wireshark.org/sharkfest.13/presentations/NAP-11_Expanding-Wireshark-Beyond-Ethernet-and-Network-Interfaces_Kershaw-Ryan.pdf">here</a>, the extcap man page <a href="https://www.wireshark.org/docs/man-pages/extcap.html">here</a> and in toe Wireshark source\doc directory there's <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob_plain;f=doc/README.extcap;hb=HEAD">README.extcap</a>. The last item is probably the most up-to-date resource.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Mar '16, 05:30</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-50783" class="comments-container"></div><div id="comment-tools-50783" class="comment-tools"></div><div class="clear"></div><div id="comment-50783-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


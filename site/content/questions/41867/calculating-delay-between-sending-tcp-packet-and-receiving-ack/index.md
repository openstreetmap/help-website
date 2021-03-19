+++
type = "question"
title = "[closed] calculating delay between sending tcp packet and receiving ack"
description = '''I am sending traffic from one computer to another and capturing the packets using wireshark, i need to calculate the waiting time between sending a packet and receiving the acknowledgment to that packet but i can&#x27;t find the sending time and receiving time of each packet ..any help??  Noting that: wh...'''
date = "2015-04-26T14:15:00Z"
lastmod = "2015-04-26T14:57:00Z"
weight = 41867
keywords = [ "delay", "tcppackets", "wireshark" ]
aliases = [ "/questions/41867" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] calculating delay between sending tcp packet and receiving ack](/questions/41867/calculating-delay-between-sending-tcp-packet-and-receiving-ack)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41867-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41867-score" class="post-score" title="current number of votes">0</div><span id="post-41867-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am sending traffic from one computer to another and capturing the packets using wireshark, i need to calculate the waiting time between sending a packet and receiving the acknowledgment to that packet but i can't find the sending time and receiving time of each packet ..any help?? Noting that: what i understand is that the time stamp is the time at which the packet was captured not sent/received so i couldn't use it.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-delay" rel="tag" title="see questions tagged &#39;delay&#39;">delay</span> <span class="post-tag tag-link-tcppackets" rel="tag" title="see questions tagged &#39;tcppackets&#39;">tcppackets</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Apr '15, 14:15</strong></p><img src="https://secure.gravatar.com/avatar/890399e77f2c0c0ff2f75ea2f43d3ff8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yas1234&#39;s gravatar image" /><p><span>yas1234</span><br />
<span class="score" title="16 reputation points">16</span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yas1234 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> closed <strong>26 Apr '15, 14:57</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-41867" class="comments-container"><span id="41872"></span><div id="comment-41872" class="comment"><div id="post-41872-score" class="comment-score"></div><div class="comment-text"><p>This is effectively the same question as you asked previously: <a href="https://ask.wireshark.org/questions/41776/thinking-time-and-waiting-time-delay-tcp">https://ask.wireshark.org/questions/41776/thinking-time-and-waiting-time-delay-tcp</a> where the answer I gave was very similar to that which <span>@Jim Aragon</span> as supplied here.</p><p>Please don't raise another question if you don't feel your original has been answered correctly, instead add amplifying comments to that question or its answers.</p></div><div id="comment-41872-info" class="comment-info"><span class="comment-age">(26 Apr '15, 14:57)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-41867" class="comment-tools"></div><div class="clear"></div><div id="comment-41867-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Duplicate Question" by grahamb 26 Apr '15, 14:57

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41870"></span>

<div id="answer-container-41870" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41870-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41870-score" class="post-score" title="current number of votes">0</div><span id="post-41870-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can't find the sending and receiving times because they are not in the packets. As. You've noticed, the capture time is what Wireshark records. The capture time is the same as the receiving time <em>on the capture system</em>. To get the time between sending a packet and receiving a reply, you need to capture on the sending system, or as close to it as possible, so that the capture times correspond to the sending and receiving times.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Apr '15, 14:29</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-41870" class="comments-container"></div><div id="comment-tools-41870" class="comment-tools"></div><div class="clear"></div><div id="comment-41870-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


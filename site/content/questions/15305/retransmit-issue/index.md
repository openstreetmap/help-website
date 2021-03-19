+++
type = "question"
title = "Retransmit issue"
description = ''' HI,  My server send packet to 202.162 but the packet retransmit again..Kindly advice... Is my server fault ? Thanks in advance..'''
date = "2012-10-26T23:05:00Z"
lastmod = "2012-10-27T02:41:00Z"
weight = 15305
keywords = [ "retransmission" ]
aliases = [ "/questions/15305" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Retransmit issue](/questions/15305/retransmit-issue)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15305-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p><img src="https://osqa-ask.wireshark.org/upfiles/image001_1.jpg" alt="alt text" /> HI,</p><p>My server send packet to 202.162 but the packet retransmit again..Kindly advice... Is my server fault ? Thanks in advance..</p></div><div id="question-tags" class="tags-container tags">retransmission</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Oct '12, 23:05</strong></p><img src="https://secure.gravatar.com/avatar/b8cbaa9ee7d5bf40e4c8f703e3197880?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="suarez123&#39;s gravatar image" /><p>suarez123<br />
<span class="score" title="1 reputation points">1</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="suarez123 has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 27 Oct '12, 05:30</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-15305" class="comments-container"></div><div id="comment-tools-15305" class="comment-tools"></div><div class="clear"></div><div id="comment-15305-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="15309"></span>

<div id="answer-container-15309" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15309-score" class="post-score" title="current number of votes">4</div></div></td><td><div class="item-right"><div class="answer-body"><p>Looks like the server is unwilling to respond after the initial three way handshake, or the packets do not make it through at all. If I am not mistaken you have a RTT of about 5ms, and the retransmissions come after a couple of hundred ms, so they're not just out of orders etc. From the timing I guess you're capturing on (or very close to) the client, so what you might do to solve this issue would be to capture close at the server instead. If you test again you can tell if the packets all make it through to the server.</p><p>My bet is that you have some kind of MTU problem, because the small SYN-SYN/ACK-ACK packets get through fine and fast, but the larger request packets after them do not. So that would be another thing you can do: find out if there's a MTU less than 1500 between client and server, because the client network and the server network DO have an MTU of 1500 (deducted from the MSS of 1460 in the SYN-SYN/ACK packets). Maybe there is one connection that has an MTU of 576 (which would be the minimum MTU allowed for IPv4) somewhere in the middle, which would block your 604 byte packets.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Oct '12, 02:41</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-15309" class="comments-container"><span id="15422"></span><div id="comment-15422" class="comment"><div id="post-15422-score" class="comment-score"></div><div class="comment-text"><p>thank you Jasper.. So the culprit is 202.162 ? do u have mediafire link to download wireeshark tutorial ?</p></div><div id="comment-15422-info" class="comment-info"><span class="comment-age">(31 Oct '12, 09:03)</span> suarez123</div></div></div><div id="comment-tools-15309" class="comment-tools"></div><div class="clear"></div><div id="comment-15309-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


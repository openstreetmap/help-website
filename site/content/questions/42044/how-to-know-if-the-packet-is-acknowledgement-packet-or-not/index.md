+++
type = "question"
title = "how to know if the packet is acknowledgement packet or not"
description = '''i am capturing packets using wireshark and almost all of them contain the [ack] flag ..i don&#x27;t know how to differentiate between data packets and tcp acknowledgement packets when all of them carry the flag [ack],so any help ?!'''
date = "2015-05-03T15:55:00Z"
lastmod = "2015-05-06T09:03:00Z"
weight = 42044
keywords = [ "ack", "tcp", "wireshark" ]
aliases = [ "/questions/42044" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how to know if the packet is acknowledgement packet or not](/questions/42044/how-to-know-if-the-packet-is-acknowledgement-packet-or-not)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42044-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42044-score" class="post-score" title="current number of votes">0</div><span id="post-42044-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>i am capturing packets using wireshark and almost all of them contain the [ack] flag ..i don't know how to differentiate between data packets and tcp acknowledgement packets when all of them carry the flag [ack],so any help ?!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ack" rel="tag" title="see questions tagged &#39;ack&#39;">ack</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 May '15, 15:55</strong></p><img src="https://secure.gravatar.com/avatar/890399e77f2c0c0ff2f75ea2f43d3ff8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yas1234&#39;s gravatar image" /><p><span>yas1234</span><br />
<span class="score" title="16 reputation points">16</span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yas1234 has no accepted answers">0%</span></p></div></div><div id="comments-container-42044" class="comments-container"></div><div id="comment-tools-42044" class="comment-tools"></div><div class="clear"></div><div id="comment-42044-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="42046"></span>

<div id="answer-container-42046" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42046-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42046-score" class="post-score" title="current number of votes">1</div><span id="post-42046-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Every packet except the initial SYN packet has the ACK flag set. That's normal. If you're looking for packets acknowledging data without carrying data themselves just look for packets that have a TCP payload length of zero. You can filter for those by using "tcp.len==0".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 May '15, 16:12</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-42046" class="comments-container"><span id="42051"></span><div id="comment-42051" class="comment"><div id="post-42051-score" class="comment-score"></div><div class="comment-text"><p>thank you so much it's clear now !</p></div><div id="comment-42051-info" class="comment-info"><span class="comment-age">(04 May '15, 02:20)</span> <span class="comment-user userinfo">yas1234</span></div></div><span id="42058"></span><div id="comment-42058" class="comment"><div id="post-42058-score" class="comment-score"></div><div class="comment-text"><p><span>@yas1234</span>: If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions. For extra points you can up vote the answer (thumb up).</p></div><div id="comment-42058-info" class="comment-info"><span class="comment-age">(04 May '15, 08:39)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="42125"></span><div id="comment-42125" class="comment"><div id="post-42125-score" class="comment-score"></div><div class="comment-text"><p>okay but if i have a packet carrying data AND ack ..how do i know that this packet contains acknowledgement if the payload is not equal to zero, i mean then i will know it's a data pkt not data+ack</p></div><div id="comment-42125-info" class="comment-info"><span class="comment-age">(06 May '15, 06:06)</span> <span class="comment-user userinfo">yas1234</span></div></div><span id="42143"></span><div id="comment-42143" class="comment"><div id="post-42143-score" class="comment-score"></div><div class="comment-text"><p><strong>every</strong> packet except the first SYN packet has the ACK flag. So there is no data packet without ACk.</p></div><div id="comment-42143-info" class="comment-info"><span class="comment-age">(06 May '15, 09:03)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-42046" class="comment-tools"></div><div class="clear"></div><div id="comment-42046-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


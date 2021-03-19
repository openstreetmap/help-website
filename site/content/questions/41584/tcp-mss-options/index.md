+++
type = "question"
title = "TCP-MSS-Options"
description = '''Hai, 1) Data is from A to B and ACK is from B to A 2) TCP sections got established with MSS as 1460 from both sides  No Question: Q1) I understood, tcp segment will not send the data beyond 1460 bytes per segment, AM I right ??? Q2) I understood TCPDUMP and wire shark work at interface level, if soo...'''
date = "2015-04-19T23:48:00Z"
lastmod = "2015-04-20T02:25:00Z"
weight = 41584
keywords = [ "tcp-mss-options" ]
aliases = [ "/questions/41584" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [TCP-MSS-Options](/questions/41584/tcp-mss-options)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41584-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41584-score" class="post-score" title="current number of votes">0</div><span id="post-41584-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hai,</p><p>1) Data is from A to B and ACK is from B to A 2) TCP sections got established with MSS as 1460 from both sides</p><p>No Question:</p><p>Q1) I understood, tcp segment will not send the data beyond 1460 bytes per segment, AM I right ??? Q2) I understood TCPDUMP and wire shark work at interface level, if soooooo How to capture the data at transport layer level ( Not at interface / wire level) ???</p><p>Regards</p><p>Hai Jasper,</p><p>Regarding Q2,</p><p>I am sending 2800 Bytes of UDP data, for MTU size of 1500 data can be sent in two packets as it is going to fragmented by IP layer...</p><p>I understood at transport layer data is one segment of 3000 bytes.... How i can capture data at transport layer (i.e before IP layer)</p><p>After IP layer, using wireshark / TCP dump i can capture two packets...</p><p>Regards</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcp-mss-options" rel="tag" title="see questions tagged &#39;tcp-mss-options&#39;">tcp-mss-options</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Apr '15, 23:48</strong></p><img src="https://secure.gravatar.com/avatar/ce1843f92a1c18db26bc79b3afa9bd50?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="srinu_bel&#39;s gravatar image" /><p><span>srinu_bel</span><br />
<span class="score" title="20 reputation points">20</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="srinu_bel has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>20 Apr '15, 02:16</strong> </span></p></div></div><div id="comments-container-41584" class="comments-container"></div><div id="comment-tools-41584" class="comment-tools"></div><div class="clear"></div><div id="comment-41584-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41589"></span>

<div id="answer-container-41589" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41589-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41589-score" class="post-score" title="current number of votes">0</div><span id="post-41589-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>1) yes. 2) both capture <strong>packets</strong>, not layers. So everything in a packet is recorded.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Apr '15, 02:05</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-41589" class="comments-container"><span id="41592"></span><div id="comment-41592" class="comment"><div id="post-41592-score" class="comment-score"></div><div class="comment-text"><p>Hai Jasper,</p><p>Regarding Q2,</p><p>I am sending 2800 Bytes of UDP data, for MTU size of 1500 data can be sent in two packets as it is going to fragmented by IP layer...</p><p>I understood at transport layer data is one segment of 3000 bytes.... How i can capture data at transport layer (i.e before IP layer)</p><p>After IP layer, using wireshark / TCP dump i can capture two packets...</p><p>Regards</p></div><div id="comment-41592-info" class="comment-info"><span class="comment-age">(20 Apr '15, 02:16)</span> <span class="comment-user userinfo">srinu_bel</span></div></div><span id="41593"></span><div id="comment-41593" class="comment"><div id="post-41593-score" class="comment-score"></div><div class="comment-text"><p>I'm not sure I understand the question - do you try to capture the 2800 bytes in one block? If so, you can't do that with Wireshark/TCP dump on the Wire, because it looks at network packets, not application data blocks.</p><p>Though sometimes it works if you do local captures, but only for outgoing packets, and those are essentially capture errors.</p><p>P.S: please do not add comment <strong>and</strong> update your question with the same text, it makes the flow really hard to read.</p></div><div id="comment-41593-info" class="comment-info"><span class="comment-age">(20 Apr '15, 02:25)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-41589" class="comment-tools"></div><div class="clear"></div><div id="comment-41589-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


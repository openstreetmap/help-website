+++
type = "question"
title = "udp header"
description = '''how do one determine the length in bytes of each of the UDP header fields?'''
date = "2014-11-03T04:07:00Z"
lastmod = "2014-11-04T00:34:00Z"
weight = 37552
keywords = [ "udp" ]
aliases = [ "/questions/37552" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [udp header](/questions/37552/udp-header)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37552-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37552-score" class="post-score" title="current number of votes">0</div><span id="post-37552-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>how do one determine the length in bytes of each of the UDP header fields?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-udp" rel="tag" title="see questions tagged &#39;udp&#39;">udp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Nov '14, 04:07</strong></p><img src="https://secure.gravatar.com/avatar/bb653e78c70ec6eace3e8e909bf774bb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Seaford%20Bacchas&#39;s gravatar image" /><p><span>Seaford Bacchas</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Seaford Bacchas has no accepted answers">0%</span></p></div></div><div id="comments-container-37552" class="comments-container"><span id="37562"></span><div id="comment-37562" class="comment"><div id="post-37562-score" class="comment-score"></div><div class="comment-text"><p>So you are saying each field is 2 bytes?</p></div><div id="comment-37562-info" class="comment-info"><span class="comment-age">(03 Nov '14, 16:24)</span> <span class="comment-user userinfo">Seaford Bacchas</span></div></div></div><div id="comment-tools-37552" class="comment-tools"></div><div class="clear"></div><div id="comment-37552-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37553"></span>

<div id="answer-container-37553" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37553-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37553-score" class="post-score" title="current number of votes">1</div><span id="post-37553-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I'd recommend reading the RFCs, e.g. <a href="https://www.ietf.org/rfc/rfc768.txt">https://www.ietf.org/rfc/rfc768.txt</a>. The UDP header has a fixed length of 8 bytes: Source Port, Destination Port (2 bytes each), Length (2 Bytes), and a (more or less optional) Checksum (2 Bytes).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Nov '14, 04:11</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-37553" class="comments-container"><span id="37554"></span><div id="comment-37554" class="comment"><div id="post-37554-score" class="comment-score"></div><div class="comment-text"><p>Or maybe the <a href="http://www.tcpipguide.com/free/t_UDPMessageFormat.htm">TCP/IP guide</a>.</p></div><div id="comment-37554-info" class="comment-info"><span class="comment-age">(03 Nov '14, 05:02)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="37563"></span><div id="comment-37563" class="comment"><div id="post-37563-score" class="comment-score"></div><div class="comment-text"><p>So you are saying each field is 2 bytes?</p></div><div id="comment-37563-info" class="comment-info"><span class="comment-age">(03 Nov '14, 16:25)</span> <span class="comment-user userinfo">Seaford Bacchas</span></div></div><span id="37565"></span><div id="comment-37565" class="comment"><div id="post-37565-score" class="comment-score"></div><div class="comment-text"><p>Yep, UDP header fields are 2 bytes each.</p></div><div id="comment-37565-info" class="comment-info"><span class="comment-age">(04 Nov '14, 00:34)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-37553" class="comment-tools"></div><div class="clear"></div><div id="comment-37553-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


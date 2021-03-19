+++
type = "question"
title = "Peculiar SACK behavior"
description = '''Hi all,  I&#x27;m having a hard time wrapping my head around some peculiar traffic, and I&#x27;m hoping that the big brains here may be able to offer some insight.  In short ... this looks plain wrong:  42737 2014-12-02 17:06:04.822626 0.000004 2.057276000 0.001216000 10.10.10.10 20.20.20.20 118 27081 80 TCP ...'''
date = "2014-12-02T10:10:00Z"
lastmod = "2015-09-24T15:03:00Z"
weight = 38281
keywords = [ "sack" ]
aliases = [ "/questions/38281" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Peculiar SACK behavior](/questions/38281/peculiar-sack-behavior)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38281-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38281-score" class="post-score" title="current number of votes">0</div><span id="post-38281-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>I'm having a hard time wrapping my head around some peculiar traffic, and I'm hoping that the big brains here may be able to offer some insight.</p><p>In short ... this looks plain wrong:</p><p>42737 2014-12-02 17:06:04.822626 0.000004 2.057276000 0.001216000 10.10.10.10 20.20.20.20 118 27081 80 TCP 66 63960 63960 1921089026 1921091786 1306854153 4011022929 [TCP Dup ACK 42718#1] 27081→80 [ACK] Seq=1306854153 Ack=4011022929 Win=63960 Len=0 SLE=1921089026 SRE=1921091786</p><p>Src: 10.10.10.10 (third party ISP network) Dst: 20.20.20.20 (FE server)</p><p>Seq=1306854153 Ack=4011022929</p><p>SLE=1921089026 SRE=1921091786</p><p>I'm having a hard time wrapping my head around this behavior.</p><p>Could this be caused by a transit device (firewall/NAT) mucking about with the SACK option data?</p><p>Thanks, Kevin</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-sack" rel="tag" title="see questions tagged &#39;sack&#39;">sack</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Dec '14, 10:10</strong></p><img src="https://secure.gravatar.com/avatar/ad02d2c94bb362339b32ac9e2ca8468e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Qwert&#39;s gravatar image" /><p><span>Qwert</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Qwert has no accepted answers">0%</span></p></div></div><div id="comments-container-38281" class="comments-container"></div><div id="comment-tools-38281" class="comment-tools"></div><div class="clear"></div><div id="comment-38281-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="38284"></span>

<div id="answer-container-38284" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38284-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38284-score" class="post-score" title="current number of votes">0</div><span id="post-38284-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Thanks to another thread for putting me on the right track. This is looking like a /?/cosmetic/?/ anomaly due to TSO in use by the NIC. There seems to be a set value that the NIC/TCPstack/(wireshark) is applying to the SLE/SRE values on a per session basis.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Dec '14, 15:00</strong></p><img src="https://secure.gravatar.com/avatar/ad02d2c94bb362339b32ac9e2ca8468e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Qwert&#39;s gravatar image" /><p><span>Qwert</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Qwert has no accepted answers">0%</span></p></div></div><div id="comments-container-38284" class="comments-container"></div><div id="comment-tools-38284" class="comment-tools"></div><div class="clear"></div><div id="comment-38284-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="46128"></span>

<div id="answer-container-46128" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46128-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46128-score" class="post-score" title="current number of votes">0</div><span id="post-46128-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wow .. been a while since I've been on this site.</p><p>This had nothing to do with TSO, and in hindsight, I recognize that my assumption to that effect was based in ignorance.</p><p>This behavior was, indeed, due to a load balancing appliance operating in inline mode that was not supporting SACK rewrites.</p><h1 id="live-and-learn">live-and-learn</h1></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Sep '15, 15:03</strong></p><img src="https://secure.gravatar.com/avatar/ad02d2c94bb362339b32ac9e2ca8468e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Qwert&#39;s gravatar image" /><p><span>Qwert</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Qwert has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>24 Sep '15, 15:06</strong> </span></p></div></div><div id="comments-container-46128" class="comments-container"></div><div id="comment-tools-46128" class="comment-tools"></div><div class="clear"></div><div id="comment-46128-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


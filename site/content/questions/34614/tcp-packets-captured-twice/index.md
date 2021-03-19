+++
type = "question"
title = "TCP packets captured twice"
description = '''Hello, I trying to debug some slowness on an application. Even if I think that these slowness are not related to an issue on network, I saw some strange behavior on TCP retransmission. I got a lot of duplicate ACK and TCP retransmission in the dump. While looking deeper in packets (heavy server resp...'''
date = "2014-07-12T05:23:00Z"
lastmod = "2014-07-16T14:17:00Z"
weight = 34614
keywords = [ "retransmissions" ]
aliases = [ "/questions/34614" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [TCP packets captured twice](/questions/34614/tcp-packets-captured-twice)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34614-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34614-score" class="post-score" title="current number of votes">0</div><span id="post-34614-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I trying to debug some slowness on an application. Even if I think that these slowness are not related to an issue on network, I saw some strange behavior on TCP retransmission.</p><p>I got a lot of duplicate ACK and TCP retransmission in the dump. While looking deeper in packets (heavy server response), I noticed that duplicate packets have same sequence number (quite normal) but are captured <strong>exactly</strong> at the same time.</p><p>It could have been a bug during capture but this behavior does not happen on each packet.</p><p>Dump is take on a citrix client.</p><p>Does sombody have an explanation?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-retransmissions" rel="tag" title="see questions tagged &#39;retransmissions&#39;">retransmissions</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Jul '14, 05:23</strong></p><img src="https://secure.gravatar.com/avatar/6d37aac49af1d517094d309b3032c300?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kireito&#39;s gravatar image" /><p><span>kireito</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kireito has no accepted answers">0%</span></p></div></div><div id="comments-container-34614" class="comments-container"></div><div id="comment-tools-34614" class="comment-tools"></div><div class="clear"></div><div id="comment-34614-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34618"></span>

<div id="answer-container-34618" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34618-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34618-score" class="post-score" title="current number of votes">2</div><span id="post-34618-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If the ip.id is the same in both packets, then the packet was just traced twice. You could 'dedup' the trace using <code>editcap -d infile outfile</code></p><p>Regards Matthias<br />
</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jul '14, 01:42</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></p></div></div><div id="comments-container-34618" class="comments-container"><span id="34713"></span><div id="comment-34713" class="comment"><div id="post-34713-score" class="comment-score"></div><div class="comment-text"><p>Thank You for the answer. The dedup on the file has resolved some problems but not all.</p><p>In fact packet are flag with interface id 0 and some other with interface id 1.</p><p>Now I got a dump from server side, witch is more cleaner. This doesn't resolv my slowness problems but it's possible to troubleshoot.</p></div><div id="comment-34713-info" class="comment-info"><span class="comment-age">(16 Jul '14, 14:17)</span> <span class="comment-user userinfo">kireito</span></div></div></div><div id="comment-tools-34618" class="comment-tools"></div><div class="clear"></div><div id="comment-34618-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


+++
type = "question"
title = "Interpreting Packets displayed with ip filter set to xyz.com"
description = '''I&#x27;ve set my filter to display packets sent to and from xyz.com and i get a bunch of info with TCP and TLS packets. I&#x27;m very very new to networking and basically using wireshark for a project. I&#x27;d be grateful if you could throw light on this question.  The TCP and TLS packets being shown on wireshark...'''
date = "2013-11-14T16:58:00Z"
lastmod = "2013-11-14T23:06:00Z"
weight = 27023
keywords = [ "tls", "packets", "tcp" ]
aliases = [ "/questions/27023" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Interpreting Packets displayed with ip filter set to xyz.com](/questions/27023/interpreting-packets-displayed-with-ip-filter-set-to-xyzcom)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27023-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27023-score" class="post-score" title="current number of votes">0</div><span id="post-27023-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've set my filter to display packets sent to and from xyz.com and i get a bunch of info with TCP and TLS packets. I'm very very new to networking and basically using wireshark for a project. I'd be grateful if you could throw light on this question.</p><ol><li>The TCP and TLS packets being shown on wireshark, are they the ones which are ACTUALLY sent over the internet to the destination ip address or is there much more to it? Also, are TLS packets sent with TCP packets (if tcp packets are sent over the internet as reported on wireshark) over the internet or do they just stop at our routers?</li></ol></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tls" rel="tag" title="see questions tagged &#39;tls&#39;">tls</span> <span class="post-tag tag-link-packets" rel="tag" title="see questions tagged &#39;packets&#39;">packets</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Nov '13, 16:58</strong></p><img src="https://secure.gravatar.com/avatar/9d419a502a5404c664fcffaf9616e58a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="anony&#39;s gravatar image" /><p><span>anony</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="anony has no accepted answers">0%</span></p></div></div><div id="comments-container-27023" class="comments-container"></div><div id="comment-tools-27023" class="comment-tools"></div><div class="clear"></div><div id="comment-27023-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27026"></span>

<div id="answer-container-27026" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27026-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27026-score" class="post-score" title="current number of votes">0</div><span id="post-27026-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Oh, this really looks like a question from an absolute novice.so this one might be of interest to you</p><p><a href="http://www.youtube.com/watch?v=ncaA4WX4jYQ">Warriors of the net</a></p><p>Yes</p><ul><li>IP packets are actually sent to or received from an IP (Internet Protocol) network.</li><li>The transport layer that is used for <em>most</em> internet traffic (Web HTTP) is called TCP.</li><li>Ontop of that you see a TLS (SSL Security Layer) which encrypts you application data.</li></ul><p>And yes, TLS requires TCP as the transport protocol and those packets -hopefully- don't stop at the (IP)-Routers, otherwise you won't be happy as you don't get anything back in your Firefox ...</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Nov '13, 23:06</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>15 Nov '13, 01:03</strong> </span></p></div></div><div id="comments-container-27026" class="comments-container"></div><div id="comment-tools-27026" class="comment-tools"></div><div class="clear"></div><div id="comment-27026-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


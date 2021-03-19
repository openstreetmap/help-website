+++
type = "question"
title = "Many TCP retransmission and tcp out-of-order found for slow connection"
description = '''Hello, I was troubleshooting a webpage connection issue and got many &quot;tcp retransmission&quot; &amp;amp; &quot;tcp out-of-order&quot;, and the actual connection was hang for over 100 seconds before the page could be shown. Below are some of the examples: https://drive.google.com/open?id=0BzRlJRE0N1eMMW5Lenp2dHVNa0k   ...'''
date = "2015-08-21T21:25:00Z"
lastmod = "2015-08-23T07:11:00Z"
weight = 45306
keywords = [ "tcp_retransmission" ]
aliases = [ "/questions/45306" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Many TCP retransmission and tcp out-of-order found for slow connection](/questions/45306/many-tcp-retransmission-and-tcp-out-of-order-found-for-slow-connection)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45306-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45306-score" class="post-score" title="current number of votes">0</div><span id="post-45306-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I was troubleshooting a webpage connection issue and got many "tcp retransmission" &amp; "tcp out-of-order", and the actual connection was hang for over 100 seconds before the page could be shown. Below are some of the examples:</p><p><a href="https://drive.google.com/open?id=0BzRlJRE0N1eMMW5Lenp2dHVNa0k">https://drive.google.com/open?id=0BzRlJRE0N1eMMW5Lenp2dHVNa0k</a></p><p><img src="https://lh5.googleusercontent.com/oP6nJu5vxvS0YFH2Tnsn6cOLZWd7SRhR88Ws5on_rKyAoR-RAGMz8_-9Z61aKYuat3EMGWmfr_Xzvik=w1648-h804" alt="alt text" /> Anyone has any idea?</p><p>Thanks in advance.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcp_retransmission" rel="tag" title="see questions tagged &#39;tcp_retransmission&#39;">tcp_retransmission</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Aug '15, 21:25</strong></p><img src="https://secure.gravatar.com/avatar/ad7b84a3c964110ed6c435380a752925?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Illidan%20Stormrage&#39;s gravatar image" /><p><span>Illidan Stor...</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Illidan Stormrage has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>21 Aug '15, 23:07</strong> </span></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span></p></div></div><div id="comments-container-45306" class="comments-container"></div><div id="comment-tools-45306" class="comment-tools"></div><div class="clear"></div><div id="comment-45306-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45307"></span>

<div id="answer-container-45307" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45307-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45307-score" class="post-score" title="current number of votes">1</div><span id="post-45307-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>All packets are inbound and all packets are traced twice and so are not real retransmissions. Looks like you need to de-duplicate the trace using <code>editcap -D</code> to get rid of the false alarms.</p><p>Regards Matthias<br />
</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Aug '15, 23:05</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></p></div></div><div id="comments-container-45307" class="comments-container"><span id="45317"></span><div id="comment-45317" class="comment"><div id="post-45317-score" class="comment-score"></div><div class="comment-text"><p>Hi mrEEde,</p><p>Thanks for the reply, would check why there was only uni-directional traffic and revert.</p></div><div id="comment-45317-info" class="comment-info"><span class="comment-age">(23 Aug '15, 07:11)</span> <span class="comment-user userinfo">Illidan Stor...</span></div></div></div><div id="comment-tools-45307" class="comment-tools"></div><div class="clear"></div><div id="comment-45307-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


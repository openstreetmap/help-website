+++
type = "question"
title = "TCPdump review"
description = '''What is going on with this packet? 4500 0030 0d69 4000 8006 3188 c0a8 1d01 c0a8 1d85 0453 008b 69f0 5c23 0000 0000 7002 4000 bc56 0000 0204 05b4 0101 0402 4500 0030 0277 4000 8006 3c7a c0a8 1d85 c0a8 1d01 008b 0453 3e29 8d15 69f0 5c24 7012 faf0 3616 0000 0204 05b4 0101 8d16 4500 0070 0d6b 4000 8006 ...'''
date = "2014-11-14T19:46:00Z"
lastmod = "2014-11-14T22:35:00Z"
weight = 37877
keywords = [ "tcppackets" ]
aliases = [ "/questions/37877" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [TCPdump review](/questions/37877/tcpdump-review)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37877-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37877-score" class="post-score" title="current number of votes">0</div><span id="post-37877-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>What is going on with this packet? 4500 0030 0d69 4000 8006 3188 c0a8 1d01 c0a8 1d85 0453 008b 69f0 5c23 0000 0000 7002 4000 bc56 0000 0204 05b4 0101 0402</p><p>4500 0030 0277 4000 8006 3c7a c0a8 1d85 c0a8 1d01 008b 0453 3e29 8d15 69f0 5c24 7012 faf0 3616 0000 0204 05b4 0101 8d16</p><p>4500 0070 0d6b 4000 8006 3146 c0a8 1d01 C0a8 1d85 0453 008b 69f0 5c24 3e29 8d16 5018 4470 a92e 0000 8100 0044 2043 4b46</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcppackets" rel="tag" title="see questions tagged &#39;tcppackets&#39;">tcppackets</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Nov '14, 19:46</strong></p><img src="https://secure.gravatar.com/avatar/687a348caf94dab10e6f9692f909ede3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nooniebunn&#39;s gravatar image" /><p><span>nooniebunn</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nooniebunn has no accepted answers">0%</span></p></div></div><div id="comments-container-37877" class="comments-container"></div><div id="comment-tools-37877" class="comment-tools"></div><div class="clear"></div><div id="comment-37877-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37878"></span>

<div id="answer-container-37878" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37878-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37878-score" class="post-score" title="current number of votes">1</div><span id="post-37878-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I'm not sure what exactly you are asking here but this is a strange 3-way (2-way) handshake.</p><ul><li>The SYN_ACK has the SACK option overridden with 0x8d16</li><li>The ACK packet contains data</li></ul><p>It would certainly save time if you'd provide a capture file instead of a truncated hexadecimal print of packets.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Nov '14, 22:35</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></div></div><div id="comments-container-37878" class="comments-container"></div><div id="comment-tools-37878" class="comment-tools"></div><div class="clear"></div><div id="comment-37878-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


+++
type = "question"
title = "Wireshark showing timestamps header instead of SEQ/ACK analysis"
description = '''Hello, My wireshark is showing Timestamps after Options header in TCP instead of SEQ/ACK analysis. Where are the settings to change it? Thanks'''
date = "2015-04-27T15:07:00Z"
lastmod = "2015-04-27T23:07:00Z"
weight = 41899
keywords = [ "timestamps" ]
aliases = [ "/questions/41899" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Wireshark showing timestamps header instead of SEQ/ACK analysis](/questions/41899/wireshark-showing-timestamps-header-instead-of-seqack-analysis)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41899-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41899-score" class="post-score" title="current number of votes">0</div><span id="post-41899-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>My wireshark is showing Timestamps after Options header in TCP instead of SEQ/ACK analysis. Where are the settings to change it?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-timestamps" rel="tag" title="see questions tagged &#39;timestamps&#39;">timestamps</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Apr '15, 15:07</strong></p><img src="https://secure.gravatar.com/avatar/39356e003826b924c6b683f177900afb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iWireshark&#39;s gravatar image" /><p><span>iWireshark</span><br />
<span class="score" title="16 reputation points">16</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iWireshark has no accepted answers">0%</span></p></div></div><div id="comments-container-41899" class="comments-container"></div><div id="comment-tools-41899" class="comment-tools"></div><div class="clear"></div><div id="comment-41899-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="41906"></span>

<div id="answer-container-41906" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41906-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41906-score" class="post-score" title="current number of votes">0</div><span id="post-41906-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="iWireshark has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You will not see "[SEQ/ACK analysis]" in the SYN packet of a TCP connection, but you should see it in all other packets. If not, go to Edit &gt; Preferences &gt; Protocols &gt; TCP and enable "Analyze TCP sequence numbers."</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Apr '15, 23:07</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>28 Apr '15, 01:25</strong> </span></p></div></div><div id="comments-container-41906" class="comments-container"></div><div id="comment-tools-41906" class="comment-tools"></div><div class="clear"></div><div id="comment-41906-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="41904"></span>

<div id="answer-container-41904" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41904-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41904-score" class="post-score" title="current number of votes">0</div><span id="post-41904-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>So you are saying you do not see [SEQ/ACK Analysis] field after the TCP timestamp option?<br />
You need to enable 'Display hidden protocol items' in Edit - Preferences - Protocols to make those visible. But it is not a 'instead', you will still see the TCP timestamp option.<br />
<img src="https://osqa-ask.wireshark.org/upfiles/Screenshot-226.png" alt="alt text" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Apr '15, 21:30</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></br></p></img></div></div><div id="comments-container-41904" class="comments-container"></div><div id="comment-tools-41904" class="comment-tools"></div><div class="clear"></div><div id="comment-41904-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


+++
type = "question"
title = "40 MHz + 40 MHz lower BW meaning in wireshark"
description = '''What does 40 MHz + 40 MHz lower or 40 MHz + 40 MHz upper mean in wireshark? This is how wireshark represents bandwidth in my trace? Is this bandwidth equal to 40 MHz or 80 MHz? '''
date = "2016-10-31T22:07:00Z"
lastmod = "2016-11-04T16:16:00Z"
weight = 56887
keywords = [ "bandwidth", "wireshark", "in" ]
aliases = [ "/questions/56887" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [40 MHz + 40 MHz lower BW meaning in wireshark](/questions/56887/40-mhz-40-mhz-lower-bw-meaning-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56887-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56887-score" class="post-score" title="current number of votes">0</div><span id="post-56887-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>What does 40 MHz + 40 MHz lower or 40 MHz + 40 MHz upper mean in wireshark? This is how wireshark represents bandwidth in my trace? Is this bandwidth equal to 40 MHz or 80 MHz?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-bandwidth" rel="tag" title="see questions tagged &#39;bandwidth&#39;">bandwidth</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span> <span class="post-tag tag-link-in" rel="tag" title="see questions tagged &#39;in&#39;">in</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Oct '16, 22:07</strong></p><img src="https://secure.gravatar.com/avatar/af9be6f06a1796e714e11c49026054e2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Harshada%20Kelkar&#39;s gravatar image" /><p><span>Harshada Kelkar</span><br />
<span class="score" title="21 reputation points">21</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Harshada Kelkar has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> converted <strong>04 Nov '16, 12:25</strong> </span></p></div></div><div id="comments-container-56887" class="comments-container"></div><div id="comment-tools-56887" class="comment-tools"></div><div class="clear"></div><div id="comment-56887-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57002"></span>

<div id="answer-container-57002" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57002-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57002-score" class="post-score" title="current number of votes">1</div><span id="post-57002-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Harshada Kelkar has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This is an active discussion:</p><p><a href="https://ask.wireshark.org/questions/56800/vht-bandwidth-representation-in-wireshark">https://ask.wireshark.org/questions/56800/vht-bandwidth-representation-in-wireshark</a></p><p>This means you are transmitting at 40MHz bandwidth. Depending on the specific field, the string represented could be differemt. This would be a 40MHz bandwidth frame sent as 802.11ac phy. Can you verify, or post a short trace with some of these frames? I can't seem to generate these exact ones, though from the link I am able to generate similar. The primary channel should be in the upper 40MHz of the 80MHz-wide total bandwidth.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Nov '16, 16:16</strong></p><img src="https://secure.gravatar.com/avatar/0a47ef51dd9c9996d194a4983295f5a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bob%20Jones&#39;s gravatar image" /><p><span>Bob Jones</span><br />
<span class="score" title="1014 reputation points"><span>1.0k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bob Jones has 19 accepted answers">21%</span></p></div></div><div id="comments-container-57002" class="comments-container"></div><div id="comment-tools-57002" class="comment-tools"></div><div class="clear"></div><div id="comment-57002-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


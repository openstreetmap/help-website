+++
type = "question"
title = "&quot;Empty&quot; Data Record Transfer Request message is interpreted as &quot;Malformed Packet&quot;"
description = '''Hi, all In the description of 3GPP TS 32.295, empty test packet(s) (with no CDR payload in the Data Record Packet IE but just the other parts of the message frame) in some error handling scenarios. &quot;If an &quot;empty packet&quot; is to be sent, then the Data Record Packet IE contains only the Type (with value...'''
date = "2014-07-09T23:30:00Z"
lastmod = "2014-07-10T01:18:00Z"
weight = 34535
keywords = [ "gtp-prime", "cdr" ]
aliases = [ "/questions/34535" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# ["Empty" Data Record Transfer Request message is interpreted as "Malformed Packet"](/questions/34535/empty-data-record-transfer-request-message-is-interpreted-as-malformed-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34535-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34535-score" class="post-score" title="current number of votes">0</div><span id="post-34535-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, all</p><p>In the description of 3GPP TS 32.295, empty test packet(s) (with no CDR payload in the Data Record Packet IE but just the other parts of the message frame) in some error handling scenarios. "If an "empty packet" is to be sent, then the Data Record Packet IE contains only the Type (with value 252 in decimal) and the Length (with value 0) fields.".</p><p>However, the "empty" packet is interpreted as "Malformed Packet(Exception occurred)" in the wireshark release of 1.12.0-rc2, 1.10.8, 1.11.2. Is there any bugs in wireshark for interpreting this kind of messages?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-gtp-prime" rel="tag" title="see questions tagged &#39;gtp-prime&#39;">gtp-prime</span> <span class="post-tag tag-link-cdr" rel="tag" title="see questions tagged &#39;cdr&#39;">cdr</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Jul '14, 23:30</strong></p><img src="https://secure.gravatar.com/avatar/c2f80712757aea21e4da741e148f1e0a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="onedayoneapple&#39;s gravatar image" /><p><span>onedayoneapple</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="onedayoneapple has no accepted answers">0%</span></p></div></div><div id="comments-container-34535" class="comments-container"></div><div id="comment-tools-34535" class="comment-tools"></div><div class="clear"></div><div id="comment-34535-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34541"></span>

<div id="answer-container-34541" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34541-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34541-score" class="post-score" title="current number of votes">0</div><span id="post-34541-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, that's probably a bug; please file a bug report at <a href="http://bugs.wireshark.org/">the Wireshark Bugzilla</a>, preferably with a capture demonstrating the problem attached, so we can track it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jul '14, 01:18</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-34541" class="comments-container"></div><div id="comment-tools-34541" class="comment-tools"></div><div class="clear"></div><div id="comment-34541-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


+++
type = "question"
title = "SS7 BSSAP Protocol"
description = '''I wonder how does Wireshark know that there is BSSAP underlying the SCCP protocol ?'''
date = "2013-01-29T04:06:00Z"
lastmod = "2013-01-30T03:40:00Z"
weight = 18030
keywords = [ "ss7", "bssap" ]
aliases = [ "/questions/18030" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [SS7 BSSAP Protocol](/questions/18030/ss7-bssap-protocol)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18030-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18030-score" class="post-score" title="current number of votes">0</div><span id="post-18030-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I wonder how does Wireshark know that there is BSSAP underlying the SCCP protocol ?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ss7" rel="tag" title="see questions tagged &#39;ss7&#39;">ss7</span> <span class="post-tag tag-link-bssap" rel="tag" title="see questions tagged &#39;bssap&#39;">bssap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Jan '13, 04:06</strong></p><img src="https://secure.gravatar.com/avatar/049954c19a42f88823709640897cb958?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ahmediukas&#39;s gravatar image" /><p><span>ahmediukas</span><br />
<span class="score" title="21 reputation points">21</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ahmediukas has no accepted answers">0%</span></p></div></div><div id="comments-container-18030" class="comments-container"></div><div id="comment-tools-18030" class="comment-tools"></div><div class="clear"></div><div id="comment-18030-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="18035"></span>

<div id="answer-container-18035" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18035-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18035-score" class="post-score" title="current number of votes">1</div><span id="post-18035-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ahmediukas has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>By the sub system number, SSN 98 is tied to BSSAP, changable by a protocol preference.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Jan '13, 05:58</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-18035" class="comments-container"><span id="18049"></span><div id="comment-18049" class="comment"><div id="post-18049-score" class="comment-score"></div><div class="comment-text"><p>Isnt SSN specified as 250 (BSC) and 251 (MSC) ? And further, it is in the SCCP DataForm1 message, so no SSN's provided (as in UDT) Example: <a href="http://cloudshark.org/captures/ea49319c49ca">http://cloudshark.org/captures/ea49319c49ca</a></p></div><div id="comment-18049-info" class="comment-info"><span class="comment-age">(29 Jan '13, 11:09)</span> <span class="comment-user userinfo">ahmediukas</span></div></div><span id="18050"></span><div id="comment-18050" class="comment"><div id="post-18050-score" class="comment-score">1</div><div class="comment-text"><p>BSSAP is also detected heuristically, SCCP has a heuristic table where dissectors can register to have a peek a the packet and claim it if it's determined to be the protocol in question - might not be correct.</p></div><div id="comment-18050-info" class="comment-info"><span class="comment-age">(29 Jan '13, 11:19)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="18081"></span><div id="comment-18081" class="comment"><div id="post-18081-score" class="comment-score"></div><div class="comment-text"><p>I am pretty sure, GSM machines knows its BSSAP somehow, they doesn't heuristically dissector packet. Even if MTP/SCTP addresses are for them.</p></div><div id="comment-18081-info" class="comment-info"><span class="comment-age">(30 Jan '13, 01:13)</span> <span class="comment-user userinfo">ahmediukas</span></div></div><span id="18090"></span><div id="comment-18090" class="comment"><div id="post-18090-score" class="comment-score"></div><div class="comment-text"><p>Sure, but the question was how Wireshark detects them.</p></div><div id="comment-18090-info" class="comment-info"><span class="comment-age">(30 Jan '13, 03:40)</span> <span class="comment-user userinfo">Anders ♦</span></div></div></div><div id="comment-tools-18035" class="comment-tools"></div><div class="clear"></div><div id="comment-18035-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


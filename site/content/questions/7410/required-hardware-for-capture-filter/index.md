+++
type = "question"
title = "required hardware for capture filter"
description = '''I&#x27;ve been trying to setup Wireshark (V1.6.2) capture filter at different windows systems and failed. At one particular PC I used 3 different network adapters. One of them (Intel PRO/1000 PL) worked (example of capture filter: port 5060 or port 53), two others (Realthek RTL8139 and VIA Rhine III) usi...'''
date = "2011-11-14T03:44:00Z"
lastmod = "2011-11-16T03:31:00Z"
weight = 7410
keywords = [ "capture-filter" ]
aliases = [ "/questions/7410" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [required hardware for capture filter](/questions/7410/required-hardware-for-capture-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7410-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7410-score" class="post-score" title="current number of votes">0</div><span id="post-7410-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've been trying to setup Wireshark (V1.6.2) capture filter at different windows systems and failed. At one particular PC I used 3 different network adapters. One of them (Intel PRO/1000 PL) worked (example of capture filter: port 5060 or port 53), two others (Realthek RTL8139 and VIA Rhine III) using the same filter failed (Wireshark does not capture anything). Everything else works without problems using these adaptors. For me it seems that there are certain requirements the network adaptor has to comply with, to support Capture Filters with Wireshark. Can anybody tell which are those?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture-filter" rel="tag" title="see questions tagged &#39;capture-filter&#39;">capture-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Nov '11, 03:44</strong></p><img src="https://secure.gravatar.com/avatar/52ad30c06760b5d9ee6ddd1c881db694?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rolstein&#39;s gravatar image" /><p><span>rolstein</span><br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rolstein has no accepted answers">0%</span></p></div></div><div id="comments-container-7410" class="comments-container"></div><div id="comment-tools-7410" class="comment-tools"></div><div class="clear"></div><div id="comment-7410-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7412"></span>

<div id="answer-container-7412" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7412-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7412-score" class="post-score" title="current number of votes">1</div><span id="post-7412-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Look into vlans...</p><p><a href="http://www.mail-archive.com/wireshark-users@wireshark.org/msg04406.html">This post</a> explains that.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Nov '11, 04:13</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-7412" class="comments-container"><span id="7413"></span><div id="comment-7413" class="comment"><div id="post-7413-score" class="comment-score"></div><div class="comment-text"><p>sorry the post you referred to, doesn't really help me. Maybe my problem description is not sufficient. The syntax of the capture filter (see above) generally works, but only with one of the three network adapters. It is somehow dependend on the hardware I use.</p></div><div id="comment-7413-info" class="comment-info"><span class="comment-age">(14 Nov '11, 04:34)</span> <span class="comment-user userinfo">rolstein</span></div></div><span id="7468"></span><div id="comment-7468" class="comment"><div id="post-7468-score" class="comment-score"></div><div class="comment-text"><p>What Jaap is saying is that capture filter syntax for the same traffic can be different depending on whether the NIC is stripping vlan tags or not.</p><p>Have a look at unfiltered captures on all three NICs of the same traffic and see whether some have vlan tagging in the frames and some don't.</p></div><div id="comment-7468-info" class="comment-info"><span class="comment-age">(16 Nov '11, 03:31)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-7412" class="comment-tools"></div><div class="clear"></div><div id="comment-7412-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


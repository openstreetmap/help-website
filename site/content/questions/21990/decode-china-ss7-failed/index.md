+++
type = "question"
title = "Decode China ss7 failed."
description = '''Hi, I found it is failed when the wireshark(version 1.10.0) decode rounting lable message of the signalling system 7 (The codec used 24 bits for DPC and OPC,however,The wireshark decode DPC and OPC uses 14 bits at present).How can I do to slove the problem? Thanks in advance. Best regards, Jason'''
date = "2013-06-12T20:37:00Z"
lastmod = "2013-06-13T20:41:00Z"
weight = 21990
keywords = [ "decode", "ss7", "dpc", "opc" ]
aliases = [ "/questions/21990" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Decode China ss7 failed.](/questions/21990/decode-china-ss7-failed)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21990-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21990-score" class="post-score" title="current number of votes">0</div><span id="post-21990-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I found it is failed when the wireshark(version 1.10.0) decode rounting lable message of the signalling system 7 (The codec used 24 bits for DPC and OPC,however,The wireshark decode DPC and OPC uses 14 bits at present).How can I do to slove the problem? Thanks in advance.</p><p>Best regards, Jason</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-decode" rel="tag" title="see questions tagged &#39;decode&#39;">decode</span> <span class="post-tag tag-link-ss7" rel="tag" title="see questions tagged &#39;ss7&#39;">ss7</span> <span class="post-tag tag-link-dpc" rel="tag" title="see questions tagged &#39;dpc&#39;">dpc</span> <span class="post-tag tag-link-opc" rel="tag" title="see questions tagged &#39;opc&#39;">opc</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Jun '13, 20:37</strong></p><img src="https://secure.gravatar.com/avatar/7c69725c2dc03e3b481b79e946c8d372?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JasonCui&#39;s gravatar image" /><p><span>JasonCui</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JasonCui has no accepted answers">0%</span></p></div></div><div id="comments-container-21990" class="comments-container"></div><div id="comment-tools-21990" class="comment-tools"></div><div class="clear"></div><div id="comment-21990-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22001"></span>

<div id="answer-container-22001" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22001-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22001-score" class="post-score" title="current number of votes">1</div><span id="post-22001-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Did you try adjusting your MTP3 protocol preferences between ANSI and ITU standard? Under edit &gt; Preferences &gt; Protocols &gt; MTP3.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jun '13, 03:51</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p><span>Quadratic</span><br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div></div><div id="comments-container-22001" class="comments-container"><span id="22007"></span><div id="comment-22007" class="comment"><div id="post-22007-score" class="comment-score"></div><div class="comment-text"><p>Starting in 1.10.0 there is also a preference to tell the MTP3 dissector to try to heuristically determine the protocol standard. It was designed primarily to automatically distinguish between ITU and ANSI but it should also work with the China variant.</p></div><div id="comment-22007-info" class="comment-info"><span class="comment-age">(13 Jun '13, 06:16)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div><span id="22027"></span><div id="comment-22027" class="comment"><div id="post-22027-score" class="comment-score"></div><div class="comment-text"><p>Really? That's awesome. I can't tell you how many times I've had to walk people through that protocol setting.</p></div><div id="comment-22027-info" class="comment-info"><span class="comment-age">(13 Jun '13, 13:53)</span> <span class="comment-user userinfo">Quadratic</span></div></div><span id="22035"></span><div id="comment-22035" class="comment"><div id="post-22035-score" class="comment-score"></div><div class="comment-text"><p>Thanks,I solved it according to your answer.</p></div><div id="comment-22035-info" class="comment-info"><span class="comment-age">(13 Jun '13, 20:41)</span> <span class="comment-user userinfo">JasonCui</span></div></div></div><div id="comment-tools-22001" class="comment-tools"></div><div class="clear"></div><div id="comment-22001-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


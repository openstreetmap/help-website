+++
type = "question"
title = "how does wireshark know the given packet is rtmp packet"
description = '''I am building a RTMP parser for which I have certain use cases as given below -   How to know if the packet I am parsing is RTMP handshake packet or RTMP message packet ? This is because I might start monitoring the RTMP stream after the handshake has been done between the client and the server.   H...'''
date = "2016-10-03T05:14:00Z"
lastmod = "2016-10-06T05:26:00Z"
weight = 56087
keywords = [ "rtmp", "wireshark" ]
aliases = [ "/questions/56087" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how does wireshark know the given packet is rtmp packet](/questions/56087/how-does-wireshark-know-the-given-packet-is-rtmp-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56087-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56087-score" class="post-score" title="current number of votes">0</div><span id="post-56087-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am building a RTMP parser for which I have certain use cases as given below -</p><ol><li><p>How to know if the packet I am parsing is RTMP handshake packet or RTMP message packet ? This is because I might start monitoring the RTMP stream after the handshake has been done between the client and the server.</p></li><li><p>How to know I am at the start of the RTMP packet ? This is because I might be parsing from the middle of the RTMP packet or from anywhere inside the packet body. In that case how to determine how many bytes to skip.</p></li><li><p>How to know the payload inside TCP is of RTMP ?? The data can correspond to any other data too.Hence how to determine the payload consists of rtmp data ? Any help on this ?? I am stuck with this for quite some time and I am unable to figure out anything from the adobe specification for RTMP.Information in the specification is very limited .</p></li></ol></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rtmp" rel="tag" title="see questions tagged &#39;rtmp&#39;">rtmp</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Oct '16, 05:14</strong></p><img src="https://secure.gravatar.com/avatar/c46f8e6bef16f207d8c9aa367f697b6c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="abhinay&#39;s gravatar image" /><p><span>abhinay</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="abhinay has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>03 Oct '16, 07:07</strong> </span></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span></p></div></div><div id="comments-container-56087" class="comments-container"></div><div id="comment-tools-56087" class="comment-tools"></div><div class="clear"></div><div id="comment-56087-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56093"></span>

<div id="answer-container-56093" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56093-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56093-score" class="post-score" title="current number of votes">0</div><span id="post-56093-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>From the comments in <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob;f=epan/dissectors/packet-rtmpt.c">the dissector code</a>, there's little to go on.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Oct '16, 06:55</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-56093" class="comments-container"><span id="56113"></span><div id="comment-56113" class="comment"><div id="post-56113-score" class="comment-score"></div><div class="comment-text"><p>Can you please specify which part in the code does the given thing ??</p></div><div id="comment-56113-info" class="comment-info"><span class="comment-age">(03 Oct '16, 22:11)</span> <span class="comment-user userinfo">abhinay</span></div></div><span id="56185"></span><div id="comment-56185" class="comment"><div id="post-56185-score" class="comment-score"></div><div class="comment-text"><p><span>@Jaap</span> Is there a way to get only RTMP data in a file from wireshark's captured data ??</p></div><div id="comment-56185-info" class="comment-info"><span class="comment-age">(06 Oct '16, 05:26)</span> <span class="comment-user userinfo">abhinay</span></div></div></div><div id="comment-tools-56093" class="comment-tools"></div><div class="clear"></div><div id="comment-56093-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


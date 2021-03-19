+++
type = "question"
title = "How wire shark calculated the  lost RTP packets"
description = '''How wire shark calculated the lost RTP packets. When I do select Telephony-&amp;gt;RTP-&amp;gt;Show All streams it shows the number of RTP packets received from a source ip:port to dest ip:port. It also shows number of packets lost under LOST tab. How wireshark is calculating the packet loss here from a sou...'''
date = "2016-02-12T03:27:00Z"
lastmod = "2016-02-12T07:57:00Z"
weight = 50131
keywords = [ "rtp_lost" ]
aliases = [ "/questions/50131" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How wire shark calculated the lost RTP packets](/questions/50131/how-wire-shark-calculated-the-lost-rtp-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50131-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50131-score" class="post-score" title="current number of votes">0</div><span id="post-50131-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How wire shark calculated the lost RTP packets. When I do select Telephony-&gt;RTP-&gt;Show All streams it shows the number of RTP packets received from a source ip:port to dest ip:port. It also shows number of packets lost under LOST tab. How wireshark is calculating the packet loss here from a source.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rtp_lost" rel="tag" title="see questions tagged &#39;rtp_lost&#39;">rtp_lost</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Feb '16, 03:27</strong></p><img src="https://secure.gravatar.com/avatar/60b4a3a349cd54639c34cb66698f54d7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Subhendu%20Kumar%20Das&#39;s gravatar image" /><p><span>Subhendu Kum...</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Subhendu Kumar Das has no accepted answers">0%</span></p></div></div><div id="comments-container-50131" class="comments-container"></div><div id="comment-tools-50131" class="comment-tools"></div><div class="clear"></div><div id="comment-50131-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50132"></span>

<div id="answer-container-50132" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50132-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50132-score" class="post-score" title="current number of votes">0</div><span id="post-50132-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The RTP header contains a sequence number which monotonously grows by 1 (and rolls over from 65535-&gt;0). Wireshark (and also normal applications processing RTP) use this field to verify correct ordering and loss of RTP packets.</p><p>This also means that Wireshark may report lost packets even in RTP flows where no actual loss has happened if the source of the RTP has created a gap in the RTP sequence numbers for any reason.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Feb '16, 03:47</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 Feb '16, 03:50</strong> </span></p></div></div><div id="comments-container-50132" class="comments-container"><span id="50142"></span><div id="comment-50142" class="comment"><div id="post-50142-score" class="comment-score"></div><div class="comment-text"><p>Note that the actual implementation is (IIRC) a bit more simplistic than this which has been known to cause problems (like Wireshark reporting <em>negative</em> 95% packet loss). IIRC Wireshark basically subtracts (modulo 65535) the last sequence number from the first and then compares this to the number of packets received. When the sequence numbers jump around this can cause funny results (I think there's at least one bug open about this).</p><p>But fundamentally this answer is spot-on.</p></div><div id="comment-50142-info" class="comment-info"><span class="comment-age">(12 Feb '16, 06:26)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div><span id="50145"></span><div id="comment-50145" class="comment"><div id="post-50145-score" class="comment-score"></div><div class="comment-text"><p><span>@JeffMorriss</span>, I assume your description is only applicable for the statistics part, and that the detailed analysis still allows to "jump at next anomaly" the way it did before, i.e. if there is a single lost packet, this fact is highlighted in the packet list of the stream?</p></div><div id="comment-50145-info" class="comment-info"><span class="comment-age">(12 Feb '16, 07:05)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="50148"></span><div id="comment-50148" class="comment"><div id="post-50148-score" class="comment-score"></div><div class="comment-text"><p>Well the part I was talking about was the statistics part (based on experience I got while trying to fix some bug). I've never worked with the "jump to next anomaly" part (I don't normally work with the VoIP stuff).</p></div><div id="comment-50148-info" class="comment-info"><span class="comment-age">(12 Feb '16, 07:23)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div><span id="50155"></span><div id="comment-50155" class="comment"><div id="post-50155-score" class="comment-score"></div><div class="comment-text"><p>FWIW the bug I'm thinking about is <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=10665">bug 10665</a>.</p></div><div id="comment-50155-info" class="comment-info"><span class="comment-age">(12 Feb '16, 07:57)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div></div><div id="comment-tools-50132" class="comment-tools"></div><div class="clear"></div><div id="comment-50132-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


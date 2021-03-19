+++
type = "question"
title = "UDP to RTP"
description = '''Is decoding UDP to RTP and seeing packet loss valid? My source protocol is all UDP and the only packet loss seen is when you convert to RTP and analyze the RTP Streams. Since UDP has no sequencing i&#x27;m curious if it&#x27;s even valid to convert it and see out of sequence packets with packet loss. thanks, ...'''
date = "2011-07-05T15:42:00Z"
lastmod = "2011-07-05T23:16:00Z"
weight = 4916
keywords = [ "loss", "udp", "rtp", "packet" ]
aliases = [ "/questions/4916" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [UDP to RTP](/questions/4916/udp-to-rtp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4916-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4916-score" class="post-score" title="current number of votes">1</div><span id="post-4916-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is decoding UDP to RTP and seeing packet loss valid? My source protocol is all UDP and the only packet loss seen is when you convert to RTP and analyze the RTP Streams. Since UDP has no sequencing i'm curious if it's even valid to convert it and see out of sequence packets with packet loss.</p><p>thanks,</p><p>Justin Oney</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-loss" rel="tag" title="see questions tagged &#39;loss&#39;">loss</span> <span class="post-tag tag-link-udp" rel="tag" title="see questions tagged &#39;udp&#39;">udp</span> <span class="post-tag tag-link-rtp" rel="tag" title="see questions tagged &#39;rtp&#39;">rtp</span> <span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Jul '11, 15:42</strong></p><img src="https://secure.gravatar.com/avatar/bd0c74787ce8643020902a3fcdb217cd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="oneman23&#39;s gravatar image" /><p><span>oneman23</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="oneman23 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 Feb '12, 22:13</strong> </span></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-4916" class="comments-container"></div><div id="comment-tools-4916" class="comment-tools"></div><div class="clear"></div><div id="comment-4916-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4921"></span>

<div id="answer-container-4921" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4921-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4921-score" class="post-score" title="current number of votes">1</div><span id="post-4921-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The question is: Do you use RTP on top of UDP for your transport? I assume not.</p><p>Then the RTP analysis, resulting in the packet loss and out of sequence reports, is invalid since these use values from the RTP packets, which are not there since it's not RTP!</p><p>So to properly dissect and analyze your protocol you'll need your own dissector, and tap.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Jul '11, 23:16</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-4921" class="comments-container"></div><div id="comment-tools-4921" class="comment-tools"></div><div class="clear"></div><div id="comment-4921-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


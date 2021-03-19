+++
type = "question"
title = "Some question about quic decode result"
description = ''' As the pic above. we has some questions:   why there are two &quot;Num Ranges&quot; ?  we think it&#x27;s quic.frame_type.ack.num_range and quic.frame_type.ack.num_revived? but we does not clear that which is quic.frame_type.ack.num_range   how can we known from the Received Packet,which is the FEC complete or re...'''
date = "2016-12-28T04:44:00Z"
lastmod = "2017-01-16T23:29:00Z"
weight = 58396
keywords = [ "quic" ]
aliases = [ "/questions/58396" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Some question about quic decode result](/questions/58396/some-question-about-quic-decode-result)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58396-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58396-score" class="post-score" title="current number of votes">0</div><span id="post-58396-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p><img src="https://osqa-ask.wireshark.org/upfiles/Capture_7a2cyaT.PNG" alt="alt text" /></p><p>As the pic above. we has some questions:</p><ol><li><p>why there are two "Num Ranges" ? we think it's quic.frame_type.ack.num_range and quic.frame_type.ack.num_revived? but we does not clear that which is quic.frame_type.ack.num_range</p></li><li><p>how can we known from the Received Packet,which is the FEC complete or retransmission complete?</p></li><li><p>why there are 4 Received Packet Sequence Number is 0 ?</p></li><li><p>how to calc "Largest Observed Delta time", why not written by power（x, y）?</p></li></ol></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-quic" rel="tag" title="see questions tagged &#39;quic&#39;">quic</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Dec '16, 04:44</strong></p><img src="https://secure.gravatar.com/avatar/853d7093103a60a3b0083b42b705b99e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="neil_hao&#39;s gravatar image" /><p><span>neil_hao</span><br />
<span class="score" title="26 reputation points">26</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="neil_hao has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>28 Dec '16, 04:45</strong> </span></p></div></div><div id="comments-container-58396" class="comments-container"><span id="58400"></span><div id="comment-58400" class="comment"><div id="post-58400-score" class="comment-score"></div><div class="comment-text"><p>Can you share a capture in a publicly accessible spot, e.g. <a href="http://cloudshark.org">CloudShark</a>, Google Drive, Dropbox etc.?</p></div><div id="comment-58400-info" class="comment-info"><span class="comment-age">(28 Dec '16, 05:33)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-58396" class="comment-tools"></div><div class="clear"></div><div id="comment-58396-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58514"></span>

<div id="answer-container-58514" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58514-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58514-score" class="post-score" title="current number of votes">1</div><span id="post-58514-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="neil_hao has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hi,</p><p>1°) it is a typo on dissector fixed on <a href="https://code.wireshark.org/review/19547">https://code.wireshark.org/review/19547</a></p><p>For other question it is better to ask directly on QUIC mailing <a href="https://groups.google.com/a/chromium.org/forum/#!forum/proto-quic">https://groups.google.com/a/chromium.org/forum/#!forum/proto-quic</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Jan '17, 12:07</strong></p><img src="https://secure.gravatar.com/avatar/d62b869ec385c6bbc2c04dc7176e8ea8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alexis%20La%20Goutte&#39;s gravatar image" /><p><span>Alexis La Go...</span><br />
<span class="score" title="110 reputation points">110</span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alexis La Goutte has one accepted answer">25%</span></p></div></div><div id="comments-container-58514" class="comments-container"><span id="58827"></span><div id="comment-58827" class="comment"><div id="post-58827-score" class="comment-score"></div><div class="comment-text"><p>thanks a lot.</p></div><div id="comment-58827-info" class="comment-info"><span class="comment-age">(16 Jan '17, 23:29)</span> <span class="comment-user userinfo">neil_hao</span></div></div></div><div id="comment-tools-58514" class="comment-tools"></div><div class="clear"></div><div id="comment-58514-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


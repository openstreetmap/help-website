+++
type = "question"
title = "Dissecting stream"
description = '''Hi,  I&#x27;m developing a dissector for a protocol that turn out to be a stream. How do I dissect PDUs which span across multiple packets. Each PDU consist of 2 parts, message and parameters. Parameters consist of few additional PDUs (number can vary from 0 to 255). All PDUs are basically strings, there...'''
date = "2013-07-09T23:33:00Z"
lastmod = "2013-07-12T01:53:00Z"
weight = 22782
keywords = [ "reassembly", "pdu", "dissector", "multipart" ]
aliases = [ "/questions/22782" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Dissecting stream](/questions/22782/dissecting-stream)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22782-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22782-score" class="post-score" title="current number of votes">0</div><span id="post-22782-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I'm developing a dissector for a protocol that turn out to be a stream. How do I dissect PDUs which span across multiple packets. Each PDU consist of 2 parts, message and parameters. Parameters consist of few additional PDUs (number can vary from 0 to 255). All PDUs are basically strings, therefore variable in length.</p><p>In documentation I found section "<em>2.7.2 Modifying the pinfo struct</em>", where it's described how to deal with such packets. I have devised a function which determines whether we have enough data to dissect a parameter. I check it's output and if there's not enough data I do the following:</p><blockquote><p>pinfo-&gt;desegment_offset = offset; pinfo-&gt;desegment_len = DESEGMENT_ONE_MORE_SEGMENT; return offset;</p></blockquote><p>I see in debugging output that it reaches this stage and returns, but I don't see actual packet re-assembling.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-reassembly" rel="tag" title="see questions tagged &#39;reassembly&#39;">reassembly</span> <span class="post-tag tag-link-pdu" rel="tag" title="see questions tagged &#39;pdu&#39;">pdu</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-multipart" rel="tag" title="see questions tagged &#39;multipart&#39;">multipart</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Jul '13, 23:33</strong></p><img src="https://secure.gravatar.com/avatar/c9aa1d36ff8501f13272de4dafa34854?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andrey&#39;s gravatar image" /><p><span>Andrey</span><br />
<span class="score" title="21 reputation points">21</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andrey has one accepted answer">50%</span></p></div></div><div id="comments-container-22782" class="comments-container"></div><div id="comment-tools-22782" class="comment-tools"></div><div class="clear"></div><div id="comment-22782-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22892"></span>

<div id="answer-container-22892" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22892-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22892-score" class="post-score" title="current number of votes">0</div><span id="post-22892-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I figured it out! I falsely though that you can request more data from Wireshark at any point. But it seem like it conflicts elements you already added to the tree. So I had to implement a function that calculates length of the PDU (by reading same bytes as dissector), in case it finds that expected length is larger than remaining buffer length it asks for another segment. If test succeeds it commences dissecting.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jul '13, 01:53</strong></p><img src="https://secure.gravatar.com/avatar/c9aa1d36ff8501f13272de4dafa34854?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andrey&#39;s gravatar image" /><p><span>Andrey</span><br />
<span class="score" title="21 reputation points">21</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andrey has one accepted answer">50%</span></p></div></div><div id="comments-container-22892" class="comments-container"></div><div id="comment-tools-22892" class="comment-tools"></div><div class="clear"></div><div id="comment-22892-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


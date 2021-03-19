+++
type = "question"
title = "Why SSL &quot;client hello&quot; message has two segments"
description = '''When my server do the SSL handshake with clients, it will receives a &quot;client hello&quot; message with two segments. My server has a bug when deal with the two segments &quot;client hello&quot;. But Why SSL &quot;client hello&quot; message has two segments.The TCP MSS is 1280.  Do you have any idea? Thanks a lot.   I capture...'''
date = "2015-09-10T08:45:00Z"
lastmod = "2015-09-10T09:36:00Z"
weight = 45762
keywords = [ "ssl", "client", "segment", "hello" ]
aliases = [ "/questions/45762" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Why SSL "client hello" message has two segments](/questions/45762/why-ssl-client-hello-message-has-two-segments)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45762-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When my server do the SSL handshake with clients, it will receives a "client hello" message with two segments.</p><p>My server has a bug when deal with the two segments "client hello".</p><p>But Why SSL "client hello" message has two segments.The TCP MSS is 1280.</p><p>Do you have any idea?</p><p>Thanks a lot.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/SSLhandshake.png" alt="alt text" /></p><hr /><p>I captured packets on the clients after fixing the bug on the serer.</p><p>Before the bug was fixed, the client would send "RST" after "client hello".</p><p><img src="https://osqa-ask.wireshark.org/upfiles/SSL-client.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">ssl client segment hello</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Sep '15, 08:45</strong></p><img src="https://secure.gravatar.com/avatar/f7e669ad23f3b3d9892bd9e0b33d76db?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frank9527&#39;s gravatar image" /><p>Frank9527<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frank9527 has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 12 Sep '15, 04:22</p></div></div><div id="comments-container-45762" class="comments-container"></div><div id="comment-tools-45762" class="comment-tools"></div><div class="clear"></div><div id="comment-45762-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45763"></span>

<div id="answer-container-45763" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45763-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>There's nothing explicitly wrong with that, a correctly written server should handle that just fine.</p><p>It is odd though, that the Client Hello has been chopped into a 216 and 4 byte segments with a very small time delay between the 2.</p><p>I'm assuming the capture has been done on the server, can you capture on the client to see what's being transmitted?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Sep '15, 09:36</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></img></div></div><div id="comments-container-45763" class="comments-container"><span id="45807"></span><div id="comment-45807" class="comment"><div id="post-45807-score" class="comment-score"></div><div class="comment-text"><p>Thanks. I'm not familiar with the SSL protocol. I just think the TCP's MSS property will cause segment. Can the SSL property decide the segment?</p></div><div id="comment-45807-info" class="comment-info"><span class="comment-age">(12 Sep '15, 04:29)</span> Frank9527</div></div><span id="45813"></span><div id="comment-45813" class="comment"><div id="post-45813-score" class="comment-score"></div><div class="comment-text"><p>The MSS of 216 is causing the segmentation. Perhaps a device inbetween has MSS clamping enabled.</p></div><div id="comment-45813-info" class="comment-info"><span class="comment-age">(12 Sep '15, 08:59)</span> Roland</div></div></div><div id="comment-tools-45763" class="comment-tools"></div><div class="clear"></div><div id="comment-45763-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</hr>

</div>

</div>


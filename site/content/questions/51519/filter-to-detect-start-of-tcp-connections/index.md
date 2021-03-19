+++
type = "question"
title = "Filter to detect start of TCP connections"
description = '''I want to list the start of every TCP connection on a pcap file. I know that in order to detect the end of the connection I can use this filter tcp.flags.fin eq 1 or tcp.flags.reset eq 1, because when a TCP connection is closed, the FIN flag or the RST flag are set. But I can&#x27;t seem to find what fla...'''
date = "2016-04-08T10:47:00Z"
lastmod = "2016-04-09T18:49:00Z"
weight = 51519
keywords = [ "filter", "tcp", "wireshark" ]
aliases = [ "/questions/51519" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Filter to detect start of TCP connections](/questions/51519/filter-to-detect-start-of-tcp-connections)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51519-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51519-score" class="post-score" title="current number of votes">0</div><span id="post-51519-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to list the start of every TCP connection on a pcap file.</p><p>I know that in order to detect the end of the connection I can use this filter <code>tcp.flags.fin eq 1 or tcp.flags.reset eq 1</code>, because when a TCP connection is closed, the FIN flag or the RST flag are set.</p><p>But I can't seem to find what flags are set when a TCP connection is started.</p><p>Can anyone help me?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Apr '16, 10:47</strong></p><img src="https://secure.gravatar.com/avatar/0638835dc95bc1f5f9435471815300bc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="twistedx&#39;s gravatar image" /><p><span>twistedx</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="twistedx has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 Apr '16, 10:48</strong> </span></p></div></div><div id="comments-container-51519" class="comments-container"></div><div id="comment-tools-51519" class="comment-tools"></div><div class="clear"></div><div id="comment-51519-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51520"></span>

<div id="answer-container-51520" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51520-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51520-score" class="post-score" title="current number of votes">1</div><span id="post-51520-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="twistedx has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>tcp.flags.syn==1</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Apr '16, 11:02</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-51520" class="comments-container"><span id="51521"></span><div id="comment-51521" class="comment"><div id="post-51521-score" class="comment-score"></div><div class="comment-text"><p>Thank you!</p></div><div id="comment-51521-info" class="comment-info"><span class="comment-age">(08 Apr '16, 11:08)</span> <span class="comment-user userinfo">twistedx</span></div></div><span id="51541"></span><div id="comment-51541" class="comment"><div id="post-51541-score" class="comment-score"></div><div class="comment-text"><p>That filter will show the first two packets of the TCP handshake. Perhaps better, the following filter will show only the first packet of the handshake, the one that is actually requesting that a connection be established:</p><p>tcp.flags.syn==1 &amp;&amp; tcp.flags.ack==0</p></div><div id="comment-51541-info" class="comment-info"><span class="comment-age">(09 Apr '16, 18:49)</span> <span class="comment-user userinfo">Jim Aragon</span></div></div></div><div id="comment-tools-51520" class="comment-tools"></div><div class="clear"></div><div id="comment-51520-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


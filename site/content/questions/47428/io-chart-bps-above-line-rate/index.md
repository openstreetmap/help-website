+++
type = "question"
title = "IO Chart bps above line rate"
description = '''I am trying to understand the IO chart below, sorry I do not have the trace file. I am told this was captured with Wireshark on a laptop connected to a SPAN port. The SPAN port was being sourced from a port channel of 4Gbps.I do not have any specific details on the settings. We can see in the IO Cha...'''
date = "2015-11-09T04:34:00Z"
lastmod = "2015-11-09T18:33:00Z"
weight = 47428
keywords = [ "chart", "io" ]
aliases = [ "/questions/47428" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [IO Chart bps above line rate](/questions/47428/io-chart-bps-above-line-rate)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47428-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47428-score" class="post-score" title="current number of votes">0</div><span id="post-47428-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to understand the IO chart below, sorry I do not have the trace file. I am told this was captured with Wireshark on a laptop connected to a SPAN port. The SPAN port was being sourced from a port channel of 4Gbps.I do not have any specific details on the settings.</p><p>We can see in the IO Chart sometimes we reach 1Gbps rate but also in the screen shot we can see what I believe is a microburst up to around 3.0Gbps.</p><p>How can I understand seeing a 3.0Gbps rate while I am connected to a 1Gbps interface? Even as microburst how can IO Chart show above 1Gbps line rate.</p><p>Thank you in advance for any guidance or suggestions for my research.</p><p>GP CC</p><p><img src="https://osqa-ask.wireshark.org/upfiles/iochart.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-chart" rel="tag" title="see questions tagged &#39;chart&#39;">chart</span> <span class="post-tag tag-link-io" rel="tag" title="see questions tagged &#39;io&#39;">io</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Nov '15, 04:34</strong></p><img src="https://secure.gravatar.com/avatar/68b7271b161241faff6b70c8f1769d63?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GP%20CC&#39;s gravatar image" /><p><span>GP CC</span><br />
<span class="score" title="10 reputation points">10</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GP CC has no accepted answers">0%</span></p></img></div></div><div id="comments-container-47428" class="comments-container"></div><div id="comment-tools-47428" class="comment-tools"></div><div class="clear"></div><div id="comment-47428-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47429"></span>

<div id="answer-container-47429" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47429-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47429-score" class="post-score" title="current number of votes">2</div><span id="post-47429-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="GP CC has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Think about how the rate is calculated. In pcap, there is no information about capture interface raw speed; in pcapng, there may be, but I assume Wireshark doesn't take it into account (yet?). So you have only the timestamps of the packets, and these are assigned at the moment when libpcap reads the packet from the driver, not at the moment when the packet physically arrives. So while other processes are given the CPU, several packets may arrive under hardware (DMA) control, and then libpcap reads all of them almost at the same time when it gets its time slice.</p><p>This idea is supported by the short "silence" right before the 3 Gbps peak on the graph.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Nov '15, 05:01</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>09 Nov '15, 05:05</strong> </span></p></div></div><div id="comments-container-47429" class="comments-container"><span id="47438"></span><div id="comment-47438" class="comment"><div id="post-47438-score" class="comment-score"></div><div class="comment-text"><p>This would be my best guess, too. If you need more precision, then you should try specialized capture hardware.</p></div><div id="comment-47438-info" class="comment-info"><span class="comment-age">(09 Nov '15, 13:46)</span> <span class="comment-user userinfo">Christian_R</span></div></div><span id="47447"></span><div id="comment-47447" class="comment"><div id="post-47447-score" class="comment-score"></div><div class="comment-text"><p>I.e., the <em>average</em> rate won't be above the interface raw speed - there might be an apparent-but-not-real surge where packets are arriving faster than possible, because multiple packets are processed in a group by the networking stack and time stamped based on when they're processed, but that will be balanced by an apparent-but-not-real slowdown, while the packets are being put into system memory but the host hasn't been notified of their arrival yet.</p></div><div id="comment-47447-info" class="comment-info"><span class="comment-age">(09 Nov '15, 18:33)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-47429" class="comment-tools"></div><div class="clear"></div><div id="comment-47429-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


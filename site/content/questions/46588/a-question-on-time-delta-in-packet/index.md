+++
type = "question"
title = "A question on time delta in packet."
description = '''Can you please help to investigate for “Time delta from previous captured frame: 0.000000000 seconds” and “Time delta from previous displayed frame: 0.000000000 seconds” values. the packets are not the first packet, I want to know that how wireshare show the time delta, get time of packet directly? ...'''
date = "2015-10-15T19:38:00Z"
lastmod = "2015-10-16T03:10:00Z"
weight = 46588
keywords = [ "delta" ]
aliases = [ "/questions/46588" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [A question on time delta in packet.](/questions/46588/a-question-on-time-delta-in-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46588-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46588-score" class="post-score" title="current number of votes">0</div><span id="post-46588-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Can you please help to investigate for “Time delta from previous captured frame: 0.000000000 seconds” and “Time delta from previous displayed frame: 0.000000000 seconds” values.</p><p>the packets are not the first packet, I want to know that how wireshare show the time delta, get time of packet directly? this time is in interior of the original packet or laptop makes a timestamp while receive it?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-delta" rel="tag" title="see questions tagged &#39;delta&#39;">delta</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Oct '15, 19:38</strong></p><img src="https://secure.gravatar.com/avatar/94c13935cafc419d4c09c4f64ded48df?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tansg631&#39;s gravatar image" /><p><span>tansg631</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tansg631 has no accepted answers">0%</span></p></div></div><div id="comments-container-46588" class="comments-container"><span id="46589"></span><div id="comment-46589" class="comment"><div id="post-46589-score" class="comment-score"></div><div class="comment-text"><p>I want to know why some packets with 0 time delta</p></div><div id="comment-46589-info" class="comment-info"><span class="comment-age">(15 Oct '15, 19:38)</span> <span class="comment-user userinfo">tansg631</span></div></div><span id="46591"></span><div id="comment-46591" class="comment"><div id="post-46591-score" class="comment-score"></div><div class="comment-text"><p>Could you provide us a trace?</p></div><div id="comment-46591-info" class="comment-info"><span class="comment-age">(15 Oct '15, 22:05)</span> <span class="comment-user userinfo">Christian_R</span></div></div><span id="46602"></span><div id="comment-46602" class="comment"><div id="post-46602-score" class="comment-score">1</div><div class="comment-text"><p>Did you take the capture in a virtual system? If so, this can happen due to several reasons, related to virtualization.</p></div><div id="comment-46602-info" class="comment-info"><span class="comment-age">(16 Oct '15, 03:10)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-46588" class="comment-tools"></div><div class="clear"></div><div id="comment-46588-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="46590"></span>

<div id="answer-container-46590" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46590-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46590-score" class="post-score" title="current number of votes">0</div><span id="post-46590-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It is possible for packet captures to not contain correct timestamps (ie: all zeros), particularly if they were imported from a text file or hex dump, where the dump didn't contain the time information. In such case, those time display settings won't help you because the information isn't actually there to be found in the file. In your example, if all the 'delta time' values are 0, then likely that is why.</p><p>How did you actually get the packet capture? Directly from a live capture on the laptop or from elsewhere?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Oct '15, 22:05</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p><span>Quadratic</span><br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>15 Oct '15, 22:09</strong> </span></p></div></div><div id="comments-container-46590" class="comments-container"><span id="46595"></span><div id="comment-46595" class="comment"><div id="post-46595-score" class="comment-score"></div><div class="comment-text"><p>thank you for you reply, I captured on live network, not all packets met this problem, just a few packets, the time delta is 0. do you mean the timestamp is in the packet in live network? wireshare just get timestamp and show it? or the timestamp is marked while arrived the laptop? thank you</p></div><div id="comment-46595-info" class="comment-info"><span class="comment-age">(15 Oct '15, 23:55)</span> <span class="comment-user userinfo">tansg631</span></div></div></div><div id="comment-tools-46590" class="comment-tools"></div><div class="clear"></div><div id="comment-46590-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="46596"></span>

<div id="answer-container-46596" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46596-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46596-score" class="post-score" title="current number of votes">0</div><span id="post-46596-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>One reason could be that the time resolution inside the trace file is greater than the gap between two frames. But they should show the same absolute time value, in that case.</p><p>Remark: This could mainly caused by those things. - Common resolution of pcap is ms. - You switched the time format manually higher in Wireshark ( maybe you could post us two absolute time values) - The inter frame gap is 0 ns, this could theoretically happen in a full duplex trace</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Oct '15, 00:37</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p><span>Christian_R</span><br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span></p></div></div><div id="comments-container-46596" class="comments-container"></div><div id="comment-tools-46596" class="comment-tools"></div><div class="clear"></div><div id="comment-46596-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


+++
type = "question"
title = "wireshark has stopped working - keeps crashing trying to view statistics/conversations"
description = '''Wireshark 2.0.1. This is on a Windows 10 pc, with plenty of memory and CPU. Task manager shows I&#x27;m using less than 20% memory and CPU, the pcap is less than 1GB in size. Any debug info available on why it keeps crashing when I try to view statistics/conversations? The pcap file I&#x27;m trying to do this...'''
date = "2016-02-22T15:34:00Z"
lastmod = "2016-02-23T07:32:00Z"
weight = 50420
keywords = [ "conversation", "crash" ]
aliases = [ "/questions/50420" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark has stopped working - keeps crashing trying to view statistics/conversations](/questions/50420/wireshark-has-stopped-working-keeps-crashing-trying-to-view-statisticsconversations)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50420-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50420-score" class="post-score" title="current number of votes">0</div><span id="post-50420-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Wireshark 2.0.1. This is on a Windows 10 pc, with plenty of memory and CPU. Task manager shows I'm using less than 20% memory and CPU, the pcap is less than 1GB in size. Any debug info available on why it keeps crashing when I try to view statistics/conversations? The pcap file I'm trying to do this with is less than 1GB in size.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-conversation" rel="tag" title="see questions tagged &#39;conversation&#39;">conversation</span> <span class="post-tag tag-link-crash" rel="tag" title="see questions tagged &#39;crash&#39;">crash</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Feb '16, 15:34</strong></p><img src="https://secure.gravatar.com/avatar/90c40081823d9acbd2600f5f09be755c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pvpete&#39;s gravatar image" /><p><span>pvpete</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pvpete has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>23 Feb '16, 07:33</strong> </span></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span></p></div></div><div id="comments-container-50420" class="comments-container"></div><div id="comment-tools-50420" class="comment-tools"></div><div class="clear"></div><div id="comment-50420-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50440"></span>

<div id="answer-container-50440" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50440-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50440-score" class="post-score" title="current number of votes">0</div><span id="post-50440-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>How much memory is it using (in kbytes)? Are you using 32- or 64-bit Wireshark? Does it crash if you split the capture in half and open each half (independently)?</p><p>I suspect you're running 32-bit Wireshark and you're running into the 32-bit memory limit (2 Gbytes). In this case using the 64-bit version should help.</p><p>On the other hand if one of the smaller captures causes the crash it may be a <a href="https://bugs.wireshark.org">bug</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Feb '16, 07:32</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-50440" class="comments-container"></div><div id="comment-tools-50440" class="comment-tools"></div><div class="clear"></div><div id="comment-50440-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


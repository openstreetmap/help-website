+++
type = "question"
title = "How to capture packets on multiple interface using Dumpcap."
description = '''Hello, I want to capture packets passing through multiple interface on linix machine. I tried   1. &quot;dumpcap -i eth1 eth2 .....&quot;  2. &quot;dumpcap -i eth1 -i eth2 .....&quot; But nothing work. I don&#x27;t want to use &quot;dumpcap -i any ....&quot; because it will capture some undesired traffic as well.  I am currently usin...'''
date = "2014-10-29T02:18:00Z"
lastmod = "2014-10-29T02:41:00Z"
weight = 37425
keywords = [ "multiple-interfaces" ]
aliases = [ "/questions/37425" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to capture packets on multiple interface using Dumpcap.](/questions/37425/how-to-capture-packets-on-multiple-interface-using-dumpcap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37425-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I want to capture packets passing through multiple interface on linix machine.</p><p>I tried 1. "dumpcap -i eth1 eth2 ....." 2. "dumpcap -i eth1 -i eth2 ....." But nothing work.</p><p>I don't want to use "dumpcap -i any ...." because it will capture some undesired traffic as well.</p><p>I am currently using dumpcap version:</p><p>Dumpcap 1.6.6 (SVN Rev Unknown from unknown)</p><p>Copyright 1998-2012 Gerald Combs [email protected] and contributors. This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p><p>Compiled (64-bit) with GLib 2.30.1, with libpcap (version unknown), with libz 1.2.5, with POSIX capabilities (Linux).</p><p>Running on Linux 3.1.10-gb14-default, with libpcap version 1.1.1, with libz 1.2.5.</p><p>Built using gcc 4.6.2."</p></div><div id="question-tags" class="tags-container tags">multiple-interfaces</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Oct '14, 02:18</strong></p><img src="https://secure.gravatar.com/avatar/1894e0b916cdcffe56d25c420f855a81?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ankitkamal&#39;s gravatar image" /><p>ankitkamal<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ankitkamal has no accepted answers">0%</span></p></div></div><div id="comments-container-37425" class="comments-container"></div><div id="comment-tools-37425" class="comment-tools"></div><div class="clear"></div><div id="comment-37425-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37426"></span>

<div id="answer-container-37426" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37426-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Dumpcap 1.6.6 (SVN Rev Unknown from unknown)</p></blockquote><p>can you please try a newer version of dumpcap, as I believe the feature to capture on multiple interfaces was implemented later.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Oct '14, 02:41</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-37426" class="comments-container"><span id="37436"></span><div id="comment-37436" class="comment"><div id="post-37436-score" class="comment-score"></div><div class="comment-text"><p>Yes, that feature was added in Wireshark 1.8.0. See the <a href="https://www.wireshark.org/docs/relnotes/wireshark-1.8.0.html">Release Notes.</a></p></div><div id="comment-37436-info" class="comment-info"><span class="comment-age">(29 Oct '14, 06:36)</span> JeffMorriss ♦</div></div><span id="37437"></span><div id="comment-37437" class="comment"><div id="post-37437-score" class="comment-score"></div><div class="comment-text"><p>thanks for the link!</p></div><div id="comment-37437-info" class="comment-info"><span class="comment-age">(29 Oct '14, 06:39)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-37426" class="comment-tools"></div><div class="clear"></div><div id="comment-37426-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


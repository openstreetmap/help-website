+++
type = "question"
title = "Bypassing dumpcap with TShark and pipes"
description = '''Because of Bug 2874 in dumpcap, tshark will normaly only respond every 500ms. I need lower latency as I am feeding a live application. I heard this can be accomplished with pipes, but am completely inexperienced with pipes. How would this be done? What I need is for the dissectors to be running in r...'''
date = "2017-07-11T15:44:00Z"
lastmod = "2017-07-12T09:33:00Z"
weight = 62684
keywords = [ "pipe", "pipes", "bug-2874", "tshark", "dumpcap" ]
aliases = [ "/questions/62684" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Bypassing dumpcap with TShark and pipes](/questions/62684/bypassing-dumpcap-with-tshark-and-pipes)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62684-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Because of <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=2874">Bug 2874</a> in dumpcap, tshark will normaly only respond every 500ms. I need lower latency as I am feeding a live application. I heard this can be accomplished with pipes, but am completely inexperienced with pipes. How would this be done? What I need is for the dissectors to be running in realtime, continually.</p></div><div id="question-tags" class="tags-container tags">pipe pipes bug-2874 tshark dumpcap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Jul '17, 15:44</strong></p><img src="https://secure.gravatar.com/avatar/a526f7caccd56a1978ad128830e65c22?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="afay&#39;s gravatar image" /><p>afay<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="afay has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 11 Jul '17, 17:20</p></div></div><div id="comments-container-62684" class="comments-container"></div><div id="comment-tools-62684" class="comment-tools"></div><div class="clear"></div><div id="comment-62684-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62712"></span>

<div id="answer-container-62712" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62712-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Use tshark -w - -F pcap | tshark -r -</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jul '17, 09:33</strong></p><img src="https://secure.gravatar.com/avatar/a526f7caccd56a1978ad128830e65c22?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="afay&#39;s gravatar image" /><p>afay<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="afay has no accepted answers">0%</span></p></div></div><div id="comments-container-62712" class="comments-container"><span id="62713"></span><div id="comment-62713" class="comment"><div id="post-62713-score" class="comment-score"></div><div class="comment-text"><p>Did you mean <code>dumpcap -w - -P | tshark -r -</code> ? Or does dumpcap spawned by tshark really behave differently if that tshark writes to stdout than if it writes to a regular file?</p></div><div id="comment-62713-info" class="comment-info"><span class="comment-age">(12 Jul '17, 10:12)</span> sindy</div></div></div><div id="comment-tools-62712" class="comment-tools"></div><div class="clear"></div><div id="comment-62712-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


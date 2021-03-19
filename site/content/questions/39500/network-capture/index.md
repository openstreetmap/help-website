+++
type = "question"
title = "Network Capture"
description = '''I&#x27;m new to using wireshark. I&#x27;ve a question for the experts. My Setup is like below. My PC (Testing) =&amp;gt; F5 (Load Balancer) =&amp;gt; App Server =&amp;gt; DB Server.. Checking tracert, I see all these servers are in the same network as my PC. Wireshark is setup in my PC When I capture network during my te...'''
date = "2015-01-30T06:25:00Z"
lastmod = "2015-01-30T06:28:00Z"
weight = 39500
keywords = [ "interface", "capture", "monitoring" ]
aliases = [ "/questions/39500" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Network Capture](/questions/39500/network-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39500-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm new to using wireshark. I've a question for the experts. My Setup is like below. My PC (Testing) =&gt; F5 (Load Balancer) =&gt; App Server =&gt; DB Server.. Checking tracert, I see all these servers are in the same network as my PC. Wireshark is setup in my PC When I capture network during my testing i see all the calls made between my PC and the F5. How can i capture the calls made between F5 (Load Balancer) =&gt; App Server and App Server =&gt; DB Server. Currently my captures doesn't include the above calls.</p></div><div id="question-tags" class="tags-container tags">interface capture monitoring</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Jan '15, 06:25</strong></p><img src="https://secure.gravatar.com/avatar/34a5f81c5c845ed22cfbd847a66c4a46?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="skhprabu&#39;s gravatar image" /><p>skhprabu<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="skhprabu has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 30 Jan '15, 06:28</p></div></div><div id="comments-container-39500" class="comments-container"></div><div id="comment-tools-39500" class="comment-tools"></div><div class="clear"></div><div id="comment-39500-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39501"></span>

<div id="answer-container-39501" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39501-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I guess you're running Wireshark on your Test-PC. With that setup, you cannot capture packets from the other systems. You might want to check the <a href="http://wiki.wireshark.org/CaptureSetup/Ethernet">Ethernet Capture Setup</a> Wiki Page for ideas on how to get the other packets.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jan '15, 06:28</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-39501" class="comments-container"></div><div id="comment-tools-39501" class="comment-tools"></div><div class="clear"></div><div id="comment-39501-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


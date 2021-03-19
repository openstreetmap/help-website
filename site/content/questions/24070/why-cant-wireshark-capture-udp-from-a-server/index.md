+++
type = "question"
title = "why can&#x27;t wireshark capture UDP from a server?"
description = '''wireshark can capture upd packets from others, but can&#x27;t capture udp packets from one server which sends out udp by HP iLO.  I am sure the server can send udp by HP iLO as hostmonitor can receive its udp packets, no any problem.  why wireshirk can&#x27;t? thanks, George'''
date = "2013-08-26T11:17:00Z"
lastmod = "2013-08-27T06:39:00Z"
weight = 24070
keywords = [ "capture1" ]
aliases = [ "/questions/24070" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [why can't wireshark capture UDP from a server?](/questions/24070/why-cant-wireshark-capture-udp-from-a-server)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24070-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>wireshark can capture upd packets from others, but can't capture udp packets from one server which sends out udp by HP iLO. I am sure the server can send udp by HP iLO as hostmonitor can receive its udp packets, no any problem. why wireshirk can't?</p><p>thanks, George</p></div><div id="question-tags" class="tags-container tags">capture1</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Aug '13, 11:17</strong></p><img src="https://secure.gravatar.com/avatar/b442060ba74b842a59ea52ccb6a370de?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="georgeyu100&#39;s gravatar image" /><p>georgeyu100<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="georgeyu100 has no accepted answers">0%</span></p></div></div><div id="comments-container-24070" class="comments-container"><span id="24074"></span><div id="comment-24074" class="comment"><div id="post-24074-score" class="comment-score"></div><div class="comment-text"><p>wireshark can capture UDP packets from other server port 161</p></div><div id="comment-24074-info" class="comment-info"><span class="comment-age">(26 Aug '13, 13:00)</span> georgeyu100</div></div><span id="24078"></span><div id="comment-24078" class="comment"><div id="post-24078-score" class="comment-score"></div><div class="comment-text"><p>Where and how are you capturing the traffic? Are you using any kind of capture filters? If wireshark is showing that same traffic from other servers, there aren't a lot of possibilities other than that the server isn't sending the traffic, your filters are dropping it, or the place where you're capturing isn't in the line of path of the packets.</p></div><div id="comment-24078-info" class="comment-info"><span class="comment-age">(26 Aug '13, 19:41)</span> Quadratic</div></div></div><div id="comment-tools-24070" class="comment-tools"></div><div class="clear"></div><div id="comment-24070-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24096"></span>

<div id="answer-container-24096" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24096-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Maybe the HP iLo traffic is using Unicast UDP packets towards the hostmonitor, while the other UDP packets you see are Broadcast/Multicast. You'll only see the Unicast packets if you capture at a location like a SPAN port.</p><p>See <a href="http://wiki.wireshark.org/CaptureSetup/Ethernet">http://wiki.wireshark.org/CaptureSetup/Ethernet</a> for capture setup options.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Aug '13, 06:39</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-24096" class="comments-container"></div><div id="comment-tools-24096" class="comment-tools"></div><div class="clear"></div><div id="comment-24096-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


+++
type = "question"
title = "Sniffing telnet packets on LAN"
description = '''Hi, I started capturing packets on my network from my PC then from one random PC on same network i connected to server using telnet but i couldn&#x27;t see telnet packets on my Wireshark however if i connect same server from my PC where i am running Wireshark i can see telnet packets of my own, so what c...'''
date = "2016-10-02T07:00:00Z"
lastmod = "2016-10-02T07:39:00Z"
weight = 56070
keywords = [ "wlan", "telnet", "wireshark" ]
aliases = [ "/questions/56070" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Sniffing telnet packets on LAN](/questions/56070/sniffing-telnet-packets-on-lan)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56070-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56070-score" class="post-score" title="current number of votes">0</div><span id="post-56070-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I started capturing packets on my network from my PC then from one random PC on same network i connected to server using telnet but i couldn't see telnet packets on my Wireshark however if i connect same server from my PC where i am running Wireshark i can see telnet packets of my own, so what can be the issue?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wlan" rel="tag" title="see questions tagged &#39;wlan&#39;">wlan</span> <span class="post-tag tag-link-telnet" rel="tag" title="see questions tagged &#39;telnet&#39;">telnet</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Oct '16, 07:00</strong></p><img src="https://secure.gravatar.com/avatar/3f6441a52654b00fbd3be3bf16ac5daf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="awadbasmeh&#39;s gravatar image" /><p><span>awadbasmeh</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="awadbasmeh has no accepted answers">0%</span></p></div></div><div id="comments-container-56070" class="comments-container"></div><div id="comment-tools-56070" class="comment-tools"></div><div class="clear"></div><div id="comment-56070-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56071"></span>

<div id="answer-container-56071" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56071-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56071-score" class="post-score" title="current number of votes">0</div><span id="post-56071-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="awadbasmeh has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The issue is that the device connecting your PC to the rest of the network is a <a href="https://en.wikipedia.org/wiki/Network_switch#Network_design">switch</a>, which means that Ethernet frames which are neither sent by nor addressed to your PC never reach your PC's network card. See <a href="https://wiki.wireshark.org/CaptureSetup/Ethernet">the Wireshark wiki page on capturing on Ethernet</a> for details and solutions.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Oct '16, 07:39</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>02 Oct '16, 07:46</strong> </span></p></div></div><div id="comments-container-56071" class="comments-container"></div><div id="comment-tools-56071" class="comment-tools"></div><div class="clear"></div><div id="comment-56071-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


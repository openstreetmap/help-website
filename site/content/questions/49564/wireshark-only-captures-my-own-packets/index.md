+++
type = "question"
title = "wireshark only captures my own packets"
description = '''I have promiscuous mode enabled on my raspberry pi (the chip supports it) yet the only packets that tshark allows me to capture are my own packets. please help. I want to capture all wireless packets near me.'''
date = "2016-01-27T16:53:00Z"
lastmod = "2016-01-27T22:36:00Z"
weight = 49564
keywords = [ "capture", "raspberry", "tshark" ]
aliases = [ "/questions/49564" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark only captures my own packets](/questions/49564/wireshark-only-captures-my-own-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49564-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have promiscuous mode enabled on my raspberry pi (the chip supports it) yet the only packets that tshark allows me to capture are my own packets. please help. I want to capture all wireless packets near me.</p></div><div id="question-tags" class="tags-container tags">capture raspberry tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Jan '16, 16:53</strong></p><img src="https://secure.gravatar.com/avatar/618e6f1d27deb71366e15ee7f0df7b81?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Scarab&#39;s gravatar image" /><p>Scarab<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Scarab has no accepted answers">0%</span></p></div></div><div id="comments-container-49564" class="comments-container"></div><div id="comment-tools-49564" class="comment-tools"></div><div class="clear"></div><div id="comment-49564-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49566"></span>

<div id="answer-container-49566" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49566-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Please look <a href="https://wiki.wireshark.org/CaptureSetup/WLAN#Turning_on_monitor_mode">here</a> for the difference between <em>promiscuous</em> and <em>monitor</em> mode. Promiscuous mode shows you other devices' traffic on wired interfaces (if other pre-requisities are met) but is of little use on wireless ones.</p><p>Plus, even with monitoring mode, you can only see packets on a single radio channel, so to see "all wireless packets near you" you'd need as many raspberries as there are WiFi channels in use in your country.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jan '16, 22:36</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-49566" class="comments-container"></div><div id="comment-tools-49566" class="comment-tools"></div><div class="clear"></div><div id="comment-49566-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


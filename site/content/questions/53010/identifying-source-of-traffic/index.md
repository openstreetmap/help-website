+++
type = "question"
title = "identifying source of traffic"
description = '''I am running Windows 10 and have recently discovered Wireshark. I use a VPN. I am bugged by the fact that Windows likes to phone home a lot. I have managed to block all the nonsense going on but have a residual issue. I start Windows and log onto my VPN in a normal manner. I start Wireshark and set ...'''
date = "2016-05-27T13:35:00Z"
lastmod = "2016-05-27T15:29:00Z"
weight = 53010
keywords = [ "program", "traffic-analysis", "tracking" ]
aliases = [ "/questions/53010" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [identifying source of traffic](/questions/53010/identifying-source-of-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53010-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am running Windows 10 and have recently discovered Wireshark. I use a VPN. I am bugged by the fact that Windows likes to phone home a lot. I have managed to block all the nonsense going on but have a residual issue. I start Windows and log onto my VPN in a normal manner. I start Wireshark and set it to capture the traffic on my TAP Windows Adapter. I don't initiate any browsers or any applications. Of course there are many back ground tasks running at startup. I go take a walk. When I come back there is a small amount of traffic - Akami, AmazonAWS, OpenVPN, something from Edgecast, something from Highwinds Network, a weird ip from Poland - that's it. Not much traffic at all (none to MS). What I want to do is to identify what process might be generating the traffic. I am not sure how to configure Wireshark or if I need another tool. Any advice? Thanks.<br />
</p></div><div id="question-tags" class="tags-container tags">program traffic-analysis tracking</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 May '16, 13:35</strong></p><img src="https://secure.gravatar.com/avatar/fe4bf0960a18466341b4ffbad2ff7d37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="share3141&#39;s gravatar image" /><p>share3141<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="share3141 has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-53010" class="comments-container"></div><div id="comment-tools-53010" class="comment-tools"></div><div class="clear"></div><div id="comment-53010-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53015"></span>

<div id="answer-container-53015" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53015-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>This is not something Wireshark could help you with. Due to the way it captures the packets, it is unable to identify the process which has sent them or which expects them.</p><p>But look for similar Questions here (search for "process"), I am sure a name of a Windows application which can do this has been given in at least one of them less than a month ago.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 May '16, 15:29</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-53015" class="comments-container"></div><div id="comment-tools-53015" class="comment-tools"></div><div class="clear"></div><div id="comment-53015-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


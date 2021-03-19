+++
type = "question"
title = "Wireless router traffic"
description = '''I am trying to capture all data that goes through my router to the cable modem (e.g. capture all traffic from PC&#x27;s connected to my wireless router). From what I understand this is possible with Wireshark, but I am unable to figure it out (I am not a techie). I am running Mac OS X 10.5.8 and using a ...'''
date = "2011-05-18T10:11:00Z"
lastmod = "2011-05-19T05:37:00Z"
weight = 4123
keywords = [ "wireless", "router", "traffic" ]
aliases = [ "/questions/4123" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireless router traffic](/questions/4123/wireless-router-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4123-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to capture all data that goes through my router to the cable modem (e.g. capture all traffic from PC's connected to my wireless router).</p><p>From what I understand this is possible with Wireshark, but I am unable to figure it out (I am not a techie).</p><p>I am running Mac OS X 10.5.8 and using a linksys WRT54 router if that makes any difference.</p><p>Can anyone explain (in layman) terms how I can achieve this?</p><p>The reason for this is that I have multiple computers connected to my wireless router nearly all the time. I have tried to secure my router using mac filtering, passwords and a mixture of both, but for some reason within a few hours to a few days all settings are back to factory defaults. I don't know if this is just the router (it is quite a few years old now, but can't afford a new one atm) or if it is someone who is using my network doing this).</p><p>Please can anyone help me?</p></div><div id="question-tags" class="tags-container tags">wireless router traffic</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 May '11, 10:11</strong></p><img src="https://secure.gravatar.com/avatar/96ad5d50fbc2e7706aa989e648f15ee5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="60seconduser&#39;s gravatar image" /><p>60seconduser<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="60seconduser has no accepted answers">0%</span></p></div></div><div id="comments-container-4123" class="comments-container"></div><div id="comment-tools-4123" class="comment-tools"></div><div class="clear"></div><div id="comment-4123-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4138"></span>

<div id="answer-container-4138" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4138-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>There are a few ways to accomplish this.<br />
1). you can install an ethernet HUB, (not switch), between your cable modem and router, so that you can capture all packets to and from your network. 2). you can use an "airpcap" adapter to capture wireless traffic, using the WLAN and Radiotap filters available in Wireshark to narrow down potential connection problems. I use the WRT style wireless routers also. For securing your wireless router, WEP has been the standard, but I've recently read that WPA2 actually encrypts the entire frame and is more secure, you might consider reconfiguring for that. If you feel the MAC filtering you're using is possibly not working, I would flash your router with the latest BIOS. I've found many units sold are not up to the latest available BIOS. You can download the BIOS free and flashing is easy.</p><p>Hope that gets you in the direction you're looking for. John</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 May '11, 05:37</strong></p><img src="https://secure.gravatar.com/avatar/1f3966b6e9de3a63326e2d3fd51c8c04?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="John_Modlin&#39;s gravatar image" /><p>John_Modlin<br />
<span class="score" title="120 reputation points">120</span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="John_Modlin has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-4138" class="comments-container"></div><div id="comment-tools-4138" class="comment-tools"></div><div class="clear"></div><div id="comment-4138-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


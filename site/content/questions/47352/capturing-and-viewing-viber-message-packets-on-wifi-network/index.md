+++
type = "question"
title = "Capturing and viewing Viber message packets on WIFI network?"
description = '''Hi all. As it says in the title. I&#x27;m referring to a home WIFI network where the phone (Windows Phone, if it matters) is used on a daily basis to send and receive messages via Viber. I&#x27;m curious if I can use Wireshark and a linux distro (last time I read Windows doesn&#x27;t allow to capture packets or di...'''
date = "2015-11-06T15:56:00Z"
lastmod = "2015-11-06T17:46:00Z"
weight = 47352
keywords = [ "texts", "viber", "messages", "wifi" ]
aliases = [ "/questions/47352" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Capturing and viewing Viber message packets on WIFI network?](/questions/47352/capturing-and-viewing-viber-message-packets-on-wifi-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47352-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all.</p><p>As it says in the title.</p><p>I'm referring to a home WIFI network where the phone (Windows Phone, if it matters) is used on a daily basis to send and receive messages via Viber. I'm curious if I can use Wireshark and a linux distro (last time I read Windows doesn't allow to capture packets or did I misread?) to capture and view the packets or are they encrypted (the messages only, not interested in the images, etc)? I saw a video uploaded on Youtube demonstrating how to capture and view packets containing images,videos, location but not messages.</p><p>Anyone have any experience with the messages? I'm interested in testing this out on my home WIFI network but thought I'd ask first before giving it a try.</p><p>Thanks in advance for any replies.</p></div><div id="question-tags" class="tags-container tags">texts viber messages wifi</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Nov '15, 15:56</strong></p><img src="https://secure.gravatar.com/avatar/f78f3bdff694573ae6229582f51275dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="riza&#39;s gravatar image" /><p>riza<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="riza has no accepted answers">0%</span></p></div></div><div id="comments-container-47352" class="comments-container"></div><div id="comment-tools-47352" class="comment-tools"></div><div class="clear"></div><div id="comment-47352-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47353"></span>

<div id="answer-container-47353" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47353-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>last time I read Windows doesn't allow to capture packets or did I misread?</p></blockquote><p>On a Wi-Fi network, WinPcap on Windows should let you capture in non-promiscuous, non-monitor mode, meaning you see the traffic the machine running {WinDump, Wireshark, other WinPcap application}, but no other traffic. You'd need an <a href="http://www.riverbed.com/products/steelcentral/steelcentral-riverbed-airpcap.html">AirPcap adapter</a> to capture other hosts' traffic on a Wi-Fi network on Windows with Wireshark; some other sniffers have their own drivers for Wi-Fi adapters, or use a newer mechanism that WInPcap uses, and can capture in monitor mode on Windows.</p><blockquote><p>to capture and view the packets or are they encrypted (the messages only, not interested in the images, etc)?</p></blockquote><p>Well, one question to ask is whether Wireshark understands the protocols or would just display them as raw data. From some Web searching, it doesn't appear that Viber uses standard protocols; Wireshark has no dissectors for whatever protocols they use.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Nov '15, 17:46</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-47353" class="comments-container"></div><div id="comment-tools-47353" class="comment-tools"></div><div class="clear"></div><div id="comment-47353-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


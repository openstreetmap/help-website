+++
type = "question"
title = "Can&#x27;t see packets on home network"
description = '''I have a wireless home network with a Mac (OS X Version 10.8.5) and a Windows PC (Windows 7) connected to it. On the Mac I am running an HTTP server and sending HTTP requests (from both the Mac and the windows PC) to it using both curl and Postman. The requests are processed correctly by the server ...'''
date = "2014-08-18T05:26:00Z"
lastmod = "2014-08-18T05:37:00Z"
weight = 35533
keywords = [ "windows", "mac", "packet-capture", "wireshark" ]
aliases = [ "/questions/35533" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Can't see packets on home network](/questions/35533/cant-see-packets-on-home-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35533-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a wireless home network with a Mac (OS X Version 10.8.5) and a Windows PC (Windows 7) connected to it.</p><p>On the Mac I am running an HTTP server and sending HTTP requests (from both the Mac and the windows PC) to it using both curl and Postman. The requests are processed correctly by the server so I know they are arriving.</p><p>I want to be able to view the IP packets using Wireshark, which I'm running on the Windows machine. However, I can only see the packets when I issue the HTTP requests from the Windows PC and not when they are issued from the Mac. I'm not using any filters and I'm monitoring all interfaces (just to be sure) but I can't see any of the packets.</p><p>Am I missing something obvious? I've used Wireshark before, briefly, but only in a work environment. I'm wondering if the router has something to do with it.</p></div><div id="question-tags" class="tags-container tags">windows mac packet-capture wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Aug '14, 05:26</strong></p><img src="https://secure.gravatar.com/avatar/8b183a4b9292082b95212e9fd0aecab7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RP1&#39;s gravatar image" /><p>RP1<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RP1 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 18 Aug '14, 05:27</p></div></div><div id="comments-container-35533" class="comments-container"></div><div id="comment-tools-35533" class="comment-tools"></div><div class="clear"></div><div id="comment-35533-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35534"></span>

<div id="answer-container-35534" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35534-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>See the Wiki page on <a href="http://wiki.wireshark.org/CaptureSetup/WLAN">Wireless capture</a>, and note in particular that you'll need monitor mode working on Windows to capture traffic from other machines, and this isn't easy to achieve. An <a href="http://www.riverbed.com/us/products/cascade/airpcap.php">AirPCap</a> adaptor can help.</p><p>You also seem to imply that the HTTP server is on the MAC, is this the same MAC that that you are issuing the request from? If so, you'll (generally) never see those packets on another machine as they will "short-circuit" on the MAC and never leave the machine via any external network interface (wired or wireless).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Aug '14, 05:37</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-35534" class="comments-container"></div><div id="comment-tools-35534" class="comment-tools"></div><div class="clear"></div><div id="comment-35534-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


+++
type = "question"
title = "Wireshark can&#x27;t see the WLAN interface??? why?? please help"
description = '''Hi guys. I wanted to capture wireless packets but when I run wireshark I can&#x27;t see the my wireless interface card listed under the interface list? please help me thank you'''
date = "2012-03-27T16:29:00Z"
lastmod = "2012-03-28T04:47:00Z"
weight = 9800
keywords = [ "wireless", "interface" ]
aliases = [ "/questions/9800" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark can't see the WLAN interface??? why?? please help](/questions/9800/wireshark-cant-see-the-wlan-interface-why-please-help)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9800-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi guys.</p><p>I wanted to capture wireless packets but when I run wireshark I can't see the my wireless interface card listed under the interface list?</p><p>please help me</p><p>thank you</p></div><div id="question-tags" class="tags-container tags">wireless interface</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Mar '12, 16:29</strong></p><img src="https://secure.gravatar.com/avatar/9f0be1760abe40684d882aca34eb6fe3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NAOUFL&#39;s gravatar image" /><p>NAOUFL<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NAOUFL has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 27 Mar '12, 17:45</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-9800" class="comments-container"></div><div id="comment-tools-9800" class="comment-tools"></div><div class="clear"></div><div id="comment-9800-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="9801"></span>

<div id="answer-container-9801" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9801-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You should tell what OS you're running, and what you DO see in the interface list. I'm just guessing but you're probably running Windows and seeing some interfaces called "Microsoft". One of them will most likely be your WiFi card. You can tell by looking at the IP address listed next to it. By the way, keep in mind that you can't capture the 802.11 layer on Windows unless you have an AirPCAP adapter.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Mar '12, 16:48</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-9801" class="comments-container"><span id="9812"></span><div id="comment-9812" class="comment"><div id="post-9812-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your reply Jasper</p><p>Yes you are right am using windows 7 and the wireshrk sees some interfaces called 'Microsoft' but you said one of them is my wifi card that means i can see the 802.11 packets. can you please tell me is there other ways to capture 802.11 packets excluding AirPCAP adapter.</p><p>Actually am using 802.11n and i need to capture the exchanged packets between the Access point and the .PC Thank you</p></div><div id="comment-9812-info" class="comment-info"><span class="comment-age">(28 Mar '12, 04:28)</span> NAOUFL</div></div><span id="9814"></span><div id="comment-9814" class="comment"><div id="post-9814-score" class="comment-score"></div><div class="comment-text"><p>You can use your Wifi adapter to capture packets from ethernet up, but not the 802.11 radio layer (unless you have an AirPCAP adapter)</p><p>If you need to see the radio layer you could use Linux. Before starting Wireshark you'll need to put the Wifi card in monitor mode, usually by using the airmon-ng tool. See the following other question that has an answer that will help you: <a href="http://ask.wireshark.org/questions/4259/wireless-showing-as-ethernet.">http://ask.wireshark.org/questions/4259/wireless-showing-as-ethernet.</a></p><p>By the way, if you like an answer you should consider accepting it with the round checkmark button ;-)</p></div><div id="comment-9814-info" class="comment-info"><span class="comment-age">(28 Mar '12, 04:49)</span> Jasper ♦♦</div></div></div><div id="comment-tools-9801" class="comment-tools"></div><div class="clear"></div><div id="comment-9801-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="9813"></span>

<div id="answer-container-9813" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9813-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>See the Wiki page on Wireless captures <a href="http://wiki.wireshark.org/CaptureSetup/WLAN">HERE</a>. Basically capturing the 802.11 packets is very hard on Windows unless you have an AirPCap adaptor.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Mar '12, 04:47</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-9813" class="comments-container"><span id="9815"></span><div id="comment-9815" class="comment"><div id="post-9815-score" class="comment-score"></div><div class="comment-text"><p>thank you very much</p></div><div id="comment-9815-info" class="comment-info"><span class="comment-age">(28 Mar '12, 04:58)</span> NAOUFL</div></div></div><div id="comment-tools-9813" class="comment-tools"></div><div class="clear"></div><div id="comment-9813-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


+++
type = "question"
title = "how to get wireshark to detect other wireless devices using my network"
description = '''I have wireshark installed on my macbook pro and it is connected to the network through wifi. wireshark sees my computer but there are 4 others also connected by wifi that it does not. How do I see the other devices?'''
date = "2011-06-29T12:58:00Z"
lastmod = "2011-06-30T10:25:00Z"
weight = 4820
keywords = [ "capture", "wifi", "wlan", "macbook" ]
aliases = [ "/questions/4820" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [how to get wireshark to detect other wireless devices using my network](/questions/4820/how-to-get-wireshark-to-detect-other-wireless-devices-using-my-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4820-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have wireshark installed on my macbook pro and it is connected to the network through wifi. wireshark sees my computer but there are 4 others also connected by wifi that it does not. How do I see the other devices?</p></div><div id="question-tags" class="tags-container tags">capture wifi wlan macbook</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Jun '11, 12:58</strong></p><img src="https://secure.gravatar.com/avatar/67b798706aefd71bf25a9f963c53f7f0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Greg&#39;s gravatar image" /><p>Greg<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Greg has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>retagged 02 Jul '11, 02:02</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-4820" class="comments-container"></div><div id="comment-tools-4820" class="comment-tools"></div><div class="clear"></div><div id="comment-4820-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="4834"></span>

<div id="answer-container-4834" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4834-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>This may help you: <a href="http://wiki.wireshark.org/CaptureSetup/WLAN">http://wiki.wireshark.org/CaptureSetup/WLAN</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Jun '11, 19:50</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-4834" class="comments-container"></div><div id="comment-tools-4834" class="comment-tools"></div><div class="clear"></div><div id="comment-4834-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="4854"></span>

<div id="answer-container-4854" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4854-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you have the 64-bit Snow Leopard binary installed, try starting the capture from the "Options" item in the "Capture" menu, select the AirPort interface (en1), and check the "Monitor mode" check box.</p><p>If you have the 32-bit Leopard binary installed, try starting the capture from the "Options" item in the "Capture" menu, select the AirPort interface (en1), and select a link-layer type value that has "802.11" in its name.</p><p>Those will cause the adapter to capture in "monitor mode", so it should see other devices, if their radio signals are reaching your MBP's antenna and are using the same channel.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jun '11, 10:25</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-4854" class="comments-container"></div><div id="comment-tools-4854" class="comment-tools"></div><div class="clear"></div><div id="comment-4854-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


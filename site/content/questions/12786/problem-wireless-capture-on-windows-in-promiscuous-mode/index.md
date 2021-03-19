+++
type = "question"
title = "Problem - wireless capture on windows in promiscuous mode"
description = '''hey i have Tp-Link Wireless Usb And I Try To Start caputre with wireshark i have this problem The capture session could not be initiated (failed to set hardware filter to promiscuous mode).  Please check that &quot;&#92;Device&#92;NPF_{1BD779A8-8634-4EB8-96FA-4A5F9AB8701F}&quot; is the proper interface.  Help can be ...'''
date = "2012-07-16T14:06:00Z"
lastmod = "2012-07-16T15:01:00Z"
weight = 12786
keywords = [ "windows", "promiscuous", "wlan" ]
aliases = [ "/questions/12786" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Problem - wireless capture on windows in promiscuous mode](/questions/12786/problem-wireless-capture-on-windows-in-promiscuous-mode)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12786-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hey i have Tp-Link Wireless Usb And I Try To Start caputre with wireshark i have this problem</p><pre><code>The capture session could not be initiated (failed to set hardware filter to promiscuous mode).

Please check that &quot;\Device\NPF_{1BD779A8-8634-4EB8-96FA-4A5F9AB8701F}&quot; is the proper interface.

Help can be found at:

   http://wiki.wireshark.org/WinPcap
   http://wiki.wireshark.org/CaptureSetup</code></pre><p>and i have windows xp can anyone help me pleas?</p></div><div id="question-tags" class="tags-container tags">windows promiscuous wlan</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Jul '12, 14:06</strong></p><img src="https://secure.gravatar.com/avatar/c5dc422e3ec2633b6499699f5531471c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="elie&#39;s gravatar image" /><p>elie<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="elie has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Jul '12, 18:06</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-12786" class="comments-container"></div><div id="comment-tools-12786" class="comment-tools"></div><div class="clear"></div><div id="comment-12786-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12788"></span>

<div id="answer-container-12788" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12788-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>promiscuous mode does not work properly on Windows with several (most) wifi adapters.</p><blockquote><p><code>http://wiki.wireshark.org/CaptureSetup/WLAN#windows</code><br />
</p></blockquote><p>If you need a working solution for Windows, please check the AirPcap adapters.</p><blockquote><p><code>http://www.riverbed.com/us/products/cascade/wireshark_enhancements/airpcap.php</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Jul '12, 15:01</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-12788" class="comments-container"><span id="12789"></span><div id="comment-12789" class="comment"><div id="post-12789-score" class="comment-score"></div><div class="comment-text"><p>thats problem :( i need to get cap file for crack :( do you know any other method to get the cap file :(</p></div><div id="comment-12789-info" class="comment-info"><span class="comment-age">(16 Jul '12, 15:11)</span> elie</div></div><span id="12790"></span><div id="comment-12790" class="comment"><div id="post-12790-score" class="comment-score"></div><div class="comment-text"><p>Capture on Linux.</p></div><div id="comment-12790-info" class="comment-info"><span class="comment-age">(16 Jul '12, 15:20)</span> Kurt Knochner ♦</div></div><span id="12796"></span><div id="comment-12796" class="comment"><div id="post-12796-score" class="comment-score"></div><div class="comment-text"><p>the Back Track Not Read Tp-Link Do You Have Any Driver Pleas Or Something To Do :S</p></div><div id="comment-12796-info" class="comment-info"><span class="comment-age">(17 Jul '12, 02:27)</span> elie</div></div><span id="12797"></span><div id="comment-12797" class="comment"><div id="post-12797-score" class="comment-score"></div><div class="comment-text"><p>If Backtrack does not detect the TP-Link adapter, then your options are kind of 'limited'.</p><p>The best recommendation I have: Read the documentation of Backtrack and buy a supported WLAN adapter.</p><blockquote><p><code>http://www.backtrack-linux.org/wiki/index.php/Wireless_Drivers</code><br />
</p></blockquote><p>One of those will most certainly work with Wireshark as well.</p><p>The <a href="http://www.amazon.com/Alfa-AWUS036H-Upgraded-Wireless-Long-Rang/dp/B000QYGNKQ/ref=sr_1_1?ie=UTF8&amp;qid=1342517645&amp;sr=8-1&amp;keywords=AWUS036H">Alfa USB Adapter - AWUS036H</a> usually get's good ratings:</p></div><div id="comment-12797-info" class="comment-info"><span class="comment-age">(17 Jul '12, 02:30)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-12788" class="comment-tools"></div><div class="clear"></div><div id="comment-12788-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


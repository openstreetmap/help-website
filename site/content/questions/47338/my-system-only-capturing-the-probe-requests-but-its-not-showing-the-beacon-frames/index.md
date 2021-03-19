+++
type = "question"
title = "My system only capturing the probe requests but its not showing the beacon frames."
description = '''I have disconnected wifi and I tried #airmon-ng check kill #airmon-ng start wlan0 #iwconfig  the monitor mode enabled I have gone for the interfaces option in the wireshark. and I selected the wlan0mon and i disabled the promiscuous mode Now iam getting only probe requests but not the beacon frames....'''
date = "2015-11-06T06:56:00Z"
lastmod = "2015-11-06T09:05:00Z"
weight = 47338
keywords = [ "beacon", "wifi", "monitor", "wireshark" ]
aliases = [ "/questions/47338" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [My system only capturing the probe requests but its not showing the beacon frames.](/questions/47338/my-system-only-capturing-the-probe-requests-but-its-not-showing-the-beacon-frames)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47338-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have disconnected wifi and I tried</p><pre><code>#airmon-ng check kill
#airmon-ng start wlan0
#iwconfig</code></pre><p>the monitor mode enabled</p><p>I have gone for the interfaces option in the wireshark. and I selected the wlan0mon and i disabled the promiscuous mode Now iam getting only probe requests but not the beacon frames. why? I am using kali linux 2.0</p></div><div id="question-tags" class="tags-container tags">beacon wifi monitor wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Nov '15, 06:56</strong></p><img src="https://secure.gravatar.com/avatar/e36cc00d960bddb05ae96f1bc8e4feb8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ashokkrishna&#39;s gravatar image" /><p>ashokkrishna<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ashokkrishna has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 06 Nov '15, 06:57</p></div></div><div id="comments-container-47338" class="comments-container"></div><div id="comment-tools-47338" class="comment-tools"></div><div class="clear"></div><div id="comment-47338-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47341"></span>

<div id="answer-container-47341" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47341-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Ya I got the solution when i checked my channel in iwconfig its changed to channel3 but my actual ap is residing in the channel 6 and there are no ap's present in the channel 3 so its not getting any beacon frames. I think please correct me if i am wrong.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Nov '15, 09:05</strong></p><img src="https://secure.gravatar.com/avatar/e36cc00d960bddb05ae96f1bc8e4feb8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ashokkrishna&#39;s gravatar image" /><p>ashokkrishna<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ashokkrishna has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 06 Nov '15, 09:06</p></div></div><div id="comments-container-47341" class="comments-container"></div><div id="comment-tools-47341" class="comment-tools"></div><div class="clear"></div><div id="comment-47341-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


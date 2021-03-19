+++
type = "question"
title = "Setting up capture interface"
description = '''Hi, I&#x27;m a new WS user, and I&#x27;m wondering how to set up the capture interface. There are 4 available interfaces for me: 1. Local Area Connection 2. Ethernet 3. Wi-Fi 4.Bluetooth Network Connections. As for 1,2, and 4, I am unable of receiving any packets. As for 3, the Ethernet, I get non-stopping pa...'''
date = "2014-11-15T17:23:00Z"
lastmod = "2014-11-16T13:04:00Z"
weight = 37883
keywords = [ "interface", "capture" ]
aliases = [ "/questions/37883" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Setting up capture interface](/questions/37883/setting-up-capture-interface)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37883-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I'm a new WS user, and I'm wondering how to set up the capture interface. There are 4 available interfaces for me: 1. Local Area Connection 2. Ethernet 3. Wi-Fi 4.Bluetooth Network Connections.</p><p>As for 1,2, and 4, I am unable of receiving any packets. As for 3, the Ethernet, I get non-stopping packets when I've just started my computer. Most importantly, For TCP, it shows "Ethernet Frame Check Sequence Incorrect," and I'm unable of getting any UDPs.</p><p>I am very lost. I have Windows 8 64 bit and wincap installed.</p></div><div id="question-tags" class="tags-container tags">interface capture</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Nov '14, 17:23</strong></p><img src="https://secure.gravatar.com/avatar/1059cafb10cc39c170c46dbffbae2711?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Davis&#39;s gravatar image" /><p>Davis<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Davis has no accepted answers">0%</span></p></div></div><div id="comments-container-37883" class="comments-container"><span id="37885"></span><div id="comment-37885" class="comment"><div id="post-37885-score" class="comment-score"></div><div class="comment-text"><p>can someone please explain to me what am I doing wrong?</p></div><div id="comment-37885-info" class="comment-info"><span class="comment-age">(16 Nov '14, 10:15)</span> Davis</div></div></div><div id="comment-tools-37883" class="comment-tools"></div><div class="clear"></div><div id="comment-37883-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37887"></span>

<div id="answer-container-37887" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37887-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>For the first part of your question, you will only see packets on interfaces that are actually in use. You can check this using the "Interfaces" display of Wireshark, from the main panel display, from the Capture Menu or via Ctrl + I. You'll see the packet count go up for the interfaces in use. You can check what those interfaces really are from a Cmd or Powershell prompt with <code>ipconfig /all</code>.</p><p>For the second part, lots of packets are expected if your computer is sending or receiving data, that's where the magic happens.</p><p>For the third part, you have either mistyped or are confused. Ethernet does have Frame Check Sequence bytes, but normally you don't see them, and this is different to TCP Checksum bytes.</p><p>If it is the Ethernet Frame Check Sequence, try disabling that part of the Ethernet dissector (in the packet details pane, right click the "Ethernet II" entry and the go to "Protocol Preferences" and make sure "Assume packets have FCS" and "Validate the Ethernet checksum if possible" aren't checked.</p><p>If it is the TCP Checksum, again, right click that part of the packet details, go to "Protocol Preferences" and make sure "Validate the TCP checksum if possible" isn't checked.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Nov '14, 13:04</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-37887" class="comments-container"><span id="37917"></span><div id="comment-37917" class="comment"><div id="post-37917-score" class="comment-score"></div><div class="comment-text"><p>Hi, I have posted a photo of what I see when I'm under wifi. all of these arps and tcps take up the page, and I have no clue what this means. Thank you for your help. <a href="http://postimg.org/image/i2xnhl48p/">http://postimg.org/image/i2xnhl48p/</a></p></div><div id="comment-37917-info" class="comment-info"><span class="comment-age">(17 Nov '14, 14:28)</span> Davis</div></div></div><div id="comment-tools-37887" class="comment-tools"></div><div class="clear"></div><div id="comment-37887-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


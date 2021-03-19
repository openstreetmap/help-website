+++
type = "question"
title = "How to set wireshark on monitor mode"
description = '''Hi all, I&#x27;m working on my project and it requires me to capture traffic on a network. below is the description of the scenario:  I&#x27;m running wire-shark on a Kali Linux virtual machine installed on a mac air laptop. I want to capture the traffic on the router network using the wire-shark installed on...'''
date = "2017-01-13T12:13:00Z"
lastmod = "2017-01-13T14:31:00Z"
weight = 58745
keywords = [ "traffic", "capture", "udp", "http", "tcp" ]
aliases = [ "/questions/58745" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to set wireshark on monitor mode](/questions/58745/how-to-set-wireshark-on-monitor-mode)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58745-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>I'm working on my project and it requires me to capture traffic on a network. below is the description of the scenario:</p><p>I'm running wire-shark on a Kali Linux virtual machine installed on a mac air laptop.</p><p>I want to capture the traffic on the router network using the wire-shark installed on the kali linux.</p><p>current i only receive DNS, ARP, ICMP Traffic. I do need help to achieve the following</p><ol><li>How can i set the network on a monitor mode.</li><li>how do i successful capture tcp traffic and other relevant traffic.</li></ol><p>Thanks</p></div><div id="question-tags" class="tags-container tags">traffic capture udp http tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Jan '17, 12:13</strong></p><img src="https://secure.gravatar.com/avatar/0f3dd5cad846e1bd507b76ed5b3e7265?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="edafe&#39;s gravatar image" /><p>edafe<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="edafe has no accepted answers">0%</span></p></div></div><div id="comments-container-58745" class="comments-container"></div><div id="comment-tools-58745" class="comment-tools"></div><div class="clear"></div><div id="comment-58745-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="58746"></span>

<div id="answer-container-58746" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58746-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Read the following:</p><p>Wired Ethernet = <a href="https://wiki.wireshark.org/CaptureSetup/Ethernet">https://wiki.wireshark.org/CaptureSetup/Ethernet</a></p><p>WLAN = <a href="https://wiki.wireshark.org/CaptureSetup/WLAN">https://wiki.wireshark.org/CaptureSetup/WLAN</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jan '17, 12:27</strong></p><img src="https://secure.gravatar.com/avatar/d9cf592a79eafbc3b2a8b3f38cf38362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amato_C&#39;s gravatar image" /><p>Amato_C<br />
<span class="score" title="1098 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amato_C has 15 accepted answers">14%</span></p></div></div><div id="comments-container-58746" class="comments-container"></div><div id="comment-tools-58746" class="comment-tools"></div><div class="clear"></div><div id="comment-58746-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="58750"></span>

<div id="answer-container-58750" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58750-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You really can't set monitor mode with your current setup. If you are on a VM, as you describe, all interfaces are virtual and further 'wired'. So @Amato's links are certainly appropriate, especially the wired one. If you want wireless traffic, you need direct access to the wireless hardware which does not really come through a VM (in general).<br />
</p><p>Why not capture on the MAC directly? If you use @Amato's wireless link, you will find the MAC will go into monitor mode nicely and pick up lots of wireless frames. It's actually a great tool for wireless traffic capture.</p><p>Alternatively, add a USB wifi adapter and pass the USB into the VM and then you could have Linux put the device into monitor mode, etc.</p><p>Also if you just need the network traffic for some purpose, wired traffic capture is much easier.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jan '17, 14:31</strong></p><img src="https://secure.gravatar.com/avatar/0a47ef51dd9c9996d194a4983295f5a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bob%20Jones&#39;s gravatar image" /><p>Bob Jones<br />
<span class="score" title="1014 reputation points"><span>1.0k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bob Jones has 19 accepted answers">21%</span> </br></p></div></div><div id="comments-container-58750" class="comments-container"></div><div id="comment-tools-58750" class="comment-tools"></div><div class="clear"></div><div id="comment-58750-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


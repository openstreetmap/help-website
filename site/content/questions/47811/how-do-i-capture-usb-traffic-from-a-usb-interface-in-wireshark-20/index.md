+++
type = "question"
title = "How do i capture USB traffic from a USB interface in wireshark 2.0"
description = '''i was excited to hear that wireshark 2.0 has integrated with USBPcap which is a tool you can use to capture USB device traffic/activity, save as a pcap file and then open and analyse it in Wireshark. So i gave it a go, and sure enough, the option popped up during the install about installing usbpcap...'''
date = "2015-11-20T12:31:00Z"
lastmod = "2015-11-20T14:21:00Z"
weight = 47811
keywords = [ "usbpcapcmd", "wireshark-2.0", "usb", "usbpcap" ]
aliases = [ "/questions/47811" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How do i capture USB traffic from a USB interface in wireshark 2.0](/questions/47811/how-do-i-capture-usb-traffic-from-a-usb-interface-in-wireshark-20)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47811-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>i was excited to hear that wireshark 2.0 has integrated with USBPcap which is a tool you can use to capture USB device traffic/activity, save as a pcap file and then open and analyse it in Wireshark. So i gave it a go, and sure enough, the option popped up during the install about installing usbpcap or using the one already pre-installed (i had toyed around with USBpcap before). So, logically, i was expecting that at least my active USB interfaces would be listed alongside my virtual and physical network interfaces but that was not the case. I looked around a bit more and did not find anything. So can anyone help me make it possible to configure wireshark to capture USB interface data/traffic by selecting the uSB interface from among the network interfaces?</p></div><div id="question-tags" class="tags-container tags">usbpcapcmd wireshark-2.0 usb usbpcap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Nov '15, 12:31</strong></p><img src="https://secure.gravatar.com/avatar/db34a8b9a219ef7bef1764b01e4c6f08?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bob%20Ross&#39;s gravatar image" /><p>Bob Ross<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bob Ross has no accepted answers">0%</span></p></div></div><div id="comments-container-47811" class="comments-container"></div><div id="comment-tools-47811" class="comment-tools"></div><div class="clear"></div><div id="comment-47811-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47815"></span>

<div id="answer-container-47815" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47815-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You need to install the new version of USBPcap bundled with Wireshark. So I recommend you to uninstall your previous USBPcap installation (1.0.07?) and reinstall Wireshark and selecting USBPcap 1.1.0.0-g794bf26 during the installation procedure. It will install a USBPcapCMD.exe compatible with Wireshark extcap interface in extcap subfolder of your Wireshark installation. Next time you start Wireshark, you will see USBPcap interfaces listed.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Nov '15, 14:21</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-47815" class="comments-container"><span id="47822"></span><div id="comment-47822" class="comment"><div id="post-47822-score" class="comment-score"></div><div class="comment-text"><p>thanks a lot! it worked!</p></div><div id="comment-47822-info" class="comment-info"><span class="comment-age">(20 Nov '15, 15:46)</span> Bob Ross</div></div></div><div id="comment-tools-47815" class="comment-tools"></div><div class="clear"></div><div id="comment-47815-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


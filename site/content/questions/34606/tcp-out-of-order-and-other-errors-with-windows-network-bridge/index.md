+++
type = "question"
title = "TCP Out-Of-Order and other errors with Windows Network Bridge"
description = '''Hi together, after I set up a Windows Network Bridge on Windows 8.1 on a PC with 2 physical network interfaces, I&#x27;m experiencing a problem with one direction of the network connection. My setup:  - PC 1 with 2 NICs. One NIC connected to Wireless AP, the other to a switch. Network bridge setup betwee...'''
date = "2014-07-11T13:21:00Z"
lastmod = "2014-07-11T13:21:00Z"
weight = 34606
keywords = [ "networkbridge", "windows", "out-of-order" ]
aliases = [ "/questions/34606" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [TCP Out-Of-Order and other errors with Windows Network Bridge](/questions/34606/tcp-out-of-order-and-other-errors-with-windows-network-bridge)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34606-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi together,</p><p>after I set up a Windows Network Bridge on Windows 8.1 on a PC with 2 physical network interfaces, I'm experiencing a problem with one direction of the network connection. My setup: - PC 1 with 2 NICs. One NIC connected to Wireless AP, the other to a switch. Network bridge setup between these two NICs (differend models) - PC 2 with 1 NIC connected to a switch. When transferring files from PC 2 to PC 1 everything is fine and fast. The other way is too slow to transfer files. Its hardly enough for a RDP session. Wireshark shows several TCP Out-of-Order and other errors, no matter on what PC I capture. When removing the bridge everything is back to normal.</p><p>As I'm not very experienced in network related topics I hope someone will be able to help out :-)</p><p>Thanks a lot, have a nice weekend.</p></div><div id="question-tags" class="tags-container tags">networkbridge windows out-of-order</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Jul '14, 13:21</strong></p><img src="https://secure.gravatar.com/avatar/e8bbb2b98b351580378e046fb8a34c5a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Timo&#39;s gravatar image" /><p>Timo<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Timo has no accepted answers">0%</span></p></div></div><div id="comments-container-34606" class="comments-container"><span id="34612"></span><div id="comment-34612" class="comment"><div id="post-34612-score" class="comment-score"></div><div class="comment-text"><p>Can you provide a capture and upload it at www.cloudshark.org?</p></div><div id="comment-34612-info" class="comment-info"><span class="comment-age">(12 Jul '14, 01:32)</span> Jasper ♦♦</div></div><span id="34621"></span><div id="comment-34621" class="comment"><div id="post-34621-score" class="comment-score"></div><div class="comment-text"><p>Sure thing! Please find the capture here: <a href="https://www.cloudshark.org/captures/e0b524e838fa">https://www.cloudshark.org/captures/e0b524e838fa</a></p><p>Thanks for your help, much appreciated!</p></div><div id="comment-34621-info" class="comment-info"><span class="comment-age">(13 Jul '14, 05:01)</span> Timo</div></div><span id="34652"></span><div id="comment-34652" class="comment"><div id="post-34652-score" class="comment-score"></div><div class="comment-text"><p>I can't find any specific 'slowness' in one direction. Could you please add more information, especially the session you believe to be slower that the other? BTW: there are only two sessions in the capture file!.</p></div><div id="comment-34652-info" class="comment-info"><span class="comment-age">(15 Jul '14, 03:30)</span> Kurt Knochner ♦</div></div><span id="34705"></span><div id="comment-34705" class="comment"><div id="post-34705-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt, thanks for helping me out. In this short capture I just started the file transfer wich doesn't work. The direction was 192.168.0.101 --&gt; 192.168.0.25. "Slowness" in this case means, that a file transfer is nearly impossible. Please let me know, if I can get you something that might make this more clear (A special capture?). I'm no network expert unfortunately ;-)</p></div><div id="comment-34705-info" class="comment-info"><span class="comment-age">(16 Jul '14, 04:44)</span> Timo</div></div><span id="34734"></span><div id="comment-34734" class="comment"><div id="post-34734-score" class="comment-score"></div><div class="comment-text"><p>Today I found out, that it must be somehow OS related. When I activate the bridge, name resolution doesn't work anymore. Does anyone have an idea whats wrong here? I use Windows 8.1. Thanks again :-)</p></div><div id="comment-34734-info" class="comment-info"><span class="comment-age">(17 Jul '14, 12:17)</span> Timo</div></div></div><div id="comment-tools-34606" class="comment-tools"></div><div class="clear"></div><div id="comment-34606-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>


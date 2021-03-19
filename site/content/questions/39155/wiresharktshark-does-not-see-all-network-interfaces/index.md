+++
type = "question"
title = "Wireshark/Tshark does not see all network interfaces"
description = '''Hello, On a Windows 7 computer, I have startech.com USB32000SPT. It is a USB 3.0, 2-port NIC adapter. To Windows, two nics are visible when it is plugged in: ASIX AX88179 USB 3.0 to Gigabit Ethernet Adapter #1 ASIX AX88179 USB 3.0 to Gigabit Ethernet Adapter #2 In Wireshark, and in Tshark -D, only o...'''
date = "2015-01-15T04:32:00Z"
lastmod = "2015-01-15T04:32:00Z"
weight = 39155
keywords = [ "usb32000spt" ]
aliases = [ "/questions/39155" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark/Tshark does not see all network interfaces](/questions/39155/wiresharktshark-does-not-see-all-network-interfaces)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39155-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>On a Windows 7 computer, I have startech.com USB32000SPT. It is a USB 3.0, 2-port NIC adapter.</p><p>To Windows, two nics are visible when it is plugged in: ASIX AX88179 USB 3.0 to Gigabit Ethernet Adapter #1 ASIX AX88179 USB 3.0 to Gigabit Ethernet Adapter #2</p><p>In Wireshark, and in Tshark -D, only one of the two NICS appears.</p><p>Is there anything that I can do (need to do) to make both NICS appear to WS?</p><p>Thanks.</p><p>Bryan Hunt</p></div><div id="question-tags" class="tags-container tags">usb32000spt</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jan '15, 04:32</strong></p><img src="https://secure.gravatar.com/avatar/c92eec1a64a2150cbef6aef1e2070755?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="brhunt&#39;s gravatar image" /><p>brhunt<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="brhunt has no accepted answers">0%</span></p></div></div><div id="comments-container-39155" class="comments-container"><span id="39156"></span><div id="comment-39156" class="comment"><div id="post-39156-score" class="comment-score"></div><div class="comment-text"><p>I have the identical adapters and both show up on my system (and work with Wireshark).</p><p>Can you please post the output of the following two commands.</p><blockquote><p>dumpcap -D<br />
dumpcap -D -M</p></blockquote></div><div id="comment-39156-info" class="comment-info"><span class="comment-age">(15 Jan '15, 06:02)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-39155" class="comment-tools"></div><div class="clear"></div><div id="comment-39155-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>


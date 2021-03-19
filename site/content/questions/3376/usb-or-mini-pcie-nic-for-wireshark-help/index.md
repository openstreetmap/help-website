+++
type = "question"
title = "USB or Mini PCIe NIC for Wireshark? HELP!"
description = '''Does anyone know of a good mini half card for a laptop or usb NIC that supports raw, monitoring, or promiscuous mode? I am not having any luck on manufacturors websites or through email help. '''
date = "2011-04-06T08:13:00Z"
lastmod = "2011-04-06T09:16:00Z"
weight = 3376
keywords = [ "wireless", "nic", "promiscuous", "laptop", "usb" ]
aliases = [ "/questions/3376" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [USB or Mini PCIe NIC for Wireshark? HELP!](/questions/3376/usb-or-mini-pcie-nic-for-wireshark-help)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3376-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Does anyone know of a good mini half card for a laptop or usb NIC that supports raw, monitoring, or promiscuous mode? I am not having any luck on manufacturors websites or through email help.<br />
</p></div><div id="question-tags" class="tags-container tags">wireless nic promiscuous laptop usb</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Apr '11, 08:13</strong></p><img src="https://secure.gravatar.com/avatar/0b105197d9caf7e8c886c6a1f9b67405?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="are_we_hvn_fun_yet&#39;s gravatar image" /><p>are_we_hvn_f...<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="are_we_hvn_fun_yet has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-3376" class="comments-container"></div><div id="comment-tools-3376" class="comment-tools"></div><div class="clear"></div><div id="comment-3376-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3377"></span>

<div id="answer-container-3377" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3377-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Most if not all Ethernet adapters should support promiscuous mode.</p><p>On Windows, <em>NO</em> regular 802.11 adapters support monitor mode in Wireshark, and they don't support promiscuous mode, either. If you want to capture raw 802.11 traffic, you'll need an <a href="http://www.riverbed.com/us/products/cascade/airpcap.php">AirPcap adapter</a>, which is a USB device that acts only as a network traffic capture device (i.e., it won't act as a regular network adapter).</p><p>On Linux and *BSD, many 802.11 adapters support monitor mode - probably most do, including the ones built into laptops.</p><p>In Mac OS X, the AirPort adapters built into laptops and iMacs support monitor mode.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Apr '11, 09:16</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-3377" class="comments-container"></div><div id="comment-tools-3377" class="comment-tools"></div><div class="clear"></div><div id="comment-3377-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


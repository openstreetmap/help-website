+++
type = "question"
title = "Vlan tagging on Atheros network card"
description = '''Hi, I try to capture vlan tags on Atheros ar8161. I have read this instruction http://wiki.wireshark.org/CaptureSetup/VLAN but I cant find solution for vlan stripping on Atheros interface. Maybe somebody had solved this problem?'''
date = "2014-12-30T14:19:00Z"
lastmod = "2014-12-30T14:28:00Z"
weight = 38809
keywords = [ "vlan", "tag", "atheros", "tagging" ]
aliases = [ "/questions/38809" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Vlan tagging on Atheros network card](/questions/38809/vlan-tagging-on-atheros-network-card)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38809-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I try to capture vlan tags on Atheros ar8161. I have read this instruction <a href="http://wiki.wireshark.org/CaptureSetup/VLAN">http://wiki.wireshark.org/CaptureSetup/VLAN</a> but I cant find solution for vlan stripping on Atheros interface. Maybe somebody had solved this problem?</p></div><div id="question-tags" class="tags-container tags">vlan tag atheros tagging</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Dec '14, 14:19</strong></p><img src="https://secure.gravatar.com/avatar/3629b148c2fa77ae250f2544a09f999f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ortep&#39;s gravatar image" /><p>ortep<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ortep has no accepted answers">0%</span></p></div></div><div id="comments-container-38809" class="comments-container"></div><div id="comment-tools-38809" class="comment-tools"></div><div class="clear"></div><div id="comment-38809-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38811"></span>

<div id="answer-container-38811" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38811-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you are trying to do this on Windows and it does not work (you are no seeing VLAN tags), then your Windows AR8161 driver (probably) strips VLAN tags. If there is no option in the advanced driver settings or regsitry keys (ask your vendor), you still have the option to boot Linux from a CD or a flash drive.</p><p>There are many distributions that include Wireshark. One I like is Kali:</p><blockquote><p><a href="http://www.kali.org">http://www.kali.org</a><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Dec '14, 14:28</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-38811" class="comments-container"><span id="38812"></span><div id="comment-38812" class="comment"><div id="post-38812-score" class="comment-score"></div><div class="comment-text"><p>I asked about Windows 7 64bit - can't find any stripping option in driver settings. I try to define MonitorMode/PreserveVlanInfoInRxPacket in registry but nothing happend.</p><p>Lets say that I must use Windows. Can I install Kali on virtual machine (VirtualBox) and forward all network traffic (with vlans) to virtual interface?</p></div><div id="comment-38812-info" class="comment-info"><span class="comment-age">(30 Dec '14, 14:43)</span> ortep</div></div><span id="38814"></span><div id="comment-38814" class="comment"><div id="post-38814-score" class="comment-score"></div><div class="comment-text"><blockquote><p>MonitorMode/PreserveVlanInfoInRxPacket in registry but nothing happend.</p></blockquote><p>because that's Registry entries for <strong>other drivers</strong></p><blockquote><p>Can I install Kali on virtual machine (VirtualBox) and <strong>forward all network traffic (with vlans) to virtual interface?</strong></p></blockquote><p>Maybe, see here:</p><blockquote><p><a href="https://www.virtualbox.org/manual/ch06.html#network_bridged">https://www.virtualbox.org/manual/ch06.html#network_bridged</a></p></blockquote><p>However, if your adapter (in hardware) or your driver strips VLAN tags, it might not work.</p></div><div id="comment-38814-info" class="comment-info"><span class="comment-age">(30 Dec '14, 15:18)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-38811" class="comment-tools"></div><div class="clear"></div><div id="comment-38811-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


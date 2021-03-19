+++
type = "question"
title = "capturing packets from pc startup"
description = '''Is there any way I can capture all packets from my ethernet network adapter from the point where my desktop is first displayed? The reason being my pc hangs upon windows startup, for a good minute or more... I have noticed using procmon.exe that although it seems nothing is happening, procmon.exe re...'''
date = "2010-09-19T15:49:00Z"
lastmod = "2012-07-20T13:27:00Z"
weight = 222
keywords = [ "windows", "capture", "packets", "boot-process" ]
aliases = [ "/questions/222" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [capturing packets from pc startup](/questions/222/capturing-packets-from-pc-startup)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-222-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there any way I can capture all packets from my ethernet network adapter from the point where my desktop is first displayed? The reason being my pc hangs upon windows startup, for a good minute or more... I have noticed using procmon.exe that although it seems nothing is happening, procmon.exe reports svchost.exe is looking at almost every file on my computer. then after a while, this 'hang' status disappears and my startup items, as listed in msconfig then start up. Therefore, putting wireshark into my startup programs will not serve the purpose because I want to see what traffic is taking place during this apparent 'hang' at startup. I have run a full virus scan with kaspersky pure and no treats appear. Any suggestions most welcome and thank you in advance.</p></div><div id="question-tags" class="tags-container tags">windows capture packets boot-process</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Sep '10, 15:49</strong></p><img src="https://secure.gravatar.com/avatar/1e82a56fdbd12a1e9cd84b6257dd5b94?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Stezzer4298&#39;s gravatar image" /><p>Stezzer4298<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Stezzer4298 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Sep '10, 01:53</p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span></p></div></div><div id="comments-container-222" class="comments-container"></div><div id="comment-tools-222" class="comment-tools"></div><div class="clear"></div><div id="comment-222-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="225"></span>

<div id="answer-container-225" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-225-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark, just like any other packet capturing software, can only be started after the PC has been started up. You need to use a second PC to capture the packets of the PC whose network traffic of the boot-process you want to capture. You can either use a (real) hub to duplicate the packets, a switch with mirror capabilities, a network tap or create a machine-in-the-middle machine.</p><p>These options are explained on the wireshark wiki:</p><ul><li><a href="http://wiki.wireshark.org/CaptureSetup">http://wiki.wireshark.org/CaptureSetup</a></li><li><a href="http://wiki.wireshark.org/CaptureSetup/Ethernet">http://wiki.wireshark.org/CaptureSetup/Ethernet</a></li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Sep '10, 00:23</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-225" class="comments-container"><span id="316"></span><div id="comment-316" class="comment"><div id="post-316-score" class="comment-score"></div><div class="comment-text"><p>Thank you SynBit for your explanation with reference link, I really appreciate your help and will give this a try.</p></div><div id="comment-316-info" class="comment-info"><span class="comment-age">(24 Sep '10, 09:56)</span> Stezzer4298</div></div></div><div id="comment-tools-225" class="comment-tools"></div><div class="clear"></div><div id="comment-225-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="12886"></span>

<div id="answer-container-12886" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12886-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If someone with rights to install a service, I'd suggest using the AutoExNT utility as supplied from the resource kits, and running dumpcap from the associated BAT file. This link provides instructions for an out-of-date OS, but they work on xp &amp; windows 7.</p><p><a href="http://support.microsoft.com/kb/243486">http://support.microsoft.com/kb/243486</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Jul '12, 13:27</strong></p><img src="https://secure.gravatar.com/avatar/f925156d68c922919a4ffe0b3d857be3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kcullimo&#39;s gravatar image" /><p>kcullimo<br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kcullimo has no accepted answers">0%</span></p></div></div><div id="comments-container-12886" class="comments-container"></div><div id="comment-tools-12886" class="comment-tools"></div><div class="clear"></div><div id="comment-12886-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


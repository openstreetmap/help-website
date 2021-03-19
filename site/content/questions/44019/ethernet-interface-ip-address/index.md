+++
type = "question"
title = "ethernet interface ip address"
description = '''hello, i am giving my ethernet interface static ip, i am trying to run wireshark over different eth interfaces, i have eth1 ,eth2 and i am not using eth0, can i give eth1 and eth2 same ip address when i am not using both of them at the same time ? and if it&#x27;s possible in this case, what about when i...'''
date = "2015-07-09T10:33:00Z"
lastmod = "2015-07-10T05:56:00Z"
weight = 44019
keywords = [ "ethernet", "interfaces", "configuration", "static" ]
aliases = [ "/questions/44019" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [ethernet interface ip address](/questions/44019/ethernet-interface-ip-address)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44019-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hello, i am giving my ethernet interface static ip, i am trying to run wireshark over different eth interfaces, i have eth1 ,eth2 and i am not using eth0, can i give eth1 and eth2 same ip address when i am not using both of them at the same time ? and if it's possible in this case, what about when i use them at Same time ? noting im on Linux machines and over tcp connection.</p></div><div id="question-tags" class="tags-container tags">ethernet interfaces configuration static</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Jul '15, 10:33</strong></p><img src="https://secure.gravatar.com/avatar/890399e77f2c0c0ff2f75ea2f43d3ff8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yas1234&#39;s gravatar image" /><p>yas1234<br />
<span class="score" title="16 reputation points">16</span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yas1234 has no accepted answers">0%</span></p></div></div><div id="comments-container-44019" class="comments-container"></div><div id="comment-tools-44019" class="comment-tools"></div><div class="clear"></div><div id="comment-44019-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="44020"></span>

<div id="answer-container-44020" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44020-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>No, the IP Address of each NIC must be different if they are on the same network.</p><p>Each NIC is it's own entity even if they are installed on the same computer.</p><p>In the perspective of the other nodes/devices on the network, your eth1 and eth2 NIC's are no different than if they were completely different computers. - And you might already know that different devices/computers on the same network must have unique IP Addresses.</p><p>In other words, just because your NIC's are on the same computer, doesn't mean that you can get away from the rule that the NIC's can have the same IP Address.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Jul '15, 10:39</strong></p><img src="https://secure.gravatar.com/avatar/1259897b9b42059302967b55c0dc2228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KTM&#39;s gravatar image" /><p>KTM<br />
<span class="score" title="76 reputation points">76</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KTM has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Jul '15, 10:45</p></div></div><div id="comments-container-44020" class="comments-container"></div><div id="comment-tools-44020" class="comment-tools"></div><div class="clear"></div><div id="comment-44020-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="44051"></span>

<div id="answer-container-44051" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44051-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>@yas1234 - I am uncertain of your application of using two Ethernet interfaces for capturing data, but you might want to read the Wireshark wiki regarding Ethernet capturing:</p><p><a href="https://wiki.wireshark.org/CaptureSetup/Ethernet">https://wiki.wireshark.org/CaptureSetup/Ethernet</a></p><p>Refer to section called "Capture using a network tap", 4.5. Starting in version 1.8, Wireshark is able to capture from two interfaces at once. In addition most Linux distros support bonding of interfaces.</p><p><a href="http://www.linuxfoundation.org/collaborate/workgroups/networking/bonding">http://www.linuxfoundation.org/collaborate/workgroups/networking/bonding</a></p><p>"The Linux bonding driver provides a method for aggregating multiple network interfaces into a single logical bonded interface."</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jul '15, 05:56</strong></p><img src="https://secure.gravatar.com/avatar/d9cf592a79eafbc3b2a8b3f38cf38362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amato_C&#39;s gravatar image" /><p>Amato_C<br />
<span class="score" title="1098 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amato_C has 15 accepted answers">14%</span></p></div></div><div id="comments-container-44051" class="comments-container"></div><div id="comment-tools-44051" class="comment-tools"></div><div class="clear"></div><div id="comment-44051-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


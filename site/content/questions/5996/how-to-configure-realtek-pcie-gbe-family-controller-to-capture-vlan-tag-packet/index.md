+++
type = "question"
title = "How to configure &quot;Realtek PCIe GBE Family Controller&quot;  to capture vlan tag packet?"
description = '''Could you please tell me how to configure Ethernet card for capturing vlan tag packet with wireshark? My ethernet card is the &quot;Realtek PCIe GBE Family Controller&quot; in WINDOWS 7. I have download the latest drivers and the utility software. with the utility network software i have te possibility to set...'''
date = "2011-08-31T06:38:00Z"
lastmod = "2016-06-01T08:48:00Z"
weight = 5996
keywords = [ "realtek", "qinq", "vlan" ]
aliases = [ "/questions/5996" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How to configure "Realtek PCIe GBE Family Controller" to capture vlan tag packet?](/questions/5996/how-to-configure-realtek-pcie-gbe-family-controller-to-capture-vlan-tag-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5996-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Could you please tell me how to configure Ethernet card for capturing vlan tag packet with wireshark? My ethernet card is the "Realtek PCIe GBE Family Controller" in WINDOWS 7. I have download the latest drivers and the utility software. with the utility network software i have te possibility to set vlan id in the port but the wireshark isn't able to capture vlan id (I Send ethernet frames with 1518 bytes packet size and the wireshark captures 1514 bytes. the 4 bytes for vlan tagging don't appear). thanks</p></div><div id="question-tags" class="tags-container tags">realtek qinq vlan</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Aug '11, 06:38</strong></p><img src="https://secure.gravatar.com/avatar/a38e15befb6d704b57aa8513c40c2ef4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="akalavri&#39;s gravatar image" /><p>akalavri<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="akalavri has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 31 Aug '11, 06:40</p></div></div><div id="comments-container-5996" class="comments-container"><span id="19267"></span><div id="comment-19267" class="comment"><div id="post-19267-score" class="comment-score"></div><div class="comment-text"><p>Hello,</p><p>I have the same "Realtek PCIe GBE Family Controller" in Windows 7 Home Premium, driver 7.67.1226.2012. I have disabled the setting "Priority &amp; VLAN" and the Wireshark is NOT able to capture the Vlan ID. Thanks for the answers!</p></div><div id="comment-19267-info" class="comment-info"><span class="comment-age">(07 Mar '13, 02:22)</span> Josemi</div></div></div><div id="comment-tools-5996" class="comment-tools"></div><div class="clear"></div><div id="comment-5996-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="6016"></span>

<div id="answer-container-6016" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6016-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>The "Realtek PCIe GBE Family Controller" NIC can be configured to <strong>not</strong> strip the vlan tags, by going to the Adapter Settings and setting "Priority &amp; VLAN" to "Priority &amp; VLAN disabled". All the other values for this option will make the driver delete the VLAN tags from the frame.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Aug '11, 10:25</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-6016" class="comments-container"><span id="6070"></span><div id="comment-6070" class="comment"><div id="post-6070-score" class="comment-score"></div><div class="comment-text"><p>I disabled the setting "Priority &amp; VLAN" and the Wireshark is able to capture the Vlan ID. Thanks for the answers!</p></div><div id="comment-6070-info" class="comment-info"><span class="comment-age">(04 Sep '11, 02:23)</span> akalavri</div></div><span id="6071"></span><div id="comment-6071" class="comment"><div id="post-6071-score" class="comment-score"></div><div class="comment-text"><p>I changed your answer to a comment to keep the nature of Q&amp;A going. You might want to accept SYNbits answer by using the checkmark button to the left to mark it as accepted.</p></div><div id="comment-6071-info" class="comment-info"><span class="comment-age">(04 Sep '11, 02:59)</span> Jasper ♦♦</div></div><span id="41520"></span><div id="comment-41520" class="comment"><div id="post-41520-score" class="comment-score"></div><div class="comment-text"><p>This Q&amp;A saved my life. Just goes to show the internet can solve just about anything if you know what question to ask. Thank you people of the internet :-)</p><p>So... yeah, I was having difficulty getting anything to fly on my realtek adapaters to between my router/switch lab. I could never figure out if the "VLAN &amp; Priority" was supposed to be disabled or enabled so I figured enabled would allow VLAN traffic to pass and the only other comments on it said, "if you have VLAN &amp; Priority in the adpater settings then it supports VLAN tagging..." ugh... thank you again. I buy you shots of your choice :-)</p></div><div id="comment-41520-info" class="comment-info"><span class="comment-age">(16 Apr '15, 21:57)</span> Iz Lo</div></div></div><div id="comment-tools-6016" class="comment-tools"></div><div class="clear"></div><div id="comment-6016-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="5999"></span>

<div id="answer-container-5999" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5999-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The Realtek cards I have usually allow capturing of VLAN tags without any problems, and it shouldn't be necessary to set any VLAN id on the capture card itself.</p><p>If you're saying you're only getting 1514 bytes I'd guess it's an untagged frame without the FCS (Ethernet checksum), not the VLAN header - which would mean, you can't capture VLAN tags because there weren't any. If you're capturing on a SPAN port you probably have to tell the switch to include VLAN tags in the spanned data (on Cisco devices you can do that by telling it to include the "encapsulation dot1q" when creating the span session). Otherwise the switch will strip the VLAN header before copying it to the SPAN output port.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Aug '11, 06:45</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 31 Aug '11, 06:46</p></div></div><div id="comments-container-5999" class="comments-container"></div><div id="comment-tools-5999" class="comment-tools"></div><div class="clear"></div><div id="comment-5999-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="53113"></span>

<div id="answer-container-53113" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53113-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I wasn't able to get this to work properly just changing the "Priority &amp; Vlan" setting. After 2 days of exploring and various google searches I found <a href="http://forum.gns3.net/topic7559.html">this</a> topic.</p><p>If changing that setting alone doesn't work for you:</p><p>1: Update your realtek drivers</p><p>2: The key HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Control\Class{4D36E972-E325-11CE-BFC1-08002BE10318}\00nn needs to have 4 values. '00nn' is the specific key that has the information for the adapter you intend on capturing on. Add or edit the following DWORDs</p><pre><code>MonitorModeEnabled - 1
MonitorMode - 1
*PriorityVLANTag - 0
SkDisableVlanStrip - 1</code></pre><p>Restart your computer, make sure there's no firewall preventing wireshark from seeing the nolonger vlan tagged packets, and you should be good to go.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jun '16, 08:48</strong></p><img src="https://secure.gravatar.com/avatar/8475c381134dd89b1d582586d020e4ed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Darinth&#39;s gravatar image" /><p>Darinth<br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Darinth has no accepted answers">0%</span></p></div></div><div id="comments-container-53113" class="comments-container"><span id="53150"></span><div id="comment-53150" class="comment"><div id="post-53150-score" class="comment-score"></div><div class="comment-text"><p>Thanks, this has really worked!</p></div><div id="comment-53150-info" class="comment-info"><span class="comment-age">(02 Jun '16, 09:35)</span> Josemi</div></div><span id="59107"></span><div id="comment-59107" class="comment"><div id="post-59107-score" class="comment-score"></div><div class="comment-text"><p>Thanks Darinth it worked, I just modified the MonitorModeEnabled, it was in 0. The *PriorityVLANTag was already in 0. I didn't add MonitorMode neither add SkDisableVlanStrip. I modified the "Priority &amp; VLAN" settings and set to "Priority &amp; VLAN disabled" but it didn't work.</p></div><div id="comment-59107-info" class="comment-info"><span class="comment-age">(27 Jan '17, 07:15)</span> Adan Ortiz</div></div></div><div id="comment-tools-53113" class="comment-tools"></div><div class="clear"></div><div id="comment-53113-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


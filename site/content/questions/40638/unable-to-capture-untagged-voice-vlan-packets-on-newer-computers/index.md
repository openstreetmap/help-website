+++
type = "question"
title = "Unable to capture untagged voice vlan packets on newer computers"
description = '''Hi Guys, Got a bit of a strange one with a IP phone using an untagged voice vlan and a untagged data vlan. I am capturing the traffic through a 3750x for the following int: source (IP Phone): interface GigabitEthernet2/0/3  description Mitel IP Phone  switchport access vlan 108  switchport voice vla...'''
date = "2015-03-17T08:25:00Z"
lastmod = "2015-03-17T12:13:00Z"
weight = 40638
keywords = [ "capture", "vlan", "voip" ]
aliases = [ "/questions/40638" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Unable to capture untagged voice vlan packets on newer computers](/questions/40638/unable-to-capture-untagged-voice-vlan-packets-on-newer-computers)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40638-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Guys,</p><p>Got a bit of a strange one with a IP phone using an untagged voice vlan and a untagged data vlan.</p><p>I am capturing the traffic through a 3750x for the following int:</p><pre><code>source (IP Phone):
interface GigabitEthernet2/0/3
 description Mitel IP Phone
 switchport access vlan 108
 switchport voice vlan 107
 mls qos trust dscp</code></pre><p>mirroring the port:</p><p>Session 1</p><pre><code>Type                    Local Session
Source Ports           : 
    Both               : Gi2/0/3
Destination Ports      : Gi1/0/8
    Encapsulation      : Native
          Ingress      : Disabled</code></pre><p>If i use laptop #1:</p><pre><code>OS - win 7 x86
wireshark - 1.10.6 
win pcap 4.1.3 
NIC - intel (R) 82577LM</code></pre><p>it works fine when i capture and filter:</p><p>ip.addr==ip phone ip</p><p>However as i need to capture a call at multiple locations, i need another machine with wireshark:</p><p>Laptop#2 :</p><pre><code>OS - win 7 x64
wireshark - 1.12.4 
win pcap 4.1.3 
NIC - Broadcom NetXtreme Gigabit Ethernet</code></pre><p>I'm unable to see any packets for the untagged voice vlan 107 even through im using the same syntax and same destination port and cable.</p><p>I have tried this on multiple different machines and it seems that anything relatively new doesnt work</p><p>Any help would be greatly appreciated, thank you</p><p>Rich</p></div><div id="question-tags" class="tags-container tags">capture vlan voip</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Mar '15, 08:25</strong></p><img src="https://secure.gravatar.com/avatar/0d439d1593e89dc017bcc5c30cdf05ba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RJE&#39;s gravatar image" /><p>RJE<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RJE has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 Mar '15, 09:48</p></div></div><div id="comments-container-40638" class="comments-container"></div><div id="comment-tools-40638" class="comment-tools"></div><div class="clear"></div><div id="comment-40638-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40644"></span>

<div id="answer-container-40644" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40644-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>First of all, your configuration makes the switch forward the voice packets with a 802.1Q tag of 107. Have a look at <a href="http://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst2950/software/release/12-1_11_yj/configuration/guide/scg/swvoip.html">http://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst2950/software/release/12-1_11_yj/configuration/guide/scg/swvoip.html</a>:</p><pre><code>switchport voice vlan vlan-id

Instruct the Cisco IP phone to forward all voice traffic through the specified VLAN. By default, the Cisco IP phone forwards the voice traffic with an 802.1Q priority of 5.

Valid VLAN IDs are from 1 to 4094 when the enhanced software image (EI) is installed and 1 to 1001 when the standard software image is installed. Do not enter leading zeros.</code></pre><p>Whether vlan tagged frames are being discarded or forwarded with the vlan tags stripped or as is depends on the registry settings for the NIC driver. Have a look at <a href="https://wiki.wireshark.org/CaptureSetup/VLAN#Windows">https://wiki.wireshark.org/CaptureSetup/VLAN#Windows</a> for more info on how to capture vlan tagged packets.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Mar '15, 12:13</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-40644" class="comments-container"><span id="40651"></span><div id="comment-40651" class="comment"><div id="post-40651-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the reply Syn-bit, trying out these fixes now</p></div><div id="comment-40651-info" class="comment-info"><span class="comment-age">(18 Mar '15, 03:48)</span> RJE</div></div></div><div id="comment-tools-40644" class="comment-tools"></div><div class="clear"></div><div id="comment-40644-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


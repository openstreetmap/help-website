+++
type = "question"
title = "Packet from Device how to integrate and show up virtually in wireshark device list"
description = '''I have written a device driver to read Infiniband packets for some properity infiniband Cards. I will getting packet to user space by reading a charector device file and even i dont want to register to netdevice ..  Can please let me know as to how can i integrate my driver with wireshark .. I would...'''
date = "2011-02-04T05:55:00Z"
lastmod = "2011-02-13T13:43:00Z"
weight = 2146
keywords = [ "device", "from", "packets", "file.." ]
aliases = [ "/questions/2146" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Packet from Device how to integrate and show up virtually in wireshark device list](/questions/2146/packet-from-device-how-to-integrate-and-show-up-virtually-in-wireshark-device-list)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2146-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have written a device driver to read Infiniband packets for some properity infiniband Cards. I will getting packet to user space by reading a charector device file and even i dont want to register to netdevice .. Can please let me know as to how can i integrate my driver with wireshark .. I would like to know where can i hookup , my packet read function. and how can i register a device with wireshark , so whenever user clicks i want to start reading packets from tht device file and then get feeded to dissector ..</p><p>How to virtually showup in wireshark device list it might be some data structure where i need to provide device name and corrospinding read function for the same. I would appriciate if you point me to name of file and procedure to acheive same.</p></div><div id="question-tags" class="tags-container tags">device from packets file..</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Feb '11, 05:55</strong></p><img src="https://secure.gravatar.com/avatar/eb8b3c7eb38dfdef188cc69a356dc135?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mdayyaz&#39;s gravatar image" /><p>mdayyaz<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mdayyaz has no accepted answers">0%</span></p></div></div><div id="comments-container-2146" class="comments-container"></div><div id="comment-tools-2146" class="comment-tools"></div><div class="clear"></div><div id="comment-2146-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="2159"></span>

<div id="answer-container-2159" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2159-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark doesn't concern itself with packet capture, that task is delegated to <a href="http://www.wireshark.org/docs/man-pages/dumpcap.html">dumpcap</a>. Dumpcap itsels doesn't do the packet capture, that is done via libpcap, or WinPcap on Windows. These capture libraries, or service, is only capable of handling devices in the network domain. Therefore your character device won't be accessible.</p><p>There are two ways to solve that:</p><ol><li>Create a net device</li><li>Create a support reader process that can pipe network packets to Wireshark.</li></ol><p>From your description the last option looks the most attractive. Look at the Wireshark command line options to see how to interface with pipes.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Feb '11, 14:19</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-2159" class="comments-container"></div><div id="comment-tools-2159" class="comment-tools"></div><div class="clear"></div><div id="comment-2159-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="2312"></span>

<div id="answer-container-2312" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2312-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Actually, there's a third way to solve that:</p><p>Change libpcap or WinPcap (although, as he says "character device file", he's probably not using Windows, so it's libpcap) to support your device. The best place to ask about this is <a href="http://www.tcpdump.org/#mailing-lists">the tcpdump-workers mailing list</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Feb '11, 13:43</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 Feb '11, 13:43</p></div></div><div id="comments-container-2312" class="comments-container"></div><div id="comment-tools-2312" class="comment-tools"></div><div class="clear"></div><div id="comment-2312-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


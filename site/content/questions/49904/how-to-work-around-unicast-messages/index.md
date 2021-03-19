+++
type = "question"
title = "how to work around unicast messages"
description = '''Hi I&#x27;m a newby and I&#x27;m trying to capture some information using Wireshark and I&#x27;m not able to see it. I&#x27;ve read through the FAQ page a couple of times and I believe my issue is with the actual messages I&#x27;m looking for. I have a very small network, one router, 2 3rd party products, and a laptop runni...'''
date = "2016-02-05T13:32:00Z"
lastmod = "2016-02-05T14:24:00Z"
weight = 49904
keywords = [ "unicast", "snmp", "mibs" ]
aliases = [ "/questions/49904" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [how to work around unicast messages](/questions/49904/how-to-work-around-unicast-messages)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49904-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi I'm a newby and I'm trying to capture some information using Wireshark and I'm not able to see it. I've read through the FAQ page a couple of times and I believe my issue is with the actual messages I'm looking for. I have a very small network, one router, 2 3rd party products, and a laptop running the 3rd party application that communicates with the 2 products. I want to add a sniffer onto the network to see the communication between the application and the products. I believe MIBs are being transmitted using SNMP protocol and I basically can't see anything relating to the data on the sniffer. I see a lot messages but nothing related to the actual data. I'm assuming they are broadcast messages. Maybe there is a private community associated with the MIBs I'm looking for or maybe it's a unicast message. Wireshark appears to be configured in promiscuous mode running on my laptop (independent of the laptop in the current network). I don't know if my network interface into the network is my network card or the common router I'm connected to. Can I do something using wireshark in terms of its setup or operation to see these messages or am I out of luck because it is a proprietary messaging. I know it's not a specific question but any input would be helpful. Thanks</p></div><div id="question-tags" class="tags-container tags">unicast snmp mibs</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Feb '16, 13:32</strong></p><img src="https://secure.gravatar.com/avatar/00afa4fa65698c8cd860320ef99ed9de?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hockey5&#39;s gravatar image" /><p>hockey5<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hockey5 has no accepted answers">0%</span></p></div></div><div id="comments-container-49904" class="comments-container"></div><div id="comment-tools-49904" class="comment-tools"></div><div class="clear"></div><div id="comment-49904-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="49908"></span>

<div id="answer-container-49908" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49908-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I cannot see a reason why SNMP would use broadcast, so let's concentrate on the unicast messages. Also, I would assume that in such a simple network, the box between the laptop running the control application and the 2 devices is more likely to be a switch than a router, but it is not really important for the principle.</p><p>The principle is that if you want to see unicast traffic which is sent neither by nor to the interface you use for capturing, you must use a tap, a hub, or a switch with traffic monitoring capability to obtain a copy of the traffic and deliver it to the interface on which you are capturing.</p><p>Have you read <a href="https://wiki.wireshark.org/CaptureSetup/Ethernet">this page</a>? In your specific case, if you can capture on the laptop running the 3pty application, you don't need any additional hardware. If you cannot for any reason, you may still be lucky and the box you call "router" may be a manageable switch with monitoring capability, a router capable of taking traffic captures or, much less likely, a hub. In any other case you'll have to obtain additional hardware.</p><p>Only after capturing the traffic between the control laptop and the devices (which you recognize by source and destination IP addresses) you'll be able to see whether SNMP or some other protocol is used between them.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Feb '16, 14:18</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-49908" class="comments-container"></div><div id="comment-tools-49908" class="comment-tools"></div><div class="clear"></div><div id="comment-49908-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="49911"></span>

<div id="answer-container-49911" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49911-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You don't indicate whether your network is Ethernet or Wireless, you should read the appropriate Capture setup page for <a href="https://wiki.wireshark.org/CaptureSetup/Ethernet">Ethernet</a> or <a href="https://wiki.wireshark.org/CaptureSetup/WLAN">Wireless</a>.</p><p>Presuming you have Wireshark installed on the laptop running the application you should be able to capture traffic on the appropriate NIC for the products.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Feb '16, 14:24</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-49911" class="comments-container"></div><div id="comment-tools-49911" class="comment-tools"></div><div class="clear"></div><div id="comment-49911-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


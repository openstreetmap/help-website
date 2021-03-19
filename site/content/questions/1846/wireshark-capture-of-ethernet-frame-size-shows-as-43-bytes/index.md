+++
type = "question"
title = "Wireshark capture of Ethernet frame - size shows as 43 bytes"
description = '''Hi there, I&#x27;m using Wireshark in an attempt, along with other means, as a learning tool. Bearing in mind that the supposed minimum length of an Ethernet Frame is 64 bytes, I can&#x27;t quite work out the following capture from Wireshark. I basically sent a ping of 1 byte in size to my default gateway, an...'''
date = "2011-01-21T05:08:00Z"
lastmod = "2011-01-22T17:01:00Z"
weight = 1846
keywords = [ "10base2" ]
aliases = [ "/questions/1846" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark capture of Ethernet frame - size shows as 43 bytes](/questions/1846/wireshark-capture-of-ethernet-frame-size-shows-as-43-bytes)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1846-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi there,</p><p>I'm using Wireshark in an attempt, along with other means, as a learning tool. Bearing in mind that the supposed minimum length of an Ethernet Frame is 64 bytes, I can't quite work out the following capture from Wireshark. I basically sent a ping of 1 byte in size to my default gateway, and here is the information from Wireshark:</p><p><img src="http://i1207.photobucket.com/albums/bb462/white-zombie1/WiresharkEthernet.jpg" alt="alt text" /></p><p>I can't understand why the frame only seems to be 43 bytes in length.</p><p>According to this article:</p><p>http://wiki.wireshark.org/Ethernet</p><p>The preamble (8 bytes) and Frame Check Sequence (4 bytes) may not be displayed, yet this takes that total frame size up to 55 bytes.</p><p>Am I reading this incorrectly, ir missing something? Are there implementations of Ethernet that do not specify a minimum frame length?</p><p>Any help would be appreciated</p></div><div id="question-tags" class="tags-container tags">10base2</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Jan '11, 05:08</strong></p><img src="https://secure.gravatar.com/avatar/c87806af2099c3361fbcfe5e0300a7ed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="whitezombie&#39;s gravatar image" /><p>whitezombie<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="whitezombie has no accepted answers">0%</span></p></img></div></div><div id="comments-container-1846" class="comments-container"></div><div id="comment-tools-1846" class="comment-tools"></div><div class="clear"></div><div id="comment-1846-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="1847"></span>

<div id="answer-container-1847" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1847-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>This is outgoing traffic from your PC. That means that it hits the capture engine before passing on to the network card. It's at that lower layer that the 64 octet rule comes into play.</p><p>Try capturing 'on the wire' with another PC on a hub or monitor port of a switch. Then spot the difference.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jan '11, 05:28</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-1847" class="comments-container"><span id="1850"></span><div id="comment-1850" class="comment"><div id="post-1850-score" class="comment-score"></div><div class="comment-text"><p>Aha, thank you, I looked at the response, and the "Bytes on Wire" is 60, so presumably this is the frame, with buffers, having had the Preamble and/or the FCS removed, and passed 'up', and captured by Wireshark?</p><p>Thank you very much!</p></div><div id="comment-1850-info" class="comment-info"><span class="comment-age">(21 Jan '11, 06:32)</span> whitezombie</div></div><span id="1851"></span><div id="comment-1851" class="comment"><div id="post-1851-score" class="comment-score">1</div><div class="comment-text"><p>Yes and no.</p><p>Yes - the FCS is usually removed from all frames, so you see 60 bytes at the receiving side when the frame had 64 bytes for real.</p><p>And no - it is not the preamble missing on the sender side, but the padding bytes. What you see is 14 bytes ethernet header, 20 bytes IP header, 8 bytes ICMP header, 1 byte payload, equals 43. The NIC will later add padding bytes to get it up to 60 bytes and adds the FCS. Voila, 64 bytes - but Wireshark grabs the packet too early as Jaap already explained, so you see 43 bytes on the sender side.</p></div><div id="comment-1851-info" class="comment-info"><span class="comment-age">(21 Jan '11, 09:14)</span> Jasper ♦♦</div></div><span id="1873"></span><div id="comment-1873" class="comment"><div id="post-1873-score" class="comment-score"></div><div class="comment-text"><p>Thank you Jasper (and Jaap). Sorry, what I meant was when I see the response to the ping, it shows as 60 bytes, which I presumed was the frame minus the FCS. Dopes the Preamle not actually display as part of the frame, as it's all it's doing is, according to Cisco: "Preamble (PRE) - Consists of 7 bytes. The PRE is an alternating pattern of ones and zeros that tells receiving stations that a frame is coming, and that provides a means to synchronize the frame-reception portions of receiving physical layers with the incoming bit stream", so may not strictly be seen as part of the frame?</p><p>Presumably then, with the outgoing frame, if it consists of 14 bytes ethernet header, and the rest being info from the upper layers, the data is not captured as it leaves the Ethernet interface, as there's no evidence yet of Ethernet SOF, DA, SA, Length/Type, Data and FCS. Though not sure what the Ethernet header consists, of, will have to have a look.</p></div><div id="comment-1873-info" class="comment-info"><span class="comment-age">(22 Jan '11, 02:56)</span> whitezombie</div></div></div><div id="comment-tools-1847" class="comment-tools"></div><div class="clear"></div><div id="comment-1847-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1884"></span>

<div id="answer-container-1884" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1884-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi, no, the Preamble is not part of the frame and cannot be captured with Wireshark (and I know of no other other network analyzer using standard PC NICs that could). Your 60 bytes frame is the 64 byte minimum frame minus the FCS, which had been discarded since it's not necessary to keep it. If it had been wrong the frame would have been dropped anyway, and Wireshark would never have seen it.</p><p>The Ethernet header is 14 bytes, 6 for the destination address, 6 for the source address, and 2 for the ethertype telling which protocol header comes next. Usually it's hex 0800 for IPv4 or 0806 for ARP, but others can be observed sometimes as well (IPv6 coming up with 86DD). If you take a look at your 43 byte ping packet you will see that everything's in there: the ethernet, ip, icmp headers plus your 1 byte ping payload. All that is missing is the padding that is added later to get to 60 bytes, which will be enough to get to 64 required minimum size with the FCS applied.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jan '11, 17:01</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-1884" class="comments-container"><span id="1909"></span><div id="comment-1909" class="comment"><div id="post-1909-score" class="comment-score"></div><div class="comment-text"><p>Ah yes, well done.</p><p>For the outgoing Ping. IP Header Length 20 bytes, ICMP 8 bytes, plus 1 byte pay load. Ethernet - 6 bytes each for the Mac address of my network card, and then my default gateway, plus two for the type (IP (0x0800).</p><p>Thanks for all your help.</p></div><div id="comment-1909-info" class="comment-info"><span class="comment-age">(24 Jan '11, 13:19)</span> whitezombie</div></div></div><div id="comment-tools-1884" class="comment-tools"></div><div class="clear"></div><div id="comment-1884-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


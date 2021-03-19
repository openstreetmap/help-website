+++
type = "question"
title = "Packet type, ethernet type and HLP?"
description = '''Frame 1 (42 bytes on wire, 42 bytes captured) Ethernet II, Src: AsustekC_b3:af:31 (00:18:f3:b3:af:31), Dst: Broadcast (ff:ff:ff:ff:ff:ff) Destination: Broadcast (ff:ff:ff:ff:ff:ff) Address: Broadcast (ff:ff:ff:ff:ff:ff) .... ...1 .... .... .... .... = IG bit: Group address (multicast/broadcast) .......'''
date = "2011-01-29T15:02:00Z"
lastmod = "2011-01-30T05:28:00Z"
weight = 2012
keywords = [ "ethertype", "hexidecimal", "protocol", "packet" ]
aliases = [ "/questions/2012" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Packet type, ethernet type and HLP?](/questions/2012/packet-type-ethernet-type-and-hlp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2012-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2012-score" class="post-score" title="current number of votes">0</div><span id="post-2012-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><pre><code>Frame 1 (42 bytes on wire, 42 bytes captured)
Ethernet II, Src: AsustekC_b3:af:31 (00:18:f3:b3:af:31), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
Destination: Broadcast (ff:ff:ff:ff:ff:ff)
Address: Broadcast (ff:ff:ff:ff:ff:ff)
.... ...1 .... .... .... .... = IG bit: Group address (multicast/broadcast)
.... ...0 .... .... .... .... = LG bit: Locally administered address (this is NOT the factory default)
Source: AsustekC_b3:af:31 (00:18:f3:b3:af:31)
Address: AsustekC_b3:af:31 (00:18:f3:b3:af:31)
.... ...0 .... .... .... .... = IG bit: Individual address (unicast)
.... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
Type: ARP
Address Resolution Protocol (request)
Hardware type: Ethernet (0x0001)
Protocol type: IP (0x0800)
Hardware size: 6
Protocol size: 4
Opcode: request (0x0001)
Sender MAC address: AsustekC_b3:af:31 (00:18:f3:b3:af:31)
Sender IP address: 172.26.1.25 (172.26.1.25)
Target MAC address: 00:00:00_00:00 (00:00:00:00:00:00)
Target IP address: 172.26.1.33 (172.26.1.33)</code></pre><p>I need to know:</p><pre><code>1. highest level protocol that is carried in this frame?
2. type of packet that this protocol message is encapsulated in?
3. the EherType value (in Hex) that identifies this protocol?</code></pre><p>I know it's probably all right there in front of me but I'm really new at this and can't seem to decipher it.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ethertype" rel="tag" title="see questions tagged &#39;ethertype&#39;">ethertype</span> <span class="post-tag tag-link-hexidecimal" rel="tag" title="see questions tagged &#39;hexidecimal&#39;">hexidecimal</span> <span class="post-tag tag-link-protocol" rel="tag" title="see questions tagged &#39;protocol&#39;">protocol</span> <span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Jan '11, 15:02</strong></p><img src="https://secure.gravatar.com/avatar/18b9653dabf61ed9c3db78e485792e93?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GeekyKitty&#39;s gravatar image" /><p><span>GeekyKitty</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GeekyKitty has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>29 Jan '11, 16:56</strong> </span></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span></p></div></div><div id="comments-container-2012" class="comments-container"></div><div id="comment-tools-2012" class="comment-tools"></div><div class="clear"></div><div id="comment-2012-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="2013"></span>

<div id="answer-container-2013" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2013-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2013-score" class="post-score" title="current number of votes">1</div><span id="post-2013-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Looks like a pretty normal ARP request to me, so:</p><ol><li>highest level protocol would be ARP</li><li>not sure what you mean, but this ARP request is encapsulated in an ethernet frame and looking for a MAC address belonging to an IPv4 address</li><li>Ethertype for is 0x0806, which usually appears in the same line like the "Type: ARP" you have quoted. At least my Wireshark quotes it right behind it, so my ARP packets have a line like this: "<code>Type: ARP (0x0806)</code>". No idea why yours doesn't.</li></ol><p>Hope this helps.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jan '11, 05:03</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>30 Jan '11, 05:04</strong> </span></p></div></div><div id="comments-container-2013" class="comments-container"></div><div id="comment-tools-2013" class="comment-tools"></div><div class="clear"></div><div id="comment-2013-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="2018"></span>

<div id="answer-container-2018" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2018-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2018-score" class="post-score" title="current number of votes">1</div><span id="post-2018-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Open up the Frame details in the Wireshark packet details pane. It shows you:</p><p>[Protocols in frame: eth:arp]</p><p>So, ARP is the highest level protocol, and it's encapsulated in Ethernet.</p><p>Next open up the Ethernet details. It shows you:</p><p>Type: ARP (0x0806)</p><p>So there it is: 0x0806</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jan '11, 05:28</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-2018" class="comments-container"></div><div id="comment-tools-2018" class="comment-tools"></div><div class="clear"></div><div id="comment-2018-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


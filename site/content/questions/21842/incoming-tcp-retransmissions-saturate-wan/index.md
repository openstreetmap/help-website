+++
type = "question"
title = "incoming TCP Retransmissions saturate WAN"
description = '''My internet slowed to a halt, and after checking the obvious things I suspected a DOS attack. Wireshark shows an astronomical number of TCP retransmissions coming from an IP on the internet. What does this mean? Pcap file: http://www.cloudshark.org/captures/64f2c70a977c'''
date = "2013-06-09T07:16:00Z"
lastmod = "2013-06-09T09:26:00Z"
weight = 21842
keywords = [ "dos", "dsl", "retransmissions", "tcp" ]
aliases = [ "/questions/21842" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [incoming TCP Retransmissions saturate WAN](/questions/21842/incoming-tcp-retransmissions-saturate-wan)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21842-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>My internet slowed to a halt, and after checking the obvious things I suspected a DOS attack. Wireshark shows an astronomical number of TCP retransmissions coming from an IP on the internet. What does this mean?<img src="http://i.imgur.com/YuWRDDi.png?1" alt="alt text" /></p><p>Pcap file: <a href="http://www.cloudshark.org/captures/64f2c70a977c">http://www.cloudshark.org/captures/64f2c70a977c</a></p></div><div id="question-tags" class="tags-container tags">dos dsl retransmissions tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Jun '13, 07:16</strong></p><img src="https://secure.gravatar.com/avatar/4e51bce9f8d9994894f84842d70f0ec3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="staticchanger&#39;s gravatar image" /><p>staticchanger<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="staticchanger has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 09 Jun '13, 10:36</p></div></div><div id="comments-container-21842" class="comments-container"><span id="21845"></span><div id="comment-21845" class="comment"><div id="post-21845-score" class="comment-score"></div><div class="comment-text"><p>indeed looks like DOS, especially since the delta times in no way fit retransmission intervals. The IP though refers to google so I guess someone is faking their source IP or totally other possibility -&gt; one of your network devices indeed retransmits this one single packet like hell (which is in my opinion more unlikely).</p><p>Do you see the tcp handshake before the burst? That would exclude s.o. faking the packet</p></div><div id="comment-21845-info" class="comment-info"><span class="comment-age">(09 Jun '13, 08:37)</span> Landi</div></div><span id="21848"></span><div id="comment-21848" class="comment"><div id="post-21848-score" class="comment-score"></div><div class="comment-text"><p>Nope, just this same packet over and over. I requested a static IP change and that fixed the problem. (for me anyway). I'm just curious as to what type of attack it is, and if there's a way to prevent it in the future.</p></div><div id="comment-21848-info" class="comment-info"><span class="comment-age">(09 Jun '13, 09:19)</span> staticchanger</div></div><span id="21850"></span><div id="comment-21850" class="comment"><div id="post-21850-score" class="comment-score"></div><div class="comment-text"><p>Normally your firewall should prevent incoming packets without pre-established tcp sessions. If there really is no handshake before this flood of packets - I'd check the firewall first</p></div><div id="comment-21850-info" class="comment-info"><span class="comment-age">(09 Jun '13, 09:26)</span> Landi</div></div><span id="21851"></span><div id="comment-21851" class="comment"><div id="post-21851-score" class="comment-score"></div><div class="comment-text"><p>If you switched static IP, are you able to share the tracefile on www.cloudshark.org? Or maybe after rewriting the IP header with a tool like tcprewrite or bittwiste?</p></div><div id="comment-21851-info" class="comment-info"><span class="comment-age">(09 Jun '13, 09:28)</span> SYN-bit ♦♦</div></div><span id="21852"></span><div id="comment-21852" class="comment"><div id="post-21852-score" class="comment-score"></div><div class="comment-text"><p>@Landi, well, since the IP destination is whited out, I suspect the trace was taken on the public side of the FW :-)</p></div><div id="comment-21852-info" class="comment-info"><span class="comment-age">(09 Jun '13, 09:30)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-21842" class="comment-tools"></div><div class="clear"></div><div id="comment-21842-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="21849"></span>

<div id="answer-container-21849" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21849-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Well, it means that either someone is sending you the same packet over and over again to fill your WAN link. In the 68ms in your image, I see 35 full size packets. This results in a bandwidth usage of (1000/68)*35*1514*8/1000000 = ~6 Mbit/s of traffic. Is that your WAN bandwidth? Is the absolute sequence number 0 (click on the sequence number in the packet details and look at the hex value in the hex-data)?</p><p>It could also be that one of the packets is bouncing back and forth, either routed or switched. Could you check whether the IP identification (ip.id) and TTL (ip.ttl) are the same in each packet?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Jun '13, 09:26</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Jun '13, 09:54</p></div></div><div id="comments-container-21849" class="comments-container"><span id="21853"></span><div id="comment-21853" class="comment"><div id="post-21853-score" class="comment-score"></div><div class="comment-text"><p>Sake, I almost follow the arithmetic here, but how did you determine the 351514 (bytes?) figure from the above screenshot?</p></div><div id="comment-21853-info" class="comment-info"><span class="comment-age">(09 Jun '13, 09:52)</span> griff</div></div><span id="21854"></span><div id="comment-21854" class="comment"><div id="post-21854-score" class="comment-score"></div><div class="comment-text"><p>Oops, the *'s were interpreted as Italic start and Italic stop. I corrected the calculation :-)</p></div><div id="comment-21854-info" class="comment-info"><span class="comment-age">(09 Jun '13, 09:55)</span> SYN-bit ♦♦</div></div><span id="21855"></span><div id="comment-21855" class="comment"><div id="post-21855-score" class="comment-score"></div><div class="comment-text"><p>Thanks. ;-) Makes much more sense.</p></div><div id="comment-21855-info" class="comment-info"><span class="comment-age">(09 Jun '13, 10:11)</span> griff</div></div><span id="21856"></span><div id="comment-21856" class="comment"><div id="post-21856-score" class="comment-score"></div><div class="comment-text"><p>Here is the capture file if anyone is interested.</p></div><div id="comment-21856-info" class="comment-info"><span class="comment-age">(09 Jun '13, 10:34)</span> staticchanger</div></div><span id="21857"></span><div id="comment-21857" class="comment"><div id="post-21857-score" class="comment-score"></div><div class="comment-text"><p>The ip.id is unique for every packet, so the packet is not bouncing back and forth. As there are only small gaps between the ip.id values it is probably not a google host, but someone else flooding this to you.</p><p>Just curious, if you ping 74.125.130.155 and make a trace, what IP TTL does the response have?</p></div><div id="comment-21857-info" class="comment-info"><span class="comment-age">(09 Jun '13, 10:58)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-21849" class="comment-tools"></div><div class="clear"></div><div id="comment-21849-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


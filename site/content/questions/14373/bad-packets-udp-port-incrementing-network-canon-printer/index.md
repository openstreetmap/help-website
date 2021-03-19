+++
type = "question"
title = "Bad packets - UDP port incrementing - Network Canon printer"
description = '''Hello and thank you for reading my post. Here is my problem:  My PC IP address is x.y.z.w1. On the same LAN, I have a Canon printer which IP address is x.y.z.w2. When I observe the traffic on my PC network interface using Wireshark, I observe lots of packets like these:   No. Time Source Destination...'''
date = "2012-09-19T04:40:00Z"
lastmod = "2012-09-26T02:18:00Z"
weight = 14373
keywords = [ "udp", "printer", "port", "packet", "network" ]
aliases = [ "/questions/14373" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Bad packets - UDP port incrementing - Network Canon printer](/questions/14373/bad-packets-udp-port-incrementing-network-canon-printer)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14373-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14373-score" class="post-score" title="current number of votes">0</div><span id="post-14373-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello and thank you for reading my post.</p><p>Here is my problem:</p><ul><li>My PC IP address is x.y.z.w1.</li><li>On the same LAN, I have a Canon printer which IP address is x.y.z.w2.</li><li>When I observe the traffic on my PC network interface using Wireshark, I observe lots of packets like these:</li></ul><hr /><pre><code>No.  Time         Source    Destination Protocol Length Info
---------------------------------------------------------------------------------------------------------
1    0.000000000  x.y.z.w1  x.y.z.w2    UDP      154    Source port: 57101  Destination port: canon-mfnp
3    4.003164000  x.y.z.w1  x.y.z.w2    UDP      154    Source port: 57102  Destination port: canon-mfnp
5    8.006314000  x.y.z.w1  x.y.z.w2    UDP      154    Source port: 57103  Destination port: canon-mfnp
7   12.009452000  x.y.z.w1  x.y.z.w2    UDP      154    Source port: 57104  Destination port: canon-mfnp
10  16.012623000  x.y.z.w1  x.y.z.w2    UDP      154    Source port: 57105  Destination port: canon-mfnp
---------------------------------------------------------------------------------------------------------</code></pre><p>and it goes on and on like this with the source port incrementing.</p><p>The colouring rules indicate "Bad TCP" packets (in this case UDP packets).</p><p>I also have "good" packets like this one:</p><pre><code>---------------------------------------------------------------------------------------------------------
No.  Time         Source    Destination Protocol Length Info
---------------------------------------------------------------------------------------------------------
4    4.004840000  x.y.z.w2  x.y.z.w1    UDP      74     Source port: canon-mfnp  Destination port: 53724
---------------------------------------------------------------------------------------------------------</code></pre><p>I don't really understand what it means, I just know they are bad packets.</p><p>Nonetheless, I've tried adding a rule (an outbound rule) in my Windows firewall:</p><ul><li>applying to UDP</li><li>for all remote ports</li><li>for domain and private use</li><li>for the IP x.y.z.w2 ("Scope" -&gt; "Local IP address").</li></ul><p>It hasn't changed anything. Can you see what the problem is?</p><p>Thank you for helping and best regards.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-udp" rel="tag" title="see questions tagged &#39;udp&#39;">udp</span> <span class="post-tag tag-link-printer" rel="tag" title="see questions tagged &#39;printer&#39;">printer</span> <span class="post-tag tag-link-port" rel="tag" title="see questions tagged &#39;port&#39;">port</span> <span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span> <span class="post-tag tag-link-network" rel="tag" title="see questions tagged &#39;network&#39;">network</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Sep '12, 04:40</strong></p><img src="https://secure.gravatar.com/avatar/54138bbbbcbc69f4b523d9669de0121b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="L%C3%A9a%20Massiot&#39;s gravatar image" /><p><span>Léa Massiot</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Léa Massiot has no accepted answers">0%</span></p></div></div><div id="comments-container-14373" class="comments-container"></div><div id="comment-tools-14373" class="comment-tools"></div><div class="clear"></div><div id="comment-14373-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="14408"></span>

<div id="answer-container-14408" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14408-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14408-score" class="post-score" title="current number of votes">2</div><span id="post-14408-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The packets are four seconds apart. The source port numbers are changing because the application considers each transmission to be a separate and distinct communication, not part of an ongoing session, so it's selecting a new source port number instead of re-using a recently used port number. No, the PC is not looking for a suitable UDP port. Whatever ephemeral source port the PC chooses for the communication is a suitable port. All that matters is that the destination port is the correct port that the printer is listening to.</p><p>To see what coloring rule a packet matched, expand the Frame section in the Packet Details pane and look for "Coloring Rule Name". Two different coloring rules might use the same colors, so you can't tell what coloring rule was matched simply by looking at the colors under "View &gt; Coloring Rules." Since these are UDP packets, by definition they can't be "Bad TCP."</p><p>You probably don't have a checksum problem. Most modern NICs/PCs implement checksum offloading, meaning that the checksum is calculated by the NIC, not by the operating system. The checksum has not been calculated when Wireshark sees the packet, but the checksum will be correct when the packet is transmitted onto the wire. The clues that checksum offloading is in use are: 1) the bad checksum is 0x0000 and not some random value, and 2) the checksum error only appears on outgoing packets. Checksum errors are usually cosmetic errors that can be disregarded. Many of us disable checksum validation or disable the Checksum Errors coloring rule.</p><p>You don't need to add a firewall rule. The traffic was already getting through, so the firewall was not blocking it.</p><p>I agree with <span>@Jasper</span>. This is normal PC-to-printer traffic initiated by the printer driver.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Sep '12, 13:52</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-14408" class="comments-container"><span id="14417"></span><div id="comment-14417" class="comment"><div id="post-14417-score" class="comment-score"></div><div class="comment-text"><p>Ok then. Thank you very much for these very interesting and detailed information :) Best regards.</p></div><div id="comment-14417-info" class="comment-info"><span class="comment-age">(21 Sep '12, 01:24)</span> <span class="comment-user userinfo">Léa Massiot</span></div></div></div><div id="comment-tools-14408" class="comment-tools"></div><div class="clear"></div><div id="comment-14408-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="14374"></span>

<div id="answer-container-14374" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14374-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14374-score" class="post-score" title="current number of votes">1</div><span id="post-14374-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I guess this is just normal PC-to-Printer traffic, usually initiated by the printer driver, and containing printer status requests, like toner/ink status etc. I don't think these are bad packet, just a little chatty maybe. And how do you know the coloring is "Bad TCP"? Did you compare color schemes, or did you look at the first section in the frame decode? There is a line in there telling you which color rule matched. My guess is that the UDP checksum is incorrect, but that is not a problem. It is usually caused by the way you capture the packets on the affected system, and UDP checksums do not have to be correct anyway (unless we're talking about IPv6).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Sep '12, 05:00</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>19 Sep '12, 05:03</strong> </span></p></div></div><div id="comments-container-14374" class="comments-container"><span id="14392"></span><div id="comment-14392" class="comment"><div id="post-14392-score" class="comment-score"></div><div class="comment-text"><p>Hello and thank you for your answer.</p><blockquote><p><strong>Quote Jasper:</strong> I guess this is just normal PC-to-Printer traffic, usually initiated by the printer driver, and containing printer status requests, like toner/ink status etc.</p></blockquote><p>Really? Why is the "Source port" changing endlessly (by increments of 1)?</p><blockquote><p><strong>Quote Jasper:</strong> And how do you know the coloring is "Bad TCP"?</p></blockquote><p>I compared the color schemes from the "View" -&gt; "Colouring Rules..." Wireshark menu: (sort of) salmon foreground + black blackground. These are the "out of the box" Wireshark settings, I didn't change anything.</p><blockquote><p><strong>Quote Jasper:</strong> My guess is that the UDP checksum is incorrect</p></blockquote><p>Indeed, it looks like there is a checksum problem:</p><pre><code>Frame 1001: 154 bytes on wire (1232 bits), 154 bytes captured (1232 bits) on interface 0
Interface id: 0
WTAP_ENCAP: 1
Arrival Time: Sep 20, 2012 13:48:53.158749000 Pacific Daylight Time
Time shift for this packet: 0.000000000 seconds
Epoch Time: 1348174133.158749000 seconds
Time delta from previous captured frame: 0.850133000 seconds
Time delta from previous displayed frame: 0.850133000 seconds
Time since reference or first frame: 284.812729000 seconds
Frame Number: 1001
Frame Length: 154 bytes (1232 bits)
Capture Length: 154 bytes (1232 bits)
Frame is marked: False
Frame is ignored: False
Protocols in frame: eth:ip:udp:data
Coloring Rule Name: Checksum Errors
Coloring Rule String: cdp.checksum_bad==1 || edp.checksum_bad==1 || ip.checksum_bad==1 || tcp.checksum_bad==1 || udp.checksum_bad==1 || sctp.checksum_bad==1 || mstp.checksum_bad==1
[...]
Internet Protocol Version 4, Src: 192.168.2.240 (192.168.2.240), Dst: 192.168.2.65 (192.168.2.65)
[...]
Header checksum: 0x0000 [incorrect, should be 0x84c2 (may be caused by &quot;IP checksum offload&quot;?)]
[...]

User Datagram Protocol, Src Port: 50683 (50683), Dst Port: canon-mfnp (8610)
[...]
Checksum: 0x870b [validation disabled]
  Good Checksum: False
  Bad Checksum: False
[...]</code></pre><blockquote><p><strong>Quote Jasper:</strong> It is usually caused by the way you capture the packets on the affected system</p></blockquote><p>On the printer or on the PC?</p><p>Do you have any idea why all these packets are being sent all the time with the "Source port" incrementing? I mean, it looks like a lot of useless traffic on the LAN... And also, it looks like it (the PC) is trying to find a suitable UDP port, don't you think?</p><p>Thank you and best regards.</p></div><div id="comment-14392-info" class="comment-info"><span class="comment-age">(20 Sep '12, 06:21)</span> <span class="comment-user userinfo">Léa Massiot</span></div></div><span id="14443"></span><div id="comment-14443" class="comment"><div id="post-14443-score" class="comment-score"></div><div class="comment-text"><p>A few packets every few seconds isn't something to worry about (in the big scheme of things). SRC port incrementing could be a bug or the way the app works. It wants to open multiple connections for some reason.</p></div><div id="comment-14443-info" class="comment-info"><span class="comment-age">(21 Sep '12, 14:18)</span> <span class="comment-user userinfo">hansangb</span></div></div><span id="14448"></span><div id="comment-14448" class="comment"><div id="post-14448-score" class="comment-score"></div><div class="comment-text"><blockquote><p><strong>Quote Léa Massiot:</strong> Do you have any idea why all these packets are being sent all the time with the "Source port" incrementing?</p></blockquote><p>As Jasper said. That's most certainly status monitoring traffic.</p><blockquote><p>I mean, it looks like a lot of useless traffic on the LAN...</p></blockquote><p>Well, there is a lot of 'useless' traffic on a standard network ;-) Those few bytes won't cause any trouble.</p><blockquote><p>And also, it looks like it (the PC) is trying to find a suitable UDP port, don't you think?</p></blockquote><p>it's probably just using a different socket every 4 seconds. That's a bit strange, but not strange enough to worry about.</p><p>BTW: Look at the data part of the packets. What do you see there?</p></div><div id="comment-14448-info" class="comment-info"><span class="comment-age">(22 Sep '12, 11:43)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="14535"></span><div id="comment-14535" class="comment"><div id="post-14535-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Kurt wrote: Look at the data part of the packets. What do you see there?</p></blockquote><p>Not much (to me)... the only humanly readable part is the PC's name.</p><p>Thank you and best regards.</p></div><div id="comment-14535-info" class="comment-info"><span class="comment-age">(26 Sep '12, 02:18)</span> <span class="comment-user userinfo">Léa Massiot</span></div></div></div><div id="comment-tools-14374" class="comment-tools"></div><div class="clear"></div><div id="comment-14374-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</hr>

</div>

</div>


+++
type = "question"
title = "Retransmissions"
description = '''I get hundreds of these when i copy from my windows 2003 server at one site to a windows 2008 r2 server at another. Any idea on what&#x27;s going on or how to troubleshoot it? 10193 0.000000000 192.168.20.30 192.168.183.10 TCP 1514 [TCP Fast Retransmission] [TCP segment of a reassembled PDU]  10203 0.003...'''
date = "2013-01-16T19:12:00Z"
lastmod = "2013-01-17T03:55:00Z"
weight = 17730
keywords = [ "retransmissions" ]
aliases = [ "/questions/17730" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Retransmissions](/questions/17730/retransmissions)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17730-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I get hundreds of these when i copy from my windows 2003 server at one site to a windows 2008 r2 server at another. Any idea on what's going on or how to troubleshoot it?</p><pre><code>10193   0.000000000 192.168.20.30   192.168.183.10  TCP 1514    [TCP Fast Retransmission] [TCP segment of a reassembled PDU]

10203   0.003003000 192.168.20.30   192.168.183.10  TCP 1514    [TCP Retransmission] [TCP segment of a reassembled PDU]</code></pre><p>Its also at <a href="https://www.cloudshark.org/captures/a198e1dad32c">https://www.cloudshark.org/captures/a198e1dad32c</a></p></div><div id="question-tags" class="tags-container tags">retransmissions</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Jan '13, 19:12</strong></p><img src="https://secure.gravatar.com/avatar/29c58be3d3185018b724cf9f0aebf8bf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Willmeister&#39;s gravatar image" /><p>Willmeister<br />
<span class="score" title="6 reputation points">6</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Willmeister has no accepted answers">0%</span></p></div></div><div id="comments-container-17730" class="comments-container"><span id="17734"></span><div id="comment-17734" class="comment"><div id="post-17734-score" class="comment-score"></div><div class="comment-text"><p>You say you get hundreds of retransmissions, but when I load your capture file, I only see 11 retransmissions, and they do not include the two packets that you show above, numbers 10193 and 10203. What version of Wireshark are you using?</p></div><div id="comment-17734-info" class="comment-info"><span class="comment-age">(16 Jan '13, 22:02)</span> Jim Aragon</div></div><span id="17738"></span><div id="comment-17738" class="comment"><div id="post-17738-score" class="comment-score"></div><div class="comment-text"><p>Oh i should have explained that. That capture above (packet numbers 10203 10193) was the 10 second capture i had originally. It was 50 megs. I couldn't upload it. I had to quickly grab a smaller one to upload. Since the file copy i was doing originally stopped i had to do the whole process over...i just didn't update the above.</p></div><div id="comment-17738-info" class="comment-info"><span class="comment-age">(17 Jan '13, 03:48)</span> Willmeister</div></div></div><div id="comment-tools-17730" class="comment-tools"></div><div class="clear"></div><div id="comment-17730-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="17735"></span>

<div id="answer-container-17735" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17735-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Assuming you refer to the "[TCP segment of a reassembled PDU]" messages when saying "I get hundreds of these", these are perfectly normal messages. Wireshark re-assembles higher layer protocol PDU's. This means multiple packets that belong together will be shown as one appliaction message. Have a look at frame 1849, it says:</p><pre><code>24 Reassembled TCP Segments (32831 bytes): #1815(304), #1818(1460), #1819(1460), #1820(1460), #1822(1460), #1823(1460), #1825(1460), #1826(1460), #1827(1460), #1829(1460), #1830(1460), #1832(1460), #1833(1460), #1835(1460), #1836(1460), etc.</code></pre><p>This means the SMB PDU "Read AndX Response, FID: 0x4017, 32768 bytes" was split over 24 packets (which is logical as the payload part of that PDU alone is 32768).</p><p>More info on <a href="http://wiki.wireshark.org/TCP_Reassembly">http://wiki.wireshark.org/TCP_Reassembly</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jan '13, 00:34</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-17735" class="comments-container"><span id="17742"></span><div id="comment-17742" class="comment"><div id="post-17742-score" class="comment-score"></div><div class="comment-text"><p>It's not the reassembly's i'm concerned with. It's the fact they are Retransmissions. Unfortunatley i'm limited to a 10meg upload on that site so you don't see the problem as I do.</p><p>When i copy between the 192.168.183.10 and 192.168.20.30 server it may take about an hour to copy several hundred MB. When i copy the same files from 192.168.183.10 to 192.168.183.11 it's seconds....and no Retransmissions. Trying to track down what may be happening on 192.168.20.0/24's network. Or server NIC. But I get the same issue with 192.168.20.10 as well.</p></div><div id="comment-17742-info" class="comment-info"><span class="comment-age">(17 Jan '13, 04:02)</span> Willmeister</div></div></div><div id="comment-tools-17735" class="comment-tools"></div><div class="clear"></div><div id="comment-17735-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="17739"></span>

<div id="answer-container-17739" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17739-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Assuming that you refer to "[TCP Retransmission]" that usually indicates trouble - or at least potential trouble.</p><p>Most file copy programs rely on TCP to facilitate the data transfer. The receiver acknowledges received data. If a packet is lost for any reason it is retransmitted by the sender.</p><p>Wireshark usually does a good job in detecting the retransmission and marks those packets.</p><p>An occasional retransmission is not a big matter. However, an excessive number of retransmissions (like "hundreds") will significantly increase the time for the file transfer and annoy the user.</p><p>Packets get lost for any number of reasons. Here are a few likely candidates for large number of retransmissions:</p><ul><li>Full Duplex / Half Duplex mismatch (check the configuration of the network card and switch interfaces)</li><li>The server transmits data with a high speed (say 1 GBit) and the receiver is connected with a lower speed (say 100 MBit). Drops occur if the receiver is signalling a large TCP window size, found in the TCP header.</li><li>One of your routers is configured with a quality of service rule that enforces a certain the bandwidth</li><li>A broken cable offers very poor signal quality</li><li>A wireless network is busy or suffers from interference</li></ul><p>The second reason is often observed when Windows Vista / Win 7 pulls data from a Server 2008.</p><p>Good hunting!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jan '13, 03:55</strong></p><img src="https://secure.gravatar.com/avatar/3b60e92020a427bb24332efc0b560943?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="packethunter&#39;s gravatar image" /><p>packethunter<br />
<span class="score" title="2137 reputation points"><span>2.1k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="packethunter has 8 accepted answers">8%</span></p></div></div><div id="comments-container-17739" class="comments-container"><span id="17743"></span><div id="comment-17743" class="comment"><div id="post-17743-score" class="comment-score"></div><div class="comment-text"><p>I'm leaning here: The server transmits data with a high speed (say 1 GBit) and the receiver is connected with a lower speed (say 100 MBit). Drops occur if the receiver is signalling a large TCP window size, found in the TCP header.</p><p>I'm going to have them change one server and lock it down to 100 full as my next step.</p><p>Thank you.</p></div><div id="comment-17743-info" class="comment-info"><span class="comment-age">(17 Jan '13, 04:06)</span> Willmeister</div></div><span id="17744"></span><div id="comment-17744" class="comment"><div id="post-17744-score" class="comment-score">2</div><div class="comment-text"><p><strong>Please be careful with changes to your life network.</strong></p><p>The Gigabit link allows the server to serve multiple clients simultaneously. Forcing the system to 100 MBit could hurt you more than you gain.</p><p>For your "hundreds" of retransmissions, an FDX / HDX mismatch somewhere between transmitter and receiver is a likely reason.</p><p>Another mundane explanation is, that another connection is using bandwidth at the choke point during the times of drops.</p><p>Please include the following steps in your analysis process:</p><ul><li>Check error counters of all switch / router ports involved</li><li>Check drop counters of all switch / router ports involved</li></ul></div><div id="comment-17744-info" class="comment-info"><span class="comment-age">(17 Jan '13, 05:08)</span> packethunter</div></div><span id="31609"></span><div id="comment-31609" class="comment"><div id="post-31609-score" class="comment-score"></div><div class="comment-text"><p>I don't understand the second reason. What triggers the retransmit? How can I know if this reason is applicable to my capture?</p></div><div id="comment-31609-info" class="comment-info"><span class="comment-age">(07 Apr '14, 20:06)</span> xkgt</div></div></div><div id="comment-tools-17739" class="comment-tools"></div><div class="clear"></div><div id="comment-17739-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


+++
type = "question"
title = "Dissect traffic between Lutron RadioRa2 and Alarm.com"
description = '''I am looking at the Wireshark trace from a Lutron RadioRa2 repeater communicating with Alarm.com (209.222.135.33) over UDP port 1130. If I follow UDP stream in wireshark, I am getting gibberish.  Is there a way to decrypt and see what information is being sent to Alarm.com? Thanks'''
date = "2013-03-01T09:54:00Z"
lastmod = "2013-03-01T10:43:00Z"
weight = 19042
keywords = [ "radiora2", "casp", "lutron" ]
aliases = [ "/questions/19042" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Dissect traffic between Lutron RadioRa2 and Alarm.com](/questions/19042/dissect-traffic-between-lutron-radiora2-and-alarmcom)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19042-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am looking at the Wireshark trace from a Lutron RadioRa2 repeater communicating with Alarm.com (209.222.135.33) over UDP port 1130. If I follow UDP stream in wireshark, I am getting gibberish.</p><p>Is there a way to decrypt and see what information is being sent to Alarm.com?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">radiora2 casp lutron</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Mar '13, 09:54</strong></p><img src="https://secure.gravatar.com/avatar/bcfdf26904f3a8a9fb69c7ca0dc5e7b1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="net_tech&#39;s gravatar image" /><p>net_tech<br />
<span class="score" title="116 reputation points">116</span><span title="30 badges"><span class="badge1">●</span><span class="badgecount">30</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="net_tech has 2 accepted answers">13%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 01 Mar '13, 22:25</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-19042" class="comments-container"></div><div id="comment-tools-19042" class="comment-tools"></div><div class="clear"></div><div id="comment-19042-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="19044"></span>

<div id="answer-container-19044" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19044-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>I don't know what <strong>CASP</strong> traffic is (please explain), but on the webpage of alarm.com they claim to be able to do this with their products through a mobile app.</p><ul><li>Lock/Unlock doors</li><li>Turn lights on/off</li><li>Adjust Temperature</li></ul><p>I really hope they <strong>encrypt</strong> that traffic to prevent an eavesdropper from intercepting the door commands, modifying it and unlocking the door instead of locking it.</p><p>So I strongly assume (hope) they use encrypted communication and that's the reason why you 'get gibberish'.</p><p>If that is true, I don't see a realistic way to decrypt the traffic, unless you hack into their systems to steal the crypto keys ;-))</p><p>If the traffic is not encrypted, they are maybe using a binary protocol. Unless you know the structure of that protocol, there is again no realistic way to decipher the communication.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Mar '13, 10:08</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 01 Mar '13, 10:09</p></div></div><div id="comments-container-19044" class="comments-container"><span id="19047"></span><div id="comment-19047" class="comment"><div id="post-19047-score" class="comment-score"></div><div class="comment-text"><p>this is what I found about CASP <a href="http://user.informatik.uni-goettingen.de/~casp/draft-schulzrinne-nsis-casp-01.pdf">http://user.informatik.uni-goettingen.de/~casp/draft-schulzrinne-nsis-casp-01.pdf</a></p><p>Wireshark identifies Port 1130 as CASP traffic, so my guess it is CASP</p></div><div id="comment-19047-info" class="comment-info"><span class="comment-age">(01 Mar '13, 10:24)</span> net_tech</div></div><span id="19050"></span><div id="comment-19050" class="comment"><div id="post-19050-score" class="comment-score"></div><div class="comment-text"><p>Hm.. can you please post a few sample packets (pcap format!) somewhere (google docs, one-click hoster, cloudshark.org)?</p></div><div id="comment-19050-info" class="comment-info"><span class="comment-age">(01 Mar '13, 10:30)</span> Kurt Knochner ♦</div></div><span id="19051"></span><div id="comment-19051" class="comment"><div id="post-19051-score" class="comment-score"></div><div class="comment-text"><p>sure</p><p><a href="http://www.cloudshark.org/captures/28719c863324">http://www.cloudshark.org/captures/28719c863324</a></p></div><div id="comment-19051-info" class="comment-info"><span class="comment-age">(01 Mar '13, 10:36)</span> net_tech</div></div><span id="19057"></span><div id="comment-19057" class="comment"><div id="post-19057-score" class="comment-score">1</div><div class="comment-text"><p>If you look at the data, you will see, that there is a structure, based on the length of the packets.</p><pre><code>All packets start with 0x7d.

Packets with 60 Bytes seem to count up in the second octet: 0d, 0e, next? Then there is a repeating pattern 00:00:11:22:33:44:55:6a. Looks like a status message or some kind of keep-alive.

#1 7d 0d 00 00 11 22 33 44 55 6a 79 75 00 fc 61 31

#5 7d 0e 00 00 11 22 33 44 55 6a 7c 83 75 00 fc 64 3d

Packets with 77 Bytes start with 7d202028, then &#39;gibberish&#39;

#2 7d 20 20 28 a0 3c a7 62 5a 03 1a f8 db 5f c0 0d 25 4c 8b 0d a5 5f 5e 38 1b fe b5 4c 90 41 54 b6 49 63 f6

#6 7d 20 20 28 da 93 ee ff 04 00 0b 00 22 46 ad 6e 61 b0 29 8e 05 12 da c3 c1 43 a1 69 f0 66 81 3f 64 db f0

Packets with 93 Bytes start with 7d3020 then &#39;gibberish&#39;

#3 7d 30 20 50 85 98 09 0e 5a 99 38 86 4b c3 9d df d0 0e 39 a5 23 e7 3d e9 ec 11 8c 78 d6 8b 35 c4 d6 f2 ec cb 0e 0f 74 fe 13 fb b4 6f 79 b8 31 81 96 a1 a0

#7 7d 30 20 1a d5 61 e1 88 97 10 5d 00 d7 63 29 7f d5 aa db e3 36 db d5 b8 39 b7 64 95 9d ae 17 1b 67 84 1e 6b 4f 6f 5a 9d 5a 8c 30 5d 06 f4 fd ba de 40 3b

#8 7d 30 20 f7 cd 61 03 1a 76 fe d6 02 95 3b 42 60 b3 13 99 e2 63 f7 b6 00 dd 21 12 01 18 bc c3 45 7f 54 25 87 0f 73 20 1c 24 09 0f 84 1a 31 c8 dd 08 9a a9

I guess those &quot;prefixes&quot; (7d2020 and 7d3020) are different message types and the rest may or may not contain encrypted data.
</code></pre></div><div id="comment-19057-info" class="comment-info"><span class="comment-age">(01 Mar '13, 11:20)</span> Kurt Knochner ♦</div></div><span id="19066"></span><div id="comment-19066" class="comment"><div id="post-19066-score" class="comment-score"></div><div class="comment-text"><p>UPDATE: As @SYN-bit figured out, 0x7d is probably a protocol identifier, the second octet is the data length and the third octet probably flags an/or message type!?!</p></div><div id="comment-19066-info" class="comment-info"><span class="comment-age">(01 Mar '13, 12:56)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-19044" class="comment-tools"></div><div class="clear"></div><div id="comment-19044-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="19052"></span>

<div id="answer-container-19052" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19052-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>From /etc/services:</p><pre><code>[email protected]:~/Wireshark/trunk$ grep casp /etc/services 
casp            1130/tcp    # CAC App Service Protocol
casp            1130/udp    # CAC App Service Protocol
caspssl         1131/tcp    # CAC App Service Protocol Encripted
caspssl         1131/udp    # CAC App Service Protocol Encripted
[email protected]:~/Wireshark/trunk$</code></pre><p>So traffic on port 1130 should probably not be encrypted at the transport layer. The document you refer too has one paragraph on security:</p><pre><code>The session ownership problem described in [8] makes an efficient security protection
difficult. For this version of CASP confidentiality protection of the session identifier
can be provided by both IPsec and TLS (as provided by most cipher-suites for TLS and
IPSec ESP without NULL encryption) to Security protection for the session ownership
first version of the protocol may rely prevent eavesdroppers to learn the 128-bit
randomly generated session identifier.</code></pre><p>So, it might be IPsec. Or it might be encryption at the application layer.</p><p>In any case, wireshark currently has no casp dissector AFAICT. So the first steps would be to create a casp dissector (based on the protocol specification).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Mar '13, 10:43</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-19052" class="comments-container"><span id="19053"></span><div id="comment-19053" class="comment"><div id="post-19053-score" class="comment-score"></div><div class="comment-text"><p>Well, looking at the CASP specfication and the packet data, I don't hink this traffic is CASP traffic. Look at the fourth byte in each frame, it is not always 1, 2 or 3... which it should be according to page 6 in the specification.</p></div><div id="comment-19053-info" class="comment-info"><span class="comment-age">(01 Mar '13, 10:50)</span> SYN-bit ♦♦</div></div><span id="19055"></span><div id="comment-19055" class="comment"><div id="post-19055-score" class="comment-score"></div><div class="comment-text"><p>Looking a bit deeper into the packets, each packet seems to have the following structure:</p><pre><code>octet 1 : 7d =&gt; Identifier?
octed 2 : xx =&gt; Length of data
octed 3 : xx =&gt; Flags??
remaining octets : &lt;data&gt;</code></pre></div><div id="comment-19055-info" class="comment-info"><span class="comment-age">(01 Mar '13, 11:06)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-19052" class="comment-tools"></div><div class="clear"></div><div id="comment-19052-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


+++
type = "question"
title = "protocol text file to pcap"
description = '''Hi friends! I need to convert text to pcap, this is an example. Can you help me? Thanks! Julian ================================================================================  [No. ] 1 [TimeStamp ] 2012-06-13 11:49:03 [Msg Name ] &amp;lt;BYE [Module No ] 1407 [Remote Address] 172.26.2.65:9163 [Ticks ]...'''
date = "2012-06-13T13:29:00Z"
lastmod = "2012-06-15T01:32:00Z"
weight = 11878
keywords = [ "text2pcap", "text", "convert" ]
aliases = [ "/questions/11878" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [protocol text file to pcap](/questions/11878/protocol-text-file-to-pcap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11878-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p><strong>Hi friends! I need to convert text to pcap, this is an example. Can you help me? Thanks! Julian</strong></p><pre><code>================================================================================

[No.           ] 1
[TimeStamp     ] 2012-06-13 11:49:03
[Msg Name      ] &lt;BYE
[Module No     ] 1407
[Remote Address] 172.26.2.65:9163
[Ticks         ] 1561178745
[Hex Msg       ] 42 59 45 20 73 69 70 3A 31 37 32 2E 32 36 2E 32 2E 36 35 3A ...

BYE sip:172.26.2.65:9163;yop=00.00.B69D8639.0000.436A SIP/2.0
Via: SIP/2.0/UDP 172.26.1.164:5072;branch=z9hG4bK84ebbd18599de4fc4d25e1cd9;X-DispCookie=1000;X-DptMsg=1407
Route: &lt;sip:172.26.2.65:9163;transport=udp;lr&gt;
Call-ID: [email protected]
From: &quot;33545314179&quot;&lt;sip:[email protected];transport=udp;user=phone&gt;;tag=5e5fb6dc-CC-1000
To: &quot;5114370684&quot;&lt;sip:[email protected];transport=udp;user=phone&gt;;tag=sbc0503dg986A83Uc6ee_h0
CSeq: 2 BYE
Max-Forwards: 70
Reason: Q.850;cause=16;text=&quot;Normal call clearing&quot;
Content-Length: 0</code></pre><p><strong>also I can obtain this other format</strong></p><pre><code>==========================================================================================
[No.           ] 1
[TimeStamp     ] 2012-06-13 11:49:03
[Msg Name      ] &lt;BYE
[Module No     ] 1407
[Remote Address] 172.26.2.65:9163
[Ticks         ] 1561178745
[Hex Msg       ] 42 59 45 20 73 69 70 3A 31 37 32 2E 32 36 2E 32 2E 36 35 3A 39 31 36 33 3B 79 6F 70 3D 30 30 2E 30 30 2E 42 36 39 44 38 36 33 39 2E 30 30 30 30 2E 34 33 36 41 20 53 49 50 2F 32 2E 30 0A 56 69 61 3A 20 53 49 50 2F 32 2E 30 2F 55 44 50 20 31 37 32 2E 32 36 2E 31 2E 31 36 34 3A 35 30 37 32 3B 62 72 61 6E 63 68 3D 7A 39 68 47 34 62 4B 38 34 65 62 62 64 31 38 35 39 39 64 65 34 66 63 34 64 32 35 65 31 63 64 39 3B 58 2D 44 69 73 70 43 6F 6F 6B 69 65 3D 31 30 30 30 3B 58 2D 44 70 74 4D 73 67 3D 31 34 30 37 0A 52 6F 75 74 65 3A 20 3C 73 69 70 3A 31 37 32 2E 32 36 2E 32 2E 36 35 3A 39 31 36 33 3B 74 72 61 6E 73 70 6F 72 74 3D 75 64 70 3B 6C 72 3E 0A 43 61 6C 6C 2D 49 44 3A 20 64 39 38 30 31 62 61 34 65 33 62 37 35 63 31 62 37 39 36 39 61 33 34 31 66 35 65 31 30 32 30 66 40 31 30 2E 31 38 2E 35 2E 36 34 0A 46 72 6F 6D 3A 20 22 33 33 35 34 35 33 31 34 31 37 39 22 3C 73 69 70 3A 2B 33 33 35 34 35 33 31 34 31 37 39 40 31 37 32 2E 32 36 2E 31 2E 31 36 34 3B 74 72 61 6E 73 70 6F 72 74 3D 75 64 70 3B 75 73 65 72 3D 70 68 6F 6E 65 3E 3B 74 61 67 3D 35 65 35 66 62 36 64 63 2D 43 43 2D 31 30 30 30 0A 54 6F 3A 20 22 35 31 31 34 33 37 30 36 38 34 22 3C 73 69 70 3A 2B 35 31 31 34 33 37 30 36 38 34 40 31 37 32 2E 32 36 2E 32 2E 36 35 3B 74 72 61 6E 73 70 6F 72 74 3D 75 64 70 3B 75 73 65 72 3D 70 68 6F 6E 65 3E 3B 74 61 67 3D 73 62 63 30 35 30 33 64 67 39 38 36 41 38 33 55 63 36 65 65 5F 68 30 0A 43 53 65 71 3A 20 32 20 42 59 45 0A 4D 61 78 2D 46 6F 72 77 61 72 64 73 3A 20 37 30 0A 52 65 61 73 6F 6E 3A 20 51 2E 38 35 30 3B 63 61 75 73 65 3D 31 36 3B 74 65 78 74 3D 22 4E 6F 72 6D 61 6C 20 63 61 6C 6C 20 63 6C 65 61 72 69 6E 67 22 0A 43 6F 6E 74 65 6E 74 2D 4C 65 6E 67 74 68 3A 20 30 0A 0A</code></pre></div><div id="question-tags" class="tags-container tags">text2pcap text convert</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Jun '12, 13:29</strong></p><img src="https://secure.gravatar.com/avatar/25c996f9c81d5bdf32a92365b210870e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chochi&#39;s gravatar image" /><p>chochi<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chochi has no accepted answers">0%</span></p></div></div><div id="comments-container-11878" class="comments-container"></div><div id="comment-tools-11878" class="comment-tools"></div><div class="clear"></div><div id="comment-11878-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="11887"></span>

<div id="answer-container-11887" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11887-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>You could write a script that takes the second output and format that to something readable by text2pcap and then use text2pap to convert that to a libpcap format file.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jun '12, 22:12</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-11887" class="comments-container"><span id="11915"></span><div id="comment-11915" class="comment"><div id="post-11915-score" class="comment-score"></div><div class="comment-text"><p>The idea is to know if somebody known how to do that :) I don't know how to do what you said Anders. Thanks for your answer anyway.</p></div><div id="comment-11915-info" class="comment-info"><span class="comment-age">(14 Jun '12, 21:34)</span> chochi</div></div></div><div id="comment-tools-11887" class="comment-tools"></div><div class="clear"></div><div id="comment-11887-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="11921"></span>

<div id="answer-container-11921" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11921-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>just a few comments/thoughts:</p><ol><li>Why do you rely on a log file? Why don't you sniff the SIP traffic in the first place, if you need a pcap file?</li><li>What do you expect to get if you convert the SIP log to pcap? You won't see more in wireshark than in the log.</li><li>As it's SIP, you might be interested in RTP traffic as well. I doubt, that RTP traffic will be logged entirely, so that would be missing in the pcap file.</li></ol><p>It would be possible to write a converter script to format your log into "something" that text2pcap can read. However, one would have to insert a lot of fake data (like ethernet frame, ip frame, tcp ports) that are not in your log.</p><blockquote><p>The idea is to know if somebody known how to do that</p></blockquote><ul><li>Try to understand the text2pcap format first. Look at the source code</li><li>Use any programming language you know</li><li>Read your log and build the data structure that's needed for text2pcap</li><li>Write the output</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jun '12, 01:32</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-11921" class="comments-container"><span id="11934"></span><div id="comment-11934" class="comment"><div id="post-11934-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt! I used Wireshark almost all days with SIP traffic, I don't really need the RTP traffic, only signalling. I work in a ISP provider and sometimes we have to analyse only errors on the network to know how the ASR goes. Unfortunately my company have new equipment (Huawei) and when you capture in a remote servers only capture SIP signalling, they export in proprietary format or in this two text options. They made my work harder because to find a complete call flow in all the SIP traces is a pain in the ass... Thanks anyway for your support!</p></div><div id="comment-11934-info" class="comment-info"><span class="comment-age">(15 Jun '12, 06:44)</span> chochi</div></div><span id="11940"></span><div id="comment-11940" class="comment"><div id="post-11940-score" class="comment-score">1</div><div class="comment-text"><blockquote><p>they export in proprietary format or in this two text options...</p></blockquote><p>I see. What is that proprietary format used for? Do they offer a protocol analyzer for it?</p><p>Please check Homer. It looks like it can talk to Huawei equipment and the capture agent on it. This is just a wild guess, as I don't know Homer personally!</p><blockquote><p><code>http://www.sipcapture.org/</code></p></blockquote></div><div id="comment-11940-info" class="comment-info"><span class="comment-age">(15 Jun '12, 07:17)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-11921" class="comment-tools"></div><div class="clear"></div><div id="comment-11921-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


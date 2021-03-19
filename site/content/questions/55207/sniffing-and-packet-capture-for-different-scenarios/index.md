+++
type = "question"
title = "Sniffing and packet capture for different scenarios"
description = '''Hello, For the image attached which shows a set up of network, I have the following questions. 1.In the scenario A, is there any device required after the ethernet converter for wireshark to capture the  packets?  2. Does it sniffs and capture the packets in this scenario? Thank you. '''
date = "2016-08-30T09:05:00Z"
lastmod = "2016-08-31T01:07:00Z"
weight = 55207
keywords = [ "packet-capture" ]
aliases = [ "/questions/55207" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Sniffing and packet capture for different scenarios](/questions/55207/sniffing-and-packet-capture-for-different-scenarios)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55207-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, For the image attached which shows a set up of network, I have the following questions. 1.In the scenario A, is there any device required after the ethernet converter for wireshark to capture the packets? 2. Does it sniffs and capture the packets in this scenario?</p><p>Thank you.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/example3_YZav1Xd.PNG" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">packet-capture</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Aug '16, 09:05</strong></p><img src="https://secure.gravatar.com/avatar/1d8583ebaa635698618e362af9eeb4d7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stadkama&#39;s gravatar image" /><p>stadkama<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stadkama has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 30 Aug '16, 09:07</p></div></div><div id="comments-container-55207" class="comments-container"></div><div id="comment-tools-55207" class="comment-tools"></div><div class="clear"></div><div id="comment-55207-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="55208"></span>

<div id="answer-container-55208" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55208-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you are sniffing on two cables you would need (2) capture NICs on the PC, or (2) separate capture PCs, or you would need a TAP that aggregates the two cables into one capture port that you then use the PC to capture off of. For the first two options, you would use mergecap to get both conversations into one PCAP file.</p><p>I am not familiar with what the converter is accomplishing, so if that aggregates somehow then that may also be a solution. But from the diagram I am assuming that there are two cables leaving the converter.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Aug '16, 09:25</strong></p><img src="https://secure.gravatar.com/avatar/bfccba6dc51febee5ca1641be7df63ba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BruteForce&#39;s gravatar image" /><p>BruteForce<br />
<span class="score" title="120 reputation points">120</span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BruteForce has one accepted answer">9%</span></p></div></div><div id="comments-container-55208" class="comments-container"><span id="55225"></span><div id="comment-55225" class="comment"><div id="post-55225-score" class="comment-score"></div><div class="comment-text"><p>2 wire ethernet represents simultaneous transmit and receive (i.e., full-duplex) operations on a single-pair cable.</p><p>100 base Tx cable after the converter towards PC represents cat5e cable where one pair for transmit and one for receive to achieve the same data rate. Converter is just for physical layer conversion. Please let me know is there any TAP required after the converter.</p></div><div id="comment-55225-info" class="comment-info"><span class="comment-age">(31 Aug '16, 01:55)</span> stadkama</div></div></div><div id="comment-tools-55208" class="comment-tools"></div><div class="clear"></div><div id="comment-55208-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="55223"></span>

<div id="answer-container-55223" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55223-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Your description is unclear and even confusing: "two-wire" usually means "single-pair", which would mean that both directions of the connection (μC A &lt;-&gt; μC B) use the same pair, while the description in the bubble says "2 cable ethernet" which could mean a separate cable (possibly with several pairs) per direction.</p><p>But as a 2-wire "Ethernet" is a common solution where both directions use the same pair of wires, I'll deal with that part: no, the way you have drawn it it will not work. Depending on the way how the 2-wire "Ethernet" solution is implemented, the 2-wire connection may carry:</p><ul><li><p>two modulated signals in different bands (if you have to set a role on each of the converters)</p></li><li><p>a superposition of both directions' baseband (not modulated) signals, if both ends use a "hybrid coil" to separate what they transmit themselves from what they receive on the pair, to get only what the other party transmits.</p></li><li><p>some kind of half-duplex protocol</p></li></ul><p>In any of the first two cases, you have to use the following architecture (==== means a pair of wires) for sniffing:</p><pre><code>                -------------                __    -------------
               |          Tx |==============|  |==| Rx          |
μC A ==========| Converter A |   __          ||   | Converter B |========== μC B
               |          Rx |==|  |=========||===| Tx          |
                -------------    ||          ||    -------------
                               --||----------||--
                              |  Rx          Rx  |
                              | eth0        eth1 |
                              |    sniffing PC   |
                               ------------------</code></pre><p>I.e. you have to create a section of standard 4-wire Ethernet between the two μcontrollers using two 2W/4W converters connected back-to-back, and use a tap on it to feed two ports on the sniffing PC, each sniffing its own direction. Instead, you can also use a switch capable of monitoring, connect it between the two converters, and monitor Tx direction of each of the ports separately (i.e. copy it to another sniffing port of your PC). If you don't care much about timing and the aggregate traffic between the two μcontrollers is lower than the bandwidth on the sniffing port (or if you can use a 1 Gbit/s port to connect the PC while the 2wire Ethernet is just 100 Mbit/s in each direction), you can monitor Tx and Rx of just one of the ports on a single sniffing port of the PC, and you'll be fine as well.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Aug '16, 01:07</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 31 Aug '16, 01:11</p></div></div><div id="comments-container-55223" class="comments-container"><span id="55226"></span><div id="comment-55226" class="comment"><div id="post-55226-score" class="comment-score"></div><div class="comment-text"><p>The representation in the figure is described below: 2 wire ethernet represents simultaneous transmit and receive (i.e., full-duplex) operations on a single-pair cable.</p><p>100 base Tx cable after the converter towards PC represents cat5e cable where one pair for transmit and one for receive to achieve the same data rate. Converter is just for physical layer conversion.</p></div><div id="comment-55226-info" class="comment-info"><span class="comment-age">(31 Aug '16, 01:58)</span> stadkama</div></div><span id="55227"></span><div id="comment-55227" class="comment"><div id="post-55227-score" class="comment-score"></div><div class="comment-text"><p>In that case, all what I wrote above is true. The Tx and Rx on the 2-wire are arranged in one of the first two ways and so you need to insert two back to back connected converters into the 2-wire line to be able to sniff both directions properly. If frequency separation is used, a single converter connected in parallel can only read one direction; if hybrids are used, a mix of both directions is present on the wire so if both μcontrollers transmit at the same time, the converter connected in parallel cannot translate the superposition of the two signals into two packets which do not overlap in time.</p></div><div id="comment-55227-info" class="comment-info"><span class="comment-age">(31 Aug '16, 02:13)</span> sindy</div></div></div><div id="comment-tools-55223" class="comment-tools"></div><div class="clear"></div><div id="comment-55223-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


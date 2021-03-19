+++
type = "question"
title = "Developing 10G supportable packet analyser"
description = '''Hi,  I am developing 10G packet capturer and analyser.I searched many in google and i can&#x27;t able to find the solution. what are all the steps i needed to achieve this. I have a 10G napatech interface card.using that i capture 600GB packets in 10 mins.The packet mainly consist of GTP packets.When i a...'''
date = "2016-03-02T21:40:00Z"
lastmod = "2016-03-03T02:50:00Z"
weight = 50694
keywords = [ "10gbe", "packet-capture", "pcap", "tshark", "wireshark" ]
aliases = [ "/questions/50694" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Developing 10G supportable packet analyser](/questions/50694/developing-10g-supportable-packet-analyser)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50694-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I am developing 10G packet capturer and analyser.I searched many in google and i can't able to find the solution. what are all the steps i needed to achieve this. I have a 10G napatech interface card.using that i capture 600GB packets in 10 mins.The packet mainly consist of GTP packets.When i am extracting it was changed to thrice the times of memory. My question is how can i manage such kind of big memory and how can i do parse it.whereas wireshark or tshark doesn't support these kind of large files.Please answer me if anyone was developed or anyone knows the idea about this.I was so much confused and i am new to this.</p><p>Thank you,</p></div><div id="question-tags" class="tags-container tags">10gbe packet-capture pcap tshark wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Mar '16, 21:40</strong></p><img src="https://secure.gravatar.com/avatar/8a669421eea30a71c4677fff8b0c5734?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rathnaTech&#39;s gravatar image" /><p>rathnaTech<br />
<span class="score" title="31 reputation points">31</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rathnaTech has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 07 Mar '16, 02:12</p></div></div><div id="comments-container-50694" class="comments-container"></div><div id="comment-tools-50694" class="comment-tools"></div><div class="clear"></div><div id="comment-50694-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50701"></span>

<div id="answer-container-50701" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50701-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>As both Wireshark and tshark accumulate context information about the packets, it is inevitable that you run out of memory at some size of the file. The more memory, the bigger file can be handled, but there is always a limit.</p><p>So the simplest way to address this would be to use a circular file buffer while capturing using dumpcap or your tailor-made capturing application (which do not build any context, which means that only capture filters can be used) and limit the size of the individual files to one which Wireshark/tshark can handle on your machine. Then, you would process these individual files, and maybe filter the interesting flows from them into yet smaller files which you would then merge together so that you could see the whole flow in a single file.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Mar '16, 02:50</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 03 Mar '16, 02:51</p></div></div><div id="comments-container-50701" class="comments-container"><span id="50738"></span><div id="comment-50738" class="comment"><div id="post-50738-score" class="comment-score"></div><div class="comment-text"><p>Thankyou sindy , does tshark captures and extracts without any loss of packets and data??</p></div><div id="comment-50738-info" class="comment-info"><span class="comment-age">(07 Mar '16, 02:11)</span> rathnaTech</div></div><span id="50739"></span><div id="comment-50739" class="comment"><div id="post-50739-score" class="comment-score"></div><div class="comment-text"><p>tshark is pretty much Wireshark but with a command line interface. It uses the same dissection engine and suffers from the same memory limitations.</p><p>In addition to the memory usage, tshark and Wireshark represent a heavier load on the capture system because of the dissection they do on the packets for reassembly etc. For high speed (&gt; 500Mps in my experience) commodity PC hardware (NIC, CPU, disk) isn't enough.</p><p>If you do manage to capture without drops into multiple files (e.g. using dumpcap or maybe the Napatech software) then have a look at <a href="http://www.riverbed.com/products/steelcentral/network-performance-management/steelcentral-packet-analyzer.html">Packet Analyzer</a> from Riverbed. It's a software tool that allows views of packet data over multiple capture files, and then can drill down to specific items using Wireshark to display the packet details.</p></div><div id="comment-50739-info" class="comment-info"><span class="comment-age">(07 Mar '16, 02:49)</span> grahamb ♦</div></div><span id="50748"></span><div id="comment-50748" class="comment"><div id="post-50748-score" class="comment-score"></div><div class="comment-text"><p>Problem with Napatech is that they don't distribute the software except to capture device vendors. I learned that the hard way - they're not interested in the consumer market, just selling to businesses they have an NDA with (and apparently you can't sign their NDA as a private person)</p></div><div id="comment-50748-info" class="comment-info"><span class="comment-age">(07 Mar '16, 06:25)</span> Jasper ♦♦</div></div></div><div id="comment-tools-50701" class="comment-tools"></div><div class="clear"></div><div id="comment-50701-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


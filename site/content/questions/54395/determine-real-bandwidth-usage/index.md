+++
type = "question"
title = "Determine real bandwidth usage"
description = '''Hi, i need to determine my real bandwidth usage in windows, but i find discrepancies when comparing different methods. Cacti says im using 3Mbps I/O: Net Limiter says aim using 2Mbps I/O Resource monitor says im using 2Mbps I/O Task manager says im using 3% of 100Mbps = 3Mbps I/O (I think so) I atta...'''
date = "2016-07-28T02:40:00Z"
lastmod = "2016-07-28T08:10:00Z"
weight = 54395
keywords = [ "bandwidth" ]
aliases = [ "/questions/54395" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Determine real bandwidth usage](/questions/54395/determine-real-bandwidth-usage)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54395-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, i need to determine my real bandwidth usage in windows, but i find discrepancies when comparing different methods.</p><p>Cacti says im using 3Mbps I/O:</p><p>Net Limiter says aim using 2Mbps I/O</p><p>Resource monitor says im using 2Mbps I/O</p><p>Task manager says im using 3% of 100Mbps = 3Mbps I/O (I think so)</p><p>I attach an image with this methods in that order..</p><p><img src="https://s32.postimg.org/5v6t6uc0l/bandw.jpg" title="Bandwidth" alt="alt text" /></p><p>This differences increases and are more noticeable when bandwidth usage increases. Which method should i trust and why this differences?</p><p>Is there any way i can measure bandwidth usage capturing packets with Wireshark?</p><p>Thank you!</p></div><div id="question-tags" class="tags-container tags">bandwidth</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Jul '16, 02:40</strong></p><img src="https://secure.gravatar.com/avatar/4d379d6778f93794bbe3c79d58f8b498?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dobledosis&#39;s gravatar image" /><p>dobledosis<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dobledosis has no accepted answers">0%</span></p></img></div></div><div id="comments-container-54395" class="comments-container"></div><div id="comment-tools-54395" class="comment-tools"></div><div class="clear"></div><div id="comment-54395-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54401"></span>

<div id="answer-container-54401" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54401-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You have two options...</p><p>Load the file under WireShark and select Statistics -&gt; Summary and look at the bottom.</p><p>OR...</p><p>Use Capinfos and dump the results to a text file showing something similar to the following:</p><pre><code>File name:           10.0.25.131.pcapng
File type:           Wireshark/... - pcapng
File encapsulation:  Ethernet
File timestamp precision:  microseconds (6)
Packet size limit:   file hdr: (not set)
Number of packets:   147 k
File size:           121 MB
Data size:           116 MB
Capture duration:    2502.877350 seconds
First packet time:   2016-07-20 13:29:29.987184
Last packet time:    2016-07-20 14:11:12.864534
Data byte rate:      46 kBps
Data bit rate:       371 kbps
Average packet size: 785.35 bytes
Average packet rate: 59 packets/s
...</code></pre><p>Note: Packets DON'T LIE!!! ( <em>GRIN</em> )</p><p>FWIW</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Jul '16, 08:10</strong></p><img src="https://secure.gravatar.com/avatar/6c8f0de8cb4ef9ad7093eefe24030e4b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wbenton&#39;s gravatar image" /><p>wbenton<br />
<span class="score" title="29 reputation points">29</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wbenton has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 28 Jul '16, 09:38</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-54401" class="comments-container"><span id="54427"></span><div id="comment-54427" class="comment"><div id="post-54427-score" class="comment-score"></div><div class="comment-text"><p>Thank you. That option is in legacy version. After looking at Wireshark i found that Cacti and Task manager are more accurate. What could be the reason for this difference?</p></div><div id="comment-54427-info" class="comment-info"><span class="comment-age">(28 Jul '16, 17:03)</span> dobledosis</div></div><span id="54430"></span><div id="comment-54430" class="comment"><div id="post-54430-score" class="comment-score"></div><div class="comment-text"><p>I would assume that each of the tools uses a different classification on which traffic on the interface should be taken into account for bandwidth occupation calculation (not all frames on the Ethernet interface make it beyond the first router, and people are usually interested in the bandwidth on the site uplink). Wireshark gives you the possibility to define the criteria yourself (at worst by filtering only some packets into a new file and using capinfos on it).</p><p>Another possibility could be that some tools may include the Ethernet preambles and checksums into the calculation, which to date Wireshark doesn't.</p><p>As for accuracy - to what reference value do you compare? If Cacti and Task manager just show the same value over the same traffic, it only means they use the same formula.</p></div><div id="comment-54430-info" class="comment-info"><span class="comment-age">(29 Jul '16, 00:32)</span> sindy</div></div><span id="54431"></span><div id="comment-54431" class="comment"><div id="post-54431-score" class="comment-score"></div><div class="comment-text"><blockquote><blockquote><blockquote><p>After looking at Wireshark i found that Cacti and Task manager are more accurate&lt;&lt;&lt;</p></blockquote></blockquote></blockquote><p>How are you comparing?</p><p>Did you capture using all 3 tools and compared the difference? Or did you use one tool (which one) to capture and all 3 tools to compare the differences?</p><p>Wireshark captures at the DLL layer and includes all packets from that layer upwards so it doesn't include the preamble data at layer 1.</p><p>As for which is more accurate, you would have to compare apples to apples to really say for sure.</p><p>Each program has their own calculation method so I guess it would be more correct to say, which calculation method do you prefer?</p><p>FWIW</p></div><div id="comment-54431-info" class="comment-info"><span class="comment-age">(29 Jul '16, 01:28)</span> wbenton</div></div><span id="54441"></span><div id="comment-54441" class="comment"><div id="post-54441-score" class="comment-score"></div><div class="comment-text"><p>In the exaple i gave there's only 1Mbps I/O of difference, but as bandwith usage increases, that difference increases even more, for example last night i had 14Mbps I/O with Cacti, task manager and Wireshark, and 10Mbps I/O with Net limiter and Resource monitor. So i preffer the method that includes as many packets as it can add to the final result.</p></div><div id="comment-54441-info" class="comment-info"><span class="comment-age">(29 Jul '16, 04:49)</span> dobledosis</div></div></div><div id="comment-tools-54401" class="comment-tools"></div><div class="clear"></div><div id="comment-54401-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


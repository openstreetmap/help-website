+++
type = "question"
title = "Tshark | Best Performance, Intel vs. AMD"
description = '''Before you guys say &quot;do your own research&quot; (which I will if this is inconclusive) I was just curious if anyone has tried out similar AMD/Intel rigs and benchmarked their performance on highly parallelized Tshark/Wireshark operations. Upwards of 60 cores. From my googling I couldn&#x27;t find that anyone ...'''
date = "2014-08-19T10:49:00Z"
lastmod = "2014-08-20T15:05:00Z"
weight = 35587
keywords = [ "optimize", "tshark", "intel", "wireshark" ]
aliases = [ "/questions/35587" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Tshark | Best Performance, Intel vs. AMD](/questions/35587/tshark-best-performance-intel-vs-amd)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35587-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Before you guys say "do your own research" (which I will if this is inconclusive) I was just curious if anyone has tried out similar AMD/Intel rigs and benchmarked their performance on highly parallelized Tshark/Wireshark operations. Upwards of 60 cores. From my googling I couldn't find that anyone looked into this. Also, any optimization or performance suggestions would be highly appreciated. I did find some great info with using 'dd -bs' to speed up reading from disk.</p><p>I should make it more clear. I am running multiple instances of Tshark at once over multiple different capture files.</p></div><div id="question-tags" class="tags-container tags">optimize tshark intel wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Aug '14, 10:49</strong></p><img src="https://secure.gravatar.com/avatar/5032e6783aeacbd305a38c0bb622b329?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Blackdragon1400&#39;s gravatar image" /><p>Blackdragon1400<br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Blackdragon1400 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 19 Aug '14, 12:07</p></div></div><div id="comments-container-35587" class="comments-container"><span id="35590"></span><div id="comment-35590" class="comment"><div id="post-35590-score" class="comment-score"></div><div class="comment-text"><p>Presumably by "paralellized" you mean "running many copies of TShark or Wireshark in parallel"; as grahamb notes, they aren't multi-threaded (multi-threading may be possible, but it's not easy; dissecting network traffic is <em>not</em> easily parallelizeable because dissection of later data in a packet depends on dissection of earlier data in a packet and dissection of data in a later packet often depends on data in earlier packets).</p></div><div id="comment-35590-info" class="comment-info"><span class="comment-age">(19 Aug '14, 11:20)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-35587" class="comment-tools"></div><div class="clear"></div><div id="comment-35587-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="35589"></span>

<div id="answer-container-35589" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35589-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Tshark/Wireshark are basically single threaded apps so don't benefit from multiple cores.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Aug '14, 11:09</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-35589" class="comments-container"><span id="35592"></span><div id="comment-35592" class="comment"><div id="post-35592-score" class="comment-score"></div><div class="comment-text"><p>I run many instances at once.</p></div><div id="comment-35592-info" class="comment-info"><span class="comment-age">(19 Aug '14, 11:47)</span> Blackdragon1400</div></div><span id="35594"></span><div id="comment-35594" class="comment"><div id="post-35594-score" class="comment-score"></div><div class="comment-text"><blockquote><p>any optimization or performance suggestions would be highly appreciated</p></blockquote><p>For capturing performance libpcap &gt;= 1.5.3</p><p>I would imagine, without having any measurements to back it up that CPU and memory speed would matter more than manufacturer. Disc access is also a bottleneck.</p><p>I would also recomend using the development verson as we have done some optimiztions to the dissection Engine recently.</p><p>Running the valgrind script on one of your traces might indicate if something in the protocol mix you are using could be optimized further. ( in the Tools dir valgrind-wireshark.sh )</p></div><div id="comment-35594-info" class="comment-info"><span class="comment-age">(19 Aug '14, 12:51)</span> Anders ♦</div></div></div><div id="comment-tools-35589" class="comment-tools"></div><div class="clear"></div><div id="comment-35589-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="35644"></span>

<div id="answer-container-35644" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35644-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you only want to capture dumpcap would be preferable. Like Wireshark, tshark builds data structures for decode purposes whereas dumpcap just takes the data from the npf driver (via the buffer) and writes it to disk. We've run dumpcap captures for weeks without a problem.</p><p>We use Dell R320 and R420 units and for outright performance, the disk is definitely the bottleneck. Our units have one system disk and three data disks. We stripe across the three disks and my colleagues claim we can handle a sustained rate of 3 Gbps before we start losing packets. OS is Windows 7.</p><p>Best regards...Paul</p><p>PS: just noticed you reference to libpcap, so transpose the above accordingly. Not sure if dumpcap is applicable on Linux, so perhaps tcpdump would be preferable.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Aug '14, 15:05</strong></p><img src="https://secure.gravatar.com/avatar/2e1b4057f2ff59fe059b23cc6571abaf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PaulOfford&#39;s gravatar image" /><p>PaulOfford<br />
<span class="score" title="131 reputation points">131</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="32 badges"><span class="silver">●</span><span class="badgecount">32</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PaulOfford has 5 accepted answers">11%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 20 Aug '14, 15:08</p></div></div><div id="comments-container-35644" class="comments-container"></div><div id="comment-tools-35644" class="comment-tools"></div><div class="clear"></div><div id="comment-35644-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


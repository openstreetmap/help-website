+++
type = "question"
title = "Wireshark Capture Analysis"
description = '''There is an application which runs smoothly but, during random intervals the application fails. There nothing int the servers or appllication and the problem is directed towrds network with a wireshark capture. I give below some of the captured packets and hoping that some clues would be posted thro...'''
date = "2012-05-08T17:16:00Z"
lastmod = "2012-05-09T01:08:00Z"
weight = 10795
keywords = [ "monitoring" ]
aliases = [ "/questions/10795" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark Capture Analysis](/questions/10795/wireshark-capture-analysis)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10795-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>There is an application which runs smoothly but, during random intervals the application fails. There nothing int the servers or appllication and the problem is directed towrds network with a wireshark capture. I give below some of the captured packets and hoping that some clues would be posted through this forum as I am unfamiliar with interpreting the output.</p><pre><code>737783, &quot;13237.043511&quot;  ,&quot;Vmware_57:a4  :2a&quot;,&quot;Broadcas  t&quot;,&quot;0x8 922&quot;,   &quot;77&quot;,&quot;Ethernet II&quot;
737784, &quot;13237.051094&quot;  ,&quot;10.61.67.47&quot;  ,&quot;172.18.3.25&quot;  ,&quot;TCP&quot;, &quot;62&quot;,   &quot;[TCP Port numbers reused] ovtopmd &gt; ms-sql-s [SYN] Seq=0 Win=64240 Len=0 MSS=1460

SACK_PE RM=1&quot;                   
737785, &quot;13237.055775&quot;  ,&quot;172.18.3.25&quot;  ,&quot;10.61.67.47&quot;  ,&quot;TCP&quot;, &quot;62&quot;,   &quot;ms-sql-s &gt; ovtopmd [SYN, ACK] Seq=0 Ack=1 Win=65535 Len=0 MSS=1380 SACK_PERM=1&quot;
737786, &quot;13237.055795&quot;  ,&quot;10.61.67.47&quot;  ,&quot;172.18.3.25&quot;  ,&quot;TCP&quot;, &quot;54&quot;,   &quot;ovtopmd &gt; ms-sql-s [ACK] Seq=1 Ack=1 Win=64240 Len=0&quot;
737787, &quot;13237.056195&quot;  ,&quot;10.61.67.47&quot;  ,&quot;172.18.3.25&quot;  ,&quot;TDS&quot;, &quot;258&quot;   ,&quot;TDS7 login&quot;
737788, &quot;13237.067079&quot;  ,&quot;172.18.3.25&quot;  ,&quot;10.61.67.47&quot;  ,&quot;TDS&quot;, &quot;439&quot;   ,&quot;Response&quot;
737789, &quot;13237.091552&quot;  ,&quot;10.61.67.47&quot;  ,&quot;172.18.3.25&quot;  ,&quot;TDS&quot;, &quot;118&quot;   ,&quot;SQL batch&quot;
737790, &quot;13237.092148&quot;  ,&quot;10.61.67.47&quot;  ,&quot;172.18.3.25&quot;  ,&quot;TCP&quot;, &quot;62&quot;,   &quot;[TCP Port numbers reused] snifferserver &gt; ms-sql-s [SYN] Seq=0 Win=64240 Len=0 MSS=146 0 SACK_PERM=1&quot;                  
737791, &quot;13237.095027&quot;  ,&quot;172.18.3.25&quot;  ,&quot;10.61.67.47&quot;  ,&quot;TDS&quot;, &quot;71&quot;,   &quot;Response&quot;
737792, &quot;13237.095163&quot;  ,&quot;10.61.67.47&quot;  ,&quot;172.18.3.25&quot;  ,&quot;TDS&quot;, &quot;106&quot;   ,&quot;SQL batch&quot;
737793, &quot;13237.095369&quot;  ,&quot;172.18.3.25&quot;  ,&quot;10.61.67.47&quot;  ,&quot;TCP&quot;, &quot;62&quot;,   &quot;ms-sql-s &gt; snifferserver [SYN, ACK] Seq=0 Ack=1 Win=65535 Len=0 MSS=1380 SACK_PERM=1&quot;
737794, &quot;13237.095384&quot;  ,&quot;10.61.67.47&quot;  ,&quot;172.18.3.25&quot;  ,&quot;TCP&quot;, &quot;54&quot;,   &quot;snifferserver &gt; ms-sql-s [ACK] Seq=1 Ack=1 Win=64240 Len=0&quot;
737795, &quot;13237.095744&quot;  ,&quot;10.61.67.47&quot;  ,&quot;172.18.3.25&quot;  ,&quot;TDS&quot;, &quot;258&quot;   ,&quot;TDS7 login&quot;
737796, &quot;13237.098584&quot;  ,&quot;172.18.3.25&quot;  ,&quot;10.61.67.47&quot;  ,&quot;TDS&quot;, &quot;82&quot;,   &quot;Response&quot;
737797, &quot;13237.098698&quot;  ,&quot;10.61.67.47&quot;  ,&quot;172.18.3.25&quot;  ,&quot;TDS&quot;, &quot;118&quot;   ,&quot;SQL batch&quot;
737798, &quot;13237.100706&quot;  ,&quot;172.18.3.25&quot;  ,&quot;10.61.67.47&quot;  ,&quot;TDS&quot;, &quot;439&quot;   ,&quot;Response&quot;
737799, &quot;13237.102516&quot;  ,&quot;172.18.3.25&quot;  ,&quot;10.61.67.47&quot;  ,&quot;TDS&quot;, &quot;71&quot;,   &quot;Response&quot;
737800, &quot;13237.103375&quot;  ,&quot;10.61.67.47&quot;  ,&quot;172.18.3.25&quot;  ,&quot;TDS&quot;, &quot;118&quot;   ,&quot;SQL batch&quot;
737801, &quot;13237.103889&quot;  ,&quot;10.61.67.47&quot;  ,&quot;172.18.3.25&quot;  ,&quot;TCP&quot;, &quot;1434   &quot;,&quot;[TCP segment of a reassembled PDU]&quot;
737802, &quot;13237.103906&quot;  ,&quot;10.61.67.47&quot;  ,&quot;172.18.3.25&quot;  ,&quot;TDS&quot;, &quot;801&quot;   ,&quot;Remote Procedure Call&quot;
737803, &quot;13237.104403&quot;  ,&quot;10.61.67.47&quot;  ,&quot;172.18.3.25&quot;  ,&quot;TCP&quot;, &quot;62&quot;,   &quot;[TCP Port numbers reused] combox-web-acc &gt; ms-sql-s [SYN] Seq=0 Win=64240 Len=0</code></pre></div><div id="question-tags" class="tags-container tags">monitoring</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 May '12, 17:16</strong></p><img src="https://secure.gravatar.com/avatar/92b777dcfcdb1b2fa8c718be990b94ac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NizamSri&#39;s gravatar image" /><p>NizamSri<br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NizamSri has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 May '12, 02:08</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-10795" class="comments-container"></div><div id="comment-tools-10795" class="comment-tools"></div><div class="clear"></div><div id="comment-10795-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="10812"></span>

<div id="answer-container-10812" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10812-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Sorry buddy, but what you are looking for is serious network consulting / analysis. This Q&amp;A is dedicated to people having specific questions about wireshark and/or network analysis and everybody here answers on his own time, so sorry for making that statement.</p><p>From your point saying that you're "unfamiliar with interpreting the output", you should either get help by hiring someone doing netw.analysis or start looking at several good websites/tutorials on how to get started with wireshark.</p><p>If you have a specific question regarding the output of your sniffer, feel free to ask it here again.</p><p>Oh BTW: Give me two cents for every time I heard "There is nothing wrong with server/application, it MUST be the network", you better don't rely on this unless you found a network-based problem ;)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 May '12, 01:01</strong></p><img src="https://secure.gravatar.com/avatar/36b41326bff63eb5ad73a0436914e05c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Landi&#39;s gravatar image" /><p>Landi<br />
<span class="score" title="2269 reputation points"><span>2.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Landi has 28 accepted answers">28%</span></p></div></div><div id="comments-container-10812" class="comments-container"></div><div id="comment-tools-10812" class="comment-tools"></div><div class="clear"></div><div id="comment-10812-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="10814"></span>

<div id="answer-container-10814" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10814-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I second what Landi said, and would like to ask: how do you know the problem is within the few packets you provided?</p><p>Anyway, there is one message, that calls for trouble: '<strong>TCP Port numbers reused</strong>'. However, based on the few samples you posted, no further analysis is possible.</p><p>Please ask your application developers why the application (or the OS) is re-using TCP Ports and if that could cause any trouble.</p><p>So, maybe it's not the network, but rather the application (or OS) ;-))</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 May '12, 01:08</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 May '12, 02:27</p></div></div><div id="comments-container-10814" class="comments-container"><span id="10828"></span><div id="comment-10828" class="comment"><div id="post-10828-score" class="comment-score"></div><div class="comment-text"><p>Also look at any device that performs natting or loadbalancing (which basically is natting as well). Theses devices might be re-using port numbers to quickly too.</p><p>It could also be that your trace is just very large (I see 700K+ packets) and the port number rotation is not a problem at all.</p><p>As said before, Network Analysis is not a triviality that can be done on couple of packets. For specific questions (like "What does [TCP port numbers reused] mean?") you can always ask here. If you want your problem analyzed for you, you can always hire someone (even people from here) to do it for you.</p></div><div id="comment-10828-info" class="comment-info"><span class="comment-age">(09 May '12, 05:50)</span> SYN-bit ♦♦</div></div><span id="10857"></span><div id="comment-10857" class="comment"><div id="post-10857-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the comments..This is only a portion of capture and the rest of it also looks similar. This does not have natting or load balancing and goes through only an ASA fw which is having default config for the traffic. It too does not show any anomally. The frequency of break down happens intermittenly and no packet drop observed during those times. But there are maformed packets throuhgout the capture.rgds - NizamSri</p></div><div id="comment-10857-info" class="comment-info"><span class="comment-age">(09 May '12, 16:46)</span> NizamSri</div></div><span id="10882"></span><div id="comment-10882" class="comment"><div id="post-10882-score" class="comment-score"></div><div class="comment-text"><p>Ah, a firewall...</p><p>Well, let's go back to the <strong>'TCP Port numbers reused'</strong> message. If that is really a problem (and not just caused by the large capture file), then your firewall might occasionally drop single connection requests if the port reuse is to fast. This usuallys happens, when there is still a connection record in the firewalls state table. So, I suggest to look for unanswerd SYN packets (firewall drop) and/or for TCP RESET (firewall reject) in the capture file.</p><p>See here (and others in the forum) to find unanswered SYNs.<br />
<strong><a href="http://ask.wireshark.org/questions/10640/how-to-find-syn-not-followed-by-a-synack?page=1#10641">http://ask.wireshark.org/questions/10640/how-to-find-syn-not-followed-by-a-synack?page=1#10641</a></strong></p><p>Regards<br />
Kurt</p></div><div id="comment-10882-info" class="comment-info"><span class="comment-age">(10 May '12, 02:08)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-10814" class="comment-tools"></div><div class="clear"></div><div id="comment-10814-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


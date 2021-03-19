+++
type = "question"
title = "Try to obtain RTT average in windows"
description = '''Hi, For my internship i have to do network performance. With wireshark i cannot obtain the RTT average or have all RTT values (i could do the average with excel if i have it). I tried with statistics -&amp;gt; RTT StreamGraph -&amp;gt; RTT Graph the values appears in a graph but i can&#x27;t collect them. One ot...'''
date = "2013-06-17T03:07:00Z"
lastmod = "2013-06-18T05:39:00Z"
weight = 22113
keywords = [ "rtt", "average", "list" ]
aliases = [ "/questions/22113" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Try to obtain RTT average in windows](/questions/22113/try-to-obtain-rtt-average-in-windows)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22113-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>For my internship i have to do network performance.</p><p>With wireshark i cannot obtain the RTT average or have all RTT values (i could do the average with excel if i have it).</p><p>I tried with statistics -&gt; RTT StreamGraph -&gt; RTT Graph the values appears in a graph but i can't collect them.</p><p>One other try: IO Graph, with filter and unit advanced, AVG(tcp.analysis.ack_rtt), the "Analyze TCP sequence numbers" activated in TCP protocol options in Wireshark preferences, and there is an empty grap without values.</p><p>Can someone help me?</p><p>PS: I work with Windows Server 2008 R2.</p><p>Thank's</p></div><div id="question-tags" class="tags-container tags">rtt average list</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Jun '13, 03:07</strong></p><img src="https://secure.gravatar.com/avatar/a52e10e572ae5ad74df7cb60aec62b1b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Geoffrey%20Plv%20CouchCouch&#39;s gravatar image" /><p>Geoffrey Plv...<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Geoffrey Plv CouchCouch has no accepted answers">0%</span></p></div></div><div id="comments-container-22113" class="comments-container"></div><div id="comment-tools-22113" class="comment-tools"></div><div class="clear"></div><div id="comment-22113-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="22122"></span>

<div id="answer-container-22122" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22122-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I believe RTT is a calculated value, not a stored value, where latency is represented as the time between a sent packet and it's corresponding acknowledgement. So exporting the packets in text so that you could import it into Excel wouldn't give you an RTT value that you could average without some manipulation.<br />
I think you would have to use the tcp.analysis.ack_rtt as you indicated, also use View | Time Display Format | Seconds Since Last Captured Packet, export it to a text file, import it into Excel, and then in your spreadsheet average the values, along with using the tcp.analysis.ack_rtt as you indicated. This <em>may</em> be what you're looking for?</p><p>Hope this is helpful, and best of luck with your project, John</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jun '13, 12:52</strong></p><img src="https://secure.gravatar.com/avatar/1f3966b6e9de3a63326e2d3fd51c8c04?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="John_Modlin&#39;s gravatar image" /><p>John_Modlin<br />
<span class="score" title="120 reputation points">120</span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="John_Modlin has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-22122" class="comments-container"><span id="22127"></span><div id="comment-22127" class="comment"><div id="post-22127-score" class="comment-score"></div><div class="comment-text"><p>Thanks for that, i think it will work. However, I still have one problem, i don't know how to export only the RTT value, when i try to export in wireshark it's all the information I obtain.</p><p>Do you know how to select one detail of a TCP stream and export it?</p><p>Thank you for the information.</p></div><div id="comment-22127-info" class="comment-info"><span class="comment-age">(18 Jun '13, 01:19)</span> Geoffrey Plv...</div></div><span id="22128"></span><div id="comment-22128" class="comment"><div id="post-22128-score" class="comment-score"></div><div class="comment-text"><p>Other thing, when i do the statistic "Packets length..." it give a stats on all packets filtered ( filter = "ip.dst == X.X.X.X and tcp.analysis.ack_rtt" ) and one column is rate in ms, do you the meaning of that?</p><p>Thank's in avance</p></div><div id="comment-22128-info" class="comment-info"><span class="comment-age">(18 Jun '13, 01:30)</span> Geoffrey Plv...</div></div></div><div id="comment-tools-22122" class="comment-tools"></div><div class="clear"></div><div id="comment-22122-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="22132"></span>

<div id="answer-container-22132" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22132-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I don't believe the RTT value is an exportable value. You would have to calculate the RTT, once you export the selected packets, based on the seconds between the sent packet and it's corresponding acknowledgement.<br />
</p><p>You can right click on a packet within wireshark and then select Follow TCP Stream to display only that stream. Then you can select File | Export Selected Packets to export those packets to another .pcapng file or another format if needed.</p><p>The packet length is displayed in the Frame Header and a column is normally set as a default so you can see packet length between Protocol and Info columns.<br />
</p><p>If you're going to be using Wireshark a lot going forward, I highly recommend Laura Chappell's book, Wireshark Network Analysis, Second Edition. You will learn tons!</p><p>Best of luck Geoffrey :)</p><p>John</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Jun '13, 05:39</strong></p><img src="https://secure.gravatar.com/avatar/1f3966b6e9de3a63326e2d3fd51c8c04?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="John_Modlin&#39;s gravatar image" /><p>John_Modlin<br />
<span class="score" title="120 reputation points">120</span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="John_Modlin has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 18 Jun '13, 07:46</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-22132" class="comments-container"></div><div id="comment-tools-22132" class="comment-tools"></div><div class="clear"></div><div id="comment-22132-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


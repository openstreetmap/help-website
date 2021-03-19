+++
type = "question"
title = "Save tcp stream according to number of packets?"
description = '''In my current pcap file, I have over 500 TCP streams and UDP streams (according to the Statistics -&amp;gt; Conversations in Wireshark). But many of them only have a few packets being passed between the source and destination.  I want to analyze the streams that have more than, say 100 packets, sent fro...'''
date = "2016-12-10T20:54:00Z"
lastmod = "2016-12-12T05:36:00Z"
weight = 57998
keywords = [ "tcp.stream", "flow", "tshark", "stream", "wireshark" ]
aliases = [ "/questions/57998" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Save tcp stream according to number of packets?](/questions/57998/save-tcp-stream-according-to-number-of-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57998-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In my current pcap file, I have over 500 TCP streams and UDP streams (according to the Statistics -&gt; Conversations in Wireshark). But many of them only have a few packets being passed between the source and destination.</p><p>I want to analyze the streams that have more than, say 100 packets, sent from A to B. I saw a way to save tcp streams to separate pcap files here: <a href="https://ask.wireshark.org/questions/4677/easy-way-to-save-tcp-streams">https://ask.wireshark.org/questions/4677/easy-way-to-save-tcp-streams</a></p><p>But that command saves all the tcp streams, which I don't need. As a matter of fact, I don't need all the payload either, I only want all the basic information of each stream saved in a separate file. I thought about exporting straight from Wireshark, but that wouldn't group them according to individual flows.</p><p>So basically, I want a way to save all the packet information (without the payload) of every flow (that has more than 100 packets) in separate files. Is there anyway to do this?</p><p>Thanks for the help!</p></div><div id="question-tags" class="tags-container tags">tcp.stream flow tshark stream wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Dec '16, 20:54</strong></p><img src="https://secure.gravatar.com/avatar/8c6f9b84c663cb4c178ced1e6aace2e7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrk&#39;s gravatar image" /><p>mrk<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrk has no accepted answers">0%</span></p></div></div><div id="comments-container-57998" class="comments-container"></div><div id="comment-tools-57998" class="comment-tools"></div><div class="clear"></div><div id="comment-57998-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58018"></span>

<div id="answer-container-58018" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58018-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can do this with <a href="https://www.tracewrangler.com">TraceWrangler</a>, using the latest semi-automated build available here: <a href="https://www.tracewrangler.com/download/automated/">https://www.tracewrangler.com/download/automated/</a></p><ol><li>Start TraceWrangler</li><li>Add capture file(s) to the list</li><li>Open Tools -&gt; Conversation Summary</li><li>Select TCP Tab, and sort by "Packets" column with descending number of packets</li><li>Mark the number of rows you want, e.g. by clicking on the first row, and using Shift + Cursor down</li><li>Right click on the selected rows, and select "Extract" -&gt; "to multiple files"</li><li>Activate the "Truncate" checkmark box and select "Layer 4"</li><li>Press the "Okay" button to run the extraction</li></ol><p>You should get a sub directory called "extracted" with one file per flow.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Dec '16, 05:36</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-58018" class="comments-container"><span id="58063"></span><div id="comment-58063" class="comment"><div id="post-58063-score" class="comment-score"></div><div class="comment-text"><p>Thank you! This is exactly what I wanted</p></div><div id="comment-58063-info" class="comment-info"><span class="comment-age">(13 Dec '16, 21:41)</span> mrk</div></div></div><div id="comment-tools-58018" class="comment-tools"></div><div class="clear"></div><div id="comment-58018-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


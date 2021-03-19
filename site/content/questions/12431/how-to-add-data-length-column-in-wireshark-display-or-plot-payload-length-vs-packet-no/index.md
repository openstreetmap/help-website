+++
type = "question"
title = "how to add data length column in wireshark display or plot payload length vs packet no"
description = '''if i open any pcap in wireshark, it will have several columns to display the information like src/dest ip &amp;amp; port no&#x27;s, prot, info etc for each packet. i want one more column to be added which displays the data length field. i searched for this field but rather i could only find &quot;packet length&quot; f...'''
date = "2012-07-03T23:32:00Z"
lastmod = "2012-07-04T01:55:00Z"
weight = 12431
keywords = [ "winpcap", "pcap", "tshark", "wireshark" ]
aliases = [ "/questions/12431" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [how to add data length column in wireshark display or plot payload length vs packet no](/questions/12431/how-to-add-data-length-column-in-wireshark-display-or-plot-payload-length-vs-packet-no)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12431-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>if i open any pcap in wireshark, it will have several columns to display the information like src/dest ip &amp; port no's, prot, info etc for each packet. i want one more column to be added which displays the data length field. i searched for this field but rather i could only find "packet length" field which shows the length of packet including the headers but i want only the payload length. is there any way to do that ??</p><p>OR</p><p>is there any way to plot the graph with packet no on the x axis and payload length on the y axis ?</p></div><div id="question-tags" class="tags-container tags">winpcap pcap tshark wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Jul '12, 23:32</strong></p><img src="https://secure.gravatar.com/avatar/ce14610470a60c9adcc5f03599f66608?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="viks&#39;s gravatar image" /><p>viks<br />
<span class="score" title="16 reputation points">16</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="viks has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 03 Jul '12, 23:38</p></div></div><div id="comments-container-12431" class="comments-container"></div><div id="comment-tools-12431" class="comment-tools"></div><div class="clear"></div><div id="comment-12431-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12435"></span>

<div id="answer-container-12435" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12435-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can add a new column like this:</p><blockquote><p><code>Edit -&gt; Preferences -&gt; User Interface -&gt; Columns -&gt; Add</code></p></blockquote><p>Choose the <strong>Field Type</strong> to be <code>Custom</code> and the <strong>Field name</strong> either <code>tcp.len</code> or <code>udp.length</code>.</p><p>Click Apply and Save. BTW: You can change the position of the column with drag-n-drop.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Jul '12, 01:55</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-12435" class="comments-container"><span id="12437"></span><div id="comment-12437" class="comment"><div id="post-12437-score" class="comment-score"></div><div class="comment-text"><p>@kurt : thanks a lot. one more thing...is there any way to export only the payload bytes (rather than export in c arrays form which has headers also) or to plot the payload bytes vs packet number ?</p></div><div id="comment-12437-info" class="comment-info"><span class="comment-age">(04 Jul '12, 02:55)</span> viks</div></div><span id="12445"></span><div id="comment-12445" class="comment"><div id="post-12445-score" class="comment-score">1</div><div class="comment-text"><p>you can do that with tshark.</p><p><strong>payload bytes</strong><br />
</p><blockquote><p><code>tshark -r input.cap -T fields -e frame.number -e tcp.data -E header=y -E separator=;</code><br />
</p></blockquote><p><strong>payload length</strong><br />
</p><blockquote><p><code>tshark -r input.cap -T fields -e frame.number -e frame.len -e ip.len -e tcp.len  -E header=y -E separator=;</code><br />
</p></blockquote><p>tcp.len is the payload length for TCP. For a list of other fields, run this command:</p><blockquote><p><code>tshark -G</code></p></blockquote></div><div id="comment-12445-info" class="comment-info"><span class="comment-age">(04 Jul '12, 10:58)</span> Kurt Knochner ♦</div></div><span id="12449"></span><div id="comment-12449" class="comment"><div id="post-12449-score" class="comment-score"></div><div class="comment-text"><p>@kurt : thanks for the info. when i Choose the Field Type to be Custom and the Field name data.len it doesn't work. Any idea ?</p></div><div id="comment-12449-info" class="comment-info"><span class="comment-age">(04 Jul '12, 19:02)</span> viks</div></div><span id="12450"></span><div id="comment-12450" class="comment"><div id="post-12450-score" class="comment-score"></div><div class="comment-text"><p>the fields <code>data.*</code> will be only set if the dissector for a protcol is disabled (Analyze -&gt; Enabled Protocols) or if there is no dissector for a protocol. Example: If you disable the protocol 'HTTP' and then <code>data.len</code> will work. You better use <strong><code>tcp.len</code></strong> or <strong><code>udp.length</code></strong></p></div><div id="comment-12450-info" class="comment-info"><span class="comment-age">(04 Jul '12, 22:40)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-12435" class="comment-tools"></div><div class="clear"></div><div id="comment-12435-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


+++
type = "question"
title = "python extraction of flow statistics of a pcap file"
description = '''hello all i must use some features of all log-data of a adsl router traffic with various users (features like max-min-median length packet in forward or backward flow). after saving traffic with wireshark in pcap or pcapng format, how can i calculate or use this features from a pcap file and use the...'''
date = "2017-10-14T12:24:00Z"
lastmod = "2017-10-18T07:47:00Z"
weight = 63902
keywords = [ "python", "wireshark" ]
aliases = [ "/questions/63902" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [python extraction of flow statistics of a pcap file](/questions/63902/python-extraction-of-flow-statistics-of-a-pcap-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63902-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hello all i must use some features of all log-data of a adsl router traffic with various users (features like max-min-median length packet in forward or backward flow). after saving traffic with wireshark in pcap or pcapng format, how can i calculate or use this features from a pcap file and use them in a python program??</p></div><div id="question-tags" class="tags-container tags">python wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Oct '17, 12:24</strong></p><img src="https://secure.gravatar.com/avatar/2c1240eb24fe6b4abf2578b2a2843831?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MohammadE&#39;s gravatar image" /><p>MohammadE<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MohammadE has no accepted answers">0%</span></p></div></div><div id="comments-container-63902" class="comments-container"></div><div id="comment-tools-63902" class="comment-tools"></div><div class="clear"></div><div id="comment-63902-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="64001"></span>

<div id="answer-container-64001" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-64001-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you have file1.pcap to process, you can use <strong><em>tshark -T fields -e frame.len -Eseparator=/t -r file1.pcap &gt;file1_out.tab</em></strong> to get the length of each frame in a tab-delimited format for processing via stats library in python or other languages.</p><p>the -e option can take any wireshark display filter so you can add additional info if needed (e.g. ip src/dst, tcp src/dst, frame number)</p><p>If you want to do all of the processing within python, look into pylibpcap or other pcap-related libraries.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Oct '17, 07:47</strong></p><img src="https://secure.gravatar.com/avatar/3f2f87a6a68e4c51c3851c20b6c56a1a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="CMH_Tim&#39;s gravatar image" /><p>CMH_Tim<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="CMH_Tim has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 18 Oct '17, 07:50</p></div></div><div id="comments-container-64001" class="comments-container"></div><div id="comment-tools-64001" class="comment-tools"></div><div class="clear"></div><div id="comment-64001-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


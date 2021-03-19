+++
type = "question"
title = "decode as http on all ports"
description = '''Hi want to decode all packets as if they were http. How can i do this?  The packets that don&#x27;t have an http.request.uri I will just awk out.  At the moment I have been doing it with this bash script iterating over port numbers. I am sure i must be missing something.  Horrific hack:  #!/bin/bash for ...'''
date = "2013-08-26T12:37:00Z"
lastmod = "2013-08-26T12:37:00Z"
weight = 24072
keywords = [ "filter", "tcp.port", "all", "http", "ports" ]
aliases = [ "/questions/24072" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [decode as http on all ports](/questions/24072/decode-as-http-on-all-ports)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24072-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi want to decode all packets as if they were http. How can i do this? The packets that don't have an http.request.uri I will just awk out.</p><p>At the moment I have been doing it with this bash script iterating over port numbers. I am sure i must be missing something.</p><p>Horrific hack:</p><pre><code>#!/bin/bash
for i in `seq 1 65535`;
   do

tshark -r mycap.pcap -d tcp.port==$i,http -T fields -e frame.time -e http.request.method -e http.request.uri -e http.host -e http.user_agent -e tcp.dstport -E  header=y | awk &#39;{if (NR!=1) {print}}&#39; | awk -F&#39;\t&#39; &#39;x$3&#39; &gt;&gt; output.csv

  done</code></pre><p>Thanks</p><p>Edit:</p><p>Found <a href="https://www.wireshark.org/docs/man-pages/tshark.html">https://www.wireshark.org/docs/man-pages/tshark.html</a> Example: -d tcp.port==8888:3,http will decode any traffic running over TCP ports 8888, 8889 or 8890 as HTTP.</p><p>Solution: ./wireshark-1.10.1/tshark -r mycap.pcap -d tcp.port==1-65535,http -T fields -e frame.time -e http.request.method -e http.request.uri -e http.host -e http.user_agent -e tcp.dstport -E header=y</p><p>You must have 1.10.1 for it to work.</p></div><div id="question-tags" class="tags-container tags">filter tcp.port all http ports</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Aug '13, 12:37</strong></p><img src="https://secure.gravatar.com/avatar/8eb0ead229db87bf1459695e9183b4e6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="computeruser1&#39;s gravatar image" /><p>computeruser1<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="computeruser1 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 29 Aug '13, 13:33</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-24072" class="comments-container"><span id="24073"></span><div id="comment-24073" class="comment"><div id="post-24073-score" class="comment-score"></div><div class="comment-text"><p>Good question! I wonder this same thing every time I use the "Decode As" dialog box...</p></div><div id="comment-24073-info" class="comment-info"><span class="comment-age">(26 Aug '13, 12:54)</span> smp</div></div><span id="24077"></span><div id="comment-24077" class="comment"><div id="post-24077-score" class="comment-score"></div><div class="comment-text"><p>Please cut your answer from the question and paste it into an answer, so that this question is marked as answered, and so that it's clearer that the question has an answer.</p></div><div id="comment-24077-info" class="comment-info"><span class="comment-age">(26 Aug '13, 15:51)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-24072" class="comment-tools"></div><div class="clear"></div><div id="comment-24072-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>


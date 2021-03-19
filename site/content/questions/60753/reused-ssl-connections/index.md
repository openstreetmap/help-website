+++
type = "question"
title = "Reused SSL connections"
description = '''How can I filter in Wireshark for reused SSL connections or reused port numbers? i.e. different SSL TCP Streams using the same tuple. I&#x27;m troubleshooting a tcpdump and I want to check if connections are reused successfully or not at all. From what i understand, I want to filter for all established c...'''
date = "2017-04-11T17:07:00Z"
lastmod = "2017-04-12T02:26:00Z"
weight = 60753
keywords = [ "reused", "connection" ]
aliases = [ "/questions/60753" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Reused SSL connections](/questions/60753/reused-ssl-connections)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60753-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How can I filter in Wireshark for reused SSL connections or reused port numbers? i.e. different SSL TCP Streams using the same tuple.</p><p>I'm troubleshooting a tcpdump and I want to check if connections are reused successfully or not at all.</p><p>From what i understand, I want to filter for all established connections (tcp.flags.syn==1) &amp;&amp; (tcp.flags.ack==0)</p><p>and then find which ones use the same port pair</p><p>How can i filter by reused port numbers?</p></div><div id="question-tags" class="tags-container tags">reused connection</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Apr '17, 17:07</strong></p><img src="https://secure.gravatar.com/avatar/3c9ea34649c8d322e9cfd6dca1280643?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="evgenia&#39;s gravatar image" /><p>evgenia<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="evgenia has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 11 Apr '17, 17:28</p></div></div><div id="comments-container-60753" class="comments-container"></div><div id="comment-tools-60753" class="comment-tools"></div><div class="clear"></div><div id="comment-60753-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60759"></span>

<div id="answer-container-60759" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60759-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>My idea would be to use the TCP analysis results provided by Wireshark, and filter on them like this:</p><pre><code>tcp.analysis.reused_ports</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Apr '17, 02:26</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-60759" class="comments-container"><span id="60775"></span><div id="comment-60775" class="comment"><div id="post-60775-score" class="comment-score"></div><div class="comment-text"><p>Do all reused connections always have a TCP packet with description "TCP port numbers reused"?</p><p>I thought that one would see the "TCP port numbers reused" in combination with "RST" (reset) packets because the reuse of the connection is forced by interrupting the graceful closing of the connection (waiting for TIME_WAIT to elapse) But if the connection is closed gracefully without forcing reset, then one would not see the "TCP port numbers reused" -&gt; Is my understanding of the above correct?</p></div><div id="comment-60775-info" class="comment-info"><span class="comment-age">(12 Apr '17, 11:07)</span> evgenia</div></div><span id="60776"></span><div id="comment-60776" class="comment"><div id="post-60776-score" class="comment-score"></div><div class="comment-text"><p>No, unfortunately not. The "port reused" symptom is diagnosed like this (excerpt from the TCP dissector code of wireshark):</p><pre><code>    /* If this is a SYN packet, then check if its seq-nr is different
     * from the base_seq of the retrieved conversation. If this is the
     * case, create a new conversation with the same addresses and ports
     * and set the TA_PORTS_REUSED flag. If the seq-nr is the same as
     * the base_seq, then do nothing so it will be marked as a retrans-
     * mission later.
     */</code></pre><p>So as long as Wireshark sees the new SYN packet with the different initial sequence number, it's marked as "Port Reused", and it doesn't matter if there was a RST, FIN or nothing else in the old connection.</p></div><div id="comment-60776-info" class="comment-info"><span class="comment-age">(12 Apr '17, 11:26)</span> Jasper ♦♦</div></div><span id="60777"></span><div id="comment-60777" class="comment"><div id="post-60777-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your quick response.. It helps to answer some of my questions in dissecting tcpdumps</p></div><div id="comment-60777-info" class="comment-info"><span class="comment-age">(12 Apr '17, 12:22)</span> evgenia</div></div><span id="60791"></span><div id="comment-60791" class="comment"><div id="post-60791-score" class="comment-score"></div><div class="comment-text"><p>I realise now that reused connections in our particular case meant following:</p><p>We needed to see multiple "Application Data" packets coming from the source to the backend server within the same TCP Stream.</p></div><div id="comment-60791-info" class="comment-info"><span class="comment-age">(12 Apr '17, 18:25)</span> evgenia</div></div></div><div id="comment-tools-60759" class="comment-tools"></div><div class="clear"></div><div id="comment-60759-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


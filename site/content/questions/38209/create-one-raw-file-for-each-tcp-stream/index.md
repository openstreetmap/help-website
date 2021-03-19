+++
type = "question"
title = "Create one raw file for each TCP stream"
description = '''I would like to use tshark or some other tool for listening on a network interface, and generate a file for each TCP/UDP stream containing the raw stream data (the same thing I get with &quot;follow stream&quot; in wireshark).  I can do a similar thing using tcpflow. The problem of tcpflow is that it splits t...'''
date = "2014-11-27T05:38:00Z"
lastmod = "2014-11-27T05:38:00Z"
weight = 38209
keywords = [ "udp", "tshark", "stream", "tcp" ]
aliases = [ "/questions/38209" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Create one raw file for each TCP stream](/questions/38209/create-one-raw-file-for-each-tcp-stream)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38209-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I would like to use tshark or some other tool for listening on a network interface, and generate a file for each TCP/UDP stream containing the raw stream data (the same thing I get with "follow stream" in wireshark).</p><p>I can do a similar thing using tcpflow. The problem of tcpflow is that it splits the TCP stream in two files: one for each endpoint. So if I capture an HTTP request, I can find the GET in one file, and the 200 OK in another. I want them in the same one.</p><p>I can also do a similar thing using tshark like shown <a href="https://ask.wireshark.org/questions/4677/easy-way-to-save-tcp-streams">here</a>, but only works for existing pcap files, not for live traffic.</p></div><div id="question-tags" class="tags-container tags">udp tshark stream tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Nov '14, 05:38</strong></p><img src="https://secure.gravatar.com/avatar/9dd986107a5f408f063b3c8221a75ffd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Otacon22&#39;s gravatar image" /><p>Otacon22<br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Otacon22 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 27 Nov '14, 05:39</p></div></div><div id="comments-container-38209" class="comments-container"></div><div id="comment-tools-38209" class="comment-tools"></div><div class="clear"></div><div id="comment-38209-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>


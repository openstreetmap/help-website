+++
type = "question"
title = "Connection reset after &quot;Previous segment not captured&quot;"
description = '''I have a Docker container running on a virtual machine and I&#x27;m trying to upload a file to S3 (or Google Cloud Storage, both with the same result) from inside it. While there are no problems for small files (&amp;lt;1MB), with larger ones the connection is reset by the remote end in the middle of the tra...'''
date = "2014-01-10T08:11:00Z"
lastmod = "2014-01-12T04:33:00Z"
weight = 28772
keywords = [ "reset", "iptables", "virtualbox" ]
aliases = [ "/questions/28772" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Connection reset after "Previous segment not captured"](/questions/28772/connection-reset-after-previous-segment-not-captured)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28772-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a Docker container running on a virtual machine and I'm trying to upload a file to S3 (or Google Cloud Storage, both with the same result) from inside it.</p><p>While there are no problems for small files (&lt;1MB), with larger ones the connection is reset by the remote end in the middle of the transfer and a Broken Pipe or Connection reset error is raised by the application.</p><p>If I execute exactly the same command from the virtual machine itself, everything works fine. The problem appears only when the command is run from inside the container. (Docker uses iptables to forward traffic, maybe that's the culprit).</p><p>I started measuring the traffic on the "docker0" interface from the virtual machine, and I noticed that the connection is reset shortly after each time that a "TCP Previous segment not captured" message occurs.</p><p>The capture is available at <a href="http://www.cloudshark.org/captures/77be48e86fc1">http://www.cloudshark.org/captures/77be48e86fc1</a> can somebody explain me why this happens and what can I do to solve this situation?</p></div><div id="question-tags" class="tags-container tags">reset iptables virtualbox</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Jan '14, 08:11</strong></p><img src="https://secure.gravatar.com/avatar/0340081d861ced6802ff4861313bbc55?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GaretJax&#39;s gravatar image" /><p>GaretJax<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GaretJax has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 12 Jan '14, 03:27</p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-28772" class="comments-container"><span id="28811"></span><div id="comment-28811" class="comment"><div id="post-28811-score" class="comment-score"></div><div class="comment-text"><p>There is no trace at that URL.</p></div><div id="comment-28811-info" class="comment-info"><span class="comment-age">(12 Jan '14, 03:00)</span> Jasper ♦♦</div></div><span id="28812"></span><div id="comment-28812" class="comment"><div id="post-28812-score" class="comment-score"></div><div class="comment-text"><p>Please try again now</p></div><div id="comment-28812-info" class="comment-info"><span class="comment-age">(12 Jan '14, 03:28)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-28772" class="comment-tools"></div><div class="clear"></div><div id="comment-28772-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28813"></span>

<div id="answer-container-28813" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28813-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Packets 377-380 are written out of order into the pcap file. The timestamps of those are earlier than 374-376, which can only mean they were 'timestamped' correctly. If the trace was taken in the VM (virtualbox) tracing docker0 interface then it is probably the VM that is also forwarding them out_of_order to then next hop. The receiving TCP (one hop away - so probably not S3 but some proxy software in your host OS) is responding by acking 1-byte segments 610338,610339,610340,610341,610342,610343 with a RTT of 2ms. Soon after that the RST arrives with a TTL of 254, so again must be coming from the TCP layer 1 hop away (TCP in your VM host system?)</p><p>I'd suggest you continue to analyze there ...</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Selection_028.png" alt="alt text" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jan '14, 04:33</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></img></div></div><div id="comments-container-28813" class="comments-container"><span id="36041"></span><div id="comment-36041" class="comment"><div id="post-36041-score" class="comment-score"></div><div class="comment-text"><p>We hit a similar issue with running an HTTP server in a container and reported it as a Docker issue a while back (3089). Did you find a solution to your flavor of the problem? Any information you can share would be much appreciated.</p><p>(Tried to add this as a comment, but the site keeps marking it as spam, no matter what I do.)</p></div><div id="comment-36041-info" class="comment-info"><span class="comment-age">(06 Sep '14, 06:26)</span> parente</div></div><span id="36462"></span><div id="comment-36462" class="comment"><div id="post-36462-score" class="comment-score"></div><div class="comment-text"><p>I'm sorry @parente, I gave up, moved the registry from google cloud to brightbox and everything started working correctly (note that storage is still on S3).</p></div><div id="comment-36462-info" class="comment-info"><span class="comment-age">(19 Sep '14, 09:46)</span> GaretJax</div></div></div><div id="comment-tools-28813" class="comment-tools"></div><div class="clear"></div><div id="comment-28813-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


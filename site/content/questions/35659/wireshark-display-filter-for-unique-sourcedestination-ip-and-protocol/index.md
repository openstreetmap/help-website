+++
type = "question"
title = "Wireshark Display Filter for Unique Source/Destination IP and Protocol"
description = '''I need to create a display filter that does the following: For each source IP address, list all destination IP addresses, but only list unique protocols for each destination IP address. In other words, I want to see only one row of data for each unique:  ip.src = X, ip.dst = Y, protocol = Z I&#x27;d like...'''
date = "2014-08-21T13:03:00Z"
lastmod = "2014-08-25T12:47:00Z"
weight = 35659
keywords = [ "tshark", "wireshark" ]
aliases = [ "/questions/35659" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Wireshark Display Filter for Unique Source/Destination IP and Protocol](/questions/35659/wireshark-display-filter-for-unique-sourcedestination-ip-and-protocol)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35659-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I need to create a display filter that does the following: For each source IP address, list all destination IP addresses, but only list unique protocols for each destination IP address.</p><p>In other words, I want to see only one row of data for each unique: ip.src = X, ip.dst = Y, protocol = Z</p><p>I'd like to create this filter such that it covers all source IPs, so I don't have to create a separate filter for each source IP address.</p><p>I need to do the above for many PCAP files in "batch" mode. If this cannot be done in the Wireshark GUI, then I would like a command-line (tshark) solution.</p></div><div id="question-tags" class="tags-container tags">tshark wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Aug '14, 13:03</strong></p><img src="https://secure.gravatar.com/avatar/08f929285ad175fa9725b00e9fb7d1be?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="moving2&#39;s gravatar image" /><p>moving2<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="moving2 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 21 Aug '14, 13:08</p></div></div><div id="comments-container-35659" class="comments-container"></div><div id="comment-tools-35659" class="comment-tools"></div><div class="clear"></div><div id="comment-35659-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35722"></span>

<div id="answer-container-35722" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35722-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I think you'll have to use <code>tshark</code> for this. One potential solution might be:</p><pre><code>`tshark -r file.pcap -Y ip -T fields -e ip.src -e ip.dst -e _ws.col.Protocol | sort | uniq`</code></pre><p>Note: If you want protocol numbers instead of protocol names, substitute <code>-e ip.proto</code> for <code>_ws.col.Protocol</code>, or use both if you prefer that.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Aug '14, 12:47</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-35722" class="comments-container"></div><div id="comment-tools-35722" class="comment-tools"></div><div class="clear"></div><div id="comment-35722-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


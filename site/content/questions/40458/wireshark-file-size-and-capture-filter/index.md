+++
type = "question"
title = "Wireshark file size and capture filter"
description = '''I&#x27;m running a capture on a firewall from one side and on a server at the other to monitor AV update traffic. The server has a capture filter (not display filter) applied to capture traffic only from the firewall IP. Each wireshark capture file size is 300-400MB however when I go to the wireshark con...'''
date = "2015-03-11T01:56:00Z"
lastmod = "2015-03-11T01:56:00Z"
weight = 40458
keywords = [ "capture-filter" ]
aliases = [ "/questions/40458" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark file size and capture filter](/questions/40458/wireshark-file-size-and-capture-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40458-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm running a capture on a firewall from one side and on a server at the other to monitor AV update traffic. The server has a capture filter (not display filter) applied to capture traffic only from the firewall IP. Each wireshark capture file size is 300-400MB however when I go to the wireshark conversations in the 400MB file the biggest bytes count is 2MB on the server from my firewall to the server. Is this a case of wireshark is actually capturing all the traffic on the server hence the large file size but only displaying what is specified in the capture filter or is the server getting 300-400MB of traffic from the firewall that's not showing up in conversations. Thanks.</p></div><div id="question-tags" class="tags-container tags">capture-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Mar '15, 01:56</strong></p><img src="https://secure.gravatar.com/avatar/68ce515bc08f1da09ed2200c8aca252c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Costello&#39;s gravatar image" /><p>Costello<br />
<span class="score" title="30 reputation points">30</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Costello has no accepted answers">0%</span></p></div></div><div id="comments-container-40458" class="comments-container"><span id="40463"></span><div id="comment-40463" class="comment"><div id="post-40463-score" class="comment-score"></div><div class="comment-text"><p>please post the following screenshots.</p><ul><li>Statistics --&gt; Summary</li><li>Statistics --&gt; Conversations</li><li>Statistics --&gt; Conversations --&gt; TCP</li></ul></div><div id="comment-40463-info" class="comment-info"><span class="comment-age">(11 Mar '15, 03:28)</span> Kurt Knochner ♦</div></div><span id="40521"></span><div id="comment-40521" class="comment"><div id="post-40521-score" class="comment-score"></div><div class="comment-text"><p>Apologies I can't post due to IP's being displayed. I have discovered an error in my findings anyway. Thank you for replying.</p></div><div id="comment-40521-info" class="comment-info"><span class="comment-age">(12 Mar '15, 14:46)</span> Costello</div></div></div><div id="comment-tools-40458" class="comment-tools"></div><div class="clear"></div><div id="comment-40458-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>


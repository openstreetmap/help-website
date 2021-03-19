+++
type = "question"
title = "Fog Server slow to respond during peak office hours."
description = '''We are running an internal Fog server with address 10.X.X.X and when we try logging into it between the hours of 8am-4pm, we are seeing sluggish response times. Ran wireshark and saw lots of SYN/ACK packets and at one point I see an RST packet then a RETRANSMISSION. I don&#x27;t even know where to start ...'''
date = "2011-10-26T12:46:00Z"
lastmod = "2011-10-26T12:46:00Z"
weight = 7088
keywords = [ "fog", "server" ]
aliases = [ "/questions/7088" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Fog Server slow to respond during peak office hours.](/questions/7088/fog-server-slow-to-respond-during-peak-office-hours)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7088-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We are running an internal Fog server with address 10.X.X.X and when we try logging into it between the hours of 8am-4pm, we are seeing sluggish response times. Ran wireshark and saw lots of SYN/ACK packets and at one point I see an RST packet then a RETRANSMISSION. I don't even know where to start to look. The reset packet, as well as all the others say Header Checksum: 0x0000 incorrect, should be...(different numbers). Maybe caused by IP Checksum offload. Does any of this help?</p><p>thank you RM</p><p>update: after looking at Fog server as src, noticed it was sending an RST with following attributes:</p><p>Length: 60, Port: random, Seq=1, Win=0, Len=0 (If that helps?)</p></div><div id="question-tags" class="tags-container tags">fog server</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Oct '11, 12:46</strong></p><img src="https://secure.gravatar.com/avatar/ad752e419882af61ef26606d035eb8e2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rmjrtx&#39;s gravatar image" /><p>rmjrtx<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rmjrtx has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Oct '11, 14:13</p></div></div><div id="comments-container-7088" class="comments-container"></div><div id="comment-tools-7088" class="comment-tools"></div><div class="clear"></div><div id="comment-7088-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>


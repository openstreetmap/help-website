+++
type = "question"
title = "inconsistent Throughput, RTT, packet loss on TCP service (FTP)"
description = '''Hi, currently I do a routing simulation on GNS3 with FTP as reliable service and Video streaming as unreliable service together. I&#x27;m using 4 different scenario on routing: no link down, 1 link down, 2 link down, and 3 link down on every route that used to send packet. Theoretically, the more link do...'''
date = "2014-05-07T19:32:00Z"
lastmod = "2014-05-07T19:32:00Z"
weight = 32630
keywords = [ "ftp" ]
aliases = [ "/questions/32630" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [inconsistent Throughput, RTT, packet loss on TCP service (FTP)](/questions/32630/inconsistent-throughput-rtt-packet-loss-on-tcp-service-ftp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32630-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, currently I do a routing simulation on GNS3 with FTP as reliable service and Video streaming as unreliable service together. I'm using 4 different scenario on routing: no link down, 1 link down, 2 link down, and 3 link down on every route that used to send packet. Theoretically, the more link down the QoS or data will get worse, for example QoS with no link down will be better (higher throughput, less packet loss, and less delay/RTT) rather than 3 link down (in reverse). The Video streaming result is come with correct result, I mean with it supposed to be. But the FTP result didn't come as I hope, the throughput, RTT, and packet loss has inconsistent result on every scenario. Sometimes 1st scenario is worse than 2nd scenario, or 4st scenario is better than 2nd scenario. Is it normal or TCP service actually doesn't affected by how often link dropped even the link is used to route packet?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">ftp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 May '14, 19:32</strong></p><img src="https://secure.gravatar.com/avatar/d5396afc8eb22685854556215342ec5c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Aldindha&#39;s gravatar image" /><p>Aldindha<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Aldindha has no accepted answers">0%</span></p></div></div><div id="comments-container-32630" class="comments-container"><span id="32676"></span><div id="comment-32676" class="comment"><div id="post-32676-score" class="comment-score"></div><div class="comment-text"><p>I'm sorry, but I don't fully understand your different scenarios. As nobody else answered, I'm probably not the only one.</p><p>Please add or more details or a better description of your 'problem'.</p><p>What do you mean exactly be "2 link down" or "3 link down", or more generally, how does your setup look like?</p></div><div id="comment-32676-info" class="comment-info"><span class="comment-age">(09 May '14, 11:37)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-32630" class="comment-tools"></div><div class="clear"></div><div id="comment-32630-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>


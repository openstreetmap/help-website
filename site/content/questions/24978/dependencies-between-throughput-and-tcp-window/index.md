+++
type = "question"
title = "Dependencies between throughput and TCP window"
description = '''Hi, I have observed an interesting throughput pattern when testing two different WiFi access points &amp;amp; Windows7. In both cases the radio link is perfect. FTP download throughput is always around 50% lower on one of the APs (40 vs 20Mbps). Both APs show no dup-acks or retransmissions. Link is just...'''
date = "2013-09-19T18:31:00Z"
lastmod = "2013-09-19T18:31:00Z"
weight = 24978
keywords = [ "window", "tcp", "size" ]
aliases = [ "/questions/24978" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Dependencies between throughput and TCP window](/questions/24978/dependencies-between-throughput-and-tcp-window)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24978-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I have observed an interesting throughput pattern when testing two different WiFi access points &amp; Windows7. In both cases the radio link is perfect. FTP download throughput is always around 50% lower on one of the APs (40 vs 20Mbps).</p><p>Both APs show no dup-acks or retransmissions. Link is just perfect. The difference is that when the faster AP is used TCP window keeps increasing all the the to 1.5Mbytes, while on the slower AP the TCP window increases to 200kbytes and stays at this level.</p><p>Other differences are: Fast AP - TCP SYNC time around 40ms - Maximum segment size - 1442</p><p>Slow AP - TCP SYNC time around 30ms - Maximum segment size - 1414</p><p>Any suggestions?</p><p>Cheers, Amebcia</p></div><div id="question-tags" class="tags-container tags">window tcp size</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Sep '13, 18:31</strong></p><img src="https://secure.gravatar.com/avatar/4f57b04a65017ec2d96d14a909bb74ce?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="amebcia&#39;s gravatar image" /><p>amebcia<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="amebcia has no accepted answers">0%</span></p></div></div><div id="comments-container-24978" class="comments-container"><span id="24982"></span><div id="comment-24982" class="comment"><div id="post-24982-score" class="comment-score"></div><div class="comment-text"><p>can you please post the two capture files somewhere (google docs, dropbox, cloudshark)?</p></div><div id="comment-24982-info" class="comment-info"><span class="comment-age">(20 Sep '13, 00:49)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-24978" class="comment-tools"></div><div class="clear"></div><div id="comment-24978-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>


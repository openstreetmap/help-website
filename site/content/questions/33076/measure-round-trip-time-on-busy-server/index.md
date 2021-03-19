+++
type = "question"
title = "Measure round trip time on busy server"
description = '''Hi I am still new to Wireshark but I think that this should be an easy one:&#92; How can I monitor from a busy server (many GB of data/h) over an extended period of time (6h at least) the RTT times?  Since the data volume is massive I cannot store all sent data on disc. I am searching for latency issues...'''
date = "2014-05-26T02:41:00Z"
lastmod = "2014-05-26T02:41:00Z"
weight = 33076
keywords = [ "rtt" ]
aliases = [ "/questions/33076" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Measure round trip time on busy server](/questions/33076/measure-round-trip-time-on-busy-server)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33076-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi I am still new to Wireshark but I think that this should be an easy one:\</p><p>How can I monitor from a busy server (many GB of data/h) over an extended period of time (6h at least) the RTT times?</p><p>Since the data volume is massive I cannot store all sent data on disc. I am searching for latency issues where RTT &gt; 0.1s. Ideally I would like to start a live capture and keep only the packets in memory which have such high RTT times to analyze later customer complaints with the monitored RTT times if the problems were network related or not. I have seen nice display filters like tcp.analysis.ack_rtt&gt;0.1 which would do exactly that but when I look at the memory consumption of wireshark I see a steady increase which would bring down the server quite soon.</p><p>I have hoped that capture filters would help me to keep only the relevant packages which match the filter. Is this possible somehow? In general an option in Wireshark that drops all not visible packets would be great to achive that. If the feature is already there I would love to hear how I can use it.</p></div><div id="question-tags" class="tags-container tags">rtt</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 May '14, 02:41</strong></p><img src="https://secure.gravatar.com/avatar/9432d8dab23758894913ff56e3836f8b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="akraus1&#39;s gravatar image" /><p>akraus1<br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="akraus1 has no accepted answers">0%</span></p></div></div><div id="comments-container-33076" class="comments-container"></div><div id="comment-tools-33076" class="comment-tools"></div><div class="clear"></div><div id="comment-33076-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>


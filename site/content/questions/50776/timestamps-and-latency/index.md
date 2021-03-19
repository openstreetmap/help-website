+++
type = "question"
title = "Timestamps and Latency."
description = '''Hi, I am running a captures on my PC of a SSL transfer to a server about 14 hops away. ICMP gives me an average roundtrip time in the order of 160ms. But when looking at this through wireshark 1.12.9, it appears the displayed time delta averages about 200 Microseconds. This seems consistent througho...'''
date = "2016-03-09T00:10:00Z"
lastmod = "2016-03-09T00:10:00Z"
weight = 50776
keywords = [ "timestamp", "latency" ]
aliases = [ "/questions/50776" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Timestamps and Latency.](/questions/50776/timestamps-and-latency)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50776-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am running a captures on my PC of a SSL transfer to a server about 14 hops away. ICMP gives me an average roundtrip time in the order of 160ms.</p><p>But when looking at this through wireshark 1.12.9, it appears the displayed time delta averages about 200 Microseconds. This seems consistent throughout the capture (I use the IO graph). This time value seems impossibly small given the distance between the nodes. I have max latency values of 100ms and min values of 10microseconds in this set of data. When calculating max, min and average are calculated through the IO graph (with a DISPLAY FILTER in the main window restricting it to the TCP conversation).</p><p>Additionally the conversation seems to be tit for tat, i.e one packet sent for me, then one from the server and the pattern repeats (I was thinking maybe my results were due to consecutive server transmits, but the Seq and Ack values make sense for these packets in sequence with incredibly small latency).</p><p>Could this be an issue with my PC mucking up the timestamps for sub millisecond values?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">timestamp latency</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Mar '16, 00:10</strong></p><img src="https://secure.gravatar.com/avatar/98bd18a6f957c01c4ae2acf420bee185?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Edward%20Teach&#39;s gravatar image" /><p>Edward Teach<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Edward Teach has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Mar '16, 00:14</p></div></div><div id="comments-container-50776" class="comments-container"><span id="50778"></span><div id="comment-50778" class="comment"><div id="post-50778-score" class="comment-score"></div><div class="comment-text"><p>It would be easier to understand what is the issue if you could post the capture (maybe after shaving away the payload using tracewrangler if you are afraid of data leakage), but is there any NAT or proxy device between the session client and server or are all the intermediate devices just routers? Also, a capture taken simultaneously at the client and server side could bring more light.</p></div><div id="comment-50778-info" class="comment-info"><span class="comment-age">(09 Mar '16, 00:27)</span> sindy</div></div></div><div id="comment-tools-50776" class="comment-tools"></div><div class="clear"></div><div id="comment-50776-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>


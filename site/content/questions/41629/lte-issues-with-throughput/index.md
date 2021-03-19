+++
type = "question"
title = "LTE issues with throughput"
description = '''Hi to all,  I am curently working on troubleshooting e2e issues on LTE. So I use wireshark logs for analysis. I am quete new in this, so all the help would be welcome. I have issues with limiting DL throughput. RTT is ok, so there is not any additional delays, but flight size drops happen all the ti...'''
date = "2015-04-21T06:21:00Z"
lastmod = "2015-04-21T07:34:00Z"
weight = 41629
keywords = [ "throughput", "lte" ]
aliases = [ "/questions/41629" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [LTE issues with throughput](/questions/41629/lte-issues-with-throughput)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41629-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi to all, I am curently working on troubleshooting e2e issues on LTE. So I use wireshark logs for analysis. I am quete new in this, so all the help would be welcome. I have issues with limiting DL throughput. RTT is ok, so there is not any additional delays, but flight size drops happen all the time. I use some matlab tool for this analysis to generate some graphs (see the figure below to see the situation). This is the receiver side. It seems that there are some IP loss, but having a deeper look in the logs in wireshark it seems that IP loss is not the real cause of the low flight size which limit the throughput. There are a lot of Dup ACK which couse retransmissions, but even whan there aren't retransmission, flight size still drops.</p><p>Any ideas or experiance to share what is actually the problem here?</p><p>I could upload the log if you are that kind to have a look at it.</p><p>BR, coMI <img src="https://osqa-ask.wireshark.org/upfiles/server_820_329_nZsjP09.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">throughput lte</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Apr '15, 06:21</strong></p><img src="https://secure.gravatar.com/avatar/e537ac098228d3b1870464d6c1d7dc21?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="coMi&#39;s gravatar image" /><p>coMi<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="coMi has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 22 Apr '15, 05:29</p></div></div><div id="comments-container-41629" class="comments-container"></div><div id="comment-tools-41629" class="comment-tools"></div><div class="clear"></div><div id="comment-41629-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41634"></span>

<div id="answer-container-41634" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41634-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I've done LTE throughput troubleshooting before, and usually this has been a buffer bloat problem. It happens when high speed links are switched/routed to lower speed links, causing the device to buffer packets (and starting to drop at some point).</p><p>An indicator I have often seen is that as soon as the buffers are hit with 100 kbyte in flight you'll see packet loss, because this seems to be a common buffer size for network devices (per port, I guess). So the buffer fills up to the maximum and has to drop because more and more is coming in.</p><p>It can go as bad as seeing 1/10th of the theoretical maximum throughput, caused by the delay until the retransmission has a chance to get through the clogged device. The cause for this is that the receiving device advertises a TCP window size that is too large, resulting in the sender pushing out tons of data which overloads the infrastructure (some LTE device drivers seem to use hard coded 4MB TCP window sizes, which is absolutely deadly in heterogeneous networks).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Apr '15, 07:34</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 21 Apr '15, 07:37</p></div></div><div id="comments-container-41634" class="comments-container"><span id="41672"></span><div id="comment-41672" class="comment"><div id="post-41672-score" class="comment-score"></div><div class="comment-text"><p>First of all, thanks Jasper, I appreciate your help. The first part of the the answer makes sense. Probably the bottleneck is somewhere in transport part of the network, so there are some limiting links that doesn't let flighsize to grow. One more question. I have filtered that duplicated ACKs with high counter numbers (over 70, so packet loss for sure) are actually connected with the specific source port numbers, or this is something Does this tell us that ports are actually bottleneck and how thay can be found in the network? I am a radio engineer, so I quite new in transport troubleshooting of the network.</p><p>Thanks, coMi</p></div><div id="comment-41672-info" class="comment-info"><span class="comment-age">(22 Apr '15, 04:53)</span> coMi</div></div><span id="41673"></span><div id="comment-41673" class="comment"><div id="post-41673-score" class="comment-score"></div><div class="comment-text"><p>I can't really tell from the information you have given, but what I've seen many times is UL latency, caused by delays in getting UL grants from the scheduler in the eNodeB. If you can get a MAC/RLC/PDCP log (at either end of the link), or just the IP traffic at or beyond the eNodeB, you could check the TCP ACKs being sent in the uplink. If you see big bunches of them received close together in time, then check the TCP timestamps in the options (if present), and I expect you'll see they were more spread out in time. Obviously the closer to the eNodeB, the surer you can be that they originated over the air interface.</p></div><div id="comment-41673-info" class="comment-info"><span class="comment-age">(22 Apr '15, 05:14)</span> MartinM</div></div><span id="41676"></span><div id="comment-41676" class="comment"><div id="post-41676-score" class="comment-score"></div><div class="comment-text"><p>Duplicate ACKs are simply telling you that there is a gap (meaning, packet loss), and the higher the dup ack count the longer the gap existed. This means that a lot of packets arrived before the retransmission finally made it through. Most LAN networks have dup ack counts less than a dozen, but with buffer bloat the numbers usually go much higher. The highest I had on an LTE test setup suffering from massive buffer bloating was a dup ack count over 1000.</p><p>Finding ports that are overloaded is usually done by looking at the switch console. The admins should be able which port is in trouble; it's not possible to do this from packets because you often do not know which path they take on the network.</p></div><div id="comment-41676-info" class="comment-info"><span class="comment-age">(22 Apr '15, 05:41)</span> Jasper ♦♦</div></div></div><div id="comment-tools-41634" class="comment-tools"></div><div class="clear"></div><div id="comment-41634-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


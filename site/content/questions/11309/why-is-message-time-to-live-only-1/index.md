+++
type = "question"
title = "Why is message Time To Live only 1?"
description = '''About half of my packets are window size 32768 and TTL = 64, which is what I would expect. I&#x27;m on a dedicated VLAN for iSCSI. The other half of my packets are window size 524 and TTL = 1. All these packets come from one host. Like I said, this is a dedicated non-routed VLAN. The customer is experien...'''
date = "2012-05-24T06:15:00Z"
lastmod = "2012-05-25T10:03:00Z"
weight = 11309
keywords = [ "analysis" ]
aliases = [ "/questions/11309" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Why is message Time To Live only 1?](/questions/11309/why-is-message-time-to-live-only-1)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11309-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>About half of my packets are window size 32768 and TTL = 64, which is what I would expect. I'm on a dedicated VLAN for iSCSI. The other half of my packets are window size 524 and TTL = 1. All these packets come from one host. Like I said, this is a dedicated non-routed VLAN. The customer is experiencing latency issues across the board from several hosts. I'll be getting a network capture from a second host today.</p></div><div id="question-tags" class="tags-container tags">analysis</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 May '12, 06:15</strong></p><img src="https://secure.gravatar.com/avatar/a472d068843eefd8a4ef69c4f94e4160?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gipper&#39;s gravatar image" /><p>gipper<br />
<span class="score" title="30 reputation points">30</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gipper has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 May '12, 10:41</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-11309" class="comments-container"><span id="11310"></span><div id="comment-11310" class="comment"><div id="post-11310-score" class="comment-score"></div><div class="comment-text"><p>...and your question is what exactly? :-)</p><p>You should either provide a trace (keep in mind that you might expose sensitive data) via <a href="http://www.cloudshark.org">www.cloudshark.org</a>, or tell us more about your observations. For example: what host is sending the TTL 1 packets, what protocol is it, which direction (to client, to server) etc.</p></div><div id="comment-11310-info" class="comment-info"><span class="comment-age">(24 May '12, 06:26)</span> Jasper ♦♦</div></div><span id="11312"></span><div id="comment-11312" class="comment"><div id="post-11312-score" class="comment-score"></div><div class="comment-text"><p>I suggest to do either of these:</p><ol><li><p>check your routing infrastructure in the iSCSI "subnet". According to your description it's just a flat net within one VLAN, however: never trust any assumptions, so better check ;-)</p></li><li><p>figure out the vendor of that device and contact their support (regarding the TTL and the window size). Maybe they already know this (bug or something)</p></li><li><p>As @Jasper said: if you can provide a capture sample, we might be able to help.</p></li></ol><p>Regards<br />
Kurt</p></div><div id="comment-11312-info" class="comment-info"><span class="comment-age">(24 May '12, 07:39)</span> Kurt Knochner ♦</div></div><span id="11313"></span><div id="comment-11313" class="comment"><div id="post-11313-score" class="comment-score"></div><div class="comment-text"><p>Not sure how to attach my trace export file</p></div><div id="comment-11313-info" class="comment-info"><span class="comment-age">(24 May '12, 08:02)</span> gipper</div></div><span id="11314"></span><div id="comment-11314" class="comment"><div id="post-11314-score" class="comment-score"></div><div class="comment-text"><ol><li><p>You can upload it to <a href="http://cloudshark.org">cloudshark.org</a>. BEWARE: You cannot delete an uploaded file.</p></li><li><p>You can use a one-click file hoster (search google) to upload the file and then post the link. <a href="http://netload.in">http://netload.in</a> seems to be acceptable in terms of user annoyance and ads.</p></li></ol></div><div id="comment-11314-info" class="comment-info"><span class="comment-age">(24 May '12, 08:49)</span> Kurt Knochner ♦</div></div><span id="11333"></span><div id="comment-11333" class="comment"><div id="post-11333-score" class="comment-score"></div><div class="comment-text"><p>I uploaded some of the capture. Had to cut it in to pieces due to 10MB size limit. <a href="http://cloudshark.org/captures/2b1890434ed9">http://cloudshark.org/captures/2b1890434ed9</a> Look at frame 1.</p></div><div id="comment-11333-info" class="comment-info"><span class="comment-age">(25 May '12, 08:43)</span> gipper</div></div></div><div id="comment-tools-11309" class="comment-tools"></div><div class="clear"></div><div id="comment-11309-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="11334"></span>

<div id="answer-container-11334" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11334-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The trace is a bit problematic since there is lots of packets missing from it, and not so many big packets at all. I guess most large packets were coming in too fast and too big to be captured by your capture device...</p><p>Anyway, working with what we have, here's what I think:</p><ol><li><p>The TTL = 1 is uncommon, but a reason could be that the system using it wants to make sure that the packet is not routed, because that isn't exactly something you want to happen when talking to a storage array with as little latency as possible. I just checked with my own ESX servers talking to an iSCSI SAN (using the software iSCSI adapter) to see if it does the same, but it uses a TTL of 64, so it's not a default to have TTL 1.</p></li><li><p>Regarding the Window size - unfortunately there is no TCP Session Start (SYN SYN/ACK ACK), so we do not know if Window Scaling was negotiated. Usually when I see a window hovering around a value of 500 bytes (or in this case, staying dead center on 524 bytes) it is because there was a scale factor negotiated, usually 8. Which would mean that the window size needs to be multiplied by 256. But one can't say for sure unless you capture a session start. Also, it doesn't look like the other node is sending back chunks of 524 bytes, but some larger packets as well (above 1000 bytes), even when it's rare. Which is probably due to packet loss problems on the capture device.</p></li></ol><p>Preliminary verdict: I doubt the TTL is a problem. Also, the window size is too constant and the other node is sending more data than it would if the window size would not have to be scaled. But this is something that needs verification, and without packet loss on capture (a.k.a. "drops"). So you probably need a capable gigabit capture solution.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 May '12, 09:12</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span> </br></p></div></div><div id="comments-container-11334" class="comments-container"><span id="11337"></span><div id="comment-11337" class="comment"><div id="post-11337-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the reply. I'm having some ICMP issues longe reply times since I investigated further. So I'm waiting for the customer to capture a trace of this. I figure I need to work at this layer first and correct the problems there. What capture filter would I use to get the syn syn/ack ack?</p></div><div id="comment-11337-info" class="comment-info"><span class="comment-age">(25 May '12, 10:04)</span> gipper</div></div><span id="11373"></span><div id="comment-11373" class="comment"><div id="post-11373-score" class="comment-score"></div><div class="comment-text"><p>You could use a filter like "tcp[tcpflags] &amp; tcp-syn != 0" to get all packets with a SYN flag. Those are the ones containing the Window Scaling parameters.</p></div><div id="comment-11373-info" class="comment-info"><span class="comment-age">(26 May '12, 06:05)</span> Jasper ♦♦</div></div></div><div id="comment-tools-11334" class="comment-tools"></div><div class="clear"></div><div id="comment-11334-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="11336"></span>

<div id="answer-container-11336" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11336-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I also believe the trace is problematic, however due to other reasons:</p><ol><li><p>If you select tcp.stream 0 you see a lot of ACK packages for "unseen" data. Possible causes are:</p><ul><li>the data is coming in to fast and your capture device is dropping it (as @Jasper said).</li><li>your capture setup might be faulty, e.g. capturing only on one physical interface of an aggregated link (LACP / "Adapter Teaming" on your ESX server). How did you capture the data?</li></ul></li><li><p>If you look at <code>tcp.stream eq 2</code> and <code>tcp.stream eq 3</code> there is virtually unidirectional TCP communication for 18 seconds. That's traffic from one src to one dst, no data the other way round. These packets are mostly ACKs, sometimes SCSI "commands". Where is the data that has been ACKed?</p></li></ol><p>This leads me to the conclusion, that your capture setup might be faulty. Please tell us more about how you captured the data.</p><p>Unless we can't trust the capture data, no assumptions can be made about the possible problems.</p><p>Regarding the TTL: Only one of your VMware servers seems to set the TTL=1. Is there any difference in the version of the VMWare software running on that host (10.1.10.121)?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 May '12, 10:03</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 May '12, 10:15</p></div></div><div id="comments-container-11336" class="comments-container"></div><div id="comment-tools-11336" class="comment-tools"></div><div class="clear"></div><div id="comment-11336-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


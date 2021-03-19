+++
type = "question"
title = "iSCSI Communication appears incorrect handshaking"
description = '''I have a customer that&#x27;s having performance problems. Looking at their trace it seems clear why.  See first 50 packets at link below. This pattern basically repeats itself. http://cloudshark.org/captures/68a28bf0fd38 client IP = 172.18.1.14 Storage IP = 172.18.1.15 All on same switch and same VLAN. ...'''
date = "2013-01-29T12:13:00Z"
lastmod = "2013-01-29T16:45:00Z"
weight = 18054
keywords = [ "push", "iscsi" ]
aliases = [ "/questions/18054" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [iSCSI Communication appears incorrect handshaking](/questions/18054/iscsi-communication-appears-incorrect-handshaking)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18054-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a customer that's having performance problems. Looking at their trace it seems clear why. See first 50 packets at link below. This pattern basically repeats itself. <a href="http://cloudshark.org/captures/68a28bf0fd38">http://cloudshark.org/captures/68a28bf0fd38</a></p><p>client IP = 172.18.1.14 Storage IP = 172.18.1.15 All on same switch and same VLAN. First of all the client sends a read LUN request in frame 8. This looks fine. But I'm not sure why he keeps sending ACKS. Then in frame 17 the storage sends back the data requested in the read. However, there's a few things to note here. 1) This ia an ACK to frame 8. 2) The PUSH bit is set. 3) The frame is not a full jumbo frame of 9014 bytes.</p><p>Normally what I see when iSCSI is working efficiently</p><p>Client sends a read LUN request. Next frame from storage is an ACK only from the storage (60 byte packet) no data Next frame from the storage is read data requested with full 9000 bytes. ACK bit is set but no push</p><p>The storage is capable of sending a larger frame. The largest it sends is 7583 bytes. But never a full 9000 bytes. And PUSH bit is set here as well.</p><p>I have some suspicions about the NIC on the client not acting correctly based on some cases I've had in the past where the delayed ACK wasn't working. But I would like more proof of what this network pattern is telling me.</p></div><div id="question-tags" class="tags-container tags">push iscsi</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Jan '13, 12:13</strong></p><img src="https://secure.gravatar.com/avatar/a472d068843eefd8a4ef69c4f94e4160?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gipper&#39;s gravatar image" /><p>gipper<br />
<span class="score" title="30 reputation points">30</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gipper has no accepted answers">0%</span></p></div></div><div id="comments-container-18054" class="comments-container"></div><div id="comment-tools-18054" class="comment-tools"></div><div class="clear"></div><div id="comment-18054-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="18063"></span>

<div id="answer-container-18063" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18063-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Sorry to rain on your parade, but I think your interpretation is a bit off. Lets see if I can bring some light into the matter here.</p><p>So, in frame 8 there is a read request, and then you do NOT see any data packets coming in from the server BUT the client increases it's acknowledge number in huge steps. For example you see that in frame 9 the relative ack number is 155697, while the relative ack number in frame 8 was 131121. That means that your client received 24576 bytes (155697-131121) between frame 8 and 9. Your trace does not contain the packets with those bytes, but when the client acknowledges them they MUST have been on the wire. In case you're wondering what "TCP ACKed unseen segment" means (starting in frame 19): it means exactly what I just explained - there were packets that are acknowledged but they're NOT in the trace.</p><p>Next question that will come up is "yeah, but why does this message only show up in frame 19, when there were already unseen packets before that?". Good question. Answer is: because your trace starts right in the middle, not at the SYN, and before frame 17 there NEVER was a data frame coming back, so Wireshark obviously only states "unseen segment" when it knows that it has at least seen one of them at all before. By the way, I think frame 17 only made it into the capture because it is not the full 9000 bytes. And it makes sense that PSH is set because it is the last remaining bytes of a larger chunk, most of which was sliced into 9000 byte segments. So it is the signal saying "this is it, process, please".</p><p>Final verdict: unfortunately, your trace is useless and cannot be used to diagnose any trouble of the iSCSI connection. Your capturing device was not fast enough to record the jumbo data frames to disk as they appeared, and only was able to write the small ACKs and the occasional non-full jumbo frame to disk. You cannot diagnose iSCSI - or any high bandwith shared storage protocol - with capture hardware that doesn't at least write 120MB/s to disk. Because that's what a full Gigabit link will slam your capturing NIC with if it is doing full throttle in one direction. It gets worse if you capture a Gigabit link with full throttle in both directions, because then you need to write about 240MB/s. So unless you captured with a fast RAID disk configuration or an SSD setup you're not fast enough. A laptop with a single non-SSD disk will never be fast enough for this if the storage system gets going at full speed.</p><p>Sorry for the bad news, but it's better to know when the captured data is no good than spending hours and hours trying to make sense of what isn't there.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Jan '13, 16:45</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 29 Jan '13, 16:48</p></div></div><div id="comments-container-18063" class="comments-container"><span id="18064"></span><div id="comment-18064" class="comment"><div id="post-18064-score" class="comment-score"></div><div class="comment-text"><p>On a side note - because that often happens with setups where a VMware virtualization host (in your case an ESX) connects to a iSCSI device: make sure that the customer understands the ESX virtual network loadbalancing strategies. It usually doesn't help to have multiple Gigabit cards aggregated to gain Speed, because if the communication is Single-ESX-VMKernel-IP to Single-Storage-IP you'll only be using ONE link all the time, while the others are doing nothing.</p><p>This might help (in case you need it): <a href="http://kensvirtualreality.wordpress.com/2009/04/05/the-great-vswitch-debate%E2%80%93part-3/">http://kensvirtualreality.wordpress.com/2009/04/05/the-great-vswitch-debate%E2%80%93part-3/</a></p></div><div id="comment-18064-info" class="comment-info"><span class="comment-age">(29 Jan '13, 16:55)</span> Jasper ♦♦</div></div><span id="18125"></span><div id="comment-18125" class="comment"><div id="post-18125-score" class="comment-score"></div><div class="comment-text"><blockquote><p>with capture hardware that doesn't at least write 120MB/s to disk.</p></blockquote><p>wouldn't it be sufficient to capture only the first 120-200 bytes of a frame to analyze performance problems (at least as a first shot), so a much lower disk I/O bandwidth would be needed?</p></div><div id="comment-18125-info" class="comment-info"><span class="comment-age">(30 Jan '13, 12:53)</span> Kurt Knochner ♦</div></div><span id="18126"></span><div id="comment-18126" class="comment"><div id="post-18126-score" class="comment-score"></div><div class="comment-text"><p>yes it would, good point. I just mentioned the write speed because the sample capture was taken with full frame size.</p></div><div id="comment-18126-info" class="comment-info"><span class="comment-age">(30 Jan '13, 12:56)</span> Jasper ♦♦</div></div></div><div id="comment-tools-18063" class="comment-tools"></div><div class="clear"></div><div id="comment-18063-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


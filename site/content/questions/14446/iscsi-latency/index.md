+++
type = "question"
title = "iSCSI Latency"
description = '''Hello, I have been working on a major issue in our enviroment since monday morning. We have a couple of iscsi san&#x27;s (equallogic) those are connected to a stack of 4 dell switches and then i have a couple of dell server running vmware esx. (i ever have it from windows btw..) Now i generate with IOmet...'''
date = "2012-09-22T03:35:00Z"
lastmod = "2012-09-22T03:35:00Z"
weight = 14446
keywords = [ "iscsi", "srt" ]
aliases = [ "/questions/14446" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [iSCSI Latency](/questions/14446/iscsi-latency)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14446-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I have been working on a major issue in our enviroment since monday morning. We have a couple of iscsi san's (equallogic) those are connected to a stack of 4 dell switches and then i have a couple of dell server running vmware esx. (i ever have it from windows btw..) Now i generate with IOmeter 64KB read's and i get a latency of +/-270MS.</p><p>So i opened cases with both vmware and dell. Dell is blaming the switches and vmware is blaming the san's.</p><p>I would like to know where the latency is generated. I have no idea if that is even possible to find out? But i thought wireshark would be the right tool for that.</p><p>I made a portgroup on esx with promiscuous mode enabled and installed a virtual machine with wireshark.</p><p>Beside that i created a spawn port on the switch to mirror all traffic of the switchport where the server is connected. I mirrored the traffic to a physical machine with wireshark installed.</p><p>Then i created a trace and while doing my IO test. After that i went to statistics and clicked conversations, used my conversation as a filter, went to statistics again, selected service response time and selected scsi. This showed me an average of 0.273 srt. So the same as my iometer results was telling me.</p><p>I also did exactly the same with a san port (mirrored it to the physical machine.)</p><p>So i see the same latency on the traces as in iomter. But how can i find out which device is generating this latency? I would be very greatfull if you can take the time to help me. Its a very serieus issue for us with big impact for our business..</p><p>Thanks...</p><p>Regards</p></div><div id="question-tags" class="tags-container tags">iscsi srt</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Sep '12, 03:35</strong></p><img src="https://secure.gravatar.com/avatar/677074bdad6906b7a6195e8ca5c9a89b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hdejongh&#39;s gravatar image" /><p>Hdejongh<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hdejongh has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 Sep '12, 03:35</p></div></div><div id="comments-container-14446" class="comments-container"><span id="14452"></span><div id="comment-14452" class="comment"><div id="post-14452-score" class="comment-score"></div><div class="comment-text"><p>Open up the trace in Wireshark and do "tcp.analysis.flags" And check out my Sharkfest 2012's "Deep Dive" presentation. If I had to guess, you are experiencing packet loss and lots of it. good luck.</p></div><div id="comment-14452-info" class="comment-info"><span class="comment-age">(22 Sep '12, 16:58)</span> hansangb</div></div><span id="14456"></span><div id="comment-14456" class="comment"><div id="post-14456-score" class="comment-score"></div><div class="comment-text"><p>if i first filter my conversation i have around 15 tcp acked unseen segments... nothing more.</p><p>I dont see any dropped frames in ESX or on the switch...</p></div><div id="comment-14456-info" class="comment-info"><span class="comment-age">(22 Sep '12, 22:40)</span> Hdejongh</div></div><span id="14470"></span><div id="comment-14470" class="comment"><div id="post-14470-score" class="comment-score"></div><div class="comment-text"><p>Huh...that's just the span port (mirror port) that's dropping the packet. Any chance you can post a snippet of your trace? in pcap not, txt output.</p></div><div id="comment-14470-info" class="comment-info"><span class="comment-age">(23 Sep '12, 17:11)</span> hansangb</div></div></div><div id="comment-tools-14446" class="comment-tools"></div><div class="clear"></div><div id="comment-14446-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>


+++
type = "question"
title = "Maxing out CPU, monitoring USB traffic on Windows?!"
description = '''Hello,  Trying to boil down my hardware choices on a small embedded project, I decided to test USB throughput correlating with CPU usage for: FullHD Webcam, Wireless AC capable USB adapter and USB 3.0 capable FlashDrive, or HDD. As input for analysis I basically just need a I/O graph showing me how ...'''
date = "2016-08-08T14:54:00Z"
lastmod = "2016-08-08T16:36:00Z"
weight = 54676
keywords = [ "usbpcap" ]
aliases = [ "/questions/54676" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Maxing out CPU, monitoring USB traffic on Windows?!](/questions/54676/maxing-out-cpu-monitoring-usb-traffic-on-windows)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54676-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>Trying to boil down my hardware choices on a small embedded project, I decided to test USB throughput correlating with CPU usage for: FullHD Webcam, Wireless AC capable USB adapter and USB 3.0 capable FlashDrive, or HDD.</p><p>As input for analysis I basically just need a I/O graph showing me how much traffic is generated at a certain point in time, no need for in depth information. Is there an option to do just that? Problem: The fancy webcam generates 100Mb+/s, causing Wireshark to completely saturate the small CPU. In the end my readings are not accurate.</p><p>There are tools for HDD throughput and Wireless speed but for other USB devices like the webcam, I did not find a solution. If possible, it would also be great to do this with the same tool.</p><p>TIA, Matt</p></div><div id="question-tags" class="tags-container tags">usbpcap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Aug '16, 14:54</strong></p><img src="https://secure.gravatar.com/avatar/30a16d4455defff743b330ae1feed16b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="primergy&#39;s gravatar image" /><p>primergy<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="primergy has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Aug '16, 16:55</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-54676" class="comments-container"><span id="54678"></span><div id="comment-54678" class="comment"><div id="post-54678-score" class="comment-score"></div><div class="comment-text"><p>So does the CPU max out when capturing USB traffic with Wireshark, but not when capturing other traffic with Wireshark, so that it's probably an issue with USBPcap? Or is it an issue even when not capturing USB traffic, so that it's probably a Wireshark issue?</p></div><div id="comment-54678-info" class="comment-info"><span class="comment-age">(08 Aug '16, 16:58)</span> Guy Harris ♦♦</div></div><span id="54684"></span><div id="comment-54684" class="comment"><div id="post-54684-score" class="comment-score"></div><div class="comment-text"><p>@Guy Harris,</p><ul><li><p>my laptop's hardware seems to be a bit more powerful than the one of @primergy's fanless micro board, yet it starts sweating each time I start a live capture at any of the three USB root hubs from Wireshark (i.e., using the extcap API) even if no traffic is present on that root hub. So complexity of the dissector is clearly not the source of the CPU load.</p></li><li><p>when running USBPcapCMD on much weaker hardware with embedded XP in the past, before it has been enhanced the extcap API, I haven't noticed any CPU load issues.</p></li></ul><p>Hence my suggestion to the OP.</p><p>Now since there was no acoustic indicator of CPU load on that old hardware running XP, unlike my laptop where the fan noise tells you immediately that something wrong is going on, I wasn't sure whether I haven't just missed the load to exist back then. So I've made a test just now on my laptop:</p><ul><li><p>running the USBPcapCMD on a silent root hub from the command line takes less than 0.05 % of CPU according to the Windows task manager,</p></li><li><p>if the capture at the same root hub is triggered from the Wireshark window, three instances of USBPcapCMD are running (any ideas why?), each taking about 28 % of CPU, while Wireshark's CPU use at that time is around 0.1 %.</p></li></ul><p>So my conclusion is that the USBPcapCMD has got an issue with handling of the named queue, yet I have no idea how to use that conclusion as I've seen the last message from @desowin many months ago. I can see that the USBPcap package has been updated between 2.0.1 and 2.0.4 but I don't know whether it was by @desowin or someone else.</p></div><div id="comment-54684-info" class="comment-info"><span class="comment-age">(09 Aug '16, 00:12)</span> sindy</div></div></div><div id="comment-tools-54676" class="comment-tools"></div><div class="clear"></div><div id="comment-54676-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54677"></span>

<div id="answer-container-54677" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54677-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you run Windows on the machine and thus use USBPcap, then yes, the CPU load is enormous and I cannot exactly say why. On linux, <code>tcpdump</code> on <code>usbmon</code> isn't nearly that heavy. But please try to run USBPcap as a standalone command line application writing the captured URBs to a pcap file rather than feeding Wireshark with them through the named pipe, you may get better results (at least because Wireshark wouldn't dissect the frames immediately).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Aug '16, 16:36</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-54677" class="comments-container"><span id="54680"></span><div id="comment-54680" class="comment"><div id="post-54680-score" class="comment-score"></div><div class="comment-text"><p>Sindy,</p><p>Spot on, I was not aware of the command line option! For the record: <a href="http://desowin.org/usbpcap/tour.html">http://desowin.org/usbpcap/tour.html</a></p><p>Guy Harris: I have not tried other traffic in Wireshark on the weak hardware but the issue sure becomes negligible when using USBPCap via command line. It does look like a Wireshark issue.</p><p>Config. example: OS: Win 10 ENT LTSB 64bit - CPU Intel N3700, 8GB memory, SSD</p></div><div id="comment-54680-info" class="comment-info"><span class="comment-age">(08 Aug '16, 17:03)</span> primergy</div></div><span id="54683"></span><div id="comment-54683" class="comment"><div id="post-54683-score" class="comment-score"></div><div class="comment-text"><p>As my comment turned out to be useful to resolve your issue, I've made it an Answer so that you (and nobody else) could Accept it (using the checkmark icom, <strong>not</strong> the thumbs up one) so that the Question would become highlighted in green to indicate to others that a useful Answer exists.</p><p>On the other hand, as your post was clearly not an Answer to your original Question, I've made it a comment.</p></div><div id="comment-54683-info" class="comment-info"><span class="comment-age">(08 Aug '16, 23:05)</span> sindy</div></div><span id="54709"></span><div id="comment-54709" class="comment"><div id="post-54709-score" class="comment-score"></div><div class="comment-text"><p>If the resulting file also takes long to open in wireshark it might be a dissector performance thing that might be interesting to look at or profile to see if anything can be improved. If so file a bug and attach a sample file.</p></div><div id="comment-54709-info" class="comment-info"><span class="comment-age">(09 Aug '16, 11:38)</span> Anders ♦</div></div><span id="54710"></span><div id="comment-54710" class="comment"><div id="post-54710-score" class="comment-score"></div><div class="comment-text"><p>@Anders, see my comment to the Question. If something urgently needs profiling it is the USBPcapCMD handling of the named pipe.</p></div><div id="comment-54710-info" class="comment-info"><span class="comment-age">(09 Aug '16, 11:52)</span> sindy</div></div><span id="54771"></span><div id="comment-54771" class="comment"><div id="post-54771-score" class="comment-score"></div><div class="comment-text"><p><a href="https://github.com/desowin/usbpcap/issues/32">An issue</a> filed on GitHub.</p></div><div id="comment-54771-info" class="comment-info"><span class="comment-age">(12 Aug '16, 06:01)</span> sindy</div></div></div><div id="comment-tools-54677" class="comment-tools"></div><div class="clear"></div><div id="comment-54677-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


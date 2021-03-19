+++
type = "question"
title = "capturing 5 gig of traffic using dumpcap on VM"
description = '''hi expert, we are in situation where we have to capture around 5 gig of traffic. we are going to build out VM and install wireshark package on it. using dumpcap, we plan to capture traffic and later analyze with wireshark. can anyone has doc which can steps through me how to setup capture using dump...'''
date = "2015-11-18T11:35:00Z"
lastmod = "2015-11-19T09:20:00Z"
weight = 47726
keywords = [ "dumpcap" ]
aliases = [ "/questions/47726" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [capturing 5 gig of traffic using dumpcap on VM](/questions/47726/capturing-5-gig-of-traffic-using-dumpcap-on-vm)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47726-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi expert,</p><p>we are in situation where we have to capture around 5 gig of traffic. we are going to build out VM and install wireshark package on it. using dumpcap, we plan to capture traffic and later analyze with wireshark. can anyone has doc which can steps through me how to setup capture using dumpcap on vm.</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">dumpcap</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Nov '15, 11:35</strong></p><img src="https://secure.gravatar.com/avatar/56308ca3a95cf204a91902233da192f0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anush&#39;s gravatar image" /><p>Anush<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anush has no accepted answers">0%</span></p></div></div><div id="comments-container-47726" class="comments-container"><span id="47746"></span><div id="comment-47746" class="comment"><div id="post-47746-score" class="comment-score"></div><div class="comment-text"><p>Is that 5 Gig/s or 5 Gig in total? Any why do you want to do the capturing in a VM??</p></div><div id="comment-47746-info" class="comment-info"><span class="comment-age">(19 Nov '15, 03:57)</span> Kurt Knochner ♦</div></div><span id="47749"></span><div id="comment-47749" class="comment"><div id="post-47749-score" class="comment-score"></div><div class="comment-text"><p>it's 5 Gig/s. we don't have any network capturing tool which can capture that much rate of data. so we decided to setup VM on existing esx host and install wireshark on it and do the capture using dumpcap. ESX host is directly connected to the network switch. we will configure the switch to capture the traffic on interested interface and send that stream to interface where ESX host is connected.<br />
</p><p>Thanks</p></div><div id="comment-47749-info" class="comment-info"><span class="comment-age">(19 Nov '15, 07:30)</span> Anush</div></div></div><div id="comment-tools-47726" class="comment-tools"></div><div class="clear"></div><div id="comment-47726-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47759"></span>

<div id="answer-container-47759" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47759-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>it's 5 Gig/s. we don't have any network capturing tool which can capture that much rate of data.</p></blockquote><p>I doubt that this will work, because if you want to capture the full frame size, your VM would have to write 500 Mbyte/s. If you want to capture only the first 100 bytes, it would much less than that, but then you can't look very deep into the frames.</p><p>Furthermore, putting such a high network IO load on a VM might lead to dropped frames in the vSwitch, so you won't see those frames in the capture file.</p><p>And finally, do you have a spare 10 Gig port on the Switch and on the VM host to capture 5 Gig/s? If not, it's going to become hard, because if you flood the productive VM host interface with the mirrored traffic as well, it could easily lead to an oversubscribing of that link.</p><p>There is nothing special you have to do to run dumcap in a VM. You just need an OS that offers Wireshark/dumpcap. So, Linux and Windows are good candidate. The problem will be network IO load for your VM host and disk IO load to write the pcap file.</p><p>But hey, give it a try. Maybe it works.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Nov '15, 09:20</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-47759" class="comments-container"><span id="47772"></span><div id="comment-47772" class="comment"><div id="post-47772-score" class="comment-score"></div><div class="comment-text"><p>Thanks Kurt for this explanation. I spoke to server guy and he said VM will use 10 gig pipe through the ESX host so he is not expecting any issue there. for writing disk, we will get 1 TB hard drive. and yes ESX host get connected to 10gig port on switch. I will keep you posted how it goes.</p><p>Thanks</p></div><div id="comment-47772-info" class="comment-info"><span class="comment-age">(19 Nov '15, 11:37)</span> Anush</div></div><span id="47774"></span><div id="comment-47774" class="comment"><div id="post-47774-score" class="comment-score"></div><div class="comment-text"><blockquote><p>we will get 1 TB hard drive.</p></blockquote><p>it's not about the size of the disk. It's about the write speed! Size comes later, if you need to run the capture for a longer period.</p><p>Would be interesting to know how this works and/or if it works at all.</p><p>Please keep in mind: If you see signs for packet loss in the resulting capture file, it could be caused by the capturing systems inability to capture and write all frames and not due to real packet loss on the network!!</p></div><div id="comment-47774-info" class="comment-info"><span class="comment-age">(19 Nov '15, 11:50)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-47759" class="comment-tools"></div><div class="clear"></div><div id="comment-47759-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


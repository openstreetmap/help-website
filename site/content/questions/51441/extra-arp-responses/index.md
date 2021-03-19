+++
type = "question"
title = "Extra ARP Responses"
description = '''Looking at a capture in which I see the following sequence repeated throughout:  1. an ARP request goes out  2. an ARP response comes back in.  3. The requestor then sends the packet it wanted to go to that destination, e.g., a UDP packet, so I can tell that it saw the ARP response.  4. Then, it app...'''
date = "2016-04-06T13:15:00Z"
lastmod = "2016-04-06T13:15:00Z"
weight = 51441
keywords = [ "arp", "switch", "multiple" ]
aliases = [ "/questions/51441" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Extra ARP Responses](/questions/51441/extra-arp-responses)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51441-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Looking at a capture in which I see the following sequence repeated throughout: 1. an ARP request goes out 2. an ARP response comes back in.<br />
3. The requestor then sends the packet it wanted to go to that destination, e.g., a UDP packet, so I can tell that it saw the ARP response.<br />
4. Then, it appears that the responder sends back the same ARP response (exact duplicate) several more times, ranging from 6 to 15 times, all in a short time window.<br />
</p><p>This appears to be happening for all devices on the network, regardless of type or manufacture. So I don't suspect a device stack problem, but a network issue. Could this be some network switch behavior?<br />
</p><p>We are having some communication reliability issues with our equipment on this network and wonder if this points to a core issue with the network devices.</p></div><div id="question-tags" class="tags-container tags">arp switch multiple</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Apr '16, 13:15</strong></p><img src="https://secure.gravatar.com/avatar/b09a1ec6f727524ca803d99bc2fd7391?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kentench&#39;s gravatar image" /><p>kentench<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kentench has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-51441" class="comments-container"><span id="51442"></span><div id="comment-51442" class="comment"><div id="post-51442-score" class="comment-score"></div><div class="comment-text"><p>could you provide us a trace with the ARP packets at public accessible place, like google or clouds</p></div><div id="comment-51442-info" class="comment-info"><span class="comment-age">(06 Apr '16, 13:46)</span> Christian_R</div></div><span id="51443"></span><div id="comment-51443" class="comment"><div id="post-51443-score" class="comment-score"></div><div class="comment-text"><p>Here it is (Dropbox): <a href="https://www.dropbox.com/s/1ufdnycwqoqh9de/cap4-6-16nocobra.pcapng?dl=0">https://www.dropbox.com/s/1ufdnycwqoqh9de/cap4-6-16nocobra.pcapng?dl=0</a></p></div><div id="comment-51443-info" class="comment-info"><span class="comment-age">(06 Apr '16, 13:52)</span> kentench</div></div><span id="51469"></span><div id="comment-51469" class="comment"><div id="post-51469-score" class="comment-score"></div><div class="comment-text"><p>Where did you take the trace? ( Span port/ vm,....)</p></div><div id="comment-51469-info" class="comment-info"><span class="comment-age">(07 Apr '16, 06:29)</span> Christian_R</div></div><span id="51477"></span><div id="comment-51477" class="comment"><div id="post-51477-score" class="comment-score"></div><div class="comment-text"><p>It was captured on a Windows NIC for the device with MAC MitacInt_ac:af:0e, IP:10.71.67.21, which is our controller that is talking to various devices in the system. It was easier to see all the ARP traffic after I applied the View Filter !tcp which eliminated all the VNC and RFB remote access traffic. This capture was taken by remoting into this operational system and performing the capture on the controller box. So, this is the traffic seen at the controller NIC minus some network audio traffic which was filtered out of the capture.</p></div><div id="comment-51477-info" class="comment-info"><span class="comment-age">(07 Apr '16, 07:54)</span> kentench</div></div><span id="51482"></span><div id="comment-51482" class="comment"><div id="post-51482-score" class="comment-score"></div><div class="comment-text"><p>First of all: The easiest way to filter for arp is: arp<br />
</p><p>Can trace outside the system. Perhaps it is just a capturing problem, also you can check if you use the newest network drivers.</p></div><div id="comment-51482-info" class="comment-info"><span class="comment-age">(07 Apr '16, 09:38)</span> Christian_R</div></div></div><div id="comment-tools-51441" class="comment-tools"></div><div class="clear"></div><div id="comment-51441-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>


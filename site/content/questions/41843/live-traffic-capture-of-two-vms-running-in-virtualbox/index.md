+++
type = "question"
title = "Live Traffic Capture of two VMs running in VirtualBox"
description = '''I want to create following lab setup using VirtualBox and Wireshark:  Two VMs to communicate with each other. Wireshark to be installed in the Host. And able to capture live traffic of above two communicating VMs. Ubuntu as a host and 2 Guests (Windows XP and Tiny Core Linux)  Any suggestion or poss...'''
date = "2015-04-25T15:34:00Z"
lastmod = "2015-05-03T14:06:00Z"
weight = 41843
keywords = [ "ubuntu", "virtualbox", "wireshark" ]
aliases = [ "/questions/41843" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Live Traffic Capture of two VMs running in VirtualBox](/questions/41843/live-traffic-capture-of-two-vms-running-in-virtualbox)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41843-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>I want to create following lab setup using VirtualBox and Wireshark:</p><ol><li>Two VMs to communicate with each other.</li><li>Wireshark to be installed in the Host. And able to capture live traffic of above two communicating VMs.</li><li>Ubuntu as a host and 2 Guests (Windows XP and Tiny Core Linux)</li></ol><p>Any suggestion or possible work around?</p></div><div id="question-tags" class="tags-container tags">ubuntu virtualbox wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Apr '15, 15:34</strong></p><img src="https://secure.gravatar.com/avatar/abebafb6d8867b406b5735482fc1e828?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mushtaq%20Hussain&#39;s gravatar image" /><p>Mushtaq Hussain<br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mushtaq Hussain has no accepted answers">0%</span></p></div></div><div id="comments-container-41843" class="comments-container"></div><div id="comment-tools-41843" class="comment-tools"></div><div class="clear"></div><div id="comment-41843-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="42000"></span>

<div id="answer-container-42000" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42000-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>For the VMs use Network: Host-only Adapter</p><p>On the Host PC open Wireshark and start the capture on Virtualbox Host-Only Network.</p><p>*Tested on Win 7 with Virtualbox 4.3.26 and Wireshark 1.12.4</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 May '15, 04:11</strong></p><img src="https://secure.gravatar.com/avatar/721b9692d2a30fc3b386b7fae9a44220?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland&#39;s gravatar image" /><p>Roland<br />
<span class="score" title="764 reputation points">764</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland has 9 accepted answers">13%</span></p></div></div><div id="comments-container-42000" class="comments-container"><span id="42005"></span><div id="comment-42005" class="comment"><div id="post-42005-score" class="comment-score">1</div><div class="comment-text"><p>I had tried same setup previously; however again repeated after seeing your answer. But I am unable to capture the traffic between two VMs running in VirtualBox. I am able to capture broadcast packets from the two VMs, however no unicast packets (like ICMP packets) between the two VMs are being captured by the Wireshark on vboxnet0 interface.<br />
</p><p>My Environment is: Host is Ubuntu 14.04 LTS, Wireshark Version 1.10.6, VirtualBox Version 4.3.10_Ubuntu r93012. Both VMs are in Host-Only mode attached to vboxnet0 adapter. And I am capturing on vboxnet0 interface on Wireshark.</p></div><div id="comment-42005-info" class="comment-info"><span class="comment-age">(01 May '15, 13:25)</span> Mushtaq Hussain</div></div><span id="42011"></span><div id="comment-42011" class="comment"><div id="post-42011-score" class="comment-score"></div><div class="comment-text"><p>It also works on Linux, but I only tested with Virtualbox 4.3.26.</p></div><div id="comment-42011-info" class="comment-info"><span class="comment-age">(01 May '15, 15:32)</span> Roland</div></div><span id="42025"></span><div id="comment-42025" class="comment"><div id="post-42025-score" class="comment-score"></div><div class="comment-text"><p>Upgraded to Virtualbox 4.3.26 r98988. It does seems a more refined and light on resources. However, my original problem remains exactly the same. I have also set the Promiscuous mode policy for vboxnet0 interface in both VMs to 'Allow All', still Wireshark only captures the broadcast packets not the unicast ping between the two VMs. Wireshark is also set to capture in promiscuous mode.</p></div><div id="comment-42025-info" class="comment-info"><span class="comment-age">(02 May '15, 15:39)</span> Mushtaq Hussain</div></div><span id="42026"></span><div id="comment-42026" class="comment"><div id="post-42026-score" class="comment-score"></div><div class="comment-text"><p>Can you share any specific interface settings for VMs or Virtualbox global configurations?</p></div><div id="comment-42026-info" class="comment-info"><span class="comment-age">(02 May '15, 15:41)</span> Mushtaq Hussain</div></div><span id="42028"></span><div id="comment-42028" class="comment"><div id="post-42028-score" class="comment-score"></div><div class="comment-text"><p>I used the default settings, promiscuous mode was set to Deny. Do you have the firewall enabled on the host?</p></div><div id="comment-42028-info" class="comment-info"><span class="comment-age">(03 May '15, 05:08)</span> Roland</div></div><span id="42029"></span><div id="comment-42029" class="comment not_top_scorer"><div id="post-42029-score" class="comment-score"></div><div class="comment-text"><p>I have also checked with firewalls disabled, but same result. Also firewall does not seem to be a problem here, as I am able to capture all traffic through same interface when one VM is in Virtualbox and other one in the VMware player. However, it seems when both VMs are in virtualbox they have some kind of direct link and unicast traffic does not reach at vboxnet0. As broadcast traffic from both VMs is being captured.</p></div><div id="comment-42029-info" class="comment-info"><span class="comment-age">(03 May '15, 08:41)</span> Mushtaq Hussain</div></div><span id="42030"></span><div id="comment-42030" class="comment not_top_scorer"><div id="post-42030-score" class="comment-score"></div><div class="comment-text"><p>I have also checked with firewalls disabled, but same result. Also firewall does not seem to be a problem here, as I am able to capture all traffic through same interface when one VM is in Virtualbox and other one in the VMware player. However, it seems when both VMs are in virtualbox they have some kind of direct link and unicast traffic does not reach at vboxnet0. As broadcast traffic from both VMs is being captured.</p></div><div id="comment-42030-info" class="comment-info"><span class="comment-age">(03 May '15, 09:21)</span> Mushtaq Hussain</div></div><span id="42117"></span><div id="comment-42117" class="comment not_top_scorer"><div id="post-42117-score" class="comment-score"></div><div class="comment-text"><p>Can you try it on another host?</p></div><div id="comment-42117-info" class="comment-info"><span class="comment-age">(06 May '15, 01:42)</span> Roland</div></div></div><div id="comment-tools-42000" class="comment-tools"><span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a></div><div class="clear"></div><div id="comment-42000-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="42033"></span>

<div id="answer-container-42033" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42033-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Virtualbox includes a feature to capture traffic generated by the virtual machines.</p><blockquote><p><a href="https://www.virtualbox.org/wiki/Network_tips">https://www.virtualbox.org/wiki/Network_tips</a></p></blockquote><p>This looks like the most reliable way to capture traffic between two VMs, besides capturing the traffic directly in the VMs.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 May '15, 14:06</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-42033" class="comments-container"><span id="42036"></span><div id="comment-42036" class="comment"><div id="post-42036-score" class="comment-score"></div><div class="comment-text"><p>Thank you for pointing to this feature. However, I need to monitor the live capturing of traffic in Wireshark, whereas in this feature case you can not analyse the traffic in real time.</p></div><div id="comment-42036-info" class="comment-info"><span class="comment-age">(03 May '15, 14:22)</span> Mushtaq Hussain</div></div><span id="42037"></span><div id="comment-42037" class="comment"><div id="post-42037-score" class="comment-score">1</div><div class="comment-text"><p>well, then your option is to capture inside one of the VMs (or even both).</p></div><div id="comment-42037-info" class="comment-info"><span class="comment-age">(03 May '15, 14:48)</span> Kurt Knochner ♦</div></div><span id="42040"></span><div id="comment-42040" class="comment"><div id="post-42040-score" class="comment-score">1</div><div class="comment-text"><p>Definitely one way is to capture inside the VM. But is it not possible to do a capture in host? As may be there comes a situation where one is looking to capture live traffic of a network formed from more than two VMs at a time. Any thoughts.</p></div><div id="comment-42040-info" class="comment-info"><span class="comment-age">(03 May '15, 15:19)</span> Mushtaq Hussain</div></div><span id="42047"></span><div id="comment-42047" class="comment"><div id="post-42047-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Any thoughts.</p></blockquote><p>Ask the Virtualbox community. They should know <strong>their</strong> product better than we do ;-))</p></div><div id="comment-42047-info" class="comment-info"><span class="comment-age">(03 May '15, 16:41)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-42033" class="comment-tools"></div><div class="clear"></div><div id="comment-42033-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


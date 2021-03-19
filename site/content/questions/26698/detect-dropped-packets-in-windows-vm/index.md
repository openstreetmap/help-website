+++
type = "question"
title = "Detect dropped packets in Windows VM"
description = '''We have about 30 Windows VMs under vSphere 5.1. I am using esxtop to monitor the network and I see some odd behavior. Under the %DroppedPacketsReceived (%DRPRX) column you can see the problem. This column will show zeros for all VMs for a few seconds then all the VMs will show packet loss for a few ...'''
date = "2013-11-06T10:50:00Z"
lastmod = "2013-11-07T06:10:00Z"
weight = 26698
keywords = [ "dropped", "vmware" ]
aliases = [ "/questions/26698" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Detect dropped packets in Windows VM](/questions/26698/detect-dropped-packets-in-windows-vm)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26698-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We have about 30 Windows VMs under vSphere 5.1. I am using esxtop to monitor the network and I see some odd behavior. Under the %DroppedPacketsReceived (%DRPRX) column you can see the problem. This column will show zeros for all VMs for a few seconds then all the VMs will show packet loss for a few seconds, then back to zero. I have a Win7 machine with Wireshark installed on this host, you can see it at the bottom of the screen shot. When I do a packet capture: - Will it show these dropped packets? - If so what would I be looking for?</p><p><img src="https://osqa-ask.wireshark.org/upfiles/DroppedPackets_1.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">dropped vmware</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Nov '13, 10:50</strong></p><img src="https://secure.gravatar.com/avatar/9e2b9a8c8a81ac14e20c63157c262cc9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="HendersonD&#39;s gravatar image" /><p>HendersonD<br />
<span class="score" title="51 reputation points">51</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="HendersonD has one accepted answer">100%</span></p></img></div></div><div id="comments-container-26698" class="comments-container"><span id="26699"></span><div id="comment-26699" class="comment"><div id="post-26699-score" class="comment-score"></div><div class="comment-text"><p>Not a direct answer to your questions but just a hint, can this be related to one of this:</p><p><a href="http://kb.vmware.com/kb/1010071">http://kb.vmware.com/kb/1010071</a></p><p><a href="http://kb.vmware.com/kb/2039495">http://kb.vmware.com/kb/2039495</a></p></div><div id="comment-26699-info" class="comment-info"><span class="comment-age">(06 Nov '13, 14:58)</span> Edmond</div></div></div><div id="comment-tools-26698" class="comment-tools"></div><div class="clear"></div><div id="comment-26698-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="26713"></span>

<div id="answer-container-26713" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26713-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I figured it out This thread about half way through talks about VDS Health Check sending out broadcast packets</p><p><a href="https://communities.vmware.com/message/2280450">https://communities.vmware.com/message/2280450</a></p><p>I disabled the Health Check and the dropped packets vanished. The Virtual Distributed Switch Health Check just looks at this switch and sees if it is setup correctly. Having the health check turned on generates broadcast packets. Not sure why my VMs are dropping these packets but turning it off is the solution.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Nov '13, 06:10</strong></p><img src="https://secure.gravatar.com/avatar/9e2b9a8c8a81ac14e20c63157c262cc9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="HendersonD&#39;s gravatar image" /><p>HendersonD<br />
<span class="score" title="51 reputation points">51</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="HendersonD has one accepted answer">100%</span></p></div></div><div id="comments-container-26713" class="comments-container"><span id="26717"></span><div id="comment-26717" class="comment"><div id="post-26717-score" class="comment-score"></div><div class="comment-text"><p>I accepted the answer, as it solves the problem.</p></div><div id="comment-26717-info" class="comment-info"><span class="comment-age">(07 Nov '13, 06:18)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-26713" class="comment-tools"></div><div class="clear"></div><div id="comment-26713-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="26708"></span>

<div id="answer-container-26708" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26708-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>From the VMware KB article:</p><blockquote><p>Cite: 'Even though esxtop shows the packets as dropped at the virtual switch, <strong>they are actually dropped between the virtual switch and the guest operating system driver.</strong>'</p></blockquote><p>So, to answer your question:</p><blockquote><p><strong>I have a Win7 machine with Wireshark installed</strong> on this host, you can see it at the bottom of the screen shot. When I do a packet capture: - <strong>Will it show these dropped packets?</strong></p></blockquote><p>The virtual machine will only be able to capture traffic directed to it's own machine, and therefor you won't see the traffic of the other virtual machines.</p><p>Answer to you question: No, you won't see any packets of other virtual machines. BTW: You won't see the 'dropped' packets anyway, as they are, well ... dropped ;-)).</p><p>You can change the operational mode of the vSwitch to 'promiscuous' mode. In that mode, the Win7 system (with Wireshark) will see 'everything' (depends on the configuration of port groups, vlans, etc.).</p><blockquote><p><a href="http://kb.vmware.com/selfservice/microsites/search.do?language=en_US&amp;cmd=displayKC&amp;externalId=1002934">http://kb.vmware.com/selfservice/microsites/search.do?language=en_US&amp;cmd=displayKC&amp;externalId=1002934</a><br />
<a href="http://kb.vmware.com/selfservice/microsites/search.do?language=en_US&amp;cmd=displayKC&amp;externalId=1004099">http://kb.vmware.com/selfservice/microsites/search.do?language=en_US&amp;cmd=displayKC&amp;externalId=1004099</a><br />
</p></blockquote><p><strong>However</strong>, that will probably cause even more problems (due to overload)!!</p><p>One possible solution to your problem is described in the VMware KB article: raise receive buffer sizes.</p><p><strong>HOWEVER</strong>: it remains unclear what causes dropped frames for so many machines. It could be a network burst, a DoS attack or an error in the design.</p><p>To figure out what's going on, I suggest to mirror the physical network port(s) of the VMware host and capture that traffic. Maybe there is a traffic spike in the IO stats, that correlates to those dropped frames shown in esxtop. If there is nothing, the network traffic could be caused by another virtual machine. In that case you can either capture the traffic in each virtual machine (probably to many) or on the virtual switch after you placed it in <strong>promiscuous</strong> mode. <strong>WARNING</strong>: Don't do that without talking to your local VMware guru!! As I said, that might cause even more (severe) problems.</p><p>Another option: Capture on the VMware host itself with tcpdump</p><blockquote><p><a href="http://kb.vmware.com/selfservice/microsites/search.do?language=en_US&amp;cmd=displayKC&amp;externalId=1000880">http://kb.vmware.com/selfservice/microsites/search.do?language=en_US&amp;cmd=displayKC&amp;externalId=1000880</a><br />
</p></blockquote><p>And finally: See a blog post of @Jasper</p><blockquote><p><a href="http://blog.packet-foo.com/2013/04/capturing-packets-of-vmware-machines/">http://blog.packet-foo.com/2013/04/capturing-packets-of-vmware-machines/</a><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Nov '13, 02:25</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 07 Nov '13, 02:33</p></div></div><div id="comments-container-26708" class="comments-container"><span id="26712"></span><div id="comment-26712" class="comment"><div id="post-26712-score" class="comment-score"></div><div class="comment-text"><p>Thanks for all the great suggestions I have seen the two VMWare KB articles. I will give them another shot but the first time I changed the Small RX buffer and RX Ring Size on one VM I did not see any changes in dropped packets. This is happening on every one of my 40+ server VMs and all of my View desktops so I would hate to think that these two parameters needed to be changed on all of them.</p><p>Kurt - I actually made a VM with Win7 and Wireshark installed. If you look at my screen shot above it is the last VM listed. I ran the capture using this VM and did not see a smoking gun. Again, this could be due to my ignorance on not knowing exactly what to look for in a packet capture or the packets are dropped between the virtual switch and the guest OS driver and therefore doing the capture inside the guest OS will never capture these dropped packets.</p><p>If I do the capture on the physical switch by running a port-mirror, what types of things am I looking for that would indicate packets are being dropped?</p></div><div id="comment-26712-info" class="comment-info"><span class="comment-age">(07 Nov '13, 05:34)</span> HendersonD</div></div><span id="26716"></span><div id="comment-26716" class="comment"><div id="post-26716-score" class="comment-score"></div><div class="comment-text"><p>Apparently you found the solution yourself (see your answer). Just for the records:</p><blockquote><p>I ran the capture using this VM and did not see a smoking gun.</p></blockquote><p>As I said, you won't see any 'dropped' traffic in the virtual machine if the packets are dropped by the driver, so Wireshark will never know about those packets, hence no 'smoking gun' visible in Wireshark</p></div><div id="comment-26716-info" class="comment-info"><span class="comment-age">(07 Nov '13, 06:18)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-26708" class="comment-tools"></div><div class="clear"></div><div id="comment-26708-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


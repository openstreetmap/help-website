+++
type = "question"
title = "Why Does wireshark not capture any traffic from Source Machine with Outbound Firewall Rules?"
description = '''Hi, I was testing on Windows 2008 Standard Edition (Local Machine IP :- 192.168.2.160) with normal windows firewall (no 3rd party) and created an outbound firewall rule to deny for TCP Ports 80/443 of Remote IP (i.e. 192.168.10.104) (and Local Port All as it could be random). The firewall worked fin...'''
date = "2012-05-19T22:00:00Z"
lastmod = "2012-05-20T09:10:00Z"
weight = 11149
keywords = [ "source", "wireshark", "outboundfirewall", "capture" ]
aliases = [ "/questions/11149" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Why Does wireshark not capture any traffic from Source Machine with Outbound Firewall Rules?](/questions/11149/why-does-wireshark-not-capture-any-traffic-from-source-machine-with-outbound-firewall-rules)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11149-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I was testing on Windows 2008 Standard Edition (Local Machine IP :- 192.168.2.160) with normal windows firewall (no 3rd party) and created an outbound firewall rule to deny for TCP Ports 80/443 of Remote IP (i.e. 192.168.10.104) (and Local Port All as it could be random). The firewall worked fine and I could block all outbound traffic to Ports 80/443 of that remote IP. Traffic to same ports on any other remote IP worked just fine.</p><p>However I would have expected wireshark to have picked up the traffic initiation attempt at least from local PC/random ports and drops when matched against remote IP/Port that I have defined in the Outbound Rules.</p><p>== &gt; However I could see absolutely no traffic for this when running wire shark on the Local PC where I had applied such a rule.</p><p>== &gt; Checking the windows Firewall Logs I could see the Drops:-</p><p>2012-05-20 10:08:34 DROP TCP 192.168.2.160 192.168.10.104 49215 80 0 - 0 0 0 - - - SEND</p><p>2012-05-20 10:08:35 DROP TCP 192.168.2.160 192.168.10.104 49216 80 0 - 0 0 0 - - - SEND</p><p>== &gt; So the windows firewall clearly shows the drops then why does that not reflect in the wireshark?</p><p>== &gt; Is it because the Firewall is software based and the request was made via a browser that it never gets sent down beyond the network layer from the App layer of the same PC when Windows firewall and the PC in fact never sends the packet.</p><p>Or is there some setting on wire-shark that can allow such drops to show as well as we can see in the Firewall logs above.</p><p>The main reason for me to ask this I want to clarify the way this works as the traffic not showing could be an issue with:-</p><p>1.) An application as well which might not be able to invoke the lower layers and initiate from source itself. OR, 2.) It could be an issue with block as well like this and we would not be able to distinguish via packet captures b/w them and more so if no such logs / 3rd party unknown firewall apps are present.</p><p>== &gt; I am not sure if I should have posted this concern in Windows forum or wireshark but since I could see nothing in wire-shark unlike in the Windows Firewall Logs.</p><p>Please suggest</p><p>Regards, Prad :)</p></div><div id="question-tags" class="tags-container tags">source wireshark outboundfirewall capture</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 May '12, 22:00</strong></p><img src="https://secure.gravatar.com/avatar/a34698968aabc8ad733cd1445d1f4bb2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="im_prad&#39;s gravatar image" /><p>im_prad<br />
<span class="score" title="5 reputation points">5</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="im_prad has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 19 May '12, 22:03</p></div></div><div id="comments-container-11149" class="comments-container"></div><div id="comment-tools-11149" class="comment-tools"></div><div class="clear"></div><div id="comment-11149-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="11152"></span>

<div id="answer-container-11152" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11152-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Most likely the Windows Firewall will drop the packets before they even get close to the point where dumpcap (which does the actually capture for Wireshark) can see it and pick it up.</p><p>My advice is always the same: if you want to verify if a node behaves like it should, do <strong>not</strong> capture on the node. Capture on a third, passive device, that runs Wireshark and that picks up the nodes packets from a SPAN Port/HUB/TAP. It's the only way to know what really happens (or doesn't happen).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 May '12, 05:27</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-11152" class="comments-container"><span id="11430"></span><div id="comment-11430" class="comment"><div id="post-11430-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the suggestion Jasper,</p><p>However if the packet capture from Same system where the firewall is implemented doesn't show in Wireshark, then while capturing for a third, passive device, that runs Wireshark and is port spanned for System where firewall is, will that show the traffic initiation there?</p><p>Thanks, Prad</p></div><div id="comment-11430-info" class="comment-info"><span class="comment-age">(28 May '12, 16:49)</span> im_prad</div></div><span id="11452"></span><div id="comment-11452" class="comment"><div id="post-11452-score" class="comment-score"></div><div class="comment-text"><p>Yes, because if you use a third system that captures the traffic between the other two will see packets that are already "on their way" and on the wire. They can't be "hidden" inside internal OS channels or paths. As long as they have been put on the wire you will see them, unless they get damaged (which means: discarded) or your capture device is too slow to pick them all up.</p></div><div id="comment-11452-info" class="comment-info"><span class="comment-age">(29 May '12, 10:18)</span> Jasper ♦♦</div></div><span id="11453"></span><div id="comment-11453" class="comment"><div id="post-11453-score" class="comment-score">1</div><div class="comment-text"><p>Even when you are on a third system, any traffic originating on the firewall machine and blocked by the firewall (Windows internal, for example) will still not show up, since it never reaches the network. But if you are looking for packets that are managing to evade the firewall in some way and get out anyway, then they will be seen.</p></div><div id="comment-11453-info" class="comment-info"><span class="comment-age">(29 May '12, 11:47)</span> inetdog</div></div><span id="11483"></span><div id="comment-11483" class="comment"><div id="post-11483-score" class="comment-score"></div><div class="comment-text"><p>Conflicting views here from the experts.</p><p>I'll mark this as answered for now as it's on VM and can't test anytime soon with the port span/ 3rd Machine option.</p><p>Thanks a lot to all of you here.</p></div><div id="comment-11483-info" class="comment-info"><span class="comment-age">(30 May '12, 20:15)</span> im_prad</div></div></div><div id="comment-tools-11152" class="comment-tools"></div><div class="clear"></div><div id="comment-11152-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="11155"></span>

<div id="answer-container-11155" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11155-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The Windows 2008 firewall is implemented with the WFP (Windows Filtering Platform), which is implemented deeply in the windows kernel, as one of the core components. Before a packet is allowed, the related stack (e.g. TCP) uses the WFP API to determine if the connection/packet is allowed, according to the filtering rules.</p><p>The NPF driver of WinPcap is implemented as a NDIS protocol driver. Without knowing it for sure, I strongly assume that the NPF filter is located somewhere "below" the windows TCP/IP stack, so you won't see any blocked packets/connections.</p><p>For further reading I recommend these links:</p><blockquote><p><code>http://www.winpcap.org/docs/docs_41b5/html/group__NPF.html</code><br />
<code>http://msdn.microsoft.com/en-us/library/windows/desktop/aa366510(v=vs.85).aspx</code><br />
<code>http://msdn.microsoft.com/en-us/library/windows/desktop/aa366509(v=vs.85).aspx</code><br />
</p></blockquote><p>Furthermore I second what @Jasper said. If sniffing is your main interest, please do it "off system". If the internal workings of the Windows Firewall is your main interest, I recommend the links above.</p><p>Regards Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 May '12, 09:10</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-11155" class="comments-container"><span id="11156"></span><div id="comment-11156" class="comment"><div id="post-11156-score" class="comment-score"></div><div class="comment-text"><p>You have to keep in mind TCP chimney offloading as well, setting up some kind of "vitrual tunnel" between application/network stack interface and an NDIS capable NIC, which also has an impact on the data wireshark is able to "see".</p><p>So I'd always go for a by-system analysis if those question are of interest, because with simply changing the NIC to another driver version / manufacturer things could change at all</p></div><div id="comment-11156-info" class="comment-info"><span class="comment-age">(20 May '12, 09:21)</span> Landi</div></div></div><div id="comment-tools-11155" class="comment-tools"></div><div class="clear"></div><div id="comment-11155-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


+++
type = "question"
title = "WireShark on LAN"
description = '''Hello. I have problems with a PC/PCS from my LAN network. One PC made spam on 25 port but i don&#x27;t know who. My Network is like ex: ROUTER (with wan IP -xxx.xxx.xxx.xxx snd lan IP 192.168.1.1) and many PC&#x27;s linked to router . I want to install whireshark on a pc from network (192.168.1.2) to monitori...'''
date = "2012-04-29T06:47:00Z"
lastmod = "2012-04-30T16:24:00Z"
weight = 10504
keywords = [ "on", "lan", "wireshark" ]
aliases = [ "/questions/10504" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [WireShark on LAN](/questions/10504/wireshark-on-lan)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10504-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello. I have problems with a PC/PCS from my LAN network. One PC made spam on 25 port but i don't know who. My Network is like ex: ROUTER (with wan IP -xxx.xxx.xxx.xxx snd lan IP 192.168.1.1) and many PC's linked to router . I want to install whireshark on a pc from network (192.168.1.2) to monitoring the router to find what PC from LAN made spam on internet. How i can do that with WireShark?</p></div><div id="question-tags" class="tags-container tags">on lan wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Apr '12, 06:47</strong></p><img src="https://secure.gravatar.com/avatar/cd2418fe04f82d7478d2be4b5cbf19fb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="luciffere&#39;s gravatar image" /><p>luciffere<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="luciffere has no accepted answers">0%</span></p></div></div><div id="comments-container-10504" class="comments-container"></div><div id="comment-tools-10504" class="comment-tools"></div><div class="clear"></div><div id="comment-10504-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="10505"></span>

<div id="answer-container-10505" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10505-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Unless you can make your router mirror or span the traffic from other ports onto the port to which your Wireshark machine is connected then you will probably not be able to see the traffic as your router is most likely to be a switch and Wireshark will not be able to capture traffic from the other ports.</p><p>If you post some more info about your router (make and model) and your WAN type (DSL, Cable, Fibre) we may give you more help.</p><p>See the <a href="http://wiki.wireshark.org/CaptureSetup">Capture Setup</a> page on the Wiki for more info about capturing.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Apr '12, 10:11</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-10505" class="comments-container"><span id="10506"></span><div id="comment-10506" class="comment"><div id="post-10506-score" class="comment-score"></div><div class="comment-text"><p>My router is ASUS WL520gc and the WAN type is:</p><p>WAN Type: Static<br />
IP Address: 82.77.xxx.xxx<br />
Subnet Mask: 255.255.255.224<br />
Gateway: 82.77.xxx.xx<br />
DNS Servers: 217.156.101.10<br />
</p><hr /><p>LAN Interface IP Address: 192.168.1.1 Subnet Mask: 255.255.255.0<br />
Default Gateway: 192.168.1.1<br />
</p></div><div id="comment-10506-info" class="comment-info"><span class="comment-age">(29 Apr '12, 10:42)</span> luciffere</div></div><span id="10507"></span><div id="comment-10507" class="comment"><div id="post-10507-score" class="comment-score"></div><div class="comment-text"><p>continue: Firmware Version: 2.0.1.1</p></div><div id="comment-10507-info" class="comment-info"><span class="comment-age">(29 Apr '12, 10:43)</span> luciffere</div></div><span id="10509"></span><div id="comment-10509" class="comment"><div id="post-10509-score" class="comment-score"></div><div class="comment-text"><p>OK, that's a "Cable" type wireless router, with the stock firmware it won't mirror or span ports for either the wired or wireless traffic.</p><p>If you connected a hub or a switch that could mirror port on the WAN side then although you would be able to see the SPAM traffic, it's likely that the IP addresses of the traffic won't help as your Asus router will have NAT'd them to the WAN IP.</p><p>I think you are just going to have to visit each machine and inspect it for the SPAM traffic, either by installing Wireshark or looking at the output of netstat for connections on port 25.</p></div><div id="comment-10509-info" class="comment-info"><span class="comment-age">(29 Apr '12, 13:23)</span> grahamb ♦</div></div></div><div id="comment-tools-10505" class="comment-tools"></div><div class="clear"></div><div id="comment-10505-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="10541"></span>

<div id="answer-container-10541" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10541-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>as your router does not support port mirroring, there are two "cheap" options.</p><p>1.) Buy a cheap switch that is able to do port mirroring (e.g. HP ProCurve Switch 1810G-8, 8-Port, managed) and plug it between your router and the lan switch of your network. Then connect a sniffer to the mirrord port and filter on 'port 25'.</p><p>2.) Add a second network interface to your sniffer PC / Laptop and create a brigde between the two interface. Then connect the router to one interface and the lan switch to the other interface. Start sniffing on any one of the interfaces. DON'T switch off the PC/Laptop, as this will interrupt your internet connection. If you're done with sniffing, re-connect the router to the internal switch.</p><p>Create a Bridge with Windows 7<br />
<a href="http://windows.microsoft.com/en-US/windows-vista/Create-a-network-bridge">http://windows.microsoft.com/en-US/windows-vista/Create-a-network-bridge</a></p><p>Create a Bridge with Linux<br />
<a href="http://www.linuxjournal.com/article/8172?page=0,0">http://www.linuxjournal.com/article/8172?page=0,0</a></p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Apr '12, 16:24</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 30 Apr '12, 16:24</p></div></div><div id="comments-container-10541" class="comments-container"></div><div id="comment-tools-10541" class="comment-tools"></div><div class="clear"></div><div id="comment-10541-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


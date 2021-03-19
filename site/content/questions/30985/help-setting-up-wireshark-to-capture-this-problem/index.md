+++
type = "question"
title = "Help setting up wireshark to capture this problem"
description = '''Networking is outside of my wheelhouse so I thought I&#x27;d see if I could find some help here. Device &quot;A&quot; is sending out data over ethernet/IP. Device &quot;A&quot; is not set to unicast so I assume that means it is multicast or broadcast. Device &quot;B&quot; is listening to device &quot;A&quot; and always collects the data output...'''
date = "2014-03-20T06:24:00Z"
lastmod = "2014-03-20T08:50:00Z"
weight = 30985
keywords = [ "broadcast", "misseddata", "configuration", "ethernetip", "multicast" ]
aliases = [ "/questions/30985" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Help setting up wireshark to capture this problem](/questions/30985/help-setting-up-wireshark-to-capture-this-problem)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30985-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Networking is outside of my wheelhouse so I thought I'd see if I could find some help here. Device "A" is sending out data over ethernet/IP. Device "A" is not set to unicast so I assume that means it is multicast or broadcast. Device "B" is listening to device "A" and always collects the data output from device "A". Device "C" is also listening to device "A" and usually collects the data from device "A", but occasionally does not collect any data as though device "A" never sent anything. But, I can verify that device "A" did send data by looking at the memory registers in device "B". I need some advice on the best way to configure wireshark to detect what is going on here. Thanks</p></div><div id="question-tags" class="tags-container tags">broadcast misseddata configuration ethernetip multicast</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Mar '14, 06:24</strong></p><img src="https://secure.gravatar.com/avatar/80dd2abc2213319a7448c79a26f5b063?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mitsubishi47591&#39;s gravatar image" /><p>mitsubishi47591<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mitsubishi47591 has no accepted answers">0%</span></p></div></div><div id="comments-container-30985" class="comments-container"></div><div id="comment-tools-30985" class="comment-tools"></div><div class="clear"></div><div id="comment-30985-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30993"></span>

<div id="answer-container-30993" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30993-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>What do you mean by "Device "A" is not set to unicast"? If device A is a typical device, it only sends certain packets as Ethernet broadcast, such as ARP requests, DHCP requests, various discovery protocols, etc. But most packets will be sent unicast, namely to the Ethernet destination MAC address of the remote device it resolved the IP to, or the local gateway/router's MAC. (in either case, something it learned from ARP typically)</p><p>So assuming you can't run Wireshark directly on Device A or Device B, which would be the best thing to do, instead you can run it on Device C or some other PC. The "trick" is connecting that Device C or PC to the network in such a way that it sees the unicast packets. Connecting it to a normal Ethernet switch port, for example, won't do it since the switch only sends a unicast packet out the port it needs to go to. So you need to either use an old-school repeater/hub, or if your ethernet switch supports a monitor port then using that. (there are various other hacks possible, but those two are the easiest)</p><p>Or are you using some protocol that specifically sends broadcast or multicast IP/Ethernet packets? (there are such protocols, but they're not common)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Mar '14, 08:50</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p>Hadriel<br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-30993" class="comments-container"><span id="31014"></span><div id="comment-31014" class="comment"><div id="post-31014-score" class="comment-score"></div><div class="comment-text"><p>I've cleared up some of my personal ignorance today, but I still have a long way to go. What I should've said was that "Device A" has 1 "master" and 1 "listen only" connection. "Device A" outputs data when polled to do so. I'm assuming that both the master and the listen only connection can poll the device, but the master and the listen only connection are time synced with each other and have the same RPI which means they both poll "Device A" at the same time (I don't know if that's good or bad). Devices A, B, and C, don't support wireshark, so I'll be connecting a PC to the network to get a network capture. There is a managed switch between "Device A" and "Devices B and C", but I'm not sure if there is a monitor port or not. So when setting up wireshark, do I use my computers LAN port IP address, or would I set it to the address of "Device C"?</p></div><div id="comment-31014-info" class="comment-info"><span class="comment-age">(20 Mar '14, 13:33)</span> mitsubishi47591</div></div><span id="31015"></span><div id="comment-31015" class="comment"><div id="post-31015-score" class="comment-score"></div><div class="comment-text"><p>I don't know what you mean by the first part of your comment. But to answer the last sentence, no you do not set it to the address of Device C. Wireshark runs in promiscuous mode, meaning it will capture+display whatever packets arrive at the PC running Wireshark, even if their destination MAC/IP does not belong to the PC running Wireshark. (there are some situations where Wireshark cannot run in promiscuous mode, but I'll ignore that for sake of brevity :)</p><p>The point of using a switch monitor port, or old-style repeater, is to get Ethernet packets that have a unicast destination address of something else, to arrive at the PC running wireshark as well.</p><p>In the switch monitor port scenario, that happens because the switch copies all Ethernet packets to the monitor port, so they can be monitored by tools like Wireshark (hence the name "monitor port").</p></div><div id="comment-31015-info" class="comment-info"><span class="comment-age">(20 Mar '14, 14:09)</span> Hadriel</div></div></div><div id="comment-tools-30993" class="comment-tools"></div><div class="clear"></div><div id="comment-30993-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


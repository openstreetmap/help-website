+++
type = "question"
title = "Deciphering Ethernet II Src information"
description = '''I&#x27;m trying to track down network traffic coming from my Exchange server that is going to an external IP address that is in China according to Network Solutions. My firewall logs show TCP traffic on various uncommon ports being sent from the Exchange server to several IP addresses in China. They are ...'''
date = "2011-07-08T09:49:00Z"
lastmod = "2011-07-08T14:17:00Z"
weight = 4959
keywords = [ "ii", "ethernet", "wireshark", "results", "hewlettp_" ]
aliases = [ "/questions/4959" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Deciphering Ethernet II Src information](/questions/4959/deciphering-ethernet-ii-src-information)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4959-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to track down network traffic coming from my Exchange server that is going to an external IP address that is in China according to Network Solutions.</p><p>My firewall logs show TCP traffic on various uncommon ports being sent from the Exchange server to several IP addresses in China. They are being sent out on TCP ports such as 5296, 31671, etc. Because of the way I've configured my firewall, the packets are being dropped, so they aren't getting sent out, but I'd like to track down what it is on the server that is sending them.</p><p>I've run a capture on my Exchange server using Wireshark. I matched an IP address and TCP port from one of these firewall logs to an entry in the capture in Wireshark.</p><p>What I'm trying to figure out is what on the Exchange server originated this packet. When I highlight the entry in the capture window, and then expand Ethernet II SRC in the 2nd window, it lists the source as HewlettP_e3:4b:2c. I've noticed that almost every entry in the capture list shows these source and destination entries to be HewlettP_, Cisco_, Fortinet_, Dell_, etc. I don't understand how to interpret this, as it seems odd to me that something from a HP printer or other device on my server would be sending packets to an IP address in China. What exactly are these listings (HewlettP_, Cisco_) in the Ethernet II section and what do they actually represent.</p><p>I've spent several hours searching for this information and have yet to find an answer. I also read the manual. I've found mentioned of the Ethernet II section of the results, but no detailed explanation on what these entries mean. Can someone help?</p></div><div id="question-tags" class="tags-container tags">ii ethernet wireshark results hewlettp_</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Jul '11, 09:49</strong></p><img src="https://secure.gravatar.com/avatar/14d3dfb5960ce75047f8a9d386058821?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alienux&#39;s gravatar image" /><p>alienux<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alienux has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Jul '11, 09:55</p></div></div><div id="comments-container-4959" class="comments-container"></div><div id="comment-tools-4959" class="comment-tools"></div><div class="clear"></div><div id="comment-4959-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="4960"></span>

<div id="answer-container-4960" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4960-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>What you are looking at is the MAC address of the adapters involved, which will probably not be very helpful for what you are looking for. The reason it shows up as <code>Dell_xx:xx:xx</code> is that Wireshark is making a guess about who manufactured the device based on the MAC address (Dell for <code>Dell_</code>, HP for <code>HP_</code>, etc). This is done because each manufacturer uses certain MAC prefixes in their devices --the full MAC address is the one in parenthesis next to the string you are looking at.</p><p>What will probably be more helpful to you is examining the running programs on your server. Can you see what programs and services are running on your server when these events happen?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jul '11, 10:30</strong></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p>multipleinte...<br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="multipleinterfaces has 9 accepted answers">12%</span></p></div></div><div id="comments-container-4960" class="comments-container"><span id="4963"></span><div id="comment-4963" class="comment"><div id="post-4963-score" class="comment-score"></div><div class="comment-text"><p>Ok, thanks for the info. That clears up a lot about the Ethernet II entries.</p><p>As far as things running on the server, yes, I have looked at what is running and haven't found anything that looks unusual. However, I'm going to try to get some more details using something like Process Explorer or an app that shows threads instead of just running processes and I'm hopeful that one of those apps will provide some more info.</p><p>Thanks for your answer.</p></div><div id="comment-4963-info" class="comment-info"><span class="comment-age">(08 Jul '11, 11:48)</span> alienux</div></div><span id="4964"></span><div id="comment-4964" class="comment"><div id="post-4964-score" class="comment-score"></div><div class="comment-text"><p>to check which program is using the suspicious ports you can use the "netstat -ano" command on the command line. It will give you a list of all ports in use and tell you which process owns which port. You should only find programs that are supposed to be running on that server (and using ports), everything else is suspicious. Determining which is which can be tricky though.</p></div><div id="comment-4964-info" class="comment-info"><span class="comment-age">(08 Jul '11, 11:50)</span> Jasper ♦♦</div></div></div><div id="comment-tools-4960" class="comment-tools"></div><div class="clear"></div><div id="comment-4960-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="4966"></span>

<div id="answer-container-4966" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4966-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Although I'm a Wireshark guy, Microsoft's Network Monitor my help you out here, as that can show the ID of the process sending the data. Wireshark can load captures from NetMon, but can't display the process info.</p><p>netstat with the -b flag can show the process ID associated with a socket if run with admin privs, and there is also TCPView from SysInternals that is a graphical version of netstat.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jul '11, 14:17</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-4966" class="comments-container"><span id="4979"></span><div id="comment-4979" class="comment"><div id="post-4979-score" class="comment-score"></div><div class="comment-text"><p>Thanks Jasper and grahamb, I'll look into those as well.</p></div><div id="comment-4979-info" class="comment-info"><span class="comment-age">(11 Jul '11, 05:07)</span> alienux</div></div></div><div id="comment-tools-4966" class="comment-tools"></div><div class="clear"></div><div id="comment-4966-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


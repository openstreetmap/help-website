+++
type = "question"
title = "running wireshark on a server"
description = '''configuration is an intel mac with an airport card and several usb nics. The airport card is for connectivity to the internet. the usb nics provide connectivity to the local lan. internet sharing is used on the mac to distribute internet access and the mac is also a file repository.  Internet sharin...'''
date = "2011-07-16T23:02:00Z"
lastmod = "2011-07-17T01:32:00Z"
weight = 5076
keywords = [ "machine", "sharing", "virtual", "internet" ]
aliases = [ "/questions/5076" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [running wireshark on a server](/questions/5076/running-wireshark-on-a-server)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5076-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>configuration is an intel mac with an airport card and several usb nics. The airport card is for connectivity to the internet. the usb nics provide connectivity to the local lan. internet sharing is used on the mac to distribute internet access and the mac is also a file repository. Internet sharing on the mac results in a dhcp serving addresses in a different class c for each nic-so one nic for example will get 192.168.2.x, the next nic gets 192.168.3.x, etc. This allows each nic to service a whole lan segment. Wireshark installed on the mac sees all interfaces and allows monitoring of traffic. I do not want to run wireshark natively on the mac. It's a production machine and messing around with the bare metal is discouraged. A virtual appliance is perceived as safer (even though it may not be, i cannot convince the responsible higher ups) So, vmware fusion is set up on the mac to run an instance of windows xp sp3. wireshark is installed on windows.in this configuration, wireshark only sees the airport but not the usb nics. The network adapters are set up in bridged mode on vmware. Is there a tutorial that clarifies setup for the nics in fusion and the proper ip addresses they should have in windows? Should they be bridged there as well? If i use the same ip as that used on the mac, obviously i get an ip address conflict.</p></div><div id="question-tags" class="tags-container tags">machine sharing virtual internet</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Jul '11, 23:02</strong></p><img src="https://secure.gravatar.com/avatar/ad1ea5a611b4a0826c9f215a71f77580?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bwana&#39;s gravatar image" /><p>bwana<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bwana has no accepted answers">0%</span></p></div></div><div id="comments-container-5076" class="comments-container"></div><div id="comment-tools-5076" class="comment-tools"></div><div class="clear"></div><div id="comment-5076-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5079"></span>

<div id="answer-container-5079" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5079-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I don't think this will work for you. All vNics in your WinXP system with be connected to the virtual switch in VMware Fusion. So only traffic that is destined for your XP machine (and broad/multicasts) will be visible on the XP machine.</p><p>The functionality of the virtual switch is very limited and it does not have the possibility to configure a mirroring port (as you would have done when there was a real switch in place).</p><p>I just tested this on my own MacBookPro with fusion. The behavior is actually a little different than expected from the above clarification. If I ping from my MacOS host to the Internet, I only see the outgoing packets on my Win7 guest. The incoming echo reply packets are not forwarded to my Win7 machine (which has the Airport adapter bridged to a vNic).</p><p>So all-in-all, if you need to analyze <strong>all</strong> traffic on a particular interface on the Mac, you will have to capture the traffic on the Mac and not in a VM. At least with the current version of Fusion, things might change in the future.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jul '11, 01:32</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-5079" class="comments-container"><span id="5082"></span><div id="comment-5082" class="comment"><div id="post-5082-score" class="comment-score"></div><div class="comment-text"><p>thank you. yes, i was hoping for the virtual machine to be a 'network tap'. i guess another way to get the traffic to go through the xp instance would be to have a dhcp server running in xp (on the vm). This dhcp server would service the nics. i tried tftpd but that is a little too rudimentary- it does not see the virtual interfaces. i'll keep looking.</p></div><div id="comment-5082-info" class="comment-info"><span class="comment-age">(17 Jul '11, 06:55)</span> bwana</div></div></div><div id="comment-tools-5079" class="comment-tools"></div><div class="clear"></div><div id="comment-5079-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


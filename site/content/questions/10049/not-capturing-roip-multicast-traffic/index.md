+++
type = "question"
title = "Not capturing RoIP multicast traffic"
description = '''I have a Telex Radio over IP multicast network and have had trouble getting it to pass over a carrier&#x27;s ethernet link. I am trying to make sure the traffic is getting out to the carrier network. I have simplified the network to a minimum configuration for troubleshooting, so I have a radio console c...'''
date = "2012-04-10T16:42:00Z"
lastmod = "2012-04-11T09:21:00Z"
weight = 10049
keywords = [ "multicast" ]
aliases = [ "/questions/10049" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Not capturing RoIP multicast traffic](/questions/10049/not-capturing-roip-multicast-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10049-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a Telex Radio over IP multicast network and have had trouble getting it to pass over a carrier's ethernet link. I am trying to make sure the traffic is getting out to the carrier network. I have simplified the network to a minimum configuration for troubleshooting, so I have a radio console connected to a Linksys SF300-24 switch, connected to the Telex IP-223 (radio controller), then connected to the radio. The radio and console work correctly over the switch and IP-223.</p><p>Besides looking for the multicast on a regular port, I have tried mirroring the port and VLAN, and connecting the console (and radio) directly into the wireshark ethernet port. I have also tried a connection to a 10baseT hub (repeater, not a switch) without any multicast traffic showing up.<br />
</p><p>I can see (sniff) the normal traffic like spanning tree, arp and the constant pings (unicast) the console does to make sure they are in contact with the radio, but I still don't see the multicast. When hooked to the 10baseT hub, I can see (while transmitting) that there is high activity on all three ports (console, IP223 and wireshark) but there isn't any multicast traffic showing up. I am pretty sure the packets are getting to the NIC on the wireshark host because of link light activity, but still can't see them in wireshark.</p><p>I am running wireshark version 1.6.6 on a Dell Latitude E6400. I suspect it is a PC or NIC driver problem similar to the VLAN tagging problem with the Dell Latitude D620. Any Ideas?</p></div><div id="question-tags" class="tags-container tags">multicast</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Apr '12, 16:42</strong></p><img src="https://secure.gravatar.com/avatar/39739af2c52a21d75aff1bf883d0b966?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Thor&#39;s gravatar image" /><p>Thor<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Thor has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-10049" class="comments-container"></div><div id="comment-tools-10049" class="comment-tools"></div><div class="clear"></div><div id="comment-10049-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="10050"></span>

<div id="answer-container-10050" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10050-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I assume that you are not using any capture filters and that you capture in promiscuous mode? If you are, WinPcap (which Wireshark uses to capture the packets) should be able to see the multicasts. If it is not, then the NIC/NIC-driver combination is filtering them out.</p><p>On the product page f the <a href="http://www.dell.com/us/dfb/p/latitude-e6400/pd">Dell E6400</a>, it does not say which NIC is being used. Could you add the NIC brand and type to your question?</p><p>Have you tried capturing with a different system (with a different NIC) in the same setup?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Apr '12, 00:43</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-10050" class="comments-container"><span id="10056"></span><div id="comment-10056" class="comment"><div id="post-10056-score" class="comment-score"></div><div class="comment-text"><p>Correct, I wasn't using any capture filters. I first tried a Dell Latitiude D620 and then the E6400. Today I am going to try capturing from a workstation.</p></div><div id="comment-10056-info" class="comment-info"><span class="comment-age">(11 Apr '12, 07:50)</span> Thor</div></div></div><div id="comment-tools-10050" class="comment-tools"></div><div class="clear"></div><div id="comment-10050-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="10058"></span>

<div id="answer-container-10058" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10058-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I tried to capture traffic with a workstation today with the same results, no multicast.</p><p>After closer inspection of the capture packets I notice there were ping responses, but I didn't see any ping requests. Thinking about ping DOS attacks I disabled the firewalls (Symantec Endpoint Protection and Windows firewall) and now I can see all multicasts and both sides of the pings.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Apr '12, 09:21</strong></p><img src="https://secure.gravatar.com/avatar/39739af2c52a21d75aff1bf883d0b966?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Thor&#39;s gravatar image" /><p>Thor<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Thor has no accepted answers">0%</span></p></div></div><div id="comments-container-10058" class="comments-container"></div><div id="comment-tools-10058" class="comment-tools"></div><div class="clear"></div><div id="comment-10058-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


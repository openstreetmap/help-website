+++
type = "question"
title = "Seeing Traffic I shouldn&#x27;t"
description = '''Please excuse my ignorance, I am a nitwit (Nerd In Training With Information Technology). I am running wireshark on my PC and seeing ton&#x27;s of traffic I think I should not be seeing. For example a Server has a mapi connection to another server. I thought the idea of a switch is that that traffic is o...'''
date = "2012-04-04T16:07:00Z"
lastmod = "2012-05-31T10:53:00Z"
weight = 9945
keywords = [ "broadcast", "brocade", "stack", "trunk" ]
aliases = [ "/questions/9945" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Seeing Traffic I shouldn't](/questions/9945/seeing-traffic-i-shouldnt)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9945-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Please excuse my ignorance, I am a nitwit (Nerd In Training With Information Technology). I am running wireshark on my PC and seeing ton's of traffic I think I should not be seeing. For example a Server has a mapi connection to another server. I thought the idea of a switch is that that traffic is only between those two hosts? The environment I setup has 4 Brocade FCX48's in a stack in the server farm and a seperate stack of 8 fcx48's for the user's. The stacks are trunked together using 8 gbit links between the stacks. I also have a transparent ips system intercepting all traffic between the stacks (in line) and noticed it things some mac spoofing happening. I figure that is because traffic from a mac comes from one link one time and then another link another time, i.e. port-1 then later from port-2.</p><p>Could the trunk between the switch stacks be causing the traffic to be sent "everywhere" and if so what is the fix?<br />
Thanks in advance for any advice.</p></div><div id="question-tags" class="tags-container tags">broadcast brocade stack trunk</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Apr '12, 16:07</strong></p><img src="https://secure.gravatar.com/avatar/2128ffb15a7c1eb7d51756d608f1b735?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nitwit&#39;s gravatar image" /><p>nitwit<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nitwit has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-9945" class="comments-container"><span id="11493"></span><div id="comment-11493" class="comment"><div id="post-11493-score" class="comment-score"></div><div class="comment-text"><p>I would be very interested to see if anyone has an answer on this. I am experiencing the same thing. We are using Cisco gear here but on my workstation I'm seeing a packet every now and then that has nothing to do with my IP nor is it a broadcast. These aren't full on conversations I'm seeing, just a packet here, packet there. Very strange.</p></div><div id="comment-11493-info" class="comment-info"><span class="comment-age">(31 May '12, 10:08)</span> davj1</div></div></div><div id="comment-tools-9945" class="comment-tools"></div><div class="clear"></div><div id="comment-9945-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11499"></span>

<div id="answer-container-11499" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11499-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I am running wireshark on my PC and seeing ton's of traffic I think I should not be seeing. For example a Server has a mapi connection to another server.</p></blockquote><p>It depends where you connected your PC. If it's a simple <strong>access port</strong> on the switch you should NOT see that traffic. If the port is a <strong>mirror/span port</strong>, you SHOULD see that traffic. Please check the configuration of the switch port your PC is connected to. If the switch port is a regular access port, please try another switch port. If it's the same there, I suggest a brocade expert should check the switch configuration. One possible cause could be the switch running in <strong>fail-open mode (basically a hub)</strong>, which would degrade the overall performance of your network significantly. However that's just speculation. One cannot tell, based on the amount of information given.</p><blockquote><p>The stacks are trunked together using 8 gbit links between the stacks.</p></blockquote><p>Is this a vendor specific link (virtual chassis link / multi chassis link (MCT) / Inter chassis link (ICL)) or is it LACP (Link Aggregation)?</p><blockquote><p>I also have a transparent ips system intercepting all traffic between the stacks (in line) and noticed it things some mac spoofing happening. I figure that is because traffic from a mac comes from one link one time and then another link another time, i.e. port-1 then later from port-2.</p></blockquote><p>If the IPS is between those trunk ports, I assume it's LACP (as there is usally no way to tap into vendor specific links). If it's LACP it's perfectly normal to see the same (source) MAC address on both ports, depending on the hash method defined for LACP (round-robin, L3, L4). You would also see the same MAC address on another link, for a connection to a different endpoint!</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 May '12, 10:53</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 31 May '12, 19:24</p></div></div><div id="comments-container-11499" class="comments-container"><span id="11501"></span><div id="comment-11501" class="comment"><div id="post-11501-score" class="comment-score"></div><div class="comment-text"><p>Kurt,</p><p>I can give some more insight to my specific situation. This was a simple TCP SYN from one machine to another. One machine on the same network as mine, the sending machine on a completely different network. No SPAN sessions are configured on my switch.</p><p>This cancels out the broadcast theory at both layer 2 and 3 and the fact that it's being routed makes the overload situation seem like a reach. I will definitely look more into that though and see if any bugs have been reported for the IOS we are running. Thanks for throwing some more options out and giving a fresh point of view.</p></div><div id="comment-11501-info" class="comment-info"><span class="comment-age">(31 May '12, 11:09)</span> davj1</div></div></div><div id="comment-tools-11499" class="comment-tools"></div><div class="clear"></div><div id="comment-11499-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


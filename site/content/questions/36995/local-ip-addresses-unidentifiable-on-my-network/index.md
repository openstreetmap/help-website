+++
type = "question"
title = "Local IP addresses unidentifiable on my network"
description = '''I just want to know how they got there, when I pinged the address, the local address turned into an AT&amp;amp;T address.  When an attempt is made to ping those local IP addresses that are on a different subnet, the following happens:    It makes no sense to me, as I&#x27;m able to ping a local network on a ...'''
date = "2014-10-12T15:12:00Z"
lastmod = "2014-10-20T03:36:00Z"
weight = 36995
keywords = [ "snmp", "weird", "snmpwireshark", "traffic" ]
aliases = [ "/questions/36995" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Local IP addresses unidentifiable on my network](/questions/36995/local-ip-addresses-unidentifiable-on-my-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36995-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I just want to know how they got there, when I pinged the address, the local address turned into an AT&amp;T address.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/snmptrafficweird.PNG" alt="alt text" /></p><p>When an attempt is made to ping those local IP addresses that are on a different subnet, the following happens:</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Ping_to109.PNG" alt="alt text" /></p><p><img src="https://osqa-ask.wireshark.org/upfiles/Pingto111.PNG" alt="alt text" /></p><p><img src="https://osqa-ask.wireshark.org/upfiles/pingto112.PNG" alt="alt text" /></p><p>It makes no sense to me, as I'm able to ping a local network on a different subnet, let it's showing up as SNMP traffic. Not only that, when pinged the network resolves the 12.83.88.97 and 12.83.88.105 as its actual IP address (both of which are public class A IP addresses belonging to AT&amp;T): <a href="http://www.whois.com/whois/12.83.88.105">http://www.whois.com/whois/12.83.88.105</a> and <a href="http://www.whois.com/whois/12.83.88.97">http://www.whois.com/whois/12.83.88.97</a></p><p>Anyone know why I'm seeing this Local network traffic? It shouldn't be there I believe.</p></div><div id="question-tags" class="tags-container tags">snmp weird snmpwireshark traffic</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Oct '14, 15:12</strong></p><img src="https://secure.gravatar.com/avatar/4784c5fb1a0142030d51a339706a456c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Beldum&#39;s gravatar image" /><p>Beldum<br />
<span class="score" title="49 reputation points">49</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Beldum has no accepted answers">0%</span></p></img></div></div><div id="comments-container-36995" class="comments-container"><span id="36996"></span><div id="comment-36996" class="comment"><div id="post-36996-score" class="comment-score"></div><div class="comment-text"><p>Anyone? It would be nice to see a response.</p></div><div id="comment-36996-info" class="comment-info"><span class="comment-age">(12 Oct '14, 20:33)</span> Beldum</div></div><span id="36998"></span><div id="comment-36998" class="comment"><div id="post-36998-score" class="comment-score"></div><div class="comment-text"><p>What is your own IP? And can you show the quote of the ICMP packet? That's what should tell why you get an answer like that, but your screenshot doesn't show.</p></div><div id="comment-36998-info" class="comment-info"><span class="comment-age">(12 Oct '14, 22:39)</span> Jasper ♦♦</div></div><span id="36999"></span><div id="comment-36999" class="comment"><div id="post-36999-score" class="comment-score"></div><div class="comment-text"><p>My own local IP address is 192.168.10.101. When you say the quote of the ICMP packet, what do you mean by that? I'm not too familiar with the quote.</p></div><div id="comment-36999-info" class="comment-info"><span class="comment-age">(12 Oct '14, 23:41)</span> Beldum</div></div><span id="37007"></span><div id="comment-37007" class="comment"><div id="post-37007-score" class="comment-score"></div><div class="comment-text"><p>Isn't this just more of the same from your previous <a href="https://ask.wireshark.org/questions/36984/i-am-seeing-snmp-traffic-on-my-local-network">question</a>? Now it's getting out of your local subnet via your default gateway, and some device in your ISP's network is reporting that it can't route to the destination.</p></div><div id="comment-37007-info" class="comment-info"><span class="comment-age">(13 Oct '14, 03:41)</span> grahamb ♦</div></div><span id="37020"></span><div id="comment-37020" class="comment"><div id="post-37020-score" class="comment-score"></div><div class="comment-text"><p>Ok Ghraham, the purpose for the question is to make sure that those IP addresses that I listed which are not a part of my local network, should they actually be showing up in SNMP traffic? They are on a different subnet. That's my main concern.</p></div><div id="comment-37020-info" class="comment-info"><span class="comment-age">(13 Oct '14, 10:31)</span> Beldum</div></div><span id="37022"></span><div id="comment-37022" class="comment not_top_scorer"><div id="post-37022-score" class="comment-score"></div><div class="comment-text"><p>I suspect that they are still being generated by some widget on your PC searching for an external device, you'll need to use something like MS Message Analyzer that can capture the traffic and show you the sending process to determine what the actual process is.</p></div><div id="comment-37022-info" class="comment-info"><span class="comment-age">(13 Oct '14, 10:38)</span> grahamb ♦</div></div><span id="37023"></span><div id="comment-37023" class="comment not_top_scorer"><div id="post-37023-score" class="comment-score"></div><div class="comment-text"><p>Thanks Grahamb, I really appreciate that assistance. I'll try to check it out.</p></div><div id="comment-37023-info" class="comment-info"><span class="comment-age">(13 Oct '14, 10:39)</span> Beldum</div></div></div><div id="comment-tools-36995" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-36995-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37182"></span>

<div id="answer-container-37182" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37182-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I'd say Graham's answer about the pings is right: when you ping something not in your subnet then it goes out your default router to AT&amp;T's network which sends you back an ICMP saying you can't get to that subnet (through AT&amp;T).</p><p>For the SNMP requests whatever the 192.168.10.11 device is, it seems to have that 192.168.1.112 destination programmed into it. Presumably it's not actually succeeding in talking to it since you can't ping it either (and, if this is a home installation with only one subnet, presumably it's not actually something you should be able to reach).</p><p>If you're worried about the SNMP requests go find whatever 192.168.10.11 is and try to find some configuration item about 192.168.1.112. Or just unplug the thing. ;-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Oct '14, 03:36</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></img></div></div><div id="comments-container-37182" class="comments-container"></div><div id="comment-tools-37182" class="comment-tools"></div><div class="clear"></div><div id="comment-37182-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


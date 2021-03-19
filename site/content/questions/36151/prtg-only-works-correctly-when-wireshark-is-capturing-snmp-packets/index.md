+++
type = "question"
title = "PRTG only works correctly when wireshark is capturing snmp packets"
description = '''Hi guys, i have the curious problem that my PRTG snmp sensors does only work with a running wireshark capturing session. Can you tell me what the problem can be or how i can solve it.'''
date = "2014-09-10T04:31:00Z"
lastmod = "2014-09-10T05:11:00Z"
weight = 36151
keywords = [ "snmp", "prtg" ]
aliases = [ "/questions/36151" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [PRTG only works correctly when wireshark is capturing snmp packets](/questions/36151/prtg-only-works-correctly-when-wireshark-is-capturing-snmp-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36151-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi guys, i have the curious problem that my PRTG snmp sensors does only work with a running wireshark capturing session. Can you tell me what the problem can be or how i can solve it.</p></div><div id="question-tags" class="tags-container tags">snmp prtg</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Sep '14, 04:31</strong></p><img src="https://secure.gravatar.com/avatar/5c26d858658122acbd3483917ae5581c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="burge&#39;s gravatar image" /><p>burge<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="burge has no accepted answers">0%</span></p></div></div><div id="comments-container-36151" class="comments-container"></div><div id="comment-tools-36151" class="comment-tools"></div><div class="clear"></div><div id="comment-36151-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36155"></span>

<div id="answer-container-36155" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36155-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Check the MAC addresses of the SNMP packets. They are most likely not having the destination MAC of the system you want them to be received on, which is why the NIC of that system discards them (unless Wireshark is running, which means the card accepts any frame).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Sep '14, 05:11</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-36155" class="comments-container"><span id="36156"></span><div id="comment-36156" class="comment"><div id="post-36156-score" class="comment-score"></div><div class="comment-text"><p>You are right. I have a 4 port bond0 configured and sometimes Packets with the mac of a member comes in. How do i implement that the packets always have the mac of the bonding interface as destination?</p></div><div id="comment-36156-info" class="comment-info"><span class="comment-age">(10 Sep '14, 05:32)</span> burge</div></div><span id="36157"></span><div id="comment-36157" class="comment"><div id="post-36157-score" class="comment-score"></div><div class="comment-text"><p>good question - you'll have to figure out why the sender got the wrong MAC in the first place. I guess there are ARP requests for the IP of the target system that sometimes carry the wrong MAC. You need determine why that happens; I guess some kind of misconfiguration is involved.</p><p>Does the switch where the bond members connect to also know that those links are supposed to be treated as a bonded channel? Otherwise you'll get into different kinds of trouble all the time.</p></div><div id="comment-36157-info" class="comment-info"><span class="comment-age">(10 Sep '14, 05:43)</span> Jasper ♦♦</div></div><span id="36160"></span><div id="comment-36160" class="comment"><div id="post-36160-score" class="comment-score"></div><div class="comment-text"><p>Yes. Bonding is already configured on the switch</p></div><div id="comment-36160-info" class="comment-info"><span class="comment-age">(10 Sep '14, 05:58)</span> burge</div></div><span id="36162"></span><div id="comment-36162" class="comment"><div id="post-36162-score" class="comment-score"></div><div class="comment-text"><p>Hint: please use comments instead of answers if you have to add something ;-)</p><p>If bonding is fine, you need to capture traffic at one of the sources for the SNMP packets to see what kind of ARP replies they get when looking for the SNMP destination, and which system sends them. Usually, ARP replies come from the destination MAC, so if you see that the bounded NICs respond with bad values you may have a problem with the bond software.</p></div><div id="comment-36162-info" class="comment-info"><span class="comment-age">(10 Sep '14, 06:01)</span> Jasper ♦♦</div></div></div><div id="comment-tools-36155" class="comment-tools"></div><div class="clear"></div><div id="comment-36155-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


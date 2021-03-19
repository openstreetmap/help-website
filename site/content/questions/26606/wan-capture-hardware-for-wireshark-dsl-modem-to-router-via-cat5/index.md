+++
type = "question"
title = "WAN Capture Hardware for WireShark (DSL Modem to Router via Cat5)"
description = '''Hello, I am looking at the feasibilty of using Wireshark to passively monitor my WAN traffic. I am particularly interested in seeing if I have traffic going to US states (or even foreign destinations) where we have no reason to be comunicating with. I have not used Wireshark before, but a quick stud...'''
date = "2013-10-31T18:54:00Z"
lastmod = "2013-11-01T06:33:00Z"
weight = 26606
keywords = [ "wanmonitordslrouter" ]
aliases = [ "/questions/26606" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [WAN Capture Hardware for WireShark (DSL Modem to Router via Cat5)](/questions/26606/wan-capture-hardware-for-wireshark-dsl-modem-to-router-via-cat5)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26606-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I am looking at the feasibilty of using Wireshark to passively monitor my WAN traffic. I am particularly interested in seeing if I have traffic going to US states (or even foreign destinations) where we have no reason to be comunicating with. I have not used Wireshark before, but a quick study shows it will easily give me the endpoint addresses I seek. I am trying to determine what hardware I need to put in place as well as quickly get up the learning curve.</p><p>The hardware config is simply a DSL modem that connects to a router via a Cat5 cable.<br />
</p><p>TWO QUESTIONS:</p><p>What hardware device do I need to get wireshark passively patched in and capturing all WAN traffic without interfereing with the WAN link?</p><p>I have a JMicron PCI Express Gigabit Ethernet Adapter in a notebook I can dedicate to the monitor process. How can I determine if this can be used with WireShark for passive monitoring?</p><p>Any suggestions for smarter/better ways to handle this would be welcome!</p><p>I appreciate any help that you might offer to a WS newbie!!!</p><p>Thanks! Bruce</p></div><div id="question-tags" class="tags-container tags">wanmonitordslrouter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Oct '13, 18:54</strong></p><img src="https://secure.gravatar.com/avatar/2c1320d3cfcca512d1ffa5ec51aa8f69?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bruce52&#39;s gravatar image" /><p>Bruce52<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bruce52 has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 31 Oct '13, 19:02</p></div></div><div id="comments-container-26606" class="comments-container"><span id="26609"></span><div id="comment-26609" class="comment"><div id="post-26609-score" class="comment-score"></div><div class="comment-text"><p>Note that neither Wireshark, or tshark, is suitable for long term monitoring. Both applications build up state about the traffic and will eventually run out of memory, the rate at which this happens depends on the traffic and any capture filters you apply.</p></div><div id="comment-26609-info" class="comment-info"><span class="comment-age">(01 Nov '13, 03:50)</span> grahamb ♦</div></div></div><div id="comment-tools-26606" class="comment-tools"></div><div class="clear"></div><div id="comment-26606-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26617"></span>

<div id="answer-container-26617" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26617-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I am particularly interested in <strong>seeing if I have traffic going to US states</strong> (or even foreign destinations) where we have no reason to be comunicating with.</p></blockquote><p>Forget about that, seriously!</p><p>Even after what we have learned in the last couple of months, about the NSA and secret backdoors, that might have been placed in products (routers etc.), especially if they are manufactured by US companies, you won't see any traffic to the NSA headquarters or anywhere else, as that would be ways to easy to detect.</p><p>Chances are much better to see traffic from an infected PC in your network, that tries to contact its C&amp;C server.</p><p>Anyway, if there is a backdoor in your router it will certainly be triggered by a special byte sequence from the outside, like: 'sesame open your doors, I'm your master' (at least I would have chosen that as a 'door opener' ;-)) Nobody knows if there is a backdoor in your router and manufactures are obviously forced to silence about that issue - otherwise --&gt; prison (see the <a href="http://www.google.de/url?sa=t&amp;rct=j&amp;q=&amp;esrc=s&amp;source=web&amp;cd=3&amp;cad=rja&amp;ved=0CEoQtwIwAg&amp;url=http%3A%2F%2Fwww.democracynow.org%2F2013%2F8%2F13%2Fexclusive_owner_of_snowdens_email_service&amp;ei=ealzUsHWBImh4gScmYH4Cg&amp;usg=AFQjCNEomDslcifFzS3uV9F3M95QwrRneA&amp;bvm=bv.55819444,d.bGE">Lavabit case, where the owner of the company was not even allowed to talk with this lawyer about all details. wow!</a> ).</p><p>So, (<strong>hypothetically</strong>) if your router sees a packet (ICMP, IP, UDP, TCP - who knows what) with that string, it might open a secret management interface or shell access for the sender IP address.</p><p>So, <strong>you will only see that kind of traffic</strong> if <strong>you are already being monitored</strong> because <strong>you are on one of those terror and/or "axis of evil" lists</strong> of whatever TLA (CIA, NSA, WTF, etc.).</p><p><strong>However</strong>: In that case I would be <strong>really scared</strong> if I were you and wouldn't care too much about monitoring that traffic! ;-))</p><p>Anyway: If you really want to monitor that traffic.</p><ul><li>take into account what @grahamb said about long term monitoring</li><li>Take a look at the following Wiki article: <code>http://wiki.wireshark.org/CaptureSetup/Ethernet</code>. You can use a hub, a mirror port on a <a href="http://ask.wireshark.org/questions/13892/port-mirror-switch">small managed switch</a>, or you can use a bridge of two interfaces on your Wireshark PC.</li></ul><p>Method 1: HUB or switch with port mirroring/monitoring</p><pre><code>LAN ---- router ---- HUB/SWITCH --- DSL modem
                      |
                      |
                   Wireshark</code></pre><p>Method 2: Wireshark PC with two interfaces, configured as a bridge.</p><pre><code>LAN ---- router ---- Wireshark --- DSL modem</code></pre><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Nov '13, 06:33</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-26617" class="comments-container"></div><div id="comment-tools-26617" class="comment-tools"></div><div class="clear"></div><div id="comment-26617-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


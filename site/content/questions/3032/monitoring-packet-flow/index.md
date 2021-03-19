+++
type = "question"
title = "monitoring packet flow"
description = '''Hello, I need to make sure that our data flow, specifically our email flow, is following a certain path, or I should say to find out what path it comes in and out of our network. For example, when email enters our network we want to make sure that it flows seamlessly in a correct manner as well as w...'''
date = "2011-03-22T14:11:00Z"
lastmod = "2011-03-25T01:47:00Z"
weight = 3032
keywords = [ "flow", "packet" ]
aliases = [ "/questions/3032" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [monitoring packet flow](/questions/3032/monitoring-packet-flow)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3032-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I need to make sure that our data flow, specifically our email flow, is following a certain path, or I should say to find out what path it comes in and out of our network. For example, when email enters our network we want to make sure that it flows seamlessly in a correct manner as well as when it leaves our network, not looping around, getting stuck somewhere for unnecessary amount of time, etc.. Our network is quite complex so I want to know if there is a way I can follow email traffic and see the actual path it takes from the client to the gateway and vice versa. I would like to see some sort of report I can look at to see all the different devices it stops at etc..Is it possible to do this with Wireshark? Thanks!</p></div><div id="question-tags" class="tags-container tags">flow packet</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Mar '11, 14:11</strong></p><img src="https://secure.gravatar.com/avatar/2ecfaaf06b51f1ee754784019619043a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tolinrome&#39;s gravatar image" /><p>tolinrome<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tolinrome has no accepted answers">0%</span></p></div></div><div id="comments-container-3032" class="comments-container"></div><div id="comment-tools-3032" class="comment-tools"></div><div class="clear"></div><div id="comment-3032-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="3070"></span>

<div id="answer-container-3070" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3070-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>No. You can't unless you capture at every single router hop. There are many factors that complicate this. For example, when you have redundant paths in the network, the forwarding decision is not made based on the routing table (RIB) but the forwarding table (FIB). So things like Cisco's CEF come into picture. But I think you're worried about the wrong things.</p><p>Your network can't be that complicated, and if routing loops are common enough to worry about, then the infrastructure is fundamentally flawed.<br />
</p><p>In a modern day network, routers and switches are <em>rarely</em> the bottleneck. Especially if you're talking about email servers.<br />
</p><p>What you may want to analyze are TTL fields as the packets traverse your network. So long as it doesn't vary by that much, you are most likely taking the same route.<br />
</p><p>Do you have a Cisco based network? If so, I have a Visio program that maps out the network at the CEF level. So the macro takes source IP, source IP's GW, and destination. It then logs into every router and looks at the CEF table. It only works for IOS based routers and will not work on Nexus platform.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Mar '11, 16:36</strong></p><img src="https://secure.gravatar.com/avatar/63805f079ac429902641cad9d7cd69e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hansangb&#39;s gravatar image" /><p>hansangb<br />
<span class="score" title="791 reputation points">791</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hansangb has 7 accepted answers">12%</span> </br></br></p></div></div><div id="comments-container-3070" class="comments-container"></div><div id="comment-tools-3070" class="comment-tools"></div><div class="clear"></div><div id="comment-3070-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="3085"></span>

<div id="answer-container-3085" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3085-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>IP has an option that encourages routers to record their own IP address in the IP header. Try this on a Windows system:</p><pre><code>ping -r 9 1.2.3.4</code></pre><p>The option "-r 9" leaves room for a maximum of 9 devices to record their IP address.</p><p>The option is from the "good old days" of the Internet. So your firewall, IPS or other device might drop the packet because we most networks don't need any option in the IP header.</p><p>If you just want to see which mail servers process the message: Try looking at the X-headers where the mail servers, SPAM gateways and virus filters all leave a time stamp (including their IP address). These headers are usually hidden from the user. Each program has an option to make them visible.</p><p>Good hunting!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Mar '11, 09:57</strong></p><img src="https://secure.gravatar.com/avatar/3b60e92020a427bb24332efc0b560943?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="packethunter&#39;s gravatar image" /><p>packethunter<br />
<span class="score" title="2137 reputation points"><span>2.1k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="packethunter has 8 accepted answers">8%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 24 Mar '11, 09:59</p></div></div><div id="comments-container-3085" class="comments-container"><span id="3092"></span><div id="comment-3092" class="comment"><div id="post-3092-score" class="comment-score"></div><div class="comment-text"><p>But because the header doesn't have the room to record the full route, it's not much use in a modern day network. But if you're persistent enough, you could go from router to router (radius of the record option limitation) and map it out. The only other caveat however, is that CEF behavior <em>can</em> change based on tcp port numbers. It's easy enough for someone to include port numbers in the CEF hash calculation, so traceroute/ping-record may not take the same hop. Just something to be aware of.</p></div><div id="comment-3092-info" class="comment-info"><span class="comment-age">(24 Mar '11, 16:16)</span> hansangb</div></div></div><div id="comment-tools-3085" class="comment-tools"></div><div class="clear"></div><div id="comment-3085-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="3106"></span>

<div id="answer-container-3106" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3106-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Since you are precisely referring to email flow - why don't check email headers in any email client to see what all smtp relay servers it has used. That should give you directions of the exact mail flow.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Mar '11, 01:47</strong></p><img src="https://secure.gravatar.com/avatar/d1e5efe891c907bf6be8231eca9db31a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vijay%20Gharge&#39;s gravatar image" /><p>Vijay Gharge<br />
<span class="score" title="36 reputation points">36</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vijay Gharge has no accepted answers">0%</span></p></div></div><div id="comments-container-3106" class="comments-container"></div><div id="comment-tools-3106" class="comment-tools"></div><div class="clear"></div><div id="comment-3106-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


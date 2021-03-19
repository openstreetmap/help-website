+++
type = "question"
title = "Troubleshooting Network Slowness by Comparing I/O Graphs"
description = '''Hi Fellow Wireshark Enthusiasts I&#x27;m having a hard time troubleshooting a Real Time Stocks Trading Application. Apparently, this is the only Real-Time Application in the company I&#x27;m working at that&#x27;s experiencing slowness. Here are the Steps I&#x27;ve done so far: Performed Traceroute from App to DB, Clie...'''
date = "2014-08-08T03:07:00Z"
lastmod = "2014-08-11T14:43:00Z"
weight = 35323
keywords = [ "application", "packet-capture", "cisco", "slowness" ]
aliases = [ "/questions/35323" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Troubleshooting Network Slowness by Comparing I/O Graphs](/questions/35323/troubleshooting-network-slowness-by-comparing-io-graphs)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35323-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Fellow Wireshark Enthusiasts</p><p>I'm having a hard time troubleshooting a Real Time Stocks Trading Application. Apparently, this is the only Real-Time Application in the company I'm working at that's experiencing slowness. Here are the Steps I've done so far:</p><p>Performed Traceroute from App to DB, Client to App, DB to App, <strong>traceroute averages at 4ms.</strong></p><p>I have also performed Sniffing using Wireshark. At first I only sniffed one device at a time and that didn't give me the details so I sniffed two devices at a time: The Switch closest to Trade Application Server and the Switch closest to the Database Server. I <strong>compared their I/O graphs</strong> and I've found out that the <strong>delay of packet transmission from App to DB is the same on both switches</strong> but the latency of DB to App is different on both switches. <strong>The switch closest to the db shows 10ms or less latency</strong> while the <strong>switch closest to the Trade server shows 100 - 254ms delay!.</strong></p><p><strong>One problem I'm having with wireshark though is</strong> that all our <strong>switches(except those that connects to the client's PC)perform loads balancing</strong> so it's hard to monitor a specific transaction. <strong>Also, the communication between the Client PC to App and App to DB is encrypted so what I'm just looking at is the</strong> tcp.time_delta****</p><p>Unfortunately, I don't know if the high delay is caused by the Application Response Time or by the Network Transmission. Also, the are a lot of network devices in between the App, DB and the Client's PC, around 30 devices including the 2 two firewalls. I'm planning on sniffing at least all the devices between App and DB excluding the firewalls and that would take me 6 Laptops running at the same time.</p><p>Before I perform that though, I have a few questions:</p><p>1.) Am I doing the troubleshooting process correctly?</p><p>2.) Are there other things I could look at/check?</p><p>3.) Does the number of network hops increases the latency? If yes, does it vary between switches, routers and firewalls?</p><p>4.) The vendor for the trading application recommends to implement QoS for this trading application. Is that really necessary?</p><p>Thank you in advance for all your help and sorry for the long block of text. :)</p></div><div id="question-tags" class="tags-container tags">application packet-capture cisco slowness</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Aug '14, 03:07</strong></p><img src="https://secure.gravatar.com/avatar/baaa6678eb41fc5aa58992954bab2fc8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sharknado&#39;s gravatar image" /><p>Sharknado<br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sharknado has no accepted answers">0%</span></p></div></div><div id="comments-container-35323" class="comments-container"><span id="35390"></span><div id="comment-35390" class="comment"><div id="post-35390-score" class="comment-score"></div><div class="comment-text"><p>"switch closest to the Trade server shows 100 - 254ms delay!" it's very unlikely that a switch would be buffering/queueing frames this long. How do you believe you are determining this result?</p><p>It sounds like a reasonable approach you are using. It is probably important to determine application response time near the server. On many occasions I have been asked to troubleshoot or diagnose "network performance issues". Only to find things like DNS queries being unresolved correctly and resulting in default fallbacks (leading to seconds of delays), or authentication issues (where client and server spend a lot of negotiating there way around various options), application running in debug mode and spending precious seconds executing wasted processing, and finally poorly understood database queries that consistently chew up seconds as the many CPUs seem to pull in the whole database index while they search for a result. This seems to be more prevalent in custom or bespoke application when developers really don't have a good handle on what they are asking their server to do - and only when they deploy to production do they realise that going from a handful users in dev doesn't scale to 100's of real world users.</p><p>I usually try to even do wireshark captures on the server (running transactions to localhost), and also have run their CPU/disk perf mon tools when the transactions are being run.</p></div><div id="comment-35390-info" class="comment-info"><span class="comment-age">(10 Aug '14, 18:30)</span> martyvis</div></div></div><div id="comment-tools-35323" class="comment-tools"></div><div class="clear"></div><div id="comment-35323-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="35375"></span>

<div id="answer-container-35375" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35375-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>this is <strong>the only Real-Time Application</strong> in the company I'm working at <strong>that's experiencing slowness</strong>.</p></blockquote><p>please define 'slowness' first.</p><blockquote><p>1.) Am I doing the troubleshooting process correctly?</p></blockquote><p>basically yes. In details: hard to say as you did not provide enough information about the whole application data flow.</p><blockquote><p>2.) Are there other things I could look at/check?</p></blockquote><p>Obviously the logs of all involved systems (app server, db server, firewalls, etc.)</p><blockquote><p>3.) Does the number of network hops increases the latency?</p></blockquote><p>Sure, every node needs some time to process the packet.</p><blockquote><p>If yes, does it vary between switches, routers and firewalls?</p></blockquote><p>sure, as they need a different amount of time to process the packet. A firewall usually needs more time than a switch, as it has to do much more with the packet. It also depends on the load (CPU, line, etc.)</p><blockquote><p>4.) The vendor for the trading application recommends to implement QoS for this trading application. Is that really necessary?</p></blockquote><p>Well, hard to tell with the amount of information you provided so far. If the traffic is passing the internet, you can forget QoS, as you won't have any influence on the packet as soon as it leaves your network.</p><p>If you implement QoS you'll have to do it properly on <strong>all involved systems</strong>. You mentioned 30 devices <strong>between</strong> the client and the backend. So, good luck with that endeavor ;-)) But if this is really a 'real time' application (please define that as well), you'll probably need QoS to make the application work fast enough.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Aug '14, 07:27</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-35375" class="comments-container"></div><div id="comment-tools-35375" class="comment-tools"></div><div class="clear"></div><div id="comment-35375-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="35423"></span>

<div id="answer-container-35423" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35423-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi sharknado,</p><p>An alternative approach is to use a Wireshark plugin called TRANSUM. You can find a demo of using it for a similar problem at <a href="http://www.lovemytool.com/blog/2014/08/transum-analyzing-a-website-problem-by-paul-offord.html">http://www.lovemytool.com/blog/2014/08/transum-analyzing-a-website-problem-by-paul-offord.html</a></p><p>TRANSUM is available at <a href="http://www.tribelabzero.com/resources">http://www.tribelabzero.com/resources</a></p><p>It's a top down approach. So you start by identifying which flows are a problem and then drill down to service or network problem.</p><p>Best regards...Paul</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Aug '14, 14:43</strong></p><img src="https://secure.gravatar.com/avatar/2e1b4057f2ff59fe059b23cc6571abaf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PaulOfford&#39;s gravatar image" /><p>PaulOfford<br />
<span class="score" title="131 reputation points">131</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="32 badges"><span class="silver">●</span><span class="badgecount">32</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PaulOfford has 5 accepted answers">11%</span></p></div></div><div id="comments-container-35423" class="comments-container"></div><div id="comment-tools-35423" class="comment-tools"></div><div class="clear"></div><div id="comment-35423-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


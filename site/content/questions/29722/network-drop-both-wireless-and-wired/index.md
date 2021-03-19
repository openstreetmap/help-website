+++
type = "question"
title = "Network Drop both Wireless and Wired"
description = '''I&#x27;m writing on behalf of a small school district. In early January, a colleague and myself installed 20 Ubiquiti Unifi AP-Pro devices as well as about 20, 10/100/1000 hp procurve switches. Two schools are connected by Cisco Aironet. Towards the end of January we started experiencing high latency and...'''
date = "2014-02-11T16:06:00Z"
lastmod = "2014-02-12T01:17:00Z"
weight = 29722
keywords = [ "latency", "drop", "newbie", "network", "slowness" ]
aliases = [ "/questions/29722" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Network Drop both Wireless and Wired](/questions/29722/network-drop-both-wireless-and-wired)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29722-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm writing on behalf of a small school district. In early January, a colleague and myself installed 20 Ubiquiti Unifi AP-Pro devices as well as about 20, 10/100/1000 hp procurve switches. Two schools are connected by Cisco Aironet. Towards the end of January we started experiencing high latency and network drop throughout the district. I am in over my head trying to troubleshoot and someone pointed me to Wireshark. I don't have any formal education in networking and looking at the data in Wireshark is intimidating to say the least. Can anyone help me interpret some of our data to help isolate where our issue might be? If not, is there a good starting point or list of things to do in Wireshark somewhere that would get me going down the right path?<br />
</p><p>I am thankful for any help.</p></div><div id="question-tags" class="tags-container tags">latency drop newbie network slowness</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Feb '14, 16:06</strong></p><img src="https://secure.gravatar.com/avatar/c8e8623059551f4a25631c775e533953?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tiosend&#39;s gravatar image" /><p>tiosend<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tiosend has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-29722" class="comments-container"></div><div id="comment-tools-29722" class="comment-tools"></div><div class="clear"></div><div id="comment-29722-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29739"></span>

<div id="answer-container-29739" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29739-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I don't have any formal education in networking and <strong>looking at the data in Wireshark is intimidating to say the least</strong>.</p></blockquote><p>I don't want to discourage you, but the kind of problem you are describing, requires somebody with a pretty good understanding of the network, protocols and devices (switches, router, firewalls, server) in place. Without that knowledge, you will be simply lost, even if you get some hints from me. So, before I give you those hints, I strongly recommend to hire a networking professional to troubleshoot the problem for you.</p><p>Now, here are my hints:</p><ul><li>If the whole network is affected (as you say), it could be a central network component and/or server that all users are trying to use/access. So, first get some detailed reports of the users <strong>what exactly does not work</strong> (access to target systems, servers, etc.) and <strong>when exactly the problem shows up</strong>. If you are lucky, you will find similar reports from different users which helps to limit your search to a few core components.</li><li>If the whole network is affected, Wireshark is (usually) that second best thing to start with, because you don't know where to start capturing traffic. Of course, you could try to capture at one of the core components (core switch), but the amount of traffic there is tremendous and without a profound knowledge of the protocols and networking in general, you will be overwhelmed by that flood of data. Unfortunately, there is no "best practice approach" for every network problem, so even if you have that data from the core network, it would be hard to tell you what to look for. I usually look for 'unusual patterns', but how an unusual pattern looks like, is only stored in by brain, created by experience. I don't know how to dump that information in a usable way ;-)</li></ul><p>So, to sum it up. Here is how I would try to figure out the problem</p><ul><li>Talk intensively to different user groups and ask them <strong>what kind of problems</strong> they experience. <strong>When</strong> do the problems show up and <strong>what exactly is affected</strong>. Don't accept answer like: The whole network is slower than before.</li><li>Filter and aggregate the answers. Maybe you'll find a common reason for the problems (central server, central switch, DNS, Firewalls, etc.)</li><li>Look at all switch logs!! If logging is not enabled, do it now and check the logs later</li><li>Monitor the switch port counters (there are a lot of tools available. google will help. Do you see 'unusual patterns' at the times when people report the problems? If so, where (which switch) do you see those patterns (like massive spikes or drops in number of packets)</li><li>If there is an 'unusual pattern' somewhere, capture the traffic 'near that place/component' with Wireshark and try to figure out what's going on. Unfortunately, there is no 'best practice' approach for this and you'll need a lot of experience to sort things out. You could start with the statistics functions of Wireshark (<a href="http://www.wireshark.org/docs/wsug_html_chunked/ChUseStatisticsMenuSection.html">Menu: Statistics</a>).</li></ul><p>The 'good thing' of your problem is: After you have done all that, you will have a much better understanding of your network architecture and a much better understanding of networking/protocols in general ;-))</p><p>Good luck!</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Feb '14, 01:17</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 12 Feb '14, 01:34</p></div></div><div id="comments-container-29739" class="comments-container"></div><div id="comment-tools-29739" class="comment-tools"></div><div class="clear"></div><div id="comment-29739-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


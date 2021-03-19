+++
type = "question"
title = "Wireshark not seeing traffic from other machines on virtual network"
description = '''I&#x27;m trying to run a network of three Ubuntu VMs in host only mode on VirtualBox. Two are to send/recieve messages to one another while the third has wireshark to intercept traffic. They&#x27;re all listed as being on eth0, but when I attempt to view the capture options for eth0 in wireshark, it lists onl...'''
date = "2015-04-24T12:02:00Z"
lastmod = "2015-04-25T04:33:00Z"
weight = 41797
keywords = [ "capture-setup", "virtualbox", "ubuntu" ]
aliases = [ "/questions/41797" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark not seeing traffic from other machines on virtual network](/questions/41797/wireshark-not-seeing-traffic-from-other-machines-on-virtual-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41797-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to run a network of three Ubuntu VMs in host only mode on VirtualBox. Two are to send/recieve messages to one another while the third has wireshark to intercept traffic. They're all listed as being on eth0, but when I attempt to view the capture options for eth0 in wireshark, it lists only the IP of the VM wireshark is installed on.</p><p>Why isn't wireshark seeing traffic from my other two VMs?</p></div><div id="question-tags" class="tags-container tags">capture-setup virtualbox ubuntu</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Apr '15, 12:02</strong></p><img src="https://secure.gravatar.com/avatar/2b6aa7d80381b4ebf9815f0c9d238c46?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ab0mber89&#39;s gravatar image" /><p>ab0mber89<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ab0mber89 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 Apr '15, 11:42</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-41797" class="comments-container"><span id="41807"></span><div id="comment-41807" class="comment"><div id="post-41807-score" class="comment-score"></div><div class="comment-text"><p>What do you mean by "They're all listed as being on eth0"? Listed where?</p><p>Do you mean "Why isn't wireshark seeing traffic from my other two VMs?", or "Why isn't Wireshark showing multiple IP addresses for eth0 in the capture options dialog?" (The two are <em>not</em> the same question; the IP addresses it shows are the IP addresses that the host running Wireshark has for that interface, <em>not</em> the IP addresses from which it sees traffic.)</p></div><div id="comment-41807-info" class="comment-info"><span class="comment-age">(24 Apr '15, 16:18)</span> Guy Harris ♦♦</div></div><span id="41823"></span><div id="comment-41823" class="comment"><div id="post-41823-score" class="comment-score"></div><div class="comment-text"><p>I suppose I should be more clear. Why won't wireshark see the traffic from my other two VMs?</p><p>When I said they're listed as being on eth0, I meant when I used ifconfig on each VM it listed their IP addresses for the host only network under eth0, which is why I tried to capture traffic from that interface. I also tried the 'any' interface offered by wireshark after trying to capture traffic from eth0 proved unsuccessful. I just want this third VM to be able to see traffic between the other two and capture it, and I'm not sure how to make it happen.</p></div><div id="comment-41823-info" class="comment-info"><span class="comment-age">(25 Apr '15, 00:37)</span> ab0mber89</div></div></div><div id="comment-tools-41797" class="comment-tools"></div><div class="clear"></div><div id="comment-41797-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41824"></span>

<div id="answer-container-41824" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41824-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>What I have understood from your explanation, you are looking at individual/local eth0 interfaces of each of the individual VM, it is not a common eth0 interface from where you can place a hook to get the captured traffic. So it will not work this way. IMHO.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Apr '15, 04:33</strong></p><img src="https://secure.gravatar.com/avatar/abebafb6d8867b406b5735482fc1e828?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mushtaq%20Hussain&#39;s gravatar image" /><p>Mushtaq Hussain<br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mushtaq Hussain has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 Apr '15, 16:18</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-41824" class="comments-container"><span id="41837"></span><div id="comment-41837" class="comment"><div id="post-41837-score" class="comment-score"></div><div class="comment-text"><blockquote><p>What I have understood from your explanation, you are looking at individual/local eth0 interfaces of each of the individual VM, it is not a common eth0 interface from where you can place a hook to get the captured traffic.</p></blockquote><p>Correct. The "any" interface is <em>also</em> an individual/local interface. It's best to think of the virtual network as being similar to a real network, with multiple independent virtual machines, each of which has its own independent network interfaces, which will <em>not</em> show the IP addresses of other machines' interfaces - and the virtual network probably looks like a <em>switched</em> network, so that a host on the network won't necessarily see traffic between other hosts on the network.</p></div><div id="comment-41837-info" class="comment-info"><span class="comment-age">(25 Apr '15, 11:46)</span> Guy Harris ♦♦</div></div><span id="41838"></span><div id="comment-41838" class="comment"><div id="post-41838-score" class="comment-score"></div><div class="comment-text"><p>I understand. So how do I get wireshark to see traffic from the other VMs? I'm pretty much brand new to VirtualBox and I've never used Wireshark or an Ubuntu OS before. Does anyone have a suggestion or possibly an example of how to do this?</p></div><div id="comment-41838-info" class="comment-info"><span class="comment-age">(25 Apr '15, 12:03)</span> ab0mber89</div></div><span id="41839"></span><div id="comment-41839" class="comment"><div id="post-41839-score" class="comment-score"></div><div class="comment-text"><p>Would <a href="https://www.virtualbox.org/wiki/Network_tips">VirtualBox's NIC tracing</a> help here?</p></div><div id="comment-41839-info" class="comment-info"><span class="comment-age">(25 Apr '15, 12:13)</span> Guy Harris ♦♦</div></div><span id="41840"></span><div id="comment-41840" class="comment"><div id="post-41840-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I'm pretty much brand new to VirtualBox and I've never used Wireshark or an Ubuntu OS before.</p></blockquote><p>This probably has little, if anything, to do with Ubuntu and everything to do with VirtualBox.</p><p>VirtualBox might also provide interfaces on the <em>host</em> on which you can capture, showing traffic between the host and a particular guest.</p></div><div id="comment-41840-info" class="comment-info"><span class="comment-age">(25 Apr '15, 12:23)</span> Guy Harris ♦♦</div></div><span id="41841"></span><div id="comment-41841" class="comment"><div id="post-41841-score" class="comment-score"></div><div class="comment-text"><p>I'll try it out. I have very little time left before I have to leave for work, as it stands, but I will try to test it when I get home.</p><p>It mentions that I need to disable tracing once the test is over, but it doesn't show how.</p></div><div id="comment-41841-info" class="comment-info"><span class="comment-age">(25 Apr '15, 12:24)</span> ab0mber89</div></div><span id="41842"></span><div id="comment-41842" class="comment not_top_scorer"><div id="post-41842-score" class="comment-score"></div><div class="comment-text"><p>I'm afraid I have very little idea about how to configure the network in VirtualBox. I've tried using several different types of adapters (host only, internal, bridge) to connect these VMs so I can capture the packets, but nothing has worked so far.</p><p>I appreciate the help thus far. Hopefully the nictrace helps me uncover the issue.</p></div><div id="comment-41842-info" class="comment-info"><span class="comment-age">(25 Apr '15, 12:48)</span> ab0mber89</div></div></div><div id="comment-tools-41824" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-41824-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


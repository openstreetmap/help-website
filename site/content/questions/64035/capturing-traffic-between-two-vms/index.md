+++
type = "question"
title = "Capturing traffic between two VMs"
description = '''I have two virtual machines vm1 and vm2 running on my host with virtualbox, connected through a host-only adapter. I have Wireshark running on my host. VM(1|2): Ubuntu Host: Arch Linux I have turned promiscuous mode to &quot;allow-all&quot; and set ifconfig vboxnet0 promisc on the network interface that virtu...'''
date = "2017-10-19T11:58:00Z"
lastmod = "2017-10-20T01:37:00Z"
weight = 64035
keywords = [ "promiscuous", "virtualbox" ]
aliases = [ "/questions/64035" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Capturing traffic between two VMs](/questions/64035/capturing-traffic-between-two-vms)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-64035-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have two virtual machines vm1 and vm2 running on my host with virtualbox, connected through a host-only adapter. I have Wireshark running on my host.</p><p><strong>VM(1|2):</strong> Ubuntu<br />
<strong>Host:</strong> Arch Linux</p><p>I have turned promiscuous mode to "allow-all" and set <code>ifconfig vboxnet0 promisc</code> on the network interface that virtualbox is using and I am listening to:</p><p><code>[email protected] ifconfig vboxnet0: flags=4419&lt; UP,BROADCAST,RUNNING,PROMISC,MULTICAST &gt;  mtu 1500         inet 192.168.56.1  netmask 255.255.255.0  broadcast 192.168.56.255         inet6 fe80::800:27ff:fe00:0  prefixlen 64  scopeid 0x20&lt;link&gt;         ether 0a:00:27:00:00:00  txqueuelen 1000  (Ethernet)         RX packets 0  bytes 0 (0.0 B)         RX errors 0  dropped 0  overruns 0  frame 0         TX packets 692  bytes 61427 (59.9 KiB)         TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0</code></p><p>From my host system, I am able to capture traffic between <strong>vm* &lt;=&gt; host</strong>, but not <strong>vm1 &lt;=&gt; vm2</strong>. That is the goal I trie to achieve.</p><p>But from vm1 I am able to listen to traffic between vm2 &lt;=&gt; host.</p><p>My Settings for the network interface in wireshark are standard, so promiscuous mode is on. Is there any setting I have overseen?</p></div><div id="question-tags" class="tags-container tags">promiscuous virtualbox</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Oct '17, 11:58</strong></p><img src="https://secure.gravatar.com/avatar/6264ebe809328b34c7cd2f6adddcb43d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="eknoes&#39;s gravatar image" /><p>eknoes<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="eknoes has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-64035" class="comments-container"></div><div id="comment-tools-64035" class="comment-tools"></div><div class="clear"></div><div id="comment-64035-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="64043"></span>

<div id="answer-container-64043" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-64043-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>According to the answers in <a href="https://ask.wireshark.org/questions/41843/live-traffic-capture-of-two-vms-running-in-virtualbox">this question</a>, some folks can capture the VM-VM traffic from the host, some can't.</p><p>As noted on the question mentioned above, this would seem to be more a question for the VirtualBox support folks.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Oct '17, 01:37</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-64043" class="comments-container"></div><div id="comment-tools-64043" class="comment-tools"></div><div class="clear"></div><div id="comment-64043-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


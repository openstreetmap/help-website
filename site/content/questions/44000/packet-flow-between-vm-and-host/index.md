+++
type = "question"
title = "Packet Flow between vm and host"
description = '''Hi all, I am trying to understand packet flow between vm and host outside.Although this question is not directly related to Wireshark but i want to make use of general networking expertise in this forum.I am sorry for this lengthy question.  &amp;amp;&amp;amp;&amp;amp;&amp;amp;&amp;amp;&amp;amp;&amp;amp;&amp;amp;&amp;amp;&amp;amp;&amp;amp;&amp;am...'''
date = "2015-07-09T02:22:00Z"
lastmod = "2015-07-09T02:22:00Z"
weight = 44000
keywords = [ "bridging", "kvm" ]
aliases = [ "/questions/44000" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Packet Flow between vm and host](/questions/44000/packet-flow-between-vm-and-host)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44000-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44000-score" class="post-score" title="current number of votes">0</div><span id="post-44000-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>I am trying to understand packet flow between vm and host outside.Although this question is not directly related to Wireshark but i want to make use of general networking expertise in this forum.I am sorry for this lengthy question.</p><p>&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;</p><p>Setup:</p><p>Host1 running RHEL7 with KVM Virtualization.</p><p>Guest/VM running RHEL7 on Host1.</p><p>Host2 running Fedora.</p><p>&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;</p><p>Brief output on Host1</p><p>root#ip a s</p><p>1.lo 2.enp4s0f2 3.wlp3s0 4.virbr0 5.virbr0-nic 6.vnet0</p><p>root#brctl show</p><p>bridgename bridge id STP enabled interfaces</p><p>virbr0 xxxx.xxxxxxxxxxxx yes virbr0-nic,vnet0</p><p>I came to know that vnet0 is the interface connected to eth0 of virtual machine.virbr0 is the bridge and i am not sure about virbr0-nic. Like vnet0,the interface connected to eth0 of virtual machine,i assumed that virbr0-nic is the virtual interface connected to enp4s0f2 (which is the Physical interface of Host1).</p><p>&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;</p><p>Test case1:</p><p>Host1 is connected to Host2 on wired network(enp4s0f2)</p><p>I tried ssh from virtual machine on Host1 to Host2. Up on collecting Wireshark traces I assumed that packet was switched from vnet0 to virbr0-nic by bridge(virbr0).Virbr0-nic placed the packet on Ethernet interface(enp4s0f2) which did routing(ip.forward=1) and Natting to forward the packet to Host2.The flow was such that Host2 thinks that the ssh packet is originated from Host1 and in same way,for reply traffic (from Host2) ,Host1 did natting to replace dest ip to VM IP.This packet on virbr0-nic switched to vnet0 by virbr0 to finally place it on eth0 of virtual machine.</p><p>Test Case2:</p><p>Host1 is connected to Host2 on wireless network(wlp3s0)</p><p>I disabled wired interfaces on Host1 and Host2.</p><p>I expected that VM on Host1 can't ssh to Host2 because of lack of ethernet connectivity but to my surprise it worked like before(Test case1). Is it safe to assume now virbr0-nic is virtual interface of wlp3s0(wireless interface) on host1?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-bridging" rel="tag" title="see questions tagged &#39;bridging&#39;">bridging</span> <span class="post-tag tag-link-kvm" rel="tag" title="see questions tagged &#39;kvm&#39;">kvm</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Jul '15, 02:22</strong></p><img src="https://secure.gravatar.com/avatar/2b038237e64839261fcc88e9fdef2b68?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="krishnayeddula&#39;s gravatar image" /><p><span>krishnayeddula</span><br />
<span class="score" title="629 reputation points">629</span><span title="35 badges"><span class="badge1">●</span><span class="badgecount">35</span></span><span title="41 badges"><span class="silver">●</span><span class="badgecount">41</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="krishnayeddula has 3 accepted answers">6%</span></p></div></div><div id="comments-container-44000" class="comments-container"></div><div id="comment-tools-44000" class="comment-tools"></div><div class="clear"></div><div id="comment-44000-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>


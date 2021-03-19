+++
type = "question"
title = "[closed] Running wireshark from a VM, unit has a virtual port and physical port only seeing one port in wireshark"
description = '''We are running Wireshark on a VM and this virtual machine, ESX, has two ports. One physical port and one virtual port. The virtual port is setup to be the management port (with an ip) and the physical port is setup in promiscuous mode and attached to a span port on my core switch. The VM is running ...'''
date = "2016-02-24T16:21:00Z"
lastmod = "2016-02-24T16:21:00Z"
weight = 50493
keywords = [ "promiscuous", "span", "vmware", "esx" ]
aliases = [ "/questions/50493" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] Running wireshark from a VM, unit has a virtual port and physical port only seeing one port in wireshark](/questions/50493/running-wireshark-from-a-vm-unit-has-a-virtual-port-and-physical-port-only-seeing-one-port-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50493-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We are running Wireshark on a VM and this virtual machine, ESX, has two ports. One physical port and one virtual port. The virtual port is setup to be the management port (with an ip) and the physical port is setup in promiscuous mode and attached to a span port on my core switch. The VM is running Ubuntu 14.04 and the interfaces it sees are the management port (eth0) and Loopback. No reference of the promiscuous interface. When running wireshark, it only see traffic coming to the eth0 management interface, and it's not seeing the traffic that's coming across my SPAN port. Would this be an issue with my VM configuration? Or how wireshark is setup? The Ubuntu installation was pretty straight forward, would I have been able to add the promiscuous interface then? I just don't know why wireshark isn't able to pull traffic from my physical promiscuous interface on my span port?</p></div><div id="question-tags" class="tags-container tags">promiscuous span vmware esx</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Feb '16, 16:21</strong></p><img src="https://secure.gravatar.com/avatar/7dc1fee5b4e29c4e6cc3d5059312aac7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="msmorten&#39;s gravatar image" /><p>msmorten<br />
<span class="score" title="4 reputation points">4</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="msmorten has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>closed 25 Feb '16, 11:58</p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span></p></div></div><div id="comments-container-50493" class="comments-container"><span id="50511"></span><div id="comment-50511" class="comment"><div id="post-50511-score" class="comment-score"></div><div class="comment-text"><p>I'm confused about a VM having a virtual and a physical port (NIC). VMs usually have only virtual NICs which VMware's configuration allows you to connect to the server's physical NIC(s) (or not if you're using one or more VM-to-VM networks that don't need to exit the server).</p><p>Also, I didn't think VMware allowed you to enable promiscuous mode on a physical NIC. My understanding is that you enable promiscuous mode on a vSwitch (which probably also has some effect on the physical NIC?).</p><p>So: How many physical NICs do you have? How many virtual networks do you have? How many virtual NICs have you created on the VM? I'm guessing 1 since you said you only see 1 but some tools only show interfaces that are actually configured.</p></div><div id="comment-50511-info" class="comment-info"><span class="comment-age">(25 Feb '16, 11:14)</span> JeffMorriss ♦</div></div></div><div id="comment-tools-50493" class="comment-tools"></div><div class="clear"></div><div id="comment-50493-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Duplicate Question - https://ask.wireshark.org/questions/50349/running-wireshark-on-a-linux-vm-seeing-traffic-only-from-the-machine-wireshark-is-running-on" by JeffMorriss 25 Feb '16, 11:58

</div>

</div>

</div>


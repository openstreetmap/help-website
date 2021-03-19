+++
type = "question"
title = "virtual hosts and smb2 transfers"
description = '''I&#x27;m trying to understand the captures I&#x27;ve done. I&#x27;m getting an enormous number of &quot;previous packet&quot; and &quot;ack&#x27;d lost packet&quot;. I&#x27;ve done my captures on two windows 2012 virtual hosts simultaneously with Wireshark installed on the VMs and the expert infos results are radically different. These hosts h...'''
date = "2013-10-28T19:09:00Z"
lastmod = "2014-02-12T01:00:00Z"
weight = 26496
keywords = [ "10gbe", "windows", "pre_seq_lost", "ack_lost_seq", "vmware" ]
aliases = [ "/questions/26496" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [virtual hosts and smb2 transfers](/questions/26496/virtual-hosts-and-smb2-transfers)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26496-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to understand the captures I've done. I'm getting an enormous number of "previous packet" and "ack'd lost packet". I've done my captures on two windows 2012 virtual hosts simultaneously with Wireshark installed on the VMs and the expert infos results are radically different. These hosts have 10G interfaces. Wireshark doesn't show any dropped packets in the gui while capturing and the file comes over without a problem. There are some duplicate acks and some retransmissions. Where are my packets going? Is the Wireshark capture too slow to keep up? I don't have a virtual shark. I need to find out why I'm only getting 600Mbps average with iperf. The servers are on the same vlan.</p></div><div id="question-tags" class="tags-container tags">10gbe windows pre_seq_lost ack_lost_seq vmware</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Oct '13, 19:09</strong></p><img src="https://secure.gravatar.com/avatar/6de3659fc936859669fb3d6c499ed5ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="psdufour&#39;s gravatar image" /><p>psdufour<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="psdufour has no accepted answers">0%</span></p></div></div><div id="comments-container-26496" class="comments-container"></div><div id="comment-tools-26496" class="comment-tools"></div><div class="clear"></div><div id="comment-26496-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="26504"></span>

<div id="answer-container-26504" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26504-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I've done my captures on two windows 2012 <strong>virtual</strong> hosts<br />
These <strong>hosts have 10G interfaces.</strong></p></blockquote><p>Do the <strong>hosts</strong> or the <strong>virtual machines</strong> have 10G interfaces?</p><blockquote><p>I need to find out why I'm only getting 600Mbps average with iperf.</p></blockquote><p>sounds like the interfaces <strong>in the virtual machines</strong> are only (simulated) 1Gig interfaces (or the ports of the virtual switch are only 1G - if that is even configurable within your virtualization tool). Did you check that?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Oct '13, 04:08</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 29 Oct '13, 05:13</p></div></div><div id="comments-container-26504" class="comments-container"><span id="26511"></span><div id="comment-26511" class="comment"><div id="post-26511-score" class="comment-score"></div><div class="comment-text"><p>When I do the iperf test using Redhat linux VM's, I get better than 2 Gbps.</p></div><div id="comment-26511-info" class="comment-info"><span class="comment-age">(29 Oct '13, 07:23)</span> psdufour</div></div><span id="26514"></span><div id="comment-26514" class="comment"><div id="post-26514-score" class="comment-score"></div><div class="comment-text"><blockquote><p>When I do the iperf test using Redhat linux VM's, I get better than 2 Gbps.</p></blockquote><p>O.K. but what if the driver in Windows detects only 1G (virtual) interfaces? Please check that!</p><p>BTW: What is your Virtualization product (KVM, Xen, VMware)?</p></div><div id="comment-26514-info" class="comment-info"><span class="comment-age">(29 Oct '13, 08:08)</span> Kurt Knochner ♦</div></div><span id="26592"></span><div id="comment-26592" class="comment"><div id="post-26592-score" class="comment-score"></div><div class="comment-text"><p>I'm using VMware. The Windows guests are set at 10G. So that would be a shared 10G. They are using TCP offloading. I set up and did another test. I used a laptop with a 1G interface and used the default parameters for iperf and got 900+. When I went from VM server load to VM server load, I got 600+. When I tried to use Wireshark on one of the VM's at the same time I was doing the test between VM's, I got 400+ and the server end of iperf dropped packets in Wireshark. I see variations in TCP window sizes (I got the SYN packets), driving down to the 200's. I tried running Wireshark on the laptop while doing the test, but Wireshark dropped 30% of the packets according to the GUI bar.</p></div><div id="comment-26592-info" class="comment-info"><span class="comment-age">(31 Oct '13, 07:48)</span> psdufour</div></div><span id="26594"></span><div id="comment-26594" class="comment"><div id="post-26594-score" class="comment-score">1</div><div class="comment-text"><p>sounds like your VMware guests are fast enough to deliver more throughput.</p><p>As you said:</p><blockquote><p>using Redhat linux VM's, I get better than 2 Gbps.</p></blockquote><p>if we can assume, that you used the same hardware specs for the Linux and Windows VM guests, there might be an issue with the 'network driver' in the Windwos guests (which virtual network hardware did you assign to them?). Did you enable Jumbo Frames in Linux? Did you enable them in Windows?</p><p>BTW: Running Wireshark in parallel to iperf on a possibly overloaded system, will kill your performance, especially as you'll have a huge disk IO load if you try to capture that amount of network traffic.</p><p>I think it's a good idea to ask your local VMware guru how to get the best networking performance for Windows guests, as other people describe that they can easily saturate a 10G link with two virtual guests.</p><blockquote><p><a href="http://virtualtricks.blogspot.de/2009/04/10-gbps-networking-performance-on.html">http://virtualtricks.blogspot.de/2009/04/10-gbps-networking-performance-on.html</a></p></blockquote><p>Maybe it's also a good idea to read some of the following papers (vSphere might be older than your environment).</p><blockquote><p><a href="http://www.cisco.com/en/US/prod/collateral/switches/ps9441/ps9670/c07-601040-00_vm_10gbn_dn_v2a.pdf">http://www.cisco.com/en/US/prod/collateral/switches/ps9441/ps9670/c07-601040-00_vm_10gbn_dn_v2a.pdf</a><br />
<a href="http://www.vmware.com/pdf/Perf_Best_Practices_vSphere4.1.pdf">http://www.vmware.com/pdf/Perf_Best_Practices_vSphere4.1.pdf</a><br />
<a href="http://www.vmware.com/files/pdf/techpaper/network-io-latency-perf-vsphere5.pdf">http://www.vmware.com/files/pdf/techpaper/network-io-latency-perf-vsphere5.pdf</a><br />
<a href="http://www.vmware.com/files/pdf/techpaper/Performance-Networking-vSphere4-1-WP.pdf">http://www.vmware.com/files/pdf/techpaper/Performance-Networking-vSphere4-1-WP.pdf</a><br />
</p></blockquote></div><div id="comment-26594-info" class="comment-info"><span class="comment-age">(31 Oct '13, 08:22)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-26504" class="comment-tools"></div><div class="clear"></div><div id="comment-26504-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="26502"></span>

<div id="answer-container-26502" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26502-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Looks like tons of dropped frames to me. You should keep in mind that drops may happen way before Dumpcap/Wireshark even sees the frame, so if you're slamming your NICs with frames it is very likely that a lot of them are already dropped on driver or OS level, and Wireshark will never even know (and thus not show them as dropped).</p><p>Also, I'm pretty sure that a standard PC cannot hope to record 10GB/s speeds, let alone write them to disk. You would have to be able to write more than 1GByte/s to disk at that speed, and I doubt you have a disk array that can do that.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Oct '13, 03:43</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span> </br></br></p></div></div><div id="comments-container-26502" class="comments-container"><span id="26505"></span><div id="comment-26505" class="comment"><div id="post-26505-score" class="comment-score"></div><div class="comment-text"><p>@Jasper: I wonder if two virtual machines, given they really use the 10G interfaces of the host, are able to saturate the 10G link (with iperf or other tests)? Do you have any experience with such a setup, let's say in VMware?</p></div><div id="comment-26505-info" class="comment-info"><span class="comment-age">(29 Oct '13, 04:10)</span> Kurt Knochner ♦</div></div><span id="26510"></span><div id="comment-26510" class="comment"><div id="post-26510-score" class="comment-score"></div><div class="comment-text"><p>Unfortunately I do not have access to virtualization hosts with that kind of hardware (10G NICs plus 10G switches), sorry :-)</p></div><div id="comment-26510-info" class="comment-info"><span class="comment-age">(29 Oct '13, 07:07)</span> Jasper ♦♦</div></div><span id="26513"></span><div id="comment-26513" class="comment"><div id="post-26513-score" class="comment-score"></div><div class="comment-text"><p>No problem. I thought you might have had a chance in the last couple of years, during vmware trainings or so... ;-)</p></div><div id="comment-26513-info" class="comment-info"><span class="comment-age">(29 Oct '13, 08:08)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-26502" class="comment-tools"></div><div class="clear"></div><div id="comment-26502-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="29737"></span>

<div id="answer-container-29737" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29737-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, you'll have a huge disk IO load if you try to capture that amount of network traffic. Thanks for sharing nice or informative post.. Our comment source:</p><p><strong><a href="http://intilop.com">10G bit tcp offload</a></strong></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Feb '14, 01:00</strong></p><img src="https://secure.gravatar.com/avatar/0241b0a411cbaadc998770fb27051d41?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="intilop&#39;s gravatar image" /><p>intilop<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="intilop has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-29737" class="comments-container"><span id="29740"></span><div id="comment-29740" class="comment"><div id="post-29740-score" class="comment-score"></div><div class="comment-text"><p>Is this <strong>advertisement spam</strong>, promoting the products of your company? If it's not spam, can you please add some information how <strong>your products</strong> help to <strong>reduce the IO load</strong> while capturing at 10G ?</p></div><div id="comment-29740-info" class="comment-info"><span class="comment-age">(12 Feb '14, 01:18)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-29737" class="comment-tools"></div><div class="clear"></div><div id="comment-29737-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


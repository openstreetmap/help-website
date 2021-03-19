+++
type = "question"
title = "Does e1000e driver support libpcap and thus tshark to view Ethernet FCS?"
description = '''I have a PC with Intel Corporation 82573L GigE NIC. It uses e1000e(version 1.5.1-k) driver. Driver is loaded with CRC stripping disabled: root@localhost:~# modprobe -v e1000e CrcStripping=0 insmod /lib/modules/3.2.0-4-686-pae/kernel/drivers/net/ethernet/intel/e1000e/e1000e.ko CrcStripping=0 root@loc...'''
date = "2015-01-15T03:56:00Z"
lastmod = "2015-01-15T06:15:00Z"
weight = 39153
keywords = [ "fcs" ]
aliases = [ "/questions/39153" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Does e1000e driver support libpcap and thus tshark to view Ethernet FCS?](/questions/39153/does-e1000e-driver-support-libpcap-and-thus-tshark-to-view-ethernet-fcs)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39153-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a PC with <em>Intel Corporation 82573L</em> GigE NIC. It uses <em>e1000e</em>(version 1.5.1-k) driver. Driver is loaded with CRC stripping disabled:</p><pre><code>[email protected]:~# modprobe -v e1000e CrcStripping=0
insmod /lib/modules/3.2.0-4-686-pae/kernel/drivers/net/ethernet/intel/e1000e/e1000e.ko CrcStripping=0
[email protected]:~#</code></pre><p>In addition, all the Ethernet related Rx checksum offloading should be disabled:</p><pre><code>[email protected]:~# ethtool -k eth2
Features for eth2:
rx-checksumming: off
tx-checksumming: off
    tx-checksum-ipv4: off [fixed]
    tx-checksum-unneeded: off [fixed]
    tx-checksum-ip-generic: off
    tx-checksum-ipv6: off [fixed]
    tx-checksum-fcoe-crc: off [fixed]
    tx-checksum-sctp: off [fixed]
scatter-gather: off
    tx-scatter-gather: off [requested on]
    tx-scatter-gather-fraglist: off [fixed]
tcp-segmentation-offload: off
    tx-tcp-segmentation: off [requested on]
    tx-tcp-ecn-segmentation: off [fixed]
    tx-tcp6-segmentation: off [requested on]
udp-fragmentation-offload: off [fixed]
generic-segmentation-offload: off [requested on]
generic-receive-offload: on
large-receive-offload: off [fixed]
rx-vlan-offload: on
tx-vlan-offload: on
ntuple-filters: off [fixed]
receive-hashing: off [fixed]
highdma: on [fixed]
rx-vlan-filter: on [fixed]
vlan-challenged: off [fixed]
tx-lockless: off [fixed]
netns-local: off [fixed]
tx-gso-robust: off [fixed]
tx-fcoe-segmentation: off [fixed]
fcoe-mtu: off [fixed]
tx-nocache-copy: on
loopback: off [fixed]
[email protected]:~#</code></pre><p>Still, if I capture packets with <code>tshark -i eth2 -V</code> I do not see any FCS of CRC fields. Am I doing something wrong or does this NIC or driver not support Ethernet FCS passing?</p></div><div id="question-tags" class="tags-container tags">fcs</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jan '15, 03:56</strong></p><img src="https://secure.gravatar.com/avatar/c153148e19e1e7c04c48a2a5c4f68b54?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrtn&#39;s gravatar image" /><p>mrtn<br />
<span class="score" title="11 reputation points">11</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrtn has no accepted answers">0%</span></p></div></div><div id="comments-container-39153" class="comments-container"></div><div id="comment-tools-39153" class="comment-tools"></div><div class="clear"></div><div id="comment-39153-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39159"></span>

<div id="answer-container-39159" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39159-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>I don't see the FCS related options in the output. Please run the following commands:</p><blockquote><p>ethtool -K eth2 rx-fcs on<br />
ethtool -K eth2 rx-all on<br />
</p></blockquote><p>Then run ethtool -k eth2 again and check if those options are set.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jan '15, 06:15</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-39159" class="comments-container"><span id="39161"></span><div id="comment-39161" class="comment"><div id="post-39161-score" class="comment-score"></div><div class="comment-text"><p>Thanks! Both for <code>ethtool -K eth2 rx-fcs on</code> and <code>ethtool -K eth2 rx-all on</code> I receive the <code>ethtool: bad command line argument(s)</code> error. However, on another machine with e1000e version 2.1.4-k I am able to pass FCS up to network stack. So I guess both <code>rx-fcs</code> and <code>rx-all</code> features are heavily driver and NIC hardware dependent? In addition, I have to say that at least <code>tshark</code> version 1.8.5 is often confused about FCS field and sometimes interprets it as part of some other protocol(for example <em>VSS-Monitoring ethernet trailer</em> if ICMP "echo request" is padded with zeros) and sometimes counts it in as a part of <em>Data</em> field(for example in case of Cisco IOS keepalive packages). Has anyone else observed this behavior?</p></div><div id="comment-39161-info" class="comment-info"><span class="comment-age">(15 Jan '15, 08:11)</span> mrtn</div></div></div><div id="comment-tools-39159" class="comment-tools"></div><div class="clear"></div><div id="comment-39159-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


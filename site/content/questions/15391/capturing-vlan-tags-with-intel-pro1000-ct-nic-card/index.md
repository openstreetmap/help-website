+++
type = "question"
title = "Capturing VLAN Tags with Intel Pro/1000 CT NIC Card"
description = '''Hi, I am running CentOS 6.2 using the default e1000 driver for my Intel Pro/1000 CT Gb NIC card. I am running Dumpcap to capture packets from this interface. I am seeing NO packets being captured. I looked at this site: http://wiki.wireshark.org/CaptureSetup/VLAN I was unable to determine a resoluti...'''
date = "2012-10-30T12:06:00Z"
lastmod = "2012-10-31T11:55:00Z"
weight = 15391
keywords = [ "vlan", "centos", "tags" ]
aliases = [ "/questions/15391" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Capturing VLAN Tags with Intel Pro/1000 CT NIC Card](/questions/15391/capturing-vlan-tags-with-intel-pro1000-ct-nic-card)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15391-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am running CentOS 6.2 using the default e1000 driver for my Intel Pro/1000 CT Gb NIC card.</p><p>I am running Dumpcap to capture packets from this interface.</p><p>I am seeing NO packets being captured.</p><p>I looked at this site: <a href="http://wiki.wireshark.org/CaptureSetup/VLAN">http://wiki.wireshark.org/CaptureSetup/VLAN</a></p><p>I was unable to determine a resolution for issue.</p><p>Any guidance or assistance will be greatly appreciated.</p><p>Thanks,</p><p>John</p></div><div id="question-tags" class="tags-container tags">vlan centos tags</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Oct '12, 12:06</strong></p><img src="https://secure.gravatar.com/avatar/cccf8e497e5c13ae9a4dac3641c2521c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="xq1&#39;s gravatar image" /><p>xq1<br />
<span class="score" title="0 reputation points">0</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="xq1 has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 30 Oct '12, 12:44</p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-15391" class="comments-container"></div><div id="comment-tools-15391" class="comment-tools"></div><div class="clear"></div><div id="comment-15391-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="15428"></span>

<div id="answer-container-15428" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15428-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Problem Solved - added MTU="9000" to /etc/sysconfig/network-scripts/ifcfg-ethx</p><p>Thanks Kurt for your time!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Oct '12, 11:55</strong></p><img src="https://secure.gravatar.com/avatar/cccf8e497e5c13ae9a4dac3641c2521c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="xq1&#39;s gravatar image" /><p>xq1<br />
<span class="score" title="0 reputation points">0</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="xq1 has one accepted answer">100%</span></p></div></div><div id="comments-container-15428" class="comments-container"><span id="15474"></span><div id="comment-15474" class="comment"><div id="post-15474-score" class="comment-score"></div><div class="comment-text"><p>As it turns out this solution does NOT make the change permanent.</p></div><div id="comment-15474-info" class="comment-info"><span class="comment-age">(01 Nov '12, 11:12)</span> xq1</div></div></div><div id="comment-tools-15428" class="comment-tools"></div><div class="clear"></div><div id="comment-15428-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="15394"></span>

<div id="answer-container-15394" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15394-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>There are discussions on the internet about the e1000 driver and VLAN handling. Taking these into account, I have some questions and some suggestions:</p><p>Questions:<br />
</p><ul><li>do you capture on ethx or on ethx.100 (VLAN tag 100)?</li><li>if you capture on ethx (eth0,eth1,etc.) is there any VLAN interface configured?</li><li>what do you see if you run this command: <strong>tcpdump -ni eth0 vlan</strong>?</li></ul><p>Suggestions:</p><ul><li>If there is a VLAN interface configured (e.g. ethx.100) the e1000 driver seems to handle VLAN tags in a different way, than if there is no VLAN interface. I <strong>suggest</strong> to remove the VLAN interface and then capture on the interface ethx, if that is possible in your environment.</li><li>Can you please post the output of the command: <strong>modinfo -d -p e1000</strong>?<br />
</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Oct '12, 12:38</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-15394" class="comments-container"><span id="15401"></span><div id="comment-15401" class="comment"><div id="post-15401-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt,</p><p>Below are the answers to your questions.</p><p>Any guidance to troubleshooting and resolving is greatly appreciated.</p><p>-John</p><p>=======================</p><p>None of my interfaces are set up with VLAN subinterfaces (ie eth1.100)</p><p>=======================</p><p>tcpdump -ni eth1 vlan - produces no output</p><p>=======================</p><h1 id="tcpdump--ni-eth1-vlan">tcpdump -ni eth1 vlan</h1><p>tcpdump: verbose output suppressed, use -v or -vv for full protocol decode</p><p>listening on eth1, link-type EN10MB (Ethernet), capture size 65535 bytes</p><p>=======================</p><p>modinfo -d -p e1000 output</p><p>=======================</p><h1 id="modinfo--d--p-e1000">modinfo -d -p e1000</h1><p>debug:Debug level (0=none,...,16=all)</p><p>copybreak:Maximum size of packet that is copied to a new buffer on receive</p><p>KumeranLockLoss:Enable Kumeran lock loss workaround</p><p>SmartPowerDownEnable:Enable PHY smart power down</p><p>InterruptThrottleRate:Interrupt Throttling Rate</p><p>RxAbsIntDelay:Receive Absolute Interrupt Delay</p><p>RxIntDelay:Receive Interrupt Delay</p><p>TxAbsIntDelay:Transmit Absolute Interrupt Delay</p><p>TxIntDelay:Transmit Interrupt Delay</p><p>XsumRX:Disable or enable Receive Checksum offload</p><p>FlowControl:Flow Control setting</p><p>AutoNeg:Advertised auto-negotiation setting</p><p>Duplex:Duplex setting</p><p>Speed:Speed setting</p><p>RxDescriptors:Number of receive descriptors</p><p>TxDescriptors:Number of transmit descriptors</p></div><div id="comment-15401-info" class="comment-info"><span class="comment-age">(30 Oct '12, 16:03)</span> xq1</div></div><span id="15402"></span><div id="comment-15402" class="comment"><div id="post-15402-score" class="comment-score"></div><div class="comment-text"><h1 id="ethtool--i-eth1">ethtool -i eth1</h1><p>driver: e1000e</p><p>version: 1.9.5-k</p><p>firmware-version: 1.8-0</p><p>bus-info: 0000:20:00.0</p></div><div id="comment-15402-info" class="comment-info"><span class="comment-age">(30 Oct '12, 16:05)</span> xq1</div></div><span id="15403"></span><div id="comment-15403" class="comment"><div id="post-15403-score" class="comment-score"></div><div class="comment-text"><p>I noticed the driver loaded for this NIC is actually e1000e so here is the output for e1000e:</p><h1 id="modinfo--d--p-e1000e">modinfo -d -p e1000e</h1><p>EEE:Enable/disable on parts that support the feature</p><p>CrcStripping:Enable CRC Stripping, disable if your BMC needs the CRC</p><p>WriteProtectNVM:Write-protect NVM [WARNING: disabling this can lead to corrupted NVM]</p><p>KumeranLockLoss:Enable Kumeran lock loss workaround</p><p>SmartPowerDownEnable:Enable PHY smart power down</p><p>IntMode:Interrupt Mode</p><p>InterruptThrottleRate:Interrupt Throttling Rate</p><p>RxAbsIntDelay:Receive Absolute Interrupt Delay</p><p>RxIntDelay:Receive Interrupt Delay</p><p>TxAbsIntDelay:Transmit Absolute Interrupt Delay</p><p>TxIntDelay:Transmit Interrupt Delay</p><p>copybreak:Maximum size of packet that is copied to a new buffer on receive</p></div><div id="comment-15403-info" class="comment-info"><span class="comment-age">(30 Oct '12, 16:07)</span> xq1</div></div><span id="15404"></span><div id="comment-15404" class="comment"><div id="post-15404-score" class="comment-score"></div><div class="comment-text"><p>lspci output:</p><p>20:00.0 Ethernet controller: Intel Corporation 82574L Gigabit Network Connection</p><p>30:00.0 Ethernet controller: Intel Corporation 82574L Gigabit Network Connection</p></div><div id="comment-15404-info" class="comment-info"><span class="comment-age">(30 Oct '12, 16:10)</span> xq1</div></div></div><div id="comment-tools-15394" class="comment-tools"></div><div class="clear"></div><div id="comment-15394-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


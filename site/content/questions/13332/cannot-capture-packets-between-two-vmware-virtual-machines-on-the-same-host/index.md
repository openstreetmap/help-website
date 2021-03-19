+++
type = "question"
title = "Cannot capture packets between two vmware virtual machines on the same host"
description = '''I set them both at bridged model. I tried NAT as well, still cannot get the packets between them. The capture interface I chose was the physical interface of the host. Any ideas, thank u!'''
date = "2012-08-02T19:45:00Z"
lastmod = "2012-08-03T14:05:00Z"
weight = 13332
keywords = [ "vmware" ]
aliases = [ "/questions/13332" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Cannot capture packets between two vmware virtual machines on the same host](/questions/13332/cannot-capture-packets-between-two-vmware-virtual-machines-on-the-same-host)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13332-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I set them both at bridged model. I tried NAT as well, still cannot get the packets between them. The capture interface I chose was the physical interface of the host.</p><p>Any ideas, thank u!</p></div><div id="question-tags" class="tags-container tags">vmware</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Aug '12, 19:45</strong></p><img src="https://secure.gravatar.com/avatar/f06d618450f64d3f8657e3a995b78b7d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Siyang&#39;s gravatar image" /><p>Siyang<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Siyang has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 Aug '12, 04:27</p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-13332" class="comments-container"></div><div id="comment-tools-13332" class="comment-tools"></div><div class="clear"></div><div id="comment-13332-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="13345"></span>

<div id="answer-container-13345" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13345-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi,</p><p>This works on my system:</p><p>System:<br />
</p><blockquote><p>Host: Win 7 64 Bit<br />
Vmware: Workstation 7.1.5<br />
VM 1+2: Win XP SP3<br />
</p></blockquote><p>Test case #1</p><blockquote><p>Setup: Both VMs mapped their interface to "bridged"<br />
<strong>Result:</strong> I can see traffic of/between those machines on my Host LAN interface</p></blockquote><p>Test case #2</p><blockquote><p>Setup: Both VMs mapped their interface to "host-only"<br />
<strong>Result:</strong> I can see traffic of/between those machines on my Host "vmnet1" interface</p></blockquote><p>So, what is your</p><ul><li>OS / OS version of the vmware host</li><li>Vmware version</li><li>Wireshark capture setup</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Aug '12, 03:35</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-13345" class="comments-container"><span id="13377"></span><div id="comment-13377" class="comment"><div id="post-13377-score" class="comment-score"></div><div class="comment-text"><p>Thank you Kurt, your case #2 works on my system.</p><p>Mine system is the same with u, except my Vmware is workstation 8.0.0.</p><p>However, I understand the differences of the models, I'm still not clear that why the case #1 cannot work on my system.</p><p>Could you explain the reason in detail? That would help a lot!</p><p>Thank you! Siyang</p></div><div id="comment-13377-info" class="comment-info"><span class="comment-age">(05 Aug '12, 23:45)</span> Siyang</div></div><span id="13388"></span><div id="comment-13388" class="comment"><div id="post-13388-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I'm still not clear that why the case #1 cannot work on my system.</p></blockquote><p>VMware Workstation uses 'auto-bridging' per default. If you have multiple interfaces on your host (including WLAN interfaces), VMware might have mapped the VM interfaces to a host interface you do not expect. Please configure manual mapping of the bridged interfaces and then try again.</p><blockquote><p><code>Edit -&gt; Virtual Network Editor -&gt; VMnet0 (bridged) -&gt; Bridged to: (Automatic)</code><br />
</p></blockquote><p>Change 'Automatic' the your LAN interface. You should be able to capture on the host now. If that does not work, they have changed something in VMware 8.0.</p></div><div id="comment-13388-info" class="comment-info"><span class="comment-age">(06 Aug '12, 05:39)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-13345" class="comment-tools"></div><div class="clear"></div><div id="comment-13345-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="13360"></span>

<div id="answer-container-13360" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13360-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>With Wireshark installed on the VM, all you will see is traffic to &amp; from the VM plus broadcasts &amp; multicasts. This is because when in bridged mode the physical Win 7 OS is acting as a switch, only passing up the traffic to &amp; from the VM plus broadcasts &amp; multicasts.</p><p>If you install Wireshark on the Win 7 host, then you will be able to put the NIC in promiscuous mode and capture whatever passes your NIC (obviously dependant then on you SPAN session etc).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Aug '12, 14:05</strong></p><img src="https://secure.gravatar.com/avatar/030196d67dc4e2b8f4ecff65eefdb63e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KeithFrench&#39;s gravatar image" /><p>KeithFrench<br />
<span class="score" title="121 reputation points">121</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KeithFrench has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-13360" class="comments-container"><span id="13378"></span><div id="comment-13378" class="comment"><div id="post-13378-score" class="comment-score"></div><div class="comment-text"><p>Thank you!</p><p>In theoretically, Wireshark should capture all the packages passed through it.</p><p>Just in my case, when the 2 VMs are set in 'bridged' model, wireshark cannot capture the communication between them.</p></div><div id="comment-13378-info" class="comment-info"><span class="comment-age">(05 Aug '12, 23:52)</span> Siyang</div></div></div><div id="comment-tools-13360" class="comment-tools"></div><div class="clear"></div><div id="comment-13360-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


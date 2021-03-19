+++
type = "question"
title = "Wireshark (WinPCap) does not see Intel X520-DA2 10 GbE NIC teaming intermittently"
description = '''I am running a team of two 10 GigE ports on Intel X520-DA2 network card. They work well in tandem and achieve the desired throughput. However, I see an intermittent issue whereby WireShark and my own application (using WinPCap) only show the underlying ports, failing to recognize the team adapter. D...'''
date = "2012-12-10T10:29:00Z"
lastmod = "2012-12-10T10:29:00Z"
weight = 16751
keywords = [ "nic-team" ]
aliases = [ "/questions/16751" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark (WinPCap) does not see Intel X520-DA2 10 GbE NIC teaming intermittently](/questions/16751/wireshark-winpcap-does-not-see-intel-x520-da2-10-gbe-nic-teaming-intermittently)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16751-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am running a team of two 10 GigE ports on Intel X520-DA2 network card. They work well in tandem and achieve the desired throughput. However, I see an intermittent issue whereby WireShark and my own application (using WinPCap) only show the underlying ports, failing to recognize the team adapter.</p><p>Details: Intel 17.4 NIC drivers on Windows Server 2008 R2 with all patches. HP DL370 G6 server. RSS enabled on Intel both underlying Intel NICs.</p><p>The exact error: Unable to open the adapter (rpcap://\Device\NPF_{401D5903-16E7-41DC-8484-5D96765B9692}). failed to set hardware filter to promiscuous mode</p><p>Cross-posted from <a href="http://serverfault.com/q/456264/10618">ServerFault</a>.</p></div><div id="question-tags" class="tags-container tags">nic-team</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Dec '12, 10:29</strong></p><img src="https://secure.gravatar.com/avatar/9784e8dd1a8be188a42896c33ac9d392?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gregory%20Chernis&#39;s gravatar image" /><p>Gregory Chernis<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gregory Chernis has no accepted answers">0%</span></p></div></div><div id="comments-container-16751" class="comments-container"><span id="16802"></span><div id="comment-16802" class="comment"><div id="post-16802-score" class="comment-score"></div><div class="comment-text"><p>can you post the output of the following commands (run it on the server with the teaming NICs).</p><blockquote><p><code>dumpcap -D -M</code><br />
<code>ipconfig /all</code></p></blockquote></div><div id="comment-16802-info" class="comment-info"><span class="comment-age">(12 Dec '12, 07:21)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-16751" class="comment-tools"></div><div class="clear"></div><div id="comment-16751-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>


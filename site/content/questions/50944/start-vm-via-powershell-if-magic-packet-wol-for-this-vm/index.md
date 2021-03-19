+++
type = "question"
title = "Start Vm via Powershell if Magic Packet (WOL) for this VM"
description = '''Hi, I try to find a option to start a VM via WOL. MY Problem: I use hyper-v on a Windows Server 2012R2. Hyper-v dose not support WOL for VM&#x27;s. What I want to do: I want to send a magic package to wakeup one of the VM&#x27;s. (If wol for Vm1 stat VM1; if Wil fir VM2 start VM2) I would need also something ...'''
date = "2016-03-15T11:46:00Z"
lastmod = "2016-03-15T11:57:00Z"
weight = 50944
keywords = [ "wol", "vm" ]
aliases = [ "/questions/50944" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Start Vm via Powershell if Magic Packet (WOL) for this VM](/questions/50944/start-vm-via-powershell-if-magic-packet-wol-for-this-vm)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50944-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I try to find a option to start a VM via WOL.</p><p>MY Problem: I use hyper-v on a Windows Server 2012R2. Hyper-v dose not support WOL for VM's.</p><p>What I want to do: I want to send a magic package to wakeup one of the VM's. (If wol for Vm1 stat VM1; if Wil fir VM2 start VM2) I would need also something like a transfer table to translate the Mac address to the VM's name, so that I can use the Name of the VM in a Powershel script for the start. It have to work as a service because there will be no user.</p><p>I have read completely different things (t-shark;dumpcap;....)</p><p>Howe to implement something like this.</p><p>Got anybodya idea what's the " easiest" way to do this ?</p><p>Regards Michael</p></div><div id="question-tags" class="tags-container tags">wol vm</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Mar '16, 11:46</strong></p><img src="https://secure.gravatar.com/avatar/011002fdb4e024a3b27a04174c164efa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Micha82&#39;s gravatar image" /><p>Micha82<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Micha82 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Mar '16, 02:39</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-50944" class="comments-container"></div><div id="comment-tools-50944" class="comment-tools"></div><div class="clear"></div><div id="comment-50944-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50945"></span>

<div id="answer-container-50945" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50945-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I'd go to a site like Stackoverflow with such question, Wireshark is all about packet <em>analysis</em>, not generation. I.e. Wireshark would show you how the magic packet should look like if you wouldn't know it, but cannot help you to send it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Mar '16, 11:57</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-50945" class="comments-container"><span id="50946"></span><div id="comment-50946" class="comment"><div id="post-50946-score" class="comment-score"></div><div class="comment-text"><p>Hi sindy,</p><p>Howe to send the magic package is not the problem.</p><p>My Problem is that I have to analyze all magic packages in the network and if one of the "right " packages comes by I want to start a specific script</p><p>(for each specified magic package a other script or maby the same but then I have to transfer the corosponding VM name as a variable to it )</p></div><div id="comment-50946-info" class="comment-info"><span class="comment-age">(15 Mar '16, 12:24)</span> Micha82</div></div><span id="50959"></span><div id="comment-50959" class="comment"><div id="post-50959-score" class="comment-score"></div><div class="comment-text"><p>OK, so I've completely misunderstood your issue.</p><p>The problem with tshark is that it will get out of memory sooner or later (it would probably take years in your case, but it would happen), and the problem with dumpcap is that it can only save the captured packets to file or send them via pipe but not to analyse them (which prevents it from eating memory).</p><p>So your script would have to run two instances of tshark with a narrow capture filter like <code>udp and (dst port 7 or dst port 9)</code> in parallel, restarting them at different times so that at least one of them would always be running while the other one would be restarted. The output of the tshark instances piped to an executive script would either be the MAC (using <code>-T fields -o wol.mac</code>), or, if you feel dizzy, you could create a Lua post-dissector creating a new field <code>vm_name</code> and let Lua do the MAC -&gt; VM name translation (so you would use <code>-T fields -o wol.vm_name</code>). You cannot ask Lua to spawn an external command.</p></div><div id="comment-50959-info" class="comment-info"><span class="comment-age">(15 Mar '16, 13:49)</span> sindy</div></div></div><div id="comment-tools-50945" class="comment-tools"></div><div class="clear"></div><div id="comment-50945-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


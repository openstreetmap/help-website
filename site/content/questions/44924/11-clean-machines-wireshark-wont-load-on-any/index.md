+++
type = "question"
title = "11 Clean Machines, Wireshark won&#x27;t load on any"
description = '''Hello, we have a classroom with 11 Windows 8.1 Machines. These are various machines (HP Proliant, Supermico, Dell, Tyan, etc.) All of which are fresh installations with full upgrades. We installed Wireshark-win64-1.12.6.exe The software installed successfully along with WinPcap On no machine would W...'''
date = "2015-08-07T09:31:00Z"
lastmod = "2015-08-10T03:20:00Z"
weight = 44924
keywords = [ "windows8.1" ]
aliases = [ "/questions/44924" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [11 Clean Machines, Wireshark won't load on any](/questions/44924/11-clean-machines-wireshark-wont-load-on-any)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44924-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, we have a classroom with 11 Windows 8.1 Machines. These are various machines (HP Proliant, Supermico, Dell, Tyan, etc.) All of which are fresh installations with full upgrades.</p><p>We installed Wireshark-win64-1.12.6.exe The software installed successfully along with WinPcap</p><p>On no machine would Wireshark load. On each machine Wireshark Splashscreen is stuck at 100%. A few of the have been stuck at 100% since yesterday, the other we had to reboot.</p><p>These machines do not have anti-virus softwares on anything of the like. Nearly all are fresh, clean installations with hardly anything installed except alternative web browsers and text editors.</p><p>Any help will be greatly appreciated.</p><p>Some students have said that they have never been able to get Wireshark to properly load on Windows 8.1</p></div><div id="question-tags" class="tags-container tags">windows8.1</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Aug '15, 09:31</strong></p><img src="https://secure.gravatar.com/avatar/20af3e7b1944ab5efe3780be6d34aae3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="charlesrenaullt&#39;s gravatar image" /><p>charlesrenaullt<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="charlesrenaullt has no accepted answers">0%</span></p></div></div><div id="comments-container-44924" class="comments-container"></div><div id="comment-tools-44924" class="comment-tools"></div><div class="clear"></div><div id="comment-44924-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44941"></span>

<div id="answer-container-44941" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44941-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Almost certainly this is something particular to your environment, as it isn't generally an issue elsewhere.</p><p>There have been reports of a lock-up caused by WinPCap, as when Wireshark starts it makes a call into WinPCap to get the list of network adaptors and for reasons currently unknown this call hangs.</p><p>Can you use a tool such as <a href="https://technet.microsoft.com/en-gb/sysinternals/bb896653.aspx?f=255&amp;MSPPError=-2147217396">Process Explorer</a> and check for instances of dumpcap running, and if there are, the command line parameters to the instance(s).</p><p>Do you have any "odd" adaptors in the machines, e.g. other than a standard on-board Ethernet NIC?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Aug '15, 03:20</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-44941" class="comments-container"><span id="44945"></span><div id="comment-44945" class="comment"><div id="post-44945-score" class="comment-score"></div><div class="comment-text"><p>Hi grahamb,</p><p>Thank you very much for your reply. [As far as the network cards ... all on-board.] These are all standard, affordable machines. All of various brands. We have two (2) laptops: Toshiba Satellite, Lenovo ThinkPad. We have servers converted to desktops (Intel motherboard, SuperMicro, Tyan, Dell, HP Proliant).</p><p>I do recall that dumpcap was running in the background (as installed by Wireshark package installer. I'll reply with further details - "command line parameters to the instance(s)".</p><p>In any case, thanks again.</p></div><div id="comment-44945-info" class="comment-info"><span class="comment-age">(10 Aug '15, 09:04)</span> charlesrenaullt</div></div><span id="44948"></span><div id="comment-44948" class="comment"><div id="post-44948-score" class="comment-score"></div><div class="comment-text"><blockquote>I do recall that dumpcap was running in the background (as installed by Wireshark package installer.</blockquote><p>I vaguely remember seeing discussions about that as well. When you stop Wireshark there should be no instances of dumpcap.exe running. If you can achieve that, then you can also try <code>dumpcap -D</code> from the command line to list the interfaces found by WinPCap.</p></div><div id="comment-44948-info" class="comment-info"><span class="comment-age">(10 Aug '15, 09:56)</span> grahamb ♦</div></div></div><div id="comment-tools-44941" class="comment-tools"></div><div class="clear"></div><div id="comment-44941-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


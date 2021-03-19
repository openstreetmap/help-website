+++
type = "question"
title = "Can not see packets from local machine"
description = '''Hello  Can&#x27;t see the packets from my local Win7 machine in wireshark trace. I&#x27;m using wireshark 1.8.1 (x86) with winpcap (x86) 4.1.2 (4.1.0.2001) but my win7 x64. The machine itself is a DELL laptop with Intel(R) 82579LM Gigabit Network adapter (driver e1c62x64.sys (11.13.51.0) and DW1530 Wireless-N...'''
date = "2012-09-05T22:15:00Z"
lastmod = "2012-09-07T02:36:00Z"
weight = 14075
keywords = [ "missing", "local", "packet", "wireshark" ]
aliases = [ "/questions/14075" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Can not see packets from local machine](/questions/14075/can-not-see-packets-from-local-machine)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14075-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello</p><p>Can't see the packets from my local Win7 machine in wireshark trace. I'm using wireshark 1.8.1 (x86) with winpcap (x86) 4.1.2 (4.1.0.2001) but my win7 x64. The machine itself is a DELL laptop with Intel(R) 82579LM Gigabit Network adapter (driver e1c62x64.sys (11.13.51.0) and DW1530 Wireless-N WLAN Half-Mini Card - I have the same problem on both.</p></div><div id="question-tags" class="tags-container tags">missing local packet wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Sep '12, 22:15</strong></p><img src="https://secure.gravatar.com/avatar/a29ad41036132c6b8ad6f9b3ac62d91c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pgavrailov&#39;s gravatar image" /><p>pgavrailov<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pgavrailov has no accepted answers">0%</span></p></div></div><div id="comments-container-14075" class="comments-container"><span id="14100"></span><div id="comment-14100" class="comment"><div id="post-14100-score" class="comment-score"></div><div class="comment-text"><p>Do you see local traffic if you use <a href="http://www.winpcap.org/windump/default.htm">WinDump</a>? If not, it's more than likely a <a href="http://www.winpcap.org/default.htm">WinPcap</a> issue and not a Wireshark issue. Speaking of WinPcap, I vaguely recall a problem someone had where downgrading to an earlier version of WinPcap solved his problem. I don't recall the specifics so I'm not sure if it would be applicable in your case, but I suppose it wouldn't hurt to try. If memory serves, I think he had tried <a href="http://www.winpcap.org/archive/3.1-WinPcap.exe">WinPcap version 3.1</a>.</p></div><div id="comment-14100-info" class="comment-info"><span class="comment-age">(06 Sep '12, 18:44)</span> cmaynard ♦♦</div></div></div><div id="comment-tools-14075" class="comment-tools"></div><div class="clear"></div><div id="comment-14075-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14110"></span>

<div id="answer-container-14110" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14110-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Here are some possible reasons.</p><ul><li><p>TCP Offloading, although you should then see "some" traffic. Anyway, please check:</p><blockquote><p><code>http://ask.wireshark.org/questions/13131/wireshark-does-not-capture-packets-w-payloads</code><br />
<code>http://ask.wireshark.org/questions/12996/pci-nic-interferes-with-traffic-wireshark-setup</code><br />
</p></blockquote></li><li><p>Windows Firewall or any other interfering software on the PC (AV, VPN, Endpoint Security, IDS, etc.). Please disable and try again.</p></li></ul><blockquote><p><code>http://ask.wireshark.org/questions/11149/why-does-wireshark-not-capture-any-traffic-from-source-machine-with-outbound-firewall-rules</code><br />
</p></blockquote><ul><li>WinPcap not running (properly)</li></ul><blockquote><p><code>sc stop npf</code><br />
<code>sc start npf</code><br />
</p></blockquote><p>BTW: Dou you see non-local traffic (Broadcasts)?</p><p>Regards Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Sep '12, 02:36</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-14110" class="comments-container"></div><div id="comment-tools-14110" class="comment-tools"></div><div class="clear"></div><div id="comment-14110-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


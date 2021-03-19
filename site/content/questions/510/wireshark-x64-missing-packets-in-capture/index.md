+++
type = "question"
title = "Wireshark x64 missing packets in capture"
description = '''I have a laptop with Windows 7 x64 Ultimate. I run the latest Wireshark version 1.4.1. I am running a capture on a switch port that has LACP traffic, which Wireshark should decode as &quot;slow&quot;. All these packets are missing in my capture. If I boot into a Windows 7 x32 (laptop has a dual boot). I can r...'''
date = "2010-10-14T13:01:00Z"
lastmod = "2010-10-19T16:29:00Z"
weight = 510
keywords = [ "lacp" ]
aliases = [ "/questions/510" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark x64 missing packets in capture](/questions/510/wireshark-x64-missing-packets-in-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-510-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a laptop with Windows 7 x64 Ultimate. I run the latest Wireshark version 1.4.1. I am running a capture on a switch port that has LACP traffic, which Wireshark should decode as "slow". All these packets are missing in my capture. If I boot into a Windows 7 x32 (laptop has a dual boot). I can run the same 32bit version of Wireshark &amp; see this traffic in the capture.</p><p>Is there some know bug? Could someone help? I'd be happy to provide additional information if needed.</p><p>Thanks -Kevin</p></div><div id="question-tags" class="tags-container tags">lacp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Oct '10, 13:01</strong></p><img src="https://secure.gravatar.com/avatar/65d7288d8d50cd5739ab7bb7f5c983e0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ktwo&#39;s gravatar image" /><p>ktwo<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ktwo has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 10 Nov '10, 07:02</p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-510" class="comments-container"><span id="519"></span><div id="comment-519" class="comment"><div id="post-519-score" class="comment-score"></div><div class="comment-text"><p>Hi Keven, I don't have an answer, but I seeing very alike issues with the latest version of w-shark on a 64bit windows 2008 R2 with MS TMG installed on it. It seems to be missing packets in the capture and it's irregular. I have duplicated the situation on a number of systems, some miss all packets, others see the packets going out of the nic but no return packets. Kind regards, Tom</p></div><div id="comment-519-info" class="comment-info"><span class="comment-age">(16 Oct '10, 01:42)</span> Tom Decaluwe</div></div></div><div id="comment-tools-510" class="comment-tools"></div><div class="clear"></div><div id="comment-510-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="548"></span>

<div id="answer-container-548" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-548-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>There are a number of possible reasons, but they may be hard to verify:</p><ul><li>the Windows personal firewall discards the frames before Wireshark can capture them -&gt; turn of Firewall to check</li><li>The NIC driver discards the LACP frames because it isn't capable or configured to handle them (I have seen similar things happen to VLAN tagged frames being dropped and Wireshark never receiving them) -&gt; install a different capture software, like NetMon and check, if the frames are still missing. Then at least you can rule out Wireshark (or not).</li><li>Can you configure LACP on your NIC? Is it configured on the 32bit OS?</li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Oct '10, 16:29</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-548" class="comments-container"><span id="555"></span><div id="comment-555" class="comment"><div id="post-555-score" class="comment-score"></div><div class="comment-text"><p>Firewall is disabled. Nic driver should be irrelevant, I've tried 2 separate NIC's. Same device &amp; NIC's booted into 32bit version of W7 capture packets. This is clearly an x64 issue. Be it OS or driver <em>shrugs</em></p><p>LACP is not required to be configured on the capture device.</p></div><div id="comment-555-info" class="comment-info"><span class="comment-age">(20 Oct '10, 05:32)</span> ktwo</div></div></div><div id="comment-tools-548" class="comment-tools"></div><div class="clear"></div><div id="comment-548-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


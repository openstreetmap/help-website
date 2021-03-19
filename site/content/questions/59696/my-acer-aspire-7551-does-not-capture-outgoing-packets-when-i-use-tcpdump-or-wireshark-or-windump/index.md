+++
type = "question"
title = "My Acer ASPIRE 7551 does not capture outgoing packets when I use tcpdump or Wireshark or Windump"
description = '''For measuring performance I want to use my laptop ACER ASPIRE 7551 to capture packet headers with tcpdump. However this laptop does only capture incoming packets and no outgoing packets. Anyone knows a solution?'''
date = "2017-02-26T12:41:00Z"
lastmod = "2017-02-26T14:53:00Z"
weight = 59696
keywords = [ "capture", "packet" ]
aliases = [ "/questions/59696" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [My Acer ASPIRE 7551 does not capture outgoing packets when I use tcpdump or Wireshark or Windump](/questions/59696/my-acer-aspire-7551-does-not-capture-outgoing-packets-when-i-use-tcpdump-or-wireshark-or-windump)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59696-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>For measuring performance I want to use my laptop ACER ASPIRE 7551 to capture packet headers with tcpdump. However this laptop does only capture incoming packets and no outgoing packets. Anyone knows a solution?</p></div><div id="question-tags" class="tags-container tags">capture packet</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Feb '17, 12:41</strong></p><img src="https://secure.gravatar.com/avatar/a44fd1d21bb8b2bb3c3fa185651359e7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Michael%20Kok&#39;s gravatar image" /><p>Michael Kok<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Michael Kok has no accepted answers">0%</span></p></div></div><div id="comments-container-59696" class="comments-container"><span id="59699"></span><div id="comment-59699" class="comment"><div id="post-59699-score" class="comment-score"></div><div class="comment-text"><p>So is your laptop running Windows or some other OS? I presume from "Windump" that it's running Windows, but does "tcpdump" mean you also run, for example, Linux on it, or is this a version of tcpdump built for Windows (as opposed to the packaged WinDump)?</p></div><div id="comment-59699-info" class="comment-info"><span class="comment-age">(26 Feb '17, 20:51)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-59696" class="comment-tools"></div><div class="clear"></div><div id="comment-59696-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59698"></span>

<div id="answer-container-59698" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59698-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>In that case you have to disable the antivirus, vpn or personal fw software</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Feb '17, 14:53</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p>Christian_R<br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Feb '17, 15:05</p></div></div><div id="comments-container-59698" class="comments-container"><span id="59817"></span><div id="comment-59817" class="comment"><div id="post-59817-score" class="comment-score"></div><div class="comment-text"><p>Hi Guy, Christian, Thanks for responding. I tried this on Windows 7 with, Windump, MicroOLAP Tcpdump and wireshark. Always no outbound packets captured. No Virus scanner, no restrictions on the firewall (traffic is handled normally, only captures fail), there is no VPN. Other PC and other laptop configured likewise do not show the problem.</p></div><div id="comment-59817-info" class="comment-info"><span class="comment-age">(03 Mar '17, 01:36)</span> Michael Kok</div></div><span id="59820"></span><div id="comment-59820" class="comment"><div id="post-59820-score" class="comment-score"></div><div class="comment-text"><p>Well I thought there were no restrictions at the firewall, but sometimes the firewall itself causes the problem. So please try to disable it for one try.</p></div><div id="comment-59820-info" class="comment-info"><span class="comment-age">(03 Mar '17, 02:13)</span> Christian_R</div></div><span id="59823"></span><div id="comment-59823" class="comment"><div id="post-59823-score" class="comment-score"></div><div class="comment-text"><p>As WinPcap plainly works for millions (yes literally) of other users as @Christian_R says it likely that it's something on your system that's interfering.</p><p>A stock Windows system has no issues, once you install software from others, e.g VPN, Firewall, AV and others, then they can interfere with the network stack. Various application of this sort have definitely been known to cause this issue.</p><p>Please try downloading WinPCap from <a href="https://www.winpcap.org/install/default.htm">here</a>, uninstalling WinPcap, rebooting and reinstalling WinPCap.</p></div><div id="comment-59823-info" class="comment-info"><span class="comment-age">(03 Mar '17, 03:54)</span> grahamb ♦</div></div></div><div id="comment-tools-59698" class="comment-tools"></div><div class="clear"></div><div id="comment-59698-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


+++
type = "question"
title = "Does Wireshark support this adapter?"
description = '''My house has a wireless network, with a Netgear router that is password protected. I am on my desktop, which initially to get internet I had to bridge the connection between it and a laptop. The other week, I bought a Netgear N300 Wireless USB adapter. Anyways, I was using Wireshark the other week w...'''
date = "2012-04-20T10:08:00Z"
lastmod = "2012-04-20T10:52:00Z"
weight = 10353
keywords = [ "supported", "usb", "wireshark" ]
aliases = [ "/questions/10353" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Does Wireshark support this adapter?](/questions/10353/does-wireshark-support-this-adapter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10353-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>My house has a wireless network, with a Netgear router that is password protected. I am on my desktop, which initially to get internet I had to bridge the connection between it and a laptop. The other week, I bought a Netgear N300 Wireless USB adapter. Anyways, I was using Wireshark the other week while the desktop was tethered to my laptop. Now, however, I have the USB adapter. When I open Wireshark, I see the interface list, which only shows my wired connection, that isn't even active. My question is, how do I get my USB adapter to show up in the 'interfaces' list? I would really like to get to know how to use Wireshark better, but I am not going to bridge a connection between my desktop and laptop forever. Any help is greatly appreciated!</p></div><div id="question-tags" class="tags-container tags">supported usb wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Apr '12, 10:08</strong></p><img src="https://secure.gravatar.com/avatar/92b93851d825820bdbc548172f153724?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ekaj&#39;s gravatar image" /><p>ekaj<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ekaj has no accepted answers">0%</span></p></div></div><div id="comments-container-10353" class="comments-container"></div><div id="comment-tools-10353" class="comment-tools"></div><div class="clear"></div><div id="comment-10353-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10354"></span>

<div id="answer-container-10354" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10354-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark supports an adapter if and only if libpcap/WinPcap, and the underlying capture mechanism it supports, does so, as Wireshark relies on libpcap/WinPcap for capturing.</p><p>If this is Windows, you should see whether <a href="http://www.winpcap.org/windump/install/default.htm">WinDump</a> recognizes the adapter. If not, this is a WinPcap bug, and should be <a href="http://www.winpcap.org/bugs.htm">reported to the WinPcap developers</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Apr '12, 10:52</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-10354" class="comments-container"></div><div id="comment-tools-10354" class="comment-tools"></div><div class="clear"></div><div id="comment-10354-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


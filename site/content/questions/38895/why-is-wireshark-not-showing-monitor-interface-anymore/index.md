+++
type = "question"
title = "Why is Wireshark not showing monitor interface anymore?"
description = '''I&#x27;ve been using Kali for about 2 weeks and been playing around with Wireshark a lot in that time. About 30 minutes ago, Wireshark stopped showing the &quot;mon0&quot; interface after I input the &quot;airmon-ng start wlan0&quot; command. I refresh the interface list and get nothing. And NOW when I sniff with just the &quot;...'''
date = "2015-01-05T12:34:00Z"
lastmod = "2015-01-06T14:51:00Z"
weight = 38895
keywords = [ "packets", "monitor" ]
aliases = [ "/questions/38895" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Why is Wireshark not showing monitor interface anymore?](/questions/38895/why-is-wireshark-not-showing-monitor-interface-anymore)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38895-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've been using Kali for about 2 weeks and been playing around with Wireshark a lot in that time.</p><p>About 30 minutes ago, Wireshark stopped showing the "mon0" interface after I input the "airmon-ng start wlan0" command. I refresh the interface list and get nothing.</p><p>And NOW when I sniff with just the "wlan0" interface, promiscuous mode only (no monitor mode check box) I can't capture ANY packets. What could be causing this? It was working wonderfully just this morning.</p></div><div id="question-tags" class="tags-container tags">packets monitor</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Jan '15, 12:34</strong></p><img src="https://secure.gravatar.com/avatar/edbd4c64dc2b657a3c858042a6cbf85b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TerribleIvan&#39;s gravatar image" /><p>TerribleIvan<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TerribleIvan has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 06 Jan '15, 08:32</p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-38895" class="comments-container"></div><div id="comment-tools-38895" class="comment-tools"></div><div class="clear"></div><div id="comment-38895-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38912"></span>

<div id="answer-container-38912" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38912-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Well, this has been resolved. Somehow, under preferences, the check box for "hide interface" was checked on mon0. But, it seems to revert to that each time I reopen the program. It's probably something dumb I did accidentally.</p><p>Wlan0 capturing resolved itself somehow, so I'm back to full functionality, I'm just not sure exactly what caused the initial issue.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Jan '15, 14:51</strong></p><img src="https://secure.gravatar.com/avatar/edbd4c64dc2b657a3c858042a6cbf85b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TerribleIvan&#39;s gravatar image" /><p>TerribleIvan<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TerribleIvan has no accepted answers">0%</span></p></div></div><div id="comments-container-38912" class="comments-container"></div><div id="comment-tools-38912" class="comment-tools"></div><div class="clear"></div><div id="comment-38912-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


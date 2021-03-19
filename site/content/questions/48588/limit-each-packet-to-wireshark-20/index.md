+++
type = "question"
title = "&quot;Limit each packet to&quot; Wireshark 2.0"
description = '''Hi, Where can i find &quot;Limit each packet to&quot; in Windows 10 Wireshark? I can find it in linux by doubleclicking on my interface. But i cant find it on Windows? Any clues?'''
date = "2015-12-16T15:09:00Z"
lastmod = "2015-12-16T17:05:00Z"
weight = 48588
keywords = [ "snaplen", "wireshark" ]
aliases = [ "/questions/48588" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# ["Limit each packet to" Wireshark 2.0](/questions/48588/limit-each-packet-to-wireshark-20)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48588-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, Where can i find "Limit each packet to" in Windows 10 Wireshark? I can find it in linux by doubleclicking on my interface. But i cant find it on Windows? Any clues?</p></div><div id="question-tags" class="tags-container tags">snaplen wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Dec '15, 15:09</strong></p><img src="https://secure.gravatar.com/avatar/464c35db7abc9a7a3ec7b163eac84d99?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Marko&#39;s gravatar image" /><p>Marko<br />
<span class="score" title="1 reputation points">1</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Marko has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Dec '15, 17:06</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-48588" class="comments-container"></div><div id="comment-tools-48588" class="comment-tools"></div><div class="clear"></div><div id="comment-48588-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48589"></span>

<div id="answer-container-48589" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48589-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>In the GTK+ ("legacy") version of Wireshark 2.0 and later, as in Wireshark 1.12, on <em>all</em> operating systems (Linux, OS X, Windows, *BSD, Solaris, AIX, HP-UX, etc.), you can change various per-interface settings, including the size to which captured packets are truncated before saving them, by double-clicking on the interface in the splash screen or the Capture -&gt; Options dialog and editing the "Limit each packet to" field.</p><p>In the Qt version of Wireshark 2.0 and later, on <em>all</em> operating systems, you can change various per-interface settings, including the size to which captured packets are truncated before saving them, by selecting Capture -&gt; Options, clicking on the "Snaplen (B)" column for the interface, and editing the value.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Dec '15, 17:05</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-48589" class="comments-container"></div><div id="comment-tools-48589" class="comment-tools"></div><div class="clear"></div><div id="comment-48589-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


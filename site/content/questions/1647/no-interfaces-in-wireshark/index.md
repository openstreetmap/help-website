+++
type = "question"
title = "No interfaces in wireshark"
description = '''Hello all, I installed wireshark on Ubuntu 10.4 with Synaptic, but in Capture Options I don&#x27;t see any interfaces? Some one know what is wrong here? Thanks for the support Sincerely Herman'''
date = "2011-01-06T03:13:00Z"
lastmod = "2011-01-06T15:02:00Z"
weight = 1647
keywords = [ "interfaces", "missing" ]
aliases = [ "/questions/1647" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [No interfaces in wireshark](/questions/1647/no-interfaces-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1647-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello all,</p><p>I installed wireshark on Ubuntu 10.4 with Synaptic, but in Capture Options I don't see any interfaces? Some one know what is wrong here?</p><p>Thanks for the support Sincerely Herman</p></div><div id="question-tags" class="tags-container tags">interfaces missing</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Jan '11, 03:13</strong></p><img src="https://secure.gravatar.com/avatar/5de2e3d49a9a0474005c91f3d5831069?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="blakkie&#39;s gravatar image" /><p>blakkie<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="blakkie has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 28 Feb '12, 20:14</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-1647" class="comments-container"></div><div id="comment-tools-1647" class="comment-tools"></div><div class="clear"></div><div id="comment-1647-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1655"></span>

<div id="answer-container-1655" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1655-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Your dumpcap program needs elevated privileges. Either look to setuid dumpcap as root, create a wireshark group with elevated privileges, setgid dumpcap to that group, and add yourself to that group. Another, but bad, option is to run wireshark with root privileges.</p><p>There's a <a href="https://blog.wireshark.org/2010/02/running-wireshark-as-you/">good blog entry</a> by Gerald on this issue.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Jan '11, 15:02</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-1655" class="comments-container"></div><div id="comment-tools-1655" class="comment-tools"></div><div class="clear"></div><div id="comment-1655-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


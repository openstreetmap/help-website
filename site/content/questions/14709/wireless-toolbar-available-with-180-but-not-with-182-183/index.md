+++
type = "question"
title = "Wireless Toolbar Available with 1.8.0 but NOT with 1.8.2, 1.8.3"
description = '''AirPcap is installed, Wireshark 1.8.0 displays wireless toolbar, 1.8.2, 1.8.3 DO NOT. Is there a remedy? Has that not been tested? Jasper&#x27;s answer was not the solution. The wireless toolbar is more specifically grayed-out and unavailable, not completely absent. If the View option is used to disabled...'''
date = "2012-10-04T08:54:00Z"
lastmod = "2012-10-05T19:33:00Z"
weight = 14709
keywords = [ "wireless_toolbar", "1.8.3", "wireshark" ]
aliases = [ "/questions/14709" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Wireless Toolbar Available with 1.8.0 but NOT with 1.8.2, 1.8.3](/questions/14709/wireless-toolbar-available-with-180-but-not-with-182-183)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14709-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>AirPcap is installed, Wireshark 1.8.0 displays wireless toolbar, 1.8.2, 1.8.3 DO NOT. Is there a remedy? Has that not been tested?</p><p>Jasper's answer was not the solution. The wireless toolbar is more specifically grayed-out and unavailable, not completely absent. If the View option is used to disabled it, the display of the wireless toolbar disappears. Re-enabling it in the view only restores the grayed-out, inaccessible display. I have seen the behavior on 3 different PCs here in my workplace.</p><p>The toolbar remains grayed-out during an active wireless capture. The main problem is that there is no way to select a channel during a running capture. Windows XP is the OS.</p></div><div id="question-tags" class="tags-container tags">wireless_toolbar 1.8.3 wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Oct '12, 08:54</strong></p><img src="https://secure.gravatar.com/avatar/fd19e916537be26c16dd3af85218c492?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tegwood&#39;s gravatar image" /><p>tegwood<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tegwood has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 05 Oct '12, 05:22</p></div></div><div id="comments-container-14709" class="comments-container"><span id="14726"></span><div id="comment-14726" class="comment"><div id="post-14726-score" class="comment-score"></div><div class="comment-text"><p>Does it remain grayed out when you have a capture running on the AirPcap adapter? I tried 1.8.2 on a (virtual) Windows 7 machine with an AirPcap adapter plugged into it, and the toolbar was grayed out until I started a capture on the AirPcap adapter.</p></div><div id="comment-14726-info" class="comment-info"><span class="comment-age">(04 Oct '12, 18:45)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-14709" class="comment-tools"></div><div class="clear"></div><div id="comment-14709-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="14719"></span>

<div id="answer-container-14719" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14719-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Have you tried the View menu option "Wireless Toolbar"? Is it checkmarked? If not, checkmark it -&gt; there you have your toolbar.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Oct '12, 13:31</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-14719" class="comments-container"></div><div id="comment-tools-14719" class="comment-tools"></div><div class="clear"></div><div id="comment-14719-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="14743"></span>

<div id="answer-container-14743" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14743-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Could you file a bug on this at the <a href="http://bugs.wireshark.org/">Wireshark Bugzilla</a>? From a quick look at the code, there's no place where the wireless toolbar gets explicitly enabled, just places where it's explicitly <em>dis</em>abled, so it might be that it's only enabled if it's been created and never been disabled.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Oct '12, 19:33</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-14743" class="comments-container"><span id="15005"></span><div id="comment-15005" class="comment"><div id="post-15005-score" class="comment-score"></div><div class="comment-text"><p>Bug opened by Tom: <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=7837">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=7837</a></p></div><div id="comment-15005-info" class="comment-info"><span class="comment-age">(15 Oct '12, 01:48)</span> Raul Siles</div></div></div><div id="comment-tools-14743" class="comment-tools"></div><div class="clear"></div><div id="comment-14743-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


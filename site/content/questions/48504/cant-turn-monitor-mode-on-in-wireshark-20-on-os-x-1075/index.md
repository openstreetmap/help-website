+++
type = "question"
title = "Can&#x27;t turn monitor mode on in Wireshark 2.0 on OS X 10.7.5"
description = '''Sadly I&#x27;m getting the same problem as in this question on 2.0.0-g9a73b82 on OSX 10.7.5 (Wireshark 1.12.x was working fine with monitor mode capture).'''
date = "2015-12-14T02:42:00Z"
lastmod = "2016-01-03T13:12:00Z"
weight = 48504
keywords = [ "osx", "monitor-mode" ]
aliases = [ "/questions/48504" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Can't turn monitor mode on in Wireshark 2.0 on OS X 10.7.5](/questions/48504/cant-turn-monitor-mode-on-in-wireshark-20-on-os-x-1075)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48504-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Sadly I'm getting the same problem as in <a href="https://ask.wireshark.org/questions/47125/cant-turn-on-monitor-mode-on-macbook-pro-with-wireshark-1999">this question</a> on 2.0.0-g9a73b82 on OSX 10.7.5 (Wireshark 1.12.x was working fine with monitor mode capture).</p></div><div id="question-tags" class="tags-container tags">osx monitor-mode</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Dec '15, 02:42</strong></p><img src="https://secure.gravatar.com/avatar/244c3e907ae3f16a00a6c18ea331b36b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pierz&#39;s gravatar image" /><p>pierz<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pierz has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 14 Dec '15, 10:22</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-48504" class="comments-container"><span id="48509"></span><div id="comment-48509" class="comment"><div id="post-48509-score" class="comment-score"></div><div class="comment-text"><p>I.e., if you select the Options item from the Capture menu, the entry in the list for your Wi-Fi adapter has "disabled" in the "Monitor Mode" column - note that you might have to scroll that list horizontally to see that column - and if you double-click "disabled", it doesn't let you select "enabled" from a drop-down list of "enabled" and "disabled"?</p></div><div id="comment-48509-info" class="comment-info"><span class="comment-age">(14 Dec '15, 10:20)</span> Guy Harris ♦♦</div></div><span id="48778"></span><div id="comment-48778" class="comment"><div id="post-48778-score" class="comment-score"></div><div class="comment-text"><p>Furthermore - - as the OP said - 2.0 didn't do monitor mode - 1.12 did - 2.0 coudn't be uninstalled - - 2.01 says it installed but is not there - even though 2.0 was thrown away - 1.12 cannot be re-installed Wwe were told at Sharkfest you could have both 1 and 2 -</p></div><div id="comment-48778-info" class="comment-info"><span class="comment-age">(31 Dec '15, 12:49)</span> packetlevel</div></div><span id="48808"></span><div id="comment-48808" class="comment"><div id="post-48808-score" class="comment-score"></div><div class="comment-text"><p>Update - 2.0.1 installed, sees interfaces But will not do monitor mode 1.12.9 which used to work fine, will not install on OS X</p><p>The error "Unable to set data link type on interface 'en0' (EN10MB is not one of the DLTs supported by this device)." is displayed.</p></div><div id="comment-48808-info" class="comment-info"><span class="comment-age">(03 Jan '16, 09:25)</span> packetlevel</div></div><span id="48809"></span><div id="comment-48809" class="comment"><div id="post-48809-score" class="comment-score"></div><div class="comment-text"><p>What do <code>tcpdump -i en0 -L</code> and <code>tcpdump -i en0 -I -L</code> print?</p></div><div id="comment-48809-info" class="comment-info"><span class="comment-age">(03 Jan '16, 12:46)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-48504" class="comment-tools"></div><div class="clear"></div><div id="comment-48504-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48810"></span>

<div id="answer-container-48810" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48810-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>This is probably <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=11364">bug 11364</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Jan '16, 13:12</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-48810" class="comments-container"></div><div id="comment-tools-48810" class="comment-tools"></div><div class="clear"></div><div id="comment-48810-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


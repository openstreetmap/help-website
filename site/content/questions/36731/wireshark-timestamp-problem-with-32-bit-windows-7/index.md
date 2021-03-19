+++
type = "question"
title = "Wireshark timestamp problem with 32-bit Windows 7"
description = '''Hello, I have installed Wireshark 1.12.1 on two machines, one with 64-bit Windows 7, and the other with 32-bit Windows 7. Both machine&#x27;s dates and timezones are set correctly (Central Europe summer time, which is currently 2 hours in advance of GMT/UTC. The 64-bit machine displays timestamps correct...'''
date = "2014-09-30T10:04:00Z"
lastmod = "2014-10-01T06:14:00Z"
weight = 36731
keywords = [ "windows7", "wrongtimestamp" ]
aliases = [ "/questions/36731" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark timestamp problem with 32-bit Windows 7](/questions/36731/wireshark-timestamp-problem-with-32-bit-windows-7)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36731-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I have installed Wireshark 1.12.1 on two machines, one with 64-bit Windows 7, and the other with 32-bit Windows 7. Both machine's dates and timezones are set correctly (Central Europe summer time, which is currently 2 hours in advance of GMT/UTC.</p><p>The 64-bit machine displays timestamps correctly, the 32-bit machine displays time delayed by 2 hours (GMT/UTC?). I've checked that the same options are displayed for both machines using "View -&gt; Time Display Format -&gt; Time Of Day".</p><p>When I select the "UTC Time Of Day" option, the 64-bit machine adjusts its timestamps backwards by two hours, as expected; the 32-bit machine displays the same timestamps unchanged. I've changed the 32-bit computer's timezone to use other timezones, and the timestamps remain unchanged. When I use other display formats, such as "Date (with day of year) and Time Of Day", the timestamps remain unchanged.</p><p>I've uninstalled and reinstalled the 32-bit version, but the problem is still there. Is this a bug with 32-bit Windows timestamps?</p><p>Can anyone help? Paul</p></div><div id="question-tags" class="tags-container tags">windows7 wrongtimestamp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Sep '14, 10:04</strong></p><img src="https://secure.gravatar.com/avatar/a4b4d81519d7610213af734081ad6cb6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="polomora&#39;s gravatar image" /><p>polomora<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="polomora has no accepted answers">0%</span></p></div></div><div id="comments-container-36731" class="comments-container"></div><div id="comment-tools-36731" class="comment-tools"></div><div class="clear"></div><div id="comment-36731-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36756"></span>

<div id="answer-container-36756" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36756-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Does the "broken" version (32 bit one) have the time column set to be "Time (format as specified)" or "UTC time" (right click the column, then select "Edit Column Details" to check). I suspect you have the latter that doesn't track the specified time format.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Oct '14, 06:14</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-36756" class="comments-container"><span id="36761"></span><div id="comment-36761" class="comment"><div id="post-36761-score" class="comment-score"></div><div class="comment-text"><p>grahamb,</p><p>Many thanks, that fixed it. Confusing that it cannot be adjust from the "View -&gt; Time Display Format -&gt; Time Of Day" menu option. Wierd.</p><p>In any case, fixed.</p><p>Paul</p></div><div id="comment-36761-info" class="comment-info"><span class="comment-age">(01 Oct '14, 11:28)</span> polomora</div></div><span id="36763"></span><div id="comment-36763" class="comment"><div id="post-36763-score" class="comment-score"></div><div class="comment-text"><p>The view option only affects those columns that use the "... as specified" type.</p><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-36763-info" class="comment-info"><span class="comment-age">(01 Oct '14, 12:05)</span> grahamb ♦</div></div></div><div id="comment-tools-36756" class="comment-tools"></div><div class="clear"></div><div id="comment-36756-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


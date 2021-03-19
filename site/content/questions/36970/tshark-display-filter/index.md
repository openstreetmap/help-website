+++
type = "question"
title = "tshark display filter"
description = '''I&#x27;m using tshark extract smb.file information from a capture file. I have verified the the requested information is in the file using this wireshark filter:  smb.file == &quot;&#92;&#92;EVS_LowRes&#92;&#92;20141009 MLB TESTING_4.dv&quot;  However when using the following tshark filter I get no result: tshark -Y &quot;smb.file == ...'''
date = "2014-10-11T12:39:00Z"
lastmod = "2014-10-11T12:43:00Z"
weight = 36970
keywords = [ "filter", "tshark" ]
aliases = [ "/questions/36970" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [tshark display filter](/questions/36970/tshark-display-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36970-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm using tshark extract smb.file information from a capture file. I have verified the the requested information is in the file using this wireshark filter:</p><pre><code>smb.file == &quot;\\EVS_LowRes\\20141009 MLB TESTING_4.dv&quot;</code></pre><p>However when using the following tshark filter I get no result:</p><pre><code>tshark -Y &quot;smb.file == \&quot;\EVS_LowRes\20141009 MLB TESTING_4.dv&quot;\&quot; -r SharingViolation.trc</code></pre><p>can someone please provide some insight…</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">filter tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Oct '14, 12:39</strong></p><img src="https://secure.gravatar.com/avatar/9fbf87fc0b9912321ad25e9e51c60f46?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dblk&#39;s gravatar image" /><p>dblk<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dblk has no accepted answers">0%</span></p></div></div><div id="comments-container-36970" class="comments-container"></div><div id="comment-tools-36970" class="comment-tools"></div><div class="clear"></div><div id="comment-36970-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36971"></span>

<div id="answer-container-36971" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36971-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>What happens if you use the filter</p><pre><code>tshark -Y &quot;smb.file == \&quot;\\\\EVS_LowRes\20141009 MLB TESTING_4.dv&quot;\&quot; -r SharingViolation.trc</code></pre><p>or</p><pre><code>tshark -Y &quot;smb.file == \&quot;\\EVS_LowRes\20141009 MLB TESTING_4.dv&quot;\&quot; -r SharingViolation.trc</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Oct '14, 12:43</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-36971" class="comments-container"><span id="36973"></span><div id="comment-36973" class="comment"><div id="post-36973-score" class="comment-score"></div><div class="comment-text"><p>Guy thanks for the insight. Below is what worked:</p><pre><code>\&quot;\\\EVS_LowRes\\\20141009 MLB TESTING_4.dv&quot;\&quot; -r SharingViolation.trc</code></pre></div><div id="comment-36973-info" class="comment-info"><span class="comment-age">(11 Oct '14, 12:50)</span> dblk</div></div><span id="36975"></span><div id="comment-36975" class="comment"><div id="post-36975-score" class="comment-score"></div><div class="comment-text"><p>Was this done with a Windows command line or a UN*X command line? The one with four backslashes might be required on UN*X.</p></div><div id="comment-36975-info" class="comment-info"><span class="comment-age">(11 Oct '14, 12:57)</span> Guy Harris ♦♦</div></div><span id="36976"></span><div id="comment-36976" class="comment"><div id="post-36976-score" class="comment-score"></div><div class="comment-text"><p>It was done in mac os x terminal</p></div><div id="comment-36976-info" class="comment-info"><span class="comment-age">(11 Oct '14, 13:44)</span> dblk</div></div></div><div id="comment-tools-36971" class="comment-tools"></div><div class="clear"></div><div id="comment-36971-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


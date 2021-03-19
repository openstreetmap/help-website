+++
type = "question"
title = "WS 2.4 fails to start - Err  Field &#x27;APDU Rsp Time&#x27; (transum.art) is a FT_ABSOLUTE_TIME ..."
description = '''I installed Wireshark 2.4. On startup I got: 20:06:51 Err Field &#x27;APDU Rsp Time&#x27; (transum.art) is a FT_ABSOLUTE_TIME but is being displayed as BASE_NONE instead of as a time I&#x27;ll answer this myself - I just wanted to record it here.'''
date = "2017-07-19T12:15:00Z"
lastmod = "2017-07-19T12:18:00Z"
weight = 62894
keywords = [ "wireshark-2.4" ]
aliases = [ "/questions/62894" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [WS 2.4 fails to start - Err Field 'APDU Rsp Time' (transum.art) is a FT\_ABSOLUTE\_TIME ...](/questions/62894/ws-24-fails-to-start-err-field-apdu-rsp-time-transumart-is-a-ft_absolute_time)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62894-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I installed Wireshark 2.4. On startup I got:</p><p>20:06:51 Err Field 'APDU Rsp Time' (transum.art) is a FT_ABSOLUTE_TIME but is being displayed as BASE_NONE instead of as a time</p><p>I'll answer this myself - I just wanted to record it here.</p></div><div id="question-tags" class="tags-container tags">wireshark-2.4</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Jul '17, 12:15</strong></p><img src="https://secure.gravatar.com/avatar/2e1b4057f2ff59fe059b23cc6571abaf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PaulOfford&#39;s gravatar image" /><p>PaulOfford<br />
<span class="score" title="131 reputation points">131</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="32 badges"><span class="silver">●</span><span class="badgecount">32</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PaulOfford has 5 accepted answers">11%</span></p></div></div><div id="comments-container-62894" class="comments-container"></div><div id="comment-tools-62894" class="comment-tools"></div><div class="clear"></div><div id="comment-62894-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62895"></span>

<div id="answer-container-62895" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62895-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>This problem occurs if you used the TribeLab transum.dll with Wireshark 2.2. To fix it go to %APPDATA%\Wireshark\plugins and delete the copy of transum.dll that you find there.</p><p>If this isn't the cause, make sure that you don't have the transum.dll installed in c:\program files\Wireshark\plugins\2.2.x</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jul '17, 12:18</strong></p><img src="https://secure.gravatar.com/avatar/2e1b4057f2ff59fe059b23cc6571abaf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PaulOfford&#39;s gravatar image" /><p>PaulOfford<br />
<span class="score" title="131 reputation points">131</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="32 badges"><span class="silver">●</span><span class="badgecount">32</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PaulOfford has 5 accepted answers">11%</span></p></div></div><div id="comments-container-62895" class="comments-container"></div><div id="comment-tools-62895" class="comment-tools"></div><div class="clear"></div><div id="comment-62895-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


+++
type = "question"
title = "Wireshark does not start. Error 0xC0000005"
description = '''Hi, I recently updated my local copy, i fixed all conflict I had but now wireshark does not start. When I debug the code the program stops at test_if_on() function (airpcap_loader.c). The message error is &quot;Unhandled exception at 0x0108add4 in wireshark.exe: 0xC0000005: Access violation reading locat...'''
date = "2013-12-24T06:05:00Z"
lastmod = "2013-12-24T12:09:00Z"
weight = 28366
keywords = [ "start", "0xc0000005", "wireshark" ]
aliases = [ "/questions/28366" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Wireshark does not start. Error 0xC0000005](/questions/28366/wireshark-does-not-start-error-0xc0000005)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28366-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I recently updated my local copy, i fixed all conflict I had but now wireshark does not start. When I debug the code the program stops at <code>test_if_on()</code> function (airpcap_loader.c).</p><p>The message error is "Unhandled exception at 0x0108add4 in wireshark.exe: 0xC0000005: Access violation reading location 0xbaadf00d."</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">start 0xc0000005 wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Dec '13, 06:05</strong></p><img src="https://secure.gravatar.com/avatar/4ec6105789137df01b9abed5fcb9ab95?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Afrim&#39;s gravatar image" /><p>Afrim<br />
<span class="score" title="160 reputation points">160</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Afrim has 2 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 24 Dec '13, 06:06</p></div></div><div id="comments-container-28366" class="comments-container"></div><div id="comment-tools-28366" class="comment-tools"></div><div class="clear"></div><div id="comment-28366-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28371"></span>

<div id="answer-container-28371" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28371-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>I also saw this a few days ago but haven't had time to look into it yet: <a href="http://www.wireshark.org/lists/wireshark-dev/201312/msg00224.html.">http://www.wireshark.org/lists/wireshark-dev/201312/msg00224.html.</a></p><p>I looked at it again and it appeared to be a mis-matched prefs structure definition between object files. A <code>make -f Makefile.nmake clean</code> followed by another build fixed it up.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Dec '13, 12:09</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 Dec '13, 02:18</p></div></div><div id="comments-container-28371" class="comments-container"><span id="28401"></span><div id="comment-28401" class="comment"><div id="post-28401-score" class="comment-score"></div><div class="comment-text"><p>Thank you I had the same error and it's fixed now.</p></div><div id="comment-28401-info" class="comment-info"><span class="comment-age">(26 Dec '13, 01:52)</span> Afrim</div></div></div><div id="comment-tools-28371" class="comment-tools"></div><div class="clear"></div><div id="comment-28371-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


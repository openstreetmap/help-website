+++
type = "question"
title = "64 bit plugins on portable wireshark"
description = '''If I compile custom plugin on Windows 64 bit, can I use this plugin on portable Version of wireshark? Thanks'''
date = "2016-10-28T01:58:00Z"
lastmod = "2016-10-28T02:02:00Z"
weight = 56774
keywords = [ "wireshark", "portable", "plugin" ]
aliases = [ "/questions/56774" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [64 bit plugins on portable wireshark](/questions/56774/64-bit-plugins-on-portable-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56774-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>If I compile custom plugin on Windows 64 bit, can I use this plugin on portable Version of wireshark? Thanks</p></div><div id="question-tags" class="tags-container tags">wireshark portable plugin</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Oct '16, 01:58</strong></p><img src="https://secure.gravatar.com/avatar/a908c48c60a3ba8f08a762a9cb58268f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="xaheen&#39;s gravatar image" /><p>xaheen<br />
<span class="score" title="71 reputation points">71</span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="xaheen has one accepted answer">50%</span></p></div></div><div id="comments-container-56774" class="comments-container"></div><div id="comment-tools-56774" class="comment-tools"></div><div class="clear"></div><div id="comment-56774-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56775"></span>

<div id="answer-container-56775" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56775-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Unfortunately no. The portable version is 32 bit, as this allows it to run on both 32 and 64 bit OS's.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Oct '16, 02:02</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-56775" class="comments-container"><span id="56779"></span><div id="comment-56779" class="comment"><div id="post-56779-score" class="comment-score">1</div><div class="comment-text"><p>Note that on Windows 64 bits, you can still copile a 32 bits version of Wireshark. This plugin would be compatible with Wireshark portable.</p></div><div id="comment-56779-info" class="comment-info"><span class="comment-age">(28 Oct '16, 02:18)</span> Pascal Quantin</div></div><span id="56780"></span><div id="comment-56780" class="comment"><div id="post-56780-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot. I just needed this Information. :)</p></div><div id="comment-56780-info" class="comment-info"><span class="comment-age">(28 Oct '16, 02:39)</span> xaheen</div></div><span id="56781"></span><div id="comment-56781" class="comment"><div id="post-56781-score" class="comment-score"></div><div class="comment-text"><p>Ah, I slightly misread the question, @Pascal Quantin is correct that for Windows, you can build both 32 bit and 64 bit Wireshark on either 32 bit or 64 bit of the OS, as Visual Studio provides a cross-compiler.</p></div><div id="comment-56781-info" class="comment-info"><span class="comment-age">(28 Oct '16, 03:10)</span> grahamb ♦</div></div><span id="56784"></span><div id="comment-56784" class="comment"><div id="post-56784-score" class="comment-score"></div><div class="comment-text"><p>so, can I compile wireshark for 32bit Environment on Windows 64bit operating System? So that I can get 32bit plugin.</p></div><div id="comment-56784-info" class="comment-info"><span class="comment-age">(28 Oct '16, 06:33)</span> xaheen</div></div><span id="56785"></span><div id="comment-56785" class="comment"><div id="post-56785-score" class="comment-score">1</div><div class="comment-text"><p>Sure, I do that all the time (compile that is), should be all detailed in the Developers Guide.</p><p>Basically set the env var WIRESHARK_TARGET_PLATFORM to "win32", and download and install a 32 bit Qt and then point the env var QT5_BASE_DIR to the 32 bit Qt. You can have 32 and 64 bit Qt installed at the same time, but in different directories.</p><p>Finally, open the appropriate Visual Studio <a href="https://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html#ChSetupPrepareCommandCom">command prompt</a>.</p></div><div id="comment-56785-info" class="comment-info"><span class="comment-age">(28 Oct '16, 07:00)</span> grahamb ♦</div></div><span id="56786"></span><div id="comment-56786" class="comment not_top_scorer"><div id="post-56786-score" class="comment-score"></div><div class="comment-text"><p>Thanks a bunch :)</p></div><div id="comment-56786-info" class="comment-info"><span class="comment-age">(28 Oct '16, 07:06)</span> xaheen</div></div></div><div id="comment-tools-56775" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-56775-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


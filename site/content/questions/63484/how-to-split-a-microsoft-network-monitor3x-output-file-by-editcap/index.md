+++
type = "question"
title = "how to split a microsoft Network monitor3.x output file by editcap"
description = '''Hi  we get a *.cap file from microsoft Network monitor3.x tools. but it&#x27;s too large for analysis. when we want to split those file by editcap.exe but no file create.  editcap -c 5000 -F netmon2 D:&#92;MicrosoftNTP.cap D:&#92;temp  how to specify the input file type of editcap . the -T -F parameter is only u...'''
date = "2017-08-18T05:07:00Z"
lastmod = "2017-08-18T21:28:00Z"
weight = 63484
keywords = [ "editcap" ]
aliases = [ "/questions/63484" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how to split a microsoft Network monitor3.x output file by editcap](/questions/63484/how-to-split-a-microsoft-network-monitor3x-output-file-by-editcap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63484-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi we get a *.cap file from microsoft Network monitor3.x tools. but it's too large for analysis. when we want to split those file by editcap.exe but no file create. editcap -c 5000 -F netmon2 D:\MicrosoftNTP.cap D:\temp</p><p>how to specify the input file type of editcap . the -T -F parameter is only used for output file.</p></div><div id="question-tags" class="tags-container tags">editcap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Aug '17, 05:07</strong></p><img src="https://secure.gravatar.com/avatar/853d7093103a60a3b0083b42b705b99e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="neil_hao&#39;s gravatar image" /><p>neil_hao<br />
<span class="score" title="26 reputation points">26</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="neil_hao has no accepted answers">0%</span></p></div></div><div id="comments-container-63484" class="comments-container"></div><div id="comment-tools-63484" class="comment-tools"></div><div class="clear"></div><div id="comment-63484-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="63490"></span>

<div id="answer-container-63490" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63490-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>how to specify the input file type of editcap</p></blockquote><p>You can't.</p><p>Because you don't have to.</p><p>The library that Wireshark, TShark, editcap, capinfos, etc. uses to read capture files figures out the file type for you.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Aug '17, 21:28</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-63490" class="comments-container"><span id="63493"></span><div id="comment-63493" class="comment"><div id="post-63493-score" class="comment-score"></div><div class="comment-text"><p>thanks, but how to split this file by tshark? after we run script "editcap -c 5000 -F netmon2 D:\MicrosoftNTP.cap D:\temp", the output file is broken and cant opened by wireshark</p></div><div id="comment-63493-info" class="comment-info"><span class="comment-age">(20 Aug '17, 23:17)</span> neil_hao</div></div><span id="63494"></span><div id="comment-63494" class="comment"><div id="post-63494-score" class="comment-score">1</div><div class="comment-text"><blockquote><p>editcap ... the output file is broken and cant opened by wireshark</p></blockquote><p>That would therefore be a bug in editcap - if it writes a file that can't be read by Wireshark, that's a bug.</p><p>Please file a but on <a href="http://bugs.wireshark.org">the Wireshark Bugzilla</a>, and attach the input file you're using, so we can try to reproduce it.</p></div><div id="comment-63494-info" class="comment-info"><span class="comment-age">(20 Aug '17, 23:47)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-63490" class="comment-tools"></div><div class="clear"></div><div id="comment-63490-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


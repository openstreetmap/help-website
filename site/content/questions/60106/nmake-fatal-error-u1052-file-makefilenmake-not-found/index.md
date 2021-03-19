+++
type = "question"
title = "NMAKE : fatal error U1052: file &#x27;Makefile.nmake&#x27; not found"
description = '''i have dowloaded the source code of Wireshark 2.2.5 and setup the environment for the same by following the procedure for building the wireshark. C:&#92;Dhanush&#92;wireshark-2.2.5&amp;gt;Nmake -f Makefile.nmake verify_tools Microsoft (R) Program Maintenance Utility Version 9.00.21022.08 Copyright (C) Microsoft...'''
date = "2017-03-16T04:13:00Z"
lastmod = "2017-03-16T04:26:00Z"
weight = 60106
keywords = [ "makefile.nmake" ]
aliases = [ "/questions/60106" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [NMAKE : fatal error U1052: file 'Makefile.nmake' not found](/questions/60106/nmake-fatal-error-u1052-file-makefilenmake-not-found)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60106-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60106-score" class="post-score" title="current number of votes">0</div><span id="post-60106-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>i have dowloaded the source code of Wireshark 2.2.5 and setup the environment for the same by following the procedure for building the wireshark.</p><p>C:\Dhanush\wireshark-2.2.5&gt;Nmake -f Makefile.nmake verify_tools</p><p>Microsoft (R) Program Maintenance Utility Version 9.00.21022.08 Copyright (C) Microsoft Corporation. All rights reserved.</p><p>NMAKE : fatal error U1052: file 'Makefile.nmake' not found Stop.</p><p>THE ABOVE ERROR was obtained</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-makefile.nmake" rel="tag" title="see questions tagged &#39;makefile.nmake&#39;">makefile.nmake</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Mar '17, 04:13</strong></p><img src="https://secure.gravatar.com/avatar/600778689935688cd4eaaa966e880cae?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DhanuShalz&#39;s gravatar image" /><p><span>DhanuShalz</span><br />
<span class="score" title="36 reputation points">36</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DhanuShalz has one accepted answer">100%</span></p></div></div><div id="comments-container-60106" class="comments-container"></div><div id="comment-tools-60106" class="comment-tools"></div><div class="clear"></div><div id="comment-60106-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60108"></span>

<div id="answer-container-60108" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60108-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60108-score" class="post-score" title="current number of votes">2</div><span id="post-60108-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="DhanuShalz has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You're not following the correct build procedure for 2.2.5 as shown in the <a href="https://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html">Developers Guide Sect 2.2</a>.</p><p>Basically, you need to run CMake to produce a Visual Studio solution and then use msbuild to build that solution. You should follow the steps in the Developers Guide, any deviation is likely to lead to build issues.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Mar '17, 04:26</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-60108" class="comments-container"></div><div id="comment-tools-60108" class="comment-tools"></div><div class="clear"></div><div id="comment-60108-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


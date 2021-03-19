+++
type = "question"
title = "compile dissector in windows?"
description = '''hello, we are would like to make dissector for in-house project. we are planning to use 32bit vc2013 on win7 64 bits after installing all staff from https://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html we are still not able compile anything because glib.h is missing. we are tried to us...'''
date = "2016-02-06T03:59:00Z"
lastmod = "2016-02-07T23:53:00Z"
weight = 49924
keywords = [ "glib", "windows", "dissector", "compile" ]
aliases = [ "/questions/49924" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [compile dissector in windows?](/questions/49924/compile-dissector-in-windows)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49924-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49924-score" class="post-score" title="current number of votes">0</div><span id="post-49924-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hello,</p><p>we are would like to make dissector for in-house project. we are planning to use 32bit vc2013 on win7 64 bits after installing all staff from <a href="https://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html">https://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html</a> we are still not able compile anything because glib.h is missing. we are tried to use glib sources but as we are don't have glibconfig.h we are also can't compile plugin.</p><p>can anyone explain minimal set of libraries and tools to make custom dissector?</p><p>or does anyone have glibconfig.h for glib that could be used in windows environment?</p><p>alex</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-glib" rel="tag" title="see questions tagged &#39;glib&#39;">glib</span> <span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-compile" rel="tag" title="see questions tagged &#39;compile&#39;">compile</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Feb '16, 03:59</strong></p><img src="https://secure.gravatar.com/avatar/fbf20379453a8ca027ddc62687e9e382?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxfox&#39;s gravatar image" /><p><span>maxfox</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxfox has no accepted answers">0%</span></p></div></div><div id="comments-container-49924" class="comments-container"></div><div id="comment-tools-49924" class="comment-tools"></div><div class="clear"></div><div id="comment-49924-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49927"></span>

<div id="answer-container-49927" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49927-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49927-score" class="post-score" title="current number of votes">1</div><span id="post-49927-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You must have missed a step from the Developers Guide, glib.h can be found in the wireshark-win32-libs\gtk2\include\glib-2.0 directory.</p><p>Please post the output of the CMake generation step, editing your question to attach it. You can obtain the output by redirecting to a file, e.g. <code>cmake -G ... 2&gt;&amp;1 &gt; c:\temp\cmake.txt</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Feb '16, 05:09</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-49927" class="comments-container"><span id="49954"></span><div id="comment-49954" class="comment"><div id="post-49954-score" class="comment-score"></div><div class="comment-text"><p>hello,</p><p>yeah, maybe we have been missed something. after repeating all steps from guide and compiling wireshark we found glib.h and glibconfig.h files.</p><p>alex.</p></div><div id="comment-49954-info" class="comment-info"><span class="comment-age">(07 Feb '16, 17:36)</span> <span class="comment-user userinfo">maxfox</span></div></div><span id="49957"></span><div id="comment-49957" class="comment"><div id="post-49957-score" class="comment-score">1</div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-49957-info" class="comment-info"><span class="comment-age">(07 Feb '16, 23:53)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-49927" class="comment-tools"></div><div class="clear"></div><div id="comment-49927-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


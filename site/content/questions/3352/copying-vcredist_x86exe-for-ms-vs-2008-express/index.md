+++
type = "question"
title = "copying vcredist_x86.exe for MS VS 2008 Express"
description = '''Hi, I am facing one error while installing. I am using Visual Studio Express 2008 and getting one error in setup. When i see config.nmake, there is one comment. ELSEIF &quot;$(MSVC_VARIANT)&quot; == &quot;MSVC2005EE&quot; || &quot;$(MSVC_VARIANT)&quot; == &quot;DOTNET20&quot; || &quot;$(MSVC_VARIANT)&quot; == &quot;MSVC2008EE&quot; you need to download the r...'''
date = "2011-04-05T13:08:00Z"
lastmod = "2011-04-05T14:02:00Z"
weight = 3352
keywords = [ "vcredist_x86.exe", "copying" ]
aliases = [ "/questions/3352" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [copying vcredist\_x86.exe for MS VS 2008 Express](/questions/3352/copying-vcredist_x86exe-for-ms-vs-2008-express)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3352-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3352-score" class="post-score" title="current number of votes">0</div><span id="post-3352-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I am facing one error while installing. I am using Visual Studio Express 2008 and getting one error in setup. When i see config.nmake, there is one comment.</p><p>ELSEIF "$(MSVC_VARIANT)" == "MSVC2005EE" || "$(MSVC_VARIANT)" == "DOTNET20" || "$(MSVC_VARIANT)" == "MSVC2008EE"</p><h1 id="you-need-to-download-the-redistributable-package-vcredist_x86.exe-from-microsoft-first">you need to download the redistributable package vcredist_x86.exe from Microsoft first,</h1><h1 id="and-copy-it-to-the-lib-folder">and copy it to the lib folder!!!</h1><p>I have downloaded vcredist.x86.exe but where should it be copied??</p><p>Thanks, Dhanashree</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-vcredist_x86.exe" rel="tag" title="see questions tagged &#39;vcredist_x86.exe&#39;">vcredist_x86.exe</span> <span class="post-tag tag-link-copying" rel="tag" title="see questions tagged &#39;copying&#39;">copying</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Apr '11, 13:08</strong></p><img src="https://secure.gravatar.com/avatar/c33cba1d3fea69f74f6c8c0425c16c75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dsprabhu4&#39;s gravatar image" /><p><span>dsprabhu4</span><br />
<span class="score" title="11 reputation points">11</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dsprabhu4 has no accepted answers">0%</span></p></div></div><div id="comments-container-3352" class="comments-container"></div><div id="comment-tools-3352" class="comment-tools"></div><div class="clear"></div><div id="comment-3352-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3355"></span>

<div id="answer-container-3355" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3355-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3355-score" class="post-score" title="current number of votes">0</div><span id="post-3355-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As suggested in the error message, you need to copy <code>vcredist_x86.exe</code> to the libs folder. This folder is created at the same level as your Wireshark source directory. So, if your Wireshark sources are in <code>C:\\wireshark-1.4.4</code> then the libs folder will be <code>C:\\wireshark-win32-libs-1.4</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Apr '11, 14:02</strong></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p><span>multipleinte...</span><br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="multipleinterfaces has 9 accepted answers">12%</span></p></div></div><div id="comments-container-3355" class="comments-container"></div><div id="comment-tools-3355" class="comment-tools"></div><div class="clear"></div><div id="comment-3355-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


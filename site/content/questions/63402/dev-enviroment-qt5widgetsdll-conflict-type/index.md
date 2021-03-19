+++
type = "question"
title = "Dev enviroment qt5widgets.dll conflict type"
description = '''I am trying to build a wireshark dev environment and I am having trouble with the msbuild step. I want to build a 32-bit version but I get an error that says  &quot;Qt5Widgets.lib(Qt5Widgets.dll): fatal error LNK1112: module machine type &#x27;x64&#x27; conflicts with target machine type &#x27;x86&#x27;&quot; I downloaded the 32...'''
date = "2017-08-04T09:16:00Z"
lastmod = "2017-08-04T10:03:00Z"
weight = 63402
keywords = [ "build_error", "x64", "x86", "qt", "lnk1112" ]
aliases = [ "/questions/63402" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Dev enviroment qt5widgets.dll conflict type](/questions/63402/dev-enviroment-qt5widgetsdll-conflict-type)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63402-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63402-score" class="post-score" title="current number of votes">0</div><span id="post-63402-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to build a wireshark dev environment and I am having trouble with the msbuild step. I want to build a 32-bit version but I get an error that says</p><p>"Qt5Widgets.lib(Qt5Widgets.dll): fatal error LNK1112: module machine type 'x64' conflicts with target machine type 'x86'"</p><p>I downloaded the 32 bit version of qt and I set the QT5_BASE_DIR to the appropriate version. also WIRESHARK_TARGET_PLATFORM=win32 and I am using VS2013 x86 command prompt.</p><p>I had successfully built a 64 bit wireshark version, but now am having trouble building the 32 bit version.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-build_error" rel="tag" title="see questions tagged &#39;build_error&#39;">build_error</span> <span class="post-tag tag-link-x64" rel="tag" title="see questions tagged &#39;x64&#39;">x64</span> <span class="post-tag tag-link-x86" rel="tag" title="see questions tagged &#39;x86&#39;">x86</span> <span class="post-tag tag-link-qt" rel="tag" title="see questions tagged &#39;qt&#39;">qt</span> <span class="post-tag tag-link-lnk1112" rel="tag" title="see questions tagged &#39;lnk1112&#39;">lnk1112</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Aug '17, 09:16</strong></p><img src="https://secure.gravatar.com/avatar/f5b7f4029bc4724fd35867c07f85712b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="allantse&#39;s gravatar image" /><p><span>allantse</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="allantse has one accepted answer">100%</span></p></div></div><div id="comments-container-63402" class="comments-container"><span id="63403"></span><div id="comment-63403" class="comment"><div id="post-63403-score" class="comment-score"></div><div class="comment-text"><p>What version of wireshark ate you building? And which version of CMake are you using?</p></div><div id="comment-63403-info" class="comment-info"><span class="comment-age">(04 Aug '17, 09:24)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="63404"></span><div id="comment-63404" class="comment"><div id="post-63404-score" class="comment-score"></div><div class="comment-text"><p>wireshark version 2.2.7 and cmake 3.5.2 win32</p></div><div id="comment-63404-info" class="comment-info"><span class="comment-age">(04 Aug '17, 09:30)</span> <span class="comment-user userinfo">allantse</span></div></div><span id="63409"></span><div id="comment-63409" class="comment"><div id="post-63409-score" class="comment-score"></div><div class="comment-text"><p>You shouldn't have to set <code>WIRESHARK_TARGET_PLATFORM</code> any more. It was necessary when we were still using Nmake, but the target platform should be determined by the VS environment variables and the CMake generator (<code>-G</code>).</p></div><div id="comment-63409-info" class="comment-info"><span class="comment-age">(04 Aug '17, 10:03)</span> <span class="comment-user userinfo">Gerald Combs ♦♦</span></div></div></div><div id="comment-tools-63402" class="comment-tools"></div><div class="clear"></div><div id="comment-63402-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="63406"></span>

<div id="answer-container-63406" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63406-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63406-score" class="post-score" title="current number of votes">0</div><span id="post-63406-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="allantse has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>ah- I figured it out. I had mistakenly generated the build files earlier while setting the qt5_base_dir to the wrong 64bit version. I had to delete first then regenerate these files with the correct qt5 version.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Aug '17, 09:37</strong></p><img src="https://secure.gravatar.com/avatar/f5b7f4029bc4724fd35867c07f85712b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="allantse&#39;s gravatar image" /><p><span>allantse</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="allantse has one accepted answer">100%</span></p></div></div><div id="comments-container-63406" class="comments-container"><span id="63407"></span><div id="comment-63407" class="comment"><div id="post-63407-score" class="comment-score"></div><div class="comment-text"><p>Please accept your own answer as the correct one, it may help others.</p></div><div id="comment-63407-info" class="comment-info"><span class="comment-age">(04 Aug '17, 09:41)</span> <span class="comment-user userinfo">Anders ♦</span></div></div></div><div id="comment-tools-63406" class="comment-tools"></div><div class="clear"></div><div id="comment-63406-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


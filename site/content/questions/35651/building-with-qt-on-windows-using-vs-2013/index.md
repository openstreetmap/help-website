+++
type = "question"
title = "Building with QT on Windows using VS 2013"
description = '''In reference to an issue discussed on Wireshark-dev submitted June 03, 2014 by Graham Bloice: There are several DLL&#x27;s that are not included when the QT interface is compiled. Other than manually copying these files is there something within the build process that can be modified to get these files t...'''
date = "2014-08-21T11:30:00Z"
lastmod = "2014-08-22T07:51:00Z"
weight = 35651
keywords = [ "qtshark", "qt5" ]
aliases = [ "/questions/35651" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Building with QT on Windows using VS 2013](/questions/35651/building-with-qt-on-windows-using-vs-2013)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35651-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35651-score" class="post-score" title="current number of votes">0</div><span id="post-35651-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In reference to an issue discussed on Wireshark-dev submitted June 03, 2014 by Graham Bloice: There are several DLL's that are not included when the QT interface is compiled. Other than manually copying these files is there something within the build process that can be modified to get these files to include properly. I am not familiar with QT and how it includes its dependencies when creating a deployment package.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-qtshark" rel="tag" title="see questions tagged &#39;qtshark&#39;">qtshark</span> <span class="post-tag tag-link-qt5" rel="tag" title="see questions tagged &#39;qt5&#39;">qt5</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Aug '14, 11:30</strong></p><img src="https://secure.gravatar.com/avatar/77a6292b33bba58628514a3acb4e0646?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="syk0sis6&#39;s gravatar image" /><p><span>syk0sis6</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="syk0sis6 has no accepted answers">0%</span></p></div></div><div id="comments-container-35651" class="comments-container"><span id="35655"></span><div id="comment-35655" class="comment"><div id="post-35655-score" class="comment-score"></div><div class="comment-text"><p>Currently using 1.12.1 (just cloned) and QT 5.3 ... QT version says it can't find libGLESv2.dll after build. The issue on wireshark-dev forum says that there are dlls that are not copied to the release directory: libGLESv2.dll libEGL.dll</p><p>I just can't seem to figure out where to put this in (properly) before creating my deployment package.</p></div><div id="comment-35655-info" class="comment-info"><span class="comment-age">(21 Aug '14, 11:46)</span> <span class="comment-user userinfo">syk0sis6</span></div></div><span id="35656"></span><div id="comment-35656" class="comment"><div id="post-35656-score" class="comment-score"></div><div class="comment-text"><p>All the Qt developments are done in master branch and not in the master-1.12 branch. You should consider switching your branch as Wireshark 1.12.X Qt support will most likely stay as it is today.</p></div><div id="comment-35656-info" class="comment-info"><span class="comment-age">(21 Aug '14, 12:12)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div></div><div id="comment-tools-35651" class="comment-tools"></div><div class="clear"></div><div id="comment-35651-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35652"></span>

<div id="answer-container-35652" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35652-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35652-score" class="post-score" title="current number of votes">0</div><span id="post-35652-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="syk0sis6 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Current master branch should copy all the required Dlls when compiling with Qt 5.3 or later. Which version of Wireshark and Qt are you using?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Aug '14, 11:34</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-35652" class="comments-container"><span id="35653"></span><div id="comment-35653" class="comment"><div id="post-35653-score" class="comment-score"></div><div class="comment-text"><p>Currently using 1.12.1 (just cloned) and QT 5.3 ... QT version says it can't find libGLESv2.dll after build. The issue on wireshark-dev forum says that there are dlls that are not copied to the release directory: libGLESv2.dll libEGL.dll</p><p>I just can't seem to figure out where to put this in (properly) before creating my deployment package.</p></div><div id="comment-35653-info" class="comment-info"><span class="comment-age">(21 Aug '14, 11:40)</span> <span class="comment-user userinfo">syk0sis6</span></div></div><span id="35662"></span><div id="comment-35662" class="comment"><div id="post-35662-score" class="comment-score"></div><div class="comment-text"><p>You should switch to the master branch. I'm not sure if the fixes for QT builds have been backported to the 1.12.x branches.</p></div><div id="comment-35662-info" class="comment-info"><span class="comment-age">(21 Aug '14, 14:33)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="35674"></span><div id="comment-35674" class="comment"><div id="post-35674-score" class="comment-score"></div><div class="comment-text"><p>Thanks guys.. worked with current master .... QT works ... Unfortunately have to track down why the GTK version doesn't..</p></div><div id="comment-35674-info" class="comment-info"><span class="comment-age">(22 Aug '14, 07:51)</span> <span class="comment-user userinfo">syk0sis6</span></div></div></div><div id="comment-tools-35652" class="comment-tools"></div><div class="clear"></div><div id="comment-35652-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


+++
type = "question"
title = "Use of Visual Studio Community 2015"
description = '''I am interested in contributing to the Wireshark effort. For this the development guide mentions that I use Visual Studio Community 2013. Can I use Visual Studio Community 2015 instead, as it has better features and can be used for multiple projects. I will be using it to contribute for V2.0'''
date = "2016-07-15T22:21:00Z"
lastmod = "2016-07-16T07:33:00Z"
weight = 54091
keywords = [ "visual-studio" ]
aliases = [ "/questions/54091" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Use of Visual Studio Community 2015](/questions/54091/use-of-visual-studio-community-2015)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54091-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54091-score" class="post-score" title="current number of votes">0</div><span id="post-54091-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am interested in contributing to the Wireshark effort.</p><p>For this the development guide mentions that I use Visual Studio Community 2013. Can I use Visual Studio Community 2015 instead, as it has better features and can be used for multiple projects.</p><p>I will be using it to contribute for V2.0</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-visual-studio" rel="tag" title="see questions tagged &#39;visual-studio&#39;">visual-studio</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jul '16, 22:21</strong></p><img src="https://secure.gravatar.com/avatar/977ef806acda5d7ef202cb07ab20be61?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rishiraje&#39;s gravatar image" /><p><span>rishiraje</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rishiraje has no accepted answers">0%</span></p></div></div><div id="comments-container-54091" class="comments-container"></div><div id="comment-tools-54091" class="comment-tools"></div><div class="clear"></div><div id="comment-54091-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="54092"></span>

<div id="answer-container-54092" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54092-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54092-score" class="post-score" title="current number of votes">0</div><span id="post-54092-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The master branch (used to compile Wireshark 2.1.x development releases and that will become soon Wireshark 2.2.0 stable release) can be used with MSVC 2015 CE. I don't think we did all the changes required for this MSVC version in master-2.0 branch (used for Wireshark 2.0.x). Anyway for contributing to Wireshark you should use master branch (the stable branch only gets bugfixes).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Jul '16, 01:00</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-54092" class="comments-container"></div><div id="comment-tools-54092" class="comment-tools"></div><div class="clear"></div><div id="comment-54092-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="54094"></span>

<div id="answer-container-54094" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54094-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54094-score" class="post-score" title="current number of votes">0</div><span id="post-54094-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As the current buildbot, releases and Development Guide all use VS2013, unless you want to debug any remaining issues in VS2015 compatibility, then it would be best to start with VS2013.</p><p>Experience of helping other users setup their Windows build environment has shown that deviating in any way from the instructions in the Developers Guide leads to issues and frustration. Start with VS2013, once you have confidence in that, then move over to VS2015. Apart from the different Qt versions required, the only other change is in the environment setup for your build shell and the CMake generation step. You can have both versions of VS installed at the same time.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Jul '16, 04:07</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-54094" class="comments-container"><span id="54097"></span><div id="comment-54097" class="comment"><div id="post-54097-score" class="comment-score"></div><div class="comment-text"><p>Thanks. I will start with VS2013</p></div><div id="comment-54097-info" class="comment-info"><span class="comment-age">(16 Jul '16, 07:33)</span> <span class="comment-user userinfo">rishiraje</span></div></div></div><div id="comment-tools-54094" class="comment-tools"></div><div class="clear"></div><div id="comment-54094-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


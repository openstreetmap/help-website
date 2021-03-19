+++
type = "question"
title = "1.12.x release missing Visual Studio .sln files"
description = '''Although not necessary for building, the helpful .sln files that came with the source of 1.10.x and prior version are missing. I&#x27;m curious as to the reasons for this decision. Why have they been removed?'''
date = "2014-08-11T10:48:00Z"
lastmod = "2014-08-11T13:32:00Z"
weight = 35417
keywords = [ "visual", "studio" ]
aliases = [ "/questions/35417" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [1.12.x release missing Visual Studio .sln files](/questions/35417/112x-release-missing-visual-studio-sln-files)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35417-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35417-score" class="post-score" title="current number of votes">0</div><span id="post-35417-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Although not necessary for building, the helpful .sln files that came with the source of 1.10.x and prior version are missing. I'm curious as to the reasons for this decision. Why have they been removed?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-visual" rel="tag" title="see questions tagged &#39;visual&#39;">visual</span> <span class="post-tag tag-link-studio" rel="tag" title="see questions tagged &#39;studio&#39;">studio</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Aug '14, 10:48</strong></p><img src="https://secure.gravatar.com/avatar/0b4ddeb095ff16e8a84fe92d03bbdef4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tlann&#39;s gravatar image" /><p><span>tlann</span><br />
<span class="score" title="76 reputation points">76</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tlann has 4 accepted answers">100%</span></p></div></div><div id="comments-container-35417" class="comments-container"></div><div id="comment-tools-35417" class="comment-tools"></div><div class="clear"></div><div id="comment-35417-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35418"></span>

<div id="answer-container-35418" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35418-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35418-score" class="post-score" title="current number of votes">1</div><span id="post-35418-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="tlann has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hi,</p><p>They were removed because they were obsolete, unmaintained and confusing some people who thought that Wireshark could be built from them while it was not the case.</p><p>You can still load the executable (from the wireshark-gtk2 folder) in case you want to use the debugger integrated in the IDE.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Aug '14, 11:11</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-35418" class="comments-container"><span id="35419"></span><div id="comment-35419" class="comment"><div id="post-35419-score" class="comment-score"></div><div class="comment-text"><p>I can see how they became obsolete with a lot of the new Qt changes. But I would like to point out that the .slns were helpful with building and troubleshooting plugins. It was nice to choose run from the IDE and have the plugins built and troubleshoot right there.</p></div><div id="comment-35419-info" class="comment-info"><span class="comment-age">(11 Aug '14, 11:15)</span> <span class="comment-user userinfo">tlann</span></div></div><span id="35420"></span><div id="comment-35420" class="comment"><div id="post-35420-score" class="comment-score">1</div><div class="comment-text"><p>Once we get it working properly, CMake will be able to produce .sln files for any installed version of Visual Studio.</p></div><div id="comment-35420-info" class="comment-info"><span class="comment-age">(11 Aug '14, 13:05)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="35421"></span><div id="comment-35421" class="comment"><div id="post-35421-score" class="comment-score"></div><div class="comment-text"><p>Thank you. That is good to know.</p></div><div id="comment-35421-info" class="comment-info"><span class="comment-age">(11 Aug '14, 13:32)</span> <span class="comment-user userinfo">tlann</span></div></div></div><div id="comment-tools-35418" class="comment-tools"></div><div class="clear"></div><div id="comment-35418-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


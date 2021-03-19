+++
type = "question"
title = "How can I find the latest Wireshark development build that built on all platforms?"
description = '''Hi! I have installed the Wireshark sources and built a working executable under Windows Vista SP2. I occasionally update the sources using TortoiseSVN to a more recent revision (after checking the Wireshark Recent Builds Summary Page). Lately, there have been many failures (it seems there is at leas...'''
date = "2011-01-26T16:10:00Z"
lastmod = "2012-09-04T01:41:00Z"
weight = 1961
keywords = [ "wireshark", "build", "revision" ]
aliases = [ "/questions/1961" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How can I find the latest Wireshark development build that built on all platforms?](/questions/1961/how-can-i-find-the-latest-wireshark-development-build-that-built-on-all-platforms)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1961-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi!</p><p>I have installed the Wireshark sources and built a working executable under Windows Vista SP2. I occasionally update the sources using TortoiseSVN to a more recent revision (after checking the <a href="http://buildbot.wireshark.org/trunk/one_line_per_build">Wireshark Recent Builds Summary Page</a>). Lately, there have been many failures (it seems there is at least one failure on <em>some</em> platform for every revision).</p><p>I'm currently using revision 34673 and I was wondering if there was a location/link where I could quickly find the last revision that built successfully on all platforms. Would it be possible to add this piece of information to the <a href="http://buildbot.wireshark.org/trunk/">Wireshark Buildbot Welcome Page</a> and have it automatically updated? If not, is there an easy/quick way to get this (without just brute force searching through the build results until I find a revision with all six platforms succeeding)?</p><p>Thanks in advance! Jim</p></div><div id="question-tags" class="tags-container tags">wireshark build revision</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jan '11, 16:10</strong></p><img src="https://secure.gravatar.com/avatar/ce5520d8101de9c9b56dce564b8cbf10?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jim_demarco&#39;s gravatar image" /><p>jim_demarco<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jim_demarco has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 30 Jan '11, 11:04</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-1961" class="comments-container"><span id="1963"></span><div id="comment-1963" class="comment"><div id="post-1963-score" class="comment-score"></div><div class="comment-text"><p>What do you mean by "good" here?</p><p>If you mean "stable and reliable", we make no claim that any of the buildbot builds are "good" - if you want a stable and reliable build, stick with the stable releases (currently 1.2.x and 1.4.x). If you're willing to sacrifice some stability and reliability for Shiny New Features, but don't want to live on the bleeding edge, try one of the trunk development releases (currently 1.5.x).</p></div><div id="comment-1963-info" class="comment-info"><span class="comment-age">(26 Jan '11, 18:27)</span> Guy Harris ♦♦</div></div><span id="2021"></span><div id="comment-2021" class="comment"><div id="post-2021-score" class="comment-score"></div><div class="comment-text"><p>Hi Guy!</p><p>By "good", I only mean "builds successfully on all platforms". I know that a successful build doesn't imply a working build, but it's one less hurdle to deal with.</p></div><div id="comment-2021-info" class="comment-info"><span class="comment-age">(30 Jan '11, 07:11)</span> jim_demarco</div></div></div><div id="comment-tools-1961" class="comment-tools"></div><div class="clear"></div><div id="comment-1961-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="2022"></span>

<div id="answer-container-2022" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2022-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>There's no mechanism for that.</p><p>Note that</p><ol><li>the failure of a build might merely be due to, for example, a deprecated API being used, or other "code cleanliness" problems - this may or may not cause problems if you're trying to use it;</li><li>the failure of a build on one platform may, or may not, reflect a problem on another platform, so if, for example, you're only using Windows, a build failure on one of the UN*Xes might not matter, and if you're only using Windows and Linux, a build failure on OS X or Solaris might not matter.</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jan '11, 11:08</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-2022" class="comments-container"><span id="2024"></span><div id="comment-2024" class="comment"><div id="post-2024-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the answer ("No") and the explanatory notes.</p><p>My intent was to <em>easily</em> find a recent "good" (see my definition) revision to use to minimize the likelihood of problems in bleeding-edge code. I don't update my sources very often and was trying to come up with a reasonable strategy for when to do so (that is, update the sources more frequently than when a stable release comes out).</p></div><div id="comment-2024-info" class="comment-info"><span class="comment-age">(30 Jan '11, 16:33)</span> jim_demarco</div></div></div><div id="comment-tools-2022" class="comment-tools"></div><div class="clear"></div><div id="comment-2022-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="14014"></span>

<div id="answer-container-14014" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14014-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You may not be able to get the executable of exact reversion, But if it is in latest revision not dropped due to critical bugs or something then you can always pick up latest development executable's <a href="http://www.wireshark.org/download/automated/win32">http://www.wireshark.org/download/automated/win32</a>.</p><p>Go to parent directory and find relevant binary for other platforms.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Sep '12, 01:41</strong></p><img src="https://secure.gravatar.com/avatar/0cf7e05b14ad6662ecde4c327bb2c39f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Harsha&#39;s gravatar image" /><p>Harsha<br />
<span class="score" title="46 reputation points">46</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Harsha has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 Sep '12, 01:41</p></div></div><div id="comments-container-14014" class="comments-container"></div><div id="comment-tools-14014" class="comment-tools"></div><div class="clear"></div><div id="comment-14014-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


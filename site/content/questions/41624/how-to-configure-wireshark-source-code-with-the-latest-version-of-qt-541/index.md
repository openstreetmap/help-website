+++
type = "question"
title = "How to configure wireshark source code with the latest version of qt 5.4.1?"
description = '''Is wireshark&#x27;s latest version compaitable with QT 5.4.1 and how can we configure that code in qt?'''
date = "2015-04-21T05:04:00Z"
lastmod = "2015-04-22T20:15:00Z"
weight = 41624
keywords = [ "code", "qt5", "wireshark" ]
aliases = [ "/questions/41624" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to configure wireshark source code with the latest version of qt 5.4.1?](/questions/41624/how-to-configure-wireshark-source-code-with-the-latest-version-of-qt-541)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41624-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41624-score" class="post-score" title="current number of votes">0</div><span id="post-41624-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is wireshark's latest version compaitable with QT 5.4.1 and how can we configure that code in qt?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-code" rel="tag" title="see questions tagged &#39;code&#39;">code</span> <span class="post-tag tag-link-qt5" rel="tag" title="see questions tagged &#39;qt5&#39;">qt5</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Apr '15, 05:04</strong></p><img src="https://secure.gravatar.com/avatar/8efce51fbbf3dbd6c9b9132056f45eb5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ankit&#39;s gravatar image" /><p><span>ankit</span><br />
<span class="score" title="65 reputation points">65</span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ankit has one accepted answer">25%</span></p></div></div><div id="comments-container-41624" class="comments-container"></div><div id="comment-tools-41624" class="comment-tools"></div><div class="clear"></div><div id="comment-41624-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41625"></span>

<div id="answer-container-41625" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41625-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41625-score" class="post-score" title="current number of votes">0</div><span id="post-41625-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>In my build environment I'm compiling Wireshark master branch with Qt 5.4.1 on Windows without any issue. Then the way to "configure" depends on your platform and build environment. For Windows, you need to set a QT5_BASE_DIR environment variable with the Qt 5.4.1 installation path.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Apr '15, 05:30</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-41625" class="comments-container"><span id="41628"></span><div id="comment-41628" class="comment"><div id="post-41628-score" class="comment-score"></div><div class="comment-text"><p>As detailed in the Wireshark Developers Guide, sect. <a href="https://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html#ChSetupPrepareCommandCom">2.2.9</a></p><p>For OS's other than Windows, it depends on what configure mechanism you use, either autotools or CMake.</p></div><div id="comment-41628-info" class="comment-info"><span class="comment-age">(21 Apr '15, 06:11)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="41654"></span><div id="comment-41654" class="comment"><div id="post-41654-score" class="comment-score"></div><div class="comment-text"><p>I also want to setup this build environment in windows. I just want to ask that before running .pro file in qt is there any prerequisites that we have to install some tools or some files additionally?</p></div><div id="comment-41654-info" class="comment-info"><span class="comment-age">(21 Apr '15, 20:32)</span> <span class="comment-user userinfo">ankit</span></div></div><span id="41660"></span><div id="comment-41660" class="comment"><div id="post-41660-score" class="comment-score"></div><div class="comment-text"><p>Why are you running the .pro file?</p><p>The supported methods to build Wireshark, including the prequisites and setup, are detailed in the <a href="https://www.wireshark.org/docs/wsdg_html_chunked/">Developers Guide</a>.</p></div><div id="comment-41660-info" class="comment-info"><span class="comment-age">(22 Apr '15, 01:55)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="41712"></span><div id="comment-41712" class="comment"><div id="post-41712-score" class="comment-score"></div><div class="comment-text"><p>ok, got your point grahamb, thanks for suggesting</p></div><div id="comment-41712-info" class="comment-info"><span class="comment-age">(22 Apr '15, 20:15)</span> <span class="comment-user userinfo">ankit</span></div></div></div><div id="comment-tools-41625" class="comment-tools"></div><div class="clear"></div><div id="comment-41625-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


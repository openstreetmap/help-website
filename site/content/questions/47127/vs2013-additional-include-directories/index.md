+++
type = "question"
title = "VS2013 Additional Include Directories"
description = '''Although this isn&#x27;t really a Wireshark issue, I thought someone on here may have already figured this out. I am setting up a Visual Studio 2013 Community Edition project to build and debug Wireshark. The Wireshark source has a complex directory structure, and the include files are spread across dire...'''
date = "2015-11-01T01:30:00Z"
lastmod = "2015-11-01T06:55:00Z"
weight = 47127
keywords = [ "visual-studio" ]
aliases = [ "/questions/47127" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [VS2013 Additional Include Directories](/questions/47127/vs2013-additional-include-directories)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47127-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47127-score" class="post-score" title="current number of votes">0</div><span id="post-47127-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Although this isn't really a Wireshark issue, I thought someone on here may have already figured this out.</p><p>I am setting up a Visual Studio 2013 Community Edition project to build and debug Wireshark. The Wireshark source has a complex directory structure, and the include files are spread across directories, subdirectories and subsubdirectories.</p><p>In many places in the source there are includes like this:</p><pre><code>#include &lt;ui_main_window.h&gt;</code></pre><p>My C knowledge is rusty but I understand that the angle brackets mean that it's for the compile tool (in this case VS2013) to resolve this reference to an absolute location. I get loads of errors showing that many of these references can't be resolved. I can add directories in the "Additional Include Directories" field of the Project Properties and this fixes the references.</p><p>Now to the question. Do I need to add every include directory individually? Can I get VS to automatically descend down through the directory structure? I tried using a wild card (C:\Development\wireshark*) but this doesn't work.</p><p>Thanks and regards...Paul</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-visual-studio" rel="tag" title="see questions tagged &#39;visual-studio&#39;">visual-studio</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Nov '15, 01:30</strong></p><img src="https://secure.gravatar.com/avatar/2e1b4057f2ff59fe059b23cc6571abaf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PaulOfford&#39;s gravatar image" /><p><span>PaulOfford</span><br />
<span class="score" title="131 reputation points">131</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="32 badges"><span class="silver">●</span><span class="badgecount">32</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PaulOfford has 5 accepted answers">11%</span></p></div></div><div id="comments-container-47127" class="comments-container"></div><div id="comment-tools-47127" class="comment-tools"></div><div class="clear"></div><div id="comment-47127-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47133"></span>

<div id="answer-container-47133" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47133-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47133-score" class="post-score" title="current number of votes">2</div><span id="post-47133-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="PaulOfford has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>No need to create your own project, which has been tried in the past and is very difficult to maintain.</p><p>For Wireshark 2.0, the recommended build system on Windows uses CMake not nmake. CMake can generate Visual Studio solution files, or nmake makefiles if you wish to live in the past. All the 2.0 (and 1.99) releases have been built with CMake.</p><p>See README.cmake in the top level of the source files for more info.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Nov '15, 06:55</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>01 Nov '15, 13:33</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-47133" class="comments-container"></div><div id="comment-tools-47133" class="comment-tools"></div><div class="clear"></div><div id="comment-47133-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


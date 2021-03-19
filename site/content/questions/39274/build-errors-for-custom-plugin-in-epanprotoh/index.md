+++
type = "question"
title = "Build Errors for Custom Plugin in epan&#92;proto.h"
description = '''I&#x27;m trying to add a custom plugin to a Wireshark built from source for Windows. The plugin has previously been successfully added to a Wireshark built from source for Linux, and the code has not been changed. I&#x27;ve gotten Wireshark to build successfully from source without adding the plugin, and have...'''
date = "2015-01-19T06:49:00Z"
lastmod = "2015-01-19T09:03:00Z"
weight = 39274
keywords = [ "windows", "custom", "plugins", "epan", "wireshark" ]
aliases = [ "/questions/39274" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Build Errors for Custom Plugin in epan\\proto.h](/questions/39274/build-errors-for-custom-plugin-in-epanprotoh)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39274-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39274-score" class="post-score" title="current number of votes">0</div><span id="post-39274-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to add a custom plugin to a Wireshark built from source for Windows. The plugin has previously been successfully added to a Wireshark built from source for Linux, and the code has not been changed. I've gotten Wireshark to build successfully from source without adding the plugin, and have built it successfully with the plugin in the plugins folder but without any of the changes to add it as an extension.</p><p>When I change the custom.example files as directed in the README.plugins file, I immediately run into build errors. There are hundreds of compilation errors not in any of the source files, but in wireshark\epan\proto.h. They're all of the syntax error type, things like missing parenthesis and nonstandard extensions used. The plugin files compiled successfully for linux--why would they not work here? And why would the errors show up in epan\proto.h?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-custom" rel="tag" title="see questions tagged &#39;custom&#39;">custom</span> <span class="post-tag tag-link-plugins" rel="tag" title="see questions tagged &#39;plugins&#39;">plugins</span> <span class="post-tag tag-link-epan" rel="tag" title="see questions tagged &#39;epan&#39;">epan</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Jan '15, 06:49</strong></p><img src="https://secure.gravatar.com/avatar/8151306827aa578935b52f99a49cbde2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mehubb985&#39;s gravatar image" /><p><span>mehubb985</span><br />
<span class="score" title="11 reputation points">11</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mehubb985 has no accepted answers">0%</span></p></div></div><div id="comments-container-39274" class="comments-container"></div><div id="comment-tools-39274" class="comment-tools"></div><div class="clear"></div><div id="comment-39274-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39278"></span>

<div id="answer-container-39278" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39278-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39278-score" class="post-score" title="current number of votes">0</div><span id="post-39278-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It's possible the plugin includes header files only found on Linux, or includes something that then breaks subsequent includes, e.g. proto.h.</p><p>Redirect the build output to a file, e.g. <code>nmake -f makefile.nmake &gt; test.txt 2&gt;&amp;1</code> and look at the first errors found, you can post it here as a comment.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jan '15, 09:03</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-39278" class="comments-container"></div><div id="comment-tools-39278" class="comment-tools"></div><div class="clear"></div><div id="comment-39278-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


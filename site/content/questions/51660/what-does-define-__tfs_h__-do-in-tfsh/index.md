+++
type = "question"
title = "What does #define __TFS_H__ do in tfs.h?"
description = '''Hi all, due to some problems I&#x27;ve had with compiling a plugin I stumbled upon __TFS_H__ in tfs.h while tracing the error. What does it do and what happens if I do something like this TFS(&amp;amp;tfs_set_notset) somewhere else in the code? Thanks. Mike'''
date = "2016-04-14T01:05:00Z"
lastmod = "2016-04-14T03:11:00Z"
weight = 51660
keywords = [ "function", "source-code", "understanding" ]
aliases = [ "/questions/51660" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [What does \#define \_\_TFS\_H\_\_ do in tfs.h?](/questions/51660/what-does-define-__tfs_h__-do-in-tfsh)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51660-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51660-score" class="post-score" title="current number of votes">0</div><span id="post-51660-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all, due to some problems I've had with compiling a plugin I stumbled upon <code>__TFS_H__</code> in tfs.h while tracing the error. What does it do and what happens if I do something like this <code>TFS(&amp;tfs_set_notset)</code> somewhere else in the code?</p><p>Thanks. Mike</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-function" rel="tag" title="see questions tagged &#39;function&#39;">function</span> <span class="post-tag tag-link-source-code" rel="tag" title="see questions tagged &#39;source-code&#39;">source-code</span> <span class="post-tag tag-link-understanding" rel="tag" title="see questions tagged &#39;understanding&#39;">understanding</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Apr '16, 01:05</strong></p><img src="https://secure.gravatar.com/avatar/c288ec16e3d47bc1e1602e5b4e283949?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mikethebo&#39;s gravatar image" /><p><span>mikethebo</span><br />
<span class="score" title="21 reputation points">21</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mikethebo has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 Apr '16, 01:06</strong> </span></p></div></div><div id="comments-container-51660" class="comments-container"></div><div id="comment-tools-51660" class="comment-tools"></div><div class="clear"></div><div id="comment-51660-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51662"></span>

<div id="answer-container-51662" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51662-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51662-score" class="post-score" title="current number of votes">1</div><span id="post-51662-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="mikethebo has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>What does it do</p></blockquote><p>It makes sure that, if a Wireshark source file includes both <code>tfs.h</code> and some other header file that includes <code>tfs.h</code>, the header file's contents are processed only once, so you don't, for example, get warnings or errors from redefinitions or redeclaration.</p><p>This is a <strong><em>VERY</em></strong> common technique in C header files; you'll probably find at least one header file for the OS or compiler you're using that has a "<a href="https://en.wikipedia.org/wiki/Include_guard">header guard</a>" of that type.</p><blockquote><p>what happens if I do something like this <code>TFS(&amp;tfs_set_notset)</code> somewhere else in the code?</p></blockquote><p>It works, if you do that in the right place (a definition of a named packet field) and if you've included either <code>tfs.h</code> or some header file that includes <code>tfs.h</code> before you use <code>TFS(&amp;tfs_set_notset)</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Apr '16, 01:54</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-51662" class="comments-container"><span id="51663"></span><div id="comment-51663" class="comment"><div id="post-51663-score" class="comment-score"></div><div class="comment-text"><p>Although as noted <a href="https://ask.wireshark.org/questions/51625/how-to-solve-error-c2099-and-lnk2019-when-building-dissector-plugin-on-windows-7-64bit">elsewhere</a>, on Windows, there appear to be issues including pre-defined tfs values from libwireshark in a plugin.</p></div><div id="comment-51663-info" class="comment-info"><span class="comment-age">(14 Apr '16, 02:12)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="51666"></span><div id="comment-51666" class="comment"><div id="post-51666-score" class="comment-score">1</div><div class="comment-text"><p>From <code>proto.h</code></p><pre><code>/** Make a const true_false_string[] look like a _true_false_string pointer, used to set header_field_info.strings */
#define TFS(x)  (const struct true_false_string*)(x)</code></pre><p>The declarations in tfs.h are just handy, pre-canned true_false strings, which, on Windows, can't unfortunately be use in plugins. You can just define those strings yourself (as in tfs.c) if you need any of them.</p></div><div id="comment-51666-info" class="comment-info"><span class="comment-age">(14 Apr '16, 03:11)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-51662" class="comment-tools"></div><div class="clear"></div><div id="comment-51662-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


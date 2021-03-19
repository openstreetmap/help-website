+++
type = "question"
title = "&#x27;--disable-glibtest&#x27; not working"
description = '''Trying to run configure without having to test for gtk and glib like so: ./configure --enable-wireshark=no --disable-glibtest  But at one point in the log it&#x27;ll give me this and fail:  checking for GLIB - version &amp;gt;= 2.4.0... no  Could not run GLIB test program, checking why...  Could not run GLIB...'''
date = "2011-04-05T15:53:00Z"
lastmod = "2011-04-25T10:38:00Z"
weight = 3360
keywords = [ "glib", "test", "disable" ]
aliases = [ "/questions/3360" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# ['--disable-glibtest' not working](/questions/3360/-disable-glibtest-not-working)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3360-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3360-score" class="post-score" title="current number of votes">0</div><span id="post-3360-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Trying to run configure without having to test for gtk and glib like so:</p><pre><code>./configure --enable-wireshark=no --disable-glibtest</code></pre><p>But at one point in the log it'll give me this and fail:</p><blockquote><p>checking for GLIB - version &gt;= 2.4.0... no <strong><em>Could not run GLIB test program, checking why...</em></strong> Could not run GLIB test program, checking why... <strong><em>The test program failed to compile or link. See the file config.log for the</em></strong> exact error that occured. This usually means GLIB is incorrectly installed. configure: error: GLib 2.4 or later distribution not found.</p></blockquote><p>I may just be confusing what these options actually do. But by the looks of the message it shouldn't be trying to run a test program.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-glib" rel="tag" title="see questions tagged &#39;glib&#39;">glib</span> <span class="post-tag tag-link-test" rel="tag" title="see questions tagged &#39;test&#39;">test</span> <span class="post-tag tag-link-disable" rel="tag" title="see questions tagged &#39;disable&#39;">disable</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Apr '11, 15:53</strong></p><img src="https://secure.gravatar.com/avatar/e38821ea7ed026bbdf8032a0fdc64d6d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tokolosh&#39;s gravatar image" /><p><span>Tokolosh</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tokolosh has no accepted answers">0%</span></p></div></div><div id="comments-container-3360" class="comments-container"></div><div id="comment-tools-3360" class="comment-tools"></div><div class="clear"></div><div id="comment-3360-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="3388"></span>

<div id="answer-container-3388" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3388-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3388-score" class="post-score" title="current number of votes">0</div><span id="post-3388-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There is very likely a bug in <code>configure.in</code> or possibly in <code>aclocal-fallback/glib-2.0.m4</code>. Please file a bug report for this <a href="https://bugs.wireshark.org/bugzilla/">here</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Apr '11, 08:08</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-3388" class="comments-container"></div><div id="comment-tools-3388" class="comment-tools"></div><div class="clear"></div><div id="comment-3388-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="3707"></span>

<div id="answer-container-3707" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3707-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3707-score" class="post-score" title="current number of votes">0</div><span id="post-3707-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>try with --enable-glibtest=no instead of --disable-glibtest</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Apr '11, 10:38</strong></p><img src="https://secure.gravatar.com/avatar/0e1cb7363a97f9b6771e2bd6abcd6274?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yoshac&#39;s gravatar image" /><p><span>yoshac</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yoshac has no accepted answers">0%</span></p></div></div><div id="comments-container-3707" class="comments-container"></div><div id="comment-tools-3707" class="comment-tools"></div><div class="clear"></div><div id="comment-3707-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


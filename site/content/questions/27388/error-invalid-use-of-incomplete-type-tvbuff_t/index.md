+++
type = "question"
title = "error: invalid use of incomplete type &#x27;tvbuff_t"
description = '''I&#x27;m trying to build an old dissector with the new wireshark source and I&#x27;m facing this compilation problem and am not able to resolve it.  More log: packet-xxx.cpp:467:7: error: invalid use of incomplete type &#x27;tvbuff_t {aka struct tvbuff}&#x27; In file included from ../../epan/proto.h:51:0,  from ../../e...'''
date = "2013-11-26T02:05:00Z"
lastmod = "2013-11-27T01:51:00Z"
weight = 27388
keywords = [ "make", "makefile", "build", "plugin" ]
aliases = [ "/questions/27388" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [error: invalid use of incomplete type 'tvbuff\_t](/questions/27388/error-invalid-use-of-incomplete-type-tvbuff_t)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27388-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27388-score" class="post-score" title="current number of votes">0</div><span id="post-27388-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to build an old dissector with the new wireshark source and I'm facing this compilation problem and am not able to resolve it.</p><p>More log: packet-xxx.cpp:467:7: error: invalid use of incomplete type 'tvbuff_t {aka struct tvbuff}' In file included from ../../epan/proto.h:51:0, from ../../epan/packet.h:29, from packet-xxx.cpp:51: ../../epan/tvbuff.h:64:8: error: forward declaration of 'tvbuff_t {aka struct tvbuff}' make: *** [packet-xxx.lo] Error 1</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-make" rel="tag" title="see questions tagged &#39;make&#39;">make</span> <span class="post-tag tag-link-makefile" rel="tag" title="see questions tagged &#39;makefile&#39;">makefile</span> <span class="post-tag tag-link-build" rel="tag" title="see questions tagged &#39;build&#39;">build</span> <span class="post-tag tag-link-plugin" rel="tag" title="see questions tagged &#39;plugin&#39;">plugin</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Nov '13, 02:05</strong></p><img src="https://secure.gravatar.com/avatar/0a3500d83a034d54be7470d7ed010604?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pysudhir&#39;s gravatar image" /><p><span>pysudhir</span><br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pysudhir has no accepted answers">0%</span></p></div></div><div id="comments-container-27388" class="comments-container"><span id="27409"></span><div id="comment-27409" class="comment"><div id="post-27409-score" class="comment-score"></div><div class="comment-text"><p>Are you building a C++ dissector? Not sure that will work.</p></div><div id="comment-27409-info" class="comment-info"><span class="comment-age">(26 Nov '13, 04:01)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="27462"></span><div id="comment-27462" class="comment"><div id="post-27462-score" class="comment-score"></div><div class="comment-text"><p>That is exactly the problem. Could you point me out to the changes in the configure.ac file that are needed to compile a c++ dissecotr?</p></div><div id="comment-27462-info" class="comment-info"><span class="comment-age">(26 Nov '13, 22:36)</span> <span class="comment-user userinfo">pysudhir</span></div></div><span id="27467"></span><div id="comment-27467" class="comment"><div id="post-27467-score" class="comment-score"></div><div class="comment-text"><p>Why not go with the flow and write it in C? That also makes it possible to contribute the code.</p></div><div id="comment-27467-info" class="comment-info"><span class="comment-age">(27 Nov '13, 00:24)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="27474"></span><div id="comment-27474" class="comment"><div id="post-27474-score" class="comment-score"></div><div class="comment-text"><p><span>@pysudhir</span></p><p>As suggested by <span>@Anders</span> comment, there aren't any C++ dissectors in the mainline Wireshark source code.</p><p>External additions to the project (plugins) have used C++, <a href="http://wsgd.free.fr/">WSGD</a> comes to mind, so maybe look at that.</p></div><div id="comment-27474-info" class="comment-info"><span class="comment-age">(27 Nov '13, 01:51)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-27388" class="comment-tools"></div><div class="clear"></div><div id="comment-27388-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27423"></span>

<div id="answer-container-27423" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27423-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27423-score" class="post-score" title="current number of votes">0</div><span id="post-27423-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The problem is that the <code>tvbuff_t</code> structure has been made opaque. That means you cannot do anything with the structure other than store pointers to it and pass them around. That means you can't access, for example, <code>tvb-&gt;length</code>. Rather, you must use accessor functions (e.g., <code>tvb_length()</code>).</p><p>(The reason the structure is opaque is exactly to ensure that it is only accessed via the accessor functions.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Nov '13, 06:26</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-27423" class="comments-container"></div><div id="comment-tools-27423" class="comment-tools"></div><div class="clear"></div><div id="comment-27423-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


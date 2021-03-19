+++
type = "question"
title = "How can I fix this Glib-ERROR?"
description = '''Using an unmodified verion of wireshark 1.4.9 that I build from source I am getting the following error when I attempt to load a capture file with a proprietary protocol: Glib-ERROR **:gmem.c:176: failed to allocate 2516584916 bytes aborting After this I get a MSVC error and wireshark closes. I get ...'''
date = "2011-10-19T09:04:00Z"
lastmod = "2011-10-19T10:09:00Z"
weight = 6987
keywords = [ "glib", "gmem", "error" ]
aliases = [ "/questions/6987" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How can I fix this Glib-ERROR?](/questions/6987/how-can-i-fix-this-glib-error)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6987-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6987-score" class="post-score" title="current number of votes">0</div><span id="post-6987-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Using an unmodified verion of wireshark 1.4.9 that I build from source I am getting the following error when I attempt to load a capture file with a proprietary protocol:</p><p><code>Glib-ERROR **:gmem.c:176: failed to allocate 2516584916 bytes aborting</code></p><p>After this I get a MSVC error and wireshark closes.</p><p>I get the same error when I run the same version of wireshark with a custom plug-in to decode the proprietary protocol.</p><p>Any pointers on possible causes or where to begin troubleshooting?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-glib" rel="tag" title="see questions tagged &#39;glib&#39;">glib</span> <span class="post-tag tag-link-gmem" rel="tag" title="see questions tagged &#39;gmem&#39;">gmem</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Oct '11, 09:04</strong></p><img src="https://secure.gravatar.com/avatar/15553454dfe2d95883f27714ebc070a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lanb&#39;s gravatar image" /><p><span>lanb</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lanb has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>19 Oct '11, 10:09</strong> </span></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p><span>multipleinte...</span><br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span></p></div></div><div id="comments-container-6987" class="comments-container"><span id="6991"></span><div id="comment-6991" class="comment"><div id="post-6991-score" class="comment-score"></div><div class="comment-text"><p>It may also help if you post the "MSVC error".</p></div><div id="comment-6991-info" class="comment-info"><span class="comment-age">(19 Oct '11, 10:09)</span> <span class="comment-user userinfo">multipleinte...</span></div></div></div><div id="comment-tools-6987" class="comment-tools"></div><div class="clear"></div><div id="comment-6987-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6990"></span>

<div id="answer-container-6990" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6990-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6990-score" class="post-score" title="current number of votes">1</div><span id="post-6990-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I assume that you control the code that actually decodes your protocol (if not, there won't be much you can do other than contact the maintainer of the decoder). That said, my guess is that the dissector for your protocol is attempting to allocate a buffer for inflated/decrypted/etc data based on a size field that is not bounds-checked and either incorrectly extracted or incorrectly set in your capture file. Put differently, something like this is in the <code>dissect_PROTONAME</code> function:</p><pre><code>guint32 inflated_size;
guint8 *inflated_data_buffer;
...
inflated_size = tvb_get_ntohl(tvb, OFFSET, ENCODING);
inflated_data_buffer = g_alloc(inflated_size);</code></pre><p>Realistically, it is impossible to say what is causing the problem without seeing some dissector code, but I assume you have access to that. Since you can compile Wireshark yourself, the best thing to do will be to use the debugger to see what's going on. At the very least, a stacktrace will help you pinpoint the problem, even if it is ultimately out of your control.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Oct '11, 10:07</strong></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p><span>multipleinte...</span><br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="multipleinterfaces has 9 accepted answers">12%</span></p></div></div><div id="comments-container-6990" class="comments-container"></div><div id="comment-tools-6990" class="comment-tools"></div><div class="clear"></div><div id="comment-6990-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


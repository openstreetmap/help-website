+++
type = "question"
title = ".?AVexception AVbad_alloc AVtype_info"
description = '''Hey guys, have you seen anything like this? What are these AVexception, AVtype_info, AVbad_alloc strings? I was not able to come up with a explanation with Google, a few malware analyiser site also have these strings at specific executables, but no specific answer for these. '''
date = "2015-09-10T03:42:00Z"
lastmod = "2015-09-10T17:37:00Z"
weight = 45753
keywords = [ "avexception", "avtype_info", "avbad_alloc" ]
aliases = [ "/questions/45753" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [.?AVexception AVbad\_alloc AVtype\_info](/questions/45753/avexception-avbad_alloc-avtype_info)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45753-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45753-score" class="post-score" title="current number of votes">0</div><span id="post-45753-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey guys,</p><p>have you seen anything like this? What are these AVexception, AVtype_info, AVbad_alloc strings?</p><p>I was not able to come up with a explanation with Google, a few malware analyiser site also have these strings at specific executables, but no specific answer for these.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/ws_YR5HUiM.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-avexception" rel="tag" title="see questions tagged &#39;avexception&#39;">avexception</span> <span class="post-tag tag-link-avtype_info" rel="tag" title="see questions tagged &#39;avtype_info&#39;">avtype_info</span> <span class="post-tag tag-link-avbad_alloc" rel="tag" title="see questions tagged &#39;avbad_alloc&#39;">avbad_alloc</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Sep '15, 03:42</strong></p><img src="https://secure.gravatar.com/avatar/1855020002bac3627bb6037224464140?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="albi&#39;s gravatar image" /><p><span>albi</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="albi has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>10 Sep '15, 03:43</strong> </span></p></div></div><div id="comments-container-45753" class="comments-container"><span id="45756"></span><div id="comment-45756" class="comment"><div id="post-45756-score" class="comment-score"></div><div class="comment-text"><p>Is this a Wireshark question? We'd normally expect to see some packets rather than a hexdump.</p></div><div id="comment-45756-info" class="comment-info"><span class="comment-age">(10 Sep '15, 04:39)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="45757"></span><div id="comment-45757" class="comment"><div id="post-45757-score" class="comment-score"></div><div class="comment-text"><p>Can you share a capture in a publicly accessible spot, e.g. <a href="http://cloudshark.org">CloudShark</a>?</p></div><div id="comment-45757-info" class="comment-info"><span class="comment-age">(10 Sep '15, 04:43)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-45753" class="comment-tools"></div><div class="clear"></div><div id="comment-45753-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45771"></span>

<div id="answer-container-45771" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45771-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45771-score" class="post-score" title="current number of votes">0</div><span id="post-45771-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>My guess is that it's a <a href="https://en.wikipedia.org/wiki/Name_mangling">"mangled" symbol name</a> in an executable image; see <a href="http://www.cplusplus.com/forum/windows/116679/">these linker error messages</a>, for example. "<a href="http://en.cppreference.com/w/cpp/memory/new/bad_alloc">bad_alloc</a>", "<a href="http://en.cppreference.com/w/cpp/types/type_info">type_info</a>", and "<a href="http://en.cppreference.com/w/cpp/error/exception">exception</a>" are all names in C++'s standard library.</p><p>If this is a packet capture, it's probably an executable image file being downloaded, and that's part of the image file's symbol table.</p><p>If this isn't a packet capture, it's not really a Wireshark question....</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Sep '15, 17:37</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-45771" class="comments-container"></div><div id="comment-tools-45771" class="comment-tools"></div><div class="clear"></div><div id="comment-45771-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


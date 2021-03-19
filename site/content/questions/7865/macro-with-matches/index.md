+++
type = "question"
title = "Macro with matches"
description = '''Hi, I was trying to define some macros using the matches operator but I get not result, just a error of the macro definition. After reading the wireshark doc I get no error with that example but what I want to set is something like: tcp matches &quot;([x90])&#92;1{$1,}&quot; --&amp;gt; this would find $1 times the x9...'''
date = "2011-12-09T00:20:00Z"
lastmod = "2011-12-10T03:35:00Z"
weight = 7865
keywords = [ "macro" ]
aliases = [ "/questions/7865" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Macro with matches](/questions/7865/macro-with-matches)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7865-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7865-score" class="post-score" title="current number of votes">0</div><span id="post-7865-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I was trying to define some macros using the matches operator but I get not result, just a error of the macro definition. After reading the <a href="https://www.wireshark.org/docs/wsug_html_chunked/ChDisplayFilterMacrosSection.html">wireshark doc</a> I get no error with that example but what I want to set is something like:</p><p>tcp matches "([x90])\1{$1,}" --&gt; this would find $1 times the x90 opcode. I've called this macro BO and I've tried the following without success.:</p><p>${BO:100} $BO{100}</p><p>The problem is not the matches operator because this work --&gt; tcp matches "$1". So, for some reason the macro doesn't work when you use hex digit</p><p>Any ideas? Thank you in advance</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-macro" rel="tag" title="see questions tagged &#39;macro&#39;">macro</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Dec '11, 00:20</strong></p><img src="https://secure.gravatar.com/avatar/57c8ddb7ed6ba271696a4631abf6dd9a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BorjaMerino&#39;s gravatar image" /><p><span>BorjaMerino</span><br />
<span class="score" title="21 reputation points">21</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BorjaMerino has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>09 Dec '11, 05:28</strong> </span></p></div></div><div id="comments-container-7865" class="comments-container"></div><div id="comment-tools-7865" class="comment-tools"></div><div class="clear"></div><div id="comment-7865-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7893"></span>

<div id="answer-container-7893" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7893-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7893-score" class="post-score" title="current number of votes">3</div><span id="post-7893-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Have a look at <del><a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=6613">bug 6613</a></del></p><p><strong>UPDATE:</strong> now fixed (as of SVN 40867)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Dec '11, 03:35</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>06 Feb '12, 15:10</strong> </span></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-7893" class="comments-container"></div><div id="comment-tools-7893" class="comment-tools"></div><div class="clear"></div><div id="comment-7893-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


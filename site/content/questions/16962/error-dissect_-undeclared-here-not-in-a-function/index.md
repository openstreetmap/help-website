+++
type = "question"
title = "error: &#x27;dissect_...&#x27; undeclared here (not in a function)"
description = '''Hello, community. I keep getting this error in the ...fn.c file while compiling my dissector. What would be the reason for it? Best regards Ewgenij'''
date = "2012-12-17T02:36:00Z"
lastmod = "2013-01-08T06:48:00Z"
weight = 16962
keywords = [ "function", "undeclared", "compiler", "error" ]
aliases = [ "/questions/16962" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [error: 'dissect\_...' undeclared here (not in a function)](/questions/16962/error-dissect_-undeclared-here-not-in-a-function)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16962-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16962-score" class="post-score" title="current number of votes">0</div><span id="post-16962-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, community. I keep getting this error in the ...fn.c file while compiling my dissector. What would be the reason for it?</p><p>Best regards Ewgenij</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-function" rel="tag" title="see questions tagged &#39;function&#39;">function</span> <span class="post-tag tag-link-undeclared" rel="tag" title="see questions tagged &#39;undeclared&#39;">undeclared</span> <span class="post-tag tag-link-compiler" rel="tag" title="see questions tagged &#39;compiler&#39;">compiler</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Dec '12, 02:36</strong></p><img src="https://secure.gravatar.com/avatar/74ba4ba7a26d5efda01b6ae18bbe48e4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ewgenijkkg&#39;s gravatar image" /><p><span>Ewgenijkkg</span><br />
<span class="score" title="66 reputation points">66</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ewgenijkkg has 3 accepted answers">60%</span></p></div></div><div id="comments-container-16962" class="comments-container"></div><div id="comment-tools-16962" class="comment-tools"></div><div class="clear"></div><div id="comment-16962-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="17564"></span>

<div id="answer-container-17564" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17564-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17564-score" class="post-score" title="current number of votes">0</div><span id="post-17564-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Ewgenijkkg has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>OK, I figured it out :-) My main ASN.1 file imported structure definitions from other ASN.1 files. But these files were absent in the dissector development folder. Nor did I use them as input arguments in the asn2wrs call. Nevertheless asn2wrs compiler did not report any errors. The errors became obvious later, at compile time of the resulting C-Sources. That was the error output I asked my question for.</p><p>Hmm, actually I would expect asn2wrs to notice the missing files to be included. Why doesn't it do that?</p><p>BR</p><p>Ewgenij</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jan '13, 06:48</strong></p><img src="https://secure.gravatar.com/avatar/74ba4ba7a26d5efda01b6ae18bbe48e4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ewgenijkkg&#39;s gravatar image" /><p><span>Ewgenijkkg</span><br />
<span class="score" title="66 reputation points">66</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ewgenijkkg has 3 accepted answers">60%</span></p></div></div><div id="comments-container-17564" class="comments-container"></div><div id="comment-tools-17564" class="comment-tools"></div><div class="clear"></div><div id="comment-17564-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="16971"></span>

<div id="answer-container-16971" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16971-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16971-score" class="post-score" title="current number of votes">1</div><span id="post-16971-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hi, You need to give more background for some one to be able to answer. I think you asked about asn2wrs before if that's the case your problem might be that that functions are declared in the wrong order you may have to do a forward declaration of the function or move the include. Look at other template files.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Dec '12, 04:57</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-16971" class="comments-container"><span id="17017"></span><div id="comment-17017" class="comment"><div id="post-17017-score" class="comment-score"></div><div class="comment-text"><p>Hello, thank you for the answer. What background would help? Actually, this error occurs a lot of time and concerns different asn objects...</p></div><div id="comment-17017-info" class="comment-info"><span class="comment-age">(18 Dec '12, 04:38)</span> <span class="comment-user userinfo">Ewgenijkkg</span></div></div><span id="17023"></span><div id="comment-17023" class="comment"><div id="post-17023-score" class="comment-score"></div><div class="comment-text"><p>If you are planning to release your dissector to Wireshark we could set up the asn directory and actually see your source files which would be easier. Otherwise a small piece of the template file and some more of the error log might help.</p></div><div id="comment-17023-info" class="comment-info"><span class="comment-age">(18 Dec '12, 06:14)</span> <span class="comment-user userinfo">Anders ♦</span></div></div></div><div id="comment-tools-16971" class="comment-tools"></div><div class="clear"></div><div id="comment-16971-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


+++
type = "question"
title = "capture connections/summaries only?"
description = '''dear sharkianers: is there any opportunity to capture nothing but date, ip &amp;amp; mac-address automatically each 24 hours to a file on windows? i tried the capturing with detailed options but that does log everything instead of the summary only.'''
date = "2011-04-29T11:37:00Z"
lastmod = "2011-04-29T14:47:00Z"
weight = 3816
keywords = [ "connections", "windows", "summary" ]
aliases = [ "/questions/3816" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [capture connections/summaries only?](/questions/3816/capture-connectionssummaries-only)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3816-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3816-score" class="post-score" title="current number of votes">0</div><span id="post-3816-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>dear sharkianers: is there any opportunity to capture nothing but date, ip &amp; mac-address automatically each 24 hours to a file on windows? i tried the capturing with detailed options but that does log everything instead of the summary only.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-connections" rel="tag" title="see questions tagged &#39;connections&#39;">connections</span> <span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-summary" rel="tag" title="see questions tagged &#39;summary&#39;">summary</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Apr '11, 11:37</strong></p><img src="https://secure.gravatar.com/avatar/56bb49dfc0e447ac7e5180ef9d063229?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Trucklejunior&#39;s gravatar image" /><p><span>Trucklejunior</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Trucklejunior has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>29 Apr '11, 11:38</strong> </span></p></div></div><div id="comments-container-3816" class="comments-container"></div><div id="comment-tools-3816" class="comment-tools"></div><div class="clear"></div><div id="comment-3816-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3820"></span>

<div id="answer-container-3820" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3820-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3820-score" class="post-score" title="current number of votes">2</div><span id="post-3820-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can use TShark:<br />
$ tshark -i 3 -T fields -e frame.time -e ip.addr -e eth.addr -a duration:86400 &gt; outfile.txt</p><p>You can find more information in the <a href="http://www.wireshark.org/docs/man-pages/tshark.html">man-page</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Apr '11, 13:03</strong></p><img src="https://secure.gravatar.com/avatar/fac200552b0c24be2bc93a740bd54d0d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joke&#39;s gravatar image" /><p><span>joke</span><br />
<span class="score" title="1278 reputation points"><span>1.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joke has 6 accepted answers">9%</span> </br></p></div></div><div id="comments-container-3820" class="comments-container"><span id="3823"></span><div id="comment-3823" class="comment"><div id="post-3823-score" class="comment-score"></div><div class="comment-text"><p>i knew it must be that simple, thanks you very much indeed!</p></div><div id="comment-3823-info" class="comment-info"><span class="comment-age">(29 Apr '11, 14:47)</span> <span class="comment-user userinfo">Trucklejunior</span></div></div></div><div id="comment-tools-3820" class="comment-tools"></div><div class="clear"></div><div id="comment-3820-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


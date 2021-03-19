+++
type = "question"
title = "how to filter tcap.tid with matches ?"
description = '''tcap.tid == 05:95:27:01 I want to filter the tcap.tid begin with 05:::** ,I use tcap.tid contains 05 to filter,ther many GSM_MAP message.I use tcap.tid matches &quot;^05&quot; ,filter nothing'''
date = "2013-02-04T06:48:00Z"
lastmod = "2015-08-10T20:00:00Z"
weight = 18279
keywords = [ "matches", "pcre", "filter", "perl" ]
aliases = [ "/questions/18279" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [how to filter tcap.tid with matches ?](/questions/18279/how-to-filter-tcaptid-with-matches)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18279-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18279-score" class="post-score" title="current number of votes">0</div><span id="post-18279-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>tcap.tid == 05:95:27:01 I want to filter the tcap.tid begin with 05:<strong>:</strong>:** ,I use tcap.tid contains 05 to filter,ther many GSM_MAP message.I use tcap.tid matches "^05" ,filter nothing</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-matches" rel="tag" title="see questions tagged &#39;matches&#39;">matches</span> <span class="post-tag tag-link-pcre" rel="tag" title="see questions tagged &#39;pcre&#39;">pcre</span> <span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-perl" rel="tag" title="see questions tagged &#39;perl&#39;">perl</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Feb '13, 06:48</strong></p><img src="https://secure.gravatar.com/avatar/2657181effdd2f83f8ac0e312161bfc2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="anshaohui&#39;s gravatar image" /><p><span>anshaohui</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="anshaohui has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>04 Feb '13, 19:33</strong> </span></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-18279" class="comments-container"></div><div id="comment-tools-18279" class="comment-tools"></div><div class="clear"></div><div id="comment-18279-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="18301"></span>

<div id="answer-container-18301" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18301-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18301-score" class="post-score" title="current number of votes">1</div><span id="post-18301-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="anshaohui has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Try <code>tcap.tid matches "^\x05"</code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Feb '13, 19:32</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-18301" class="comments-container"><span id="18312"></span><div id="comment-18312" class="comment"><div id="post-18312-score" class="comment-score"></div><div class="comment-text"><p>it works,thanks,</p></div><div id="comment-18312-info" class="comment-info"><span class="comment-age">(05 Feb '13, 02:10)</span> <span class="comment-user userinfo">anshaohui</span></div></div><span id="18313"></span><div id="comment-18313" class="comment"><div id="post-18313-score" class="comment-score"></div><div class="comment-text"><p>how to filter tcap.tid begin with 05:95?</p></div><div id="comment-18313-info" class="comment-info"><span class="comment-age">(05 Feb '13, 02:15)</span> <span class="comment-user userinfo">anshaohui</span></div></div><span id="18315"></span><div id="comment-18315" class="comment"><div id="post-18315-score" class="comment-score"></div><div class="comment-text"><p>If an answer provides a solution to your issue, please accept it for the benefit of other users by clicking the checkmark next to the answer. Please see the FAQ for more info.</p></div><div id="comment-18315-info" class="comment-info"><span class="comment-age">(05 Feb '13, 02:17)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="18317"></span><div id="comment-18317" class="comment"><div id="post-18317-score" class="comment-score">1</div><div class="comment-text"><p><span>@anshaohui</span>, try <code>tcap.tid matches "^\x05\x95"</code></p></div><div id="comment-18317-info" class="comment-info"><span class="comment-age">(05 Feb '13, 05:22)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="44953"></span><div id="comment-44953" class="comment"><div id="post-44953-score" class="comment-score"></div><div class="comment-text"><p><span>@cmaynard</span>，thanks</p></div><div id="comment-44953-info" class="comment-info"><span class="comment-age">(10 Aug '15, 20:00)</span> <span class="comment-user userinfo">anshaohui</span></div></div></div><div id="comment-tools-18301" class="comment-tools"></div><div class="clear"></div><div id="comment-18301-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


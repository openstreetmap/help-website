+++
type = "question"
title = "wireshark filter"
description = '''I am decoding SS7 messages on wireshark.  Is it possible to filter all messages in which particular number starts from &quot;0792xxxxxxx&quot; ? It should not gives you a result &quot;xxx0792xxx&quot;. Some filter like beginswith or starts with needed. '''
date = "2011-03-21T22:21:00Z"
lastmod = "2011-03-22T00:05:00Z"
weight = 3004
keywords = [ "ss7" ]
aliases = [ "/questions/3004" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark filter](/questions/3004/wireshark-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3004-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3004-score" class="post-score" title="current number of votes">0</div><span id="post-3004-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am decoding SS7 messages on wireshark. Is it possible to filter all messages in which particular number starts from "0792xxxxxxx" ? It should not gives you a result "xxx0792xxx".</p><p>Some filter like beginswith or starts with needed.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ss7" rel="tag" title="see questions tagged &#39;ss7&#39;">ss7</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Mar '11, 22:21</strong></p><img src="https://secure.gravatar.com/avatar/669f5d293c5f65994ce825c89e9d45c1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="parthe&#39;s gravatar image" /><p><span>parthe</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="parthe has no accepted answers">0%</span></p></div></div><div id="comments-container-3004" class="comments-container"></div><div id="comment-tools-3004" class="comment-tools"></div><div class="clear"></div><div id="comment-3004-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="3010"></span>

<div id="answer-container-3010" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3010-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3010-score" class="post-score" title="current number of votes">1</div><span id="post-3010-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can use the "matches" operator. You will have to use something like:</p><pre><code>&lt;field&gt; matches &quot;^0792.*&quot;</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Mar '11, 23:24</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-3010" class="comments-container"><span id="3011"></span><div id="comment-3011" class="comment"><div id="post-3011-score" class="comment-score"></div><div class="comment-text"><p>thanks for the solution. But It gives same result as Contains.</p></div><div id="comment-3011-info" class="comment-info"><span class="comment-age">(21 Mar '11, 23:44)</span> <span class="comment-user userinfo">parthe</span></div></div><span id="3012"></span><div id="comment-3012" class="comment"><div id="post-3012-score" class="comment-score"></div><div class="comment-text"><p>Did you use the "^" at the start of the filter? It means "match at the start of the string", so that should exclude "xxx0792xxx"</p></div><div id="comment-3012-info" class="comment-info"><span class="comment-age">(22 Mar '11, 00:05)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-3010" class="comment-tools"></div><div class="clear"></div><div id="comment-3010-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="3006"></span>

<div id="answer-container-3006" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3006-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3006-score" class="post-score" title="current number of votes">0</div><span id="post-3006-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Try:<br />
contains<br />
You can find more information in the <a href="http://wiki.wireshark.org/DisplayFilters">Wireshark Wiki</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Mar '11, 22:41</strong></p><img src="https://secure.gravatar.com/avatar/fac200552b0c24be2bc93a740bd54d0d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joke&#39;s gravatar image" /><p><span>joke</span><br />
<span class="score" title="1278 reputation points"><span>1.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joke has 6 accepted answers">9%</span> </br></br></p></div></div><div id="comments-container-3006" class="comments-container"><span id="3007"></span><div id="comment-3007" class="comment"><div id="post-3007-score" class="comment-score"></div><div class="comment-text"><p>As i told you contains also filtered messages which has number "xxxx0792xx"</p></div><div id="comment-3007-info" class="comment-info"><span class="comment-age">(21 Mar '11, 22:52)</span> <span class="comment-user userinfo">parthe</span></div></div><span id="3009"></span><div id="comment-3009" class="comment"><div id="post-3009-score" class="comment-score"></div><div class="comment-text"><p>(converted your "answer" to a "comment" to follow the Q&amp;A nature if this site, see also the FAQ)</p></div><div id="comment-3009-info" class="comment-info"><span class="comment-age">(21 Mar '11, 23:20)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-3006" class="comment-tools"></div><div class="clear"></div><div id="comment-3006-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


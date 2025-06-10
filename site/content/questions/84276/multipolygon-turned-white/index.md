+++
type = "question"
title = "Multipolygon turned white"
description = '''[Cross-post as it does not get through on Forum] Please help, I seem to have run myself into trouble. I have been editing a lot (in the ID-editor) on Koudenhoorn. The base is formed by a scrub multipolygon, containing a lot of inner relations. I follow the result in Information Freeway. At some poin...'''
date = "2022-04-26T16:38:00Z"
lastmod = "2022-04-26T19:00:00Z"
weight = 84276
keywords = [ "rendering", "multipolygon" ]
aliases = [ "/questions/84276" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Multipolygon turned white](/questions/84276/multipolygon-turned-white)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-84276-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84276-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84276-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>[Cross-post as it does not get through on Forum]</p>
<p>Please help, I seem to have run myself into trouble.</p>
<p>I have been editing a lot (in the ID-editor) on <a href="https://www.openstreetmap.org/#map=19/52.19259/4.50600">Koudenhoorn</a>.</p>
<p>The base is formed by a scrub multipolygon, containing a lot of inner relations.</p>
<p>I follow the result in <a href="https://informationfreeway.org/">Information Freeway</a>. At some point after editing, that base turned all white At first I thought it was just a matter of lagging, but it seems to be a structural problem.</p>
<p>I have reinspected the map, also tried Potlach and JOSM. I don't see anything clearly wrong. But I fear the problem is caused by the polygons, which are already pretty complicated. A clue may be that in the ID-editor marking of some edges seems to be 'jumpy' (double or alternating).</p>
<p>Do you have suggestions what may be the cause, recognizing this problem?</p>
<p>Or would you please have a look at the map, identifying some error?</p>
<p>I don't want to end up in a botched state, after improving it a lot. I hope I can just clear some error.</p>
<p>Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-multipolygon" rel="tag" title="see questions tagged &#39;multipolygon&#39;">multipolygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Apr '22, 16:38</strong></p>
<img src="https://secure.gravatar.com/avatar/858d6bd0ad7e1eb00776cceae44a7253?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BertMule&#39;s gravatar image" />
<p><span>BertMule</span><br />
<span class="score" title="7 reputation points">7</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BertMule has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Apr '22, 17:00</strong> </span></p>
</div>
</div>
<div id="comments-container-84276" class="comments-container">
&#10;</div>
<div id="comment-tools-84276" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84276-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="84279"></span>

<div id="answer-container-84279" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-84279-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84279-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-84279-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Bert,</p>
<p>I made some changes to the multipolygon that should fix it. I also decided to exclude a set of features from the multipolygon by redigitizing part of the "outer" to make it less complicated with less "inners".</p>
<p>Should take some time to re-render, but JOSM's validator now says the MP is fine (where it wasn't before).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Apr '22, 17:57</strong></p>
<img src="https://secure.gravatar.com/avatar/dc8a1ef54d3e25744ee52d1ad1459a81?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mboeringa&#39;s gravatar image" />
<p><span>mboeringa</span><br />
<span class="score" title="1542 reputation points"><span>1.5k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mboeringa has 4 accepted answers">9%</span></p>
</div>
</div>
<div id="comments-container-84279" class="comments-container">
<span id="84280"></span>
<div id="comment-84280" class="comment">
<div id="post-84280-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks!</p>
<p>It seems to be in the process of becoming better (correctly) rendered.</p>
<p>As far as I tried, the JOSM validator did not report any errors.</p>
<p>I see some of your simplifications, but I still wonder what effectively caused the problem.</p>
</div>
<div id="comment-84280-info" class="comment-info">
<span class="comment-age">(26 Apr '22, 18:45)</span> <span class="comment-user userinfo">BertMule</span>
</div>
</div>
<span id="84281"></span>
<div id="comment-84281" class="comment">
<div id="post-84281-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>There were multiple defects reported by JOSM, including overlapping section of ways that were not immediately visible. This was partly caused by your attempt not to combine nodes, leading to very "thin" sections of the multipolygon around "inners". This easily leads to geometric errors. Where possible and logical, merging nodes of two landuses bordering each other is recommmended IMO.</p>
</div>
<div id="comment-84281-info" class="comment-info">
<span class="comment-age">(26 Apr '22, 19:00)</span> <span class="comment-user userinfo">mboeringa</span>
</div>
</div>
</div>
<div id="comment-tools-84279" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84279-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


+++
type = "question"
title = "Mapping Land Uses With Multipolygon Relation"
description = '''I am updating the land uses in my neighbourhood. I’ve just found that, according to the wiki, the landuse key should not be mapped as a relation (multipolygon). Is it right? I hope not because I have mapped land uses with multipolygon relations for years. If the wiki is right, should I revert all th...'''
date = "2020-10-04T17:09:00Z"
lastmod = "2020-10-05T14:05:00Z"
weight = 76943
keywords = [ "wiki", "landuse", "mapping", "multipolygon" ]
aliases = [ "/questions/76943" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Mapping Land Uses With Multipolygon Relation](/questions/76943/mapping-land-uses-with-multipolygon-relation)

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
<span id="post-76943-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76943-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-76943-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am updating the land uses in my neighbourhood. I’ve just found that, according to the <a href="https://wiki.openstreetmap.org/wiki/Key:landuse">wiki</a>, the landuse key should not be mapped as a relation (multipolygon). Is it right? I hope not because I have mapped land uses with multipolygon relations for years.</p>
<p>If the wiki is right, should I revert all these landuse multipolygons into areas (i.e. duplicating ways for adjacent land use)?</p>
<p>Thanks in advance</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-wiki" rel="tag" title="see questions tagged &#39;wiki&#39;">wiki</span> <span class="post-tag tag-link-landuse" rel="tag" title="see questions tagged &#39;landuse&#39;">landuse</span> <span class="post-tag tag-link-mapping" rel="tag" title="see questions tagged &#39;mapping&#39;">mapping</span> <span class="post-tag tag-link-multipolygon" rel="tag" title="see questions tagged &#39;multipolygon&#39;">multipolygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Oct '20, 17:09</strong></p>
<img src="https://secure.gravatar.com/avatar/a504353df13461ace2c733906a99ce16?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jfd553&#39;s gravatar image" />
<p><span>jfd553</span><br />
<span class="score" title="389 reputation points">389</span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jfd553 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-76943" class="comments-container">
&#10;</div>
<div id="comment-tools-76943" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76943-form-container" class="comment-form-container">
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

<span id="76944"></span>

<div id="answer-container-76944" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76944-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76944-score" class="post-score" title="current number of votes">
7
</div>
<span id="post-76944-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="jfd553 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is a misunderstanding. The <img src="https://wiki.openstreetmap.org/w/images/thumb/8/8a/Osm_element_relation_no.svg/30px-Osm_element_relation_no.svg.png" alt="relation with red bar" /> icon means you shouldn't be using that on other kinds of relations, but the use on areas (<img src="https://wiki.openstreetmap.org/w/images/thumb/e/e6/Osm_element_area.svg/30px-Osm_element_area.svg.png" alt="area" /> icon) is fine, and that includes multipolygon relations.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Oct '20, 17:28</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</img>
</div>
</div>
<div id="comments-container-76944" class="comments-container">
<span id="76946"></span>
<div id="comment-76946" class="comment">
<div id="post-76946-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Baaaa! so obvious. Thanks</p>
</div>
<div id="comment-76946-info" class="comment-info">
<span class="comment-age">(04 Oct '20, 18:48)</span> <span class="comment-user userinfo">jfd553</span>
</div>
</div>
<span id="76954"></span>
<div id="comment-76954" class="comment">
<div id="post-76954-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>HI Daniel, a piece of farmland could be irrigated by a pivot, which brings even 2 farmlands in the same multypolygone :-)</p>
</div>
<div id="comment-76954-info" class="comment-info">
<span class="comment-age">(04 Oct '20, 23:59)</span> <span class="comment-user userinfo">Hendrikklaas</span>
</div>
</div>
<span id="76966"></span>
<div id="comment-76966" class="comment">
<div id="post-76966-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>This is basically a matter of mapping style. Multipolygons reduce the number of ways, but can be misuderstood by other users and accidentally damaged. Conversely using ways can make it difficult to locate the exact way to change in some editors. In general it's best to follow whatever local convention is used (in many European countries, and some US states, imports of landcover data means that the bulk of landuse polygons will be relations). There's certainly no need to change what you have already done.</p>
</div>
<div id="comment-76966-info" class="comment-info">
<span class="comment-age">(05 Oct '20, 14:05)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-76944" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76944-form-container" class="comment-form-container">
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


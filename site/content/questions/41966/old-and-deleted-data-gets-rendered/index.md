+++
type = "question"
title = "old and deleted data gets rendered"
description = '''Hi there, about 1 month ago I devided a farm into parts and created new farms and meadows. But now the old farm, that was a multipolygon, is still rendered (mapnik). It is not part of the map now (it may was part of http://www.openstreetmap.org/relation/1418460/ in the past). The same happend to a s...'''
date = "2015-03-28T16:37:00Z"
lastmod = "2015-03-30T07:48:00Z"
weight = 41966
keywords = [ "old", "data", "mapnik", "rendering" ]
aliases = [ "/questions/41966" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [old and deleted data gets rendered](/questions/41966/old-and-deleted-data-gets-rendered)

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
<span id="post-41966-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41966-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-41966-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi there,</p>
<p>about 1 month ago I devided a farm into parts and created new farms and meadows. But now the old farm, that was a multipolygon, is still rendered (mapnik). It is not part of the map now (it may was part of <a href="http://www.openstreetmap.org/relation/1418460/">http://www.openstreetmap.org/relation/1418460/</a> in the past). The same happend to a still existing residential (no multipolygon). <a href="https://www.openstreetmap.org/way/335237650">https://www.openstreetmap.org/way/335237650</a> When I change its shape, the new shape gets rendered, but the old too. When I delete a node, that was part of these shapes, then the old data is gone and not rendered any more. Moving a node seems to move the old data too.</p>
<p>Does anyone know what could cause this and how I could solve it, without removing all of the nodes and replace them by new ones.</p>
<p>I think that within the changeset check in something went wrong, both problems are may caused by the same chek in.</p>
<p><img src="http://www.norbert-freier.de/rendering.png" title="title" alt="rendering" /></p>
<p>Thanks <a href="https://www.openstreetmap.org/user/Jeti87" title="title">Jeti87</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-old" rel="tag" title="see questions tagged &#39;old&#39;">old</span> <span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Mar '15, 16:37</strong></p>
<img src="https://secure.gravatar.com/avatar/f21acfb29c93d240a1146966c48906d1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jeti87&#39;s gravatar image" />
<p><span>Jeti87</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jeti87 has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Mar '15, 19:35</strong> </span></p>
</div>
</div>
<div id="comments-container-41966" class="comments-container">
<span id="41968"></span>
<div id="comment-41968" class="comment">
<div id="post-41968-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>That's indeed interesting. Looks like the rendering database for the standard layer still contains already deleted data. When opening the data layer only the new shape is shown.</p>
</div>
<div id="comment-41968-info" class="comment-info">
<span class="comment-age">(28 Mar '15, 19:05)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-41966" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41966-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="41970"></span>

<div id="answer-container-41970" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-41970-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41970-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-41970-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There was a replication glitch roughly 1 month ago which has likely caused the issue, this will be rectified if and when the tile server databases get re-imported.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Mar '15, 21:40</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Mar '15, 21:41</strong> </span></p>
</div>
</div>
<div id="comments-container-41970" class="comments-container">
&#10;</div>
<div id="comment-tools-41970" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41970-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="41978"></span>

<div id="answer-container-41978" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-41978-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41978-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-41978-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I undeleted and deleted the <a href="https://www.openstreetmap.org/way/326491809/history">previous landuse way 326491809</a> again. Hopefully the rendering database will soon have the correct (=deleted) version of this way.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Mar '15, 09:45</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-41978" class="comments-container">
<span id="41979"></span>
<div id="comment-41979" class="comment">
<div id="post-41979-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks. We will see :-)</p>
</div>
<div id="comment-41979-info" class="comment-info">
<span class="comment-age">(29 Mar '15, 09:46)</span> <span class="comment-user userinfo">Jeti87</span>
</div>
</div>
<span id="41980"></span>
<div id="comment-41980" class="comment">
<div id="post-41980-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Note that the above action doesn't make sense. The rendering databases are literally "throw away". By artifically creating new versions you are simply increasing bloat in the "real" database.</p>
</div>
<div id="comment-41980-info" class="comment-info">
<span class="comment-age">(29 Mar '15, 09:59)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="41981"></span>
<div id="comment-41981" class="comment">
<div id="post-41981-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thats true. But seriously, the OSM database is already full of bloat. Bad imports, superfluous and meaningless tags, objects that have been deleted and drawn anew like this landuse in the first place. Of course that's a pitty. But I just added two versions to an existing object, compared to the whole database these changes are insignificant in my opinion. And so far there doesn't seem to be an alternative solution for fixing this problem except of waiting for a re-import, which may not come any time soon.</p>
</div>
<div id="comment-41981-info" class="comment-info">
<span class="comment-age">(29 Mar '15, 10:37)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="41982"></span>
<div id="comment-41982" class="comment">
<div id="post-41982-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Unfortunately it didn't make any difference :(</p>
</div>
<div id="comment-41982-info" class="comment-info">
<span class="comment-age">(29 Mar '15, 13:23)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="41985"></span>
<div id="comment-41985" class="comment">
<div id="post-41985-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>btw: OSM German style is not affected: <a href="http://openstreetmap.de/karte.html?zoom=16&amp;lat=50.65155&amp;lon=13.25607&amp;layers=B000TT">http://openstreetmap.de/karte.html?zoom=16&amp;lat=50.65155&amp;lon=13.25607&amp;layers=B000TT</a></p>
</div>
<div id="comment-41985-info" class="comment-info">
<span class="comment-age">(29 Mar '15, 13:42)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
<span id="41987"></span>
<div id="comment-41987" class="comment not_top_scorer">
<div id="post-41987-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/8708/mmd"></a><a href="http://help.openstreetmap.org/users/8708/mmd">@mmd</a> The <a href="https://www.openstreetmap.org/#map=17/50.65175/13.25163&amp;layers=H">HOT layer</a> neither. It's just the standard layer (or better the database for the standard layer) which has both old and new data.</p>
</div>
<div id="comment-41987-info" class="comment-info">
<span class="comment-age">(29 Mar '15, 14:14)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="42008"></span>
<div id="comment-42008" class="comment not_top_scorer">
<div id="post-42008-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Meanwhile some tiles have been re-rendered but now parts of it are even more weird and broken. <a href="https://www.openstreetmap.org/#map=17/50.65175/13.25163">Looks</a> a little bit like cubism.</p>
</div>
<div id="comment-42008-info" class="comment-info">
<span class="comment-age">(30 Mar '15, 07:48)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-41978" class="comment-tools">
<span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-41978-form-container" class="comment-form-container">
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


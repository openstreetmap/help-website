+++
type = "question"
title = "How to get all the city squares in a country?"
description = '''I need a list of all the city squares in a country. Does anyone know how to search for it? Thanks!'''
date = "2015-11-20T20:50:00Z"
lastmod = "2015-11-24T14:20:00Z"
weight = 46756
keywords = [ "city", "squares" ]
aliases = [ "/questions/46756" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to get all the city squares in a country?](/questions/46756/how-to-get-all-the-city-squares-in-a-country)

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
<span id="post-46756-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46756-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-46756-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I need a list of all the city squares in a country. Does anyone know how to search for it? Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-city" rel="tag" title="see questions tagged &#39;city&#39;">city</span> <span class="post-tag tag-link-squares" rel="tag" title="see questions tagged &#39;squares&#39;">squares</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Nov '15, 20:50</strong></p>
<img src="https://secure.gravatar.com/avatar/b06446fd288ce311a9441a82f43b1a99?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="eselcuk&#39;s gravatar image" />
<p><span>eselcuk</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="eselcuk has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-46756" class="comments-container">
<span id="46761"></span>
<div id="comment-46761" class="comment">
<div id="post-46761-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>It depends on what you consider a "city square". Most plazas are likely tagged as highway=pedestrian areas, but it isn't clear if that's what you're looking for.</p>
</div>
<div id="comment-46761-info" class="comment-info">
<span class="comment-age">(20 Nov '15, 23:59)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
</div>
<div id="comment-tools-46756" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46756-form-container" class="comment-form-container">
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

<span id="46816"></span>

<div id="answer-container-46816" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-46816-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46816-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-46816-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Get yourself a country extract and search for objects with</p>
<p><code>highway=pedestrian and (area=yes and/or type=multipolygon) and name is not empty</code></p>
<p>According to the tool you use the exact syntax will change. You can find documentation of suitable tools in the <a href="http://wiki.openstreetmap.org/wiki/Category:OSM_processing">osm wiki</a>, e.g. Osmosis, osmfilter, or use an online service like overpass.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Nov '15, 14:20</strong></p>
<img src="https://secure.gravatar.com/avatar/f09c0b7a655fed386e070e036e2da248?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dieterdreist&#39;s gravatar image" />
<p><span>dieterdreist</span><br />
<span class="score" title="3677 reputation points"><span>3.7k</span></span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="67 badges"><span class="bronze">●</span><span class="badgecount">67</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dieterdreist has 4 accepted answers">3%</span></p>
</div>
</div>
<div id="comments-container-46816" class="comments-container">
&#10;</div>
<div id="comment-tools-46816" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46816-form-container" class="comment-form-container">
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


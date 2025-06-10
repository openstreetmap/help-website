+++
type = "question"
title = "counting houses"
description = '''Is there a way to automatically count houses in a street/area?'''
date = "2016-09-14T12:19:00Z"
lastmod = "2023-12-07T11:05:00Z"
weight = 52041
keywords = [ "houses", "counting" ]
aliases = [ "/questions/52041" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [counting houses](/questions/52041/counting-houses)

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
<span id="post-52041-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52041-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-52041-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is there a way to automatically count houses in a street/area?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-houses" rel="tag" title="see questions tagged &#39;houses&#39;">houses</span> <span class="post-tag tag-link-counting" rel="tag" title="see questions tagged &#39;counting&#39;">counting</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Sep '16, 12:19</strong></p>
<img src="https://secure.gravatar.com/avatar/16c0a44dfac087f81d745cdc964c194b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hoatzin64&#39;s gravatar image" />
<p><span>hoatzin64</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hoatzin64 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-52041" class="comments-container">
&#10;</div>
<div id="comment-tools-52041" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52041-form-container" class="comment-form-container">
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

<span id="52042"></span>

<div id="answer-container-52042" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52042-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52042-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-52042-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="hoatzin64 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="http://overpass-turbo.eu/s/ioj">This query</a> will generate a csv of all the "houses" in your current view. Just scroll down to see the number of records in the file.</p>
<p><a href="http://overpass-turbo.eu/s/iok">This query</a> does the exact same thing, but visualizes them on a map. You can then export them in any number of formats.</p>
<p>You can also draw a bounding box on the map to have better control of what gets counted.</p>
<p>You need both "way" and "relation", because houses with a courtyard are relations in the OSM data model.</p>
<p>Houses might be mapped as building=yes, not building=house. To get all buildings instead, simply replace ["building"="house"] with ["building"].</p>
<p>If this does not answer your question, please edit your question to clarify what exactly you're trying to do. If it does, please mark the V next to this answer to mark your question as answered.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Sep '16, 14:16</strong></p>
<img src="https://secure.gravatar.com/avatar/1df835d513b1282e0edd7405d29cd8d9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joost%20schouppe&#39;s gravatar image" />
<p><span>joost schouppe</span><br />
<span class="score" title="3427 reputation points"><span>3.4k</span></span><span title="24 badges"><span class="badge1">●</span><span class="badgecount">24</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="87 badges"><span class="bronze">●</span><span class="badgecount">87</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joost schouppe has 9 accepted answers">12%</span></p>
</div>
</div>
<div id="comments-container-52042" class="comments-container">
&#10;</div>
<div id="comment-tools-52042" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52042-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="88047"></span>

<div id="answer-container-88047" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-88047-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-88047-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-88047-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi Joost,</p>
<p>I wish to thank you for your response to this post.</p>
<p>Sorry to contact you this way, but I have an additional question, is it also possible to draw a polygon or only possible to draw a square?</p>
<p>Thanks a lot in advance, Gill</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Dec '23, 09:18</strong></p>
<img src="https://secure.gravatar.com/avatar/6fb551e85937cec2f8ffd13b97098486?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gill&#39;s gravatar image" />
<p><span>Gill</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gill has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Dec '23, 09:19</strong> </span></p>
</div>
</div>
<div id="comments-container-88047" class="comments-container">
<span id="88048"></span>
<div id="comment-88048" class="comment">
<div id="post-88048-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yep, you can draw your own polygon. For example, this query draws a rough outline around Belgium: <a href="https://overpass-turbo.eu/s/1Er7">https://overpass-turbo.eu/s/1Er7</a> You simply need to list the coördinates that form your polygon. You could use a tool like <a href="https://geojson.io">https://geojson.io</a> to draw something on a map. It is also possible to search within the outline of an existing OpenStreetMap polygon.</p>
</div>
<div id="comment-88048-info" class="comment-info">
<span class="comment-age">(07 Dec '23, 11:05)</span> <span class="comment-user userinfo">joost schouppe</span>
</div>
</div>
</div>
<div id="comment-tools-88047" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-88047-form-container" class="comment-form-container">
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


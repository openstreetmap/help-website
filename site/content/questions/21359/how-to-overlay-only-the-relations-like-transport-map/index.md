+++
type = "question"
title = "How to overlay only the relations like transport map"
description = '''Hi Guys, I&#x27;m new with openstreetmap and I want to overlay on the map only the relations. Is there a way to do this using the renderTheme ? Tanks'''
date = "2013-04-09T19:36:00Z"
lastmod = "2013-04-11T17:58:00Z"
weight = 21359
keywords = [ "rendering", "theme", "osmosis" ]
aliases = [ "/questions/21359" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to overlay only the relations like transport map](/questions/21359/how-to-overlay-only-the-relations-like-transport-map)

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
<span id="post-21359-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21359-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-21359-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi Guys,</p>
<p>I'm new with openstreetmap and I want to overlay on the map only the relations. Is there a way to do this using the renderTheme ?</p>
<p>Tanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-theme" rel="tag" title="see questions tagged &#39;theme&#39;">theme</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Apr '13, 19:36</strong></p>
<img src="https://secure.gravatar.com/avatar/33534aa23873d76508b6e0e0743700b2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Thiago%20Lima&#39;s gravatar image" />
<p><span>Thiago Lima</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Thiago Lima has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-21359" class="comments-container">
<span id="21361"></span>
<div id="comment-21361" class="comment">
<div id="post-21361-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It's not entirely sure what you mean. A little web searching suggests that you might be asking about MapsForge - would it be possible to expand the question a bit?</p>
</div>
<div id="comment-21361-info" class="comment-info">
<span class="comment-age">(09 Apr '13, 19:48)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="21362"></span>
<div id="comment-21362" class="comment">
<div id="post-21362-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes,</p>
<p>I have an .osm file that has some tags called ralation. This tags represent buslines on the map. I need to make a renderTheme to highlight the "relations" on the map, however the renderTheme.xsd allows to make it only for "ways" and "nodes". In the openStreetMap official website it is possible to see a Transport Map. I want exactly that, but I don't see how to! =s</p>
</div>
<div id="comment-21362-info" class="comment-info">
<span class="comment-age">(09 Apr '13, 20:01)</span> <span class="comment-user userinfo">Thiago Lima</span>
</div>
</div>
</div>
<div id="comment-tools-21359" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21359-form-container" class="comment-form-container">
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

<span id="21366"></span>

<div id="answer-container-21366" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-21366-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21366-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-21366-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In OpenStreetMap, a relation is a collection of nodes and ways. A relation does not have a longitude or latitude, but the nodes and ways in, do have them. There are different types of relations, see <a href="https://wiki.openstreetmap.org/wiki/Relations.">https://wiki.openstreetmap.org/wiki/Relations.</a></p>
<p>When you created your .osm file with a Overpass Query, you can "extend" the relation so you retrieve the nodes and ways in it. <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Language_Guide.">https://wiki.openstreetmap.org/wiki/Overpass_API/Language_Guide.</a> But it is also possible that your .osm file already has the nodes and ways in the relation.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Apr '13, 04:32</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-21366" class="comments-container">
<span id="21410"></span>
<div id="comment-21410" class="comment">
<div id="post-21410-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes,</p>
<p>My .osm file already have nodes and ways related with the relations. The problem is how to specify that the relations should be highlighted by the mapsforge engine. Currently I did a script to add special tags into the way tags, but I don't know if it's the better.</p>
<p>Thanks</p>
</div>
<div id="comment-21410-info" class="comment-info">
<span class="comment-age">(11 Apr '13, 17:58)</span> <span class="comment-user userinfo">Thiago Lima</span>
</div>
</div>
</div>
<div id="comment-tools-21366" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21366-form-container" class="comment-form-container">
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


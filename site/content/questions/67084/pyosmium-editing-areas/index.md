+++
type = "question"
title = "PyOsmium: editing &quot;areas&quot; ?"
description = '''Hello, PyOsmium (and Osmium) has an &quot;area&quot; object, which are:  “synthetic OSM objects”. They can be created from closed ways and multipolygon relations. Areas have all the same attributes as real OSM objects and they have tags, too. In addition they have a set of outer and inner rings describing the...'''
date = "2018-12-06T16:17:00Z"
lastmod = "2018-12-08T08:21:00Z"
weight = 67084
keywords = [ "osmium", "pyosmium", "editing", "tags", "areas" ]
aliases = [ "/questions/67084" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [PyOsmium: editing "areas" ?](/questions/67084/pyosmium-editing-areas)

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
<span id="post-67084-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67084-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-67084-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>PyOsmium (and Osmium) has an "area" object, which are:</p>
<blockquote>
<p>“synthetic OSM objects”. They can be created from closed ways and multipolygon relations. Areas have all the same attributes as real OSM objects and they have tags, too. In addition they have a set of outer and inner rings describing the MultiPolygon geometry. See the chapter on Areas for details.</p>
</blockquote>
<p>I want to add some tags on "areas" (really, on building objects), but it seems there is no possibility of doing so (area tags are non mutable) and getting an osc file out of this.</p>
<p>What I need from building is a closed polygon representing the building, and using areas made it easy to have this representation.</p>
<p>Should I go and edit ways directly? It will miss building defined by relations, so i'm not really happy with this approach. How would you go and edit "buildings" programmatically?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmium" rel="tag" title="see questions tagged &#39;osmium&#39;">osmium</span> <span class="post-tag tag-link-pyosmium" rel="tag" title="see questions tagged &#39;pyosmium&#39;">pyosmium</span> <span class="post-tag tag-link-editing" rel="tag" title="see questions tagged &#39;editing&#39;">editing</span> <span class="post-tag tag-link-tags" rel="tag" title="see questions tagged &#39;tags&#39;">tags</span> <span class="post-tag tag-link-areas" rel="tag" title="see questions tagged &#39;areas&#39;">areas</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Dec '18, 16:17</strong></p>
<img src="https://secure.gravatar.com/avatar/caf6de73416fe00ae29200008ca222eb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rev&#39;s gravatar image" />
<p><span>Rev</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rev has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Dec '18, 16:46</strong> </span></p>
</div>
</div>
<div id="comments-container-67084" class="comments-container">
<span id="67092"></span>
<div id="comment-67092" class="comment">
<div id="post-67092-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>There seems to be some confusion here on how OSM data works and how Osmium/PyOsmium works with OSM data, but it is difficult to help you without understanding better what you want to achieve. Can you explain what your end goal is here, not in terms of the workings of Osmium, but on a higher level?</p>
</div>
<div id="comment-67092-info" class="comment-info">
<span class="comment-age">(07 Dec '18, 07:37)</span> <span class="comment-user userinfo">Jochen Topf</span>
</div>
</div>
<span id="67093"></span>
<div id="comment-67093" class="comment">
<div id="post-67093-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Areas are closed ways or multipolygons. What I want to do is to be able to modify "areas" (adding some tags to them) without having to understand if they are ways or multipolygons.</p>
</div>
<div id="comment-67093-info" class="comment-info">
<span class="comment-age">(07 Dec '18, 07:39)</span> <span class="comment-user userinfo">Rev</span>
</div>
</div>
</div>
<div id="comment-tools-67084" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67084-form-container" class="comment-form-container">
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

<span id="67106"></span>

<div id="answer-container-67106" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67106-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67106-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-67106-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It doesn't make sense to change the "areas", because they are not real OSM objects. "Areas" in Osmium are a fiction that makes sense when you want to export OSM data into some other format. Osmium creates those areas from the OSM data and then you can transform them into some format (like GeoJSON or so) that understands Polygons. But you can not use them to do something with the OSM data, because that still has ways and relations. So you have to change all closed ways and all multipolygon relations which isn't that hard anyway. All OSM objects (nodes, ways, relations and the pseudo-objects areas) are read-only in Osmium for performance reasons, so to change them you have to create a new object as a copy of the old one with the changes you want.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Dec '18, 08:21</strong></p>
<img src="https://secure.gravatar.com/avatar/2d4dfcdcde73aa5e2ffa4a9b3a7cb51d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jochen%20Topf&#39;s gravatar image" />
<p><span>Jochen Topf</span><br />
<span class="score" title="5244 reputation points"><span>5.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jochen Topf has 32 accepted answers">31%</span></p>
</div>
</div>
<div id="comments-container-67106" class="comments-container">
&#10;</div>
<div id="comment-tools-67106" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67106-form-container" class="comment-form-container">
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


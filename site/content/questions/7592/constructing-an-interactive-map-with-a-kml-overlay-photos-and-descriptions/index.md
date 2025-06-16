+++
type = "question"
title = "Constructing an interactive map with a kml overlay, photos and descriptions"
description = '''how should I go about constructing the map of a university compound using Openstreetmap? The project&#x27;s objectives are as stated below:  create a kml file of all places of interests(POI) i.e labs,libraries,lecture theatres etc. kml file should include descriptions and photos. Setup a website to demon...'''
date = "2011-09-03T15:22:00Z"
lastmod = "2011-09-04T01:48:00Z"
weight = 7592
keywords = [ "crtmp" ]
aliases = [ "/questions/7592" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Constructing an interactive map with a kml overlay, photos and descriptions](/questions/7592/constructing-an-interactive-map-with-a-kml-overlay-photos-and-descriptions)

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
<span id="post-7592-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7592-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-7592-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>how should I go about constructing the map of a university compound using Openstreetmap? The project's objectives are as stated below:</p>
<ol>
<li>create a kml file of all places of interests(POI) i.e labs,libraries,lecture theatres etc.</li>
<li>kml file should include descriptions and photos.</li>
<li>Setup a website to demonstrate this map.</li>
</ol>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-crtmp" rel="tag" title="see questions tagged &#39;crtmp&#39;">crtmp</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Sep '11, 15:22</strong></p>
<img src="https://secure.gravatar.com/avatar/03c53b780839235897406734ecfd4518?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Reuben%20Alfred&#39;s gravatar image" />
<p><span>Reuben Alfred</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Reuben Alfred has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Sep '11, 02:16</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/f09c0b7a655fed386e070e036e2da248?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dieterdreist&#39;s gravatar image" />
<p><span>dieterdreist</span><br />
<span class="score" title="3677 reputation points"><span>3.7k</span></span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="67 badges"><span class="bronze">●</span><span class="badgecount">67</span></span></p>
</div>
</div>
<div id="comments-container-7592" class="comments-container">
&#10;</div>
<div id="comment-tools-7592" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7592-form-container" class="comment-form-container">
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

<span id="7597"></span>

<div id="answer-container-7597" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7597-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7597-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-7597-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>.1. Not sure what is the best way to create a kml file, but you can export kml from a postgresql/postgis database. To get the osm data into the database there are several programs available (which either use predefined schemes or require from you to define a scheme) like osmosis, osm2pgsql, imposm and others. The <a href="https://wiki.openstreetmap.org/wiki/Develop">openstreetmap-wiki</a> contains descriptions about these tools.</p>
<p>.3. You can do this for example with Openlayers.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Sep '11, 01:48</strong></p>
<img src="https://secure.gravatar.com/avatar/f09c0b7a655fed386e070e036e2da248?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dieterdreist&#39;s gravatar image" />
<p><span>dieterdreist</span><br />
<span class="score" title="3677 reputation points"><span>3.7k</span></span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="67 badges"><span class="bronze">●</span><span class="badgecount">67</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dieterdreist has 4 accepted answers">3%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Sep '11, 02:11</strong> </span></p>
</div>
</div>
<div id="comments-container-7597" class="comments-container">
&#10;</div>
<div id="comment-tools-7597" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7597-form-container" class="comment-form-container">
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


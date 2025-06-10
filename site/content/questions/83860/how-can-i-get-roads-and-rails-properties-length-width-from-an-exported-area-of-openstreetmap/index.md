+++
type = "question"
title = "How can I get roads and rails properties (length, width, ....) from an exported area of OpenStreetMap?"
description = '''Hi, how can I get the roads and rails properties, as length, width, number of lanes and (traffic) direction from an exported area of OpenStreetMap? I would need to export/download nodes and edges of an area and get the roads and rails properties (at least the length) - Any idea?'''
date = "2022-03-15T12:05:00Z"
lastmod = "2022-03-20T18:52:00Z"
weight = 83860
keywords = [ "roads", "width", "length", "lanes", "rails" ]
aliases = [ "/questions/83860" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How can I get roads and rails properties (length, width, ....) from an exported area of OpenStreetMap?](/questions/83860/how-can-i-get-roads-and-rails-properties-length-width-from-an-exported-area-of-openstreetmap)

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
<span id="post-83860-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83860-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-83860-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, how can I get the roads and rails properties, as length, width, number of lanes and (traffic) direction from an exported area of OpenStreetMap?</p>
<p>I would need to export/download nodes and edges of an area and get the roads and rails properties (at least the length) - Any idea?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-roads" rel="tag" title="see questions tagged &#39;roads&#39;">roads</span> <span class="post-tag tag-link-width" rel="tag" title="see questions tagged &#39;width&#39;">width</span> <span class="post-tag tag-link-length" rel="tag" title="see questions tagged &#39;length&#39;">length</span> <span class="post-tag tag-link-lanes" rel="tag" title="see questions tagged &#39;lanes&#39;">lanes</span> <span class="post-tag tag-link-rails" rel="tag" title="see questions tagged &#39;rails&#39;">rails</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Mar '22, 12:05</strong></p>
<img src="https://secure.gravatar.com/avatar/8a0ffb17c91f5fb48a1854a707867e09?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="s_limo&#39;s gravatar image" />
<p><span>s_limo</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="s_limo has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Mar '22, 12:13</strong> </span></p>
</div>
</div>
<div id="comments-container-83860" class="comments-container">
&#10;</div>
<div id="comment-tools-83860" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83860-form-container" class="comment-form-container">
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

<span id="83932"></span>

<div id="answer-container-83932" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83932-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83932-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-83932-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You could open the file in QGIS if it is small, and do the measurements there. If it is bigger and you don’t have a dedicated software (which likely exists for road or rail lengths, but I don’t have a link at hand) you could import it into a geo database and get the lengths there. For example with osm2pgsql in latlong mode into PostGIS</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Mar '22, 18:52</strong></p>
<img src="https://secure.gravatar.com/avatar/f09c0b7a655fed386e070e036e2da248?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dieterdreist&#39;s gravatar image" />
<p><span>dieterdreist</span><br />
<span class="score" title="3677 reputation points"><span>3.7k</span></span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="67 badges"><span class="bronze">●</span><span class="badgecount">67</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dieterdreist has 4 accepted answers">3%</span></p>
</div>
</div>
<div id="comments-container-83932" class="comments-container">
&#10;</div>
<div id="comment-tools-83932" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83932-form-container" class="comment-form-container">
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


+++
type = "question"
title = "Trace GPS Coordinates"
description = '''Hi! so right now I have a database that pulls in Longitude/Latitude of Truck locations, how would I display a map of markers via a URL, CURL, or RESTful API? (each truck a different color if possible) '''
date = "2018-06-19T21:41:00Z"
lastmod = "2018-06-19T22:08:00Z"
weight = 64280
keywords = [ "url", "curl", "api", "markers" ]
aliases = [ "/questions/64280" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Trace GPS Coordinates](/questions/64280/trace-gps-coordinates)

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
<span id="post-64280-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64280-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-64280-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi! so right now I have a database that pulls in Longitude/Latitude of Truck locations, how would I display a map of markers via a URL, CURL, or RESTful API? (each truck a different color if possible)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-url" rel="tag" title="see questions tagged &#39;url&#39;">url</span> <span class="post-tag tag-link-curl" rel="tag" title="see questions tagged &#39;curl&#39;">curl</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-markers" rel="tag" title="see questions tagged &#39;markers&#39;">markers</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Jun '18, 21:41</strong></p>
<img src="https://secure.gravatar.com/avatar/0a5e6faee4b1d4a8d752386d124765db?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Maryjane0428&#39;s gravatar image" />
<p><span>Maryjane0428</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Maryjane0428 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-64280" class="comments-container">
&#10;</div>
<div id="comment-tools-64280" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64280-form-container" class="comment-form-container">
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

<span id="64282"></span>

<div id="answer-container-64282" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64282-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64282-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-64282-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There literally lots of options. given that you would likely will need a bespoke solution, you should have a look a <a href="https://leafletjs.com/">Leaflet</a> and <a href="http://openlayers.org/">OpenLayers</a>. Both are JS frameworks that allow displaying data on top of a map background.</p>
<p>Note as this doesn't actually seem to be OSM related you might fare better on <a href="https://gis.stackexchange.com/">GIS Stackexchange</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Jun '18, 22:08</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Jun '18, 22:09</strong> </span></p>
</div>
</div>
<div id="comments-container-64282" class="comments-container">
&#10;</div>
<div id="comment-tools-64282" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64282-form-container" class="comment-form-container">
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


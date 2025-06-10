+++
type = "question"
title = "[closed] Routing with OSM and private (shp) data"
description = '''A friend of mine faced me a question that I couldn&#x27;t answer. He wants to create a map (at first, an app, but also a print version) offering bicycle routing, considering OSM data (the cycleways and cyclelanes mapped) and what he calls cycleroutes (a concept different of bicycle routes on OSM), simple...'''
date = "2015-10-23T21:02:00Z"
lastmod = "2015-10-23T22:08:00Z"
weight = 46084
keywords = [ "shapefile", "routing" ]
aliases = [ "/questions/46084" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [\[closed\] Routing with OSM and private (shp) data](/questions/46084/routing-with-osm-and-private-shp-data)

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
<span id="post-46084-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46084-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-46084-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>A friend of mine faced me a question that I couldn't answer. He wants to create a map (at first, an app, but also a print version) offering bicycle routing, considering OSM data (the cycleways and cyclelanes mapped) and what he calls cycleroutes (a concept different of bicycle routes on OSM), simple and common roads that he arbitrarily choose over other streets because of their caracteristics, as in "calm roads". He has this network of calm roads mapped as a KML and as a SHP.</p>
<p>Note that those "calm roads" are not OSM living_streets, just better options to the bigger avenues, the path that is suggested to a cyclist on a given route.</p>
<p>Is it possible to use a routing application considering those paths? I thought about those possibilities:</p>
<p>1) creating a table listing each street on his road list to an array of OSM Way IDs. But this would require constant maintenance as people edit and split/merge/erase ways.</p>
<p>2) considering the street names, and somehow making the routing algorithm prefer those ways.</p>
<p>3) mapping those characteristics that made he chose those particular streets in first place (maxspeed=, incline=no, lanes=, etc etc) and tuning the routing algorithm to prefer those streets.</p>
<p>4) (worst possible option in my opinion) would be creating a tag for those streets, as in calm_street=yes and make the router prefer those.</p>
<p>All opinions are welcome.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-shapefile" rel="tag" title="see questions tagged &#39;shapefile&#39;">shapefile</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Oct '15, 21:02</strong></p>
<img src="https://secure.gravatar.com/avatar/673ca6641412c68c138afd1ba8bda156?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nighto&#39;s gravatar image" />
<p><span>Nighto</span><br />
<span class="score" title="196 reputation points">196</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nighto has one accepted answer">20%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Oct '15, 22:23</strong> </span></p>
</div>
</div>
<div id="comments-container-46084" class="comments-container">
&#10;</div>
<div id="comment-tools-46084" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46084-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Other" by Frederik Ramm 23 Oct '15, 22:09

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46085"></span>

<div id="answer-container-46085" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-46085-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46085-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-46085-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Nighto has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Your questions are interesting but this medium is not ideal for discussing the problem. Please post your question on either the "dev" or the "routing" mailing lists (see lists.openstreetmap.org/listinfo) or if you prefer on the development section of forum.openstreetmap.org.</p>
<p>This site is for finding the best answer to a concrete question (hence the upvoting of good answers and so on), but you are casting a rather wide net and this site is totally unsuitable for discussions (because it cannot keep things in sequence).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Oct '15, 21:11</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-46085" class="comments-container">
<span id="46086"></span>
<div id="comment-46086" class="comment">
<div id="post-46086-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Will do that. Thanks, Frederik!</p>
</div>
<div id="comment-46086-info" class="comment-info">
<span class="comment-age">(23 Oct '15, 22:08)</span> <span class="comment-user userinfo">Nighto</span>
</div>
</div>
</div>
<div id="comment-tools-46085" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46085-form-container" class="comment-form-container">
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


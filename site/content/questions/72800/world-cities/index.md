+++
type = "question"
title = "world cities"
description = '''Hi can I can get the cites with geographic locations and populations.'''
date = "2020-01-31T19:58:00Z"
lastmod = "2020-02-05T12:17:00Z"
weight = 72800
keywords = [ "cities", "with", "population" ]
aliases = [ "/questions/72800" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [world cities](/questions/72800/world-cities)

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
<span id="post-72800-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72800-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-72800-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi can I can get the cites with geographic locations and populations.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-cities" rel="tag" title="see questions tagged &#39;cities&#39;">cities</span> <span class="post-tag tag-link-with" rel="tag" title="see questions tagged &#39;with&#39;">with</span> <span class="post-tag tag-link-population" rel="tag" title="see questions tagged &#39;population&#39;">population</span>
</div>
<div id="question-controls" class="post-controls">
<div class="community-wiki">
This question is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Jan '20, 19:58</strong></p>
<img src="https://secure.gravatar.com/avatar/f6380d3b43daeb6bb221c23f6b50d563?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ramzan243&#39;s gravatar image" />
<p><span>Ramzan243</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ramzan243 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-72800" class="comments-container">
&#10;</div>
<div id="comment-tools-72800" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72800-form-container" class="comment-form-container">
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

<span id="72868"></span>

<div id="answer-container-72868" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72868-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72868-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-72868-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi.</p>
<p>It's quite easy to find cities of a limited area, with this <a href="https://overpass-turbo.eu/s/QpH">request</a> on overpass-turbo (build in one click using the wizard).</p>
<p>But for the <a href="https://overpass-turbo.eu/s/QpK">whole world</a> it's really hard on the server and browser, Overpass is not meant for worldwide requests. The result will be hard to parse, as most cities are nodes, but some are relations, hence to get the coordinates, you'll have to compute form the relation members. Also in OSM the <a href="https://wiki.openstreetmap.org/wiki/Key:population">population tag</a> is not really reliable, mostly used for rendering and search results ordering.</p>
<p>You should probably use wikidata, either through the <a href="https://wiki.openstreetmap.org/wiki/Key:wikidata">wikidata tag</a>, or directly using theirs tools (<a href="https://www.wikidata.org/wiki/Wikidata:SPARQL_query_service">SPARQL query service</a>).</p>
<p>From an <a href="https://www.wikidata.org/wiki/Wikidata:SPARQL_query_service/queries/examples#Largest_cities_of_the_world">example</a> and removing the 100 limit, I got 23128 cities, with population, using that <a href="https://w.wiki/Ggv">request</a>. Beware, it takes some time to compute, and some more to render.</p>
<p>Hope this helps.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Feb '20, 12:17</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-72868" class="comments-container">
&#10;</div>
<div id="comment-tools-72868" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72868-form-container" class="comment-form-container">
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


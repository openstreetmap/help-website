+++
type = "question"
title = "Just loading planet_osm_polygons to PostGIS"
description = '''Hi all, Slightly similar to another question I&#x27;ve already asked, but I think it deserved it&#x27;s own thread. I am running the below to import a Europe PBF to PostGIS. But I actually only need the building polygons (planet_osm_polygons). Is there a way to only import that table and skip the others? (and...'''
date = "2018-04-19T10:19:00Z"
lastmod = "2018-05-11T02:25:00Z"
weight = 63045
keywords = [ "buildings", "postgresql", "planet_osm_polygons", "postgis" ]
aliases = [ "/questions/63045" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Just loading planet_osm_polygons to PostGIS](/questions/63045/just-loading-planet_osm_polygons-to-postgis)

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
<span id="post-63045-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63045-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63045-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all,</p>
<p>Slightly similar to another question I've already asked, but I think it deserved it's own thread. I am running the below to import a Europe PBF to PostGIS. But I actually only need the building polygons (planet_osm_polygons). Is there a way to only import that table and skip the others? (and would doing so have a detrimental effect?)</p>
<pre><code>osm2pgsql -d osm_europe --style openstreetmap-carto/openstreetmap-carto.style -U james -H localhost --hstore --slim -G europe-latest.osm.pbf</code></pre>
<p>I've seen some examples of doing this using osmosis I think, but I've struggled getting that running, so think I'd like to stick to osm2pgsql . I guess I can always delete the tables I don't need afterwards, but it'd be nice to not import them in the first place.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-buildings" rel="tag" title="see questions tagged &#39;buildings&#39;">buildings</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-planet_osm_polygons" rel="tag" title="see questions tagged &#39;planet_osm_polygons&#39;">planet_osm_polygons</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Apr '18, 10:19</strong></p>
<img src="https://secure.gravatar.com/avatar/f05b22ddc881f05935a5416414825f5f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TheRealJimShady&#39;s gravatar image" />
<p><span>TheRealJimShady</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TheRealJimShady has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-63045" class="comments-container">
&#10;</div>
<div id="comment-tools-63045" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63045-form-container" class="comment-form-container">
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

<span id="63413"></span>

<div id="answer-container-63413" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63413-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63413-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63413-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Perhaps could you appky tge blackhole_fdw triggers from Andrew Dunstan <a href="https://bitbucket.org/adunstan/blackhole_fdw">https://bitbucket.org/adunstan/blackhole_fdw</a> and use the --append option.</p>
<p>Or else, if you decide to modify osm2pgsl, there are only 4 or 5 lines of code to comment.</p>
<p>Note that there are also 7 to 8000 (geo-) lines with the correct buildings tags.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 May '18, 02:25</strong></p>
<img src="https://secure.gravatar.com/avatar/1c90056dece0313061d8ce6edd94da8a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AntaC&#39;s gravatar image" />
<p><span>AntaC</span><br />
<span class="score" title="13 reputation points">13</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AntaC has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-63413" class="comments-container">
&#10;</div>
<div id="comment-tools-63413" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63413-form-container" class="comment-form-container">
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


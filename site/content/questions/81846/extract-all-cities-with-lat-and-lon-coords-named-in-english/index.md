+++
type = "question"
title = "Extract all cities with lat and lon coords named in English"
description = '''I need to extract all cities with lat lon coords from Czech Republic OSM with English names of suburb and cities. This is how I imported OSM file downloaded from Geofabrik: osm2pgsql --slim --username postgres --database gis --hstore clech-rebublic-latest.osm psql -U postgres -d gis CREATE EXTENSION...'''
date = "2021-09-21T16:13:00Z"
lastmod = "2021-09-22T08:20:00Z"
weight = 81846
keywords = [ "postgres", "postgis", "osm2pgsql" ]
aliases = [ "/questions/81846" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Extract all cities with lat and lon coords named in English](/questions/81846/extract-all-cities-with-lat-and-lon-coords-named-in-english)

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
<span id="post-81846-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81846-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81846-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I need to extract all cities with lat lon coords from Czech Republic OSM with English names of suburb and cities.</p>
<p>This is how I imported OSM file downloaded from Geofabrik:</p>
<pre><code>osm2pgsql --slim --username postgres --database gis --hstore clech-rebublic-latest.osm
psql -U postgres -d gis
CREATE EXTENSION hstore;</code></pre>
<p>Import went without errors.</p>
<p>Then I used this 2 queries to extract lat lon coords and names of suburb and cities:</p>
<pre><code>SELECT name, st_astext(st_transform(way, 4326)) FROM planet_osm_point WHERE place=&#39;city&#39; OR place=&#39;town&#39; ORDER BY name;</code></pre>
<p>Example:</p>
<pre><code>st_astext,name
POINT(12.3669594982785 50.1246967948147),Aleje-Zátiší
POINT(12.7287439982281 50.4273214948056),Altstadt
POINT(15.5997642978285 49.467412494836),Antonínův Důl</code></pre>
<p>It's all done well, but I got only names on Czech language. How to get the same list but with English names of suburb and cities?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-postgres" rel="tag" title="see questions tagged &#39;postgres&#39;">postgres</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Sep '21, 16:13</strong></p>
<img src="https://secure.gravatar.com/avatar/1aeb86ca63b3378f4f80751ca910ec2e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="akulin&#39;s gravatar image" />
<p><span>akulin</span><br />
<span class="score" title="21 reputation points">21</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="akulin has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Sep '21, 12:39</strong> </span></p>
</div>
</div>
<div id="comments-container-81846" class="comments-container">
&#10;</div>
<div id="comment-tools-81846" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81846-form-container" class="comment-form-container">
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

<span id="81847"></span>

<div id="answer-container-81847" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81847-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81847-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-81847-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="akulin has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You have not imported the English names into your database.</p>
<p>You will need to either modify the "style file" that comes with osm2pgsql to load the <code>name:en</code> tag into the database, or use the <code>--hstore</code> flag on import which will create an additional column called "tags" that contains the additional data.</p>
<p>Then you can select <code>"name:en"</code> respectively <code>tags-&gt;'name:en'</code> instead of <code>name</code> and work with that.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Sep '21, 16:37</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-81847" class="comments-container">
<span id="81851"></span>
<div id="comment-81851" class="comment">
<div id="post-81851-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Akuli, please also keep in mind that not all places you are looking for will have a <code>name:en</code> tag (actually, I believe only few will have). Depending on your use case you may need to have fallback to the <code>name</code> tag. Another way would be to check if there is a <code>wikidata</code> tag and look up an English name on Wikidata (outside your existing workflow).</p>
</div>
<div id="comment-81851-info" class="comment-info">
<span class="comment-age">(22 Sep '21, 08:20)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
</div>
<div id="comment-tools-81847" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81847-form-container" class="comment-form-container">
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


+++
type = "question"
title = "Places not found, can&#x27;t use reverse geocoding API"
description = '''Hi ! I&#x27;ve tried to setup my own Nominatim reverse geocoding server and I&#x27;ve come into some issues. I&#x27;ve resolved some of them myselves but I&#x27;m stuck at the API fetching in reverse geocoding. Apparently, the database is incomplete because it throws me an error at my root access (localhost/) and rever...'''
date = "2020-04-06T13:48:00Z"
lastmod = "2020-04-09T15:17:00Z"
weight = 74027
keywords = [ "api", "reversegeocoding", "nominatim", "geocoding", "osm" ]
aliases = [ "/questions/74027" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Places not found, can't use reverse geocoding API](/questions/74027/places-not-found-cant-use-reverse-geocoding-api)

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
<span id="post-74027-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74027-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74027-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi !</p>
<p>I've tried to setup my own Nominatim reverse geocoding server and I've come into some issues. I've resolved some of them myselves but I'm stuck at the API fetching in reverse geocoding. Apparently, the database is incomplete because it throws me an error at my root access (localhost/) and reverse geocoding isn't working as it's throwing that the place couldn't be found.</p>
<p>I've poked around the databse and places hasn't been found in the tables. Here is the logs :</p>
<pre><code>root@ns39147:/home/nominatim-docker# curl &quot;http://localhost:7070/&quot;</code></pre>
<p>&lt;!DOCTYPE html&gt; &lt;html lang="en"&gt; &lt;head&gt; &lt;style&gt; em { font-weight: bold; font-family: monospace; color: #e00404; background-color: #ffeaea; } &lt;/style&gt; &lt;/head&gt; &lt;body&gt;</p>
<h1 id="internal-server-error">Internal Server Error</h1>
<pre><code>    &lt;p&gt;Nominatim has encountered an internal error while accessing the database.
       This may happen because the database is broken or because of a bug in
       the software.&lt;/p&gt;
&#10;
&#10;&lt;h3&gt;Details&lt;/h3&gt;
&#10;Database query failed
&#10;&lt;p&gt;
    If you feel this error is incorrect feel file an issue on
    &lt;a href=&quot;https://github.com/openstreetmap/Nominatim/issues&quot;&gt;Github&lt;/a&gt;.
&#10;    Please include the error message above and the URL you used.
&lt;/p&gt;</code></pre>
<p>&lt;/body&gt; &lt;/html&gt;</p>
<pre><code>postgres=# \c nominatim
You are now connected to database &quot;nominatim&quot; as user &quot;postgres&quot;.
nominatim=# \dt
               List of relations
 Schema |       Name        | Type  |   Owner
--------+-------------------+-------+-----------
 public | country_name      | table | nominatim
 public | country_osm_grid  | table | nominatim
 public | gb_postcode       | table | nominatim
 public | place_boundingbox | table | nominatim
 public | spatial_ref_sys   | table | nominatim
 public | us_postcode       | table | nominatim
(6 rows)</code></pre>
<p>For info I'm using <a href="https://github.com/mediagis/nominatim-docker">nominatim-docker from mediagis</a> 3.4 which uses postgres 11 and postgis 2.5. The OSM files I've used are from geofabrik : Nord-pas-de-calais (a region of France), Monaco, and Finland. All don't work.</p>
<p>My question is : what am I missing to get the reverse geocoding API to work ?</p>
<p>Thanks for your help :)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-reversegeocoding" rel="tag" title="see questions tagged &#39;reversegeocoding&#39;">reversegeocoding</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-geocoding" rel="tag" title="see questions tagged &#39;geocoding&#39;">geocoding</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Apr '20, 13:48</strong></p>
<img src="https://secure.gravatar.com/avatar/b592d323e79d66fcd8f66c5ab17f62ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nominageek&#39;s gravatar image" />
<p><span>Nominageek</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nominageek has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-74027" class="comments-container">
<span id="74029"></span>
<div id="comment-74029" class="comment">
<div id="post-74029-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I can't help you solve the issue but I can tell you that a \dt on a proper Nominatim database will yield hundreds of tables, most importantly among them a table called <code>placex</code> which contains most OSM data. This means something has not worked during your data import process.</p>
</div>
<div id="comment-74029-info" class="comment-info">
<span class="comment-age">(06 Apr '20, 14:10)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="74030"></span>
<div id="comment-74030" class="comment">
<div id="post-74030-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the info ! I hope I'll be able to solve this issue</p>
</div>
<div id="comment-74030-info" class="comment-info">
<span class="comment-age">(06 Apr '20, 14:19)</span> <span class="comment-user userinfo">Nominageek</span>
</div>
</div>
</div>
<div id="comment-tools-74027" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74027-form-container" class="comment-form-container">
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

<span id="74075"></span>

<div id="answer-container-74075" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74075-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74075-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-74075-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Nominageek has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This was resolved in <a href="https://github.com/mediagis/nominatim-docker/issues/110">https://github.com/mediagis/nominatim-docker/issues/110</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Apr '20, 15:17</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-74075" class="comments-container">
&#10;</div>
<div id="comment-tools-74075" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74075-form-container" class="comment-form-container">
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


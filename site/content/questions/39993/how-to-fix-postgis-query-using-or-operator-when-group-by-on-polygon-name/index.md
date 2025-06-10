+++
type = "question"
title = "How to fix postgis query using &#x27;or&#x27; operator when group by on polygon name"
description = '''I have installed openstreetmap postgis database using .osm file for Scotland using osm2pgsql. I have also imported a set of polygons of parliamentary constituencies in Scotland called &#x27;area10&#x27; I want to find out how much cycle path distance is within each constituency. If I run this query: SELECT  m...'''
date = "2015-01-03T10:44:00Z"
lastmod = "2015-01-03T11:47:00Z"
weight = 39993
keywords = [ "query", "postgresql", "polygon", "postgis", "or_operator" ]
aliases = [ "/questions/39993" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to fix postgis query using 'or' operator when group by on polygon name](/questions/39993/how-to-fix-postgis-query-using-or-operator-when-group-by-on-polygon-name)

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
<span id="post-39993-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-39993-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-39993-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have installed openstreetmap postgis database using .osm file for Scotland using osm2pgsql.</p>
<p>I have also imported a set of polygons of parliamentary constituencies in Scotland called 'area10'</p>
<p>I want to find out how much cycle path distance is within each constituency.</p>
<p>If I run this query:</p>
<p><code>SELECT m.name, sum(ST_Length(r.way))/1000 as roads_km FROM planet_osm_line r, area10 m WHERE ST_Contains(m.way,r.way) AND r.highway = 'cycleway' OR r.highway = 'path' AND bicycle = 'yes' GROUP BY m.name</code></p>
<p>The query runs indefinitely or at least for 45mins or so until my computer overheats but that is another issue...</p>
<p>If I run this query (without 'OR' operator):</p>
<p><code>SELECT m.name, sum(ST_Length(r.way))/1000 as roads_km FROM planet_osm_line r, area10 m WHERE ST_Contains(m.way,r.way) AND r.highway in ('cycleway','path') GROUP BY m.name</code></p>
<p>This returns within about 30 seconds:</p>
<p>`name | roads_km</p>
<ul>
<li>Mid Fife and Glenrothes P Const | 87.17134</li>
<li>Glasgow Provan P Const | 19.11762</li>
<li>Eastwood P Const | 19.97493`</li>
</ul>
<p>...</p>
<p><strong>Question:</strong> So why does using the OR operator in the WHERE clause greatly increase the time of the query? I really need to use the OR operator as there are lots of different highway= tags which I would like to include:</p>
<p><code>OR highway = 'path' AND bicycle = 'designated' OR highway = 'footway' AND bicycle = 'designated' OR highway='footway' AND bicycle = 'yes'</code></p>
<p>etc</p>
<p>I have also tried a similar query using the h-store tag values with the same issue.</p>
<p>Any help very much appreciated. Thank you.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-polygon" rel="tag" title="see questions tagged &#39;polygon&#39;">polygon</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span> <span class="post-tag tag-link-or_operator" rel="tag" title="see questions tagged &#39;or_operator&#39;">or_operator</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Jan '15, 10:44</strong></p>
<img src="https://secure.gravatar.com/avatar/aefd12236ce046b3929cb63fca818119?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hawkeye&#39;s gravatar image" />
<p><span>Hawkeye</span><br />
<span class="score" title="241 reputation points">241</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hawkeye has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Jan '15, 11:59</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-39993" class="comments-container">
&#10;</div>
<div id="comment-tools-39993" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-39993-form-container" class="comment-form-container">
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

<span id="39994"></span>

<div id="answer-container-39994" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-39994-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-39994-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-39994-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Hawkeye has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You have your parentheses wrong. Try</p>
<pre><code>WHERE ST_Contains(m.way,r.way) AND 
   (r.highway = &#39;cycleway&#39; OR (r.highway = &#39;path&#39; AND bicycle = &#39;yes&#39;))
GROUP BY m.name</code></pre>
<p>Also, you might want to do something like</p>
<pre><code>ST_Length(r.way::geography)</code></pre>
<p>to actually get the length in metres instead of Google Mercator units which are not exactly metres.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Jan '15, 10:58</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-39994" class="comments-container">
<span id="39999"></span>
<div id="comment-39999" class="comment">
<div id="post-39999-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Thank you! It's working:</p>
<p><code>SELECT m.name, sum(ST_Length(ST_Transform(r.way,4326)::geography))/1000 as roads_km FROM planet_osm_line r, area10 m WHERE ST_Contains(m.way,r.way) AND (r.highway = 'cycleway' OR (r.highway = 'path' AND bicycle = 'yes')) GROUP BY m.name</code></p>
</div>
<div id="comment-39999-info" class="comment-info">
<span class="comment-age">(03 Jan '15, 11:47)</span> <span class="comment-user userinfo">Hawkeye</span>
</div>
</div>
</div>
<div id="comment-tools-39994" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-39994-form-container" class="comment-form-container">
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


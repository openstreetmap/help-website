+++
type = "question"
title = "How to set srid of a single point coordinates pair using PostGis?"
description = '''I think is better explain with a small example: selected a geometry point i get it back in a coordinates pair SELECT ST_AsGeoJSON(&#x27;010100002031BF0D009A999919F9BD2D41CDCCCC4C758E5241&#x27;) --result: &quot;{&quot;type&quot;:&quot;Point&quot;,&quot;coordinates&quot;:[974588.55,4864469.2]}&quot;  to return back the geometry simply i make SELECT S...'''
date = "2015-08-22T20:11:00Z"
lastmod = "2015-08-23T18:14:00Z"
weight = 44875
keywords = [ "pgrouting", "postgresql", "postgis" ]
aliases = [ "/questions/44875" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to set srid of a single point coordinates pair using PostGis?](/questions/44875/how-to-set-srid-of-a-single-point-coordinates-pair-using-postgis)

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
<span id="post-44875-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44875-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-44875-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I think is better explain with a small example: selected a geometry point i get it back in a coordinates pair</p>
<pre><code>SELECT ST_AsGeoJSON(&#39;010100002031BF0D009A999919F9BD2D41CDCCCC4C758E5241&#39;)
--result:
&quot;{&quot;type&quot;:&quot;Point&quot;,&quot;coordinates&quot;:[974588.55,4864469.2]}&quot;</code></pre>
<p>to return back the geometry simply i make</p>
<pre><code>SELECT ST_GeometryFromText(&#39;POINT(974588.55 4864469.2)&#39;)</code></pre>
<p>having for example the same pair of geographic coordinates in degrees</p>
<pre><code>coordinates:[9.7458855,48.644692]}</code></pre>
<p>How can i transform them into the previous pair format and get the starting geometry?</p>
<p>I'm working with leaflet and i would implement a kind of routing service using pgRouting, I have populated postgis with "osm2pgsql" tool and all geometries are of 900913 SRID type. My goal is to compare the source and target points on a map with the vertices stored in postgres. Applying a transformation on a point picked from the map to 900913 srid don't get me the right thing, also i notice that the last four numbers (5241) are the same for each geometry in the db and them are different when i transform the geometry returned from my point, what they refer?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-pgrouting" rel="tag" title="see questions tagged &#39;pgrouting&#39;">pgrouting</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Aug '15, 20:11</strong></p>
<img src="https://secure.gravatar.com/avatar/2dc2dce97c04e173e2dd1e0bee21edcc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gaia&#39;s gravatar image" />
<p><span>gaia</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gaia has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Aug '15, 23:13</strong> </span></p>
</div>
</div>
<div id="comments-container-44875" class="comments-container">
<span id="44880"></span>
<div id="comment-44880" class="comment">
<div id="post-44880-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>This question is not really on topic, it's more a general GIS question.</p>
</div>
<div id="comment-44880-info" class="comment-info">
<span class="comment-age">(23 Aug '15, 09:59)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="44882"></span>
<div id="comment-44882" class="comment">
<div id="post-44882-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I thought there was some special function of osm2pgsql, is osm2pgsql on topic with the forum?</p>
</div>
<div id="comment-44882-info" class="comment-info">
<span class="comment-age">(23 Aug '15, 12:36)</span> <span class="comment-user userinfo">gaia</span>
</div>
</div>
<span id="44884"></span>
<div id="comment-44884" class="comment">
<div id="post-44884-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You can change the SRID used by osm2pgsql too, but the question focussed on changing SRID with leaflet, pg_routing and already populated db.</p>
</div>
<div id="comment-44884-info" class="comment-info">
<span class="comment-age">(23 Aug '15, 18:14)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-44875" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44875-form-container" class="comment-form-container">
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

<span id="44881"></span>

<div id="answer-container-44881" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44881-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44881-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-44881-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="gaia has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The two functions you want are ST_SRID and ST_SetSRID.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Aug '15, 10:00</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-44881" class="comments-container">
<span id="44883"></span>
<div id="comment-44883" class="comment">
<div id="post-44883-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>yes, i solved setting first the srid of the coordinates and only then applying a transformation</p>
</div>
<div id="comment-44883-info" class="comment-info">
<span class="comment-age">(23 Aug '15, 12:40)</span> <span class="comment-user userinfo">gaia</span>
</div>
</div>
</div>
<div id="comment-tools-44881" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44881-form-container" class="comment-form-container">
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


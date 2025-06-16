+++
type = "question"
title = "Get city borders for Finland"
description = '''I want to extract city specific data from OSM for Finland. I have the data for Finland but I need the data for only 5 cities: Helsinki, Espoo, Vantaa, Kauniainen and Siuntio. I could extract the required data for Helsinki, but I need the city borders for the rest of the cities (so I can make a polyg...'''
date = "2013-01-25T09:47:00Z"
lastmod = "2013-01-26T22:37:00Z"
weight = 19336
keywords = [ "osm", "xapi", "gis", "overpass" ]
aliases = [ "/questions/19336" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Get city borders for Finland](/questions/19336/get-city-borders-for-finland)

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
<span id="post-19336-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19336-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-19336-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to extract city specific data from OSM for Finland. I have the data for Finland but I need the data for only 5 cities: Helsinki, Espoo, Vantaa, Kauniainen and Siuntio. I could extract the required data for Helsinki, but I need the city borders for the rest of the cities (so I can make a polygon of that). If I have the polygons I can extract the required data with osmconvert.</p>
<p>Can you help me with information on how to extract the borders for these cities?</p>
<p>Do you know any open api that provides me these information?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-xapi" rel="tag" title="see questions tagged &#39;xapi&#39;">xapi</span> <span class="post-tag tag-link-gis" rel="tag" title="see questions tagged &#39;gis&#39;">gis</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Jan '13, 09:47</strong></p>
<img src="https://secure.gravatar.com/avatar/688961ce6878210d40cac05f6163a5e9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bgergo0826&#39;s gravatar image" />
<p><span>bgergo0826</span><br />
<span class="score" title="14 reputation points">14</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bgergo0826 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-19336" class="comments-container">
&#10;</div>
<div id="comment-tools-19336" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19336-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="19338"></span>

<div id="answer-container-19338" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-19338-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19338-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-19338-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="bgergo0826 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Please have a look at question <a href="/questions/8273/how-do-i-extract-the-polygon-of-an-administrative-boundary">this question</a>:</p>
<p>You can download the full boundary with <a href="http://overpass-api.de/api/interpreter?data=(rel%5Bname=&#39;Helsinki&#39;%5D;%3E;);out;">http://overpass-api.de/api/interpreter?data=(rel[name='Helsinki'];&gt;;);out;</a> and then convert the return value with <a href="http://svn.openstreetmap.org/applications/utils/osm-extract/polygons/rel2poly.pl">http://svn.openstreetmap.org/applications/utils/osm-extract/polygons/rel2poly.pl</a> into a polygon.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Jan '13, 11:57</strong></p>
<img src="https://secure.gravatar.com/avatar/fcfdb0825826fd13d2ff0d83d58819c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland%20Olbricht&#39;s gravatar image" />
<p><span>Roland Olbricht</span><br />
<span class="score" title="6666 reputation points"><span>6.7k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland Olbricht has 40 accepted answers">36%</span></p>
</div>
</div>
<div id="comments-container-19338" class="comments-container">
<span id="19370"></span>
<div id="comment-19370" class="comment">
<div id="post-19370-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Again this will not work for Esbo, since it is a multipolygon and rel2poly doesn't support that..</p>
</div>
<div id="comment-19370-info" class="comment-info">
<span class="comment-age">(26 Jan '13, 22:37)</span> <span class="comment-user userinfo">emj</span>
</div>
</div>
</div>
<div id="comment-tools-19338" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19338-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="19337"></span>

<div id="answer-container-19337" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-19337-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19337-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-19337-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are several things about borders and tools that you have to think about.</p>
<ol>
<li>you will often end up with cut off data on the borders</li>
<li>borders in OSM are seldom perfect</li>
<li>you can import the borders and base your analysis on that, if you need exact borders.</li>
</ol>
<p>So do like the venerable <a href="http://metro.teczno.com/">metro extracts</a> and draw your own bounding boxes for extraction and if it is important to only get specific data inside Esbo you can use pgsql to do that.</p>
<p>You can see these polygons on Nominatim, and if you really want them you can cut and paste from HTML, but it will give and over view of what exactly you are getting instead of blindly copying from Overpass. Here are some examples, search for the rest on <a href="http://nominatim.osm.org">http://nominatim.osm.org</a></p>
<ul>
<li><a href="http://nominatim.openstreetmap.org/details.php?place_id=98136565">Vantaa</a></li>
<li><a href="http://nominatim.openstreetmap.org/details.php?place_id=97761941">Helsingfors</a></li>
<li><a href="http://nominatim.openstreetmap.org/details.php?place_id=98136672">Esbo</a></li>
</ul>
<p>You can copy the polygon from the javascript of those pages:</p>
<pre><code>        var feature = freader.read(&#39;POLYGON((
...
),(
...
))</code></pre>
<p>Note that Esbo is a multipolygon, can osmconvert handle that?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Jan '13, 11:38</strong></p>
<img src="https://secure.gravatar.com/avatar/dd3858f5f89f5a6b738f9dbe59824440?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="emj&#39;s gravatar image" />
<p><span>emj</span><br />
<span class="score" title="2024 reputation points"><span>2.0k</span></span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="emj has 11 accepted answers">15%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Jan '13, 22:54</strong> </span></p>
</div>
</div>
<div id="comments-container-19337" class="comments-container">
&#10;</div>
<div id="comment-tools-19337" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19337-form-container" class="comment-form-container">
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


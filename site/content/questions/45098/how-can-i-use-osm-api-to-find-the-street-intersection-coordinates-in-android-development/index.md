+++
type = "question"
title = "How Can I use OSM API to find the street intersection coordinates in android development?"
description = '''I want to create an android project about street intersections! Like I choose a street name, starting point and the radius. Then the program gives me an array of the The streets that cross that one in that radius as a list of street names in another list activity. When I choose one of the streets I ...'''
date = "2015-09-07T11:52:00Z"
lastmod = "2015-09-12T13:54:00Z"
weight = 45098
keywords = [ "intersection", "points" ]
aliases = [ "/questions/45098" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How Can I use OSM API to find the street intersection coordinates in android development?](/questions/45098/how-can-i-use-osm-api-to-find-the-street-intersection-coordinates-in-android-development)

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
<span id="post-45098-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45098-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-45098-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to create an android project about street intersections! Like I choose a street name, starting point and the radius. Then the program gives me an array of the The streets that cross that one in that radius as a list of street names in another list activity. When I choose one of the streets I want to be redirected to the map at their intersection point. So how can I use a openStreetMap API.To create this? Any suggestions are pleased.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-intersection" rel="tag" title="see questions tagged &#39;intersection&#39;">intersection</span> <span class="post-tag tag-link-points" rel="tag" title="see questions tagged &#39;points&#39;">points</span>
</div>
<div id="question-controls" class="post-controls">
<div class="community-wiki">
This question is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Sep '15, 11:52</strong></p>
<img src="https://secure.gravatar.com/avatar/e59db41fb4c0996e512149db6cfbb7d4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AzaWiza&#39;s gravatar image" />
<p><span>AzaWiza</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AzaWiza has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-45098" class="comments-container">
&#10;</div>
<div id="comment-tools-45098" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45098-form-container" class="comment-form-container">
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

<span id="45112"></span>

<div id="answer-container-45112" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-45112-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45112-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-45112-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Except in a very loose way, the answer is no. The OSM API is primarly for editing OSM data and doesn't do very much outside of providing you with the data for a specific region.</p>
<p>The <a href="http://wiki.openstreetmap.org/wiki/Overpass_API">Overpass API</a> provides more in the way of advanced queries, but I suspect your requirements will require loading OSM data in to a geo-aware database (for example Postgres with the PostGIS extension) and performing the corresponding spatial queries yourself. Before you do that you should read up on the OSM data model and the various possible database schemas.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Sep '15, 08:36</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-45112" class="comments-container">
<span id="45151"></span>
<div id="comment-45151" class="comment">
<div id="post-45151-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That is exactly what I was Looking for! Thank you! Are there any way to send a query to overpass turbo from an android device? Like Now I have OSM map on my android devidce. by choosing a specia area there, Can I write a query in getText field like this one<br />
"[bbox:{{bbox}}];<br />
way[highway][name="Юнусалиева Болота проспект"];node(w)-&gt;.n1;<br />
way[highway][name="Скрябина улица"];<br />
node(w)-&gt;.n2; node.n1.n2;<br />
out meta; "<br />
<br />
ANd get the result of the query in txt format. like this<br />
<br />
[bbox:42.84342093245924,74.60618019104004,42.85234094569768,74.63012695312499];<br />
way[highway][name="Юнусалиева Болота проспект"];node(w)-&gt;.n1;<br />
way[highway][name="Скрябина улица"];node(w)-&gt;.n2;<br />
node.n1.n2;<br />
out meta;</p>
</div>
<div id="comment-45151-info" class="comment-info">
<span class="comment-age">(10 Sep '15, 03:21)</span> <span class="comment-user userinfo">AzaWiza</span>
</div>
</div>
<span id="45154"></span>
<div id="comment-45154" class="comment">
<div id="post-45154-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Sure, this is possible. Just send a corresponding HTTP request and parse the response. See the various examples in the <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Language_Guide">Overpass API language guide</a>.</p>
</div>
<div id="comment-45154-info" class="comment-info">
<span class="comment-age">(10 Sep '15, 07:43)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="45206"></span>
<div id="comment-45206" class="comment">
<div id="post-45206-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You should mind your terminology though. Overpass Turbo is a website build around Overpass API which just makes it easier to write queries. A bit like an IDE build around a compiler. Overpass API is one of the public instances that you can call via HTTP requests. However, Overpass API may also refer to the open-source software used to power the public instances.</p>
</div>
<div id="comment-45206-info" class="comment-info">
<span class="comment-age">(12 Sep '15, 11:48)</span> <span class="comment-user userinfo">Sanderd17</span>
</div>
</div>
<span id="45207"></span>
<div id="comment-45207" class="comment">
<div id="post-45207-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/280/sanderd17"></a><a href="http://help.openstreetmap.org/users/280/sanderd17">@Sanderd17</a>:</p>
<blockquote>
<p>Overpass API is one of the public instances that you can call via HTTP requests.</p>
</blockquote>
<p>Did you perhaps mean: <a href="http://overpass-api.de/">overpass-api.de</a> is one of the public Overpass API instances (in fact it's the <em>main instance</em>) that you can call via HTTP requests? Some of the other public instances are listed <a href="https://wiki.openstreetmap.org/wiki/Overpass_API#Introduction">here</a>.</p>
</div>
<div id="comment-45207-info" class="comment-info">
<span class="comment-age">(12 Sep '15, 13:54)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
</div>
<div id="comment-tools-45112" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45112-form-container" class="comment-form-container">
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


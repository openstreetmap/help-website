+++
type = "question"
title = "marking more than one way"
description = '''Hi! I found some links like: http://www.openstreetmap.org/?way=273332264  which mark a part of a street. So I was wondering how to mark the whole street or maybe several streets and I found in the wiki: Get way by ID - which describes what I get from the above url, because when it is entered in the ...'''
date = "2014-12-19T09:45:00Z"
lastmod = "2014-12-19T12:32:00Z"
weight = 39714
keywords = [ "ways", "marker" ]
aliases = [ "/questions/39714" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [marking more than one way](/questions/39714/marking-more-than-one-way)

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
<span id="post-39714-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-39714-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-39714-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi!</p>
<p>I found some links like:</p>
<pre><code>http://www.openstreetmap.org/?way=273332264</code></pre>
<p>which mark a part of a street. So I was wondering how to mark the whole street or maybe several streets and I found in the wiki:</p>
<p>Get way by ID - which describes what I get from the above url, because when it is entered in the browser it's rewritten by the server to</p>
<pre><code>http://www.openstreetmap.org/way/273332264</code></pre>
<p>I looked further and found</p>
<p>Get ways describing the url as being</p>
<pre><code>/ways?ways=id1,id2,id3...</code></pre>
<p>But I couldn't figure out how to apply this to "my" street which would be</p>
<pre><code>http://www.openstreetmap.org/ways?ways=273332264,273332263,33527209,142030348,33239773,22889305,273332262,190065022,273332252,257255152,273332271,273332270,273332266,208884097,129032431,273332260,273332259,273332269,273332265,273332261,273332267,273332258,273332268</code></pre>
<p>Unfortunately this did not work as expected. Is there another way to get this accomplished?</p>
<p>There is alsready a kind soul in Germany who set up a server which allows this (plus more), but I'd also like to know how this would be possible directly on openstreetmaps.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span> <span class="post-tag tag-link-marker" rel="tag" title="see questions tagged &#39;marker&#39;">marker</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Dec '14, 09:45</strong></p>
<img src="https://secure.gravatar.com/avatar/9dee2e9d5d58bbfbb91dc20ac401da3b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="5keeve&#39;s gravatar image" />
<p><span>5keeve</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="5keeve has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-39714" class="comments-container">
<span id="39715"></span>
<div id="comment-39715" class="comment not_top_scorer">
<div id="post-39715-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Can you provide a little bit more information? Where did you read about <em>/ways?ways=id1,id2,id3...</em>? Which server are you talking about already supports this? And why do you want to display multiple ways on openstreetmap.org directly?</p>
</div>
<div id="comment-39715-info" class="comment-info">
<span class="comment-age">(19 Dec '14, 09:56)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="39718"></span>
<div id="comment-39718" class="comment">
<div id="post-39718-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>As a general question, I think that it's quite a good one - "Euskirchener Straße" I suspect has a logical beginning and an end that encompass many OSM ways (split because of different other tags). Most such streets won't be tied together by a relation, so a "name search based on bounding box" would be needed - but how to know how big to make the bounding box? It's like the "graph" questions that sometimes get asked here, in reverse.</p>
</div>
<div id="comment-39718-info" class="comment-info">
<span class="comment-age">(19 Dec '14, 11:11)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="39720"></span>
<div id="comment-39720" class="comment">
<div id="post-39720-score" class="comment-score">
2
</div>
<div class="comment-text">
<blockquote>
<p>Where did you read about /ways?ways=id1,id2,id3...</p>
</blockquote>
<p>Sorry! Completely forgot to give the link. <a href="http://wiki.openstreetmap.org/wiki/API_v0.4#Get_ways">http://wiki.openstreetmap.org/wiki/API_v0.4#Get_ways</a></p>
<blockquote>
<p>Which server are you talking about already supports this?</p>
</blockquote>
<p>No clue. Just read it in the documentation and found the similarity to the first link I gave.</p>
<blockquote>
<p>And why do you want to display multiple ways on openstreetmap.org directly?</p>
</blockquote>
<p>To get an overview. I need to prepare a children's charity project here in Germany for January and so wanted to plot the streets I assigned to the groups.</p>
</div>
<div id="comment-39720-info" class="comment-info">
<span class="comment-age">(19 Dec '14, 11:48)</span> <span class="comment-user userinfo">5keeve</span>
</div>
</div>
<span id="39721"></span>
<div id="comment-39721" class="comment">
<div id="post-39721-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Regarding searching for a street: That wasn't really my issue as I already have a good list of the ways belonging to the streets</p>
<pre><code>http://regio-osm.de/listofstreets/evaluation?title=D%C3%BCren&amp;country=Bundesrepublik%20Deutschland</code></pre>
<p>The issue is more of visualizing (a group of) streets.</p>
<p>Judging from the API documentation I thought I found a way - but it seems to be not supported :(</p>
</div>
<div id="comment-39721-info" class="comment-info">
<span class="comment-age">(19 Dec '14, 11:48)</span> <span class="comment-user userinfo">5keeve</span>
</div>
</div>
<span id="39722"></span>
<div id="comment-39722" class="comment">
<div id="post-39722-score" class="comment-score">
4
</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/10202/5keeve">@5keeve</a> that's actually quite an old version of the API; try looking at <a href="http://wiki.openstreetmap.org/wiki/API_v0.6">http://wiki.openstreetmap.org/wiki/API_v0.6</a> (or more likely, other services such as Overpass)</p>
</div>
<div id="comment-39722-info" class="comment-info">
<span class="comment-age">(19 Dec '14, 12:13)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="39723"></span>
<div id="comment-39723" class="comment not_top_scorer">
<div id="post-39723-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Did so:</p>
<p><a href="http://wiki.openstreetmap.org/wiki/API_v0.6#Multi_fetch:">http://wiki.openstreetmap.org/wiki/API_v0.6#Multi_fetch:</a><em>GET</em>.2Fapi.2F0.6.2F.5Bnodes.7Cways.7Crelations.5D.3F.23parameters</p>
<p>Looks the same</p>
<pre><code>.../ways?ways=id1,id2,...</code></pre>
</div>
<div id="comment-39723-info" class="comment-info">
<span class="comment-age">(19 Dec '14, 12:27)</span> <span class="comment-user userinfo">5keeve</span>
</div>
</div>
<span id="39724"></span>
<div id="comment-39724" class="comment">
<div id="post-39724-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Besides having looked at the wrong API version: This is really just the API and not the website documentation. Moreover for visualizing you should not use the website directly but instead some framework such as Leaflet or OpenLayers. It is also possible that uMap will suit your needs.</p>
<p><em>edit:</em></p>
<p>It <em>does</em> work, but just for the <em>API</em> calls which just return raw data without visualization. See this working example: <a href="http://www.openstreetmap.org/api/0.6/ways?ways=1234,2345">http://www.openstreetmap.org/api/0.6/ways?ways=1234,2345</a></p>
</div>
<div id="comment-39724-info" class="comment-info">
<span class="comment-age">(19 Dec '14, 12:28)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-39714" class="comment-tools">
<span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-39714-form-container" class="comment-form-container">
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

<span id="39725"></span>

<div id="answer-container-39725" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-39725-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-39725-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-39725-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I guess this <strong>isn't possible</strong> as currently osm.org has just permalinks to basic OSM objects (nodes, ways, relations, notes). Maybe you it's useful to send links of our <strong>geocoder</strong> (Nominatim) instead? For example the mentioned Euskirchener Straße <a href="http://nominatim.openstreetmap.org/details.php?place_id=150696442">http://nominatim.openstreetmap.org/details.php?place_id=150696442</a></p>
<p>But be aware that finding a complete list of street-segements isn't that trivial and AFAIK osm.org website currently has a focus on mappers/contributors and isn't tuned for perfectly satisfaction of consumers ;-)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Dec '14, 12:32</strong></p>
<img src="https://secure.gravatar.com/avatar/49a7d0e0408e9cf2f698faac0f4d837a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iii&#39;s gravatar image" />
<p><span>iii</span><br />
<span class="score" title="4892 reputation points"><span>4.9k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="82 badges"><span class="bronze">●</span><span class="badgecount">82</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iii has 16 accepted answers">10%</span></p>
</div>
</div>
<div id="comments-container-39725" class="comments-container">
&#10;</div>
<div id="comment-tools-39725" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-39725-form-container" class="comment-form-container">
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


+++
type = "question"
title = "Requests limitation and timeout"
description = '''I&#x27;m working on my master thesis for which I need the number of points of interest that can be considered cultural in 43 Italian cities. Basically, what I need is the result of the following query: query = &quot;&quot;&quot; area[name=&quot;&quot;&quot;+city_name+&quot;&quot;&quot;]-&amp;gt;.a; (  node[&quot;amenity&quot;=&quot;college&quot;];  way[&quot;amenity&quot;=&quot;college&quot;...'''
date = "2018-06-24T11:53:00Z"
lastmod = "2018-06-25T12:49:00Z"
weight = 64346
keywords = [ "limitations", "overpass", "requests", "timeout" ]
aliases = [ "/questions/64346" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Requests limitation and timeout](/questions/64346/requests-limitation-and-timeout)

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
<span id="post-64346-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64346-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-64346-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm working on my master thesis for which I need the number of points of interest that can be considered cultural in 43 Italian cities. Basically, what I need is the result of the following query:</p>
<pre><code>query = &quot;&quot;&quot;
area[name=&quot;&quot;&quot;+city_name+&quot;&quot;&quot;]-&gt;.a;
(
  node[&quot;amenity&quot;=&quot;college&quot;];
  way[&quot;amenity&quot;=&quot;college&quot;];
  relation[&quot;amenity&quot;=&quot;college&quot;];
&#10;  node[&quot;amenity&quot;=&quot;library&quot;];
  way[&quot;amenity&quot;=&quot;library&quot;];
  relation[&quot;amenity&quot;=&quot;library&quot;];
&#10;  node[&quot;amenity&quot;=&quot;archive&quot;];
  way[&quot;amenity&quot;=&quot;archive&quot;];
  relation[&quot;amenity&quot;=&quot;archive&quot;];
&#10;  node[&quot;amenity&quot;=&quot;school&quot;];
  way[&quot;amenity&quot;=&quot;school&quot;];
  relation[&quot;amenity&quot;=&quot;school&quot;];
&#10;  node[&quot;amenity&quot;=&quot;music_school&quot;];
  way[&quot;amenity&quot;=&quot;music_school&quot;];
  relation[&quot;amenity&quot;=&quot;music_school&quot;];
&#10;  node[&quot;amenity&quot;=&quot;university&quot;];
  way[&quot;amenity&quot;=&quot;university&quot;];
  relation[&quot;amenity&quot;=&quot;university&quot;];
&#10;  node[&quot;amenity&quot;=&quot;research_institute&quot;];
  way[&quot;amenity&quot;=&quot;research_institute&quot;];
  relation[&quot;amenity&quot;=&quot;research_institute&quot;];
&#10;  node[&quot;amenity&quot;=&quot;arts_centre&quot;];
  way[&quot;amenity&quot;=&quot;arts_centre&quot;];
  relation[&quot;amenity&quot;=&quot;arts_centre&quot;];
&#10;  node[&quot;amenity&quot;=&quot;cinema&quot;];
  way[&quot;amenity&quot;=&quot;cinema&quot;];
  relation[&quot;amenity&quot;=&quot;cinema&quot;];
&#10;  node[&quot;amenity&quot;=&quot;community_centre&quot;];
  way[&quot;amenity&quot;=&quot;community_centre&quot;];
  relation[&quot;amenity&quot;=&quot;community_centre&quot;];
&#10;  node[&quot;amenity&quot;=&quot;arts_centre&quot;];
  way[&quot;amenity&quot;=&quot;arts_centre&quot;];
  relation[&quot;amenity&quot;=&quot;arts_centre&quot;];
&#10;  node[&quot;amenity&quot;=&quot;planetarium&quot;];
  way[&quot;amenity&quot;=&quot;planetarium&quot;];
  relation[&quot;amenity&quot;=&quot;planetarium&quot;];
&#10;  node[&quot;amenity&quot;=&quot;social_centre&quot;];
  way[&quot;amenity&quot;=&quot;social_centre&quot;];
  relation[&quot;amenity&quot;=&quot;social_centre&quot;];
&#10;  node[&quot;amenity&quot;=&quot;studio&quot;];
  way[&quot;amenity&quot;=&quot;studio&quot;];
  relation[&quot;amenity&quot;=&quot;studio&quot;];
&#10;  node[&quot;amenity&quot;=&quot;theatre&quot;];
  way[&quot;amenity&quot;=&quot;theatre&quot;];
  relation[&quot;amenity&quot;=&quot;theatre&quot;];
)
&quot;&quot;&quot;</code></pre>
<p>As you can see, I'm interested in 15 amenities, not a negligible number for a metropolitan area. Despite the chance to set an arbitrary timeout, I faced the limitation of 3 minutes set on the server. Therefore I used the python overpass API to ask one amenity at a time (15 queries for 43 cities), but before finishing the first 43 queries, I received the following response: 'HTTP/1.1 429 Too Many Requests\r\n' I beg your pardon if my actions have been interpreted as a kind of DoS attack, but I would like to know if there is any chance to obtain the information that I need without violeting the policy of the server.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-limitations" rel="tag" title="see questions tagged &#39;limitations&#39;">limitations</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-requests" rel="tag" title="see questions tagged &#39;requests&#39;">requests</span> <span class="post-tag tag-link-timeout" rel="tag" title="see questions tagged &#39;timeout&#39;">timeout</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Jun '18, 11:53</strong></p>
<img src="https://secure.gravatar.com/avatar/b66d324b0705210da2ebe24e3ec2f6dd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GiulioFa&#39;s gravatar image" />
<p><span>GiulioFa</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GiulioFa has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Jun '18, 10:52</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-64346" class="comments-container">
&#10;</div>
<div id="comment-tools-64346" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64346-form-container" class="comment-form-container">
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

<span id="64347"></span>

<div id="answer-container-64347" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64347-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64347-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-64347-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You could simply extract them from a extract of the OSM data for Italy (see <a href="http://download.geofabrik.de/europe/italy.html)">http://download.geofabrik.de/europe/italy.html)</a> for example by using <a href="https://wiki.openstreetmap.org/wiki/Osmfilter">osmfilter</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Jun '18, 12:04</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Jun '18, 12:06</strong> </span></p>
</div>
</div>
<div id="comments-container-64347" class="comments-container">
<span id="64348"></span>
<div id="comment-64348" class="comment">
<div id="post-64348-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for your answer. I'm trying to understand how to extract the number of amenities for each city. I was thinking about two steps: 1) ./osmfilter italy-latest.o5m --keep="amenity=college =cinema ..." 2) ./osmfilter italy-latest.o5m --out-count=addr:city | grep city_name With the first one I should obtain a .o5m file with nodes, ways and relations that match my interests. With the second I expect the number of amenities in that specific city. However, I think that not all the nodes, ways and relations contain the address field. Therefore, how should I automatically limit the area?</p>
</div>
<div id="comment-64348-info" class="comment-info">
<span class="comment-age">(24 Jun '18, 16:22)</span> <span class="comment-user userinfo">GiulioFa</span>
</div>
</div>
<span id="64356"></span>
<div id="comment-64356" class="comment">
<div id="post-64356-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If you are interested in a limited number of areas, I would simply just use extracts for those areas (that you could either get ready mode or extract yourself).</p>
<p>Well actually I wouldn't, because I would simply import the IT extract in to an <a href="https://wiki.openstreetmap.org/wiki/Osm2pgsql">osm2pgsql</a> schema data base and get the the information from spatial queries (assuming that OSM contains boundary polygons for the cities you are interested in).</p>
</div>
<div id="comment-64356-info" class="comment-info">
<span class="comment-age">(25 Jun '18, 12:49)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-64347" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64347-form-container" class="comment-form-container">
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


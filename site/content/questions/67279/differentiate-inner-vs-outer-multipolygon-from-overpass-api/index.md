+++
type = "question"
title = "Differentiate Inner vs Outer multipolygon from Overpass API"
description = '''I&#x27;m making an API request to OSM with a bounding box query. When I&#x27;m getting an object back that&#x27;s a multipolygon, I&#x27;m unclear how I can differentiate if the relation is inner vs outer. I figured that would be included in the API response, but it&#x27;s not. What am I missing? Is there some way I&#x27;m able ...'''
date = "2018-12-19T23:30:00Z"
lastmod = "2018-12-22T19:22:00Z"
weight = 67279
keywords = [ "overpass", "api", "multipolygon" ]
aliases = [ "/questions/67279" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Differentiate Inner vs Outer multipolygon from Overpass API](/questions/67279/differentiate-inner-vs-outer-multipolygon-from-overpass-api)

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
<span id="post-67279-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67279-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-67279-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm making an API request to OSM with a bounding box query.</p>
<p>When I'm getting an object back that's a multipolygon, I'm unclear how I can differentiate if the relation is inner vs outer. I figured that would be included in the API response, but it's not. What am I missing? Is there some way I'm able to differentiate between the two?</p>
<pre><code>{
          &quot;type&quot; =&gt; &quot;Feature&quot;,
            &quot;id&quot; =&gt; &quot;relation/296087&quot;,
    &quot;properties&quot; =&gt; {
               &quot;timestamp&quot; =&gt; &quot;2018-07-14T19:04:53Z&quot;,
                 &quot;version&quot; =&gt; &quot;5&quot;,
               &quot;changeset&quot; =&gt; &quot;60718245&quot;,
                    &quot;user&quot; =&gt; &quot;escallic&quot;,
                     &quot;uid&quot; =&gt; &quot;2110789&quot;,
               &quot;addr:city&quot; =&gt; &quot;Isla Vista&quot;,
             &quot;addr:county&quot; =&gt; &quot;Santa Barbara&quot;,
        &quot;addr:housenumber&quot; =&gt; &quot;6585&quot;,
           &quot;addr:postcode&quot; =&gt; &quot;93117&quot;,
             &quot;addr:street&quot; =&gt; &quot;El Colegio Road&quot;,
                &quot;building&quot; =&gt; &quot;apartments&quot;,
         &quot;building:levels&quot; =&gt; &quot;2&quot;,
                    &quot;name&quot; =&gt; &quot;Tropicana Gardens&quot;,
                    &quot;type&quot; =&gt; &quot;multipolygon&quot;,
                      &quot;id&quot; =&gt; &quot;relation/296087&quot;
    },
      &quot;geometry&quot; =&gt; {
               &quot;type&quot; =&gt; &quot;Polygon&quot;,
        &quot;coordinates&quot; =&gt; [ ..... ]
      }</code></pre>
<p>}</p>
<p><strong>Update</strong> The query I'm using to make the request is below: <a href="http://overpass-api.de/api/map?bbox=-119.86475115542854%2C34.410451138127065%2C-119.85719244457147%2C34.416207261872934"><code>http://overpass-api.de/api/map?bbox=-119.86475115542854%2C34.410451138127065%2C-119.85719244457147%2C34.416207261872934</code></a></p>
<p>I'm then taking the data (XML) and using the npm package OSMToGeoJSON to convert it into JSON. I believe that is where the relation information is being lost, as I see it in the raw XML.</p>
<p>How would one make a query for all data in a bounding box, but request JSON. I tried adding the query param <code>data=[out:json];</code> to my response, but I did not get any data back&gt;</p>
<p>I need the inner/outer data for the polygons, because I am re-drawing these maps. I work on a project where were turn these maps into tactile maps for the blind community. If I don't know whether the polygon is supposed to be inner vs outer, it ends up rendering incorrectly.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-multipolygon" rel="tag" title="see questions tagged &#39;multipolygon&#39;">multipolygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Dec '18, 23:30</strong></p>
<img src="https://secure.gravatar.com/avatar/2bf2921024c31d2d4f66c4b4573f19c5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kida001&#39;s gravatar image" />
<p><span>kida001</span><br />
<span class="score" title="31 reputation points">31</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kida001 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Dec '18, 18:15</strong> </span></p>
</div>
</div>
<div id="comments-container-67279" class="comments-container">
<span id="67286"></span>
<div id="comment-67286" class="comment">
<div id="post-67286-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I doubt you made your query with Overpass, so that tag is somewhat misleading. When I request the relation with id=296087 with <a href="http://overpass-turbo.eu/s/EFb">this Overpass Query</a> there is a section with 'members'.</p>
<p>If you cannot use Overpass for some reason, I don't how how to solve the problem though.</p>
</div>
<div id="comment-67286-info" class="comment-info">
<span class="comment-age">(20 Dec '18, 07:23)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="67287"></span>
<div id="comment-67287" class="comment">
<div id="post-67287-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/5390/escada">@escada</a> I'm sending my bbox query to <a href="http://overpass-api.de/api/map"><code>http://overpass-api.de/api/map</code></a> ... is that not overpass?</p>
</div>
<div id="comment-67287-info" class="comment-info">
<span class="comment-age">(20 Dec '18, 07:28)</span> <span class="comment-user userinfo">kida001</span>
</div>
</div>
<span id="67288"></span>
<div id="comment-67288" class="comment">
<div id="post-67288-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/5390/escada">@escada</a> - i'm not requesting a specific relation ID, we request data for an entire bounding box. It would be to cumbersome to make a request for every single relation in the result of a bounding box. When I make a bbox query, it does not return the relation data</p>
</div>
<div id="comment-67288-info" class="comment-info">
<span class="comment-age">(20 Dec '18, 07:29)</span> <span class="comment-user userinfo">kida001</span>
</div>
</div>
<span id="67289"></span>
<div id="comment-67289" class="comment">
<div id="post-67289-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Please explain what you mean by "differentiate if the relation is inner vs outer". In OSM we have relations which can have members and these members can (but are not required to) have inner/outer roles. What exactly is it that you want to do?</p>
</div>
<div id="comment-67289-info" class="comment-info">
<span class="comment-age">(20 Dec '18, 08:49)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="67291"></span>
<div id="comment-67291" class="comment">
<div id="post-67291-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>please post the complete OverPass query you make. We need to know which "out" statement you are using and which output format. The sample you posted does not look like the default data type that I get.</p>
<p>It does not matter whether you ask for a particular relation or do another query.</p>
</div>
<div id="comment-67291-info" class="comment-info">
<span class="comment-age">(20 Dec '18, 11:39)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="67295"></span>
<div id="comment-67295" class="comment not_top_scorer">
<div id="post-67295-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/5390/escada"></a><a href="https://help.openstreetmap.org/users/5390/escada">@escada</a> <a href="https://help.openstreetmap.org/users/104/frederik-ramm"></a><a href="https://help.openstreetmap.org/users/104/frederik-ramm">@frederik</a>-Ramm I've updated my post with query information requested. Hopefully that helps explain what I'm doing.</p>
</div>
<div id="comment-67295-info" class="comment-info">
<span class="comment-age">(20 Dec '18, 18:12)</span> <span class="comment-user userinfo">kida001</span>
</div>
</div>
</div>
<div id="comment-tools-67279" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-67279-form-container" class="comment-form-container">
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

<span id="67301"></span>

<div id="answer-container-67301" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67301-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67301-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-67301-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is no such thing as an "inner" or "outer" polygon. There are "inner" or "outer" rings of a polygon, and in OSM these rings can consist of one or more ways. The individual members of a multipolygon relation in OSM can have "inner" or "outer" roles hinting at whether they are part of an inner or outer ring, but these roles are neither required nor guaranteed to be there. Therefore, any algorithm that turns OSM data into geometries - like the "OsmToGeoJSON" you claim to be using - needs to apply logic to build correct polygons.</p>
<p>Once a GeoJSON has been built, there's nothing you can or have to do - either the GeoJSON contains the correct polygons (with potential holes in them) or it doesn't. At this point, any inner/outer information is not relevant to you any more, it has been processed into the polygon geometry.</p>
<p>If OsmToGeoJSON does not produce correct polygons for you then this will be fore one of two reasons:</p>
<p>(1) it is implemented sloppily or incompletely (a working algorithm for polygon construction is described in <a href="https://wiki.openstreetmap.org/wiki/Relation:multipolygon/Algorithm)">https://wiki.openstreetmap.org/wiki/Relation:multipolygon/Algorithm)</a> or</p>
<p>(2) it cannot build some polygons correctly because the response you get from the "map" request lacks referential integrity, i.e. some relations reference ways that are not contained in the response.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Dec '18, 21:48</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-67301" class="comments-container">
<span id="67302"></span>
<div id="comment-67302" class="comment">
<div id="post-67302-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I re-read my post and don't see where I referred to it as an inner/outer polygon in that way. I was referring to the relation of the polygon, just as OSM describes on their wiki for polygons. Sorry if I didn't get the technicalities of it 100% . We are not 'sloppily' drawing them, we're trying to find the correct way to handle how we use 'fill' on a polygon object.. Thanks for the link.</p>
<p>This feels like the most unfriendly forum I've posted on. Both your post and the comments feel demeaning. If you're going to be salty about giving an answer and use subtle language to demean folks, just don't post.</p>
</div>
<div id="comment-67302-info" class="comment-info">
<span class="comment-age">(20 Dec '18, 22:23)</span> <span class="comment-user userinfo">kida001</span>
</div>
</div>
<span id="67305"></span>
<div id="comment-67305" class="comment">
<div id="post-67305-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Frederik, I should not be so decisive. If we read the same multipolygon related OSM Wiki main page there for a member without the inner/outer role we read "Do not use". So, yes, the multipolygon member role is required. Besides, you have a stange understanding/interpretation of the "polygon" notion, hardly in conformity with the mentioned main page. There, in the "Valid MP conditions" we read "We define a valid (closed) polygon as the combination of a subset of member ways which, when their endpoints are joined, form a closed polygon". So, it is a closed polygonal line, sometimes called "ring".</p>
</div>
<div id="comment-67305-info" class="comment-info">
<span class="comment-age">(21 Dec '18, 09:55)</span> <span class="comment-user userinfo">sanser</span>
</div>
</div>
</div>
<div id="comment-tools-67301" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67301-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="67308"></span>

<div id="answer-container-67308" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67308-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67308-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-67308-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>GeoJSON works differently than the OSM data model: It doesn't represent polygons-with-holes as relations with "inner" and "outer" members. In fact, the OSM concept of a "relation" doesn't really exist in GeoJSON.</p>
<p>Instead, the "coordinates" member of a GeoJSON Polygon will simply consist of multiple arrays of coordinates, the first of which represents the outer ring of the polygon, and the remaining of which represent the inner rings. See the <a href="https://tools.ietf.org/html/rfc7946#section-3.1.6">relevant section in the GeoJSON spec</a>.</p>
<p>So if OsmToGeoJSON is working correctly, the part that you omitted here</p>
<pre><code>&quot;coordinates&quot; =&gt; [ ..... ]</code></pre>
<p>should contain the coordinates of the inner rings and outer ring of your polygon.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Dec '18, 11:13</strong></p>
<img src="https://secure.gravatar.com/avatar/0626be5f46f32fce501353e8a5ec399c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tordanik&#39;s gravatar image" />
<p><span>Tordanik</span><br />
<span class="score" title="11998 reputation points"><span>12.0k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="106 badges"><span class="silver">●</span><span class="badgecount">106</span></span><span title="147 badges"><span class="bronze">●</span><span class="badgecount">147</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tordanik has 58 accepted answers">35%</span></p>
</div>
</div>
<div id="comments-container-67308" class="comments-container">
<span id="67322"></span>
<div id="comment-67322" class="comment">
<div id="post-67322-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Wow thank you. Yes I've seen the multiple sets of coordinates/arrays. The first array is consistently the outer ring?</p>
<p>This would be a super helpful assumption to make when drawing polygons, as I was currently going the route of using/writing a function that detects if a polygon is within any of the other polygons we receive, which if it's not needed, would make things much easier.</p>
</div>
<div id="comment-67322-info" class="comment-info">
<span class="comment-age">(22 Dec '18, 17:17)</span> <span class="comment-user userinfo">kida001</span>
</div>
</div>
<span id="67324"></span>
<div id="comment-67324" class="comment">
<div id="post-67324-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/16066/kida001">@kida001</a>: The first array <em>should</em> consistently be the outer ring according to the GeoJSON specification. I haven't checked myself if OsmToGeoJSON does implement this correctly, but I would start from the assumption that it does.</p>
</div>
<div id="comment-67324-info" class="comment-info">
<span class="comment-age">(22 Dec '18, 19:22)</span> <span class="comment-user userinfo">Tordanik</span>
</div>
</div>
</div>
<div id="comment-tools-67308" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67308-form-container" class="comment-form-container">
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


+++
type = "question"
title = "Building tiles server"
description = '''Hi everyone, currently i&#x27;m working on my own .net implementation of a tiles server. I&#x27;ve made some progress but currently im facing a problem with gaps in the rendered lines (example motorways) Look at the image, there are gaps in the blue motorway. I&#x27;m rendering data based on the nodes and ways rel...'''
date = "2017-08-24T09:36:00Z"
lastmod = "2017-08-27T15:36:00Z"
weight = 58781
keywords = [ "tileserver" ]
aliases = [ "/questions/58781" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Building tiles server](/questions/58781/building-tiles-server)

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
<span id="post-58781-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-58781-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-58781-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi everyone,</p>
<p>currently i'm working on my own .net implementation of a tiles server. I've made some progress but currently im facing a problem with gaps in the rendered lines (example motorways) Look at the image, there are gaps in the blue motorway. I'm rendering data based on the nodes and ways relations imported to my custom database. Any ideas what am I missing? I've already tried to include all types of 'roads' to my query.</p>
<p>Thank you for any suggestions :)</p>
<p><img src="/upfiles/osm_problem.JPG" alt="alt text" /></p>
<p>Here is the db structure, and a query answering scai's question So yes, all nodes seems to be imported correctly. and yes i am debuging the problem already for 2 days :) :<img src="/upfiles/osm_db_structure.JPG" alt="alt text" /></p>
<p>How data is rendered on the tile: i'm using this <span>https://wiki.openstreetmap.org/wiki/Slippy_map_tilenames#C.23</span> to get lat and lng for each tile number (left top corner). Getting the +1 tile geoposition gives me right bottom corner. Let's call those two beginingGeoPosition and endGeoPosition. that gives me a set of nodes and their lat and lng.</p>
<p>Knowing my tiles are 256x256 i can get a pixel possition for each node on the tile:</p>
<pre><code>var x = 256 * (node.Longitude - beginingGeoPosition.Longitude ) / (endGeoPosition.Longitude - beginingGeoPosition.Longitude )
var y = 256 * (node.Latitude - beginingGeoPosition.Latitude )/(endGeoPosition.Latitude -beginingGeoPosition.Latitude );</code></pre>
<p>(currently it will work only for lat and lng &gt; 0, but thats not the point)</p>
<p>so that gives us groups of points (for each way) on image tile positioned by their x and y. connectiong those points gives us a part of a motorway. Precisly in .net</p>
<p><code>gfx.DrawLines(new Pen(Color.Blue, 3), linePoints);</code> it creates line through all the points in the linePoints array - each point has its x and y</p>
<p>and the full query looks like this.</p>
<pre><code>select n.nodeid, n.latitude, n.longitude, wn.wayid, wt.tagname, wt.tagvalue, wn.orderid
                        from nodes n
                        join waynodes wn on n.nodeid = wn.nodeid
                        join waytags wt on wn.wayid = wt.wayid
                        where wt.tagname IN (&#39;route&#39;, &#39;area:highway&#39;, &#39;highway&#39;) and wt.tagvalue IN (&#39;motorway&#39;,&#39;trunk&#39;,&#39;primary&#39;,&#39;secondary&#39;,&#39;tertiary&#39;,&#39;unclassified&#39;, &#39;road&#39;, &#39;motorway_link&#39;,&#39;trunk_link&#39;,&#39;primary_link&#39;,&#39;secondary_link&#39;,&#39;tertiary_link&#39;,&#39;unclassified_link&#39;,&#39;road_link&#39;)
                        and n.latitude BETWEEN 52.30848 and 52.32191
                        and n.longitude BETWEEN 15.49072 and 15.5127
                        order by wn.orderid asc</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Aug '17, 09:36</strong></p>
<img src="https://secure.gravatar.com/avatar/7ead15b2da5578cbe4ba69e985684623?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="michal_poz&#39;s gravatar image" />
<p><span>michal_poz</span><br />
<span class="score" title="81 reputation points">81</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="michal_poz has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Aug '17, 16:32</strong> </span></p>
</div>
</div>
<div id="comments-container-58781" class="comments-container">
<span id="58782"></span>
<div id="comment-58782" class="comment">
<div id="post-58782-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Please tell us at least the location or ideally the way IDs that won't get rendered.</p>
</div>
<div id="comment-58782-info" class="comment-info">
<span class="comment-age">(24 Aug '17, 09:38)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="58786"></span>
<div id="comment-58786" class="comment">
<div id="post-58786-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>For example i'm issuing the problem for 52.319371, 15.494535 I think the problem is about connecting the ways. I'm drawing roads for nodes (lat and lng) grouped by wayid, so one line on my img is build of connected points (nodes lat lng) in one group.</p>
</div>
<div id="comment-58786-info" class="comment-info">
<span class="comment-age">(24 Aug '17, 11:11)</span> <span class="comment-user userinfo">michal_poz</span>
</div>
</div>
<span id="58787"></span>
<div id="comment-58787" class="comment">
<div id="post-58787-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>This seems to be around <a href="https://www.openstreetmap.org/way/223282681">https://www.openstreetmap.org/way/223282681</a> and there doesn't seem to be an obvious correspondance between ways in OSM and what is missing.</p>
<p>You'll need to describe in more detail what you have actually done to stand a chance of anyone being able to reply with useful information.</p>
</div>
<div id="comment-58787-info" class="comment-info">
<span class="comment-age">(24 Aug '17, 11:20)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="58788"></span>
<div id="comment-58788" class="comment not_top_scorer">
<div id="post-58788-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Maybe it helps to (re-)read about the basic OSM data model, i.e. <a href="https://wiki.openstreetmap.org/wiki/OSM_XML">https://wiki.openstreetmap.org/wiki/OSM_XML</a> and <a href="https://wiki.openstreetmap.org/wiki/Elements.">https://wiki.openstreetmap.org/wiki/Elements.</a></p>
</div>
<div id="comment-58788-info" class="comment-info">
<span class="comment-age">(24 Aug '17, 11:34)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="58792"></span>
<div id="comment-58792" class="comment not_top_scorer">
<div id="post-58792-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>For example, it's exactly this line <a href="https://www.openstreetmap.org/way/497464371#map=14/52.3202/15.4986">https://www.openstreetmap.org/way/497464371#map=14/52.3202/15.4986</a> that is not rendered correctly.</p>
<p>And to be more precise about what i alerady did: I've created db with tables that describes relations betwen nodes, ways, way tags (waytags values). Each node has its lat and lng.</p>
<p>I've also created a api that provides an endpoint for z/x/y parameters. So based on z x and y (zoom and tile number) i can get the lat and lng coordinates.</p>
<p>After that i can query my db getting all nodes betwen begining lat/lng and end lat/lng. It's a join query on ways and waytags so i get nodes for specific waytag value. In our discusion its highway = motorway It gives me all nodes between left top corner and bottom right corner of specific tile.</p>
<p>Then i know that my tile is 256x256 px, so based on node lat and lng i can specifie its position on the tile - that gives me an array of points (nodes) so i can create a polyline which is drawn on my img.</p>
<p>Hope it's clear enought what i just wrote. I could also post a quere here if that would help. Thanks again</p>
</div>
<div id="comment-58792-info" class="comment-info">
<span class="comment-age">(24 Aug '17, 12:28)</span> <span class="comment-user userinfo">michal_poz</span>
</div>
</div>
<span id="58793"></span>
<div id="comment-58793" class="comment not_top_scorer">
<div id="post-58793-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<blockquote>
<p>I've created db with tables that describes relations betwen nodes, ways, way tags (waytags values).</p>
</blockquote>
<p>That's not really enough detail - you know the schema, so you'll need to debug it. Also you've not said how the data once retrieved from the database is turned into a tile.</p>
</div>
<div id="comment-58793-info" class="comment-info">
<span class="comment-age">(24 Aug '17, 12:32)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="58794"></span>
<div id="comment-58794" class="comment">
<div id="post-58794-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Then start debugging your software. Does way 497464371 and all corresponding nodes exist in your database? Does it get selected for rendering? What does the renderer finally do with it?</p>
</div>
<div id="comment-58794-info" class="comment-info">
<span class="comment-age">(24 Aug '17, 12:34)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="58810"></span>
<div id="comment-58810" class="comment not_top_scorer">
<div id="post-58810-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I've added some more precised description to the topic on how i am drawing roads. Besides that...shouldn't i use relations that are grouping ways? i mean the relations in the osm xml file</p>
</div>
<div id="comment-58810-info" class="comment-info">
<span class="comment-age">(24 Aug '17, 16:34)</span> <span class="comment-user userinfo">michal_poz</span>
</div>
</div>
<span id="58827"></span>
<div id="comment-58827" class="comment">
<div id="post-58827-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/14116/michal_poz">@michal_poz</a>, have you had the time to test the hypothesis in my answer below? I posted it within minutes of your edit, so maybe you've missed it. Let us know if you're still seeing this problem!</p>
</div>
<div id="comment-58827-info" class="comment-info">
<span class="comment-age">(26 Aug '17, 12:33)</span> <span class="comment-user userinfo">Tordanik</span>
</div>
</div>
</div>
<div id="comment-tools-58781" class="comment-tools">
<span class="comments-showing"> showing 5 of 9 </span> <a href="#" class="show-all-comments-link">show 4 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-58781-form-container" class="comment-form-container">
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

<span id="58811"></span>

<div id="answer-container-58811" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-58811-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-58811-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-58811-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="michal_poz has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The gaps in the highway seem to be suspiciously correlated with boundaries between tiles. This might be useful for debugging your problem.</p>
<p>In particular, you write:</p>
<blockquote>
<p>After that i can query my db getting all nodes betwen begining lat/lng and end lat/lng.</p>
</blockquote>
<p>To render the section of a way that is within a given tile, you need at the very least one additional node beyond the border of the tile. Otherwise, the parts of the way that cross over into the adjacent tile will be missing.</p>
<p>So if you indeed only query for nodes within the tile boundaries, this might explain the broken highways.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Aug '17, 16:34</strong></p>
<img src="https://secure.gravatar.com/avatar/0626be5f46f32fce501353e8a5ec399c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tordanik&#39;s gravatar image" />
<p><span>Tordanik</span><br />
<span class="score" title="11998 reputation points"><span>12.0k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="106 badges"><span class="silver">●</span><span class="badgecount">106</span></span><span title="147 badges"><span class="bronze">●</span><span class="badgecount">147</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tordanik has 58 accepted answers">35%</span></p>
</img>
</div>
</div>
<div id="comments-container-58811" class="comments-container">
<span id="58836"></span>
<div id="comment-58836" class="comment">
<div id="post-58836-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I've tested it and that is what is cousing the problem When a single node is not returned in the query for a specific way and lat/ lng range im getting a gap on the edge of a tile. I've tested it by creating a query that returned data for 9 tiles (one tile that i am interested in and 8 other around that first one). That gave me a image with size 768x768 px (3 x256 = 768) and all roads were drawn correctly. So now i have to figure out how to add a additional point on the edge of a tile, that would make roads align with eachother.</p>
</div>
<div id="comment-58836-info" class="comment-info">
<span class="comment-age">(27 Aug '17, 12:58)</span> <span class="comment-user userinfo">michal_poz</span>
</div>
</div>
<span id="58838"></span>
<div id="comment-58838" class="comment">
<div id="post-58838-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I've just got it working correctly. By querying db for data for all 9 tiles and drawing just the middle tile using all nodes. Its possible becouse .net graphic DrawLine method allows to pass also points with x/y possition less than 0. The line is just drawn and ends at the edge of an image. Rendering lasts a big longer but i've added a caching mechanism</p>
<p>Than you all for your comments and help</p>
<p>He is the result.<img src="/upfiles/osm_result.JPG" alt="alt text" /></p>
</div>
<div id="comment-58838-info" class="comment-info">
<span class="comment-age">(27 Aug '17, 15:36)</span> <span class="comment-user userinfo">michal_poz</span>
</div>
</div>
</div>
<div id="comment-tools-58811" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-58811-form-container" class="comment-form-container">
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


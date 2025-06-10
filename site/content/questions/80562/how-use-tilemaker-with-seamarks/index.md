+++
type = "question"
title = "How use tilemaker with seamarks"
description = '''Hello, have successfully created vector mbtiles with tilemaker. How can I now integrate navigation marks from OpenSeaMap. Got seamark planet.osm and converted to .pbf. How do config.json and process.lua write for this case?'''
date = "2021-06-13T23:17:00Z"
lastmod = "2021-06-16T18:02:00Z"
weight = 80562
keywords = [ "seamark", "tilemaker", "openseamap" ]
aliases = [ "/questions/80562" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How use tilemaker with seamarks](/questions/80562/how-use-tilemaker-with-seamarks)

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
<span id="post-80562-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80562-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80562-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, have successfully created vector mbtiles with tilemaker. How can I now integrate navigation marks from OpenSeaMap. Got seamark planet.osm and converted to .pbf. How do config.json and process.lua write for this case?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-seamark" rel="tag" title="see questions tagged &#39;seamark&#39;">seamark</span> <span class="post-tag tag-link-tilemaker" rel="tag" title="see questions tagged &#39;tilemaker&#39;">tilemaker</span> <span class="post-tag tag-link-openseamap" rel="tag" title="see questions tagged &#39;openseamap&#39;">openseamap</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Jun '21, 23:17</strong></p>
<img src="https://secure.gravatar.com/avatar/e8a1754250bc463bada58ddd0107f68b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wkmhv&#39;s gravatar image" />
<p><span>wkmhv</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wkmhv has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-80562" class="comments-container">
&#10;</div>
<div id="comment-tools-80562" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80562-form-container" class="comment-form-container">
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

<span id="80580"></span>

<div id="answer-container-80580" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80580-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80580-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80580-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Add some Lua code to look for the tags you're expecting. For example, you could add this within <code>node_function</code>:</p>
<p><code>local seamark = node:Find("seamark_type") if seamark=="buoy_lateral" then node:Layer("seamarks", true) node:Attribute("type", seamark) node:Attribute("name", node:Find("seamark:name") end</code></p>
<p>Use code like this in <code>node_function</code> and <code>way_function</code> to identify the tags you want, and write them to vector tiles.</p>
<p>Then make sure the layers you're writing to are in the json layer config, e.g.:</p>
<p><code>"seamarks": { "minzoom": 8, "maxzoom": 14 },</code></p>
<p>That's all you need - this will write the data to the vector tiles.</p>
<p>Of course, this doesn't magically make the data render on-screen - that bit's outside the scope of tilemaker and is up to you. Use a style editor like Maputnik to choose the icons, colours etc. for the new data you've added to your vector tiles.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Jun '21, 08:35</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-80580" class="comments-container">
&#10;</div>
<div id="comment-tools-80580" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80580-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="80591"></span>

<div id="answer-container-80591" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80591-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80591-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80591-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>why it founds only the first seamark ("man_made") with name "clock"</p>
<p>&lt;node id="430222786" lat="54.1491789" lon="-4.4759688" version="6" timestamp="2016-05-20T20:49:47Z" changeset="0"&gt; &lt;tag k="name" v="Jubilee Clock"/&gt; &lt;tag k="amenity" v="clock"/&gt; &lt;tag k="display" v="analogue"/&gt; &lt;tag k="historic" v="monument"/&gt; &lt;tag k="man_made" v="clock"/&gt; &lt;/node&gt;</p>
<p>function node_function(node)</p>
<pre><code>    --local seamark = node:Find(&quot;seamark_type&quot;)
    local seamark = node:Find(&quot;man_made&quot;)
&#10;--if seamark==&quot;buoy_lateral&quot; then
    --node:Layer(&quot;seamarks&quot;, true)
    --node:Attribute(&quot;type&quot;, seamark)
    --node:Attribute(&quot;name&quot;, node:Find(&quot;seamark:name&quot;))
--end
&#10;if seamark~=&quot;&quot; then
print (&#39;found seamark&#39;)
print (seamark)
 node:Layer(&quot;seamarks&quot;, true)
 node:Attribute(&quot;type&quot;, seamark)
 node:Attribute(&quot;name&quot;, node:Find(&quot;seamark:name&quot;))
end</code></pre>
<p>end</p>
<p>kmhv@ubuntu:~/tilemaker-master$ tilemaker --input isle-of-man-latest.osm.pbf --output server/isle-of-man1.mbtiles --config config.json --process process.lua mbtiles file exists, will overwrite (Ctrl-C to abort, rerun with --merge to keep) Bounding box -5.43455, -3.68872, 53.7324, 54.6706 Layer waterway (z11-14) Layer transportation (z8-14) Layer building (z14-14) Layer poi (z13-14) Layer seamarks (z11-14) Resizing osm store to size: 64M<br />
Reading .pbf isle-of-man-latest.osm.pbf Total blocks: 33 Resizing osm store to size: 128M<br />
Resizing osm store to size: 192M<br />
found seamarkoup 0 ways 0 relations 0<br />
clock Sorting nodesroup 0 ways 0 relations 0<br />
Total blocks: 5 Resizing osm store to size: 256M<br />
Resizing osm store to size: 320M<br />
Sorting waysgroup 0 ways 8000 relations 0<br />
Total blocks: 1 Resizing osm store to size: 384M<br />
Stored 217719 nodes, 27726 ways, 82 relations<br />
Shape points: 0, lines: 0, polygons: 0 Generated points: 1, lines: 9798, polygons: 12049 Zoom level 13, writing tile 492 of 492<br />
Filled the tileset with good things at server/isle-of-man1.mbtiles</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Jun '21, 22:20</strong></p>
<img src="https://secure.gravatar.com/avatar/e8a1754250bc463bada58ddd0107f68b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wkmhv&#39;s gravatar image" />
<p><span>wkmhv</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wkmhv has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-80591" class="comments-container">
<span id="80598"></span>
<div id="comment-80598" class="comment">
<div id="post-80598-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You need to work out which keys &amp; tags to parse (i.e., you can't just work from Richard's example). For instance most of the Isle of Man semarks seem to use "seamark:type" not seamark_type. See <a href="https://overpass-turbo.eu/s/18qj">https://overpass-turbo.eu/s/18qj</a></p>
</div>
<div id="comment-80598-info" class="comment-info">
<span class="comment-age">(16 Jun '21, 13:37)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="80600"></span>
<div id="comment-80600" class="comment">
<div id="post-80600-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This work's</p>
<p>node_keys = {"seamark:type"}</p>
<p>function node_function(node)</p>
<pre><code>    local seamark = node:Find(&quot;seamark:type&quot;)
&#10;if seamark~=&quot;&quot; then
    node:Layer(&quot;seamarks&quot;, true)
    node:Attribute(&quot;type&quot;, seamark)
    node:Attribute(&quot;name&quot;, node:Find(&quot;seamark:name&quot;))
    node:Attribute(&quot;range&quot;,node:Find(&quot;seamark:light:range&quot;))
end</code></pre>
<p>end</p>
</div>
<div id="comment-80600-info" class="comment-info">
<span class="comment-age">(16 Jun '21, 18:02)</span> <span class="comment-user userinfo">wkmhv</span>
</div>
</div>
</div>
<div id="comment-tools-80591" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80591-form-container" class="comment-form-container">
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


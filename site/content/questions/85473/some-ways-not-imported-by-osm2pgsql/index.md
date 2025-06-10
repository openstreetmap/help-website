+++
type = "question"
title = "Some ways not imported by osm2pgsql"
description = '''SOLVED Following a comment below saying the script works for another user, I created a greatly simplified Overpass query to pull the missing data and it works fine. This tells me that the nodes are missing from the source query results so there&#x27;s actually nothing wrong with my LUA script. Thanks for...'''
date = "2022-08-29T14:57:00Z"
lastmod = "2022-08-30T12:12:00Z"
weight = 85473
keywords = [ "osm2pgsql" ]
aliases = [ "/questions/85473" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Some ways not imported by osm2pgsql](/questions/85473/some-ways-not-imported-by-osm2pgsql)

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
<span id="post-85473-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85473-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-85473-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<h1 id="solved">SOLVED</h1>
<p>Following a comment below saying the script works for another user, I created a greatly simplified Overpass query to pull the missing data and it works fine. This tells me that the nodes are missing from the source query results so there's actually nothing wrong with my LUA script.</p>
<p>Thanks for the replies, if I can't work out the issue with the overpass query I'll open another question. Hopefully I won't have to :)</p>
<hr />
<p>I've been working on a LUA import script for osm2pgsql and once I had it all working I checked the database in qgis and found that some ways are missing.</p>
<p>I can see them in the source XML file (from overpass), with all their node references but osm2pgsql does not import them.</p>
<p>I've created a small test script to try and visualise what is happening</p>
<pre><code>inspect = require(&#39;inspect&#39;)
&#10;local tables = {}
&#10;tables.way_test = osm2pgsql.define_table({
    name = &#39;way_test&#39;,
    ids = { type = &#39;way&#39;, id_column = &quot;id&quot;},
    columns = {
        { column = &#39;name&#39;, type = &#39;text&#39; },
        { column = &#39;geom&#39;, type = &#39;geometry&#39; },
    }
})
&#10;function osm2pgsql.process_way(object)
    if object.id == 987525760 then
        print(inspect(object))
        print(&quot;line&quot;, object.as_linestring())
        print(&quot;poly&quot;, object.as_polygon())
        print(&quot;mline&quot;, object.as_multilinestring())
        print(&quot;mpoly&quot;, object.as_multipolygon())
    end
&#10;    tables.way_test:add_row({
        name = object.tags.name,
        geom = { create = &#39;line&#39; },
    })
end</code></pre>
<p>The above script is run with the following CLI arguments to version <strong>1.7.0</strong> which I compiled myself:</p>
<pre><code>osm2pgsql --host=localhost --user=user --database=db --cache=40050 --flat-nodes=nodes.tmp -sWG --output=flex --style=test.lua data.pbf</code></pre>
<p>This script does not add the missing lines to the test table but does tell me at all four of the <code>as_</code> functions return NULL.</p>
<p>I've also imported the same data using the default style and the way does not appear in the lines table.</p>
<pre><code>osm2pgsql --host=localhost --user=user --database=db --cache=40050 --flat-nodes=nodes.tmp -sWG --output=pgsql data.pbf</code></pre>
<p>All this suggests dodgy data but the way exists and does have a geometry in OSM itself <a href="https://www.openstreetmap.org/way/987525760">https://www.openstreetmap.org/way/987525760</a></p>
<p>While this is one specific way, there are a few I've spotted due to familiarity with the area. Some, like this one are missing while a few others seem to be a straight line from the first to last node without other nodes in between. Can anyone explain why this way is not being imported?</p>
<p>Versions:</p>
<pre><code>osm2pgsql version 1.7.0 (1.7.0)
Build: RelWithDebInfo
Compiled using the following library versions:
Libosmium 2.17.3
Proj [API 6] 8.2.1
Lua 5.3.6</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Aug '22, 14:57</strong></p>
<img src="https://secure.gravatar.com/avatar/0d0a44946fe28018053741f5a225e569?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DarkSnow&#39;s gravatar image" />
<p><span>DarkSnow</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DarkSnow has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>31 Aug '22, 11:48</strong> </span></p>
</div>
</div>
<div id="comments-container-85473" class="comments-container">
<span id="85480"></span>
<div id="comment-85480" class="comment">
<div id="post-85480-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://github.com/gravitystorm/openstreetmap-carto/blob/master/openstreetmap-carto.lua">https://github.com/gravitystorm/openstreetmap-carto/blob/master/openstreetmap-carto.lua</a> is a fairly minimal implementation for the normal backend - maybe start from there and amend the functions you want to change as required?</p>
</div>
<div id="comment-85480-info" class="comment-info">
<span class="comment-age">(29 Aug '22, 20:04)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="85485"></span>
<div id="comment-85485" class="comment">
<div id="post-85485-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>As other mentioned before, you should at least post the complete command line you have been using as well as the version number of osm2pgsql. Otherwise we are stumbling in the dark. When I try your script, osm2pgsql fails with an error message, so I would expect this not to put any data in the database. When I remove the offending lines (those with <code>as_multilinestring()</code> and <code>as_multipolygon()</code>) the script runs through add adds that way to the database.</p>
</div>
<div id="comment-85485-info" class="comment-info">
<span class="comment-age">(30 Aug '22, 08:20)</span> <span class="comment-user userinfo">Jochen Topf</span>
</div>
</div>
<span id="85490"></span>
<div id="comment-85490" class="comment">
<div id="post-85490-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Jochen, it's very interesting that the script is working for you. The print lines are for testing, but work fine for me on version 1.7.0, so can be safely removed.</p>
<p>If the way is being imported for you, how are you getting the source data?</p>
<p>I'm using the following query to get data from overpass:</p>
<pre><code>[timeout:1800];
// Gather results from the UK
area[&quot;name&quot;=&quot;United Kingdom&quot;]-&gt;.boundaryarea;
(
  wr[&quot;piste:type&quot;](area.boundaryarea);
  rel[&quot;site&quot;=&quot;piste&quot;](area.boundaryarea);
  &gt;&gt;;
  wr[~&quot;^([A-Za-z]+:)?landuse$&quot;~&quot;^winter_sports$&quot;](area.boundaryarea);
  (._; &gt;;);
  way(r)[&quot;railway&quot;](area.boundaryarea)-&gt;.siterailways;
  way[&quot;railway&quot;=&quot;funicular&quot;](area.boundaryarea)-&gt;.funiculars;
  way[~&quot;^([A-Za-z]+:)?aerialway$&quot;~&quot;^.*$&quot;](area.boundaryarea)-&gt;.aerialways;
  ((.aerialways; .siterailways; .funiculars;); &gt;;);
  rel[site=piste](area.boundaryarea)-&gt;.sites;
  (way(r.sites)[!&quot;piste:type&quot;][!&quot;aerialway&quot;][!&quot;railway&quot;](area.boundaryarea);
  node(r.sites);)-&gt;.pois;
  (.pois; .pois&gt;;);
);
// print results
out body geom;</code></pre>
</div>
<div id="comment-85490-info" class="comment-info">
<span class="comment-age">(30 Aug '22, 12:12)</span> <span class="comment-user userinfo">DarkSnow</span>
</div>
</div>
</div>
<div id="comment-tools-85473" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85473-form-container" class="comment-form-container">
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

<span id="85483"></span>

<div id="answer-container-85483" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-85483-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85483-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-85483-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is a whole lot of information missing in your question, the most important one: are you using 'pgsql' or 'flex' output?</p>
<p>You can't mix both. If you create a LUA file designed for flex, you need to use the flex output parameters on the command line to have it properly function. The same for pgsql. Don't mix them up.</p>
<p>Read the osm2pgsql manual carefully:</p>
<p><a href="https://osm2pgsql.org/doc/manual.html">https://osm2pgsql.org/doc/manual.html</a></p>
<p>and realize chapters 6 (for flex) and 7 (pgsql) there should be treated as wholly separate information: either you need to read 6, or 7, depending on the choice of output. If you choose one, then forget about the information in the other chapter, as it won't be relevant.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Aug '22, 07:37</strong></p>
<img src="https://secure.gravatar.com/avatar/dc8a1ef54d3e25744ee52d1ad1459a81?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mboeringa&#39;s gravatar image" />
<p><span>mboeringa</span><br />
<span class="score" title="1542 reputation points"><span>1.5k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mboeringa has 4 accepted answers">9%</span></p>
</div>
</div>
<div id="comments-container-85483" class="comments-container">
<span id="85487"></span>
<div id="comment-85487" class="comment">
<div id="post-85487-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for that response. It's a lua script so I'm using flex, but I also tried pgsql with the default style and the way wasn't imported. I thought I was clear but I'll update the question to clarify and add the command line options.</p>
</div>
<div id="comment-85487-info" class="comment-info">
<span class="comment-age">(30 Aug '22, 10:50)</span> <span class="comment-user userinfo">DarkSnow</span>
</div>
</div>
</div>
<div id="comment-tools-85483" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85483-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="85479"></span>

<div id="answer-container-85479" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-85479-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85479-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-85479-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'm not familiar with rendering, but looking at the tags, I'd say it's because there's no rendered tags on this way. Probably there are filters to keep only known tags.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Aug '22, 19:37</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-85479" class="comments-container">
&#10;</div>
<div id="comment-tools-85479" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85479-form-container" class="comment-form-container">
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

</hr>

</div>

</div>


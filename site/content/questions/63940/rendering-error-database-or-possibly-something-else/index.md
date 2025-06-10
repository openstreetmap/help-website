+++
type = "question"
title = "Rendering error: Database or possibly something else"
description = '''Still using Unbuntu 18.04 and used the switch2osm guide along with some of @SomeoneElse&#x27;s documentation.  Somewhere in the process of, in this order, cleaning up permissions, incorporating automatic updates, reloading the database, and pre-rendering some tiles, I seem to have broken the rendering pr...'''
date = "2018-06-01T16:00:00Z"
lastmod = "2018-06-09T18:37:00Z"
weight = 63940
keywords = [ "osm2pgsql", "postgis", "mod_tile" ]
aliases = [ "/questions/63940" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Rendering error: Database or possibly something else](/questions/63940/rendering-error-database-or-possibly-something-else)

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
<span id="post-63940-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63940-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63940-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Still using Unbuntu 18.04 and used the switch2osm guide along with some of <a href="https://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a>'s documentation.</p>
<p>Somewhere in the process of, in this order, cleaning up permissions, incorporating automatic updates, reloading the database, and pre-rendering some tiles, I seem to have broken the rendering process.</p>
<p><code>render_list</code> works as I have pre-rendered, and they show up in the browser, z0 through z10. However, tiles not yet in existence fail to load.</p>
<p>Returned <code>renderd</code> to a manual run, and found it is now spitting an error:</p>
<pre><code>An error occurred while loading the map layer &#39;ajt&#39;: Postgis Plugin: ERROR:  column reference &quot;surface&quot; is ambiguous...encountered during parsing of layer &#39;turning-circle-fill&#39; in Layer at line 22178 of &#39;/home/tileserver/src/openstreetmap-carto/mapnik.xml&#39;</code></pre>
<p>My initial thinking was that I didn't get a good database (<code>osm2pgsql</code>) load this time, but I didn't see any errors in the process and I was able to use <code>render_list</code> to generate a bunch of tiles.</p>
<p>Thoughts? Is this likely a database issue? Or something with <code>mod_tile</code>? Or is the real hint related to <code>Postgis</code>? Or, something I haven't thought of?</p>
<p>Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span> <span class="post-tag tag-link-mod_tile" rel="tag" title="see questions tagged &#39;mod_tile&#39;">mod_tile</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Jun '18, 16:00</strong></p>
<img src="https://secure.gravatar.com/avatar/9d2fa479c7f7984fd8fd435b2badbc4d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tim_rohrer&#39;s gravatar image" />
<p><span>tim_rohrer</span><br />
<span class="score" title="81 reputation points">81</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tim_rohrer has one accepted answer">100%</span></p>
</div>
</div>
<div id="comments-container-63940" class="comments-container">
&#10;</div>
<div id="comment-tools-63940" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63940-form-container" class="comment-form-container">
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

<span id="63942"></span>

<div id="answer-container-63942" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63942-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63942-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-63942-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I suspect that the SQL query at line 22178 of mapnik.xml will somehow join two tables ("select something from table1, table2 where condition" and that either "something" or "condition" will reference the "surface" column, which happens to be available in table1 and table2. You will either have to fix the query, or rob one of the tables of its "surface" column. Can you post the query?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Jun '18, 16:54</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-63942" class="comments-container">
<span id="63952"></span>
<div id="comment-63952" class="comment">
<div id="post-63952-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sorry for the delay. I had to drive to our new site.</p>
<p>Your suspicion is correct.</p>
<p>Here is the entire error: <a href="https://pastebin.com/2GnSgZz3">https://pastebin.com/2GnSgZz3</a></p>
</div>
<div id="comment-63952-info" class="comment-info">
<span class="comment-age">(02 Jun '18, 00:04)</span> <span class="comment-user userinfo">tim_rohrer</span>
</div>
</div>
<span id="63958"></span>
<div id="comment-63958" class="comment">
<div id="post-63958-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I didn't know we were meanwhile applying different rendering to turning circles depending on the road surface but I guess the decline in rendering speed has to come from somewhere ;) you have a choice of changing the two occurrences of "WHEN surface IN" to either "WHEN l.surface IN" (to honour the <code>surface</code> tag of the road that ends in the turning circle) or to "WHEN p.surface IN" (to honour a potential specific surface description of the turning circle). I'd suggest the former, mimicking whe "WHEN l.service IN" line a bit further down.</p>
</div>
<div id="comment-63958-info" class="comment-info">
<span class="comment-age">(02 Jun '18, 11:11)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="63959"></span>
<div id="comment-63959" class="comment">
<div id="post-63959-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It's not 100% clear from the question, but if you're using the "OSM Carto" style straight out of github I'd suggest mentioning the problem there, too.</p>
</div>
<div id="comment-63959-info" class="comment-info">
<span class="comment-age">(02 Jun '18, 11:21)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="63967"></span>
<div id="comment-63967" class="comment">
<div id="post-63967-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Last night I reloaded the database and found the problem persists.</p>
<p>Part of what is strange is that I had built another server using the same guides, but Washington state data vice California. That server seems to be working without this issue.</p>
<p>My goal with this project is to potentially help a non-profit set up a tile server to support a couple of apps they use. I mention this because as I'm assessing the viability of this effort, I am, in part, trying to understand if this issue I'm having is coming from the maturity of the tools, or because I've goofed something up good. :-)</p>
<p>Judging from your comments above, it may be helpful for the community if I continue to track this down and enter issues into GitHub. But I'd also like to know if there are more mature software packages I should be investigating?</p>
<p>Thanks!</p>
</div>
<div id="comment-63967-info" class="comment-info">
<span class="comment-age">(02 Jun '18, 16:18)</span> <span class="comment-user userinfo">tim_rohrer</span>
</div>
</div>
<span id="63968"></span>
<div id="comment-63968" class="comment">
<div id="post-63968-score" class="comment-score">
1
</div>
<div class="comment-text">
<blockquote>
<p>But I'd also like to know if there are more mature software packages I should be investigating?</p>
</blockquote>
<p>:)</p>
<p>Short answer - no. OSM Carto is so mature it's like that piece of cheese in the fridge that it's almost opening the door from the inside in order to come out to meet you. New releases may be a bit "bleeding edge" though - it may be that there's a problem that you're seeing with different software versions that other users are not. You have various options - grab an earlier <a href="https://github.com/gravitystorm/openstreetmap-carto/releases">release</a>, grab a version by <a href="https://github.com/gravitystorm/openstreetmap-carto/commits/e3a508a0c50e7ff5e25164516ba6529872b82c44/roads.mss">date</a> that just predates the "render surface" commit, or use a different style altogether. I regularly use the one described <a href="https://wiki.openstreetmap.org/wiki/User:SomeoneElse/Ubuntu_1804_tileserver_load">here</a> on 18.04 and I've fixed at least one issue there that <em>only</em> appeared on 18.04 (one minor one, to do with roof handling, remains). You could try that instead if you don't mind blue interstates.</p>
</div>
<div id="comment-63968-info" class="comment-info">
<span class="comment-age">(02 Jun '18, 17:05)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="63974"></span>
<div id="comment-63974" class="comment not_top_scorer">
<div id="post-63974-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Interestingly I've just loaded the latest OSM Carto style on an Ubuntu 18.04 machine. Line 22178 is still "turning circle fill" so I guess it's the same as you're using, but I don't see any loading errors and a small area (corresponding to <a href="https://www.openstreetmap.org/node/65451036#map=16/37.3415/-122.0197">https://www.openstreetmap.org/node/65451036#map=16/37.3415/-122.0197</a> in CA that has a turning circle in it with surface set) displays just fine.</p>
</div>
<div id="comment-63974-info" class="comment-info">
<span class="comment-age">(03 Jun '18, 11:44)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="64116"></span>
<div id="comment-64116" class="comment not_top_scorer">
<div id="post-64116-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a>. Well, that seems to be both good news and bad news. The question then is why am I having this trouble.</p>
<p>I don't pretend to understand how all the pieces interact. Are you using carto 1.0.1 to generate mapnik.xml?</p>
<p>Also, I get a ton of warnings, but no obvious errors when I generate mapnik.xml. What is considered normal?</p>
</div>
<div id="comment-64116-info" class="comment-info">
<span class="comment-age">(09 Jun '18, 03:21)</span> <span class="comment-user userinfo">tim_rohrer</span>
</div>
</div>
<span id="64128"></span>
<div id="comment-64128" class="comment not_top_scorer">
<div id="post-64128-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/15159/tim_rohrer">@tim_rohrer</a> "carto -v" shows 1.0.0. This is on a laptop cleanly installed with Ubuntu 18.04 on 20th May 2018, and software initially installed as per <a href="https://wiki.openstreetmap.org/wiki/User:SomeoneElse/Ubuntu_1804_tileserver_load">here</a> (which is a different map style to but the same software as <a href="https://switch2osm.org/manually-building-a-tile-server-18-04-lts/">here</a>. I then added another section to renderd.conf to point at a "standard" OSM Carto style loaded from an adjacent database (I just edited dbname in mapnik.xml) on 3rd June.</p>
</div>
<div id="comment-64128-info" class="comment-info">
<span class="comment-age">(09 Jun '18, 10:33)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="64131"></span>
<div id="comment-64131" class="comment not_top_scorer">
<div id="post-64131-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I switched over to your styles and things appear to be working, which seems to confirm my setup as okay, and that <a href="https://help.openstreetmap.org/users/104/frederik-ramm">@Frederik Ramm</a> may be correct that an issue needs to be raised.</p>
<p>I'd like to (eventually) switch back in order to test the styles identified in the <code>switch2osm</code> guide. Am I correct that to do that I (technically) need to:</p>
<p>1) Recreate the <code>gis</code> database using <code>osm2pgsql</code>, pointing to whichever style I want to use (-S), and using the associated (?) lua script? I'm a little confused on these dependencies still. 2) Recompile <code>mapnik.xml</code> from the <code>project.mml</code> in the chosen carto. 3) Restart renderd service</p>
<p>I guess I'd also need to remove the already generated tiles and recreate them...</p>
<p>Am I missing anything?</p>
</div>
<div id="comment-64131-info" class="comment-info">
<span class="comment-age">(09 Jun '18, 18:37)</span> <span class="comment-user userinfo">tim_rohrer</span>
</div>
</div>
</div>
<div id="comment-tools-63942" class="comment-tools">
<span class="comments-showing"> showing 5 of 9 </span> <a href="#" class="show-all-comments-link">show 4 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-63942-form-container" class="comment-form-container">
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


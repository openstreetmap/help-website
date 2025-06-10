+++
type = "question"
title = "Can I render high Zoom tiles by render_list command ?"
description = '''Hello  I am refering this  https://wiki.openstreetmap.org/wiki/User:SomeoneElse/Ubuntu_1804_tileserver_load#An_example_site for zoom upto 10 , i need to do bellow  render_list -n 1 -s /var/run/renderd/renderd.sock -z 0 -Z 10 -m ajt -a now  if i do bellow, will it render zoom level upto 18 , i actual...'''
date = "2018-06-08T18:08:00Z"
lastmod = "2018-06-13T01:32:00Z"
weight = 64107
keywords = [ "rendering" ]
aliases = [ "/questions/64107" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Can I render high Zoom tiles by render_list command ?](/questions/64107/can-i-render-high-zoom-tiles-by-render_list-command)

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
<span id="post-64107-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64107-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-64107-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello I am refering this <a href="https://wiki.openstreetmap.org/wiki/User:SomeoneElse/Ubuntu_1804_tileserver_load#An_example_site">https://wiki.openstreetmap.org/wiki/User:SomeoneElse/Ubuntu_1804_tileserver_load#An_example_site</a> for zoom upto 10 , i need to do bellow render_list -n 1 -s /var/run/renderd/renderd.sock -z 0 -Z 10 -m ajt -a</p>
<p>now</p>
<p>if i do bellow, will it render zoom level upto 18 , i actually tryed but dont think it work, it always does upto 9 render_list -n 1 -s /var/run/renderd/renderd.sock -z 0 -Z 18 -m ajt -a</p>
<p>Please let me know</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Jun '18, 18:08</strong></p>
<img src="https://secure.gravatar.com/avatar/7bb2a94f867841b58214be09992831d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fosiul&#39;s gravatar image" />
<p><span>fosiul</span><br />
<span class="score" title="96 reputation points">96</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fosiul has one accepted answer">50%</span></p>
</div>
</div>
<div id="comments-container-64107" class="comments-container">
&#10;</div>
<div id="comment-tools-64107" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64107-form-container" class="comment-form-container">
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

<span id="64113"></span>

<div id="answer-container-64113" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64113-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64113-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-64113-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="fosiul has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It wouldn't be practical to use "<code>render_list</code>" to try and render all tiles worldwide up to zoom level 18, for the reasons described <a href="https://wiki.openstreetmap.org/wiki/Tile_disk_usage">here</a>. Most tiles at that zoom level are just sea; there's no point in pre-rendering them. Assuming that you actually have an area that you are interested in I'd suggesting using <a href="https://github.com/alx77/render_list_geo.pl"></a><a href="https://github.com/alx77/render_list_geo.pl"><code>https://github.com/alx77/render_list_geo.pl</code></a> to pre-render tiles in that area.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Jun '18, 00:11</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-64113" class="comments-container">
<span id="64115"></span>
<div id="comment-64115" class="comment">
<div id="post-64115-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a>, Thanks, basically I am interested in 3 Country for now , UK,Spain and Bangladesh. my understanding is, if i can render all tiles with zoom 18 before hand , it will speed up the user experinece when they will use our map, system will not need to render the tile on demand, is that a right assumption ? what i see is, when i browse somes tiles of some new area it takes bit time to come but next time when i try to view those area it comes very fast .</p>
<p>Please let me know.</p>
<p>Thanks</p>
</div>
<div id="comment-64115-info" class="comment-info">
<span class="comment-age">(09 Jun '18, 01:02)</span> <span class="comment-user userinfo">fosiul</span>
</div>
</div>
<span id="64153"></span>
<div id="comment-64153" class="comment">
<div id="post-64153-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/387/someoneelse"></a><a href="https://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a>,</p>
<p>after I ran render with "render_list -n 1 -s /var/run/renderd/renderd.sock -z 0 -Z 11 -m ajt -a" now lower tiles in one country (Bangladesh ) is not showing .</p>
<p>I can see Rendering happening when i try to browse the map but on Screen is totally white. Ref:<a href="https://ibb.co/cwUyso">https://ibb.co/cwUyso</a> however some higher zoom map are showing although not fully visible. <a href="https://ibb.co/bQaeXo">https://ibb.co/bQaeXo</a> and map for UK is fine.</p>
<p>Please let me know what could be wrong ? I am forcing rendering with Zoom 10 again to see if that helps</p>
<p>but Please put some light on this</p>
<p>Thanks</p>
</div>
<div id="comment-64153-info" class="comment-info">
<span class="comment-age">(11 Jun '18, 09:17)</span> <span class="comment-user userinfo">fosiul</span>
</div>
</div>
<span id="64154"></span>
<div id="comment-64154" class="comment">
<div id="post-64154-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Is there definitely data from UK,Spain and Bangladesh in your rendering database? <a href="https://www.openstreetmap.org/way/75134987">https://www.openstreetmap.org/way/75134987</a> is a tertiary road in Bangladesh, so:</p>
<pre><code>psql gis
SELECT tags FROM planet_osm_ways WHERE (id = 75134987);</code></pre>
<p>should return something. If it doesn't maybe you loaded Bangladesh first, and then replaced it with the UK? You'll need to combine it all the data together to load it in the rendering database.</p>
</div>
<div id="comment-64154-info" class="comment-info">
<span class="comment-age">(11 Jun '18, 09:32)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="64158"></span>
<div id="comment-64158" class="comment">
<div id="post-64158-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi Yes, Currently I only loaded Bangladsh and UK. ( I have not loaded the spain yet) UK map does not have any problem, but Bangladesh map, it was fine, but after Rendering with 11, now low zoom map not comming at all, but some high zoom map comming but they not complete ...</p>
<p>Your Sql provie bellow out put so does it mean Bangaldesh Data got removed ? then how i am seeing some Map with high zoom ? ( may be comming from cache ? )</p>
<p>postgres@opentile2:~$ psql gis psql (9.5.12) Type "help" for help.</p>
<p>gis=# SELECT tags FROM planet_osm_ways WHERE (id = 75134987); tags</p>
<hr />
<p>(0 rows)</p>
<p>Also intially i did this</p>
<p>osm2pgsql -d gis --create --slim -G --hstore --tag-transform-script src/openstreetmap-carto/openstreetmap-carto.lua -C 2500 --number-processes 1 -S src/openstreetmap-carto/openstreetmap-carto.style data/bangladesh-latest.osm.pbf</p>
<p>then last week in inserted UK data osm2pgsql -d gis --create --slim -G --hstore --tag-transform-script src/openstreetmap-carto/openstreetmap-carto.lua -C 2500 --number-processes 1 -S src/openstreetmap-carto/openstreetmap-carto.style data/great-britain-latest.osm.pbf</p>
<p>so how do i combine both country ?</p>
</div>
<div id="comment-64158-info" class="comment-info">
<span class="comment-age">(11 Jun '18, 11:43)</span> <span class="comment-user userinfo">fosiul</span>
</div>
</div>
<span id="64159"></span>
<div id="comment-64159" class="comment">
<div id="post-64159-score" class="comment-score">
1
</div>
<div class="comment-text">
<blockquote>
<p>so how do i combine both country ?</p>
</blockquote>
<p>osmosis is one way to do it, osmium probably another. Have a look on this help site and elsewhere for osmosis examples.</p>
</div>
<div id="comment-64159-info" class="comment-info">
<span class="comment-age">(11 Jun '18, 12:42)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="64160"></span>
<div id="comment-64160" class="comment not_top_scorer">
<div id="post-64160-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>ok let me have a look now however,</p>
<p>Can i use --append ? ref : <a href="https://gis.stackexchange.com/questions/50745/merging-osm-files-with-osmosis-and-import-to-postgres-with-osm2pgsql">https://gis.stackexchange.com/questions/50745/merging-osm-files-with-osmosis-and-import-to-postgres-with-osm2pgsql</a></p>
<p>or do you prefer to use osmosis ?</p>
<p>also what I dont understand is, when I am go through the map of Dhaka, i see bellow log why its trying to render if database does not have any information ? or its nothing to do with Rendering and having data into database ?</p>
<p>ing render cmd(3 ajt 19/393731/226371) with protocol version 2 to fd 20 Jun 11 12:42:17 opentile2 renderd[1804]: DEBUG: Sending render cmd(3 ajt 19/393730/226370) with protocol version 2 to fd 19 Jun 11 12:42:17 opentile2 renderd[1804]: DEBUG: Connection 1, fd 20 closed, now 4 left Jun 11 12:42:17 opentile2 renderd[1804]: DEBUG: Connection 3, fd 23 closed, now 3 left Jun 11 12:42:17 opentile2 renderd[1804]: DEBUG: Connection 0, fd 19 closed, now 2 left Jun 11 12:42:17 opentile2 renderd[1804]: DEBUG: Connection 1, fd 22 closed, now 1 left Jun 11 12:42:17 opentile2 renderd[1804]: DEBUG: Connection 0, fd 21 closed, now 0 left</p>
</div>
<div id="comment-64160-info" class="comment-info">
<span class="comment-age">(11 Jun '18, 12:45)</span> <span class="comment-user userinfo">fosiul</span>
</div>
</div>
<span id="64190"></span>
<div id="comment-64190" class="comment not_top_scorer">
<div id="post-64190-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/387/someoneelse">@SomeOneElse</a>,</p>
<p>After I completed insert by using "--append" , i started to render tiles with bellow by forcing to render</p>
<p>sudo render_list -n 4 -s /var/run/renderd/renderd.sock -z 1 -Z 10 -f -m ajt -a</p>
<p>now what is worried me is, I had bangladesh Tiles in past , then while i try to insert UK map, bagnaldesh map got removed but what about those tiles which was creted in past ?</p>
<p>by using -f , will it remove those old tiles for bangladesh and will re created again ?</p>
<p>or it will keep the old tiles and will create new one ?</p>
<p>do you think it can cause problem ?</p>
<p>Please let me know</p>
</div>
<div id="comment-64190-info" class="comment-info">
<span class="comment-age">(13 Jun '18, 01:32)</span> <span class="comment-user userinfo">fosiul</span>
</div>
</div>
</div>
<div id="comment-tools-64113" class="comment-tools">
<span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-64113-form-container" class="comment-form-container">
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


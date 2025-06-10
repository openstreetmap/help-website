+++
type = "question"
title = "Are there optimized (fast and minimal) osm.pbf files available for creating a tile server"
description = '''Hello there, I am very inexperienced in the whole topic, however I managed to set up a tile server using postgresql and renderd following this tutorial: https://switch2osm.org/manually-building-a-tile-server-18-04-lts/ Since I want to use the map for cosmetic purposes only (application only displays...'''
date = "2019-01-24T14:00:00Z"
lastmod = "2019-01-24T17:04:00Z"
weight = 67708
keywords = [ "geofabrik", "ubuntu", "osm2pgsql", "tileserver" ]
aliases = [ "/questions/67708" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Are there optimized (fast and minimal) osm.pbf files available for creating a tile server](/questions/67708/are-there-optimized-fast-and-minimal-osmpbf-files-available-for-creating-a-tile-server)

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
<span id="post-67708-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67708-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-67708-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello there,</p>
<p>I am very inexperienced in the whole topic, however I managed to set up a tile server using postgresql and renderd following this tutorial: <a href="https://switch2osm.org/manually-building-a-tile-server-18-04-lts/">https://switch2osm.org/manually-building-a-tile-server-18-04-lts/</a></p>
<p>Since I want to use the map for cosmetic purposes only (application only displays the surrounding map; basic shape of streets, buildings and parks), I wonder if the osm.pbf files only contain these raw shape data or if there is a lot of meta data connected with it, to allow querying the postgres for special places etc. If this is the case, is there a way to get only the "shape files" which would lead to the following:</p>
<ol>
<li>faster osm2psql imports (this is a real bottleneck if one wants to scale a tile server horizontally)</li>
<li>less disc space necessary</li>
<li>faster access times</li>
</ol>
<p>An other question I was really interested in is, if there are any scripts out there which do the steps described in the tutorial above automatically. I tried to make one by myself, but switching users (to postrges and back) does not really seem to work in a script.</p>
<p>I would be really happy if anyone could clear things up for me, maybe I completely misunderstood the kind of files that exist and how to use them.</p>
<p>Greetings,</p>
<p>Erik</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-geofabrik" rel="tag" title="see questions tagged &#39;geofabrik&#39;">geofabrik</span> <span class="post-tag tag-link-ubuntu" rel="tag" title="see questions tagged &#39;ubuntu&#39;">ubuntu</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Jan '19, 14:00</strong></p>
<img src="https://secure.gravatar.com/avatar/5eabcf32b6244f650e286d308d9341e4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Erik1988osm&#39;s gravatar image" />
<p><span>Erik1988osm</span><br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Erik1988osm has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Jan '19, 14:40</strong> </span></p>
</div>
</div>
<div id="comments-container-67708" class="comments-container">
&#10;</div>
<div id="comment-tools-67708" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67708-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="67711"></span>

<div id="answer-container-67711" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67711-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67711-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-67711-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Erik1988osm has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>One answer to the "cosmetic purposes only" part of the question might be to significantly cut down the data that load load into the database (which obviously will mean that it is smaller and will load quicker). <a href="https://www.openstreetmap.org/user/SomeoneElse/diary/47027">This diary entry</a> and the one that it lnks to describe doing that for boundaries; you'd want to include a few more features I expect but the principal should still work.</p>
<p>It still might not be the best solution for what you want though; something involving tailored shapefiles might be better, and I'm sure there's a write-up of that somewhere.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Jan '19, 14:46</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-67711" class="comments-container">
<span id="67713"></span>
<div id="comment-67713" class="comment">
<div id="post-67713-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you. Am I right with my understanding, that osm.pbf files contain much more than just the graphical structure of the map? Do the "shapefiles" (<a href="https://www.geofabrik.de/en/data/shapefiles.html)">https://www.geofabrik.de/en/data/shapefiles.html)</a> only contain the graphics? And if yes, can I somehow import just these in a postgresql to use with renderd afterwards? I guess for renderd to allow the query there must be at least the positioning data correlated with them to work properly. Do you know any hoster, which offer these minimalistic map graphic/position osm.pbf data? As far as I can overlook your link, the changes are only made on the style, the backlaying data remains still unchanged (big and slow).</p>
</div>
<div id="comment-67713-info" class="comment-info">
<span class="comment-age">(24 Jan '19, 14:57)</span> <span class="comment-user userinfo">Erik1988osm</span>
</div>
</div>
<span id="67714"></span>
<div id="comment-67714" class="comment">
<div id="post-67714-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<blockquote>
<p>Am I right with my understanding, that osm.pbf files contain much more than just the graphical structure of the map?</p>
</blockquote>
<p>Yes - the contain all the data in OSM, including many things that any particular map is unlikely to display. However to be clear is is no one "the map" - there are lots of different representations of OSM data. <a href="http://openwhatevermap.xyz/#3/28.00/18.00">This</a> is a fun map showing lots of different map styles.</p>
<p>"Shapefile" is just a file format, just as .osm.pbf is, and the page you link to explains a bit about what Geofabrik have put in their shapefiles.</p>
<blockquote>
<p>As far as I can overlook your link, the changes are only made on the style, the backlaying data remains still unchanged (big and slow).</p>
</blockquote>
<p>No, as the linked diary entry says "for boundaries I created a version of that that used osmium, osmconvert and osmfilter to select only boundaries from the data and remove non-boundary tags that might render too".</p>
</div>
<div id="comment-67714-info" class="comment-info">
<span class="comment-age">(24 Jan '19, 15:05)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="67716"></span>
<div id="comment-67716" class="comment">
<div id="post-67716-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Right. So what my solution would be is to not modify the style, as I did to hide certain thinks like name tags, banner etc., but to use osmfilter on a planet.osm.pbf and only keep certain informations of interest. This would probably lead into a way smaller file (?). But I wonder if I could still apply a style to it, since some fields would be missing. Does the osm2pgsql just skip those?</p>
</div>
<div id="comment-67716-info" class="comment-info">
<span class="comment-age">(24 Jan '19, 15:20)</span> <span class="comment-user userinfo">Erik1988osm</span>
</div>
</div>
<span id="67717"></span>
<div id="comment-67717" class="comment">
<div id="post-67717-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<blockquote>
<p>But I wonder if I could still apply a style to it, since some fields would be missing. Does the osm2pgsql just skip those?</p>
</blockquote>
<p>It depends - you do have the option to cut down the columns created in the database at data load (using a "style" file), and if you do that then yes, a rendering style that expects those columns to be present will give errors. You do however have the option to create all the columns and just not load data into them - that shouldn't cause the renderer to fail.</p>
<p>Given that you want a map that looks different to the OSM Carto one, you probably want to experiment with modifying the style as well.</p>
</div>
<div id="comment-67717-info" class="comment-info">
<span class="comment-age">(24 Jan '19, 15:40)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="67719"></span>
<div id="comment-67719" class="comment">
<div id="post-67719-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you very much for your help, it made certain things clear to me. I created a summary below on what steps are necessary, as far as I understood for now.</p>
</div>
<div id="comment-67719-info" class="comment-info">
<span class="comment-age">(24 Jan '19, 15:50)</span> <span class="comment-user userinfo">Erik1988osm</span>
</div>
</div>
<span id="67720"></span>
<div id="comment-67720" class="comment not_top_scorer">
<div id="post-67720-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Can you explain what you mean with tailored shapefiles a little more in detail?</p>
</div>
<div id="comment-67720-info" class="comment-info">
<span class="comment-age">(24 Jan '19, 16:02)</span> <span class="comment-user userinfo">Erik1988osm</span>
</div>
</div>
<span id="67722"></span>
<div id="comment-67722" class="comment not_top_scorer">
<div id="post-67722-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<blockquote>
<p>Can you explain what you mean with tailored shapefiles a little more in detail?</p>
</blockquote>
<p>One of the more GIS people here is probably better placed to do that, but essentially a shapefile is just a file format. The page you linked to before offers special purpose shapefiles for e.g. power infrastructure, for example. There may be someone out there creating "minimal" shapefiles for just major roads, towns, that sort of thing.</p>
</div>
<div id="comment-67722-info" class="comment-info">
<span class="comment-age">(24 Jan '19, 17:04)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-67711" class="comment-tools">
<span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-67711-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="67710"></span>

<div id="answer-container-67710" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67710-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67710-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-67710-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Re "doing it automatically" <a href="https://www.openstreetmap.org/user/SomeoneElse/diary/45070">this diary entry</a> describes how to do it all using Docker.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Jan '19, 14:22</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-67710" class="comments-container">
&#10;</div>
<div id="comment-tools-67710" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67710-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="67718"></span>

<div id="answer-container-67718" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67718-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67718-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-67718-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As a summary to what my understanding was, the following steps will lead to a custom file, reduced in its size (and with this probably raise the performance as well):</p>
<ol>
<li>Get a planet.osm.pbf</li>
<li><p>Examine the file, to get knowledge about the field names you require:</p>
<p>./osmfilter bremen.o5m --out-count</p>
<pre><code>  28199 highway
  22794 building
  21365 name
  18754 created_by
  17751 source
  11842 addr:housenumber
  11835 addr:street
   5925 addr:postcode
   5724 foot
   5543 addr:city</code></pre></li>
<li><p>Apply the filter</p>
<p>./osmfilter norway.osm --keep="highway=primary =secondary waterway=river" &gt;streets.osm</p></li>
<li><p>Convert the output file with osmconvert if necessary</p></li>
<li><p>Update your style xml (?)</p></li>
<li><p>Import the custom file with osm2pgsql</p></li>
</ol>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Jan '19, 15:49</strong></p>
<img src="https://secure.gravatar.com/avatar/5eabcf32b6244f650e286d308d9341e4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Erik1988osm&#39;s gravatar image" />
<p><span>Erik1988osm</span><br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Erik1988osm has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Jan '19, 15:51</strong> </span></p>
</div>
</div>
<div id="comments-container-67718" class="comments-container">
&#10;</div>
<div id="comment-tools-67718" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67718-form-container" class="comment-form-container">
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


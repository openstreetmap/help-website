+++
type = "question"
title = "Removing water boundaries from administrative boundaries from mapnik rendering"
description = '''Hello Background knowledge I am totally new to the topics of GIS. I have just started looking into this so my knowledge on topics such as mapnik and postgis is not that high. Question I am trying to remove administrative boundaries for countries that currently extend into the sea/ocean. I am looking...'''
date = "2017-12-20T15:47:00Z"
lastmod = "2018-01-03T20:34:00Z"
weight = 61296
keywords = [ "boundaries", "admin_boundary", "mapnik" ]
aliases = [ "/questions/61296" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Removing water boundaries from administrative boundaries from mapnik rendering](/questions/61296/removing-water-boundaries-from-administrative-boundaries-from-mapnik-rendering)

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
<span id="post-61296-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61296-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-61296-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello</p>
<p><strong>Background knowledge</strong></p>
<p>I am totally new to the topics of GIS. I have just started looking into this so my knowledge on topics such as mapnik and postgis is not that high.</p>
<p><strong>Question</strong></p>
<p>I am trying to remove administrative boundaries for countries that currently extend into the sea/ocean. I am looking to achieve country boundaries that look similar to openstreetmaps transport layer which show no water boundaries.</p>
<p><strong>Setup</strong></p>
<p>The way I am rendering the map tiles is using mapnik. I have followed this tutorial exactly: <a href="https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/">https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/</a></p>
<p><strong>Attempted Solutions</strong></p>
<p>I researched this question before asking and these were the possible solutions that I came across and the end result.</p>
<p>(1) I have tried to change the query in mapnik.xml that controls the admin_boundaries and added a new parameter: boundary=administrative AND NOT boundary_type=maritime. This did not render any results for me in the boundaries. Data set was azerbaijan.osm.pbf from tutorial</p>
<p>(2) <a href="https://github.com/gravitystorm/openstreetmap-carto/issues/621">https://github.com/gravitystorm/openstreetmap-carto/issues/621</a> has a query that should remove water boundaries from the map written by nebulon42 but it leaves certain boundaries in water intact. Tested using myanmar.osm.pbf</p>
<p>(3) <a href="https://help.openstreetmap.org/questions/34000/problem-hidding-a-maritime-border-with-mapnik">https://help.openstreetmap.org/questions/34000/problem-hidding-a-maritime-border-with-mapnik</a> suggests changing the ordering of the rendering but I do not know how to do that so I was unable to test this one.</p>
<p><strong>Current Solution</strong></p>
<p>I am removing the way tags from the osm file that correspond to the boundaries and replacing them with latitude and longitude acquired from <a href="https://wambachers-osm.website/boundaries/">https://wambachers-osm.website/boundaries/</a> and selecting land. In a small sample size it has worked but I am wondering if there is an easier way to do so from mapnik.xml either using a specific query or tag.</p>
<p>Any help is appreciated and Thank you.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-boundaries" rel="tag" title="see questions tagged &#39;boundaries&#39;">boundaries</span> <span class="post-tag tag-link-admin_boundary" rel="tag" title="see questions tagged &#39;admin_boundary&#39;">admin_boundary</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Dec '17, 15:47</strong></p>
<img src="https://secure.gravatar.com/avatar/206bbb2d3464a897f0b828361911ef31?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ujjawal&#39;s gravatar image" />
<p><span>Ujjawal</span><br />
<span class="score" title="46 reputation points">46</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ujjawal has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Jan '18, 20:33</strong> </span></p>
</div>
</div>
<div id="comments-container-61296" class="comments-container">
<span id="61466"></span>
<div id="comment-61466" class="comment">
<div id="post-61466-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Suggest that you make this edit an answer, and then an admin (e.g. me) can make this the accepted answer). I think it will be clearer.</p>
</div>
<div id="comment-61466-info" class="comment-info">
<span class="comment-age">(03 Jan '18, 17:18)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="61468"></span>
<div id="comment-61468" class="comment">
<div id="post-61468-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>ok removed the edit for an answer</p>
</div>
<div id="comment-61468-info" class="comment-info">
<span class="comment-age">(03 Jan '18, 20:34)</span> <span class="comment-user userinfo">Ujjawal</span>
</div>
</div>
</div>
<div id="comment-tools-61296" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61296-form-container" class="comment-form-container">
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

<span id="61302"></span>

<div id="answer-container-61302" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-61302-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61302-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-61302-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>How prevalent is the "<a href="https://overpass-turbo.eu/s/tVs">maritime=yes</a>" tag? If that's in widespread use (and in the few places I've looked it does seem to be used properly) you can just remove an admin boundary tag in lua if maritime=yes is set.</p>
<p><a href="https://github.com/SomeoneElseOSM/SomeoneElse-style/blob/90e0733593029ab5c4d4ab6d03cc4793853ea982/style.lua#L559">Here</a> is a bit of lua code that removes <em>all</em> boundaries. You want something instead like:</p>
<pre><code>if (( keyvalues[&quot;boundary&quot;] == &quot;administrative&quot; )  and
    ( keyvalues[&quot;maritime&quot;] == &quot;yes&quot;            )) then
   keyvalues[&quot;boundary&quot;] = nil
end</code></pre>
<p>Whilst you could try and do things with mapnik z-ordering or external boundary info, that sounds very much like "doing it the hard way" to me!</p>
<p>(edit)</p>
<p>If you're wondering "what is a lua and why would I want one", it's a way of changing one tag to another before loading into a rendering database. The OSM Carto style uses <a href="https://github.com/gravitystorm/openstreetmap-carto/blob/master/openstreetmap-carto.lua">this</a> lua transformation, but it doesn't do much in the way of tag changes. You can see some tile-server setup notes using a a style that does much more <a href="https://wiki.openstreetmap.org/wiki/User:SomeoneElse/Ubuntu_1604_tileserver_load">here</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Dec '17, 21:04</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Dec '17, 21:10</strong> </span></p>
</div>
</div>
<div id="comments-container-61302" class="comments-container">
<span id="61313"></span>
<div id="comment-61313" class="comment">
<div id="post-61313-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I tried to replace the style.lua file provided by the tutorial with yours and it let me remove ALL boundaries but the modified keyvalues[maritime] did remove any boundaries. I checked the osm.xml file that I use to populate the postgres tables and it does have borders that have maritime tags as yes.</p>
</div>
<div id="comment-61313-info" class="comment-info">
<span class="comment-age">(21 Dec '17, 16:28)</span> <span class="comment-user userinfo">Ujjawal</span>
</div>
</div>
<span id="61317"></span>
<div id="comment-61317" class="comment">
<div id="post-61317-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I am trying to remove the water boundaries now using osmfilter by trying to remove all ways with tags on maritime=yes and border_type=territorial based on the information written in <a href="http://wiki.openstreetmap.org/wiki/Tag:boundary%3Dmaritime">http://wiki.openstreetmap.org/wiki/Tag:boundary%3Dmaritime</a> but it still seems to keep water boundaries on provincial levels (admin_level &gt; 4). It produces the same result as nebulon42's query from attempted solution 2.</p>
</div>
<div id="comment-61317-info" class="comment-info">
<span class="comment-age">(21 Dec '17, 20:55)</span> <span class="comment-user userinfo">Ujjawal</span>
</div>
</div>
<span id="61333"></span>
<div id="comment-61333" class="comment">
<div id="post-61333-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Re the lua suggestion, you're correct that it doesn't work - and the reason is that there are 3 or more objects passed through for rendering for each bit of boundary. There's the way (which has maritime=yes on it) and one or more relations (which don't). These can be removed or retagged with lua but what isn't currently possible is to remove (or change) relation members from within the lua code. There's something a bit like it (the old-style multipolygon handling) but what osm2pgsql actually does with that is a bit of a black art :) It would be possible to change tags on the whole relation based on the members' tags, but that wouldn't help.</p>
</div>
<div id="comment-61333-info" class="comment-info">
<span class="comment-age">(23 Dec '17, 13:12)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-61302" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61302-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="61467"></span>

<div id="answer-container-61467" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-61467-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61467-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-61467-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>So in the end I managed to solve it by using the current solution. This is basically for anyone else who wants to use this method (Note: not the most efficient solution)</p>
<p>(1) Download the country osm.xml file</p>
<p>(2) remove all boundary=administrative tags (used osmfilter but use whichever tool that gets the job done).</p>
<p>(3) download the country file from <a href="https://wambachers-osm.website/boundaries/">https://wambachers-osm.website/boundaries/</a> and choose the json format and land boundary.</p>
<p>(4) Download a tool to convert geojson to osm.xml format (used geojsontoosm but note if you use this you will have to make a little changes to the code. Things to change are changing the relation id to start from a positive number and ++ increment as relations as negative dont display and add an extra tag that forces boundary = administrative in multipolygon method. And if you need lvl4(admin_level) data remove the part where it doesnt add way to relation if you have only one entry in multipolygon)</p>
<p>(5) add the new osm.xml in the original country xml. (I just made a script for it as you would need to remove the osm tags from the new osm.xml and remove the ending osm tag from the bottom of country tag and for multiple countries it would be a hassle to do manually.)</p>
<p>Hope it helps someone and Thanks to someoneElse for lua idea.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Jan '18, 20:32</strong></p>
<img src="https://secure.gravatar.com/avatar/206bbb2d3464a897f0b828361911ef31?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ujjawal&#39;s gravatar image" />
<p><span>Ujjawal</span><br />
<span class="score" title="46 reputation points">46</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ujjawal has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-61467" class="comments-container">
&#10;</div>
<div id="comment-tools-61467" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61467-form-container" class="comment-form-container">
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


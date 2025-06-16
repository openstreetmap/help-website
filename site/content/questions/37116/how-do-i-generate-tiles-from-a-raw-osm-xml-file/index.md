+++
type = "question"
title = "How do I generate tiles from a raw OSM XML file?"
description = '''I recently downloaded Maperitive and generated tiles from a raw OSM XML file. The average rate was approximately 70-80 tiles per second. This seems like a decent pace but when your map has 16 million tiles on a zoom level, it could take some time to generate all the necessary tiles. In a nutshell, M...'''
date = "2014-09-29T18:34:00Z"
lastmod = "2014-09-30T02:00:00Z"
weight = 37116
keywords = [ "tiles" ]
aliases = [ "/questions/37116" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How do I generate tiles from a raw OSM XML file?](/questions/37116/how-do-i-generate-tiles-from-a-raw-osm-xml-file)

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
<span id="post-37116-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37116-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-37116-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I recently downloaded Maperitive and generated tiles from a raw OSM XML file. The average rate was approximately 70-80 tiles per second. This seems like a decent pace but when your map has 16 million tiles on a zoom level, it could take some time to generate all the necessary tiles. In a nutshell, Maperitive (Windows, .NET 4.0) works fine and I've used it to generate some test data. I could see it being a solution but there are some gotchas.</p>
<p>Over the last few days, I've been reading articles &amp; blog posts trying to find the best approach for processing raw OSM XML files. At this point, my requirements are minimal: a) the process must take a raw OSM XML file and, at the end of the process, give me map tiles, and b) the process runs on my hardware (no SAAS). Other than that, I'm not too concerned about the actual process.</p>
<p>The process could run on Ubuntu or Windows 7/8, client machine or, if absolutely necessary, server. I'm not too familiar with Linux so that would require more detailed steps but I'm willing to learn.</p>
<p>I understand multiple products may be necessary to process the XML files. If that is the case, I can handle that. One product would be easiest but if several products are required, one for each step of the process, I can live with that.</p>
<p>Lastly, the area of my study is not available as a pre-built dataset from some of the websites. For example, my map will not cover the metro area of Chicago or New York. Its wider and doesn't fit nicely in a single state, metropolitan area, and maybe not even a single country. Therefore, I've been getting the raw data directly from OpenStreetMap.org and this will not change due to the geographic extents of the project.</p>
<p>So where an I find the best practice approach (preferably a document / tutorial / blog posts / video / ???) to processing raw OSM XML data into map tiles and which tools should I use?</p>
<p>Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Sep '14, 18:34</strong></p>
<img src="https://secure.gravatar.com/avatar/767934a648524da57388558217ad9c2d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Squatchy&#39;s gravatar image" />
<p><span>Squatchy</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Squatchy has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Sep '14, 18:55</strong> </span></p>
</div>
</div>
<div id="comments-container-37116" class="comments-container">
<span id="37120"></span>
<div id="comment-37120" class="comment">
<div id="post-37120-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Would it be possible to give an idea of the rough size of bounding box that you're interested in (perhaps using <a href="http://osm.duschmarke.de/bbox.html">http://osm.duschmarke.de/bbox.html</a> )? Also what tile zoom levels?</p>
<p>Do you want to use a map style that you've already designed (e.g. in Maperitive), an existing Mapnik one (e.g. openstreetmap-carto, used by the "standard" layer on the OSM website) or something else?</p>
<p>Also, reading between the lines of the question a bit, do you want something that you can easily automate on a client machine over which you don't have direct control?</p>
</div>
<div id="comment-37120-info" class="comment-info">
<span class="comment-age">(29 Sep '14, 20:19)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="37130"></span>
<div id="comment-37130" class="comment">
<div id="post-37130-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The rough size is the State of Minnesota. Zoom level 4 - 19, but that may be limited to 17 / 18 depending on size and ability to generate the tiles in a reasonable amount of time. Currently completing Level 17 and it's pushing my definition of "reasonable time". At the moment, out of the box styles are sufficient as I haven't created any yet in Maperitive. Custom styles may be something I attempt in the future. I would like to automate the process. Now, for example, I'd like to spin up a few cloud VMs and process each zoom level in its own vm.</p>
</div>
<div id="comment-37130-info" class="comment-info">
<span class="comment-age">(30 Sep '14, 02:00)</span> <span class="comment-user userinfo">Squatchy</span>
</div>
</div>
</div>
<div id="comment-tools-37116" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37116-form-container" class="comment-form-container">
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

<span id="37121"></span>

<div id="answer-container-37121" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-37121-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37121-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-37121-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Seeing as I've just done something a bit like this for a project of mine, I'll explain what I did. It might not match exactly what you want (hence the questions in the comment) but hopefully you'll find it useful:</p>
<p>1) Load the data into a <a href="http://switch2osm.org/serving-tiles/">switch2osm</a>-style rendering database. What I actually did is described <a href="https://wiki.openstreetmap.org/wiki/User:SomeoneElse/Ubuntu_1404_tileserver">here</a>.</p>
<p>2) In my case I wanted to use the "standard" <a href="https://github.com/gravitystorm/openstreetmap-carto">openstreetmap-carto</a> style, but loaded via a <a href="https://github.com/openstreetmap/osm2pgsql/blob/master/docs/lua.md">lua tag transform</a> similar to <a href="https://github.com/SomeoneElseOSM/designation-style">this one</a> to modify the data on the way into the database, as described <a href="https://wiki.openstreetmap.org/wiki/User:SomeoneElse/Ubuntu_1404_tileserver_load">here</a>. You could of course use a modified style of some sort (perhaps by using <a href="https://www.mapbox.com/tilemill/docs/crashcourse/introduction/">TileMill</a>).</p>
<p>3) I then used <a href="http://svn.openstreetmap.org/applications/rendering/mapnik/generate_tiles.py">generate_tiles.py</a> from <a href="http://svn.openstreetmap.org/applications/rendering/mapnik/">here</a> to generate the actual tiles that I wanted (in my case just .pngs). I had to edit "openstreetmap-carto"'s mapnik.xml slightly to not reference fonts that I didn't have installed (see <a href="https://github.com/gravitystorm/openstreetmap-carto/issues/999">here</a>) but that's very easy to do manually.</p>
<p>The reason that I took this approach is that I already had (1) and (2) set up, so only actually needed to do (3). If you have instead already got a Maperitive style that does what you want, that may be easier for you.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Sep '14, 20:37</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-37121" class="comments-container">
&#10;</div>
<div id="comment-tools-37121" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37121-form-container" class="comment-form-container">
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


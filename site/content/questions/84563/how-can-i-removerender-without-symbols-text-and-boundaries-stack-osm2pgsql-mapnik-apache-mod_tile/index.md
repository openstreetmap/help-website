+++
type = "question"
title = "How can I remove/render without symbols, text and boundaries? stack - osm2pgsql, mapnik, apache, mod_tile"
description = '''Hello, I&#x27;m on struggle street now, hence posting here -  I am running my own ubuntu 22.04 tile server, per the switch2osm.org guide, and it&#x27;s running great. I&#x27;ve since started trying to customize it, by trying to remove text, symbols/icons and (administrative) boundaries - the purple ones.  I&#x27;ve sco...'''
date = "2022-05-23T03:02:00Z"
lastmod = "2022-06-08T14:25:00Z"
weight = 84563
keywords = [ "boundaries", "rendering", "icon", "mapnik", "text" ]
aliases = [ "/questions/84563" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How can I remove/render without symbols, text and boundaries? stack - osm2pgsql, mapnik, apache, mod_tile](/questions/84563/how-can-i-removerender-without-symbols-text-and-boundaries-stack-osm2pgsql-mapnik-apache-mod_tile)

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
<span id="post-84563-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84563-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84563-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I'm on struggle street now, hence posting here - I am running my own ubuntu 22.04 tile server, per the switch2osm.org guide, and it's running great. I've since started trying to customize it, by trying to remove text, symbols/icons and (administrative) boundaries - the purple ones.</p>
<p>I've scoured the web for answer, similar questions and more, with minor success - I've deleted the majority of text using the <em>3rd</em> tip by SomeoneElse <a href="https://help.openstreetmap.org/questions/84525/how-to-render-osm-map-tiles-without-text-osm2pgsql-mapnik-apache-mod_tile">here</a> - however, I'm finding some building names and street numbers are still appearing.</p>
<p>My biggest struggle, however, has been removing all symbols and purple boundaries. I've tried simply deleting the "admin.mss" and "symbols" folder, altering the names, modifying the colour variables in the mss file and a whole heap of other hacks/attempts but to no avail (in most cases, when updating there is no difference, even if the files are deleted).</p>
<p>Unfortunately I'm quite new, so I apologies beforehand for the possible hand holding I'll need.</p>
<p>I'd really appreciate any/all advice. Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-boundaries" rel="tag" title="see questions tagged &#39;boundaries&#39;">boundaries</span> <span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-icon" rel="tag" title="see questions tagged &#39;icon&#39;">icon</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-text" rel="tag" title="see questions tagged &#39;text&#39;">text</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 May '22, 03:02</strong></p>
<img src="https://secure.gravatar.com/avatar/65bdb297b654bac58eb3679ec6789055?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hicallmeal&#39;s gravatar image" />
<p><span>hicallmeal</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hicallmeal has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-84563" class="comments-container">
&#10;</div>
<div id="comment-tools-84563" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84563-form-container" class="comment-form-container">
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

<span id="84564"></span>

<div id="answer-container-84564" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-84564-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84564-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-84564-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The project is driven by layers defined in <code>project.mml</code>. Many of the things you ask for are rendered by individual layers. You can remove them if you don't want them, but if your plan is to maintain a for of the main style, I think it would be better if you just disable them using <code>status: off</code>.</p>
<p>As for specific symbols and such, the project file also defines the SQL queries used to fetch data for rendering. They're also defined in the <code>.mms</code> files under <code>style</code>. you can either remove the fetch of the data from the SQL queries (but beware on how you edit the file if you plan to maintain the fork) or comment out (with <code>/* */</code> à la C/C++/others) in the style files.</p>
<p>I keep my own fork <a href="https://github.com/StyXman/openstreetmap-carto/tree/elevation/develop">here</a>. Here I <a href="https://github.com/StyXman/openstreetmap-carto/blob/elevation/develop/project.mml#L1703=">disable a whole layer</a>. Here I do <a href="https://github.com/StyXman/openstreetmap-carto/blob/elevation/develop/project.mml#L166=">all kinds of modifications to the SQL queries</a> to change or reduce the amount of rendered data. Here I <a href="https://github.com/StyXman/openstreetmap-carto/blob/elevation/develop/style/landcover.mss#L162=">disable a whole style block</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 May '22, 10:03</strong></p>
<img src="https://secure.gravatar.com/avatar/e4587465b2b1b94834e5e625b80a29dd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Marcos%20Dione&#39;s gravatar image" />
<p><span>Marcos Dione</span><br />
<span class="score" title="71 reputation points">71</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Marcos Dione has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-84564" class="comments-container">
<span id="84565"></span>
<div id="comment-84565" class="comment">
<div id="post-84565-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hey Marcos, thanks for the reply! So that looked really promising, so I tried out adding status:off to a bunch of items (like you did in that example), including amenities and boundaries, and I also commented out the whole amenity.mss file excluding the variables just to be safe. Unfortunately I must either be doing something wrong, as no matter what I do, the changes don't appear (my process is, carto project.mml &gt; mapnik, find and delete all .meta tiles, restart server and renderd, if all fails then I run the osm2pgsql command). At this point, I'm worried I'm not clearing the cached tiles or perhaps I'm running it differently to you. Any ideas?</p>
</div>
<div id="comment-84565-info" class="comment-info">
<span class="comment-age">(23 May '22, 11:14)</span> <span class="comment-user userinfo">hicallmeal</span>
</div>
</div>
<span id="84571"></span>
<div id="comment-84571" class="comment">
<div id="post-84571-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm sorry, but I don't know anything about the rest of your stack. What I do locally is to edit the style with a text editor and check changes in kosmtik. Once I'm happy with my changes I might do some rendering or otherwise wait for the next opportunity to do it (I only render places that I go visit or maybe the city where I live).</p>
</div>
<div id="comment-84571-info" class="comment-info">
<span class="comment-age">(23 May '22, 21:11)</span> <span class="comment-user userinfo">Marcos Dione</span>
</div>
</div>
<span id="84675"></span>
<div id="comment-84675" class="comment">
<div id="post-84675-score" class="comment-score">
1
</div>
<div class="comment-text">
<blockquote>
<p>At this point, I'm worried I'm not clearing the cached tiles</p>
</blockquote>
<p>Tiles might still be cached locally, to protect against that request them locally from a new incognito browser window (close any other incognito browser windows and create a new one).</p>
</div>
<div id="comment-84675-info" class="comment-info">
<span class="comment-age">(02 Jun '22, 12:27)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="84676"></span>
<div id="comment-84676" class="comment">
<div id="post-84676-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>To see what is actually in the database for a particular OSM object, try this (as the user who owns the database)</p>
<pre><code>psql gis
gis=&gt; select * from planet_osm_polygon where osm_id=142724406;
gis=&gt; select * from planet_osm_line where osm_id=142724406;
gis=&gt; select * from planet_osm_point where osm_id=142724406;</code></pre>
<p>nodes will be in planet_osm_point, unclosed ways and relations in planet_osm_line, and closed ways and relations in planet_osm_polygon.</p>
<p>You can look at the tags in there to see what tags are "escaping into the database" for a particular feature. You can also do things like this:</p>
<pre><code>select count(*) from planet_osm_line where name=&#39;High Street&#39;;</code></pre>
</div>
<div id="comment-84676-info" class="comment-info">
<span class="comment-age">(02 Jun '22, 12:33)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="84735"></span>
<div id="comment-84735" class="comment">
<div id="post-84735-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hey <a href="https://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a>, I tried playing around with some of that stuff you suggested but I'm going to be honest, this is far beyond me.</p>
<p>Really not where to start or what to do. I really appreciate your advice/assistance. Might just have to leave it here for now.</p>
</div>
<div id="comment-84735-info" class="comment-info">
<span class="comment-age">(08 Jun '22, 12:14)</span> <span class="comment-user userinfo">hicallmeal</span>
</div>
</div>
<span id="84736"></span>
<div id="comment-84736" class="comment not_top_scorer">
<div id="post-84736-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ultimately, if you want to change the way that osm2pgsql / renderd / mapnik displays things, you do need some sort of basic knowledge of the database that underpins it.</p>
<p>Does anything at <a href="https://ircama.github.io/osm-carto-tutorials/">https://ircama.github.io/osm-carto-tutorials/</a> help? Failing that, would <a href="https://umap.openstreetmap.fr/en/">https://umap.openstreetmap.fr/en/</a> allow you to do whatever you are trying to do?</p>
</div>
<div id="comment-84736-info" class="comment-info">
<span class="comment-age">(08 Jun '22, 14:25)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-84564" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-84564-form-container" class="comment-form-container">
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


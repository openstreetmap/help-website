+++
type = "question"
title = "Best way to serve tiles in multiple languages"
description = '''Hi, I&#x27;ve successfully installed an OSM tileserver following the switch2osm tutorial and using the OSM-Bright style. All the labels are in the country original language, but I need my server to be able to serve tiles in differents languages, depending of the current user locale, falling back to Engli...'''
date = "2018-07-11T14:31:00Z"
lastmod = "2019-08-01T08:37:00Z"
weight = 64655
keywords = [ "internationalization", "language", "tileserver" ]
aliases = [ "/questions/64655" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Best way to serve tiles in multiple languages](/questions/64655/best-way-to-serve-tiles-in-multiple-languages)

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
<span id="post-64655-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64655-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-64655-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I've successfully installed an OSM tileserver following the <a href="https://switch2osm.org/manually-building-a-tile-server-18-04-lts/">switch2osm</a> tutorial and using the OSM-Bright style. All the labels are in the country original language, but I need my server to be able to serve tiles in differents languages, depending of the current user locale, falling back to English or country language if the name is not found in his locale.</p>
<p>How do I do that? I've seen some posts relative to internationalization, talking about a "name:en" column in the planet_osm_point table, but I don't have it in my db (although I used the --hstore option with osm2pgsql). Is that normal?</p>
<p>Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-internationalization" rel="tag" title="see questions tagged &#39;internationalization&#39;">internationalization</span> <span class="post-tag tag-link-language" rel="tag" title="see questions tagged &#39;language&#39;">language</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Jul '18, 14:31</strong></p>
<img src="https://secure.gravatar.com/avatar/32a7da9bf999cc0ea4f6befea00edd8d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="voharunado&#39;s gravatar image" />
<p><span>voharunado</span><br />
<span class="score" title="66 reputation points">66</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="voharunado has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-64655" class="comments-container">
<span id="70257"></span>
<div id="comment-70257" class="comment">
<div id="post-70257-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have successfully installed an OSM tile server using ubuntu Image. but I would like to render tiles in three languages. any pointers will be helpful.</p>
</div>
<div id="comment-70257-info" class="comment-info">
<span class="comment-age">(31 Jul '19, 17:14)</span> <span class="comment-user userinfo">singhy</span>
</div>
</div>
<span id="70262"></span>
<div id="comment-70262" class="comment">
<div id="post-70262-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>@singhi: I've converted your question into a comment since it is not an answer to the original question.</p>
<p>It would probably best if you started a new question and explained where you still need help after reading all the hints on this page and the linked ones. I mean all the answers and comments here talk about setting up rendering of tiles for multiple languages and you still ask for pointers.</p>
</div>
<div id="comment-70262-info" class="comment-info">
<span class="comment-age">(31 Jul '19, 21:39)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="70276"></span>
<div id="comment-70276" class="comment">
<div id="post-70276-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi TZorn, I have also setup a tile server for a default language. I am looking for a similar solution as voharunado however I would like to have language name in the URL so user can select the language of choice. and the application render the language specific tiles.</p>
</div>
<div id="comment-70276-info" class="comment-info">
<span class="comment-age">(01 Aug '19, 08:37)</span> <span class="comment-user userinfo">singhy</span>
</div>
</div>
</div>
<div id="comment-tools-64655" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64655-form-container" class="comment-form-container">
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

<span id="64656"></span>

<div id="answer-container-64656" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64656-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64656-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-64656-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="voharunado has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You have the names in your <code>tags</code> column if you used the <code>--hstore</code> option.</p>
<p>It is therefore possible to change your SELECT statements from something like e.g.</p>
<pre><code>SELECT name, highway, way FROM planet_osm_line</code></pre>
<p>to</p>
<pre><code>SELECT COALESCE(tags-&gt;&#39;name:fi&#39;, tags-&gt;&#39;name:en&#39;, tags-&gt;&#39;int_name&#39;, name) as name, highway, ...</code></pre>
<p>which would then, in this example, prefer a Finnish name if set, then the English name, then the international name, an then the local name.</p>
<p>You have to make separate copies of your style for every language you wish to support, and set up separate URLs. Since you are producing raster tiles where labels are inseparatable from other content, you will need separate tile caches for each style, and you will want to pre-render each style on low zoom levels too.</p>
<p>This is only practicable if you are supporting a small number of languages.</p>
<p>If you want to be able to support "any language", you will have to change your approach altogether and use a vector tile based solution.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Jul '18, 15:53</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-64656" class="comments-container">
<span id="64658"></span>
<div id="comment-64658" class="comment">
<div id="post-64658-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks Frederik. It works, I was trying to access it with the column name "name:fr"... I didn't understand this thing at all.</p>
<p>I need to support 6 languages (including english) but it could increase in the future. If vector tiles is not a lot more complicated, I'll probably go for that if it allows me to have a more evolutive server. But is the osm-bright style compatible with vector tiles? And do you have a link to a tutorial like switch2osm to learn how to use vector tiles please?</p>
</div>
<div id="comment-64658-info" class="comment-info">
<span class="comment-age">(11 Jul '18, 17:03)</span> <span class="comment-user userinfo">voharunado</span>
</div>
</div>
<span id="64660"></span>
<div id="comment-64660" class="comment">
<div id="post-64660-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>A vector tiles setup is decidedly more complicated. The OSM Bright you have is not a vector tile style, but free vector tile styles exist that look similar. Most toolchains that produce vector tiles use an awful lot of Javascript-based components. Check out openmaptiles.org. You also need to decide whether you will serve vector tiles to the client and have them rendered there (requires even more Javascript on the client side) or whether you want to convert to raster tiles on the fly server-side. There's no tutorial I know of, but the makers of switch2osm would surely welcome a write-up once you've conquered the topic ;)</p>
</div>
<div id="comment-64660-info" class="comment-info">
<span class="comment-age">(11 Jul '18, 18:16)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="64671"></span>
<div id="comment-64671" class="comment">
<div id="post-64671-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>We've considered openmaptiles.org but we are looking for a less expensive solution, that's why we're making our own server. I'm not sure I'll be able to write any tutorial about the subject, it looks really more complicated to setup and I'll probably don't have the time to do this :) If 6 languages is ok to serve with raster tiles, I think it's better if we stay with that.</p>
<p>Thanks again!</p>
</div>
<div id="comment-64671-info" class="comment-info">
<span class="comment-age">(12 Jul '18, 09:54)</span> <span class="comment-user userinfo">voharunado</span>
</div>
</div>
<span id="64672"></span>
<div id="comment-64672" class="comment">
<div id="post-64672-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The whole openmaptiles.org stack is available as Open Source and you can install it yourselves like the raster tile stack.</p>
</div>
<div id="comment-64672-info" class="comment-info">
<span class="comment-age">(12 Jul '18, 09:57)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="64673"></span>
<div id="comment-64673" class="comment">
<div id="post-64673-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Oh yes, what I've tried is the very easy setup docker image available on openmaptiles.org, which required a subscription to get fresh data. So if I don't want to use this service, I need to setup my own tileserver-gl with a way to generate vector tiles? You just said it was more complicated and you didn't know any tutorial, but there is tutorials on openmaptiles.org and it seems very easy... So I think there is obviously something I don't understand...</p>
</div>
<div id="comment-64673-info" class="comment-info">
<span class="comment-age">(12 Jul '18, 10:35)</span> <span class="comment-user userinfo">voharunado</span>
</div>
</div>
</div>
<div id="comment-tools-64656" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64656-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="64674"></span>

<div id="answer-container-64674" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64674-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64674-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-64674-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Using COALESCE give me some strange results : I'm requesting some Paris tiles in french, so for that I'm doing <code>COALESCE(tags-&gt;'name:fr', tags-&gt;'name:en', tags-&gt;'int_name', name)</code>. But as you can see on the picture below, it sometimes shows both english and french names (like "Paris 18e Arrondissement" is the french name, and "18th Arrondissement" the english name).</p>
<p><img src="/upfiles/paris_fr.png" alt="alt text" /></p>
<p>Why? I suppose it is because there is two differents labels for the same thing, but one with no french name... How do I prevent that? Is there a way to use directly the "name" attribute if the requested language is the language of the place we are looking at? (seems a bit tricky when writing this...)</p>
<p>Thanks!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Jul '18, 11:55</strong></p>
<img src="https://secure.gravatar.com/avatar/32a7da9bf999cc0ea4f6befea00edd8d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="voharunado&#39;s gravatar image" />
<p><span>voharunado</span><br />
<span class="score" title="66 reputation points">66</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="voharunado has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-64674" class="comments-container">
<span id="64675"></span>
<div id="comment-64675" class="comment">
<div id="post-64675-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Most likely you have a <code>place=suburb</code> node with a French name and <code>boundary=adminsitrative</code> polygon without, or vice versa. The doubling of place names can be a problem even when you're not playing with languages. It is possible to analyse the situation in SQL and decide not to render a label in certain cases, but not easy and makes rendering slower. Yes it is possible to have different rendering rules depending on where in the world you are but this, also, slows down rendering a bit. See e.g. this SELECT statement in the old MapQuest style: <a href="https://github.com/MapQuest/MapQuest-Mapnik-Style/blob/updates2/mapquest_inc/layer-streetnames-eu.xml.inc#L569-L587">https://github.com/MapQuest/MapQuest-Mapnik-Style/blob/updates2/mapquest_inc/layer-streetnames-eu.xml.inc#L569-L587</a> - combine this with an SQL CASE statement and you could do something that prefers name over name:en in France, but name:en over name in China.</p>
</div>
<div id="comment-64675-info" class="comment-info">
<span class="comment-age">(12 Jul '18, 12:35)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="64677"></span>
<div id="comment-64677" class="comment">
<div id="post-64677-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks again Frederik! I don't really need that much info on my map, so I will disable the display of one of them and see what happens, it will probably be faster</p>
</div>
<div id="comment-64677-info" class="comment-info">
<span class="comment-age">(12 Jul '18, 13:23)</span> <span class="comment-user userinfo">voharunado</span>
</div>
</div>
<span id="64681"></span>
<div id="comment-64681" class="comment">
<div id="post-64681-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Actually the problem is bigger than expected, some of the Paris suburbs have a name:fr, some other have not. So even if I keep only these ones, I still have a problem because the names aren't always in the same language.</p>
<p>I've looked at the link you gave me, but I don't understand what this statement does. I don't have a "country_polygon_detail" table so I don't understand what I need to do to get the current country code...</p>
</div>
<div id="comment-64681-info" class="comment-info">
<span class="comment-age">(12 Jul '18, 15:24)</span> <span class="comment-user userinfo">voharunado</span>
</div>
</div>
<span id="64682"></span>
<div id="comment-64682" class="comment">
<div id="post-64682-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>The link was meant as an illustration of how you have to do it <em>basically</em>, not something you can just copy and it works. Basically you need a table that contains the outlines of areas for which you want to have special casing, and then you need to join the OSM feature table with that table on geometry to find out which of your areas of interest the feature is in. You could generate that area-of-interest table from your existing planet_osm_polygon by picking out the requisite admin_level=2 boundaries but you should definitely apply simplification to keep perfomance acceptable.</p>
</div>
<div id="comment-64682-info" class="comment-info">
<span class="comment-age">(12 Jul '18, 15:33)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="64683"></span>
<div id="comment-64683" class="comment not_top_scorer">
<div id="post-64683-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Actually all area are of interest for us, we need to display the best name possible for all of our clients, depending on their language. It definitely looks a bit tricky so I'll probably look for another way to get over this issue. Thanks for your help!</p>
</div>
<div id="comment-64683-info" class="comment-info">
<span class="comment-age">(12 Jul '18, 15:50)</span> <span class="comment-user userinfo">voharunado</span>
</div>
</div>
<span id="64684"></span>
<div id="comment-64684" class="comment">
<div id="post-64684-score" class="comment-score">
1
</div>
<div class="comment-text">
<blockquote>
<p>Actually the problem is bigger than expected, some of the Paris suburbs have a name:fr, some other have not.</p>
</blockquote>
<p>You can always pre-process the data so that (for example) within the area of France "name:fr" is always populated with something (from "name "if "name:fr" was blank).</p>
<p>As an example, <a href="https://github.com/SomeoneElseOSM/SomeoneElse-style/blob/master/update_render.sh">this script</a> is part of the process to create the maps behind <a href="https://map.atownsend.org.uk/maps/map/map.html">this map</a>, and on there "name:cy", "name:en" or "name:gd" will be used as "name" depending on location. You may actually want to do the reverse of that (set "name" to "name:fr" in a defined area) but the principle is the same.</p>
</div>
<div id="comment-64684-info" class="comment-info">
<span class="comment-age">(12 Jul '18, 17:38)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="64694"></span>
<div id="comment-64694" class="comment not_top_scorer">
<div id="post-64694-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks SomeoneElse it looks great, I'll try that!</p>
</div>
<div id="comment-64694-info" class="comment-info">
<span class="comment-age">(13 Jul '18, 09:07)</span> <span class="comment-user userinfo">voharunado</span>
</div>
</div>
</div>
<div id="comment-tools-64674" class="comment-tools">
<span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-64674-form-container" class="comment-form-container">
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


+++
type = "question"
title = "Fix Incomplete Geometries"
description = '''How can I fix the incomplete geometries of ways and relations on a local OSM server? This problem has plagued me for a while now but hasn&#x27;t caused any major issues, until a few days ago when the USA relation (148838) and the Canada relation (1428125) broke for me. My server does daily updates, and I...'''
date = "2021-08-12T15:14:00Z"
lastmod = "2021-08-13T20:59:00Z"
weight = 81289
keywords = [ "overpass", "overpass-turbo", "overpass-api", "database" ]
aliases = [ "/questions/81289" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Fix Incomplete Geometries](/questions/81289/fix-incomplete-geometries)

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
<span id="post-81289-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81289-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81289-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How can I fix the incomplete geometries of ways and relations on a local OSM server?</p>
<p>This problem has plagued me for a while now but hasn't caused any major issues, until a few days ago when the USA relation (148838) and the Canada relation (1428125) broke for me. My server does daily updates, and I was hoping that would fix it, but it hasn't yet. In fact, I assume that the daily updates are the cause of the problem in the first place. There's nothing else changing the database so unless some extraneous other event happened, that would be the only place for things to go wrong.</p>
<p>Looking at the relations in overpass turbo it says "Attention: incomplete geometry (e.g. some nodes missing)" for both of them. This also causes any area filtering using that relation's area to be completely wrong as well as not giving nearly enough results.</p>
<p>I've had this same problem for a while now but have been able to find workarounds to get the query results that I want, but the USA relation and Canada relation breaking is something that I cannot work around.</p>
<p>Any help at all would be <em>greatly</em> appreciated!</p>
<p>Edit: Found more of the specifics. The two nodes that don't exist in my local sever that are causing the problem are <a href="https://www.openstreetmap.org/node/8856238004">8856238004</a> and <a href="https://www.openstreetmap.org/node/8856295638">8856295638</a>, both of which are part of the relation for USA and Canada. They are also part of way <a href="https://www.openstreetmap.org/way/957074345#map=17/44.99673/-74.51237">957074345</a>, which does not exist at all on my server. The way itself and all of the nodes that are a part of it just don't exist for me.</p>
<p>Edit 2: In the bin/nohup.out file of my server it has a <em>lot</em> of lines that say something like</p>
<pre><code>compute_geometry: Node 8856295638 used in way 571733868 not found.</code></pre>
Where the actual node and way numbers vary, but all of the node values are in a range between 8853109156 ~ 8861281943 (not exact range). There's similar statements for missing ways for relations.
<p>It has these statements once a day, I assume, when it updates because the time stamps right before them are the same range as the update times.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-overpass-api" rel="tag" title="see questions tagged &#39;overpass-api&#39;">overpass-api</span> <span class="post-tag tag-link-database" rel="tag" title="see questions tagged &#39;database&#39;">database</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Aug '21, 15:14</strong></p>
<img src="https://secure.gravatar.com/avatar/90c1a2a6f8b3789f0622ae27f3d92bd6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nbreden&#39;s gravatar image" />
<p><span>nbreden</span><br />
<span class="score" title="26 reputation points">26</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nbreden has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Aug '21, 16:20</strong> </span></p>
</div>
</div>
<div id="comments-container-81289" class="comments-container">
&#10;</div>
<div id="comment-tools-81289" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81289-form-container" class="comment-form-container">
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

<span id="81290"></span>

<div id="answer-container-81290" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81290-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81290-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-81290-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="nbreden has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You write "a local OSM server" which I take to mean "a local Overpass server". I can't debug what the problem is exactly; I wonder if maybe you missed an update at some point and therefore are missing ways or so. If you can afford to, switching to regular full imports will of course get rid of the problem. To fix the issue at hand, you could also cheat by:</p>
<ol>
<li>identifying the IDs of all missing objects</li>
<li>using <code>osmium getid</code> to extract the objects with these IDs from a planet file (or North America file or so), be sure to save them in the "osc" format</li>
<li>feeding the resulting .osc file(s) into the update process of Overpass</li>
</ol>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Aug '21, 16:34</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-81290" class="comments-container">
<span id="81291"></span>
<div id="comment-81291" class="comment">
<div id="post-81291-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the response! Yes, I do mean "a local Overpass server", sorry for any confusion.</p>
<p>Could you expand more on what you mean by "switching to regular full imports"? Do you mean to do <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Installation#Populating_the_DB">this</a> regularly instead of what I'm doing currently which is from <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Installation#Applying_minutely_.28or_hourly.2C_or_daily.29_diffs">these</a> steps?</p>
</div>
<div id="comment-81291-info" class="comment-info">
<span class="comment-age">(12 Aug '21, 16:42)</span> <span class="comment-user userinfo">nbreden</span>
</div>
</div>
<span id="81292"></span>
<div id="comment-81292" class="comment">
<div id="post-81292-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, that's what I mean, of course you would not load a full planet but just the area of interest. If you have enough disk space, it is also possible to run the import into a secondary database and keep the "production" database running, and then switch over once the import is complete. This would give you only a minimal service interruption.</p>
</div>
<div id="comment-81292-info" class="comment-info">
<span class="comment-age">(12 Aug '21, 17:03)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="81294"></span>
<div id="comment-81294" class="comment">
<div id="post-81294-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hmm, I'm a bit confused. So with the database that I've setup following <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Installation">these</a> instructions, I can take an extract from <a href="http://download.openstreetmap.fr/extracts/">here</a> and apply it to the database? I can't find how to apply a .pbf to the database, or if I convert it to a different format using something like <a href="https://wiki.openstreetmap.org/wiki/Osmconvert#Converting_Files">osmconvert</a>, I still can't find anything to apply a different format to the database... I feel like <a href="https://wiki.openstreetmap.org/wiki/OsmChange">.osc</a> is what I want but I'm not sure. Sorry if I'm missing something obvious.</p>
</div>
<div id="comment-81294-info" class="comment-info">
<span class="comment-age">(13 Aug '21, 12:43)</span> <span class="comment-user userinfo">nbreden</span>
</div>
</div>
<span id="81295"></span>
<div id="comment-81295" class="comment">
<div id="post-81295-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>We might be confusing the concepts of "database engine" and "database content" here. Once you've set up the Overpass database engine, you have to load a data set - either the planet-wide data, or a regional excerpt. If you choose the "cloning from the dev server" option you always get a world-wide database. If you choose the "populate the overpass database from a planet file" path you have a choice of loading the full planet, or an extract. This needs to be supplied to the <code>update_database</code> script in plain XML form on stdin, so if you download a .osm.pbf file you will want to do something like</p>
<pre><code> osmium cat -f osm somefile.osm.pbf | update_database --db-dir=somedir --meta</code></pre>
<p>(you will note that the init_osm3s.sh script mentioned in the install instructions does something similar - if you have a .osm.bz2 file and not an .osm.pbf file then you do not need osmium and can use "bzcat" instead).</p>
<p>Loading a file this way will <em>replace</em> your current database with the new data. Any process that works with .osc files will <em>augment</em> your already existing data.</p>
</div>
<div id="comment-81295-info" class="comment-info">
<span class="comment-age">(13 Aug '21, 13:30)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="81297"></span>
<div id="comment-81297" class="comment">
<div id="post-81297-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That cleared up a <em>lot</em> for me, thanks. So I tried that out with this command:</p>
<pre><code>osmium cat -f osm ../canada.osm.pbf | ./bin/update_database --db-dir=./db/</code></pre>
<p>And it didn't do anything? It went through saying</p>
<pre><code>elapsed node 721769976. Flushing to database ...... done.     ]   4%              ]   0%</code></pre>
<p>...</p>
<pre><code>compute_geometry: Node 9002479052 used in way 19693304 not found.</code></pre>
<p>From my understanding (which may be wrong) this shouldn't be happening? I thought it would be taking information from canada.osm.pbf (which presumably doesn't have missing nodes like this) and replacing my current database with that information.</p>
</div>
<div id="comment-81297-info" class="comment-info">
<span class="comment-age">(13 Aug '21, 17:01)</span> <span class="comment-user userinfo">nbreden</span>
</div>
</div>
<span id="81298"></span>
<div id="comment-81298" class="comment not_top_scorer">
<div id="post-81298-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I won't delete my previous comment, but it's wrong. Your command <em>did</em> work! Thank you so much! I think this will be enough of a solution for my problems.</p>
</div>
<div id="comment-81298-info" class="comment-info">
<span class="comment-age">(13 Aug '21, 20:59)</span> <span class="comment-user userinfo">nbreden</span>
</div>
</div>
</div>
<div id="comment-tools-81290" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-81290-form-container" class="comment-form-container">
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


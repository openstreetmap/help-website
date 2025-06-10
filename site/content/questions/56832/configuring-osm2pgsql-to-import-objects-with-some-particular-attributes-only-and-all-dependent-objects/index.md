+++
type = "question"
title = "Configuring osm2pgsql to import objects with some particular attributes only (and all dependent objects)"
description = '''I downloaded a world PBF file and going to use osm2pgsql. I&#x27;m only interested in a small subset of data:  administrative boundaries (type=boundary&amp;amp;boundary=administrative) all kind of cities, towns, villages etc (place=...) - I actually just need their coordinates/polygons, names and populations...'''
date = "2017-07-02T06:06:00Z"
lastmod = "2018-11-05T12:05:00Z"
weight = 56832
keywords = [ "osm2pgsql" ]
aliases = [ "/questions/56832" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Configuring osm2pgsql to import objects with some particular attributes only (and all dependent objects)](/questions/56832/configuring-osm2pgsql-to-import-objects-with-some-particular-attributes-only-and-all-dependent-objects)

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
<span id="post-56832-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56832-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-56832-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I downloaded a world <code>PBF</code> file and going to use <code>osm2pgsql</code>. I'm only interested in a small subset of data:</p>
<ul>
<li>administrative boundaries (type=boundary&amp;boundary=administrative)</li>
<li>all kind of cities, towns, villages etc (place=...) - I actually just need their coordinates/polygons, names and populations</li>
</ul>
<p>Is there a way to configure <code>osm2pgsql</code> in such a way that only those nodes, ways and polygons are created in database which make up administrative boundaries and city/towns/etc with their respective names, populations and coordinates?</p>
<p>In my understand, I should:</p>
<ul>
<li>not use any <code>hstore</code>-related command line options when importing</li>
<li>remove everything from the <code>default.style</code> file and only list attributes that I'm interested in:
<ul>
<li>boundary:administrative <em>(how do I only import objects with attributes containing a particular value?)</em></li>
<li>type:boundary</li>
<li>place</li>
<li>name</li>
<li>population</li>
<li>population:date</li>
<li>source:population</li>
</ul></li>
</ul>
<p>Will this make the <code>osm2pgsql</code> tool to only store objects that I need (and dependent objects) and discard any other objects?</p>
<p><strong>By dependent objects</strong> I mean, for example, nodes that make up a a country boundary. The nodes won't have the attributes listed above, but they are still needed for the boundaries. How do I import these, but not the others?</p>
<p>Am I taking the right course of action, or should I do it in a different way?</p>
<p><strong>The final goal</strong> is to create a database with minimum amount of data that I can query for simple geocoding by place name, and for rendering of administrative map with administrative boundaries only and no other map features. Does it make any sense?</p>
<p>I'm not concerned about the time it will take to import, i.e. it makes no difference for me whether it will be 2 hours or 24 hours. <strong>The only concern is the final amount of data stored in the database</strong>, which I would like to reduce as much as possible.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Jul '17, 06:06</strong></p>
<img src="https://secure.gravatar.com/avatar/c9a1577cedad5cf1af59379a5bd6721b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="meglio&#39;s gravatar image" />
<p><span>meglio</span><br />
<span class="score" title="40 reputation points">40</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="meglio has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Jul '17, 06:11</strong> </span></p>
</div>
</div>
<div id="comments-container-56832" class="comments-container">
<span id="66571"></span>
<div id="comment-66571" class="comment">
<div id="post-66571-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi <a href="https://help.openstreetmap.org/users/13884/meglio">@meglio</a>, did you find a way to accomplish this? I'm looking to import only a fraction of all the features too.</p>
</div>
<div id="comment-66571-info" class="comment-info">
<span class="comment-age">(30 Oct '18, 17:24)</span> <span class="comment-user userinfo">pierrebonbon</span>
</div>
</div>
<span id="66578"></span>
<div id="comment-66578" class="comment">
<div id="post-66578-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Unfortunately, no.</p>
</div>
<div id="comment-66578-info" class="comment-info">
<span class="comment-age">(31 Oct '18, 01:23)</span> <span class="comment-user userinfo">meglio</span>
</div>
</div>
<span id="66672"></span>
<div id="comment-66672" class="comment">
<div id="post-66672-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/13884/meglio">@meglio</a> that's a bummer, was hoping that there's was some way to make the import leaner. :-(</p>
</div>
<div id="comment-66672-info" class="comment-info">
<span class="comment-age">(05 Nov '18, 12:05)</span> <span class="comment-user userinfo">pierrebonbon</span>
</div>
</div>
</div>
<div id="comment-tools-56832" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56832-form-container" class="comment-form-container">
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

<span id="56841"></span>

<div id="answer-container-56841" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56841-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56841-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-56841-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You could consider using osmfilter and osmconvert to preprocess the .osm.pbf file even before it gets to osm2pgsql.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Jul '17, 22:03</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-56841" class="comments-container">
<span id="56847"></span>
<div id="comment-56847" class="comment">
<div id="post-56847-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks <a href="https://help.openstreetmap.org/users/5/richard">@Richard</a>. Should I consider <code>--ignore-dependencies</code> if I only need my geometries of my target objects and no of separate nodes / ways from which the former consist?</p>
</div>
<div id="comment-56847-info" class="comment-info">
<span class="comment-age">(03 Jul '17, 10:54)</span> <span class="comment-user userinfo">meglio</span>
</div>
</div>
<span id="56964"></span>
<div id="comment-56964" class="comment">
<div id="post-56964-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I would not advise using the --ignore-dependencies option because you will need nodes as they are of the only OSM object type which holds coordinates. Here is an example how to prefilter OSM data and even update the database with prefiltered data: <a href="https://wiki.openstreetmap.org/wiki/Openptmap/Installation#Fill_the_Database">https://wiki.openstreetmap.org/wiki/Openptmap/Installation#Fill_the_Database</a></p>
</div>
<div id="comment-56964-info" class="comment-info">
<span class="comment-age">(08 Jul '17, 20:36)</span> <span class="comment-user userinfo">Marqqs</span>
</div>
</div>
</div>
<div id="comment-tools-56841" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56841-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="56833"></span>

<div id="answer-container-56833" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56833-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56833-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-56833-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><code>osm2pgsql</code> manages two sets of tables. The first set, the <em>geoemtry tables</em>, consists of <code>planet_osm_polygon</code>, <code>planet_osm_line</code>, <code>planet_osm_roads</code>, and <code>planet_osm_point</code>. These tables will contain the geometries you are interested in, and because they already contain ready-made geometries, no dependencies on other objects exist. Using the procedure you have outlined you will end up with a fairly minimal data set in these tables, although - and I believe this depends on the osm2pgsql version you use - there might be some duplication with both boundary lines <em>and</em> boundary polygons being generated.</p>
<p>The second set of tables, the <em>slim tables</em>, contain more or less raw OSM objects, in the adequatly named <code>planet_osm_nodes</code>, <code>planet_osm_ways</code>, and <code>planet_osm_rels</code> tables. These tables are only created if you import with <code>--slim</code>, and they will contain nearly all OSM objects, independent of your style file. That's several hundred GB in the case of a full planet import. Using <code>--slim</code> is definitely required if you want to import incremental updates, and even when you don't, <code>--slim</code> reduces RAM usage during the initial import. If you only use <code>--slime</code> to reduce RAM usage, combine with <code>--drop</code> to drop the slim tables after the import.</p>
<p>Long story short, you can reduce the total database size significantly using the process you outline, but only if don't need incremental updates.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Jul '17, 09:26</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-56833" class="comments-container">
<span id="56844"></span>
<div id="comment-56844" class="comment">
<div id="post-56844-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/104/frederik-ramm">@frederik</a>-ramm "no dependencies on other objects exist" - this is a gotcha moment, many thanks! If I understand correctly, slim tables are populated first as a normalized version of the data file, then geometry tables are populated out of those. If I need to experiment with <code>osm2pgsql</code> and let it populate various content for the geometry tables, is there a way to skip production of the <code>slim</code> tables on every run, and let the tool reuse the existing <code>slim</code> tables instead?</p>
</div>
<div id="comment-56844-info" class="comment-info">
<span class="comment-age">(03 Jul '17, 08:21)</span> <span class="comment-user userinfo">meglio</span>
</div>
</div>
<span id="56846"></span>
<div id="comment-56846" class="comment">
<div id="post-56846-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/104/frederik-ramm">@frederik</a>, may you please also clarify is my understanding is correct: whatever columns I specify in the <code>.style</code> file, if all values are null/empty for a particular object, the object is discarded and will not be present in the geometry tables. If so, how do I save names of cities, but discard all other objects that contain a <code>name</code> attribute?</p>
</div>
<div id="comment-56846-info" class="comment-info">
<span class="comment-age">(03 Jul '17, 09:52)</span> <span class="comment-user userinfo">meglio</span>
</div>
</div>
</div>
<div id="comment-tools-56833" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56833-form-container" class="comment-form-container">
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


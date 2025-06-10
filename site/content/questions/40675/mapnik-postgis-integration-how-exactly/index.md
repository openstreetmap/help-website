+++
type = "question"
title = "Mapnik PostGIS integration - how exactly?"
description = '''The OSM help wiki page on Mapnik states: It can read ESRI shapefiles, PostGIS, TIFF rasters, .osm files, any GDAL or OGR supported formats, CSV files, and more.  How exactly does Mapnik integrates with PostGIS? To me saying &quot;Mapnik can read PostGIS&quot; is kind of like saying &quot;Wordpress can read MySQL&quot;....'''
date = "2015-01-28T22:13:00Z"
lastmod = "2015-01-31T11:10:00Z"
weight = 40675
keywords = [ "postgis", "mapnik" ]
aliases = [ "/questions/40675" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Mapnik PostGIS integration - how exactly?](/questions/40675/mapnik-postgis-integration-how-exactly)

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
<span id="post-40675-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40675-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-40675-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>The <span>OSM help wiki page on Mapnik</span> states:</p>
<pre><code>It can read ESRI shapefiles, PostGIS, TIFF rasters, .osm files, any GDAL or OGR supported formats, CSV files, and more.</code></pre>
<p>How exactly does Mapnik integrates with PostGIS? To me saying "Mapnik can read PostGIS" is kind of like saying "Wordpress can read MySQL". Obviously Wordpress is heavily reliant on a given schema existing within that database. So what are the rules? What is Mapnik expecting to find / what must the PostGIS provide?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Jan '15, 22:13</strong></p>
<img src="https://secure.gravatar.com/avatar/e1430f9a10b98409c90b5a0f78c15ca1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mapgenius323&#39;s gravatar image" />
<p><span>mapgenius323</span><br />
<span class="score" title="46 reputation points">46</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mapgenius323 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Jan '15, 22:25</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-40675" class="comments-container">
<span id="40686"></span>
<div id="comment-40686" class="comment">
<div id="post-40686-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What problem are you trying to solve? Perhaps it might be better to provide a more specific example so that people can provide more specific answers.</p>
<p>Is the question that you're trying to ask actually "do I have to use PostGIS, or can I use a different database instead?"</p>
</div>
<div id="comment-40686-info" class="comment-info">
<span class="comment-age">(29 Jan '15, 08:26)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="40708"></span>
<div id="comment-40708" class="comment">
<div id="post-40708-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>No, I'm not trying to ask that question. I definitely want to at least get a handle on using the PostGIS backend with Mapnik. The problem I'm trying to solve is understanding PostGIS and Mapnik integration in general.</p>
</div>
<div id="comment-40708-info" class="comment-info">
<span class="comment-age">(30 Jan '15, 07:59)</span> <span class="comment-user userinfo">mapgenius323</span>
</div>
</div>
</div>
<div id="comment-tools-40675" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40675-form-container" class="comment-form-container">
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

<span id="40693"></span>

<div id="answer-container-40693" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-40693-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40693-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-40693-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It means what it says. Mapnik can connect to a PostGIS database, and then read the data from that. Within your mapnik style file, you specify the schema you want (connect to this table, the geometry column is called <code>geom</code>/whatever). So it doesn't matter what schema you have in the database, you can tell mapnik to work with it.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Jan '15, 13:05</strong></p>
<img src="https://secure.gravatar.com/avatar/16e12e337f6edc3750681492656097ed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rorym&#39;s gravatar image" />
<p><span>rorym</span><br />
<span class="score" title="5358 reputation points"><span>5.4k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="49 badges"><span class="silver">●</span><span class="badgecount">49</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rorym has 18 accepted answers">11%</span></p>
</div>
</div>
<div id="comments-container-40693" class="comments-container">
<span id="40702"></span>
<div id="comment-40702" class="comment">
<div id="post-40702-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>OK fair. I just need some good examples of Mapnik style file talking to PostGIS. There does not seem to be any in the OSM wiki. Right now I'm in the process of pulling some packages from ppa:kakrueger/openstreetmap repo so I can check out the style files that are apparently in there. Should be what I need.</p>
</div>
<div id="comment-40702-info" class="comment-info">
<span class="comment-age">(29 Jan '15, 19:54)</span> <span class="comment-user userinfo">mapgenius323</span>
</div>
</div>
<span id="40703"></span>
<div id="comment-40703" class="comment">
<div id="post-40703-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>The following styles have or produce mapnik Stylesheets which communicate with postgis / postgres databases (I have most of them up and running at my local server). Maybe this is what you want to find actually:</p>
<p>OSM: <a href="https://github.com/gravitystorm/openstreetmap-carto">https://github.com/gravitystorm/openstreetmap-carto</a> German OSM: <a href="https://github.com/woodpeck/openstreetmap-carto-german">https://github.com/woodpeck/openstreetmap-carto-german</a> OSMBright: <a href="https://github.com/mapbox/osm-bright/">https://github.com/mapbox/osm-bright/</a> OSMNight: <a href="https://github.com/cybercomsweden/osm-night">https://github.com/cybercomsweden/osm-night</a> SwissStyle: <a href="https://github.com/xyztobixyz/OSM-Swiss-Style">https://github.com/xyztobixyz/OSM-Swiss-Style</a> Cassini: <a href="https://github.com/frodrigo/osm-cassini-carto">https://github.com/frodrigo/osm-cassini-carto</a> Blossom: <a href="https://github.com/stekhn/blossom">https://github.com/stekhn/blossom</a></p>
</div>
<div id="comment-40703-info" class="comment-info">
<span class="comment-age">(29 Jan '15, 20:38)</span> <span class="comment-user userinfo">nordie69</span>
</div>
</div>
<span id="40709"></span>
<div id="comment-40709" class="comment">
<div id="post-40709-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/10255/nordie69"></a><a href="http://help.openstreetmap.org/users/10255/nordie69">@nordie69</a> Great links thx. The first one is good for me. I didn't realise OSM now uses CartoCSS for styling (whatever that is). Also lead to <a href="https://trac.openstreetmap.org/browser/subversion/applications/rendering/mapnik/osm.xml">https://trac.openstreetmap.org/browser/subversion/applications/rendering/mapnik/osm.xml</a> which appears to be the old XML style sheet (+4000 lines, holy crap!). This XML also declares a bunch of Layers towards the end.</p>
</div>
<div id="comment-40709-info" class="comment-info">
<span class="comment-age">(30 Jan '15, 08:23)</span> <span class="comment-user userinfo">mapgenius323</span>
</div>
</div>
<span id="40711"></span>
<div id="comment-40711" class="comment">
<div id="post-40711-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>the current style is written in CartoCSS (which is a 'nicer' way to write mapnik style files). It's then converted into mapnik XML with the <code>carto</code> command line tool. (see the <a href="https://github.com/gravitystorm/openstreetmap-carto/blob/master/INSTALL.md">docs on installing it</a> )</p>
</div>
<div id="comment-40711-info" class="comment-info">
<span class="comment-age">(30 Jan '15, 09:04)</span> <span class="comment-user userinfo">rorym</span>
</div>
</div>
<span id="40715"></span>
<div id="comment-40715" class="comment">
<div id="post-40715-score" class="comment-score">
2
</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/10128/mapgenius323">@mapgenius323</a>: "I didn't realise OSM now uses CartoCSS" – you really should just read the Mapnik wiki page. It is mentioned there (prominently in the intro section). You may find other interesting bits on that page.</p>
</div>
<div id="comment-40715-info" class="comment-info">
<span class="comment-age">(30 Jan '15, 13:53)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="40724"></span>
<div id="comment-40724" class="comment not_top_scorer">
<div id="post-40724-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/5179/aseerel4c26"></a><a href="http://help.openstreetmap.org/users/5179/aseerel4c26">@aseerel4c26</a> I did read that page. I missed that though. I disagree that that is prominent. I find the entire OSM wiki a muddle, but that is my personal opinion, and I am still grateful for its existence of course.</p>
</div>
<div id="comment-40724-info" class="comment-info">
<span class="comment-age">(30 Jan '15, 21:53)</span> <span class="comment-user userinfo">mapgenius323</span>
</div>
</div>
</div>
<div id="comment-tools-40693" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-40693-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="40729"></span>

<div id="answer-container-40729" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-40729-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40729-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-40729-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Examining OSM's Mapnik style sheet is the best way to get a feeling for how Mapnik integrates with a Postgres/PostGIS database. This is available at <a href="https://trac.openstreetmap.org/browser/subversion/applications/rendering/mapnik/osm.xml">https://trac.openstreetmap.org/browser/subversion/applications/rendering/mapnik/osm.xml</a>. Note that OSM now specifies its style in <a href="http://wiki.openstreetmap.org/wiki/CartoCSS">CartoCSS</a>, but these CartoCSS style sheets are still compiled into Mapnik XML style sheets. Also see <a href="https://github.com/gravitystorm/openstreetmap-carto">https://github.com/gravitystorm/openstreetmap-carto</a> for more info on CartoCSS.</p>
<p>Basically, Mapnik has an abstraction layer, with drivers for each type of data source ("layer"). These drivers read geometric data in some specific external format in to some internal format used by Mapnik. This internal format geometric data eventually finds its way to symbolizers and onto a canvas via way of "styles", which get attached to each layer. The PostGIS driver requires you to specify a SQL query that returns a table of data. That table must contain a column called "way" of PostGIS type "geometry". The table may contain arbitrary other columns. These other columns can be used to support rendering (how they can be used I don't know yet). But in most cases all that is needed for a symbolizer to render something is the way column. Layers also need a database connection configuration. The following link shows a complete and working, but very basic Mapnik style sheet with a PostGIS layer - <a href="http://pastebin.com/1spMSvA8">http://pastebin.com/1spMSvA8</a></p>
<hr />
P.S. Thanks for help from commenters above. Please feel free to add to or expand on this answer.
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Jan '15, 11:10</strong></p>
<img src="https://secure.gravatar.com/avatar/e1430f9a10b98409c90b5a0f78c15ca1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mapgenius323&#39;s gravatar image" />
<p><span>mapgenius323</span><br />
<span class="score" title="46 reputation points">46</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mapgenius323 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-40729" class="comments-container">
&#10;</div>
<div id="comment-tools-40729" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40729-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="40677"></span>

<div id="answer-container-40677" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-40677-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40677-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-40677-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>What about the section <a href="https://wiki.openstreetmap.org/wiki/Mapnik#PostGIS">Data Sources → PostGIS</a>? Essentially, Mapnik does not care about your database schema as long as you can provide suitable SQL queries that will extract the data for each layer you want to define. The query you provide will be augmented with a bounding box condition by Mapnik, and other than a geometry it only needs to return those column you expect to use in the styling rules that you have written.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Jan '15, 22:31</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Jan '15, 22:58</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span></p>
</div>
</div>
<div id="comments-container-40677" class="comments-container">
<span id="40682"></span>
<div id="comment-40682" class="comment">
<div id="post-40682-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>So the only advantage of having the data in PostGIS is speed and some convenience GIS function? I could essentially have any SQL server and write arbitrary queries in a Mapnik style file?</p>
</div>
<div id="comment-40682-info" class="comment-info">
<span class="comment-age">(29 Jan '15, 06:39)</span> <span class="comment-user userinfo">mapgenius323</span>
</div>
</div>
<span id="40683"></span>
<div id="comment-40683" class="comment">
<div id="post-40683-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>"... and other than a geometry ..." Could you please elaborate on this. I think this is what I'm getting at.</p>
</div>
<div id="comment-40683-info" class="comment-info">
<span class="comment-age">(29 Jan '15, 06:41)</span> <span class="comment-user userinfo">mapgenius323</span>
</div>
</div>
<span id="40684"></span>
<div id="comment-40684" class="comment">
<div id="post-40684-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>"What about the section Data Sources → PostGIS?". I did not find that very helpful.</p>
</div>
<div id="comment-40684-info" class="comment-info">
<span class="comment-age">(29 Jan '15, 06:43)</span> <span class="comment-user userinfo">mapgenius323</span>
</div>
</div>
<span id="40692"></span>
<div id="comment-40692" class="comment">
<div id="post-40692-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/10128/mapgenius323">@mapgenius323</a>: it is not "very" helpful, yes. But more than the cited part of the intro.</p>
</div>
<div id="comment-40692-info" class="comment-info">
<span class="comment-age">(29 Jan '15, 12:50)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-40677" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40677-form-container" class="comment-form-container">
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


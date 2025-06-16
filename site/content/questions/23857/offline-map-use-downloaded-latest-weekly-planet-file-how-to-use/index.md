+++
type = "question"
title = "Offline map use (downloaded latest weekly planet file) - how to use?"
description = '''Guys bare with the silly question. I just searched for a open-source map that I can use on my offline PC...sort of like my own world map. I don&#x27;t want to use Google products...eventually after searching for options I stumbled on OSM. I&#x27;ve downloaded the latest weekly planet file planet-130626.osm.bz...'''
date = "2013-07-01T07:42:00Z"
lastmod = "2013-07-02T08:44:00Z"
weight = 23857
keywords = [ "windows", "offline", "osm", "tagging" ]
aliases = [ "/questions/23857" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Offline map use (downloaded latest weekly planet file) - how to use?](/questions/23857/offline-map-use-downloaded-latest-weekly-planet-file-how-to-use)

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
<span id="post-23857-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23857-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-23857-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Guys bare with the silly question. I just searched for a open-source map that I can use on my offline PC...sort of like my own world map. I don't want to use Google products...eventually after searching for options I stumbled on OSM.</p>
<p>I've downloaded the latest weekly planet file planet-130626.osm.bz2 and the MD5 check is ok so I guess I have the entire OSM map correctly downloaded.</p>
<p>What I want to do is;</p>
<ul>
<li>have the map available to preview on my offline PC, the entire world map</li>
<li>be able to tag places (like pins on Google maps), possibly with short descriptions</li>
</ul>
<p>With the OSM file I have, what is my next step, what software do I need? Thanks a lot.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-offline" rel="tag" title="see questions tagged &#39;offline&#39;">offline</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Jul '13, 07:42</strong></p>
<img src="https://secure.gravatar.com/avatar/88829f7de51e5f3f661076a0a26e97f2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TM23&#39;s gravatar image" />
<p><span>TM23</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TM23 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Jul '13, 07:43</strong> </span></p>
</div>
</div>
<div id="comments-container-23857" class="comments-container">
&#10;</div>
<div id="comment-tools-23857" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23857-form-container" class="comment-form-container">
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

<span id="23858"></span>

<div id="answer-container-23858" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-23858-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23858-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-23858-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The file you have downloaded is not a map; it is a file that contains all the OSM data.</p>
<p>The difference is: A <em>map</em> has a certain map style - how thick the lines for roads are on what zoom scale, what the road colours are, and so on. The <em>data</em> doesn't have a style - it just has the information "there's a road of class so-and-so named so-and-so here".</p>
<p>So if you want to see a map, you need a software that draws a map from the raw data. That is usually called a rendering engine. There are no rendering engines that can directly read the OSM planet file; you will have to pre-process the data in some way. Programs that can preprocess and display the whole planet file are e.g. "gosmore" and "navit", both are however geared towards navigation use and will not show all the area and POI types might be used to from browsing www.openstreetmap.org. Another option is importing the data into a PostgreSQL database and then displaying it with MapServer or TileMill; this might give you a u ser experience more like www.openstreetmap.org but at the cost ~ 400 GB of database storage and a couple days data import.</p>
<p>I would strongly suggest that you start with a small data file, just for a state or a country, to try out the software because processing the whole planet file can take hours or, if you have a small machine, even days.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Jul '13, 08:22</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-23858" class="comments-container">
<span id="23859"></span>
<div id="comment-23859" class="comment">
<div id="post-23859-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you very much for your answer Frederik.</p>
<p>I can't believe that it's so "complicated" to have a map on your computer. Is there a non-navigational map, without street level detail that can serve the purpose?</p>
</div>
<div id="comment-23859-info" class="comment-info">
<span class="comment-age">(01 Jul '13, 08:28)</span> <span class="comment-user userinfo">TM23</span>
</div>
</div>
</div>
<div id="comment-tools-23858" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23858-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="23861"></span>

<div id="answer-container-23861" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-23861-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23861-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-23861-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Continuing after Frederiks's good answer regarding the use of the planet file …</p>
<p>(some found via <span>questions tagged "offline"</span>) you could use those other, maybe more easy, options:</p>
<ul>
<li><a href="/questions/18416/downloading-maps-in-order-to-use-marble-offline">marble</a> (vector data rendering on-the-fly or tile download [please no high level zoom tiles!]) (I am not sure if marking locations is possible) or<br />
</li>
<li>the list in that question: <a href="/questions/5374/">offline-map-software-for-windows</a></li>
<li>look in this list: <span>Software/Desktop#Map_display_features</span></li>
<li><span>QLandkarte GT</span> (or the commercial <span>BaseCamp</span>) might be useful too (they use <span>pre-made Garmin image files (using OSM data)</span>)</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Jul '13, 13:52</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Jul '13, 00:18</strong> </span></p>
</div>
</div>
<div id="comments-container-23861" class="comments-container">
<span id="23864"></span>
<div id="comment-23864" class="comment">
<div id="post-23864-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I've installed QLandkarte GT...and I can zoom in on any part of the world. So that's due to internet access I guess.</p>
<p>Is there a way to have this level of functionality without internet access?</p>
</div>
<div id="comment-23864-info" class="comment-info">
<span class="comment-age">(01 Jul '13, 15:49)</span> <span class="comment-user userinfo">TM23</span>
</div>
</div>
<span id="23883"></span>
<div id="comment-23883" class="comment">
<div id="post-23883-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The simplest solution is. Garmin BaseCamp is a free download and as a basic world map. If you wish to use OSM with it, and with more detail you can by downloading a garmin.img file see OSM on Garmin in the wiki for details. <a href="https://wiki.openstreetmap.org/w/index.php?search=basecamp&amp;title=Special%3ASearch">https://wiki.openstreetmap.org/w/index.php?search=basecamp&amp;title=Special%3ASearch</a></p>
</div>
<div id="comment-23883-info" class="comment-info">
<span class="comment-age">(01 Jul '13, 21:51)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="23885"></span>
<div id="comment-23885" class="comment">
<div id="post-23885-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@TM23</span>: I do not use it myself, but you should be able to use garmin image files (like in basecamp; download linked in my answer) in Qlandkarte GT. They can be downloaded for offline use.</p>
</div>
<div id="comment-23885-info" class="comment-info">
<span class="comment-age">(02 Jul '13, 01:15)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="23890"></span>
<div id="comment-23890" class="comment">
<div id="post-23890-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><span>@TM23</span> At least Marble is able to cache tiles and to download tiles for user-defined areas. However you have to respect the <a href="https://wiki.openstreetmap.org/wiki/Tile_usage_policy">tile usage policy</a> and keep in mind that <a href="https://wiki.openstreetmap.org/wiki/Tile_Disk_Usage">tiles are large</a>.</p>
</div>
<div id="comment-23890-info" class="comment-info">
<span class="comment-age">(02 Jul '13, 08:44)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-23861" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23861-form-container" class="comment-form-container">
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


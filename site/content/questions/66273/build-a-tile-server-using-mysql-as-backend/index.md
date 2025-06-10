+++
type = "question"
title = "build a tile server using MySQL as backend"
description = '''I need to set up a tile server using MySQL but cannot find any documentation for it. I have done it with Postgres by following this link and it works fine. I understand that after downloading the data from planet OSM I need to use osm2pgsql to store the data in Postgres. Is there any similar tool fo...'''
date = "2018-10-10T21:49:00Z"
lastmod = "2019-02-26T22:07:00Z"
weight = 66273
keywords = [ "osmosis", "tileserver", "osm2pgsql", "mapnik", "mysql" ]
aliases = [ "/questions/66273" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [build a tile server using MySQL as backend](/questions/66273/build-a-tile-server-using-mysql-as-backend)

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
<span id="post-66273-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66273-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-66273-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I need to set up a tile server using MySQL but cannot find any documentation for it. I have done it with Postgres by following this link and it works fine. I understand that after downloading the data from planet OSM I need to use osm2pgsql to store the data in Postgres. Is there any similar tool for MySQL?</p>
<p>Also, would Osmosis, Mapnik and Mod_tile work with MySQL?</p>
<p>I absolutely cannot use Postgres. Is there a step to step guide for MySQL?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-mysql" rel="tag" title="see questions tagged &#39;mysql&#39;">mysql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Oct '18, 21:49</strong></p>
<img src="https://secure.gravatar.com/avatar/153d30d9d12370c8532371eaaa3593b8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vishy91&#39;s gravatar image" />
<p><span>vishy91</span><br />
<span class="score" title="66 reputation points">66</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vishy91 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Oct '18, 19:20</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-66273" class="comments-container">
<span id="66388"></span>
<div id="comment-66388" class="comment">
<div id="post-66388-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Elaborate on "absolutely cannot use postgres" :-)</p>
</div>
<div id="comment-66388-info" class="comment-info">
<span class="comment-age">(20 Oct '18, 09:30)</span> <span class="comment-user userinfo">AddisMap_Ale...</span>
</div>
</div>
</div>
<div id="comment-tools-66273" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66273-form-container" class="comment-form-container">
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

<span id="66283"></span>

<div id="answer-container-66283" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66283-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66283-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-66283-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="vishy91 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You have a long and rocky road ahead of you and the price for "I absolutely cannot use Postgres" will be several person-weeks of work that you have to invest:</p>
<ul>
<li>the standard importer, osm2pgsql, cannot import into MySQL; there has been work in something called "osm2mysql" but that is nowhere near feature-complete. Your most likely bet is using GDAL (ogr2ogr) to load OSM data into MySQL. This will mean that you lose the ability to do incremental updates.</li>
<li>the standard renderer, Mapnik, cannot load data from MySQL. You will have to use Geoserver or MapServer instead.</li>
<li>the standard map style, OSM-Carto, is built for Mapnik and cannot be used with Geoserver or MapServer; but there are some simpler styles around on the net that work with these renderers.</li>
<li>the styles that you <em>will</em> find for Geoserver or MapServer will assume a table structure like the one generated by osm2pgsql, but your import process will generate a different table structure; you will either have to modify the styles to match your table structure, or modify your table structure post-import to look like what comes out of osm2pgsql.</li>
<li>the standard tile serving and queuing mechanism (mod_tile and renderd) only works with Mapnik; you will have to switch to a different solution that is compatible with the rendering engine you choose. Most likely you'll use the renderer in WMS mode and then use mapproxy, or MapServer's mapcache for this.</li>
</ul>
<p>All in all, you will have to invest a lot of time in this. Are you sure "not using Postgres" is worth it?</p>
<p>And no, there is no step by step guide. You'll have to figure this out yourself.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Oct '18, 08:57</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Oct '18, 09:30</strong> </span></p>
</div>
</div>
<div id="comments-container-66283" class="comments-container">
<span id="66295"></span>
<div id="comment-66295" class="comment">
<div id="post-66295-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for the answer <a href="https://help.openstreetmap.org/users/104/frederik-ramm">@Frederik</a>! This will surely give me a start.</p>
</div>
<div id="comment-66295-info" class="comment-info">
<span class="comment-age">(11 Oct '18, 14:47)</span> <span class="comment-user userinfo">vishy91</span>
</div>
</div>
</div>
<div id="comment-tools-66283" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66283-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="68168"></span>

<div id="answer-container-68168" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68168-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68168-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68168-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="https://help.openstreetmap.org/users/15764/vishy91">@vishy91</a> did you make progress on loading OSM into MySQL?</p>
<p>(Like you, I have no choice in the database behind our application and MySQL is what I have to deal with.)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Feb '19, 22:07</strong></p>
<img src="https://secure.gravatar.com/avatar/457759d0b4c4ed025dfc0a200e007a02?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PPetree&#39;s gravatar image" />
<p><span>PPetree</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PPetree has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-68168" class="comments-container">
&#10;</div>
<div id="comment-tools-68168" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68168-form-container" class="comment-form-container">
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


+++
type = "question"
title = "how to filter tile content in server?"
description = '''Hi, I just created my own tile server using the script in http://opentileserver.org/ Installation worked and now i am able to serve the map of a country. I would like to offer a clean map focussing on cultural heritage, so i would like to filter some information that shows in the tiles, like restaur...'''
date = "2017-02-22T17:45:00Z"
lastmod = "2017-02-23T17:19:00Z"
weight = 54771
keywords = [ "filtering", "server", "tileserver" ]
aliases = [ "/questions/54771" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [how to filter tile content in server?](/questions/54771/how-to-filter-tile-content-in-server)

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
<span id="post-54771-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54771-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-54771-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I just created my own tile server using the script in <a href="http://opentileserver.org/">http://opentileserver.org/</a></p>
<p>Installation worked and now i am able to serve the map of a country.</p>
<p>I would like to offer a clean map focussing on cultural heritage, so i would like to filter some information that shows in the tiles, like restaurants, bars, shops, etc...</p>
<p>Is it possible?</p>
<p>Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-filtering" rel="tag" title="see questions tagged &#39;filtering&#39;">filtering</span> <span class="post-tag tag-link-server" rel="tag" title="see questions tagged &#39;server&#39;">server</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Feb '17, 17:45</strong></p>
<img src="https://secure.gravatar.com/avatar/0a5c61f3bdee2e3090a81ce95fe6a44a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="liborio&#39;s gravatar image" />
<p><span>liborio</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="liborio has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-54771" class="comments-container">
&#10;</div>
<div id="comment-tools-54771" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54771-form-container" class="comment-form-container">
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

<span id="54779"></span>

<div id="answer-container-54779" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-54779-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54779-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-54779-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="liborio has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It is, but the base style Carto-CSS is very complex. You could change what get's rendered in two ways:</p>
<ul>
<li>Alter the SQL statements which pull data from PostGIS</li>
<li>Change styling rules</li>
</ul>
<p>However, probably the easiest way is to do this with a LUA script. An example is that of <a href="https://github.com/SomeoneElseOSM/SomeoneElse-style/blob/master/style.lua">SomeoneElse</a>. This is quite involved but has a good number of useful examples.</p>
<p><a href="https://wiki.openstreetmap.org/wiki/Osmfilter">Osmfilter</a> may also be of some use if your requirements are fairly simple.</p>
<p>The advantage of using a pre-processing step is that then there is no need to try &amp; keep synchronising with changes to the main CartoCSS repository.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Feb '17, 12:26</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-54779" class="comments-container">
<span id="54780"></span>
<div id="comment-54780" class="comment">
<div id="post-54780-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks SK53,</p>
<p>I have been reading this morning about it and checking the files in openstreetmap-carto.</p>
<p>Whas checking the database SELECTs included in "project.mml" (was thinking to make more restrictive the SELECT that use INCLUDE from amenities and shops).</p>
<p>Alsho checked the "amenity-points.mss" and the filter based in "zoom". Had the doubt if could be possible to change some filters for zoom&gt;20 (so they will never validate) or even just remove the style (dont know if that would work).</p>
<p>If i change de SELECTs and run again the "osm2pgsql" would it replace my current tiles? Or would be better a clean install?</p>
<p>Thanks!</p>
</div>
<div id="comment-54780-info" class="comment-info">
<span class="comment-age">(23 Feb '17, 12:39)</span> <span class="comment-user userinfo">liborio</span>
</div>
</div>
<span id="54783"></span>
<div id="comment-54783" class="comment">
<div id="post-54783-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Both should work &amp; changing either mml or mss means you use the same DB schema. I would recommend forking he project on github and maintain your changes in your forked repository.</p>
</div>
<div id="comment-54783-info" class="comment-info">
<span class="comment-age">(23 Feb '17, 17:19)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-54779" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54779-form-container" class="comment-form-container">
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


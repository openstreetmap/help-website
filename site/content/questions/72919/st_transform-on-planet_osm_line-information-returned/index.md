+++
type = "question"
title = "st_transform on planet_osm_line - information returned"
description = '''I&#x27;m using this query to get all the lat and lon coordinates on a way from planet_osm_line: select st_astext(st_transform(way, 4326)) from planet_osm_line  where osm_id = 482283890; The result is: LINESTRING(11.6168586 46.5434487002502,11.6168345 46.5431350002503,11.6167899 46.5429099002503,11.617215...'''
date = "2020-02-07T12:15:00Z"
lastmod = "2020-02-07T12:45:00Z"
weight = 72919
keywords = [ "st_transform", "planet_osm_line" ]
aliases = [ "/questions/72919" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [st_transform on planet_osm_line - information returned](/questions/72919/st_transform-on-planet_osm_line-information-returned)

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
<span id="post-72919-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72919-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72919-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm using this query to get all the lat and lon coordinates on a way from planet_osm_line:</p>
<p>select st_astext(st_transform(way, 4326)) from planet_osm_line where osm_id = 482283890;</p>
<p>The result is: LINESTRING(11.6168586 46.5434487002502,11.6168345 46.5431350002503,11.6167899 46.5429099002503,11.6172158 46.5425886002504,11.6176661 46.5424470002504,11.6180585 46.5424763002504,11.6181788 46.5425033002504,11.618848 46.5427728002503,11.6193672 46.5429585002503,11.6204657 46.5429528002503,11.6214048 46.5432146002503,11.6222983 46.5436187002502,11.6224615 46.5436944002502)</p>
<p>What I see are the lon and lat coordinates for every node constructing the line, but the lat seems to contain extra information (last 6 digits, ie 002502). What is this information and how can I seperate it from the lat coordinate?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-st_transform" rel="tag" title="see questions tagged &#39;st_transform&#39;">st_transform</span> <span class="post-tag tag-link-planet_osm_line" rel="tag" title="see questions tagged &#39;planet_osm_line&#39;">planet_osm_line</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Feb '20, 12:15</strong></p>
<img src="https://secure.gravatar.com/avatar/4890cbd9410be2eac49d034e66d5fc0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ruud%20Brandsma&#39;s gravatar image" />
<p><span>Ruud Brandsma</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ruud Brandsma has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-72919" class="comments-container">
&#10;</div>
<div id="comment-tools-72919" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72919-form-container" class="comment-form-container">
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

<span id="72920"></span>

<div id="answer-container-72920" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72920-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72920-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72920-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>These are floating point represenation errors (from the conversion from lat/lon to mercator coordinates during import, and back in your query); they are not useful data. You can accomplish a rounding with <code>ST_SnapToGrid</code>:</p>
<pre><code>SELECT st_astext(st_snaptogrid(st_transform(way, 4326), .000001))
FROM planet_osm_line 
WHERE osm_id = 482283890;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Feb '20, 12:28</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-72920" class="comments-container">
<span id="72921"></span>
<div id="comment-72921" class="comment">
<div id="post-72921-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your reply. Why are these floating point representation errors only occur on the latitude (precision of 13 digits) and not on the longitude (precision always 7 digits)?</p>
</div>
<div id="comment-72921-info" class="comment-info">
<span class="comment-age">(07 Feb '20, 12:39)</span> <span class="comment-user userinfo">Ruud Brandsma</span>
</div>
</div>
<span id="72922"></span>
<div id="comment-72922" class="comment">
<div id="post-72922-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This is down to the formula used to compute the spherical mercator projection; computing the latitude value requires trigonometric functions, whereas computing the longitude is just simple multiplication:</p>
<pre><code>double lon2x(double lon) { import std.math; return PI*(lon/180.0) * 6378137.0; }
double lat2y(double lat) { import std.math; return log(tan(PI_4+PI*(lat/360.0)))*6378137.0; }
double x2lon(double x) { import std.math; return 180*(x/6378137)/PI; }
double y2lat(double y) { import std.math; return 180*(2*atan(exp(y/6378137))-PI_2)/PI; }</code></pre>
<p>You could largely avoid this issue if you used the -l (the letter L) flag on osm2pgsql import, this would then refrain from projecting coordinates in the first place and make your <code>st_transform</code> redundant. But it would then require some tweaking to use this database for rendering.</p>
</div>
<div id="comment-72922-info" class="comment-info">
<span class="comment-age">(07 Feb '20, 12:45)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-72920" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72920-form-container" class="comment-form-container">
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


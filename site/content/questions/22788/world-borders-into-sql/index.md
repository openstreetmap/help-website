+++
type = "question"
title = "world borders into sql"
description = '''Hi, how can i add world borders into my sql database? i found it in mapnik-style but here is 5 files and i can&#x27;t get coordinates from this files.'''
date = "2013-05-27T07:14:00Z"
lastmod = "2013-06-06T14:30:00Z"
weight = 22788
keywords = [ "coordinate", "world", "border", "sql" ]
aliases = [ "/questions/22788" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [world borders into sql](/questions/22788/world-borders-into-sql)

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
<span id="post-22788-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22788-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-22788-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, how can i add world borders into my sql database? i found it in mapnik-style but here is 5 files and i can't get coordinates from this files.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-coordinate" rel="tag" title="see questions tagged &#39;coordinate&#39;">coordinate</span> <span class="post-tag tag-link-world" rel="tag" title="see questions tagged &#39;world&#39;">world</span> <span class="post-tag tag-link-border" rel="tag" title="see questions tagged &#39;border&#39;">border</span> <span class="post-tag tag-link-sql" rel="tag" title="see questions tagged &#39;sql&#39;">sql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 May '13, 07:14</strong></p>
<img src="https://secure.gravatar.com/avatar/c7e917dd7fcec294a5dfd922b41bca76?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stevocz&#39;s gravatar image" />
<p><span>stevocz</span><br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stevocz has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-22788" class="comments-container">
&#10;</div>
<div id="comment-tools-22788" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22788-form-container" class="comment-form-container">
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

<span id="22789"></span>

<div id="answer-container-22789" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-22789-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22789-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-22789-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you want to load shape files into a PostGIS database, check out shp2pgsql. However our Mapnik styles are usually built for reading the world boundary data directly from these shape files; there should be no need to import them into PostGIS.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 May '13, 09:03</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-22789" class="comments-container">
<span id="23017"></span>
<div id="comment-23017" class="comment">
<div id="post-23017-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>i am now imported boundaries with shp2pgsql.</p>
<p>this is one item. how can i from this get coordinate?</p>
<p>gid | cat | fips_cntry | cntry_name | the_geom / 1 | 15 | AY | Antarctica | 010600000001000000010300000001000000260000003BC .. (snipped)</p>
</div>
<div id="comment-23017-info" class="comment-info">
<span class="comment-age">(05 Jun '13, 07:12)</span> <span class="comment-user userinfo">stevocz</span>
</div>
</div>
<span id="23052"></span>
<div id="comment-23052" class="comment">
<div id="post-23052-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Use the st_astext function in your query, like "select cntry_name,st_astext(the_geom) from tablename..."</p>
</div>
<div id="comment-23052-info" class="comment-info">
<span class="comment-age">(06 Jun '13, 10:03)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="23061"></span>
<div id="comment-23061" class="comment">
<div id="post-23061-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>thank you.</p>
<p>your sql select work very well, but border is little moved. see picture: <a href="http://s18.postimg.org/6s75eqjy1/border.png">http://s18.postimg.org/6s75eqjy1/border.png</a></p>
<p>on northern hemisphere is latitude moved lower about 0.2 and on southern hemisphere is latitude moved higher about 0.2</p>
</div>
<div id="comment-23061-info" class="comment-info">
<span class="comment-age">(06 Jun '13, 14:25)</span> <span class="comment-user userinfo">stevocz</span>
</div>
</div>
<span id="23062"></span>
<div id="comment-23062" class="comment">
<div id="post-23062-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>i use this function for convert coordinate</p>
<p>double AQConverter::MercatorToLon(double x){</p>
<pre><code>double rMajor = 6378137; //Equatorial Radius, WGS84
&#10;double shift  = M_PI * rMajor;
&#10;double lon    = x / shift * 180.0;
&#10;return lon;</code></pre>
<p>}</p>
<p>double AQConverter::MercatorToLat(double y){</p>
<pre><code>double rMajor = 6378137; //Equatorial Radius, WGS84
&#10;double shift  = M_PI * rMajor;
&#10;double lat    = y / shift * 180.0;
&#10;lat = 180.0/ M_PI * (2 * qAtan(qExp((lat * M_PI) / 180.0)) - M_PI / 2.0);
&#10;return lat;</code></pre>
<p>}</p>
</div>
<div id="comment-23062-info" class="comment-info">
<span class="comment-age">(06 Jun '13, 14:30)</span> <span class="comment-user userinfo">stevocz</span>
</div>
</div>
</div>
<div id="comment-tools-22789" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22789-form-container" class="comment-form-container">
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


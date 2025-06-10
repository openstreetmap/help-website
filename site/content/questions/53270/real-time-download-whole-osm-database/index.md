+++
type = "question"
title = "Real-Time Download whole OSM database"
description = '''Hi! I am interested in downloading the whole database at real-time, both for backup and rendering. How can I do so? Thanks!  Download PostgreSQL backend database shown in image:  '''
date = "2016-12-07T05:25:00Z"
lastmod = "2016-12-07T12:14:00Z"
weight = 53270
keywords = [ "download", "data", "export", "postgres", "database" ]
aliases = [ "/questions/53270" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Real-Time Download whole OSM database](/questions/53270/real-time-download-whole-osm-database)

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
<span id="post-53270-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53270-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-53270-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi! I am interested in downloading the whole database at real-time, both for backup and rendering. How can I do so? Thanks!</p>
<p>Download PostgreSQL backend database shown in image: <img src="https://wiki.openstreetmap.org/w/images/1/15/OSM_Components.png" alt="Component Overview" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-download" rel="tag" title="see questions tagged &#39;download&#39;">download</span> <span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-postgres" rel="tag" title="see questions tagged &#39;postgres&#39;">postgres</span> <span class="post-tag tag-link-database" rel="tag" title="see questions tagged &#39;database&#39;">database</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Dec '16, 05:25</strong></p>
<img src="https://secure.gravatar.com/avatar/100f8ccde5e9799707a5056f94fe183f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Wetitpig0&#39;s gravatar image" />
<p><span>Wetitpig0</span><br />
<span class="score" title="307 reputation points">307</span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="19 badges"><span class="silver">●</span><span class="badgecount">19</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Wetitpig0 has 2 accepted answers">10%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Dec '16, 06:35</strong> </span></p>
</div>
</div>
<div id="comments-container-53270" class="comments-container">
&#10;</div>
<div id="comment-tools-53270" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53270-form-container" class="comment-form-container">
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

<span id="53281"></span>

<div id="answer-container-53281" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53281-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53281-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-53281-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Wetitpig0 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You will have to download the planet file from planet.openstreetmap.org and import it into a database on your side. Once you have done this, you can download daily, hourly, or even minutely updates from OpenStreetMap and apply them to your database to remain current. Most people choose <code>osm2pgsql</code> for importing the data into a PostGIS database which is very good for rendering, but it is a lossy process that does not capture all information from the source data. If you would like to capture all information from OSM then you would be looking at producing an "APIDB" style database with the <code>osmosis</code> utility but that, in turn, is less suitable for rendering.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Dec '16, 08:25</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-53281" class="comments-container">
<span id="53284"></span>
<div id="comment-53284" class="comment">
<div id="post-53284-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>So it cannot be directly downloaded. We must rely on planet.osm?</p>
</div>
<div id="comment-53284-info" class="comment-info">
<span class="comment-age">(07 Dec '16, 09:01)</span> <span class="comment-user userinfo">Wetitpig0</span>
</div>
</div>
<span id="53288"></span>
<div id="comment-53288" class="comment">
<div id="post-53288-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Can you explain what you mean by "So it cannot be directly downloaded"? Downloading from planet.osm (or a mirror) <em>is</em> a download of the OpenStreetMap data. What happens to it next depends on what you want to do with it - some data is almost always lost as it is moved into a database designed to support whatever the user wants to do with it (rendering, searching, something else).</p>
</div>
<div id="comment-53288-info" class="comment-info">
<span class="comment-age">(07 Dec '16, 10:36)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="53292"></span>
<div id="comment-53292" class="comment">
<div id="post-53292-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>No, you cannot directly download the OSM database that is being used on the live system, for a number of reasons - not only technical (too much impact on running system, requirement of exact same PostGIS version on receiving side etc.), but also administrative (not everything in the OSM database is public).</p>
</div>
<div id="comment-53292-info" class="comment-info">
<span class="comment-age">(07 Dec '16, 12:14)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-53281" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53281-form-container" class="comment-form-container">
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


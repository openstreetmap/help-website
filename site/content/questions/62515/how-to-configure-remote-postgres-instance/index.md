+++
type = "question"
title = "How to configure remote Postgres instance?"
description = '''Hello! I&#x27;ve been able to successfully setup the map server locally, but now I&#x27;m trying to configure the system to hit a remote Postgres instance. However, I can&#x27;t figure out where this is configured. I&#x27;ve tried adding parameters to the mapnik.xml file, but it still appears to hit the localhost: rend...'''
date = "2018-03-05T17:20:00Z"
lastmod = "2018-03-05T19:06:00Z"
weight = 62515
keywords = [ "remote", "postgresql", "external" ]
aliases = [ "/questions/62515" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to configure remote Postgres instance?](/questions/62515/how-to-configure-remote-postgres-instance)

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
<span id="post-62515-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62515-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62515-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello! I've been able to successfully setup the map server locally, but now I'm trying to configure the system to hit a remote Postgres instance. However, I can't figure out where this is configured. I've tried adding parameters to the mapnik.xml file, but it still appears to hit the localhost:</p>
<p>renderd[20693]: An error occurred while loading the map layer 'ajt': Postgis Plugin: could not connect to server: No such file or directory Is the server running locally and accepting connections on Unix domain socket "/var/run/postgresql/.s.PGSQL.5432"?</p>
<p>For reference, I was using this URL for the mapnik parameters: <a href="https://github.com/mapnik/mapnik/wiki/PostGIS">https://github.com/mapnik/mapnik/wiki/PostGIS</a></p>
<p>I've also tried guessing at what the host, user, and password variable names would be in renderd.conf, but haven't had luck with this either. Does someone have a link to an example or documentation on how to hit a remote Posgres instance? I've already loaded all of the data for North America into the external Postgres server, so I'd very much like to use that if possible.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-remote" rel="tag" title="see questions tagged &#39;remote&#39;">remote</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-external" rel="tag" title="see questions tagged &#39;external&#39;">external</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Mar '18, 17:20</strong></p>
<img src="https://secure.gravatar.com/avatar/f508de3ba12e39cc742c46d67d480a00?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gordysc&#39;s gravatar image" />
<p><span>gordysc</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gordysc has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-62515" class="comments-container">
&#10;</div>
<div id="comment-tools-62515" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62515-form-container" class="comment-form-container">
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

<span id="62516"></span>

<div id="answer-container-62516" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-62516-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62516-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-62516-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It looks like I've had a bit of a break through (of course after posting this question).. For future reference, I added host, user, and password to osm2pgsql in project.mml and then regenerated the file using carto project.mml &gt; mapnik.xml . This seemed to cause the server to connect to the database on startup. However, I'm getting connection timeouts when loading /hot/0/0/0.png. Will post back later if I figure out why.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Mar '18, 17:31</strong></p>
<img src="https://secure.gravatar.com/avatar/f508de3ba12e39cc742c46d67d480a00?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gordysc&#39;s gravatar image" />
<p><span>gordysc</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gordysc has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-62516" class="comments-container">
<span id="62518"></span>
<div id="comment-62518" class="comment">
<div id="post-62518-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>One more follow up, this solves the connection issue: <a href="https://help.openstreetmap.org/questions/32367/rendering-open-street-map-stoped">https://help.openstreetmap.org/questions/32367/rendering-open-street-map-stoped</a></p>
<p>For some reason the server went extremely fast rendering the tiles after leaving it for an hour. Perhaps it was creating indexes, etc? Anyway, hope all of this helps someone down the road!</p>
</div>
<div id="comment-62518-info" class="comment-info">
<span class="comment-age">(05 Mar '18, 19:06)</span> <span class="comment-user userinfo">gordysc</span>
</div>
</div>
</div>
<div id="comment-tools-62516" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62516-form-container" class="comment-form-container">
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


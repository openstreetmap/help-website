+++
type = "question"
title = "How big is the main SQL database where edits are saved to?"
description = '''How big is the main SQL database containing nodes, ways and relations? I do not mean the planet file but the actual GIS database (PostGIS?) where the edits are saved to along with editing history etc. I know the munin.openstreetmap.org server stats site but I cant really get oriented there. I guess ...'''
date = "2016-10-22T11:00:00Z"
lastmod = "2016-12-09T08:42:00Z"
weight = 52634
keywords = [ "size", "database", "postgres", "postgis", "sql" ]
aliases = [ "/questions/52634" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How big is the main SQL database where edits are saved to?](/questions/52634/how-big-is-the-main-sql-database-where-edits-are-saved-to)

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
<span id="post-52634-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52634-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-52634-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How big is the main SQL database containing nodes, ways and relations? I do not mean the planet file but the actual GIS database (PostGIS?) where the edits are saved to along with editing history etc. I know the <a href="http://munin.openstreetmap.org/">munin.openstreetmap.org</a> server stats site but I cant really get oriented there. I guess in the past the main db server was called <a href="https://hardware.openstreetmap.org/servers/ramoth.openstreetmap.org/">ramoth</a> but I am not sure if this is still the case. Looking at <a href="http://munin.openstreetmap.org/openstreetmap/ramoth.openstreetmap/postgres_size_openstreetmap_9_1_main.html">ramoth's SQL size stats</a> the db seems to be about 6 TB in size as of today. Will anyone please confirm ramoth really is the main database server?</p>
<p>EDIT: It seems like ramoth is read-only mirror, the main server seems to be <a href="https://hardware.openstreetmap.org/servers/katla.openstreetmap.org/">katla</a> - however the its <a href="http://munin.openstreetmap.org/openstreetmap/katla.openstreetmap/postgres_size_openstreetmap_9_1_main.html">database size</a> is the same of course.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-size" rel="tag" title="see questions tagged &#39;size&#39;">size</span> <span class="post-tag tag-link-database" rel="tag" title="see questions tagged &#39;database&#39;">database</span> <span class="post-tag tag-link-postgres" rel="tag" title="see questions tagged &#39;postgres&#39;">postgres</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span> <span class="post-tag tag-link-sql" rel="tag" title="see questions tagged &#39;sql&#39;">sql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Oct '16, 11:00</strong></p>
<img src="https://secure.gravatar.com/avatar/7d327873d48d28e563c9ad7259853c35?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kozuch&#39;s gravatar image" />
<p><span>Kozuch</span><br />
<span class="score" title="1720 reputation points"><span>1.7k</span></span><span title="58 badges"><span class="badge1">●</span><span class="badgecount">58</span></span><span title="72 badges"><span class="silver">●</span><span class="badgecount">72</span></span><span title="85 badges"><span class="bronze">●</span><span class="badgecount">85</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kozuch has one accepted answer">8%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Oct '16, 12:03</strong> </span></p>
</div>
</div>
<div id="comments-container-52634" class="comments-container">
&#10;</div>
<div id="comment-tools-52634" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52634-form-container" class="comment-form-container">
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

<span id="53144"></span>

<div id="answer-container-53144" class="answer accepted-answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53144-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53144-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-53144-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SK53 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>My findings were correct - the main database for www.openstreetmap.org that holds users, nodes, ways, relations, editing history etc. is <a href="http://munin.openstreetmap.org/openstreetmap/katla.openstreetmap/postgres_size_openstreetmap_9_1_main.html">about 6 TB in size</a> as of today (November 2016). The database master (read/write) is on <a href="https://hardware.openstreetmap.org/servers/katla.openstreetmap.org/">katla</a> and there are few mirrors (look at <a href="https://hardware.openstreetmap.org">hardware.openstreetmap.org</a> for details).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Nov '16, 10:40</strong></p>
<img src="https://secure.gravatar.com/avatar/7d327873d48d28e563c9ad7259853c35?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kozuch&#39;s gravatar image" />
<p><span>Kozuch</span><br />
<span class="score" title="1720 reputation points"><span>1.7k</span></span><span title="58 badges"><span class="badge1">●</span><span class="badgecount">58</span></span><span title="72 badges"><span class="silver">●</span><span class="badgecount">72</span></span><span title="85 badges"><span class="bronze">●</span><span class="badgecount">85</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kozuch has one accepted answer">8%</span></p>
</div>
</div>
<div id="comments-container-53144" class="comments-container">
<span id="53151"></span>
<div id="comment-53151" class="comment">
<div id="post-53151-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I've marked this as the accepted answer as I believe it is not possible for users to accept their own answers.</p>
</div>
<div id="comment-53151-info" class="comment-info">
<span class="comment-age">(28 Nov '16, 20:23)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="53275"></span>
<div id="comment-53275" class="comment">
<div id="post-53275-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="http://munin.openstreetmap.org/static/dynazoom.html?cgiurl_graph=/munin-cgi/munin-cgi-graph&amp;plugin_name=openstreetmap/katla.openstreetmap/postgres_size_openstreetmap_9_1_main&amp;size_x=800&amp;size_y=400&amp;start_epoch=1446532011&amp;stop_epoch=1481092011">Why are there sharp decreases over time?</a></p>
</div>
<div id="comment-53275-info" class="comment-info">
<span class="comment-age">(07 Dec '16, 06:32)</span> <span class="comment-user userinfo">Wetitpig0</span>
</div>
</div>
<span id="53337"></span>
<div id="comment-53337" class="comment">
<div id="post-53337-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/13060/wetitpig0">@Wetitpig0</a> - I also noticed the sharp db size drops but have no idea what that can be. I think user TomH on osm-dev IRC channel will know (try to ping him - if you get answer please post here).</p>
</div>
<div id="comment-53337-info" class="comment-info">
<span class="comment-age">(08 Dec '16, 08:06)</span> <span class="comment-user userinfo">Kozuch</span>
</div>
</div>
<span id="53432"></span>
<div id="comment-53432" class="comment">
<div id="post-53432-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>This may be due to the defragmentation of the OSM database. I have not asked the developers, but someone said this in <a href="/questions/53430/visible-tile-borders-in-rendering">one question</a>.</p>
</div>
<div id="comment-53432-info" class="comment-info">
<span class="comment-age">(09 Dec '16, 08:42)</span> <span class="comment-user userinfo">Wetitpig0</span>
</div>
</div>
</div>
<div id="comment-tools-53144" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53144-form-container" class="comment-form-container">
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


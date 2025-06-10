+++
type = "question"
title = "Error with lookup service nominatim.openstreetmap.org"
description = '''https://nominatim.openstreetmap.org/ See below - any help? I&#x27;m trying to lookup like this:  https://nominatim.openstreetmap.org/search?format=json&amp;amp;city=calgary&amp;amp;state=alberta&amp;amp;country=canada  string(19) &quot;pgsql://@/nominatim&quot; object(DB_Error)#2 (8) {  [&quot;error_message_prefix&quot;]=&amp;gt;  string(0...'''
date = "2014-10-17T02:46:00Z"
lastmod = "2014-10-17T07:23:00Z"
weight = 37670
keywords = [ "osm.org", "nominatim", "error" ]
aliases = [ "/questions/37670" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Error with lookup service nominatim.openstreetmap.org](/questions/37670/error-with-lookup-service-nominatimopenstreetmaporg)

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
<span id="post-37670-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37670-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-37670-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p><a href="https://nominatim.openstreetmap.org/">https://nominatim.openstreetmap.org/</a> See below - any help?</p>
<p>I'm trying to lookup like this: <a href="https://nominatim.openstreetmap.org/search?format=json&amp;city=calgary&amp;state=alberta&amp;country=canada">https://nominatim.openstreetmap.org/search?format=json&amp;city=calgary&amp;state=alberta&amp;country=canada</a></p>
<hr />
<pre><code>string(19) &quot;pgsql://@/nominatim&quot;
object(DB_Error)#2 (8) {
 [&quot;error_message_prefix&quot;]=&gt;
 string(0) &quot;&quot;
 [&quot;mode&quot;]=&gt;
 int(1)
 [&quot;level&quot;]=&gt;
 int(1024)
 [&quot;code&quot;]=&gt;
 int(-24)
 [&quot;message&quot;]=&gt;
 string(24) &quot;DB Error: connect failed&quot;
 [&quot;userinfo&quot;]=&gt;
 string(272) &quot; [nativecode=pg_connect(): Unable to connect to PostgreSQL server: could not connect to server: No such file or directory
   Is the server running locally and accepting
   connections on Unix domain socket &amp;quot;/var/run/postgresql/.s.PGSQL.5432&amp;quot;?] ** pgsql://@/nominatim&quot;</code></pre>
<p>...</p>
<pre><code>DB Error: connect failed</code></pre>
<hr />
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm.org" rel="tag" title="see questions tagged &#39;osm.org&#39;">osm.org</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Oct '14, 02:46</strong></p>
<img src="https://secure.gravatar.com/avatar/415d5d919cc7c8e37e88c5609e0343a5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SSF%20Support&#39;s gravatar image" />
<p><span>SSF Support</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SSF Support has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Oct '14, 07:20</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span></p>
</div>
</div>
<div id="comments-container-37670" class="comments-container">
&#10;</div>
<div id="comment-tools-37670" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37670-form-container" class="comment-form-container">
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

<span id="37673"></span>

<div id="answer-container-37673" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-37673-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37673-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-37673-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The server that does the name searches is currently broken. Admins are aware of it and will fix the problem. A first port of call for when things don't work is <a href="http://wiki.openstreetmap.org/wiki/Platform_Status">http://wiki.openstreetmap.org/wiki/Platform_Status</a> which will often tell you about known issues, or check on <a href="http://wiki.openstreetmap.org/wiki/Irc">IRC</a> whether the problem is there for everyone or just you.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Oct '14, 07:23</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-37673" class="comments-container">
&#10;</div>
<div id="comment-tools-37673" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37673-form-container" class="comment-form-container">
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

</hr>

</div>

</div>


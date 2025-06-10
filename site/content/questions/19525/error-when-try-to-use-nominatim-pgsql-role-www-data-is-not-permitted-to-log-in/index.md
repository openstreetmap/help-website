+++
type = "question"
title = "error when try to use nominatim pgsql role &quot;www-data&quot; is not permitted to log in"
description = '''After I installed nominatim when I access http://localhost/nominatim/search.php I get string(19) &quot;pgsql://@/nominatim&quot; object(DB_Error)#2 (8) { [&quot;error_message_prefix&quot;]=&amp;gt; string(0) &quot;&quot; [&quot;mode&quot;]=&amp;gt; int(1) [&quot;level&quot;]=&amp;gt; int(1024) [&quot;code&quot;]=&amp;gt; int(-24) [&quot;message&quot;]=&amp;gt; string(24) &quot;DB Error: conne...'''
date = "2013-02-01T19:04:00Z"
lastmod = "2013-02-04T09:04:00Z"
weight = 19525
keywords = [ "pgsql", "nominatim" ]
aliases = [ "/questions/19525" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [error when try to use nominatim pgsql role "www-data" is not permitted to log in](/questions/19525/error-when-try-to-use-nominatim-pgsql-role-www-data-is-not-permitted-to-log-in)

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
<span id="post-19525-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19525-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-19525-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>After I installed nominatim when I access <a href="http://localhost/nominatim/search.php">http://localhost/nominatim/search.php</a> I get</p>
<p>string(19) "pgsql://@/nominatim" object(DB_Error)#2 (8) { ["error_message_prefix"]=&gt; string(0) "" ["mode"]=&gt; int(1) ["level"]=&gt; int(1024) ["code"]=&gt; int(-24) ["message"]=&gt; string(24) "DB Error: connect failed" ["userinfo"]=&gt; string(141) " [nativecode=pg_connect(): Unable to connect to PostgreSQL server: FATAL: role "www-data" is not permitted to log in]</p>
<p>This deals with www-data role on postrges. But on install I trowed:</p>
<p>psql -U postgres -c 'create role "www-data"'; psql -U postgres -d nominatim -c 'GRANT ALL PRIVILEGES ON DATABASE nominatim TO "www-data"';</p>
<p>Any clue?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-pgsql" rel="tag" title="see questions tagged &#39;pgsql&#39;">pgsql</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Feb '13, 19:04</strong></p>
<img src="https://secure.gravatar.com/avatar/afa2913bd1ceace5a19edb7f80a43c24?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mihai%20niculita&#39;s gravatar image" />
<p><span>mihai niculita</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mihai niculita has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-19525" class="comments-container">
&#10;</div>
<div id="comment-tools-19525" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19525-form-container" class="comment-form-container">
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

<span id="19530"></span>

<div id="answer-container-19530" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-19530-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19530-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-19530-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I manged to resolve it by trowing:</p>
<p>psql -U postgres -c 'ALTER ROLE "www-data" WITH login;';</p>
<p>So i problem of PostGreSQL role creation.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Feb '13, 20:22</strong></p>
<img src="https://secure.gravatar.com/avatar/afa2913bd1ceace5a19edb7f80a43c24?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mihai%20niculita&#39;s gravatar image" />
<p><span>mihai niculita</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mihai niculita has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-19530" class="comments-container">
<span id="19570"></span>
<div id="comment-19570" class="comment">
<div id="post-19570-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Having "www-data" as a database user raises warning signs to me.</p>
<p>Remember that postgres users and system users are completely distinct. Your application (nominatim) should have a option to configure which database user is used to connect to the db. If the app doesn't specify anything, the current system user name is used to (try to) connect to the db.</p>
<p>www-data is typically the system user that runs the web server. It should not, as a whole, be allowed to connect to the db, for security and maintenance reasons.</p>
</div>
<div id="comment-19570-info" class="comment-info">
<span class="comment-age">(04 Feb '13, 09:00)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
<span id="19571"></span>
<div id="comment-19571" class="comment">
<div id="post-19571-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>(continued) Create a "nominatim" db user instead (maybe one exists already), give it access to just your nominatim db, and configure nominatim to use that user when connecting.</p>
</div>
<div id="comment-19571-info" class="comment-info">
<span class="comment-age">(04 Feb '13, 09:04)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
</div>
<div id="comment-tools-19530" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19530-form-container" class="comment-form-container">
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


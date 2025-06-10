+++
type = "question"
title = "Overpass - debugging intermittant 500 error messages"
description = '''I have an overpass api server that I set up, which is under reasonably heavy usage, although the machine is beefy (16 CPUS, 48G RAM, SSDs). 99.9% of the time it handles things fine. However every so often I get a HTTP 500 error from apache, and all I get in the apache error logs is this: [Thu Apr 07...'''
date = "2016-04-15T11:05:00Z"
lastmod = "2016-04-16T09:05:00Z"
weight = 49238
keywords = [ "overpass" ]
aliases = [ "/questions/49238" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Overpass - debugging intermittant 500 error messages](/questions/49238/overpass-debugging-intermittant-500-error-messages)

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
<span id="post-49238-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49238-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-49238-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have an overpass api server that I set up, which is under reasonably heavy usage, although the machine is beefy (16 CPUS, 48G RAM, SSDs). 99.9% of the time it handles things fine. However every so often I get a HTTP 500 error from apache, and all I get in the apache error logs is this:</p>
<pre><code>[Thu Apr 07 10:07:38.737961 2016] [cgid:error] [pid 8783:tid 140682425480960] [client 1.2.3.4:61698] End of script output before headers: interpreter</code></pre>
<p>I can't find anything in the overpass <code>transactions.log</code> file for that timestamp, nor nothing in syslog.</p>
<p>When the same query is sent at a later time, it works and returns results quickly.</p>
<p>Is there anything I can do to debug this problem more, or to find out what's going on? Or should I just resubmit the query when there is a 500 error until I get a 200 result?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Apr '16, 11:05</strong></p>
<img src="https://secure.gravatar.com/avatar/16e12e337f6edc3750681492656097ed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rorym&#39;s gravatar image" />
<p><span>rorym</span><br />
<span class="score" title="5358 reputation points"><span>5.4k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="49 badges"><span class="silver">●</span><span class="badgecount">49</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rorym has 18 accepted answers">11%</span></p>
</div>
</div>
<div id="comments-container-49238" class="comments-container">
<span id="49249"></span>
<div id="comment-49249" class="comment">
<div id="post-49249-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Better ask this question on the overpass dev list: <a href="http://listes.openstreetmap.fr/wws/info/overpass">http://listes.openstreetmap.fr/wws/info/overpass</a> and don't forget to add much more details: (a) which Overpass / apache version do you run (b) which queries do you run (c) do you run them in parallel, if so, how many parallel threads, (d) what kind of client do you use, (e) how did you set up your db, does it include attic data?... etc... basically, what is needed to reproduce this?</p>
</div>
<div id="comment-49249-info" class="comment-info">
<span class="comment-age">(15 Apr '16, 17:49)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
</div>
<div id="comment-tools-49238" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49238-form-container" class="comment-form-container">
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

<span id="49266"></span>

<div id="answer-container-49266" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-49266-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49266-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-49266-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="rorym has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>First of all, it is for sure a bug in the software. HTTP 500 means most often that the process has crashed.</p>
<p>There are HTTP 500 errors on the main instance, too. It happens about once per 100'000 requests, and the errors aren't reproducible. The Apache error log often, but not always tells "End of script output before headers".</p>
<p>After all, I have no idea what is happening there. The first log message to $DB_DIR/transactions.log is written quite early (once the process knows where the log directory is), hence I have no idea yet how to catch the error condition.</p>
<p>A general advice I can give is to run the latest version from the minor_issues branch. This branch is always intended to get patches, and some bugs that may or may not cause crashed have been fixed there.</p>
<p>The second advice is, like mmd has said, to subscribe to the Overpass list. It is probably a better place to discuss all the deeper technical details once there is more information.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Apr '16, 09:05</strong></p>
<img src="https://secure.gravatar.com/avatar/fcfdb0825826fd13d2ff0d83d58819c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland%20Olbricht&#39;s gravatar image" />
<p><span>Roland Olbricht</span><br />
<span class="score" title="6666 reputation points"><span>6.7k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland Olbricht has 40 accepted answers">36%</span></p>
</div>
</div>
<div id="comments-container-49266" class="comments-container">
&#10;</div>
<div id="comment-tools-49266" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49266-form-container" class="comment-form-container">
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


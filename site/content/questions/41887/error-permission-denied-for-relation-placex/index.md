+++
type = "question"
title = "ERROR:  permission denied for relation placex"
description = '''I imported planet data onto my CentOS machine, and when trying to use the Nominatim installation using curl: curl &#x27;http://localhost/nominatim/reverse?format=xml&amp;amp;lat=-33.859728&amp;amp;lon=151.227569&amp;amp;zoom=18&amp;amp;addressdetails=1&amp;amp;debug=1&#x27;  I get a long debug message with the reoccuring: ERROR:...'''
date = "2015-03-24T18:53:00Z"
lastmod = "2015-04-06T20:32:00Z"
weight = 41887
keywords = [ "nominatim", "relations", "permission" ]
aliases = [ "/questions/41887" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [ERROR: permission denied for relation placex](/questions/41887/error-permission-denied-for-relation-placex)

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
<span id="post-41887-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41887-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-41887-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I imported planet data onto my CentOS machine, and when trying to use the Nominatim installation using curl:</p>
<pre><code>curl &#39;http://localhost/nominatim/reverse?format=xml&amp;lat=-33.859728&amp;lon=151.227569&amp;zoom=18&amp;addressdetails=1&amp;debug=1&#39;</code></pre>
<p>I get a long debug message with the reoccuring:</p>
<pre><code>ERROR:  permission denied for relation placex</code></pre>
<p>During the installation process, I tried to alter role, and got a message saying that role "www-data_ does not exist:</p>
<pre><code>bash-4.1$ psql -d nominatim -c &#39;ALTER USER &quot;www-data&quot; RENAME TO &quot;apache&quot;&#39;
ERROR:  role &quot;www-data&quot; does not exist</code></pre>
<p>Could they be related? How do I solve the issue of permission for placex relation?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span> <span class="post-tag tag-link-permission" rel="tag" title="see questions tagged &#39;permission&#39;">permission</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Mar '15, 18:53</strong></p>
<img src="https://secure.gravatar.com/avatar/61de868d7785f30711497cecbdddf5f4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="baekacaek&#39;s gravatar image" />
<p><span>baekacaek</span><br />
<span class="score" title="176 reputation points">176</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="baekacaek has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-41887" class="comments-container">
&#10;</div>
<div id="comment-tools-41887" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41887-form-container" class="comment-form-container">
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

<span id="41894"></span>

<div id="answer-container-41894" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-41894-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41894-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-41894-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Did you follow the instructions on <a href="https://wiki.openstreetmap.org/wiki/Nominatim/Installation,">https://wiki.openstreetmap.org/wiki/Nominatim/Installation,</a> namely where it says:</p>
<pre><code>createuser -SDR www-data</code></pre>
<p>?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Mar '15, 23:46</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-41894" class="comments-container">
<span id="41896"></span>
<div id="comment-41896" class="comment">
<div id="post-41896-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes I made sure to run that command (because I forgot to at first).</p>
</div>
<div id="comment-41896-info" class="comment-info">
<span class="comment-age">(24 Mar '15, 23:59)</span> <span class="comment-user userinfo">baekacaek</span>
</div>
</div>
<span id="41912"></span>
<div id="comment-41912" class="comment">
<div id="post-41912-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Because the user didn't exist when the database was created all the grant commands will have failed. You will need to go through and run them manually. You can find them in tables.sql, an example would be:</p>
<p>GRANT SELECT ON import_status TO "www-data" ;</p>
</div>
<div id="comment-41912-info" class="comment-info">
<span class="comment-age">(25 Mar '15, 13:37)</span> <span class="comment-user userinfo">twain</span>
</div>
</div>
<span id="42156"></span>
<div id="comment-42156" class="comment">
<div id="post-42156-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That could be the reason why. Could you guide me on how I could run it manually? I found the tables.sql file, but I'm not quite sure what I am supposed to do with it. Thanks</p>
</div>
<div id="comment-42156-info" class="comment-info">
<span class="comment-age">(06 Apr '15, 20:32)</span> <span class="comment-user userinfo">baekacaek</span>
</div>
</div>
</div>
<div id="comment-tools-41894" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41894-form-container" class="comment-form-container">
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


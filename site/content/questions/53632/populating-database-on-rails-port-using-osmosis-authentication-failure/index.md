+++
type = "question"
title = "Populating database on Rails Port using osmosis authentication failure"
description = '''Hi, I&#x27;ve been following the instruction on the github page for installing the Rails Port, and have successfully completed all of those instructions. I am now trying to populate the database following the instructions here. I&#x27;ve tried running the osmosis command:  osmosis --read-pbf [my-osm-file].osm...'''
date = "2016-12-21T15:05:00Z"
lastmod = "2016-12-22T10:06:00Z"
weight = 53632
keywords = [ "osmosis", "railsport" ]
aliases = [ "/questions/53632" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Populating database on Rails Port using osmosis authentication failure](/questions/53632/populating-database-on-rails-port-using-osmosis-authentication-failure)

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
<span id="post-53632-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53632-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-53632-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I've been following the instruction on the <a href="https://github.com/openstreetmap/openstreetmap-website/blob/master/INSTALL.md">github page for installing the Rails Port</a>, and have successfully completed all of those instructions. I am now trying to populate the database following the instructions <a href="https://github.com/openstreetmap/openstreetmap-website/blob/master/CONFIGURE.md">here</a>. I've tried running the osmosis command:</p>
<blockquote>
<p>osmosis --read-pbf [my-osm-file].osm.pbf --write-apidb host="localhost" database="openstreetmap" user="openstreetmap" password="" validateSchemaVersion="no"</p>
</blockquote>
<p>However, it initially gives me an error that argument 7 (password) doesn't contain a value after the '=', so I removed that field. Now it is giving me a password authentication failed error for user "openstreetmap".</p>
<p>I tried manually logging into the openstreetmap database by running the following command:</p>
<blockquote>
<p>psql -d openstreetmap -U openstreetmap</p>
</blockquote>
<p>and I get this error:</p>
<blockquote>
<p>psql: FATAL: Peer authentication failed for user "openstreetmap"</p>
</blockquote>
<p>Running the same command but with my own username allows me to log into the database. So then I tried the osmosis command with the username replaced with mine, but it still gives me a password authentication failure error. I'm stuck now as to what to try next. Any suggestions would be very much appreciated.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span> <span class="post-tag tag-link-railsport" rel="tag" title="see questions tagged &#39;railsport&#39;">railsport</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Dec '16, 15:05</strong></p>
<img src="https://secure.gravatar.com/avatar/7a55b45e6e0757aa53441b6360410ee2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AndrewPalmer&#39;s gravatar image" />
<p><span>AndrewPalmer</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AndrewPalmer has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-53632" class="comments-container">
&#10;</div>
<div id="comment-tools-53632" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53632-form-container" class="comment-form-container">
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

<span id="53634"></span>

<div id="answer-container-53634" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53634-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53634-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-53634-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="AndrewPalmer has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Try</p>
<pre><code>sudo -u postgres psql -c &quot;alter role openstreetmap with password &#39;openstreetmap&#39;&quot;</code></pre>
<p>and then specify "openstreetmap" as a password in your osmosis command line. You will then also be able to do</p>
<pre><code>psql -W -d openstreetmap -U openstreetmap</code></pre>
<p>and log in to the database with the password. (Logging in without password, as you tried above, would require "trust" authentication configured in pg_hba.conf or a special configuration of the "peer" authentication method to allow your Unix user to connect as PostgreSQL user "openstreetmap".)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Dec '16, 16:19</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Dec '16, 16:19</strong> </span></p>
</div>
</div>
<div id="comments-container-53634" class="comments-container">
<span id="53660"></span>
<div id="comment-53660" class="comment">
<div id="post-53660-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks, adding the password worked.</p>
</div>
<div id="comment-53660-info" class="comment-info">
<span class="comment-age">(22 Dec '16, 10:06)</span> <span class="comment-user userinfo">AndrewPalmer</span>
</div>
</div>
</div>
<div id="comment-tools-53634" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53634-form-container" class="comment-form-container">
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


+++
type = "question"
title = "Nominatim setup.php problem"
description = '''I checkout osm2pgsql from svn and I manualy compile it. when I execute seture.php it create database and table and next it say me : [...] CREATE TABLE SET SET SET SET SET SET SET SET CREATE TABLE ALTER TABLE Import ERROR: please download and build osm2pgsql please download and build osm2pgsql  What ...'''
date = "2012-04-24T13:21:00Z"
lastmod = "2012-04-24T17:32:00Z"
weight = 12330
keywords = [ "nominatim", "osm2pgsql" ]
aliases = [ "/questions/12330" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Nominatim setup.php problem](/questions/12330/nominatim-setupphp-problem)

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
<span id="post-12330-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12330-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-12330-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I checkout osm2pgsql from svn and I manualy compile it.</p>
<p>when I execute seture.php it create database and table and next it say me :</p>
<pre><code>[...]
CREATE TABLE
SET
SET
SET
SET
SET
SET
SET
SET
CREATE TABLE
ALTER TABLE
Import
ERROR: please download and build osm2pgsql
please download and build osm2pgsql</code></pre>
<p>What may I miss?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Apr '12, 13:21</strong></p>
<img src="https://secure.gravatar.com/avatar/6c6458929c11785783ae7ca2e5bc3d56?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christophe%20DEBOVE&#39;s gravatar image" />
<p><span>Christophe D...</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christophe DEBOVE has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-12330" class="comments-container">
&#10;</div>
<div id="comment-tools-12330" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12330-form-container" class="comment-form-container">
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

<span id="12335"></span>

<div id="answer-container-12335" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-12335-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12335-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-12335-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You most likely forgot to set up your local configuration in <code>settings/local.php</code>. There you can state where your <code>osm2pgsql</code> binary resides. See the last step of <a href="http://wiki.openstreetmap.org/wiki/Nominatim/Installation#Compiling_the_Required_Software">Compiling the required software</a> in the installation instructions for an example.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Apr '12, 17:32</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-12335" class="comments-container">
&#10;</div>
<div id="comment-tools-12335" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12335-form-container" class="comment-form-container">
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


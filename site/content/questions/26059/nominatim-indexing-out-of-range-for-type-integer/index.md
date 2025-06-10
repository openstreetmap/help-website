+++
type = "question"
title = "Nominatim indexing: &quot;out of range for type integer&quot;"
description = '''While running &quot;./utils/setup.php --index --create-search-indices&quot;, I got this error: Done 19100942 in 44346 @ 430.725250 per second - Rank 30 ETA (seconds): 133549.953125 index_placex: UPDATE failed: ERROR: value &quot;2226265960&quot; is out of range for type integer CONTEXT: SQL statement &quot;SELECT place_id f...'''
date = "2013-09-02T02:34:00Z"
lastmod = "2013-11-17T20:04:00Z"
weight = 26059
keywords = [ "postgresql", "overflow", "nominatim", "indexing", "integer" ]
aliases = [ "/questions/26059" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Nominatim indexing: "out of range for type integer"](/questions/26059/nominatim-indexing-out-of-range-for-type-integer)

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
<span id="post-26059-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26059-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-26059-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>While running "./utils/setup.php --index --create-search-indices", I got this error:</p>
<pre><code>Done 19100942 in 44346 @ 430.725250 per second - Rank 30 ETA (seconds): 133549.953125
index_placex: UPDATE failed: ERROR:  value &quot;2226265960&quot; is out of range for type integer
CONTEXT:  SQL statement &quot;SELECT place_id from placex where osm_type=&#39;W&#39; and osm_id = substring(relation.members[i],2,200)::integer and rank_search = 26&quot;
PL/pgSQL function &quot;placex_update&quot; line 162 at SQL statement
ERROR: Error executing external command: /var/nominatim/nominatim/nominatim -i -d nominatim -t 7 -r 26</code></pre>
<p>What should I do to fix this?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-overflow" rel="tag" title="see questions tagged &#39;overflow&#39;">overflow</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-indexing" rel="tag" title="see questions tagged &#39;indexing&#39;">indexing</span> <span class="post-tag tag-link-integer" rel="tag" title="see questions tagged &#39;integer&#39;">integer</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Sep '13, 02:34</strong></p>
<img src="https://secure.gravatar.com/avatar/96d98fb13947dc1b70b3d7edd33a4b6b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mparncutt&#39;s gravatar image" />
<p><span>mparncutt</span><br />
<span class="score" title="61 reputation points">61</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mparncutt has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-26059" class="comments-container">
&#10;</div>
<div id="comment-tools-26059" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26059-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="26075"></span>

<div id="answer-container-26075" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-26075-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26075-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-26075-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="mparncutt has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Maybe this is an issue of <a href="http://wiki.openstreetmap.org/wiki/64-bit_Identifiers">64-bit_Identifiers</a></p>
<p>Please tell us how old your software framework is ... what version number has each component?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Sep '13, 16:43</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-26075" class="comments-container">
<span id="26086"></span>
<div id="comment-26086" class="comment">
<div id="post-26086-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I think the problem could be here:</p>
<pre><code>osm_id = substring(relation.members[i],2,200)::integer</code></pre>
<p>osm_id is defined in postgresql as bigint (64-bit) while integer is 32-bit</p>
<p>I've changed that line (and similar ones) in the postgresql procedure to this:</p>
<pre><code>osm_id = substring(relation.members[i],2,200)::bigint</code></pre>
<p>I'll report back when the indexing has finished.</p>
</div>
<div id="comment-26086-info" class="comment-info">
<span class="comment-age">(03 Sep '13, 03:15)</span> <span class="comment-user userinfo">mparncutt</span>
</div>
</div>
<span id="26105"></span>
<div id="comment-26105" class="comment">
<div id="post-26105-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>The change I mentioned above fixed my problem.</p>
<p>I notice that the latest code for Nominatim in GitHub includes this change, although the latest release (2.0.1) does not.</p>
</div>
<div id="comment-26105-info" class="comment-info">
<span class="comment-age">(04 Sep '13, 05:50)</span> <span class="comment-user userinfo">mparncutt</span>
</div>
</div>
</div>
<div id="comment-tools-26075" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26075-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="26458"></span>

<div id="answer-container-26458" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-26458-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26458-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-26458-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>may I ask how long it took to you to complete the 'create-search-indices' step? I ran it 4 days ago for the whole planet and it still working...</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Sep '13, 02:17</strong></p>
<img src="https://secure.gravatar.com/avatar/2565f75e2a9144cfab9cb82e6e377ecf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="neoasterix&#39;s gravatar image" />
<p><span>neoasterix</span><br />
<span class="score" title="16 reputation points">16</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="neoasterix has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-26458" class="comments-container">
<span id="26459"></span>
<div id="comment-26459" class="comment">
<div id="post-26459-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>It took me about a week. According to the OpenStreetMap wiki it took 10 days on the server for nominatim.openstreetmap.org</p>
</div>
<div id="comment-26459-info" class="comment-info">
<span class="comment-age">(18 Sep '13, 02:39)</span> <span class="comment-user userinfo">mparncutt</span>
</div>
</div>
</div>
<div id="comment-tools-26458" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26458-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="28175"></span>

<div id="answer-container-28175" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-28175-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28175-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-28175-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As I also just now stumbled upon this issue (with an EU database) and some searching led me to this question, I would like to add my found references and information, for any other people, wondering about their v.2.0.1-Nominatim's mean behaviour.</p>
<p>It was quite confusing at first because I did not take into account that this could have happened due to a too old Nominatim version. I started following instructions from the wiki which was not too long ago, but everything still was based on a zip including v2.0.1 (which seems to be dated back to the begin of the year). And also, there still are no newer Relase Notes than v2.0.1 in the <a href="https://github.com/twain47/Nominatim/wiki/_pages">Github Pages Overview</a> which made me hesitate to try any newer version.</p>
<p>Still, I found that quite old <a href="https://github.com/twain47/Nominatim/issues/46">discussion/bug report</a> explaining that there is really a known bug which has been dealt with.</p>
<p>So I continued research and noticed that recently, <strong>v2.1.0</strong> has been declared the <strong>stable version</strong>, includes these important bigint bugfixes, and the <a href="http://wiki.openstreetmap.org/wiki/Nominatim/Installation#First_Installation">basic setup</a> is also properly updated.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Nov '13, 20:04</strong></p>
<img src="https://secure.gravatar.com/avatar/ad8718bff2f6e9f5d3c9480351325924?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bewinter&#39;s gravatar image" />
<p><span>bewinter</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bewinter has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-28175" class="comments-container">
&#10;</div>
<div id="comment-tools-28175" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28175-form-container" class="comment-form-container">
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


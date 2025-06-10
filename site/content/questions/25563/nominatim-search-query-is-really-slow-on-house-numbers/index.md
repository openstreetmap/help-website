+++
type = "question"
title = "Nominatim search query is really slow on house numbers"
description = '''Hello. I have imported North America from pbf file and all TIGER data 2012 for house numbers in the US. When I do simple query like &quot;q=17th&quot; on my instance, I get results immedietely. But when I do query for house number like &quot;1250 14th Street&quot; search hangs for many minutes, with running process: &quot;p...'''
date = "2013-08-19T10:06:00Z"
lastmod = "2013-08-22T21:50:00Z"
weight = 25563
keywords = [ "search", "slow", "nominatim" ]
aliases = [ "/questions/25563" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Nominatim search query is really slow on house numbers](/questions/25563/nominatim-search-query-is-really-slow-on-house-numbers)

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
<span id="post-25563-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25563-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-25563-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello. I have imported North America from pbf file and all TIGER data 2012 for house numbers in the US.</p>
<p>When I do simple query like "q=17th" on my instance, I get results immedietely.</p>
<p>But when I do query for house number like "1250 14th Street" search hangs for many minutes, with running process: "postgres: nominatim nominatim_na [local] SELECT".</p>
<p>My slow query exactly looks like that:</p>
<p><a href="http://nominatim.openstreetmap.org/search?bounded=1&amp;viewbox=-105.58434900000003,40.225636,-104.67103400000002,39.456677&amp;q=1250%2014th%20street&amp;format=json&amp;addressdetails=1">http://nominatim.openstreetmap.org/search?bounded=1&amp;viewbox=-105.58434900000003,40.225636,-104.67103400000002,39.456677&amp;q=1250%2014th%20street&amp;format=json&amp;addressdetails=1</a></p>
<p>My settings:</p>
<p>13GB RAM on the machine</p>
<p>postgresql.conf:</p>
<p>autovacuum=off<br />
shared_buffers =4GB<br />
work_mem = 320MB<br />
maintenance work mem = 256MB<br />
effective cache size = 6GB</p>
<p>What could be the reason?</p>
<p>Regards,<br />
Michael</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-search" rel="tag" title="see questions tagged &#39;search&#39;">search</span> <span class="post-tag tag-link-slow" rel="tag" title="see questions tagged &#39;slow&#39;">slow</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Aug '13, 10:06</strong></p>
<img src="https://secure.gravatar.com/avatar/2cf4c8e19da3aade095e63b039c0d155?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="emvu&#39;s gravatar image" />
<p><span>emvu</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="emvu has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-25563" class="comments-container">
&#10;</div>
<div id="comment-tools-25563" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25563-form-container" class="comment-form-container">
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

<span id="25674"></span>

<div id="answer-container-25674" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-25674-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25674-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-25674-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This sounds like the indexes on the TIGER house number table are not properly used. Make sure that the <code>location_property_tiger</code> has its two indexes, one on <code>place_id</code> and one on <code>parent_place_id/housenumber</code>. If the indexes are there, it normally helps to run an ANALYSE on the table.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Aug '13, 21:50</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span> </br></br></p>
</div>
</div>
<div id="comments-container-25674" class="comments-container">
&#10;</div>
<div id="comment-tools-25674" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25674-form-container" class="comment-form-container">
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


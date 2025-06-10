+++
type = "question"
title = "missing ways"
description = '''Hello, I&#x27;ve processed &quot;central-america-latest.osm.pbf&quot;-file and have loaded into MySQL, then what I discovered made me doubt: SELECT count(idWay) FROM (SELECT DISTINCT idWay FROM osm.waynds) w1 - TOTAL NUMBER OF WAYS - 6885317 SELECT count(id) FROM osm.ways - it&#x27;s the TABLE OF WAYS - 6885317 SELECT ...'''
date = "2019-09-18T06:16:00Z"
lastmod = "2019-09-20T09:03:00Z"
weight = 70825
keywords = [ "missing_ways" ]
aliases = [ "/questions/70825" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [missing ways](/questions/70825/missing-ways)

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
<span id="post-70825-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70825-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70825-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, I've processed "central-america-latest.osm.pbf"-file and have loaded into MySQL, then what I discovered made me doubt:</p>
<p>SELECT count(idWay) FROM (SELECT DISTINCT idWay FROM osm.waynds) w1 - TOTAL NUMBER OF WAYS - 6885317 SELECT count(id) FROM osm.ways - it's the TABLE OF WAYS - 6885317</p>
<p>SELECT count(idMember) FROM (SELECT DISTINCT idMember FROM osm.relationMembers WHERE type = 'w') r1 - NUMBER OF RELAT/MEMBERS WHICH ARE WAYS ----- 149861</p>
<p>SELECT count(idMember) FROM (SELECT DISTINCT idMember FROM osm.relationMembers rm INNER JOIN osm.ways ON rm.idMember = ways.id) r1 - NUMBER OF RELAT/MEMBERS(ways) WHICH ARE COMPARED WITH "ways" TABLE----- 144335</p>
<p>it turns out that despite of large number(6885317), there are missing ways in the way list. And I'd like to get explanation about this case</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-missing_ways" rel="tag" title="see questions tagged &#39;missing_ways&#39;">missing_ways</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Sep '19, 06:16</strong></p>
<img src="https://secure.gravatar.com/avatar/808c67918e53a857cb62c78ab567f28b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Miky8888&#39;s gravatar image" />
<p><span>Miky8888</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Miky8888 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-70825" class="comments-container">
&#10;</div>
<div id="comment-tools-70825" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70825-form-container" class="comment-form-container">
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

<span id="70826"></span>

<div id="answer-container-70826" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70826-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70826-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-70826-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I am not familiar with the database schema you have used here. However the most likely reason for those 5000 ways is that they are part of relations that have some members inside, and some members outside the Central American bounds polygon. For example, the boundary of the USA (relation 148838) has over 800 ways. Some of them are "in" Central America but it would be a bad idea if the file would therefore contain the whole US boundary. The same is likely true for the boundary of France which has some overseas territory in the area, and so on.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Sep '19, 06:58</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-70826" class="comments-container">
<span id="70857"></span>
<div id="comment-70857" class="comment">
<div id="post-70857-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ok, thank you, is there some proto-file for compiling pbf-files. I've used the module that use another proto-file, strange is that some files can't be processed by this module, and I would like to get proto-file from official site.</p>
</div>
<div id="comment-70857-info" class="comment-info">
<span class="comment-age">(20 Sep '19, 09:03)</span> <span class="comment-user userinfo">Miky8888</span>
</div>
</div>
</div>
<div id="comment-tools-70826" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70826-form-container" class="comment-form-container">
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


+++
type = "question"
title = "JOSM&#x27;s shapefile-enabling plugin (opendata) seems to leave tags blank"
description = '''I&#x27;m using JOSM v 14824 and open data v. 34911. For years, I&#x27;ve been able to use this combo (earlier versions) to open shapefiles (.shp) with absolutely no problems, including multipolygons, etc. The tags would show up as tags do on objects in JOSM. However, recently, I can open shapefiles, but there...'''
date = "2019-04-04T00:23:00Z"
lastmod = "2019-06-04T02:06:00Z"
weight = 68628
keywords = [ "shapefile", "josm", "tags" ]
aliases = [ "/questions/68628" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [JOSM's shapefile-enabling plugin (opendata) seems to leave tags blank](/questions/68628/josms-shapefile-enabling-plugin-opendata-seems-to-leave-tags-blank)

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
<span id="post-68628-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68628-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68628-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm using JOSM v 14824 and open data v. 34911. For years, I've been able to use this combo (earlier versions) to open shapefiles (.shp) with absolutely no problems, including multipolygons, etc. The tags would show up as tags do on objects in JOSM.</p>
<p>However, recently, I can open shapefiles, but there are absolutely no tags displayed in JOSM when I select an object in the shapefile: everything is tagged simply "0" (zero). Yes, I've updated my plugins, the versions (including dependency plugins, like log4j) are all current.</p>
<p>Has anybody else seen this? Is it a known and/or reported bug?</p>
<p>Thanks, Steve</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-shapefile" rel="tag" title="see questions tagged &#39;shapefile&#39;">shapefile</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-tags" rel="tag" title="see questions tagged &#39;tags&#39;">tags</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Apr '19, 00:23</strong></p>
<img src="https://secure.gravatar.com/avatar/cf7aea21ed49687fadf85fd50e79d16b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stevea&#39;s gravatar image" />
<p><span>stevea</span><br />
<span class="score" title="22 reputation points">22</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stevea has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-68628" class="comments-container">
<span id="68645"></span>
<div id="comment-68645" class="comment">
<div id="post-68645-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Still occurring with JOSM upgrade to v. 14945. (OD 34911 didn't change but did participate in the plugins upgrade cycle at JOSM upgrade/relaunch).</p>
</div>
<div id="comment-68645-info" class="comment-info">
<span class="comment-age">(04 Apr '19, 17:55)</span> <span class="comment-user userinfo">stevea</span>
</div>
</div>
<span id="68654"></span>
<div id="comment-68654" class="comment">
<div id="post-68654-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You can create a JOSM ticket by using menu Help -&gt; Report bug from within JOSM and attach your shapefile there.</p>
</div>
<div id="comment-68654-info" class="comment-info">
<span class="comment-age">(04 Apr '19, 20:49)</span> <span class="comment-user userinfo">Klumbumbus</span>
</div>
</div>
</div>
<div id="comment-tools-68628" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68628-form-container" class="comment-form-container">
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

<span id="69434"></span>

<div id="answer-container-69434" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69434-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69434-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-69434-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As of JOSM v 15155, this appears to be working again.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Jun '19, 02:06</strong></p>
<img src="https://secure.gravatar.com/avatar/cf7aea21ed49687fadf85fd50e79d16b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stevea&#39;s gravatar image" />
<p><span>stevea</span><br />
<span class="score" title="22 reputation points">22</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stevea has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-69434" class="comments-container">
&#10;</div>
<div id="comment-tools-69434" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69434-form-container" class="comment-form-container">
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


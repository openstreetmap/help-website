+++
type = "question"
title = "Filter polygon nodes but ignore those that form angles ~90 degs"
description = '''Hi I&#x27;ve a boundary polygon I wish to import into OSM (Don&#x27;t worry, it has the required licence). However there are far too many nodes. I have software to filter them out by distance or frequency, but that removes certain intricate sections (in this case, as it passes between a number of houses.) Is ...'''
date = "2019-02-18T19:11:00Z"
lastmod = "2019-02-18T19:50:00Z"
weight = 68043
keywords = [ "filter", "nodes", "polygon" ]
aliases = [ "/questions/68043" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Filter polygon nodes but ignore those that form angles ~90 degs](/questions/68043/filter-polygon-nodes-but-ignore-those-that-form-angles-90-degs)

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
<span id="post-68043-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68043-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-68043-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi I've a boundary polygon I wish to import into OSM (Don't worry, it has the required licence). However there are far too many nodes. I have software to filter them out by distance or frequency, but that removes certain intricate sections (in this case, as it passes between a number of houses.)</p>
<p>Is there any software or algorithm which can ignore nodes which form angles around 90 degrees? I've the data in a number of formats (CSV, XML, GeoJSON etc)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-polygon" rel="tag" title="see questions tagged &#39;polygon&#39;">polygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Feb '19, 19:11</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-68043" class="comments-container">
<span id="68044"></span>
<div id="comment-68044" class="comment">
<div id="post-68044-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>not really answering your question re. the 90°, but I guess the <a href="https://en.wikipedia.org/wiki/Ramer%E2%80%93Douglas%E2%80%93Peucker_algorithm">Ramer–Douglas–Peucker algorithm</a> which is (<a href="https://blog.gpsies.com/article/170/douglas-peucker-reloaded-gps-track-glaetten-vereinfachen-oder-reduzieren">as far as I know</a>) used by e.g. <a href="https://www.gpsies.com/createTrack.do">GPSies</a> (import/upload gpx, simplify, download - does <del>not</del> need a login) should work fine.</p>
</div>
<div id="comment-68044-info" class="comment-info">
<span class="comment-age">(18 Feb '19, 19:50)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-68043" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68043-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>


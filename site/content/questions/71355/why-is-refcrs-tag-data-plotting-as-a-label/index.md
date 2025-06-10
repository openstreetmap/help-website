+++
type = "question"
title = "Why is ref:crs tag data plotting as a label?"
description = '''Hi all, Apologies if this is a naive question. I&#x27;m new to editing OSM.  The ref:crs tag for Tondu rail station is plotting onto maps such as OpenRailwayMap as a high-level label. To recreate this issue:   - search &quot;Tondu&quot; on www.openrailwaymap.org,   - click on the &quot;Tondu Station&quot; item, then   - zoo...'''
date = "2019-10-28T15:45:00Z"
lastmod = "2019-10-29T10:34:00Z"
weight = 71355
keywords = [ "zoomlevel", "railway", "openrailwaymap", "refcrs", "labels" ]
aliases = [ "/questions/71355" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Why is ref:crs tag data plotting as a label?](/questions/71355/why-is-refcrs-tag-data-plotting-as-a-label)

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
<span id="post-71355-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71355-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-71355-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all,</p>
<p>Apologies if this is a naive question. I'm new to editing OSM.<br />
The ref:crs tag for Tondu rail station is plotting onto maps such as OpenRailwayMap as a high-level label.</p>
<p>To recreate this issue:<br />
- search "Tondu" on www.openrailwaymap.org,<br />
- click on the "Tondu Station" item, then<br />
- zoom out four times.</p>
<p>I've trawled through the properties of this node and posts on this forum and can't figure out why this is.</p>
<p>This is presumably a Mapnik issue, but I figure there must be a way to edit this behaviour away within OSM, right?<br />
Can anyone help?</p>
<p>Cheers, Rob</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-zoomlevel" rel="tag" title="see questions tagged &#39;zoomlevel&#39;">zoomlevel</span> <span class="post-tag tag-link-railway" rel="tag" title="see questions tagged &#39;railway&#39;">railway</span> <span class="post-tag tag-link-openrailwaymap" rel="tag" title="see questions tagged &#39;openrailwaymap&#39;">openrailwaymap</span> <span class="post-tag tag-link-refcrs" rel="tag" title="see questions tagged &#39;refcrs&#39;">refcrs</span> <span class="post-tag tag-link-labels" rel="tag" title="see questions tagged &#39;labels&#39;">labels</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Oct '19, 15:45</strong></p>
<img src="https://secure.gravatar.com/avatar/1d82674d5f01eda416a469b6982dfe85?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RobDataCymru&#39;s gravatar image" />
<p><span>RobDataCymru</span><br />
<span class="score" title="25 reputation points">25</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RobDataCymru has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-71355" class="comments-container">
&#10;</div>
<div id="comment-tools-71355" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71355-form-container" class="comment-form-container">
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

<span id="71362"></span>

<div id="answer-container-71362" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71362-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71362-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-71362-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This appears to be a stylistic choice by those running OpenRailwayMap, presumably to make stations identifiable on a wider view with fewer label collision. If you zoom into Germany there are many more stations that appear at these zoom levels.</p>
<p>In general you <a href="https://wiki.openstreetmap.org/wiki/Tagging_for_the_renderer">shouldn't tag for the renderer</a> as more <code>ref:crs</code> tags are added over time the rendering is likely to look a lot more reasonable.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Oct '19, 23:06</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span> </br></br></p>
</div>
</div>
<div id="comments-container-71362" class="comments-container">
<span id="71364"></span>
<div id="comment-71364" class="comment">
<div id="post-71364-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ah yes. Looking at France and Germany, this makes sense.</p>
<p>Saying that, many other UK stations do seem to have the ref:crs but aren't rendered... I'm guessing this is something to do with the other tags on each station. I'll keep digging...</p>
</div>
<div id="comment-71364-info" class="comment-info">
<span class="comment-age">(29 Oct '19, 10:34)</span> <span class="comment-user userinfo">RobDataCymru</span>
</div>
</div>
</div>
<div id="comment-tools-71362" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71362-form-container" class="comment-form-container">
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


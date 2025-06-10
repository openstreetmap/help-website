+++
type = "question"
title = "How to remove &quot;hidden nonop tag&quot; from line or route?"
description = '''As I learn, I found the OSM Inspector and trying to clean up some of the errors in my local travel area. One thing I keep finding is the &quot;nonop&quot; tag. Is this due to areas that are partially under construction and thus have two tags related to the line? Do I just have to remove the &quot;old&quot; tag, such as...'''
date = "2019-04-10T05:49:00Z"
lastmod = "2019-04-10T10:17:00Z"
weight = 68740
keywords = [ "nonop", "hidden", "osminspector" ]
aliases = [ "/questions/68740" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to remove "hidden nonop tag" from line or route?](/questions/68740/how-to-remove-hidden-nonop-tag-from-line-or-route)

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
<span id="post-68740-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68740-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68740-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>As I learn, I found the OSM Inspector and trying to clean up some of the errors in my local travel area. One thing I keep finding is the "nonop" tag. Is this due to areas that are partially under construction and thus have two tags related to the line?</p>
<p>Do I just have to remove the "old" tag, such as construction for that line?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nonop" rel="tag" title="see questions tagged &#39;nonop&#39;">nonop</span> <span class="post-tag tag-link-hidden" rel="tag" title="see questions tagged &#39;hidden&#39;">hidden</span> <span class="post-tag tag-link-osminspector" rel="tag" title="see questions tagged &#39;osminspector&#39;">osminspector</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Apr '19, 05:49</strong></p>
<img src="https://secure.gravatar.com/avatar/64205d7e767055bacbe54a5d6b893164?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MeMaps&#39;s gravatar image" />
<p><span>MeMaps</span><br />
<span class="score" title="71 reputation points">71</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MeMaps has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-68740" class="comments-container">
&#10;</div>
<div id="comment-tools-68740" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68740-form-container" class="comment-form-container">
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

<span id="68741"></span>

<div id="answer-container-68741" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68741-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68741-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-68741-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The term "hidden nonop tag" is misleading.</p>
<p>No tags are hidden, all tags are in plain sight, and any editor can be used to add or remove them.</p>
<p>The longer story is this:</p>
<p>OSM allows you to record infinite detail about something. For example, if you just are interested on anything that people or vehicles can move on, you might say "I am looking at anything that has a highway tag". If you are looking only for major roads you might say "I am looking at anything that has a <code>highway=motorway</code> or <code>highway=trunk</code> tag". And there can be lots of additional tags that modify the meaning but normally the additional tags should not turn the meaning around altogether. You don't want something tagged <code>highway=motorway</code> and then <code>note=not actually a motorway, just a little brick path in my garden!!!</code>. This will confuse applications. Now there used to be a time when people would use <code>construction=yes</code> or <code>disused=yes</code> together with something like <code>highway=motorway</code> to indicate it was under construction or disused; this led to confusion among those who just looked at <code>highway=motorway</code> and assumed that's something where cars can travel. Hence we've now switched to different models of tagging these situations, that do not use a highway tag. If you have a <code>highway=motorway construction=yes</code> it could for example happen that some routing engines disregard the <code>construction=yes</code> and use the road, and others don't.</p>
<p>What the OSM Inspector wants to say is: Here is something that on first glance looks like a highway, building, or something, and there are additional tags that say "no, it isn't yet" or "no, it isn't anymore".</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Apr '19, 07:46</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-68741" class="comments-container">
<span id="68747"></span>
<div id="comment-68747" class="comment">
<div id="post-68747-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I recently found that the wiki calls these "trolltags" - <a href="https://wiki.openstreetmap.org/wiki/Trolltag">https://wiki.openstreetmap.org/wiki/Trolltag</a></p>
</div>
<div id="comment-68747-info" class="comment-info">
<span class="comment-age">(10 Apr '19, 10:17)</span> <span class="comment-user userinfo">Andy Allan</span>
</div>
</div>
</div>
<div id="comment-tools-68741" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68741-form-container" class="comment-form-container">
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


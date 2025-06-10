+++
type = "question"
title = "Why does the cycleway I just added appear less prominently than the other cycleways in the same park?"
description = '''Yesterday I added several segments of cycleway to Rebecca Park in Greenfield, Minnesota. My additions do appear today on the Open Street Map web site but not as prominently as the other cycleways in the same park. My additions are fainter, narrower and only appear when you zoom down more closely, wh...'''
date = "2020-11-24T16:22:00Z"
lastmod = "2020-11-24T17:06:00Z"
weight = 77691
keywords = [ "zoomlevel", "width", "brighter" ]
aliases = [ "/questions/77691" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Why does the cycleway I just added appear less prominently than the other cycleways in the same park?](/questions/77691/why-does-the-cycleway-i-just-added-appear-less-prominently-than-the-other-cycleways-in-the-same-park)

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
<span id="post-77691-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77691-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-77691-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Yesterday I added several segments of cycleway to Rebecca Park in Greenfield, Minnesota. My additions do appear today on the Open Street Map web site but not as prominently as the other cycleways in the same park. My additions are fainter, narrower and only appear when you zoom down more closely, whereas the other cycleways appear at higher (more distant) zoom ranges.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-zoomlevel" rel="tag" title="see questions tagged &#39;zoomlevel&#39;">zoomlevel</span> <span class="post-tag tag-link-width" rel="tag" title="see questions tagged &#39;width&#39;">width</span> <span class="post-tag tag-link-brighter" rel="tag" title="see questions tagged &#39;brighter&#39;">brighter</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Nov '20, 16:22</strong></p>
<img src="https://secure.gravatar.com/avatar/d93ee0bab1c231e7f8428911616da5a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Renner%20Anderson&#39;s gravatar image" />
<p><span>Renner Anderson</span><br />
<span class="score" title="26 reputation points">26</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Renner Anderson has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Nov '20, 16:24</strong> </span></p>
</div>
</div>
<div id="comments-container-77691" class="comments-container">
&#10;</div>
<div id="comment-tools-77691" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77691-form-container" class="comment-form-container">
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

<span id="77692"></span>

<div id="answer-container-77692" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77692-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77692-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-77692-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It is to do with the access tags, and in particular probably the access=no one. If you compare <a href="https://www.openstreetmap.org/way/876263323">this way you added</a> with <a href="https://www.openstreetmap.org/way/189412627">this one that already existed</a> you can see the difference is the access restrictions. There are differing views on whether you need quite so many access tags on cycleways. Cycle access is normally assumed, foot is often added if pedestrians can also use it, but often it is assumed that motor vehicles can't access it so none of your exclusions are usually added, though there is nothing wrong in being explicit. However I suspect it is that default access=no by default and then adding the explicit yes values that causes the faintness (like the P for private car parks compared to non-private ones).</p>
<p>Edit: Also, I'm not an expert, but I think it is the area of the stylesheet around <a href="https://github.com/gravitystorm/openstreetmap-carto/blob/master/style/roads.mss#L1951">this line</a> which is relevant.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Nov '20, 17:06</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Nov '20, 17:15</strong> </span></p>
</div>
</div>
<div id="comments-container-77692" class="comments-container">
&#10;</div>
<div id="comment-tools-77692" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77692-form-container" class="comment-form-container">
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


+++
type = "question"
title = "how do i edit/delete large river polygons"
description = '''Hi, We have a river polygon of several miles labeled as riverbank, yet the polygon and river linear data were obviously obtained from USGS NHD which is over 40 years old and not even close to where the river currently exist. A river linear is appropriate and easy enough to digitize using the aerial ...'''
date = "2018-06-28T17:26:00Z"
lastmod = "2018-06-29T13:30:00Z"
weight = 64421
keywords = [ "edit", "river", "polygons", "riverbank" ]
aliases = [ "/questions/64421" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [how do i edit/delete large river polygons](/questions/64421/how-do-i-editdelete-large-river-polygons)

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
<span id="post-64421-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64421-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-64421-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, We have a river polygon of several miles labeled as riverbank, yet the polygon and river linear data were obviously obtained from USGS NHD which is over 40 years old and not even close to where the river currently exist. A river linear is appropriate and easy enough to digitize using the aerial imagery. My goal is to delete the polygon and then edit/re-digitize the river.</p>
<p>When I select the river polygon and try to delete it, I receive the message the entire selected polygon is not visible and cannot be deleted. How do I cut the polygon to be within the visible editing range and/or cut the river polygon into editable sizes so I can correct this. Thanks for your help.</p>
<p>Bob812Many</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-edit" rel="tag" title="see questions tagged &#39;edit&#39;">edit</span> <span class="post-tag tag-link-river" rel="tag" title="see questions tagged &#39;river&#39;">river</span> <span class="post-tag tag-link-polygons" rel="tag" title="see questions tagged &#39;polygons&#39;">polygons</span> <span class="post-tag tag-link-riverbank" rel="tag" title="see questions tagged &#39;riverbank&#39;">riverbank</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Jun '18, 17:26</strong></p>
<img src="https://secure.gravatar.com/avatar/f6bbc141d72e275a6ee31bf552ea371a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bob82many&#39;s gravatar image" />
<p><span>bob82many</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bob82many has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-64421" class="comments-container">
&#10;</div>
<div id="comment-tools-64421" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64421-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="64423"></span>

<div id="answer-container-64423" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64423-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64423-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-64423-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This sounds like you are trying to do this in iD, which given the size of the object is not a good idea.</p>
<p>I would typically recommend using JOSM for such work (this is not in the context of editor wars, if an object is so large that it can't be viewed in editing mode in iD it is simply a practical concern), which should have the added advantage of allowing you to modify the existing geometries easy and fast enough that wholesale deletion is not necessary (if possible we always try to preserve an objects history, naturally if it is an untouched import there is little to be gained from that).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Jun '18, 20:27</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Jun '18, 20:29</strong> </span></p>
</div>
</div>
<div id="comments-container-64423" class="comments-container">
&#10;</div>
<div id="comment-tools-64423" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64423-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="64443"></span>

<div id="answer-container-64443" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64443-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64443-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-64443-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>A simple short term solution without using JOSM would be to retag the riverbank polygon by prefixing the waterway value, for instance disused:waterway=riverbank or similar (see <a href="https://wiki.openstreetmap.org/wiki/Lifecycle_prefix">Lifecycle prefix</a>, although most are for man made features, the concept is fine). Perhaps add a fixme too.</p>
<p>You can then draw the river centre line (or perhaps preferably the flowline or <a href="https://en.wikipedia.org/wiki/Thalweg">thalweg</a>) in its current position (or as current as aerial imagery allows).</p>
<p>The net effect is that the old polygon will no longer be rendered and the new centre line will show up. The polygon can then be cleaned up at your leisure.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Jun '18, 13:30</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-64443" class="comments-container">
&#10;</div>
<div id="comment-tools-64443" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64443-form-container" class="comment-form-container">
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


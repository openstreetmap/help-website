+++
type = "question"
title = "Is there an editor with the same functionality as Potlatch 1&#x27;s &#x27;Undelete&#x27;"
description = '''Hi I&#x27;m missing Potlatch 1&#x27;s &#x27;Undelete&#x27; command where a user could zoom to an area, press the &#x27;U&#x27; key &amp;amp; it would display all deleted entities in red from which the user could choose which to undelete. To restore objects in JOSM the specific id of each object has to be known &amp;amp; supplied. Is the...'''
date = "2021-06-26T16:37:00Z"
lastmod = "2021-06-28T19:07:00Z"
weight = 80726
keywords = [ "undelete", "restore", "potlatch", "josm" ]
aliases = [ "/questions/80726" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Is there an editor with the same functionality as Potlatch 1's 'Undelete'](/questions/80726/is-there-an-editor-with-the-same-functionality-as-potlatch-1s-undelete)

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
<span id="post-80726-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80726-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-80726-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi I'm missing Potlatch 1's 'Undelete' command where a user could zoom to an area, press the 'U' key &amp; it would display all deleted entities in red from which the user could choose which to undelete. To restore objects in JOSM the specific id of each object has to be known &amp; supplied.</p>
<p>Is there another utility which has P1's convenience.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-undelete" rel="tag" title="see questions tagged &#39;undelete&#39;">undelete</span> <span class="post-tag tag-link-restore" rel="tag" title="see questions tagged &#39;restore&#39;">restore</span> <span class="post-tag tag-link-potlatch" rel="tag" title="see questions tagged &#39;potlatch&#39;">potlatch</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Jun '21, 16:37</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Jun '21, 17:42</strong> </span></p>
</div>
</div>
<div id="comments-container-80726" class="comments-container">
&#10;</div>
<div id="comment-tools-80726" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80726-form-container" class="comment-form-container">
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

<span id="80727"></span>

<div id="answer-container-80727" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80727-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80727-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-80727-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Sadly no; there is no API call that returns deleted objects in an area that other editors could use. Potlatch 1 was using a very specific API that, while not yet decommissioned, will probably be retired very soon, and the "modern day" XML/JSON based API does not have a replacement.</p>
<p>It is not impossible to build such an API but fraught with problems and difficulties. For example, when undeleting an old way which happened to use a node that was not deleted, and meanwhile moved across town, what do you do - and things like that.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Jun '21, 16:47</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-80727" class="comments-container">
<span id="80729"></span>
<div id="comment-80729" class="comment">
<div id="post-80729-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Would the upload problem you highlight be a similar problem in JOSM?</p>
<p>Even if the utility was restricted to just being able to see the objects &amp; to retrieve the ids to use in JOSM's undelete, would be of benefit.</p>
</div>
<div id="comment-80729-info" class="comment-info">
<span class="comment-age">(26 Jun '21, 17:42)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
<span id="80743"></span>
<div id="comment-80743" class="comment">
<div id="post-80743-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="/questions/50707/locating-deleted-items">This</a> previous question has an Overpass based solution for retrieval. I don't know if this could be retrieved directly into JOSM?</p>
</div>
<div id="comment-80743-info" class="comment-info">
<span class="comment-age">(27 Jun '21, 01:23)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
<span id="80767"></span>
<div id="comment-80767" class="comment">
<div id="post-80767-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/4426/insertuser"></a><a href="https://help.openstreetmap.org/users/4426/insertuser">@InsertUser</a> I don't quite grok this query (<a href="https://overpass-turbo.eu/s/18Vf">https://overpass-turbo.eu/s/18Vf</a> in case anyone wants to play with it) but it appears to highlight the position of deleted and modified ways within the bounding box. I think maybe only those that intersected still extant elements -- so a deleted building, for instance, might not show.</p>
<p>Personally I use achavi (<a href="https://nrenner.github.io/achavi/)">https://nrenner.github.io/achavi/)</a> for sleuthing deletions -- just zoom in to the area in question (or draw a bbox), set a date range in the date boxes, and click "load". It will distinguish between moved elements in dark red and deleted ones in bright red. But it doesn't usually work well unless your search area is tiny and and your date range is short, so you need a pretty good idea about what you're looking for and when it was deleted.</p>
</div>
<div id="comment-80767-info" class="comment-info">
<span class="comment-age">(28 Jun '21, 19:07)</span> <span class="comment-user userinfo">jmapb</span>
</div>
</div>
</div>
<div id="comment-tools-80727" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80727-form-container" class="comment-form-container">
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


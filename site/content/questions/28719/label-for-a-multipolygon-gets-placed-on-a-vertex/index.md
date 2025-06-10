+++
type = "question"
title = "Label for a multipolygon gets placed on a vertex"
description = '''After creating the multipolygon http://www.openstreetmap.org/relation/3342120 , I realized that its museum symbol and the relative label on the OSM standard layer gets placed on a vertex rather than somewhere roughly in the middle of the multipolygon. Is this a known issue or am I doing something wr...'''
date = "2013-12-03T13:59:00Z"
lastmod = "2013-12-04T12:12:00Z"
weight = 28719
keywords = [ "labels", "mapnik", "multipolygon" ]
aliases = [ "/questions/28719" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Label for a multipolygon gets placed on a vertex](/questions/28719/label-for-a-multipolygon-gets-placed-on-a-vertex)

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
<span id="post-28719-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28719-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-28719-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>After creating the multipolygon <a href="http://www.openstreetmap.org/relation/3342120">http://www.openstreetmap.org/relation/3342120</a> , I realized that its museum symbol and the relative label on the OSM standard layer gets placed on a vertex rather than somewhere roughly in the middle of the multipolygon. Is this a known issue or am I doing something wrong?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-labels" rel="tag" title="see questions tagged &#39;labels&#39;">labels</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-multipolygon" rel="tag" title="see questions tagged &#39;multipolygon&#39;">multipolygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Dec '13, 13:59</strong></p>
<img src="https://secure.gravatar.com/avatar/0e00cf7b1db1273b37a075c54b383d02?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Decan&#39;s gravatar image" />
<p><span>Decan</span><br />
<span class="score" title="351 reputation points">351</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Decan has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Dec '13, 15:25</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-28719" class="comments-container">
<span id="28720"></span>
<div id="comment-28720" class="comment">
<div id="post-28720-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>the relation looks fine to me. Not sure why that is done. At <a href="http://www.openstreetmap.org/relation/2972737">relation/2972737</a> it is in the middle. I had a look at <a href="http://overpass-turbo.eu/s/1FS">some other museum relations</a>, but could not find one which is clearly the same case as yours.</p>
</div>
<div id="comment-28720-info" class="comment-info">
<span class="comment-age">(03 Dec '13, 15:09)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="28734"></span>
<div id="comment-28734" class="comment">
<div id="post-28734-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I do not think it is strictly related with the relation being a museum, and not even with being a multipolygon. A similar thing happened to me with a pedestrian area (that I further modified afterwards, therefore the problem disappeared): the only thing these two examples have in common is the presence of some narrow 'branches' emanating from the (multi)polygon.</p>
</div>
<div id="comment-28734-info" class="comment-info">
<span class="comment-age">(03 Dec '13, 17:54)</span> <span class="comment-user userinfo">Decan</span>
</div>
</div>
<span id="28757"></span>
<div id="comment-28757" class="comment">
<div id="post-28757-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Seems to be just an rendering error to me. As some other users did, I also checked the data - could not find anything wrong. A long time ago there were problems related to the direction of the outer/inner ways in a multipolygon relation, but I believe they were solved a long time ago as well. Or not. Anyway, since the data seems to be correct, I would not worry a lot about this issue.</p>
</div>
<div id="comment-28757-info" class="comment-info">
<span class="comment-age">(04 Dec '13, 12:12)</span> <span class="comment-user userinfo">MCPicoli</span>
</div>
</div>
</div>
<div id="comment-tools-28719" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28719-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>


+++
type = "question"
title = "How large (in disk size) is a current complete tile set?"
description = '''If I would set up Mapnik to render static map tiles of the whole planet, how large in disk size would the resulting set of files be? Does the volume get larger over time, as more detail is added which compresses worse? Are all theoretical tiles rendered, e.g. all zoom levels of the oceans? If not, h...'''
date = "2011-06-28T16:37:00Z"
lastmod = "2011-07-03T13:33:00Z"
weight = 6062
keywords = [ "tile", "mapnik", "size" ]
aliases = [ "/questions/6062" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How large (in disk size) is a current complete tile set?](/questions/6062/how-large-in-disk-size-is-a-current-complete-tile-set)

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
<span id="post-6062-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6062-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-6062-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>If I would set up Mapnik to render static map tiles of the whole planet, how large in disk size would the resulting set of files be? Does the volume get larger over time, as more detail is added which compresses worse? Are all theoretical tiles rendered, e.g. all zoom levels of the oceans? If not, how many files are used?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tile" rel="tag" title="see questions tagged &#39;tile&#39;">tile</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-size" rel="tag" title="see questions tagged &#39;size&#39;">size</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Jun '11, 16:37</strong></p>
<img src="https://secure.gravatar.com/avatar/97f754e0356a74acc666550948b48bd6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hfs&#39;s gravatar image" />
<p><span>hfs</span><br />
<span class="score" title="851 reputation points">851</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hfs has 3 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-6062" class="comments-container">
&#10;</div>
<div id="comment-tools-6062" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6062-form-container" class="comment-form-container">
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

<span id="6067"></span>

<div id="answer-container-6067" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-6067-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6067-score" class="post-score" title="current number of votes">
11
</div>
<span id="post-6067-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="hfs has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Using data from tileservers that I have run before, I estimate the complete tileset of zooms 0-18 to be around 342 Tb in size. The style of the map does have a reasonably large effect on this result. Also, this is extrapolated from tiles that are actually used on a tileserver (around 500Gb) so have a bias towards non-ocean areas, but the estimate does take into account the different average file sizes at different zoom levels.</p>
<p>All in all, you could be looking at anything from 60Tb upwards. If you limit the number of zoom levels this changes dramatically - only 0-17 would mean only 20% of the space needed compared to 0-18, for example.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Jun '11, 18:51</strong></p>
<img src="https://secure.gravatar.com/avatar/c3743b1b368f5e209eb8aad30164acc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Allan&#39;s gravatar image" />
<p><span>Andy Allan</span><br />
<span class="score" title="12456 reputation points"><span>12.5k</span></span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="128 badges"><span class="silver">●</span><span class="badgecount">128</span></span><span title="153 badges"><span class="bronze">●</span><span class="badgecount">153</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andy Allan has 46 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-6067" class="comments-container">
<span id="6163"></span>
<div id="comment-6163" class="comment">
<div id="post-6163-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Percentage of actual viewed tiles on <a href="http://tile.osm.org">tile.osm.org</a>: <a href="http://wiki.openstreetmap.org/wiki/Tile_Disk_Usage">http://wiki.openstreetmap.org/wiki/Tile_Disk_Usage</a></p>
</div>
<div id="comment-6163-info" class="comment-info">
<span class="comment-age">(03 Jul '11, 13:33)</span> <span class="comment-user userinfo">Firefishy ♦♦</span>
</div>
</div>
</div>
<div id="comment-tools-6067" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6067-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="6112"></span>

<div id="answer-container-6112" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-6112-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6112-score" class="post-score" title="current number of votes">
-2
</div>
<span id="post-6112-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Are Mapnik images tiled using GDAL?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Jun '11, 16:10</strong></p>
<img src="https://secure.gravatar.com/avatar/89361ea0046f14162fd340e36f3408f6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cglazier&#39;s gravatar image" />
<p><span>cglazier</span><br />
<span class="score" title="-1 reputation points">-1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cglazier has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-6112" class="comments-container">
<span id="6119"></span>
<div id="comment-6119" class="comment">
<div id="post-6119-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>No.</p>
<p>(This is probably a separate question, though, so you should start a new question on this site rather than adding further questions to your original one.)</p>
</div>
<div id="comment-6119-info" class="comment-info">
<span class="comment-age">(30 Jun '11, 20:22)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
</div>
<div id="comment-tools-6112" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6112-form-container" class="comment-form-container">
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


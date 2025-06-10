+++
type = "question"
title = "How does Mapnik handle overlap problem during rendering dense dataset"
description = '''Hi: Suppose there are so many features(say they are pois) in a single tile, then how does osm handle the overlap problem? I know osm use mapnik as the render engine, and we can set some filters during the rendering at different zoom level, but how about the filter lost the effects? For example, in a...'''
date = "2014-05-21T06:58:00Z"
lastmod = "2014-05-28T09:23:00Z"
weight = 33343
keywords = [ "rendering", "mapnik", "overlap", "labeling" ]
aliases = [ "/questions/33343" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How does Mapnik handle overlap problem during rendering dense dataset](/questions/33343/how-does-mapnik-handle-overlap-problem-during-rendering-dense-dataset)

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
<span id="post-33343-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33343-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-33343-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi:</p>
<p>Suppose there are so many features(say they are pois) in a single tile, then how does osm handle the overlap problem?</p>
<p>I know osm use mapnik as the render engine, and we can set some filters during the rendering at different zoom level, but how about the filter lost the effects?</p>
<p>For example, in a specified zooom, even we use the filter, there are still some features close to each other, if render all of them, there must be some overlap, so how does osm handle this suitation?<br />
</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-overlap" rel="tag" title="see questions tagged &#39;overlap&#39;">overlap</span> <span class="post-tag tag-link-labeling" rel="tag" title="see questions tagged &#39;labeling&#39;">labeling</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 May '14, 06:58</strong></p>
<img src="https://secure.gravatar.com/avatar/8b5f2224482b0bc3648353d36a0c8814?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hguser&#39;s gravatar image" />
<p><span>hguser</span><br />
<span class="score" title="36 reputation points">36</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hguser has no accepted answers">0%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 May '14, 08:21</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-33343" class="comments-container">
&#10;</div>
<div id="comment-tools-33343" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33343-form-container" class="comment-form-container">
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

<span id="33347"></span>

<div id="answer-container-33347" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-33347-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33347-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-33347-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="hguser has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Mapnik, by default, does not draw overlapping features for icons and text symbolizers. So the features in the first layer are drawn first, one-by-one, and if there is no space remaining then they are not drawn.</p>
<p>This means that the order of the layers, and the order of the features within the layers, are important.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 May '14, 11:38</strong></p>
<img src="https://secure.gravatar.com/avatar/c3743b1b368f5e209eb8aad30164acc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Allan&#39;s gravatar image" />
<p><span>Andy Allan</span><br />
<span class="score" title="12456 reputation points"><span>12.5k</span></span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="128 badges"><span class="silver">●</span><span class="badgecount">128</span></span><span title="153 badges"><span class="bronze">●</span><span class="badgecount">153</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andy Allan has 46 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-33347" class="comments-container">
<span id="33374"></span>
<div id="comment-33374" class="comment">
<div id="post-33374-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Do you mean that mapnik draw all features in layer A, and it will process overlap for this layer(A), once it start to render the next layer(B),for a given feature from B,mapnik will detect if the place have been taken up by other rendered feature, if not , then render this feature? If so, does it mean that the conflict(overlap) detect just happen between features in the same layer?</p>
</div>
<div id="comment-33374-info" class="comment-info">
<span class="comment-age">(22 May '14, 12:00)</span> <span class="comment-user userinfo">hguser</span>
</div>
</div>
<span id="33521"></span>
<div id="comment-33521" class="comment">
<div id="post-33521-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>By default mapnik has just one collision detection cache, which records the placements across all the layers (so that e.g. text in the roads layer avoids text from points of interest). It's possible to reset the cache between layers, but that usually leads to poor results.</p>
</div>
<div id="comment-33521-info" class="comment-info">
<span class="comment-age">(28 May '14, 09:23)</span> <span class="comment-user userinfo">Andy Allan</span>
</div>
</div>
</div>
<div id="comment-tools-33347" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33347-form-container" class="comment-form-container">
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


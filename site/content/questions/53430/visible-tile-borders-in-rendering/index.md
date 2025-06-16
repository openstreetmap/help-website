+++
type = "question"
title = "Visible tile borders in rendering"
description = '''The &quot;white pixel&quot; effect on fragments&#x27; common borders, like on the tile borders of forests, is clearly visible in some of the front page layers like here: http://osm.org/go/cLhOhw8?layers=H . These horizontal/vertical light stripes were visible in all layers until some weeks ago. Just lately, these ...'''
date = "2016-12-09T08:30:00Z"
lastmod = "2016-12-09T08:36:00Z"
weight = 53430
keywords = [ "rendering", "fragmentation", "stripes" ]
aliases = [ "/questions/53430" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Visible tile borders in rendering](/questions/53430/visible-tile-borders-in-rendering)

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
<span id="post-53430-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53430-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-53430-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>The "white pixel" effect on fragments' common borders, like on the tile borders of forests, is clearly visible in some of the front page layers like here: <a href="http://osm.org/go/cLhOhw8?layers=H">http://osm.org/go/cLhOhw8?layers=H</a> . These horizontal/vertical light stripes were visible in all layers until some weeks ago. Just lately, these stripes have disappeared in some of them like in the standard layer.<br />
So, my question is - are these changes caused by changes in the corresponding rendering model or by changes (defragmentation) in the source data?<br />
Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-fragmentation" rel="tag" title="see questions tagged &#39;fragmentation&#39;">fragmentation</span> <span class="post-tag tag-link-stripes" rel="tag" title="see questions tagged &#39;stripes&#39;">stripes</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Dec '16, 08:30</strong></p>
<img src="https://secure.gravatar.com/avatar/03cd9ea0efd97a7040fda0d6a76aba8e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sanser&#39;s gravatar image" />
<p><span>sanser</span><br />
<span class="score" title="695 reputation points">695</span><span title="38 badges"><span class="badge1">●</span><span class="badgecount">38</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="55 badges"><span class="bronze">●</span><span class="badgecount">55</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sanser has 2 accepted answers">5%</span> </br></br></p>
</div>
</div>
<div id="comments-container-53430" class="comments-container">
&#10;</div>
<div id="comment-tools-53430" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53430-form-container" class="comment-form-container">
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

<span id="53431"></span>

<div id="answer-container-53431" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53431-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53431-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-53431-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="sanser has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Normally we would not have tile borders in OSM - our data model is not tile based. Normally we would expect that someone who imports data from another source takes care to prepare the data to match OSM standards. However, CanVec importers have often done sloppy work and favoured speed and quantity of data over quality, hence the "tiled" woods in OSM (e.g. <a href="https://www.openstreetmap.org/relation/1504239">https://www.openstreetmap.org/relation/1504239</a> from your example).</p>
<p>It is possible to write your map style in a way to gloss over these problems by applying a suitable gamma value to the "Polygon Symbolizer". It is possible that changes to this gamma value are responsible for the change you say you've observed.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Dec '16, 08:36</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-53431" class="comments-container">
&#10;</div>
<div id="comment-tools-53431" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53431-form-container" class="comment-form-container">
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


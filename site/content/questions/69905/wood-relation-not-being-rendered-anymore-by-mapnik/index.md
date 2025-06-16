+++
type = "question"
title = "Wood relation not being rendered anymore by mapnik"
description = '''Please have a look at this:   You see the big white space north and west of 秋田市. This used to be wood and as far as I remember it was correctly rendered yesterday/the day before yesterday. I checked in JOSM, and the wood relation seems to look fine:  Any idea how this happened and how to fix this? I...'''
date = "2019-07-06T12:20:00Z"
lastmod = "2019-07-07T02:46:00Z"
weight = 69905
keywords = [ "rendering", "wood", "relation" ]
aliases = [ "/questions/69905" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Wood relation not being rendered anymore by mapnik](/questions/69905/wood-relation-not-being-rendered-anymore-by-mapnik)

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
<span id="post-69905-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69905-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69905-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Please have a look at <a href="https://www.openstreetmap.org/#map=10/39.8170/140.2508">this</a>: <img src="/upfiles/Screenshot_20190706_200402.png" alt="Mapnik ScreenShot" /></p>
<p>You see the big white space north and west of 秋田市. This used to be wood and as far as I remember it was correctly rendered yesterday/the day before yesterday. I checked in JOSM, and the wood relation seems to look fine: <img src="/upfiles/Screenshot_20190706_200656.png" alt="JSOM ScreenShot" /></p>
<p>Any idea how this happened and how to fix this? I looked through a lot of changesets, but I couldn't find anything matching (maybe <a href="https://www.openstreetmap.org/changeset/71320028#map=6/40.631/137.889">this</a>, but probably not). If you can't have a look at the data but have some hints I'd be grateful too.</p>
<p>(If you know a method how to properly search and display changesets it would be a big help too (I am using the history feature of osm.org which is quite inconvenient + changeset_viewer plugin of josm))</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-wood" rel="tag" title="see questions tagged &#39;wood&#39;">wood</span> <span class="post-tag tag-link-relation" rel="tag" title="see questions tagged &#39;relation&#39;">relation</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Jul '19, 12:20</strong></p>
<img src="https://secure.gravatar.com/avatar/96fe4c65bebc5588e414480fea6315ac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bkn_jap&#39;s gravatar image" />
<p><span>bkn_jap</span><br />
<span class="score" title="81 reputation points">81</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bkn_jap has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Jul '19, 12:20</strong> </span></p>
</div>
</div>
<div id="comments-container-69905" class="comments-container">
&#10;</div>
<div id="comment-tools-69905" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69905-form-container" class="comment-form-container">
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

<span id="69906"></span>

<div id="answer-container-69906" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69906-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69906-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-69906-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="bkn_jap has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I believe we're talking about <a href="https://www.openstreetmap.org/relation/5200043">relation 5200043</a>?</p>
<p>JOSM's validator did highlight a geometry error: <a href="https://www.openstreetmap.org/way/90648007">This inner way</a> is intersecting the outer boundary of the multipolygon. The intersection seems to have been introduced as part of <a href="https://www.openstreetmap.org/changeset/71024940">changeset 71024940</a> (<a href="https://osmcha.mapbox.com/changesets/71024940/">osmcha</a>). I'm not sure if this is actually the issue causing it not to be rendered, the change happened almost a month ago. It's worth correcting in any case.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Jul '19, 14:38</strong></p>
<img src="https://secure.gravatar.com/avatar/0626be5f46f32fce501353e8a5ec399c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tordanik&#39;s gravatar image" />
<p><span>Tordanik</span><br />
<span class="score" title="11998 reputation points"><span>12.0k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="106 badges"><span class="silver">●</span><span class="badgecount">106</span></span><span title="147 badges"><span class="bronze">●</span><span class="badgecount">147</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tordanik has 58 accepted answers">35%</span></p>
</img>
</div>
</div>
<div id="comments-container-69906" class="comments-container">
<span id="69912"></span>
<div id="comment-69912" class="comment">
<div id="post-69912-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thank you, I fixed the issue and it's starting to render correctly (at least at high zoom levels for now).</p>
</div>
<div id="comment-69912-info" class="comment-info">
<span class="comment-age">(07 Jul '19, 02:46)</span> <span class="comment-user userinfo">bkn_jap</span>
</div>
</div>
</div>
<div id="comment-tools-69906" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69906-form-container" class="comment-form-container">
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


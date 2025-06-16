+++
type = "question"
title = "Newbie: 3rd zoom level rendering issue after edit"
description = '''Hi, newbie here, I read all the stuff before making edits. In the 3rd most zoomed in level only, a select few of the ways I edited are displaying back broken in the view tab. Looks like I&#x27;m getting some pre-edit tiles mixed in with post edit tiles. This only appears in the 3rd zoom level all higher ...'''
date = "2011-01-04T02:25:00Z"
lastmod = "2011-01-04T07:31:00Z"
weight = 1999
keywords = [ "tiles", "concurrency", "render" ]
aliases = [ "/questions/1999" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Newbie: 3rd zoom level rendering issue after edit](/questions/1999/newbie-3rd-zoom-level-rendering-issue-after-edit)

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
<span id="post-1999-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1999-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-1999-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, newbie here, I read all the stuff before making edits. In the 3rd most zoomed in level only, a select few of the ways I edited are displaying back broken in the view tab. Looks like I'm getting some pre-edit tiles mixed in with post edit tiles. This only appears in the 3rd zoom level all higher and lower resolution zooms render correctly. Also on the edit tab, potlatch 1 and 2 both render correctly in <strong>all</strong> zoom levels including the 3rd. I do not notice this phenom anywhere else outside of the bounding box of my edits.</p>
<p>The fact that it displays correctly in higher resolution would seem to rule out data problems. Is this an artifact of batch update in progress? Or did a batch update fail?</p>
<p>My edits have time stamps in the history tab whereas they remained "still editing" for a while. Still the same observation. Just thought I'd provide that tidbit if it helps explain any timing issues.</p>
<p>In case it helps my changesets are: <a href="https://www.openstreetmap.org/browse/changeset/6856207">https://www.openstreetmap.org/browse/changeset/6856207</a> and <a href="https://www.openstreetmap.org/browse/changeset/6856085">https://www.openstreetmap.org/browse/changeset/6856085</a></p>
<p>Also these updates ran in a superset of my bounding box: <a href="https://www.openstreetmap.org/browse/changeset/6853644">https://www.openstreetmap.org/browse/changeset/6853644</a> and <a href="https://www.openstreetmap.org/browse/changeset/6856059">https://www.openstreetmap.org/browse/changeset/6856059</a> while I was in the process of editing. How does OSM handle locking and concurrent edits? Normally, one would get a "data updated by another user" error in a typical database transaction. If this is the issue will the tiles get re-rendered automatically? Or does it require a manual fix?</p>
<p>The edits were made in potlatch 1.</p>
<p>In potlatch 2 when I select osmarender for the background the whole background shows all pre-edit tiles not the mixture as sene in the view tab.</p>
<p>That's about all the data I have to offer. Can anyone explain this observation?</p>
<p>Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-concurrency" rel="tag" title="see questions tagged &#39;concurrency&#39;">concurrency</span> <span class="post-tag tag-link-render" rel="tag" title="see questions tagged &#39;render&#39;">render</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Jan '11, 02:25</strong></p>
<img src="https://secure.gravatar.com/avatar/c589579dfc9ad34fd9681fd9c8ad2822?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ducnbyu&#39;s gravatar image" />
<p><span>ducnbyu</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ducnbyu has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-1999" class="comments-container">
&#10;</div>
<div id="comment-tools-1999" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1999-form-container" class="comment-form-container">
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

<span id="2000"></span>

<div id="answer-container-2000" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-2000-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2000-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-2000-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Different zoom levels may render at different times. It is possible that your updates have appeared at one zoom level, but they have not been rendered for other zoom levels yet. (Alternatively it could be simply that your PC is caching the old tiles - clicking the permalink link, and then clicking refresh in your browser may fix this.)</p>
<p>Mapnik and Osmarender do rendering slightly differently. See <a href="https://wiki.openstreetmap.org/wiki/Slippy_Map#Tile_rendering">this page in the Wiki</a> for more information.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Jan '11, 05:22</strong></p>
<img src="https://secure.gravatar.com/avatar/f075add936ab95d2d368f2e48f5ddc22?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ebenezer&#39;s gravatar image" />
<p><span>Ebenezer</span><br />
<span class="score" title="948 reputation points">948</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ebenezer has 2 accepted answers">9%</span></p>
</div>
</div>
<div id="comments-container-2000" class="comments-container">
<span id="2005"></span>
<div id="comment-2005" class="comment">
<div id="post-2005-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks E! It looks like it was a combination of both scenarios you described. I had waited about 30 minutes for it to update that zoom level and got impatient and viewed the same inconsistency in IE (was originally working in firefox). So at that time it was probably a zoom level update timing issue and not a caching issue. But my display finally got corrected once I performed your permalink suggestion just now. So at some point it became just a caching issue.</p>
<p>I will keep that in mind in the future.</p>
<p>Again, thanks!</p>
</div>
<div id="comment-2005-info" class="comment-info">
<span class="comment-age">(04 Jan '11, 07:26)</span> <span class="comment-user userinfo">ducnbyu</span>
</div>
</div>
<span id="2008"></span>
<div id="comment-2008" class="comment">
<div id="post-2008-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If the reply answered your question please mark it as "accepted" to close the question. This removes it from the pool of "unanswered questions" that still need an answer. Thank you.</p>
</div>
<div id="comment-2008-info" class="comment-info">
<span class="comment-age">(04 Jan '11, 07:31)</span> <span class="comment-user userinfo">petschge</span>
</div>
</div>
</div>
<div id="comment-tools-2000" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2000-form-container" class="comment-form-container">
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


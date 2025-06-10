+++
type = "question"
title = "Water on aqueduct not rendered in Mapnik"
description = '''The Pont-canal du Sart http://www.openstreetmap.org/#map=18/50.49353/4.13718 is a wide bridge for ships travelling the Belgian Canal du Centre.  The waterway object alone is rendered only very narrow (the width tag is being ignored) and it would not include the cycleways on both sides, hence I&#x27;ve ad...'''
date = "2017-01-26T18:39:00Z"
lastmod = "2017-01-27T13:45:00Z"
weight = 54315
keywords = [ "aqueduct" ]
aliases = [ "/questions/54315" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Water on aqueduct not rendered in Mapnik](/questions/54315/water-on-aqueduct-not-rendered-in-mapnik)

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
<span id="post-54315-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54315-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-54315-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>The Pont-canal du Sart <a href="http://www.openstreetmap.org/#map=18/50.49353/4.13718">http://www.openstreetmap.org/#map=18/50.49353/4.13718</a> is a wide bridge for ships travelling the Belgian Canal du Centre.</p>
<p>The waterway object alone is rendered only very narrow (the width tag is being ignored) and it would not include the cycleways on both sides, hence I've added an area tagged man_made=bridge and layer=1, and there's a (smaller) natural=water area covering the canal surface, also tagged with layer=1 because this is recommended for objects ans ways on the bridge.</p>
<p>However, Mapnik would not render the water area, even not when I make its layer=2.</p>
<p>What should I do? Change the tagging? I think it is correct as it is, and I actually do not fancy adopting tagging to compensate for flaws in rendering. So if no one has an idea how to change tags in a senseful and correct way I would like to leave it as it is.</p>
<p>Can Mapnik be changed? Can I submit a bug report somewhere?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-aqueduct" rel="tag" title="see questions tagged &#39;aqueduct&#39;">aqueduct</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Jan '17, 18:39</strong></p>
<img src="https://secure.gravatar.com/avatar/5f5d99b38973b2f5f0a322f6695ff1d8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DerGuteDiktator&#39;s gravatar image" />
<p><span>DerGuteDiktator</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DerGuteDiktator has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-54315" class="comments-container">
&#10;</div>
<div id="comment-tools-54315" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54315-form-container" class="comment-form-container">
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

<span id="54322"></span>

<div id="answer-container-54322" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-54322-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54322-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-54322-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hallo,</p>
<p>you should never change the tagging to obtain a particular result in 1 renderer, see <a href="https://wiki.openstreetmap.org/wiki/Tagging_for_the_renderer">Tagging for the Renderer</a></p>
<p>You can log a bug report for the default carto-css style on <a href="https://github.com/gravitystorm/openstreetmap-carto">their github page</a>.</p>
<p>Note that they (the carto-css developers) use Mapnik as a technology, so the problem you see in in the use of the technology, not in the technology itself. With Mapnik you can make many different maps, a few can be found on osm.org, but many more exist.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Jan '17, 06:17</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Jan '17, 13:45</strong> </span></p>
</div>
</div>
<div id="comments-container-54322" class="comments-container">
<span id="54326"></span>
<div id="comment-54326" class="comment">
<div id="post-54326-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks, I said that I'd only change the tags if there would be an alternative that is inherently just as correct, not tag it wrong just to fit the rendering result.</p>
<p>I didn't know that this is only due to the style and not of Mapnik, though, so thanks for the explanation!</p>
<p>You have posted the same link twice, albeit with different labels. Do you mean this page? <a href="https://github.com/mapbox/carto/issues">https://github.com/mapbox/carto/issues</a></p>
</div>
<div id="comment-54326-info" class="comment-info">
<span class="comment-age">(27 Jan '17, 10:20)</span> <span class="comment-user userinfo">DerGuteDiktator</span>
</div>
</div>
<span id="54333"></span>
<div id="comment-54333" class="comment">
<div id="post-54333-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>No, that's yet another style. I've updated the link above. It's under "gravitystorm"</p>
</div>
<div id="comment-54333-info" class="comment-info">
<span class="comment-age">(27 Jan '17, 13:44)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="54334"></span>
<div id="comment-54334" class="comment">
<div id="post-54334-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>it won't update, the github link is <a href="https://github.com/gravitystorm/openstreetmap-carto">https://github.com/gravitystorm/openstreetmap-carto</a></p>
</div>
<div id="comment-54334-info" class="comment-info">
<span class="comment-age">(27 Jan '17, 13:45)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
</div>
<div id="comment-tools-54322" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54322-form-container" class="comment-form-container">
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


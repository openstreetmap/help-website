+++
type = "question"
title = "Can I tag ridges or aretes by sac_sacle?"
description = '''Many ridges, aretes and spurs are part of a hiking path to summit. To define difficulty level of a hiking trail, we must duplicate a way tagged natural=ridge; tag it with highway=path; and then add sac_scale. It does not seem reasonable. Is there any idea about adding sac_scale=* to natural=ridge or...'''
date = "2019-05-07T11:16:00Z"
lastmod = "2019-05-08T11:01:00Z"
weight = 69110
keywords = [ "sac_scale", "arete", "ridge", "hiking", "path" ]
aliases = [ "/questions/69110" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Can I tag ridges or aretes by sac_sacle?](/questions/69110/can-i-tag-ridges-or-aretes-by-sac_sacle)

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
<span id="post-69110-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69110-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69110-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Many ridges, aretes and spurs are part of a hiking path to summit. To define difficulty level of a hiking trail, we must duplicate a way tagged natural=ridge; tag it with highway=path; and then add sac_scale. It does not seem reasonable.</p>
<p>Is there any idea about adding sac_scale=* to natural=ridge or natural=arete directly? It seems more reasonable.</p>
<p>And is there any software to render such kind of tagging.</p>
<p>Besides, the question may be extended. Bikers can ask: "Can we add mbt:scale to ridges and aretes?"</p>
<p>What is your idea?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-sac_scale" rel="tag" title="see questions tagged &#39;sac_scale&#39;">sac_scale</span> <span class="post-tag tag-link-arete" rel="tag" title="see questions tagged &#39;arete&#39;">arete</span> <span class="post-tag tag-link-ridge" rel="tag" title="see questions tagged &#39;ridge&#39;">ridge</span> <span class="post-tag tag-link-hiking" rel="tag" title="see questions tagged &#39;hiking&#39;">hiking</span> <span class="post-tag tag-link-path" rel="tag" title="see questions tagged &#39;path&#39;">path</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 May '19, 11:16</strong></p>
<img src="https://secure.gravatar.com/avatar/5d959c47b6dc607657535cbe74aa8c2d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="babri&#39;s gravatar image" />
<p><span>babri</span><br />
<span class="score" title="66 reputation points">66</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="babri has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-69110" class="comments-container">
&#10;</div>
<div id="comment-tools-69110" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69110-form-container" class="comment-form-container">
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

<span id="69112"></span>

<div id="answer-container-69112" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69112-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69112-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-69112-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="babri has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>A ridge or an arete is a geographical feature. Period. We tag it with natural=ridge to show the distinct feature on a map and give it a name.</p>
<p>A path is something completely different. In OSM we abstract from the physical feature (beaten path to motorway) by drawing a line at the centerline. It's done to show where to walk/ride/drive/etc and again give it a name. A path may follow a ridge or it may not. It may also be in the slope a couple of meters below the ridge line.</p>
<p>Paths are also interconnected. You want to be able to find a continuous route from a village in the valley to the next summit for example. So the path following the ridge needs to be connected to the streets in the village and the path on the summit. That's why we need to duplicate the line. How would I know the ridge is supposed to be hiked along if it's not tagged as a path? You want to show how difficult it is to hike there? So put sac scale on the path, because it is a measure of how well the path can be followed not a measure of how steep or rough the ridge is (even if they are related).</p>
<p>The ridge and the path could also both have distinct names that we couldn't tag if we re-used the same way.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 May '19, 15:15</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-69112" class="comments-container">
<span id="69115"></span>
<div id="comment-69115" class="comment">
<div id="post-69115-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It's also unlikely that the path/route absolutely follows the ridge line, but rather weaves close to it to bypass harder parts. Even when it does this is likely for only short sections.</p>
</div>
<div id="comment-69115-info" class="comment-info">
<span class="comment-age">(07 May '19, 19:19)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="69116"></span>
<div id="comment-69116" class="comment">
<div id="post-69116-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I understand all you well noted and agree.</p>
<p>I'm just thinking that where there is no trail on the ridge and the path is the ridge itself, why we do not reduce the work and optimise the database volume and define the way once for both ridge and the path.</p>
<p>If we start applying sac scale to ridges, it is easy for renderers to identify sac-scaled ridges as hiking path and include them in ways for addressing. And the name of the path, where it matches the ridge, is often the name of the ridge.</p>
</div>
<div id="comment-69116-info" class="comment-info">
<span class="comment-age">(07 May '19, 19:23)</span> <span class="comment-user userinfo">babri</span>
</div>
</div>
<span id="69117"></span>
<div id="comment-69117" class="comment">
<div id="post-69117-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>It's not as if we could not spare a couple of more bytes in the database for an additional way. The benefits of having two way clearly outweigh the advantages of only one way. It's more easy to maintain, easier to understand by human as well as machine, you can have different names etc. We try to have one OSM object per feature. When you write "where there is no trail on the ridge and the path is the ridge itself", you contradict yourself. Either there is no path or there is. It may not be clearly visible, it may not be marked, it may not be popular but if there is evidence that it is walked s add a highway=path by all mean.</p>
</div>
<div id="comment-69117-info" class="comment-info">
<span class="comment-age">(07 May '19, 20:29)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="69125"></span>
<div id="comment-69125" class="comment">
<div id="post-69125-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/13210/babri">@babri</a>: I'd be fine with both tags on the same way, but as an INTERIM step, where the actual path/route &amp; the ridge gets refined later. An alternative way is to just to create a second way sharing the nodes of the ridge way for the path. This latter approach is closer to what <a href="https://help.openstreetmap.org/users/10133/tzorn">@TZorn</a> is advocating. (For instance, I've often mapped ridges in out of the way places because having the ridge pattern really assists interpreting the landscape, but no-one seems to render them now).</p>
</div>
<div id="comment-69125-info" class="comment-info">
<span class="comment-age">(08 May '19, 11:01)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-69112" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69112-form-container" class="comment-form-container">
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


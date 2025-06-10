+++
type = "question"
title = "Nominatim is returning wrong informations"
description = '''For that particular query : https://nominatim.openstreetmap.org/details.php?place_id=4103949 I&#x27;m trying why it wrongly returns things like L&#x27;Île d&#x27;Amour (Type: place:hamlet, node 2998389259, 15, 0.0222670563894245 GOTO) which is few kilometers away. '''
date = "2015-01-23T09:32:00Z"
lastmod = "2015-01-24T12:48:00Z"
weight = 40551
keywords = [ "nominatim" ]
aliases = [ "/questions/40551" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Nominatim is returning wrong informations](/questions/40551/nominatim-is-returning-wrong-informations)

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
<span id="post-40551-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40551-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-40551-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>For that particular query : <a href="https://nominatim.openstreetmap.org/details.php?place_id=4103949">https://nominatim.openstreetmap.org/details.php?place_id=4103949</a></p>
<p>I'm trying why it wrongly returns things like <em>L'Île d'Amour (Type: place:hamlet, node 2998389259, 15, 0.0222670563894245 GOTO)</em> which is few kilometers away.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Jan '15, 09:32</strong></p>
<img src="https://secure.gravatar.com/avatar/e48f202fc43dcc628a45c41463d25c20?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kyro&#39;s gravatar image" />
<p><span>Kyro</span><br />
<span class="score" title="121 reputation points">121</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kyro has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-40551" class="comments-container">
&#10;</div>
<div id="comment-tools-40551" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40551-form-container" class="comment-form-container">
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

<span id="40559"></span>

<div id="answer-container-40559" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-40559-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40559-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-40559-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>When there are no boundary relations at that level, Nominatim searches for the nearest place node. AFAIK the best solution is to have a complete set of boundary relations on each admin level.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Jan '15, 12:25</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-40559" class="comments-container">
<span id="40560"></span>
<div id="comment-40560" class="comment">
<div id="post-40560-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I would query why a location within a city is mapped as place=hamlet. I was aware of this usage (probably based on population figures) in the US, but more usually in Europe hamlet is reserved for small groups of houses in the countryside, perhaps with a church, but usually without other facilities.</p>
</div>
<div id="comment-40560-info" class="comment-info">
<span class="comment-age">(23 Jan '15, 12:32)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="40570"></span>
<div id="comment-40570" class="comment">
<div id="post-40570-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Could it be that the problem is that the point is on a boarder between 2 cities ?</p>
</div>
<div id="comment-40570-info" class="comment-info">
<span class="comment-age">(23 Jan '15, 17:27)</span> <span class="comment-user userinfo">Kyro</span>
</div>
</div>
<span id="40574"></span>
<div id="comment-40574" class="comment">
<div id="post-40574-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Maybe the real "Hamlet" is not mapped (yet), or maybe the other Hamlet's node is closer than the real one. Nominatim cannot know the difference without a boundary around the Hamlet's node.</p>
</div>
<div id="comment-40574-info" class="comment-info">
<span class="comment-age">(23 Jan '15, 22:49)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="40575"></span>
<div id="comment-40575" class="comment">
<div id="post-40575-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Kyro has since changed the L'Île d'Amour node from hamlet to locality, so it no longer shows up in the above Nominatim query. This may be "tagging for the renderer", though, because it looks like it's a populated place and locality might be the wrong tag. Maybe "neighbourhood" would be better?</p>
</div>
<div id="comment-40575-info" class="comment-info">
<span class="comment-age">(24 Jan '15, 00:36)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="40577"></span>
<div id="comment-40577" class="comment">
<div id="post-40577-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yeah, agree with neighbourhood, certainly wouldn't map it as hamlet or locality.</p>
</div>
<div id="comment-40577-info" class="comment-info">
<span class="comment-age">(24 Jan '15, 12:48)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-40559" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40559-form-container" class="comment-form-container">
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


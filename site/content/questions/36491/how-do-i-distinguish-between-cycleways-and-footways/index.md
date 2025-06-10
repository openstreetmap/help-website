+++
type = "question"
title = "How do I distinguish between cycleways and footways?"
description = '''I am having a hard time determining whether to use cycleway or footway in some situations. My area has cycling paths that run parallel to the road, as you can see in the image. They are for both pedestrians and cyclists, and are sidewalks as well. Would I tag that as highway=footway and footway=side...'''
date = "2014-09-02T03:39:00Z"
lastmod = "2014-09-02T16:30:00Z"
weight = 36491
keywords = [ "tagging", "sidewalks", "road", "footway", "cycleway" ]
aliases = [ "/questions/36491" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [How do I distinguish between cycleways and footways?](/questions/36491/how-do-i-distinguish-between-cycleways-and-footways)

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
<span id="post-36491-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36491-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-36491-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am having a hard time determining whether to use cycleway or footway in some situations. My area has cycling paths that run parallel to the road, as you can see in the image. They are for both pedestrians and cyclists, and are sidewalks as well. Would I tag that as highway=footway and footway=sidewalk? Or, would it be better to just add a sidewalk tag to the road, even though these are wider and higher quality than the average sidewalk, as well as uncommon in this area? Right now they are tagged as highway=cycleway and foot=designated.</p>
<p><img src="http://i.snag.gy/Z4Wqp.jpg" alt="alt text" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-sidewalks" rel="tag" title="see questions tagged &#39;sidewalks&#39;">sidewalks</span> <span class="post-tag tag-link-road" rel="tag" title="see questions tagged &#39;road&#39;">road</span> <span class="post-tag tag-link-footway" rel="tag" title="see questions tagged &#39;footway&#39;">footway</span> <span class="post-tag tag-link-cycleway" rel="tag" title="see questions tagged &#39;cycleway&#39;">cycleway</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Sep '14, 03:39</strong></p>
<img src="https://secure.gravatar.com/avatar/eb91b1e453fe246b3781c55172f92df3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iansan5653&#39;s gravatar image" />
<p><span>iansan5653</span><br />
<span class="score" title="191 reputation points">191</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iansan5653 has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-36491" class="comments-container">
&#10;</div>
<div id="comment-tools-36491" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-36491-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="36495"></span>

<div id="answer-container-36495" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-36495-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36495-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-36495-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="iansan5653 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This tends to be a reoccuring hotly debated topic not the least because the legal situation as escada writes tends to be different from country to country.</p>
<p>If bicycles are a simply allowed on a way that normally would be closed to them:</p>
<p>bicycle=yes</p>
<p>just the same if pedestrians would normally not be allowed to use a way</p>
<p>foot=yes</p>
<p>While some what disputed: *=designated IMHO indicates that the way in question is at least intended for the mode of transport (in many countries not just intended it may be legally mandatory and may exclude other means of transport). So a dual purpose cycleway or footway can be tagged either as:</p>
<p>highway=cycleway foot=designated</p>
<p>or (with the same implications from a pratical point of view, but different renderings on the default map style)</p>
<p>highway=footway bicycle=designated</p>
<p>Please add a segregated=no or yes if there is some kind of clear division between the areas on the way that are used for the mode of transport. Further if the way is clearly a sidewalk, a footway=sidewalk would be helpful.</p>
<p>Note: mainly in Germany the value "official" is used to indicate a way that is mandatory to use for the mode of transport. It however tries to model a distinction between mandatory and non-mandatory use that IMHO doesn't really legally exist in Germany.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Sep '14, 09:40</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Sep '14, 09:45</strong> </span></p>
</div>
</div>
<div id="comments-container-36495" class="comments-container">
&#10;</div>
<div id="comment-tools-36495" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-36495-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="36493"></span>

<div id="answer-container-36493" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-36493-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36493-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-36493-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think the rule (in BE, NL, DE) to determine whether something is a cycleway is that there is a traffic sign. (blue circle, white bicycle). In some countries (e.g. Belgium) pedestrians are allowed on cycleways (this is not the case in Germany), even when this is not explicitly stated. So foot=yes (or foot=designated) could be added in such case.</p>
<p>If there is no traffic sign I map it as highway=path (with foot=yes, bicycle=yes).</p>
<p>Depending on the country, you might also have to add bicycle=use_sidepath (or no) on the main road.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Sep '14, 08:13</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-36493" class="comments-container">
&#10;</div>
<div id="comment-tools-36493" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-36493-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="36515"></span>

<div id="answer-container-36515" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-36515-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36515-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-36515-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The sidewalk is obviously a footway, being primarily for the use of pedestrians (and in the US, depending on what part and where, either between discouraged and illegal for bicycles to use). The other path running perpendicular would be a path (being of mixed use and not bearing the pavement markings typical of a way primarily intended for cyclists).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Sep '14, 16:30</strong></p>
<img src="https://secure.gravatar.com/avatar/666698a7b13e402aba7e1e0f6de7c1d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Baloo%20Uriza&#39;s gravatar image" />
<p><span>Baloo Uriza</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="61 badges"><span class="bronze">●</span><span class="badgecount">61</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Baloo Uriza has 12 accepted answers">9%</span></p>
</div>
</div>
<div id="comments-container-36515" class="comments-container">
&#10;</div>
<div id="comment-tools-36515" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-36515-form-container" class="comment-form-container">
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


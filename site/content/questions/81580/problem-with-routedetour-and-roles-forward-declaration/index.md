+++
type = "question"
title = "Problem with route=detour and roles forward declaration"
description = '''I have a relation with route=detour and type=route. In the relation are several segments with &quot;forward&quot; declaration.  When doing a validation JOSM marks all these with a warning: Role &quot;forward&quot; is not among expected values. If change the route to &quot;road&quot; or delete the forward&#x27;s warnings disappear Is ...'''
date = "2021-08-31T15:50:00Z"
lastmod = "2021-08-31T18:52:00Z"
weight = 81580
keywords = [ "josm" ]
aliases = [ "/questions/81580" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Problem with route=detour and roles forward declaration](/questions/81580/problem-with-routedetour-and-roles-forward-declaration)

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
<span id="post-81580-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81580-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81580-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a relation with route=detour and type=route.</p>
<p>In the relation are several segments with "forward" declaration. When doing a validation JOSM marks all these with a warning: Role "forward" is not among expected values. If change the route to "road" or delete the forward's warnings disappear</p>
<p>Is this a bug?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Aug '21, 15:50</strong></p>
<img src="https://secure.gravatar.com/avatar/7fbbe44e24bdb695025fddb0879817a5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Msiipola&#39;s gravatar image" />
<p><span>Msiipola</span><br />
<span class="score" title="227 reputation points">227</span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="18 badges"><span class="silver">●</span><span class="badgecount">18</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Msiipola has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-81580" class="comments-container">
&#10;</div>
<div id="comment-tools-81580" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81580-form-container" class="comment-form-container">
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

<span id="81584"></span>

<div id="answer-container-81584" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81584-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81584-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-81584-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Msiipola has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The wiki article for <a href="https://wiki.openstreetmap.org/wiki/Tag:route%3Ddetour">route=detour</a> is a bit light on information and doesn't specify any role types. The JOSM validator is probably basing its response on that premise.</p>
<p>That being said, I don't see why you shouldn't use "forward" or "backward" roles if the detour is only in one direction. Those roles are often used on road, public transport, and other route relations to indicate a single direction, so it would make sense to use them for detours too.</p>
<p>I'd say you could just ignore the warnings, and maybe report it to the JOSM maintainers to see if they'll update the validator.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Aug '21, 16:51</strong></p>
<img src="https://secure.gravatar.com/avatar/087bb38ba920baadf1df9dfc473208ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alester&#39;s gravatar image" />
<p><span>alester</span><br />
<span class="score" title="6631 reputation points"><span>6.6k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alester has 37 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-81584" class="comments-container">
<span id="81590"></span>
<div id="comment-81590" class="comment">
<div id="post-81590-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your response! I think it's bug in the validator, and I will ignore the warning. But it's always nice to have clean validation without any warnings (and errors).</p>
</div>
<div id="comment-81590-info" class="comment-info">
<span class="comment-age">(31 Aug '21, 18:52)</span> <span class="comment-user userinfo">Msiipola</span>
</div>
</div>
</div>
<div id="comment-tools-81584" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81584-form-container" class="comment-form-container">
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


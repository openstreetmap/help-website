+++
type = "question"
title = "water &amp; relations"
description = '''Two questions: 1) In working with the &#x27;natural=water&#x27; closed-way features is it recommended to enter them into a relation with a country? What should be done if the water body crosses a country/administrative border? http://wiki.openstreetmap.org/wiki/Tag:natural%3Dwater 2) Also...is there any way t...'''
date = "2017-04-24T23:51:00Z"
lastmod = "2017-04-26T07:20:00Z"
weight = 55838
keywords = [ "water", "waterway", "relations" ]
aliases = [ "/questions/55838" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [water & relations](/questions/55838/water-relations)

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
<span id="post-55838-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55838-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-55838-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Two questions:</p>
<p>1) In working with the 'natural=water' closed-way features is it recommended to enter them into a relation with a country? What should be done if the water body crosses a country/administrative border? <a href="http://wiki.openstreetmap.org/wiki/Tag:natural%3Dwater">http://wiki.openstreetmap.org/wiki/Tag:natural%3Dwater</a></p>
<p>2) Also...is there any way to get a sense of how many entries (and where they are) with the 'natural=water' tag have a relation (I've looked at taginfo...here...but I'm the map distribution is not insightful on where the relation items are). <a href="http://wiki.openstreetmap.org/wiki/Tag:natural%3Dwater">http://wiki.openstreetmap.org/wiki/Tag:natural%3Dwater</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-water" rel="tag" title="see questions tagged &#39;water&#39;">water</span> <span class="post-tag tag-link-waterway" rel="tag" title="see questions tagged &#39;waterway&#39;">waterway</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Apr '17, 23:51</strong></p>
<img src="https://secure.gravatar.com/avatar/d8301f4449cd62755a06bd46e11db349?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="goldfishinriver&#39;s gravatar image" />
<p><span>goldfishinriver</span><br />
<span class="score" title="31 reputation points">31</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="goldfishinriver has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-55838" class="comments-container">
<span id="55846"></span>
<div id="comment-55846" class="comment">
<div id="post-55846-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Why do you want to add them to a relation? What benefits do you expect?</p>
</div>
<div id="comment-55846-info" class="comment-info">
<span class="comment-age">(25 Apr '17, 08:01)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-55838" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55838-form-container" class="comment-form-container">
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

<span id="55872"></span>

<div id="answer-container-55872" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55872-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55872-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-55872-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You should not enter any object into relation with a country. We do not add streets, houses, monuments or any other feature in a relation with a country. The fact that a feature is located in a country follows from its position.</p>
<p>A geocoder "sees" where the feature is placed and if that falls within the border of an administrative unit (e.g. city or country), it is "in" that unit. It can also solve lakes that belong to multiple units, although that is not noticeable from e.g. Lac Leman <a href="http://nominatim.openstreetmap.org/details.php?place_id=158973136">http://nominatim.openstreetmap.org/details.php?place_id=158973136</a> But that is an implementation detail / choice made by the developers of nominatim. They only show the "first" item at each administrative level they find.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Apr '17, 07:20</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Apr '17, 07:21</strong> </span></p>
</div>
</div>
<div id="comments-container-55872" class="comments-container">
&#10;</div>
<div id="comment-tools-55872" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55872-form-container" class="comment-form-container">
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


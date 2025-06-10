+++
type = "question"
title = "City street appearing under wrong Neighborhood"
description = '''I investigated a street not appearing under the streets of its city but appearing under a different neighborhood elevated as city. I use a Garmin gpsmap 64s with openstreetmaps and I couldn&#x27;t find this street, the street name is &quot;Viale della Navigazione Interna&quot; and its city should be &quot;Padova / Padu...'''
date = "2015-02-24T13:20:00Z"
lastmod = "2015-02-25T08:07:00Z"
weight = 41314
keywords = [ "city", "neighborhood", "neighbourhood" ]
aliases = [ "/questions/41314" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [City street appearing under wrong Neighborhood](/questions/41314/city-street-appearing-under-wrong-neighborhood)

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
<span id="post-41314-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41314-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-41314-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I investigated a street not appearing under the streets of its city but appearing under a different neighborhood elevated as city.</p>
<p>I use a Garmin gpsmap 64s with openstreetmaps and I couldn't find this street, the street name is "Viale della Navigazione Interna" and its city should be "Padova / Padua" while instead it is put under "Ponte di Brenta" which is not a city but a neighborhood name (it has no mayor and is just under Padua).</p>
<p>How can i deal with that? Maybe making the street both belong to Padova and Ponte di brenta would be the best solution, but for sure no one will ever think of searching it unser Ponte di Brenta!</p>
<p>A practicle example of the problem with the nominatim api:</p>
<p><a href="http://nominatim.openstreetmap.org/reverse?format=xml&amp;lat=45.4081595&amp;lon=11.9362149&amp;zoom=18&amp;addressdetails=1">http://nominatim.openstreetmap.org/reverse?format=xml&amp;lat=45.4081595&amp;lon=11.9362149&amp;zoom=18&amp;addressdetails=1</a></p>
<p>it returns no city at all, just town and county</p>
<p><a href="http://nominatim.openstreetmap.org/reverse?format=xml&amp;lat=45.4086655&amp;lon=11.9335889&amp;zoom=18&amp;addressdetails=1">http://nominatim.openstreetmap.org/reverse?format=xml&amp;lat=45.4086655&amp;lon=11.9335889&amp;zoom=18&amp;addressdetails=1</a></p>
<p>it returns correctly the city as Padua and Suburb as "Ponte di Brenta"</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-city" rel="tag" title="see questions tagged &#39;city&#39;">city</span> <span class="post-tag tag-link-neighborhood" rel="tag" title="see questions tagged &#39;neighborhood&#39;">neighborhood</span> <span class="post-tag tag-link-neighbourhood" rel="tag" title="see questions tagged &#39;neighbourhood&#39;">neighbourhood</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Feb '15, 13:20</strong></p>
<img src="https://secure.gravatar.com/avatar/82522b775fb61328d267f5c082920dc8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cendonuser&#39;s gravatar image" />
<p><span>cendonuser</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cendonuser has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Feb '15, 13:54</strong> </span></p>
</div>
</div>
<div id="comments-container-41314" class="comments-container">
&#10;</div>
<div id="comment-tools-41314" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41314-form-container" class="comment-form-container">
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

<span id="41346"></span>

<div id="answer-container-41346" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-41346-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41346-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-41346-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This question has been asked in the past. The problem is that the boundary relations are not complete for all administrative levels. Then the software has to start guessing to which neighborhood or village or town a street belongs. This "guess" is done by calculating the distance to the nearest place point (e.g. village or town). Most of the time this works fine, but not always as in your case.</p>
<p>The best solution is to try to make all boundary relations complete. However, this often requires an import with all related problems and rules. Contact the Italian community to see whether they are in touch with the government to obtain those boundaries.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Feb '15, 08:07</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Feb '15, 08:07</strong> </span></p>
</div>
</div>
<div id="comments-container-41346" class="comments-container">
&#10;</div>
<div id="comment-tools-41346" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41346-form-container" class="comment-form-container">
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


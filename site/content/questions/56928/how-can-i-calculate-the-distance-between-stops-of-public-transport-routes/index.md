+++
type = "question"
title = "How can I calculate the distance between stops of public transport routes?"
description = '''Are there any tools where I can use to caclculate the route distance between stops of public transport routes mapped in OpenStreetMap?'''
date = "2017-07-07T10:26:00Z"
lastmod = "2017-07-07T19:30:00Z"
weight = 56928
keywords = [ "public_transport" ]
aliases = [ "/questions/56928" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How can I calculate the distance between stops of public transport routes?](/questions/56928/how-can-i-calculate-the-distance-between-stops-of-public-transport-routes)

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
<span id="post-56928-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56928-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-56928-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Are there any tools where I can use to caclculate the route distance between stops of public transport routes mapped in OpenStreetMap?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-public_transport" rel="tag" title="see questions tagged &#39;public_transport&#39;">public_transport</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Jul '17, 10:26</strong></p>
<img src="https://secure.gravatar.com/avatar/da5919ad47133ec03dbb7b0bca904688?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="miklcct&#39;s gravatar image" />
<p><span>miklcct</span><br />
<span class="score" title="71 reputation points">71</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="miklcct has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Jul '17, 19:19</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span></p>
</div>
</div>
<div id="comments-container-56928" class="comments-container">
&#10;</div>
<div id="comment-tools-56928" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56928-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="56931"></span>

<div id="answer-container-56931" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56931-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56931-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-56931-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For 1 or 2 you could do it in e.g. JOSM (or the upcoming update of the iD editor). In case you want it for several tens of bus stops, you can download OSM data in e.g. a Postgis database and do the calculations there. You can also download bus stops for a route via Overpass in a csv format and do the calculations in a spreadsheet.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Jul '17, 10:38</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Jul '17, 10:40</strong> </span></p>
</div>
</div>
<div id="comments-container-56931" class="comments-container">
&#10;</div>
<div id="comment-tools-56931" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56931-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="56951"></span>

<div id="answer-container-56951" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56951-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56951-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-56951-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><img src="/upfiles/distance_between_stops.JPG" alt="alt text" /></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Jul '17, 19:30</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</img>
</div>
</div>
<div id="comments-container-56951" class="comments-container">
&#10;</div>
<div id="comment-tools-56951" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56951-form-container" class="comment-form-container">
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


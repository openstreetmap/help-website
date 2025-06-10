+++
type = "question"
title = "I need help in integrating OpenStreetMap with codeignitor PHP"
description = '''This is my first time going to work with maps, so need some help. I am looking for API and API document which can guide me and help me how to integrate OpenStreetMap with Codeignitor PHP and have to place to place marker in the map. majority of the locations are in Dubai. I want to make it simple.'''
date = "2019-02-13T10:23:00Z"
lastmod = "2019-12-04T04:47:00Z"
weight = 67995
keywords = [ "marker", "php", "codeigniter" ]
aliases = [ "/questions/67995" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [I need help in integrating OpenStreetMap with codeignitor PHP](/questions/67995/i-need-help-in-integrating-openstreetmap-with-codeignitor-php)

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
<span id="post-67995-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67995-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-67995-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>This is my first time going to work with maps, so need some help. I am looking for API and API document which can guide me and help me how to integrate OpenStreetMap with Codeignitor PHP and have to place to place marker in the map. majority of the locations are in Dubai. I want to make it simple.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-marker" rel="tag" title="see questions tagged &#39;marker&#39;">marker</span> <span class="post-tag tag-link-php" rel="tag" title="see questions tagged &#39;php&#39;">php</span> <span class="post-tag tag-link-codeigniter" rel="tag" title="see questions tagged &#39;codeigniter&#39;">codeigniter</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Feb '19, 10:23</strong></p>
<img src="https://secure.gravatar.com/avatar/c11ec2b737c03c9ee6f546f8ec3834af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="osamaahmed32&#39;s gravatar image" />
<p><span>osamaahmed32</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="osamaahmed32 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-67995" class="comments-container">
&#10;</div>
<div id="comment-tools-67995" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67995-form-container" class="comment-form-container">
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

<span id="71980"></span>

<div id="answer-container-71980" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71980-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71980-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-71980-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The maps will typically be handled client-side, i.e. in JavaScript. This can be done e.g. in <a href="https://leafletjs.com/">Leaflet</a> or <a href="https://openlayers.org/">OpenLayers</a>. Your PHP code should serve an HTML page with either one of those libs. Your PHP code will also be responsible for returning the data required by those libs to display the data points.</p>
</div>
<div class="answer-controls post-controls">
<div class="community-wiki">
This answer is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Dec '19, 04:47</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-71980" class="comments-container">
&#10;</div>
<div id="comment-tools-71980" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71980-form-container" class="comment-form-container">
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


+++
type = "question"
title = "Show multiple areas and color them"
description = '''Hello,  I would know if It is possible shows multile area simultaneously (like Countries, Region, City,..) selected one time by name or ID like Nominatim shows. In instance I imagine a link like   https://www.openstreetmap.org/relation/45319_44915 that shows simultaneously  https://www.openstreetmap...'''
date = "2019-09-26T11:02:00Z"
lastmod = "2019-09-26T16:12:00Z"
weight = 70927
keywords = [ "coloed", "multiple", "areas" ]
aliases = [ "/questions/70927" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Show multiple areas and color them](/questions/70927/show-multiple-areas-and-color-them)

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
<span id="post-70927-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70927-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70927-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, I would know if It is possible shows multile area simultaneously (like Countries, Region, City,..) selected one time by name or ID like Nominatim shows.</p>
<p>In instance I imagine a link like <a href="https://www.openstreetmap.org/relation/45319_44915">https://www.openstreetmap.org/relation/45319_44915</a> that shows simultaneously <a href="https://www.openstreetmap.org/relation/45319">https://www.openstreetmap.org/relation/45319</a> (Monza, IT) city area and <a href="https://www.openstreetmap.org/relation/44915">https://www.openstreetmap.org/relation/44915</a> (Milan, IT) auto adapt the zoom and center in order to show all areas (in this sample they are 2, but could be dozens...)</p>
<p>And also, I will pass other parameter (the area color) like <a href="https://www.openstreetmap.org/relation/45319_44915#FF0000_00FF00">https://www.openstreetmap.org/relation/45319_44915#FF0000_00FF00</a> so, first area will be RED (FF0000 , RGB Hexadecimal notation) painted and the second one Green (00FF00) all with transaprent (alpha channel) = 50% in order to show behind the coloured area.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-coloed" rel="tag" title="see questions tagged &#39;coloed&#39;">coloed</span> <span class="post-tag tag-link-multiple" rel="tag" title="see questions tagged &#39;multiple&#39;">multiple</span> <span class="post-tag tag-link-areas" rel="tag" title="see questions tagged &#39;areas&#39;">areas</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Sep '19, 11:02</strong></p>
<img src="https://secure.gravatar.com/avatar/18f7b5585b5dec78bbffd4339b05297b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Skelos&#39;s gravatar image" />
<p><span>Skelos</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Skelos has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-70927" class="comments-container">
&#10;</div>
<div id="comment-tools-70927" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70927-form-container" class="comment-form-container">
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

<span id="70930"></span>

<div id="answer-container-70930" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70930-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70930-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-70930-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You will have to write a program in e.g. JavaScript to do this. Perhaps the <a href="https://leafletjs.com/examples/choropleth/">Chloropeth Leaflet Example</a> has a lot of the functionality you need.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Sep '19, 16:12</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-70930" class="comments-container">
&#10;</div>
<div id="comment-tools-70930" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70930-form-container" class="comment-form-container">
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


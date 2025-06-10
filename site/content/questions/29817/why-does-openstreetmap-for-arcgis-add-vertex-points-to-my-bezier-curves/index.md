+++
type = "question"
title = "Why does OpenStreetMap for ArcGIS add vertex points to my bezier curves?"
description = '''I&#x27;ve downloaded data, and I&#x27;m trying to add new Street Centerlines. For some reason, when I create arc segments and bezier curves, the get broken into multiple straight segments.  Is that normal? If so, why does it work that way?'''
date = "2014-01-13T21:42:00Z"
lastmod = "2014-01-13T22:12:00Z"
weight = 29817
keywords = [ "edit", "arcgis", "bezier", "curve", "arcmap" ]
aliases = [ "/questions/29817" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Why does OpenStreetMap for ArcGIS add vertex points to my bezier curves?](/questions/29817/why-does-openstreetmap-for-arcgis-add-vertex-points-to-my-bezier-curves)

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
<span id="post-29817-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29817-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-29817-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've downloaded data, and I'm trying to add new Street Centerlines. For some reason, when I create arc segments and bezier curves, the get broken into multiple straight segments.<br />
</p>
<p>Is that normal? If so, why does it work that way?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-edit" rel="tag" title="see questions tagged &#39;edit&#39;">edit</span> <span class="post-tag tag-link-arcgis" rel="tag" title="see questions tagged &#39;arcgis&#39;">arcgis</span> <span class="post-tag tag-link-bezier" rel="tag" title="see questions tagged &#39;bezier&#39;">bezier</span> <span class="post-tag tag-link-curve" rel="tag" title="see questions tagged &#39;curve&#39;">curve</span> <span class="post-tag tag-link-arcmap" rel="tag" title="see questions tagged &#39;arcmap&#39;">arcmap</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Jan '14, 21:42</strong></p>
<img src="https://secure.gravatar.com/avatar/c2597ba1ee4ae4a4928d912ca653b683?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="CJCarsley&#39;s gravatar image" />
<p><span>CJCarsley</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="CJCarsley has no accepted answers">0%</span> </br></p>
</div>
</div>
<div id="comments-container-29817" class="comments-container">
&#10;</div>
<div id="comment-tools-29817" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29817-form-container" class="comment-form-container">
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

<span id="29818"></span>

<div id="answer-container-29818" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29818-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29818-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-29818-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="CJCarsley has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The OpenStreetMap <a href="http://wiki.openstreetmap.org/wiki/Data_model">data model</a> does not support bezier curves (or circles and arcs for that matter), hence the need to break them into straight line segments.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Jan '14, 22:12</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Jan '14, 09:41</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span></p>
</div>
</div>
<div id="comments-container-29818" class="comments-container">
&#10;</div>
<div id="comment-tools-29818" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29818-form-container" class="comment-form-container">
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


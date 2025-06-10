+++
type = "question"
title = "Merging a node and a way?"
description = '''I created a way (486594123), which is a boundary of a neighborhood. There is a node (153966491) of this neighborhood already, though some of the information is incorrect.  Is there a way to merge a way with a node? If not, should the node be deleted so that the way has the correct information with t...'''
date = "2017-04-13T16:12:00Z"
lastmod = "2020-01-07T04:40:00Z"
weight = 55588
keywords = [ "node", "way" ]
aliases = [ "/questions/55588" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Merging a node and a way?](/questions/55588/merging-a-node-and-a-way)

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
<span id="post-55588-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55588-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-55588-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I created a way (<a href="https://www.openstreetmap.org/way/486594123">486594123</a>), which is a boundary of a neighborhood. There is a node (<a href="https://www.openstreetmap.org/node/153966491">153966491</a>) of this neighborhood already, though some of the information is incorrect.</p>
<ol>
<li>Is there a way to merge a way with a node?</li>
<li>If not, should the node be deleted so that the way has the correct information with the correct boundary?</li>
</ol>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-node" rel="tag" title="see questions tagged &#39;node&#39;">node</span> <span class="post-tag tag-link-way" rel="tag" title="see questions tagged &#39;way&#39;">way</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Apr '17, 16:12</strong></p>
<img src="https://secure.gravatar.com/avatar/bf7c5af4e90fcccb4dfa685a241683b3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="divided&#39;s gravatar image" />
<p><span>divided</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="divided has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-55588" class="comments-container">
&#10;</div>
<div id="comment-tools-55588" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55588-form-container" class="comment-form-container">
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

<span id="55594"></span>

<div id="answer-container-55594" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55594-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55594-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-55594-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The name should probably just be "Hough". The other information can be calculated, for example:</p>
<p><a href="http://nominatim.openstreetmap.org/details.php?place_id=418128">http://nominatim.openstreetmap.org/details.php?place_id=418128</a></p>
<p>If there is not any government for the neighborhood, it should be tagged "landuse=residential" rather than boundary=administrative.</p>
<p>For towns and cities the usual US practice is to have both a boundary and a node. I'm not sure that makes as much sense for neighborhoods. For the cities, the node can be linked into the boundary, look at the bottom of the left pane, the admin_centre:</p>
<p><a href="https://www.openstreetmap.org/relation/135101">https://www.openstreetmap.org/relation/135101</a></p>
<p>But a neighborhood usually doesn't have an administrative function.</p>
<p>I think what I would probably do is leave the node (because they are often used for labeling) and then not put a place= tag on the landuse area.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Apr '17, 21:13</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-55594" class="comments-container">
<span id="55597"></span>
<div id="comment-55597" class="comment">
<div id="post-55597-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I see the admin_centre but how do you actually link the two?</p>
</div>
<div id="comment-55597-info" class="comment-info">
<span class="comment-age">(13 Apr '17, 21:26)</span> <span class="comment-user userinfo">divided</span>
</div>
</div>
<span id="55599"></span>
<div id="comment-55599" class="comment">
<div id="post-55599-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Open the boundary relation in the JOSM relation editor and manually add the node with the admin_centre role.</p>
<p>I don't think there is really a widely used system of linking neighborhood areas to place nodes though.</p>
</div>
<div id="comment-55599-info" class="comment-info">
<span class="comment-age">(13 Apr '17, 21:30)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
</div>
<div id="comment-tools-55594" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55594-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="55607"></span>

<div id="answer-container-55607" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55607-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55607-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-55607-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi</p>
<p>I think you can use the "Replace Geometry" function of JOSM. You have to select both the boundary and the node and press Ctrl + Shift + G. This will combine both and keep the recently created geometry, which is the boundary. Then you can just correct the information. This way, the node history will remain as well.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Apr '17, 15:32</strong></p>
<img src="https://secure.gravatar.com/avatar/c482180b767d07897d150d7b426ca4e0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmahmud&#39;s gravatar image" />
<p><span>mmahmud</span><br />
<span class="score" title="638 reputation points">638</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmahmud has one accepted answer">3%</span></p>
</div>
</div>
<div id="comments-container-55607" class="comments-container">
<span id="72389"></span>
<div id="comment-72389" class="comment">
<div id="post-72389-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Takk skal du ha this helped me in project</p>
<p>du er fantastisk å være,</p>
</div>
<div id="comment-72389-info" class="comment-info">
<span class="comment-age">(07 Jan '20, 04:40)</span> <span class="comment-user userinfo">solmaps2</span>
</div>
</div>
</div>
<div id="comment-tools-55607" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55607-form-container" class="comment-form-container">
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


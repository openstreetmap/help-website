+++
type = "question"
title = "Amenities - standalone nodes or outline nodes"
description = '''What is the best way/practice to map amenities in a building that has its outline mapped? 1) Put a standalone node within the area of building outline (not connecting it to the outline) 2) Put the node ON the outline itself? 3) Draw the whole building outline and then draw smaller polygons on top of...'''
date = "2018-02-18T07:12:00Z"
lastmod = "2018-02-18T17:15:00Z"
weight = 62179
keywords = [ "building", "amenity", "outlines" ]
aliases = [ "/questions/62179" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Amenities - standalone nodes or outline nodes](/questions/62179/amenities-standalone-nodes-or-outline-nodes)

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
<span id="post-62179-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62179-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-62179-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>What is the best way/practice to map amenities in a building that has its outline mapped?</p>
<p>1) Put a standalone node within the area of building outline (not connecting it to the outline)</p>
<p>2) Put the node ON the outline itself?</p>
<p>3) Draw the whole building outline and then draw smaller polygons on top of that that eventually fully cover the larger building outline? I've seen examples of that both with creating a relation and putting all in that and just drawing polygons on top of each other without relations.</p>
<p>My guess is that 1) is a better practice? I've seen few examples of 3) in my area but somehow it seems wrong to me to draw building polygons on top of each other.</p>
<p>This picture shows an example of 1) and 2) of them in a single building: <img src="https://i.imgur.com/66xYHgW.jpg" alt="alt text" /></p>
<p>And 3): <img src="https://i.imgur.com/X1XDPvy.jpg" alt="alt text" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-building" rel="tag" title="see questions tagged &#39;building&#39;">building</span> <span class="post-tag tag-link-amenity" rel="tag" title="see questions tagged &#39;amenity&#39;">amenity</span> <span class="post-tag tag-link-outlines" rel="tag" title="see questions tagged &#39;outlines&#39;">outlines</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Feb '18, 07:12</strong></p>
<img src="https://secure.gravatar.com/avatar/83a407005b50f4aec7b7ab0769089d5c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ivss_xx&#39;s gravatar image" />
<p><span>ivss_xx</span><br />
<span class="score" title="311 reputation points">311</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ivss_xx has 2 accepted answers">25%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Feb '18, 08:53</strong> </span></p>
</div>
</div>
<div id="comments-container-62179" class="comments-container">
&#10;</div>
<div id="comment-tools-62179" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62179-form-container" class="comment-form-container">
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

<span id="62183"></span>

<div id="answer-container-62183" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-62183-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62183-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-62183-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Option 1 keeps things simple and easy to modify for everyone. I almost always use that approach. I normally place it at same distance from the two ends of the front fachade, and a bit separated from the front building outline.</p>
<p>I would discourage option 2, because it doesn't make sense for me to mix a node of a (let's say) restaurant with the outline of the building where it is situated.</p>
<p>Option 3 are alternatives, but more complicated to edit and to maintain, specially for newbies. They may make sense in some big malls maybe, but I wouldn't use it for most of cases.</p>
<p>But I don't think we can say 1 is best practice, nor 3. It's left to the editor choice. What is good practice in general is to keep consistencies. So if you decide to map as option 3 a mall, I would suggest that you map all the same way, and not a mix.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Feb '18, 17:15</strong></p>
<img src="https://secure.gravatar.com/avatar/d45c161edd4b471fd947a7ec574274ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="edvac&#39;s gravatar image" />
<p><span>edvac</span><br />
<span class="score" title="665 reputation points">665</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="edvac has 4 accepted answers">15%</span></p>
</img>
</div>
</div>
<div id="comments-container-62183" class="comments-container">
&#10;</div>
<div id="comment-tools-62183" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62183-form-container" class="comment-form-container">
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


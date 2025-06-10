+++
type = "question"
title = "Labelling - Tag area or create label node?"
description = '''I&#x27;m a bit new to OSM, but one thing I have failed to understand is why people create separate nodes to label areas instead of putting the label directly in the name tag of the relevant area. It seems to me that it would be better to just put the label in the area&#x27;s tags because this gives renderers ...'''
date = "2017-06-22T03:05:00Z"
lastmod = "2017-06-22T06:52:00Z"
weight = 56714
keywords = [ "labels", "area" ]
aliases = [ "/questions/56714" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Labelling - Tag area or create label node?](/questions/56714/labelling-tag-area-or-create-label-node)

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
<span id="post-56714-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56714-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-56714-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm a bit new to OSM, but one thing I have failed to understand is why people create separate nodes to label areas instead of putting the label directly in the name tag of the relevant area. It seems to me that it would be better to just put the label in the area's tags because this gives renderers more freedom over where to render the name, and associates the name with the entire area to which it applies, which I thought would be ideal. Are there reasons to use one method over the other? Is one necessarily <em>wrong</em>?</p>
<p>Here is an example of what I'm talking about: <img src="https://help.openstreetmap.org/upfiles/2017-06-21-220308_905x561_scrot.png" /> The parking symbol on the left is from the area itself, and the one on the right is a separate node which only provides the name of the parking lot.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-labels" rel="tag" title="see questions tagged &#39;labels&#39;">labels</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Jun '17, 03:05</strong></p>
<img src="https://secure.gravatar.com/avatar/b1576690f58586beed7d0b554648529a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="idtownie&#39;s gravatar image" />
<p><span>idtownie</span><br />
<span class="score" title="46 reputation points">46</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="idtownie has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-56714" class="comments-container">
&#10;</div>
<div id="comment-tools-56714" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56714-form-container" class="comment-form-container">
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

<span id="56715"></span>

<div id="answer-container-56715" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56715-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56715-score" class="post-score" title="current number of votes">
9
</div>
<span id="post-56715-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="idtownie has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The general rule is <a href="https://wiki.openstreetmap.org/wiki/One_feature,_one_OSM_element">one feature should be represented by one object</a>. In the case you show, you are correct: The amenity=parking should only be tagged on the area, the node is redundant.</p>
<p>When I come across that type of thing I select both the area and the node and then use the JOSM "replace geometry" function to move all tags from the node to the area and delete the node. If there are any conflicts in the tags, JOSM will show them and let you decide what to do. If there are more tags on the node than the area (maybe addr:<em>=</em> tags) those are moved onto the area.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Jun '17, 03:26</strong></p>
<img src="https://secure.gravatar.com/avatar/f60af53a4eba0c21f25c22674fb4a8cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="n76&#39;s gravatar image" />
<p><span>n76</span><br />
<span class="score" title="10839 reputation points"><span>10.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="82 badges"><span class="silver">●</span><span class="badgecount">82</span></span><span title="172 badges"><span class="bronze">●</span><span class="badgecount">172</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="n76 has 48 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-56715" class="comments-container">
<span id="56716"></span>
<div id="comment-56716" class="comment">
<div id="post-56716-score" class="comment-score">
6
</div>
<div class="comment-text">
<p>For parking lots there is an additional problem: It used to be that you only get the "P" symbol on nodes tagged with <code>amenity=parking</code>. But some people wanted to have that symbol, so they added the extra node. Today, the parking lots are rendered not only as yellow areas but they have the additional "P" symbol. This is a prime example why you shouldn't map for the renderer. The renderer might change!</p>
</div>
<div id="comment-56716-info" class="comment-info">
<span class="comment-age">(22 Jun '17, 06:52)</span> <span class="comment-user userinfo">Jochen Topf</span>
</div>
</div>
</div>
<div id="comment-tools-56715" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56715-form-container" class="comment-form-container">
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


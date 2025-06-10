+++
type = "question"
title = "Associating an entrace with an amenity"
description = '''Is there a way to connect an entrance to an amenity/a shop/a general POI inside a building? In a wild example a huge building where the main entrance is on one side and the amenity is on the far side of the building. The amenity has its own entrance that&#x27;s nearer and should be used instead. 1 - are ...'''
date = "2017-07-13T17:07:00Z"
lastmod = "2017-07-13T18:14:00Z"
weight = 57080
keywords = [ "entrance", "routing" ]
aliases = [ "/questions/57080" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Associating an entrace with an amenity](/questions/57080/associating-an-entrace-with-an-amenity)

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
<span id="post-57080-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57080-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-57080-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is there a way to connect an entrance to an amenity/a shop/a general POI inside a building?</p>
<p>In a wild example a huge building where the main entrance is on one side and the amenity is on the far side of the building. The amenity has its own entrance that's nearer and should be used instead.</p>
<p>1 - are there any such tags to specify "this entrance can be used for this POI"?<br />
2 - are they consumed?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-entrance" rel="tag" title="see questions tagged &#39;entrance&#39;">entrance</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Jul '17, 17:07</strong></p>
<img src="https://secure.gravatar.com/avatar/f882e7865ffe23339fbaa71c9f576065?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="FredrikLindseth&#39;s gravatar image" />
<p><span>FredrikLindseth</span><br />
<span class="score" title="815 reputation points">815</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="35 badges"><span class="bronze">●</span><span class="badgecount">35</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="FredrikLindseth has 2 accepted answers">13%</span> </br></p>
</div>
</div>
<div id="comments-container-57080" class="comments-container">
&#10;</div>
<div id="comment-tools-57080" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57080-form-container" class="comment-form-container">
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

<span id="57081"></span>

<div id="answer-container-57081" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-57081-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57081-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-57081-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>A building can have more than one entrance (both in reality and in the map). If the entrance that's nearer the amenity is mapped as entrance=main or entrance=yes, I assume routers will use it.</p>
<p>Moreover, you could draw a way from the preferred entrance to the amenity and mark it as <a href="https://wiki.openstreetmap.org/wiki/Tag:highway%3Dcorridor">highway=corridor</a> (or <a href="https://wiki.openstreetmap.org/wiki/Key:indoor">indoor=corridor</a>). If the amenity is an area, I suppose the best thing would be to create an entrance node on the border of that area (that's a <em>third</em> entrance node, in addition to the two entrance nodes of the building itself) and connect that node to the corridor.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Jul '17, 18:14</strong></p>
<img src="https://secure.gravatar.com/avatar/8440750fd002fd989ab2e6b613ca3ccb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dsh4&#39;s gravatar image" />
<p><span>dsh4</span><br />
<span class="score" title="867 reputation points">867</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="30 badges"><span class="bronze">●</span><span class="badgecount">30</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dsh4 has one accepted answer">4%</span></p>
</div>
</div>
<div id="comments-container-57081" class="comments-container">
&#10;</div>
<div id="comment-tools-57081" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57081-form-container" class="comment-form-container">
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


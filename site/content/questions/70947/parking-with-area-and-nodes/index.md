+++
type = "question"
title = "Parking with area and nodes"
description = '''Hello everyone! Recently I encountered some parking areas defined by their area, but including all parking slots as nodes. See here for example. This posed to be a problem searching for a parking in the city, because my app showed all individual slots. Is this the correct way of mapping a parking ar...'''
date = "2019-09-28T16:13:00Z"
lastmod = "2019-09-29T08:13:00Z"
weight = 70947
keywords = [ "node", "area", "parking" ]
aliases = [ "/questions/70947" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Parking with area and nodes](/questions/70947/parking-with-area-and-nodes)

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
<span id="post-70947-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70947-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70947-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello everyone! Recently I encountered some parking areas defined by their area, but including all parking slots as nodes. See <a href="https://www.openstreetmap.org/edit#map=19/39.06892/-108.56550">here</a> for example. This posed to be a problem searching for a parking in the city, because my app showed all individual slots.</p>
<p>Is this the correct way of mapping a parking area? (If so, then the problem lies in my app not being able to interpret the data correctly). Or is it preferable to just use an area and use the <em>capacity</em> tag?</p>
<p>The wiki entry for the <a href="https://wiki.openstreetmap.org/wiki/Tag:amenity%3Dparking">parking</a> tag states to <em>Tag either an area or a central node, but not both.</em> . However, this implies that the same parking area has been tagged twice (with an area and with a central node). In the example mentioned above though, there is no central node, there are nodes for each slot.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-node" rel="tag" title="see questions tagged &#39;node&#39;">node</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span> <span class="post-tag tag-link-parking" rel="tag" title="see questions tagged &#39;parking&#39;">parking</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Sep '19, 16:13</strong></p>
<img src="https://secure.gravatar.com/avatar/7f9f77774a394247bc38ff54fefa5b89?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jorgman1&#39;s gravatar image" />
<p><span>jorgman1</span><br />
<span class="score" title="36 reputation points">36</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jorgman1 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-70947" class="comments-container">
&#10;</div>
<div id="comment-tools-70947" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70947-form-container" class="comment-form-container">
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

<span id="70948"></span>

<div id="answer-container-70948" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70948-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70948-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-70948-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="jorgman1 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This page gives more advice on parking place tagging <a href="https://wiki.openstreetmap.org/wiki/Tag:amenity%3Dparking_space">https://wiki.openstreetmap.org/wiki/Tag:amenity%3Dparking_space</a></p>
<p>Apparently the advice is to group parking spaces into a site relation. Maybe then the site will be rendered as the car park.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Sep '19, 18:36</strong></p>
<img src="https://secure.gravatar.com/avatar/e3283a6b5f83e16214ec39a1478f64f0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BCNorwich&#39;s gravatar image" />
<p><span>BCNorwich</span><br />
<span class="score" title="6299 reputation points"><span>6.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="44 badges"><span class="silver">●</span><span class="badgecount">44</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BCNorwich has 44 accepted answers">20%</span></p>
</div>
</div>
<div id="comments-container-70948" class="comments-container">
<span id="70952"></span>
<div id="comment-70952" class="comment">
<div id="post-70952-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for the link! I think I understand now how it should be mapped (according to <a href="https://wiki.openstreetmap.org/wiki/Tag:amenity%3Dparking_space">amenity=parking_space</a> and to <a href="https://wiki.openstreetmap.org/wiki/Proposed_features/parking">this</a> proposal). Correct me if I'm wrong.</p>
<p>If nothing else is known, use a node in the centre of the parking to mark it. Or if the outline is known, then use an area.</p>
<p>For a more detailed depiction, use either nodes or areas (recommended) to mark each space under the tag amenity=parking_space. Ideally, this should have capacity=1 (default if not mapped), but if the satellite image is not good enough, it could have a larger capacity.</p>
<p>And then use a relation (type=site, site=parking) to group individual parking spaces together.</p>
</div>
<div id="comment-70952-info" class="comment-info">
<span class="comment-age">(29 Sep '19, 08:09)</span> <span class="comment-user userinfo">jorgman1</span>
</div>
</div>
<span id="70954"></span>
<div id="comment-70954" class="comment">
<div id="post-70954-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes agreed with one exception, the amenity=parking_space would be singular therefore no need for the capacity tag. The overall parking area would hold the capacity tag and capacity of disabled or family spaces.</p>
</div>
<div id="comment-70954-info" class="comment-info">
<span class="comment-age">(29 Sep '19, 08:13)</span> <span class="comment-user userinfo">BCNorwich</span>
</div>
</div>
</div>
<div id="comment-tools-70948" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70948-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="70950"></span>

<div id="answer-container-70950" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70950-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70950-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-70950-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The parking areas you linked to are not an example of good mapping style, but not because of the attempt to map individual parking spaces – that's accepted practice.</p>
<p>Note that the individual slots are not mapped as <code>amenity=parking</code>, but as <a href="https://wiki.openstreetmap.org/wiki/Tag:amenity%3Dparking_space"><code>amenity=parking_space</code></a>. This should allow your app to make sense of the situation.</p>
<p>It's weird, however, that the nodes are part of the <em>outline</em> of the parking areas. Usually, the parking spaces would either be mapped as areas (most common), or using nodes at the center, rather than at the edge, of the parking space. Therefore, one would expect them to be located well within the parking area at some distance from the outline.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Sep '19, 20:50</strong></p>
<img src="https://secure.gravatar.com/avatar/0626be5f46f32fce501353e8a5ec399c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tordanik&#39;s gravatar image" />
<p><span>Tordanik</span><br />
<span class="score" title="11998 reputation points"><span>12.0k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="106 badges"><span class="silver">●</span><span class="badgecount">106</span></span><span title="147 badges"><span class="bronze">●</span><span class="badgecount">147</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tordanik has 58 accepted answers">35%</span></p>
</div>
</div>
<div id="comments-container-70950" class="comments-container">
<span id="70953"></span>
<div id="comment-70953" class="comment">
<div id="post-70953-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That makes sense. Thank you!</p>
</div>
<div id="comment-70953-info" class="comment-info">
<span class="comment-age">(29 Sep '19, 08:10)</span> <span class="comment-user userinfo">jorgman1</span>
</div>
</div>
</div>
<div id="comment-tools-70950" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70950-form-container" class="comment-form-container">
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


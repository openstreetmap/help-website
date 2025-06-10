+++
type = "question"
title = "IDeditor: Change a POI/business to closed"
description = '''I want to update a POI for a restaurant that has permanently closed.  OSM help (OSM help ) tells me it should be using lifecycle in tag:  disused:amenity=restaurant How can I do this change in IDeditor?'''
date = "2019-09-24T06:34:00Z"
lastmod = "2019-09-25T11:51:00Z"
weight = 70903
keywords = [ "ideditor", "out-of-business", "closed", "business", "poi" ]
aliases = [ "/questions/70903" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [IDeditor: Change a POI/business to closed](/questions/70903/ideditor-change-a-poibusiness-to-closed)

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
<span id="post-70903-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70903-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-70903-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to update a POI for a restaurant that has permanently closed. OSM help (<a href="https://wiki.openstreetmap.org/wiki/DE:Tag:amenity%3Drestaurant">OSM help</a> ) tells me it should be using lifecycle in tag: disused:amenity=restaurant How can I do this change in IDeditor?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ideditor" rel="tag" title="see questions tagged &#39;ideditor&#39;">ideditor</span> <span class="post-tag tag-link-out-of-business" rel="tag" title="see questions tagged &#39;out-of-business&#39;">out-of-business</span> <span class="post-tag tag-link-closed" rel="tag" title="see questions tagged &#39;closed&#39;">closed</span> <span class="post-tag tag-link-business" rel="tag" title="see questions tagged &#39;business&#39;">business</span> <span class="post-tag tag-link-poi" rel="tag" title="see questions tagged &#39;poi&#39;">poi</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Sep '19, 06:34</strong></p>
<img src="https://secure.gravatar.com/avatar/63547ae33ed27d57ac78c66905f5d2cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gerhard_v&#39;s gravatar image" />
<p><span>gerhard_v</span><br />
<span class="score" title="42 reputation points">42</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gerhard_v has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-70903" class="comments-container">
&#10;</div>
<div id="comment-tools-70903" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70903-form-container" class="comment-form-container">
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

<span id="70904"></span>

<div id="answer-container-70904" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70904-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70904-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-70904-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="gerhard_v has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>First of all, you <em>can</em> just delete the restaurant (be careful not to accidentally delete the building it is in though). The lifecycle concepts are not widely used, and may also clash with the concept of verifiability - as a rule of thumb you should only consider <code>disused:amenity</code> if the original character of the thing is still clearly visible, i.e. if it still looks like a restaurant, but now is permanently closed.</p>
<p>To change "amenity" to "disused:amenity", just scroll down on the properties tab on the left hand side after you have selected the object, and open the "all tags" section where you can make the change.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Sep '19, 08:30</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-70904" class="comments-container">
<span id="70906"></span>
<div id="comment-70906" class="comment">
<div id="post-70906-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I'll add my usual caution about POI deletion: Careful about deleting a node that has address tags if the address in question is still valid for the premises! Generally the next thing to come along will inherit the old address and it's good to <a href="https://wiki.openstreetmap.org/wiki/Keep_the_history">"keep the history"</a>.</p>
<p>So in these cases it's better to just delete all of the tags specific to the old occupant of that location. And, as Frederik mentioned, if the presumed use of the place has not changed then using the "<code>disused:</code>" prefix is good, eg, <code>disused:shop=yes</code>, <code>disused:amenity=restaurant</code>, <code>disused:amenity=place_of_worship</code>, etc.</p>
<p>(Not sure exactly what Frederik's bar is for "widely used" but there are currently over 12000 disused shops and 20000 disused amenities.)</p>
</div>
<div id="comment-70906-info" class="comment-info">
<span class="comment-age">(24 Sep '19, 15:25)</span> <span class="comment-user userinfo">jmapb</span>
</div>
</div>
<span id="70908"></span>
<div id="comment-70908" class="comment">
<div id="post-70908-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks, Frederik, I didn't realize I can edit the left hand side of that table and place a 'disused:' in front of 'amenity'. Couldn't find an entry 'disused:amenity' in the dropdown list, that's why I asked here.</p>
</div>
<div id="comment-70908-info" class="comment-info">
<span class="comment-age">(25 Sep '19, 06:11)</span> <span class="comment-user userinfo">gerhard_v</span>
</div>
</div>
<span id="70909"></span>
<div id="comment-70909" class="comment">
<div id="post-70909-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It appears that ID will recognize when there are address tags and "downgrade" the POI by automatically changing to disused:amenity= . But if there are no address tags, the node will be deleted. It would be better to keep the node and manually change to disused:amenity as discussed above to preserve the node's history.</p>
</div>
<div id="comment-70909-info" class="comment-info">
<span class="comment-age">(25 Sep '19, 11:51)</span> <span class="comment-user userinfo">Mike N</span>
</div>
</div>
</div>
<div id="comment-tools-70904" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70904-form-container" class="comment-form-container">
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


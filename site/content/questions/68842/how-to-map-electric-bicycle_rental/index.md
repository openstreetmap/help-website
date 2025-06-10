+++
type = "question"
title = "How to map electric bicycle_rental?"
description = '''In our city we have a bicycle rental scheme which provides both electric and conventional bikes. Are there any conventions existing that define how I can tag electric bicycle_rentals?'''
date = "2019-04-18T21:11:00Z"
lastmod = "2019-07-31T22:15:00Z"
weight = 68842
keywords = [ "tagging", "electric", "bicycle_rental" ]
aliases = [ "/questions/68842" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to map electric bicycle_rental?](/questions/68842/how-to-map-electric-bicycle_rental)

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
<span id="post-68842-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68842-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-68842-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In our city we have a bicycle rental scheme which provides both electric and conventional bikes. Are there any conventions existing that define how I can tag electric bicycle_rentals?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-electric" rel="tag" title="see questions tagged &#39;electric&#39;">electric</span> <span class="post-tag tag-link-bicycle_rental" rel="tag" title="see questions tagged &#39;bicycle_rental&#39;">bicycle_rental</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Apr '19, 21:11</strong></p>
<img src="https://secure.gravatar.com/avatar/6c4616a8bf7379d9092c353dd5889eba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EliasPajares&#39;s gravatar image" />
<p><span>EliasPajares</span><br />
<span class="score" title="71 reputation points">71</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EliasPajares has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-68842" class="comments-container">
&#10;</div>
<div id="comment-tools-68842" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68842-form-container" class="comment-form-container">
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

<span id="70263"></span>

<div id="answer-container-70263" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70263-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70263-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-70263-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'd be inclined to use the <code>amenity=bicycle_rental</code> tag (as linked to by LivingWithDragons) but I don't think that <code>amperage=</code> or <code>voltage=</code> tags are appropriate here.</p>
<p>I do think additional tags could be added to clarify the types of bicycles available. One option would be to add a <code>bicycle:type=</code> (or <code>bicycle_rental:type=</code>) tag and list the types there, ie, <code>bicycle:type=electric;pedal</code>. Another option would be to have a separate tag for each type, ie 'bicycle:electric=yes', 'bicycle:pedal=yes'.</p>
<p>Using either of these tagging styles, the messy part will be determining exactly what the names for all the bike types should be. Some people might say "electric" and some might say "e-bike." A recumbent bike has pedals, so does that mean that using "pedal" for a standard bike is wrong? (Remember that there are MANY kinds of bicycles. I recently tagged a spot that rents standard bikes, tandem bikes, and four-wheeled bikes. I didn't try to tag the types because it just seemed too complicated! But it's tagged with a website where people can see the inventory.)</p>
<p>I'd suggest just adding tags that make sense to you, and being open to discussion if someone has other suggestions. And I'd also suggest adding a <code>description=</code> tag (eg <code>description=bicycle rental station with standard and electric bikes</code>) because until bicycle type tags become reasonably popular, nobody will be looking for them.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Jul '19, 21:45</strong></p>
<img src="https://secure.gravatar.com/avatar/977d95e2184a885d9a01fb3297225872?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jmapb&#39;s gravatar image" />
<p><span>jmapb</span><br />
<span class="score" title="3387 reputation points"><span>3.4k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="61 badges"><span class="bronze">●</span><span class="badgecount">61</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jmapb has 22 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-70263" class="comments-container">
<span id="70266"></span>
<div id="comment-70266" class="comment">
<div id="post-70266-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you very much for your answer. Adding additional tags would definitely make it more clear but as you said I also see the messy part of it. In this case it makes sense for me as both bikes have a different quality. But yeah other users may think it is not important at all.</p>
</div>
<div id="comment-70266-info" class="comment-info">
<span class="comment-age">(31 Jul '19, 22:15)</span> <span class="comment-user userinfo">EliasPajares</span>
</div>
</div>
</div>
<div id="comment-tools-70263" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70263-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="69129"></span>

<div id="answer-container-69129" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69129-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69129-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-69129-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are various <a href="https://wiki.openstreetmap.org/wiki/Tag:amenity%3Dbicycle_rental">tags to add to a bicycle rental scheme</a>.</p>
<p>Do the rental schemes have different names that would be appropriate for the "Network" tag and make it obvious that they were electric? That isn't perfect as any systems to <em>find electric bike hire</em> would need to know the specific name of your city scheme.</p>
<p>Perhaps you could add additional tags like <a href="https://wiki.openstreetmap.org/wiki/Tag:amenity%3Dcharging_station">amperage= <em>or voltage=</em></a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 May '19, 12:51</strong></p>
<img src="https://secure.gravatar.com/avatar/f846f21cfbcf60a35e1f69c2cc74df77?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LivingWithDragons&#39;s gravatar image" />
<p><span>LivingWithDr...</span><br />
<span class="score" title="524 reputation points">524</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LivingWithDragons has one accepted answer">4%</span></p>
</div>
</div>
<div id="comments-container-69129" class="comments-container">
<span id="70051"></span>
<div id="comment-70051" class="comment">
<div id="post-70051-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your answer and sorry for this late answer. Unfortunately both systems are operated by the same provider. I see. So there is no standard yet. Using amperage or voltage could be a work around. Before using them I will consult the local community.</p>
</div>
<div id="comment-70051-info" class="comment-info">
<span class="comment-age">(13 Jul '19, 20:04)</span> <span class="comment-user userinfo">EliasPajares</span>
</div>
</div>
<span id="70253"></span>
<div id="comment-70253" class="comment">
<div id="post-70253-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I was thinking you might have Network="BikeCorp Electric Bikes" and Network="BikeCorp Bikes". A case that I wouldn't do that is if you join one scheme and get access to both types.</p>
</div>
<div id="comment-70253-info" class="comment-info">
<span class="comment-age">(31 Jul '19, 14:30)</span> <span class="comment-user userinfo">LivingWithDr...</span>
</div>
</div>
</div>
<div id="comment-tools-69129" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69129-form-container" class="comment-form-container">
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


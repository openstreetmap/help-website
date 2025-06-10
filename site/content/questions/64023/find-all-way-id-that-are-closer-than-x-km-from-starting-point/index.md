+++
type = "question"
title = "Find all way id that are closer than x km from starting point"
description = '''For my project I want to find all streets that can be reached within a certain driving distance. A practical example would be a car that has 50km mileage left. Which streets can be reached? The long way of doing this would be to set up a Shortest Tree Path from the starting point and cut at the desi...'''
date = "2018-06-04T18:08:00Z"
lastmod = "2018-06-06T21:07:00Z"
weight = 64023
keywords = [ "directions", "ways", "naming", "closest", "convention" ]
aliases = [ "/questions/64023" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Find all way id that are closer than x km from starting point](/questions/64023/find-all-way-id-that-are-closer-than-x-km-from-starting-point)

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
<span id="post-64023-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64023-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-64023-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>For my project I want to find all streets that can be reached within a certain driving distance. A practical example would be a car that has 50km mileage left. Which streets can be reached?</p>
<p>The long way of doing this would be to set up a Shortest Tree Path from the starting point and cut at the desired range from the starting point to get all way ids.</p>
<p>I was wondering if there is maybe an easier way. For example if I find all outermost way ids that are reachable with x km mileage left. Is there a way to deduct all way ids that are within this outer circle of way ids, meaning closer to the starting point and therefore reachable? Is there a way id naming convention that helps with this? Basically what is important for my project is getting all way or even node ids that are reachable within a ceratain mileage from a starting point. Thanks a lot!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-directions" rel="tag" title="see questions tagged &#39;directions&#39;">directions</span> <span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span> <span class="post-tag tag-link-naming" rel="tag" title="see questions tagged &#39;naming&#39;">naming</span> <span class="post-tag tag-link-closest" rel="tag" title="see questions tagged &#39;closest&#39;">closest</span> <span class="post-tag tag-link-convention" rel="tag" title="see questions tagged &#39;convention&#39;">convention</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Jun '18, 18:08</strong></p>
<img src="https://secure.gravatar.com/avatar/e49539552cb1e89cbb3f190fcee73807?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TobiC&#39;s gravatar image" />
<p><span>TobiC</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TobiC has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-64023" class="comments-container">
<span id="64028"></span>
<div id="comment-64028" class="comment">
<div id="post-64028-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What data source you want to use for that? API / imported OSM database?</p>
</div>
<div id="comment-64028-info" class="comment-info">
<span class="comment-age">(05 Jun '18, 12:44)</span> <span class="comment-user userinfo">altopalo</span>
</div>
</div>
<span id="64066"></span>
<div id="comment-64066" class="comment">
<div id="post-64066-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Right now I am planning to download map tiles from osm and then find all way_ids that are within a certain distance. Probably by defining an outer perimeter where a specific street is just within reach of x km from starting point. And in the second step find all way_id that are within this perimeter / GPS point within this geometry(polygon, circle, rectangle, whatever it might end up looking like)</p>
</div>
<div id="comment-64066-info" class="comment-info">
<span class="comment-age">(06 Jun '18, 21:07)</span> <span class="comment-user userinfo">TobiC</span>
</div>
</div>
</div>
<div id="comment-tools-64023" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64023-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>


+++
type = "question"
title = "calculate room between buildings"
description = '''Hey everyone, is there any easy way to map the room between buildings? &quot;surface&quot; doesn&#x27;t help in this case, because mostly it only shows streets around the buildings. I thought about for example landuse=residential and just subtract the building-area. But &quot;landuse&quot; is just very unspecific, because i...'''
date = "2022-05-31T09:41:00Z"
lastmod = "2022-06-01T07:39:00Z"
weight = 84636
keywords = [ "buildings", "between", "space" ]
aliases = [ "/questions/84636" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [calculate room between buildings](/questions/84636/calculate-room-between-buildings)

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
<span id="post-84636-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84636-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84636-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hey everyone, is there any easy way to map the room between buildings? "surface" doesn't help in this case, because mostly it only shows streets around the buildings. I thought about for example landuse=residential and just subtract the building-area. But "landuse" is just very unspecific, because it includes e.g. cemeteries or other surfaces I am not looking for. Can you help? Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-buildings" rel="tag" title="see questions tagged &#39;buildings&#39;">buildings</span> <span class="post-tag tag-link-between" rel="tag" title="see questions tagged &#39;between&#39;">between</span> <span class="post-tag tag-link-space" rel="tag" title="see questions tagged &#39;space&#39;">space</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 May '22, 09:41</strong></p>
<img src="https://secure.gravatar.com/avatar/749db2750393b3be709a6e9a2c654b39?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="milo22948392&#39;s gravatar image" />
<p><span>milo22948392</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="milo22948392 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-84636" class="comments-container">
<span id="84637"></span>
<div id="comment-84637" class="comment">
<div id="post-84637-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Do you want to calculate the percentage of area occupied by buildings in a residential area or is it the distance between buildings. Please explain a little more on what you want to do.</p>
</div>
<div id="comment-84637-info" class="comment-info">
<span class="comment-age">(31 May '22, 10:35)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="84638"></span>
<div id="comment-84638" class="comment">
<div id="post-84638-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I want to calculate the percentage area of space between buildings, so everything except the buildings. For example there is a part of a city where many apartments/buildings are located and I want to calculate the percentage of every landuse in this area (to get 100% of the area). The buildings are easy to calculate, but there are sealed places or something between them (which are not found through "surface=asphalt" or something) and that's what i need as well.</p>
</div>
<div id="comment-84638-info" class="comment-info">
<span class="comment-age">(31 May '22, 11:21)</span> <span class="comment-user userinfo">milo22948392</span>
</div>
</div>
<span id="84641"></span>
<div id="comment-84641" class="comment">
<div id="post-84641-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If you are working on small area I would draw the separate polygons yourself from Bing aerial images. Then subtract each polygon from the whole area...maybe? Most towns do not have all of the land mapped so it may be difficult. If you only need the area covered by buildings compared to total area that may be possible.</p>
</div>
<div id="comment-84641-info" class="comment-info">
<span class="comment-age">(31 May '22, 16:18)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="84644"></span>
<div id="comment-84644" class="comment">
<div id="post-84644-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>yes, that's the problem. It should be possible for a whole city, at best for any city.. I will see what I can do. Thanks for your help!</p>
</div>
<div id="comment-84644-info" class="comment-info">
<span class="comment-age">(01 Jun '22, 07:39)</span> <span class="comment-user userinfo">milo22948392</span>
</div>
</div>
</div>
<div id="comment-tools-84636" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84636-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>


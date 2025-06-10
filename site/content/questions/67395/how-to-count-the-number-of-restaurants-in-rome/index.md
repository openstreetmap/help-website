+++
type = "question"
title = "How to count the number of restaurants in Rome?"
description = '''Hi, I am trying to count how many restaurants have been added in Rome. In the majority of cases restaurants seem to be added as nodes and tagged as amenity=restaurant, but sometimes they are also added as polygons and tagged as either amenity=restaurants or building=restaurants.  If I union both nod...'''
date = "2018-12-30T19:59:00Z"
lastmod = "2018-12-31T06:52:00Z"
weight = 67395
keywords = [ "count", "amenity", "rome", "restaurant" ]
aliases = [ "/questions/67395" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to count the number of restaurants in Rome?](/questions/67395/how-to-count-the-number-of-restaurants-in-rome)

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
<span id="post-67395-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67395-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-67395-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I am trying to count how many restaurants have been added in Rome. In the majority of cases restaurants seem to be added as nodes and tagged as amenity=restaurant, but sometimes they are also added as polygons and tagged as either amenity=restaurants or building=restaurants. If I union both nodes and polygons, may I double-count some restaurants? I mean, is it possible to find the same restaurant added both as a polygon and as a node within that polygon? If this is the case, any idea how to remove duplicates after union the results?</p>
<p>Thanks, Jacopo</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-count" rel="tag" title="see questions tagged &#39;count&#39;">count</span> <span class="post-tag tag-link-amenity" rel="tag" title="see questions tagged &#39;amenity&#39;">amenity</span> <span class="post-tag tag-link-rome" rel="tag" title="see questions tagged &#39;rome&#39;">rome</span> <span class="post-tag tag-link-restaurant" rel="tag" title="see questions tagged &#39;restaurant&#39;">restaurant</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Dec '18, 19:59</strong></p>
<img src="https://secure.gravatar.com/avatar/70118cccb3f46cbc63cac9d1733a74ac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jprimav&#39;s gravatar image" />
<p><span>jprimav</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jprimav has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>31 Dec '18, 14:59</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-67395" class="comments-container">
<span id="67397"></span>
<div id="comment-67397" class="comment">
<div id="post-67397-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Not sure about the polygons and nodes, but to filter possible double ones you could compare them by name &amp; address, so let's say 'for each result on the whole list, if address &amp; name are the same then delete one'.</p>
</div>
<div id="comment-67397-info" class="comment-info">
<span class="comment-age">(30 Dec '18, 20:50)</span> <span class="comment-user userinfo">tijmenheid</span>
</div>
</div>
<span id="67401"></span>
<div id="comment-67401" class="comment">
<div id="post-67401-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Note that it is an "error" to map the same restaurant as node and polygon. I expect the the number of such errors is small, but if they appear, they should be fixed in the original data.</p>
</div>
<div id="comment-67401-info" class="comment-info">
<span class="comment-age">(31 Dec '18, 06:52)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
</div>
<div id="comment-tools-67395" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67395-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>


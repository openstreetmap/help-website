+++
type = "question"
title = "OSM is not displayed."
description = '''My application is being used by public institutions and displays maps with OSM. I was using osm normally, but from some moment it is not displayed like the picture below. Request URL: http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png What could be the problem? Is it blocked somewhere? https://docs.g...'''
date = "2023-07-05T10:03:00Z"
lastmod = "2023-07-07T02:00:00Z"
weight = 87440
keywords = [ "#osm" ]
aliases = [ "/questions/87440" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [OSM is not displayed.](/questions/87440/osm-is-not-displayed)

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
<span id="post-87440-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87440-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87440-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>My application is being used by public institutions and displays maps with OSM. I was using osm normally, but from some moment it is not displayed like the picture below.</p>
<p>Request URL: http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png</p>
<p>What could be the problem? Is it blocked somewhere?</p>
<p><a href="https://docs.google.com/document/d/1kcPCyuFYZs3ltwuTA0yGqXiCxylc9JTzybZR15Ue--s/edit?usp=sharing">https://docs.google.com/document/d/1kcPCyuFYZs3ltwuTA0yGqXiCxylc9JTzybZR15Ue--s/edit?usp=sharing</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-#osm" rel="tag" title="see questions tagged &#39;#osm&#39;">#osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Jul '23, 10:03</strong></p>
<img src="https://secure.gravatar.com/avatar/a80d6d00da81b11ea565b85440992e88?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sxmhxnjxn&#39;s gravatar image" />
<p><span>sxmhxnjxn</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sxmhxnjxn has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-87440" class="comments-container">
<span id="87443"></span>
<div id="comment-87443" class="comment">
<div id="post-87443-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Where are you located? Can you open dev tools of your browser to see the errors in trying to access e.g. <a href="https://a.tile.openstreetmap.org/1/1/1.png">https://a.tile.openstreetmap.org/1/1/1.png</a> ?</p>
</div>
<div id="comment-87443-info" class="comment-info">
<span class="comment-age">(06 Jul '23, 11:03)</span> <span class="comment-user userinfo">Spiekerooger</span>
</div>
</div>
<span id="87444"></span>
<div id="comment-87444" class="comment">
<div id="post-87444-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Try without the "{s}". That isn't needed any more. Also note that whatever is accessing OSM tiles needs to follow <a href="https://operations.osmfoundation.org/policies/tiles/">https://operations.osmfoundation.org/policies/tiles/</a> . It may be that you are infringing some technical requirements there.</p>
</div>
<div id="comment-87444-info" class="comment-info">
<span class="comment-age">(06 Jul '23, 12:04)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="87445"></span>
<div id="comment-87445" class="comment">
<div id="post-87445-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>While the {s} is deprecated it still would work, so it's true to best change the url, but this is - at least as of today - not the cause of the problem.</p>
<p>One cause could be the GFW. That's why I'm asking about location.</p>
</div>
<div id="comment-87445-info" class="comment-info">
<span class="comment-age">(06 Jul '23, 12:31)</span> <span class="comment-user userinfo">Spiekerooger</span>
</div>
</div>
<span id="87449"></span>
<div id="comment-87449" class="comment">
<div id="post-87449-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The location where osm is not visible is Suwon in South Korea, and the representative IPs are 211.114.22.71 and 211.114.22.131. But since yesterday afternoon, osm is showing up again. lol</p>
</div>
<div id="comment-87449-info" class="comment-info">
<span class="comment-age">(07 Jul '23, 02:00)</span> <span class="comment-user userinfo">sxmhxnjxn</span>
</div>
</div>
</div>
<div id="comment-tools-87440" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87440-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>


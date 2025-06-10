+++
type = "question"
title = "How avoiding double housenumbers, and how forcing missing icon?"
description = '''Hi everybody,  as of Oct. 4, 2013 in the following map: http://www.openstreetmap.org/#map=19/52.48565/13.38569 you see the house number twice, but you do not see the  actual icon for the laundry. How do I force an icon to  be visible, and how do I avoid double house numbers  (building without number...'''
date = "2013-10-04T15:41:00Z"
lastmod = "2013-10-05T17:02:00Z"
weight = 26950
keywords = [ "double", "housenumbers", "missing", "force", "icon" ]
aliases = [ "/questions/26950" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How avoiding double housenumbers, and how forcing missing icon?](/questions/26950/how-avoiding-double-housenumbers-and-how-forcing-missing-icon)

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
<span id="post-26950-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26950-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-26950-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi everybody,</p>
<p>as of Oct. 4, 2013 in the following map: <a href="http://www.openstreetmap.org/#map=19/52.48565/13.38569">http://www.openstreetmap.org/#map=19/52.48565/13.38569</a> you see the house number twice, but you do not see the actual icon for the laundry. How do I force an icon to be visible, and how do I avoid double house numbers (building without number, knot with house number, and specific facility in the same place with house number but without knot)?</p>
<p>Thanks</p>
<p>--</p>
<p>I'll mark this as resolved by Wednesday, I guess</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-double" rel="tag" title="see questions tagged &#39;double&#39;">double</span> <span class="post-tag tag-link-housenumbers" rel="tag" title="see questions tagged &#39;housenumbers&#39;">housenumbers</span> <span class="post-tag tag-link-missing" rel="tag" title="see questions tagged &#39;missing&#39;">missing</span> <span class="post-tag tag-link-force" rel="tag" title="see questions tagged &#39;force&#39;">force</span> <span class="post-tag tag-link-icon" rel="tag" title="see questions tagged &#39;icon&#39;">icon</span>
</div>
<div id="question-controls" class="post-controls">
<div class="community-wiki">
This question is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Oct '13, 15:41</strong></p>
<img src="https://secure.gravatar.com/avatar/6b40a86731c4b09ad4017ca3975cacd2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="C-in-Berlin&#39;s gravatar image" />
<p><span>C-in-Berlin</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="C-in-Berlin has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Oct '13, 17:37</strong> </span></p>
</div>
</div>
<div id="comments-container-26950" class="comments-container">
&#10;</div>
<div id="comment-tools-26950" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26950-form-container" class="comment-form-container">
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

<span id="26958"></span>

<div id="answer-container-26958" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-26958-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26958-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-26958-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi in the absence of answers I shall add my 2c worth.</p>
<p>The building has been tagged using address interpolation to give a # 124. The laundry has also been given an address # 124. Probably only solution is to delete the # 124 on the laundry tag leaving the other one if you prefer that. I think I would prefer to leave as is because we shouldn't leave out info to please the renderer?</p>
<p>The renderer (in the link above the openstreetmap.org mapnik version) does not display the laundry tag (It also does not display other tags such as a bench I think) All the renderers have a different priority with types of things they display and how it is displayed depending on their particular target users.</p>
<p>But be assured that you data is valued elsewhere. The maps would be too cluttered if everything was displayed on the map. It would be ideal if the renderer was able to work out that 2 # 124's on the same building and it was unnecessary to display both and choose to use just one of them but it seems not clever enough yet.</p>
<p>There is another reason that the map may not display immediately something that you have edited as a good explanation is here <a href="https://help.openstreetmap.org/questions/178/how-often-does-the-main-mapnik-map-get-updated">How often does the main (mapnik) map get updated</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Oct '13, 14:56</strong></p>
<img src="https://secure.gravatar.com/avatar/e5674dd96938593e0af5130dfffe0f90?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nevw&#39;s gravatar image" />
<p><span>nevw</span><br />
<span class="score" title="9843 reputation points"><span>9.8k</span></span><span title="26 badges"><span class="badge1">●</span><span class="badgecount">26</span></span><span title="90 badges"><span class="silver">●</span><span class="badgecount">90</span></span><span title="178 badges"><span class="bronze">●</span><span class="badgecount">178</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nevw has 32 accepted answers">9%</span></p>
</div>
</div>
<div id="comments-container-26958" class="comments-container">
<span id="26959"></span>
<div id="comment-26959" class="comment">
<div id="post-26959-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks!</p>
<p>I understand that OSM is still under development, and that many people have to discuss it to find the best compromise. However this map has become far more interesting since I am an editor now. I would like to transport this interesting part to the rest of us. They see most things only when they text-search for them, and only one by one instead of a collection of pointers on the map (like you have when looking for errors clicking on "Map Notes"). And how do they know, that a green dot is a tree? Or that a second house number is a shop/business?</p>
<p>Again, thanks, and have a nice day</p>
</div>
<div id="comment-26959-info" class="comment-info">
<span class="comment-age">(05 Oct '13, 17:02)</span> <span class="comment-user userinfo">C-in-Berlin</span>
</div>
</div>
</div>
<div id="comment-tools-26958" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26958-form-container" class="comment-form-container">
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


+++
type = "question"
title = "Overpass API: querynodes created by a user"
description = '''How can I query for nodes created by a certain user. I found an example for a query on object which were last modified by a certain user but not for the creator.'''
date = "2015-03-31T10:57:00Z"
lastmod = "2015-03-31T12:19:00Z"
weight = 42059
keywords = [ "overpass", "creation" ]
aliases = [ "/questions/42059" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Overpass API: querynodes created by a user](/questions/42059/overpass-api-querynodes-created-by-a-user)

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
<span id="post-42059-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42059-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-42059-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How can I query for nodes created by a certain user. I found an example for a query on object which were last modified by a certain user but not for the creator.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-creation" rel="tag" title="see questions tagged &#39;creation&#39;">creation</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Mar '15, 10:57</strong></p>
<img src="https://secure.gravatar.com/avatar/7ef3a3c25492438c9f0e5a548a36fa07?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ogmios&#39;s gravatar image" />
<p><span>Ogmios</span><br />
<span class="score" title="766 reputation points">766</span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ogmios has 3 accepted answers">25%</span></p>
</div>
</div>
<div id="comments-container-42059" class="comments-container">
&#10;</div>
<div id="comment-tools-42059" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42059-form-container" class="comment-form-container">
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

<span id="42060"></span>

<div id="answer-container-42060" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-42060-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42060-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-42060-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Ogmios has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Unfortunately, that's not possible as of today, i.e. you cannot query for all version 1 objects and then filter that set of objects for a given user.</p>
<p>At this time, you can only query for data at a given timestamp, or how the data changed since a timestamp. Also note that previous object versions are only available up to the first ODbL planet in September 2012. Any object version created before that time wouldn't be available in Overpass API.</p>
<p>If you like you can create a new issue for your requirement on <a href="https://github.com/drolbr/Overpass-API/issues">Github</a>.</p>
<p>In conclusion, the information you're looking for is probably only available in a full history dump.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Mar '15, 11:28</strong></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmd has 44 accepted answers">37%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>31 Mar '15, 11:34</strong> </span></p>
</div>
</div>
<div id="comments-container-42060" class="comments-container">
<span id="42065"></span>
<div id="comment-42065" class="comment">
<div id="post-42065-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks a lot. This answers my question and gives me some Background knowledge.</p>
</div>
<div id="comment-42065-info" class="comment-info">
<span class="comment-age">(31 Mar '15, 12:19)</span> <span class="comment-user userinfo">Ogmios</span>
</div>
</div>
</div>
<div id="comment-tools-42060" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42060-form-container" class="comment-form-container">
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


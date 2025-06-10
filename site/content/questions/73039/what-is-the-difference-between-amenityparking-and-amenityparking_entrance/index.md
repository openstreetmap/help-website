+++
type = "question"
title = "What is the difference between amenity=parking and amenity=parking_entrance ?"
description = '''What is the difference between amenity=parking and amenity=parking_entrance? Should I use both if I want to map an underground parking garage or just one? How are the tags interpreted by web services that use our data?'''
date = "2020-02-12T21:07:00Z"
lastmod = "2020-02-13T04:11:00Z"
weight = 73039
keywords = [ "tagging", "parking" ]
aliases = [ "/questions/73039" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [What is the difference between amenity=parking and amenity=parking_entrance ?](/questions/73039/what-is-the-difference-between-amenityparking-and-amenityparking_entrance)

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
<span id="post-73039-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73039-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-73039-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>What is the difference between amenity=parking and amenity=parking_entrance? Should I use both if I want to map an underground parking garage or just one? How are the tags interpreted by web services that use our data?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-parking" rel="tag" title="see questions tagged &#39;parking&#39;">parking</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Feb '20, 21:07</strong></p>
<img src="https://secure.gravatar.com/avatar/3f398da25e1453020723c955139a4ec7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ALE&#39;s gravatar image" />
<p><span>ALE</span><br />
<span class="score" title="1943 reputation points"><span>1.9k</span></span><span title="41 badges"><span class="badge1">●</span><span class="badgecount">41</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ALE has 4 accepted answers">14%</span></p>
</div>
</div>
<div id="comments-container-73039" class="comments-container">
&#10;</div>
<div id="comment-tools-73039" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73039-form-container" class="comment-form-container">
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

<span id="73040"></span>

<div id="answer-container-73040" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73040-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73040-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-73040-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The <code>amenity=parking</code> tag is usually used on a closed way to describe the extents of a parking area, although use on a node is acceptable, especially if imagery isn't available.</p>
<p>The <code>amenity=parking_entrance</code> tag is normally used on entrances to underground or multistory facilities, often where it is not practical to map the extents.</p>
<p>Both tags should be able to coexist for a parking facility, with the entrance tag on a node on the perimeter of the main parking area way.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Feb '20, 21:59</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-73040" class="comments-container">
<span id="73042"></span>
<div id="comment-73042" class="comment">
<div id="post-73042-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, I've often seen a highway=service dead-ending into the side of a building, with the intersection node tagged <strong>amenity=parking</strong>. I've generally been inclined to retag these <strong>amenity=parking_entrance</strong>.</p>
</div>
<div id="comment-73042-info" class="comment-info">
<span class="comment-age">(13 Feb '20, 04:11)</span> <span class="comment-user userinfo">jmapb</span>
</div>
</div>
</div>
<div id="comment-tools-73040" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73040-form-container" class="comment-form-container">
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


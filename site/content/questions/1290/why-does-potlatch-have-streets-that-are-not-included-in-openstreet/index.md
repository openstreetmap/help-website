+++
type = "question"
title = "[closed] Why does Potlatch have streets that are not included in  OpenStreet?"
description = '''I&#x27;m trying to use OpenStreets to map a relay in north Sun City Arizona, USA. Open Streets shows open areas for communities mapped in Potlatch. How can I get these streets to show in OpenStreets? These are previously mapped streets (not by me).'''
date = "2010-10-23T18:57:00Z"
lastmod = "2010-11-02T19:54:00Z"
weight = 1290
keywords = [ "potlatch" ]
aliases = [ "/questions/1290" ]
osqa_answers = 7
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] Why does Potlatch have streets that are not included in OpenStreet?](/questions/1290/why-does-potlatch-have-streets-that-are-not-included-in-openstreet)

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
<span id="post-1290-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1290-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-1290-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to use OpenStreets to map a relay in north Sun City Arizona, USA. Open Streets shows open areas for communities mapped in Potlatch. How can I get these streets to show in OpenStreets? These are previously mapped streets (not by me).</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-potlatch" rel="tag" title="see questions tagged &#39;potlatch&#39;">potlatch</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Oct '10, 18:57</strong></p>
<img src="https://secure.gravatar.com/avatar/74e3bf6ecd59167708aa603567a420e4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KA7AOK&#39;s gravatar image" />
<p><span>KA7AOK</span><br />
<span class="score" title="12 reputation points">12</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KA7AOK has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>03 Nov '10, 09:00</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/dee41dcf0aa0c08cf6b0eb935b7504b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TomH&#39;s gravatar image" />
<p><span>TomH ♦♦</span><br />
<span class="score" title="3325 reputation points"><span>3.3k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="43 badges"><span class="bronze">●</span><span class="badgecount">43</span></span></p>
</div>
</div>
<div id="comments-container-1290" class="comments-container">
&#10;</div>
<div id="comment-tools-1290" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1290-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Other - this has turned into a discussion rather than a Q&A." by TomH 03 Nov '10, 09:00

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

7 Answers:

</div>

</div>

<span id="1291"></span>

<div id="answer-container-1291" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1291-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1291-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-1291-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>By OpenStreet i presume you mean the map rendering on the main page. That map is a representation of the data in the database. For more info on how the data is represented in the database see <a href="http://wiki.openstreetmap.org/wiki/Beginners_Guide_1.3">the beginners guide</a>.</p>
<p>It is hard to understand exactly what is the problem when you do not have an example. It could be that there are some ways in the database without tags that the map renderer renders on like a highway=* tag. Or the ways might have been added recently and the map has not rendered the new changes yet. Or you might accidentally have switched on deleted ways in potlatch (hotkey 'd') that displays ways that have been deleted from the database.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Oct '10, 19:31</strong></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gnonthgol has 57 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-1291" class="comments-container">
&#10;</div>
<div id="comment-tools-1291" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1291-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="1409"></span>

<div id="answer-container-1409" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1409-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1409-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-1409-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>A pointer to the location might help us to see what the problem might be.</p>
<p>On the main map, if you zoom in to the problem area, then click "permalink" at the bottom right, that will change the URL in the browser address bar to point to the map that you're looking at. If you share that here, people can have a look at the same map as you and suggest what to do.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Nov '10, 21:22</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-1409" class="comments-container">
&#10;</div>
<div id="comment-tools-1409" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1409-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="1411"></span>

<div id="answer-container-1411" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1411-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1411-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-1411-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Following is the link to the page I am referring to. On the southeast side of the main highway (AZ303) there is a development in Potlatch that is not portrayed in OpenStreet.</p>
<p><a href="http://www.openstreetmap.org/?lat=33.7009&amp;lon=-112.32723&amp;zoom=15&amp;layers=M">http://www.openstreetmap.org/?lat=33.7009&amp;lon=-112.32723&amp;zoom=15&amp;layers=M</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Nov '10, 00:14</strong></p>
<img src="https://secure.gravatar.com/avatar/74e3bf6ecd59167708aa603567a420e4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KA7AOK&#39;s gravatar image" />
<p><span>KA7AOK</span><br />
<span class="score" title="12 reputation points">12</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KA7AOK has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-1411" class="comments-container">
<span id="1414"></span>
<div id="comment-1414" class="comment">
<div id="post-1414-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Are you viewing any aerial imagery in Potlatch? Specifically the Yahoo aerial imagery? In that area it seems to show some streets that look rather like they are mapped in Potlatch, but they are actually not.</p>
<p>You would have to trace over these streets in Potlatch to map them, then tag them appropriately. Then they will show up on the map.</p>
</div>
<div id="comment-1414-info" class="comment-info">
<span class="comment-age">(02 Nov '10, 04:21)</span> <span class="comment-user userinfo">Vclaw</span>
</div>
</div>
</div>
<div id="comment-tools-1411" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1411-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="1412"></span>

<div id="answer-container-1412" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1412-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1412-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-1412-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Curious - I don't see anything there in Potlatch that isn't there on the main map. You're talking about something between the AZ303 and "Hanson Aggregates Arizona inc" presumably?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Nov '10, 00:44</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-1412" class="comments-container">
&#10;</div>
<div id="comment-tools-1412" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1412-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="1413"></span>

<div id="answer-container-1413" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1413-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1413-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-1413-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is a development just south (and continuing east) of where the AZ303 turns north</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Nov '10, 01:10</strong></p>
<img src="https://secure.gravatar.com/avatar/74e3bf6ecd59167708aa603567a420e4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KA7AOK&#39;s gravatar image" />
<p><span>KA7AOK</span><br />
<span class="score" title="12 reputation points">12</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KA7AOK has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-1413" class="comments-container">
&#10;</div>
<div id="comment-tools-1413" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1413-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="1422"></span>

<div id="answer-container-1422" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1422-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1422-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-1422-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Still can't see it I'm afraid...</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Nov '10, 16:50</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-1422" class="comments-container">
&#10;</div>
<div id="comment-tools-1422" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1422-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="1424"></span>

<div id="answer-container-1424" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1424-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1424-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-1424-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The roads identifying it (in Potlatch) are N. El Mirage on the west side and W. Pinnacle Peak Road on the north. The other 2 roads (identified in Google Maps but not in Potlatch) are Williams Road on the south and N. 117 Ave on the east. If you cannot see it, lets just drop the subject.</p>
<p>Arnold</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Nov '10, 18:01</strong></p>
<img src="https://secure.gravatar.com/avatar/74e3bf6ecd59167708aa603567a420e4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KA7AOK&#39;s gravatar image" />
<p><span>KA7AOK</span><br />
<span class="score" title="12 reputation points">12</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KA7AOK has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-1424" class="comments-container">
<span id="1426"></span>
<div id="comment-1426" class="comment">
<div id="post-1426-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I Think it will be better when you try to solve this issue at the right forum at <a href="http://forum.openstreetmap.org">forum.openstreetmap.org</a> because here this is more a FAQ system rather than a forum.</p>
<p>Any "sysop" to close or delete this thread?</p>
</div>
<div id="comment-1426-info" class="comment-info">
<span class="comment-age">(02 Nov '10, 19:54)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
</div>
<div id="comment-tools-1424" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1424-form-container" class="comment-form-container">
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


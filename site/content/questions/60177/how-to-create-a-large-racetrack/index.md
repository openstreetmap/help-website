+++
type = "question"
title = "How to create a large racetrack"
description = '''In the part of Canada where I live most every town has a rodeo grounds, and many of those also have a large race track. I found one track at the Calgary Stampede that renders very nice as a representation of the track on the OSM map as an oval.  https://www.openstreetmap.org/#map=16/51.0333/-114.0526...'''
date = "2017-10-19T03:14:00Z"
lastmod = "2017-10-21T03:36:00Z"
weight = 60177
keywords = [ "sports_centre", "sport", "howto" ]
aliases = [ "/questions/60177" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to create a large racetrack](/questions/60177/how-to-create-a-large-racetrack)

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
<span id="post-60177-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60177-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-60177-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In the part of Canada where I live most every town has a rodeo grounds, and many of those also have a large race track. I found one track at the Calgary Stampede that renders very nice as a representation of the track on the OSM map as an oval.</p>
<p><a href="https://www.openstreetmap.org/#map=16/51.0333/-114.0526">https://www.openstreetmap.org/#map=16/51.0333/-114.0526</a></p>
<p>I've tried to play with that one to figure out how two lines render with a shaded area between them. I've tried a few things, but many of them either fill in the oval or do not show up on the map at all. I know there are lots of other sports areas with ovals that could be done the same way, but how do you do it? Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-sports_centre" rel="tag" title="see questions tagged &#39;sports_centre&#39;">sports_centre</span> <span class="post-tag tag-link-sport" rel="tag" title="see questions tagged &#39;sport&#39;">sport</span> <span class="post-tag tag-link-howto" rel="tag" title="see questions tagged &#39;howto&#39;">howto</span>
</div>
<div id="question-controls" class="post-controls">
<div class="community-wiki">
This question is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Oct '17, 03:14</strong></p>
<img src="https://secure.gravatar.com/avatar/2f31d82b2464a51ec9ad6c87744a79b3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tjstone&#39;s gravatar image" />
<p><span>tjstone</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tjstone has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-60177" class="comments-container">
<span id="60183"></span>
<div id="comment-60183" class="comment">
<div id="post-60183-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>BTW, the Calgary Stampede relation was improperly tagged as leisure=park. I have changed that tag to leisure=track so it may look slightly different once map tiles re-render.</p>
</div>
<div id="comment-60183-info" class="comment-info">
<span class="comment-age">(19 Oct '17, 20:17)</span> <span class="comment-user userinfo">neuhausr</span>
</div>
</div>
</div>
<div id="comment-tools-60177" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60177-form-container" class="comment-form-container">
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

<span id="60178"></span>

<div id="answer-container-60178" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60178-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60178-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-60178-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As explained on the <a href="https://wiki.openstreetmap.org/wiki/Tag:leisure%3Dtrack">leisure=track</a> page, you have to use a <a href="https://wiki.openstreetmap.org/wiki/Relation:multipolygon">multipolygon-relation</a> for that.</p>
<p>The accepted answer of <a href="/questions/22542/how-do-i-map-an-island-in-a-lake-using-id-editor-and-the-multipolygon-tag">this question</a> explains how to do that in the iD-editor.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Oct '17, 04:17</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-60178" class="comments-container">
&#10;</div>
<div id="comment-tools-60178" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60178-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="60187"></span>

<div id="answer-container-60187" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60187-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60187-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-60187-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Thanks for your help! I wasn't having much luck searching for an answer. I've now made about four of these and have quite a few more to go. Thanks!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Oct '17, 21:55</strong></p>
<img src="https://secure.gravatar.com/avatar/2f31d82b2464a51ec9ad6c87744a79b3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tjstone&#39;s gravatar image" />
<p><span>tjstone</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tjstone has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-60187" class="comments-container">
<span id="60199"></span>
<div id="comment-60199" class="comment">
<div id="post-60199-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi <a href="https://help.openstreetmap.org/users/14330/tjstone">@tjstone</a>, if you want to respond to an answer it is preferable to use the <code>add new comment</code> button instead of providing a new answer to your own question.</p>
</div>
<div id="comment-60199-info" class="comment-info">
<span class="comment-age">(21 Oct '17, 03:36)</span> <span class="comment-user userinfo">keithonearth</span>
</div>
</div>
</div>
<div id="comment-tools-60187" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60187-form-container" class="comment-form-container">
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


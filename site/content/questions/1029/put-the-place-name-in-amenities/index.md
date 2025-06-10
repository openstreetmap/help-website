+++
type = "question"
title = "Put the place name in amenities ?"
description = '''Does it make sense to copy the place name in amenities ? For instance, a townhall tagged &quot;amenity=townhall&quot; + &quot;name=Worcester City Hall&quot;. Or a train station building tagged with &quot;name=&quot;Worcester station&quot;. Or the post office with &quot;name=&quot;Worcester post office&quot;. Or &quot;amenity=police&quot; + &quot;name=Worcester po...'''
date = "2010-10-06T17:53:00Z"
lastmod = "2010-10-07T10:55:00Z"
weight = 1029
keywords = [ "amenity", "name" ]
aliases = [ "/questions/1029" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Put the place name in amenities ?](/questions/1029/put-the-place-name-in-amenities)

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
<span id="post-1029-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1029-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-1029-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Does it make sense to copy the place name in amenities ? For instance, a townhall tagged "amenity=townhall" + "name=Worcester City Hall". Or a train station building tagged with "name="Worcester station". Or the post office with "name="Worcester post office". Or "amenity=police" + "name=Worcester police station". Then "Worcester barkery", "Worcester pub", etc...</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-amenity" rel="tag" title="see questions tagged &#39;amenity&#39;">amenity</span> <span class="post-tag tag-link-name" rel="tag" title="see questions tagged &#39;name&#39;">name</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Oct '10, 17:53</strong></p>
<img src="https://secure.gravatar.com/avatar/0e92f2d89853fd4e04c4b40a921e519b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pieren&#39;s gravatar image" />
<p><span>Pieren</span><br />
<span class="score" title="9847 reputation points"><span>9.8k</span></span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="157 badges"><span class="bronze">●</span><span class="badgecount">157</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pieren has 34 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-1029" class="comments-container">
&#10;</div>
<div id="comment-tools-1029" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1029-form-container" class="comment-form-container">
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

<span id="1031"></span>

<div id="answer-container-1031" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1031-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1031-score" class="post-score" title="current number of votes">
7
</div>
<span id="post-1031-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><strong>If</strong> the official name of the train station is "Worcester station" the <code>name</code> tag should reflect that. However if the official name is "Shrub hill" then you shouldn't add either "worchester" nor "station" to the name.</p>
<p>Either way the fact that it is a train station should be expressed through the tag <code>railway=station</code> and the fact that it is in Worcester can be inferred from the boundary way (or relation) of Worcester.</p>
<p>As for the bakery or the pub: If the name is "Worcester pub" then use that in the <code>name</code> tag. If it is "The prancing pony" then use that.</p>
<p>I'm not sure what the naming scheme for police stations in your country is but around here police station might have a name like "Worcester Police Station".</p>
<p>However there might be a second police station in town with the name "Midlands Borough Police Office" which not a 'regular' police station but the superintendence of all the police force in the Midlands.</p>
<p>If Worcester is big enough it might have more then one police station, say "East Worcester Police Station" and "West Worcester Police Station".</p>
<p>Perhaps, and I'm really out on a stretch there, there might be a third small police station in town called "Friar Constabulary" for historic reason. That station should be tagged with <code>amenity=police</code>, <code>name=Friar Constabulary</code>. The fact that it is in Worcester can be infered from its position after all.</p>
<p>As a summary: Use the official name in the name tag without adding words for "this is in Worchester" or "this is a pub/police station/whatever".</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Oct '10, 18:17</strong></p>
<img src="https://secure.gravatar.com/avatar/465f344e31e8ba1be0e0401414815db0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="petschge&#39;s gravatar image" />
<p><span>petschge</span><br />
<span class="score" title="8279 reputation points"><span>8.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="73 badges"><span class="silver">●</span><span class="badgecount">73</span></span><span title="98 badges"><span class="bronze">●</span><span class="badgecount">98</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="petschge has 29 accepted answers">21%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Oct '10, 09:30</strong> </span></p>
</div>
</div>
<div id="comments-container-1031" class="comments-container">
<span id="1044"></span>
<div id="comment-1044" class="comment">
<div id="post-1044-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Expanded to address comment and removed comment with approval of the author</p>
</div>
<div id="comment-1044-info" class="comment-info">
<span class="comment-age">(07 Oct '10, 09:32)</span> <span class="comment-user userinfo">petschge</span>
</div>
</div>
<span id="1048"></span>
<div id="comment-1048" class="comment">
<div id="post-1048-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>For what it's worth (a practical real-world example!) there are two stations, called Worcester Shrub Hill and Worcester Foregate Street. These are the official National Rail names for them, used on all signage, displays, timetables and publicity, so they're what we use in OSM.</p>
</div>
<div id="comment-1048-info" class="comment-info">
<span class="comment-age">(07 Oct '10, 10:55)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
</div>
<div id="comment-tools-1031" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1031-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="1030"></span>

<div id="answer-container-1030" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1030-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1030-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-1030-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I would say Yes, <strong>if</strong> that is that is how the amenity is officially known or is signed on-the-ground. A city may have more than one train station, post office or police station, so the distinction can be important.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Oct '10, 18:07</strong></p>
<img src="https://secure.gravatar.com/avatar/f61876d1f1d2de794259119cdd596316?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GrahamS&#39;s gravatar image" />
<p><span>GrahamS</span><br />
<span class="score" title="3635 reputation points"><span>3.6k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="45 badges"><span class="silver">●</span><span class="badgecount">45</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GrahamS has 7 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-1030" class="comments-container">
&#10;</div>
<div id="comment-tools-1030" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1030-form-container" class="comment-form-container">
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


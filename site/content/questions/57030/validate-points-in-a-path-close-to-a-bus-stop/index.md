+++
type = "question"
title = "Validate points in a path close to a bus stop"
description = '''Hi guys  I&#x27;m a newbie so excuse me if my question could sound stupid... I have paths stored. for each path I have point where a user stopped. I need to know if each of that stop point is close to a bus stop. But... they could be quite a lot, so I need to use a single call to overpass api to retreive...'''
date = "2017-07-12T09:58:00Z"
lastmod = "2017-07-13T09:49:00Z"
weight = 57030
keywords = [ "overpass", "overpass-turbo", "bus", "query" ]
aliases = [ "/questions/57030" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Validate points in a path close to a bus stop](/questions/57030/validate-points-in-a-path-close-to-a-bus-stop)

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
<span id="post-57030-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57030-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-57030-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi guys I'm a newbie so excuse me if my question could sound stupid... I have paths stored. for each path I have point where a user stopped. I need to know if each of that stop point is close to a bus stop. But... they could be quite a lot, so I need to use a single call to overpass api to retreive that validation and I need to receive the validation sapareted for each point (to know which of them is validated and which is not...). I need halp please!!! cheers Gian Luca</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-bus" rel="tag" title="see questions tagged &#39;bus&#39;">bus</span> <span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Jul '17, 09:58</strong></p>
<img src="https://secure.gravatar.com/avatar/4e5a61ae4d679023b3890f75a1aa811d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="boka70&#39;s gravatar image" />
<p><span>boka70</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="boka70 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Jul '17, 10:02</strong> </span></p>
</div>
</div>
<div id="comments-container-57030" class="comments-container">
&#10;</div>
<div id="comment-tools-57030" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57030-form-container" class="comment-form-container">
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

<span id="57050"></span>

<div id="answer-container-57050" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-57050-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57050-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-57050-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are some details missing in your question (for example how large the area is that your paths cover and so on), but ok: I would suggest loading your data in to a spatially enabled database (for example Postgresql with postgis), then querying the Overpass-api for all stops in the area (or extracting them from an OSM planet file, depending on how large the area is). Then you should import the stop nodes in to the database.</p>
<p>Once you've done all that (which includes figuring out the database schema you want to use etc), you can use spatial queries to find for example all of your user stop position that are within a pre-defined distance to a stop and so on.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Jul '17, 09:49</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-57050" class="comments-container">
&#10;</div>
<div id="comment-tools-57050" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57050-form-container" class="comment-form-container">
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


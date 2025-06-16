+++
type = "question"
title = "How to extract ids of all the objects in an osm file and show them in a list?"
description = '''Hi everyone, I have created around 100 protected areas in Iran over last few months, in order to complete the wiki page regarding these areas, I want to show them in a list with their name and OSM ids in the wiki page. Is there a way to extract Ids of objects in a .osm file? or even better is there ...'''
date = "2016-09-13T08:49:00Z"
lastmod = "2016-09-14T14:23:00Z"
weight = 52025
keywords = [ "query", "extracts", "id" ]
aliases = [ "/questions/52025" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to extract ids of all the objects in an osm file and show them in a list?](/questions/52025/how-to-extract-ids-of-all-the-objects-in-an-osm-file-and-show-them-in-a-list)

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
<span id="post-52025-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52025-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-52025-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi everyone,</p>
<p>I have created around 100 protected areas in Iran over last few months, in order to complete the wiki page regarding these areas, I want to show them in a list with their name and OSM ids in the wiki page. Is there a way to extract Ids of objects in a .osm file? or even better is there a query which can be used to list object's Id based on a specific search criteria?</p>
<p>By the way I have tried Spatial Manger it shows all the tags except Ids.</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span> <span class="post-tag tag-link-extracts" rel="tag" title="see questions tagged &#39;extracts&#39;">extracts</span> <span class="post-tag tag-link-id" rel="tag" title="see questions tagged &#39;id&#39;">id</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Sep '16, 08:49</strong></p>
<img src="https://secure.gravatar.com/avatar/f7da215f2999ecac8d169e32e2c3502e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Adib%20Yz&#39;s gravatar image" />
<p><span>Adib Yz</span><br />
<span class="score" title="291 reputation points">291</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Adib Yz has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-52025" class="comments-container">
&#10;</div>
<div id="comment-tools-52025" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52025-form-container" class="comment-form-container">
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

<span id="52034"></span>

<div id="answer-container-52034" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52034-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52034-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-52034-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Adib Yz has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Use <a href="http://overpass-turbo.eu/">overpass turbo</a> and enter “boundary=protected_area in Iran” in the wizard. You'll have the data displayed on a map, and the corresponding json on the "data" tab. You can export that to a format of your liking.</p>
<p>Optionally, replace the "print results" section with "out ids;" so that only ids are returned (ignore the "repair query" suggestion). That might make parsing the data easier.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Sep '16, 11:09</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-52034" class="comments-container">
<span id="52043"></span>
<div id="comment-52043" class="comment">
<div id="post-52043-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Also, avoid linking to object id's whenever possible. See <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Permanent_ID">https://wiki.openstreetmap.org/wiki/Overpass_API/Permanent_ID</a></p>
</div>
<div id="comment-52043-info" class="comment-info">
<span class="comment-age">(14 Sep '16, 14:23)</span> <span class="comment-user userinfo">joost schouppe</span>
</div>
</div>
</div>
<div id="comment-tools-52034" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52034-form-container" class="comment-form-container">
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


+++
type = "question"
title = "Opentopomap doesn&#x27;t update anymore?"
description = '''Changes made in openstreetmap seem not to appear any more in Opentopomap. I made many additions to the map in Thailand. Initially they were updated quite fast. Now the service seems to have come to a stop. Also additions I made in Switzerland do not appear in Opentopomap. In Openstreetmap all my add...'''
date = "2016-08-20T08:39:00Z"
lastmod = "2022-09-06T21:04:00Z"
weight = 51558
keywords = [ "opentopomap", "update" ]
aliases = [ "/questions/51558" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Opentopomap doesn't update anymore?](/questions/51558/opentopomap-doesnt-update-anymore)

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
<span id="post-51558-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51558-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-51558-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Changes made in openstreetmap seem not to appear any more in Opentopomap. I made many additions to the map in Thailand. Initially they were updated quite fast. Now the service seems to have come to a stop. Also additions I made in Switzerland do not appear in Opentopomap. In Openstreetmap all my additions are visible. I really like Opentopomap and hope to see my additions in Opentopomap soon again. I did clear the browsing data and did refresh the page, but this didn't help.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-opentopomap" rel="tag" title="see questions tagged &#39;opentopomap&#39;">opentopomap</span> <span class="post-tag tag-link-update" rel="tag" title="see questions tagged &#39;update&#39;">update</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Aug '16, 08:39</strong></p>
<img src="https://secure.gravatar.com/avatar/7c976e0e6ac512de8b5271d0838906a0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kellerk&#39;s gravatar image" />
<p><span>kellerk</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kellerk has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-51558" class="comments-container">
<span id="51559"></span>
<div id="comment-51559" class="comment">
<div id="post-51559-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>and how long ago are your changes?</p>
</div>
<div id="comment-51559-info" class="comment-info">
<span class="comment-age">(20 Aug '16, 08:54)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="51564"></span>
<div id="comment-51564" class="comment">
<div id="post-51564-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>changes were made one month ago</p>
</div>
<div id="comment-51564-info" class="comment-info">
<span class="comment-age">(20 Aug '16, 10:20)</span> <span class="comment-user userinfo">kellerk</span>
</div>
</div>
</div>
<div id="comment-tools-51558" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51558-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="51654"></span>

<div id="answer-container-51654" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-51654-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51654-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-51654-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OpenTopoMap doesn't update the database any more. The number of users is exploding and our hardware needs a upgrade. Currently the OSM database needs 495 GB and the contour database is 505 GB. So our 1,1 TB PCIe SSD is completely full! Our normal HDD for the tiles is full, too. We get a hardware update in the next time, our University already kindly granted our request. But this doesn't solve the database issue, only the tile disk space issue. So I need to find a way to reduce the contours database by several GB. I could need help with the development of a program to delete contour lines that are very close to each other. (You don't need contour lines every 10 m in the Himalaya.)</p>
<p>During re-installation of our main server we plan to serve the tiles from our second server, but without rendering. So be prepared, there will be problems in the next weeks or months - that's the problem with a hobby projects of one single developer, who has also more than one hobby. ;-)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Aug '16, 20:41</strong></p>
<img src="https://secure.gravatar.com/avatar/5167615b33e9e8d73aa58fd0eacedc80?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="derstefan&#39;s gravatar image" />
<p><span>derstefan</span><br />
<span class="score" title="193 reputation points">193</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="derstefan has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-51654" class="comments-container">
&#10;</div>
<div id="comment-tools-51654" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51654-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="51560"></span>

<div id="answer-container-51560" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-51560-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51560-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-51560-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You need to contact the people creating and operating OpenTopoMap see <a href="https://opentopomap.org/credits">https://opentopomap.org/credits</a> Nobody else will be able to do anything about hiccups in a third party service.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Aug '16, 08:56</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-51560" class="comments-container">
<span id="51575"></span>
<div id="comment-51575" class="comment">
<div id="post-51575-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>... see <a href="https://wiki.openstreetmap.org/wiki/OpenTopoMap#Contact">https://wiki.openstreetmap.org/wiki/OpenTopoMap#Contact</a> for their OSM names (an osm message would be a contact option too)</p>
</div>
<div id="comment-51575-info" class="comment-info">
<span class="comment-age">(21 Aug '16, 01:06)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-51560" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51560-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="85573"></span>

<div id="answer-container-85573" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-85573-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85573-score" class="post-score" title="current number of votes">
-2
</div>
<span id="post-85573-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Now we are in 2022, is it fixed ?</p>
<p>I also did some updates which are not reflected on opentopomap. How often the maps are refreshed? Is it the same delay on every zoom level ?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Sep '22, 20:53</strong></p>
<img src="https://secure.gravatar.com/avatar/a42a7ffa2a33118080748ca868ed74a6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cbeyls&#39;s gravatar image" />
<p><span>cbeyls</span><br />
<span class="score" title="-1 reputation points">-1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cbeyls has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Sep '22, 20:56</strong> </span></p>
</div>
</div>
<div id="comments-container-85573" class="comments-container">
<span id="85574"></span>
<div id="comment-85574" class="comment">
<div id="post-85574-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Please fo not ask questions in an answer.</p>
</div>
<div id="comment-85574-info" class="comment-info">
<span class="comment-age">(06 Sep '22, 21:04)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-85573" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85573-form-container" class="comment-form-container">
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


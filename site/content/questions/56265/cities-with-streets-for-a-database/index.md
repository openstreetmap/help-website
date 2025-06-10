+++
type = "question"
title = "Cities with streets for a database"
description = '''Hi, I am trying to create a database with cities and their streets. Could you write down the best way to do that? Unfortunately a lot of the questions are quite confusing. (I already have my country&#x27;s osm data.) Thanks!'''
date = "2017-05-23T13:25:00Z"
lastmod = "2017-05-24T15:15:00Z"
weight = 56265
keywords = [ "city", "street", "list" ]
aliases = [ "/questions/56265" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Cities with streets for a database](/questions/56265/cities-with-streets-for-a-database)

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
<span id="post-56265-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56265-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-56265-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I am trying to create a database with cities and their streets.</p>
<p>Could you write down the best way to do that? Unfortunately a lot of the questions are quite confusing. (I already have my country's osm data.)</p>
<p>Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-city" rel="tag" title="see questions tagged &#39;city&#39;">city</span> <span class="post-tag tag-link-street" rel="tag" title="see questions tagged &#39;street&#39;">street</span> <span class="post-tag tag-link-list" rel="tag" title="see questions tagged &#39;list&#39;">list</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 May '17, 13:25</strong></p>
<img src="https://secure.gravatar.com/avatar/5f581042bfbdb7a3413915d78993ea81?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mutantChipmunk1&#39;s gravatar image" />
<p><span>mutantChipmunk1</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mutantChipmunk1 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-56265" class="comments-container">
<span id="56266"></span>
<div id="comment-56266" class="comment">
<div id="post-56266-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I think you need to clarify this: do you want a listing of all street names by each city? By city do you mean large cities or any centre of population? Do you just want streets in urban areas or are rural roads OK too?</p>
</div>
<div id="comment-56266-info" class="comment-info">
<span class="comment-age">(23 May '17, 14:35)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="56267"></span>
<div id="comment-56267" class="comment">
<div id="post-56267-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, you are right. So i will try to specify my project. Actually I would like to keep all data from the roads file. If a street or road is in a city I would want to connect them somehow in my database. Here is my proplem, I cant seem to find the relation between the streets/roads and the cities in the downloaded file. And I will be needing the GPS coordinates of the element in the roads file, I already know that I need the points of the roads to do so. (I would like to visualize a streetmap.) Thank you for your help!</p>
</div>
<div id="comment-56267-info" class="comment-info">
<span class="comment-age">(23 May '17, 14:52)</span> <span class="comment-user userinfo">mutantChipmunk1</span>
</div>
</div>
</div>
<div id="comment-tools-56265" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56265-form-container" class="comment-form-container">
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

<span id="56268"></span>

<div id="answer-container-56268" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56268-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56268-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-56268-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I suspect, given that you seem to be rather stuck early on, that your best approach is to use an "off the shelf" solution in the form of an osm2pgsql schema database and import your country data in to that.</p>
<p>That will provide you with the geometries of all the streets and administrative borders (if available in your country) which you can then use however you wish.</p>
<p>See <a href="https://switch2osm.org/serving-tiles/">https://switch2osm.org/serving-tiles/</a> (while these are instructions for a tile server, you can naturally use the data in the DB any way you see fit).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 May '17, 16:04</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-56268" class="comments-container">
<span id="56288"></span>
<div id="comment-56288" class="comment">
<div id="post-56288-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Okay, I have it in my database, I used osm2pgsql and opened my database in pgAndmin4. But I just cannot find the connection between the cities and the streets. I have my tables, planet_osm_line, planet_osm_nodes, etc. I can see that a street contains nodes, and from the nodes I will get the coordinates. As a result I would need just a csv file or something like that.</p>
</div>
<div id="comment-56288-info" class="comment-info">
<span class="comment-age">(24 May '17, 15:15)</span> <span class="comment-user userinfo">mutantChipmunk1</span>
</div>
</div>
</div>
<div id="comment-tools-56268" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56268-form-container" class="comment-form-container">
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


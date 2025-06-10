+++
type = "question"
title = "Need to create Graph of a certain city with nodes being places and edges as roads."
description = '''My group is creating an application for our college minor project. In this project we&#x27;re going to find nearest users to a specified user. To do this, I am thinking of using the OSM data points and use it to populate a graph of the specified user&#x27;s city and then plot all the users in that location. I...'''
date = "2016-05-15T11:31:00Z"
lastmod = "2017-06-08T13:43:00Z"
weight = 49699
keywords = [ "asp.net" ]
aliases = [ "/questions/49699" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Need to create Graph of a certain city with nodes being places and edges as roads.](/questions/49699/need-to-create-graph-of-a-certain-city-with-nodes-being-places-and-edges-as-roads)

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
<span id="post-49699-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49699-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-49699-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>My group is creating an application for our college minor project. In this project we're going to find nearest users to a specified user. To do this, I am thinking of using the OSM data points and use it to populate a graph of the specified user's city and then plot all the users in that location. I dont need tiling as, i dont need to display the map. I am just going to use the OSM data points to calculate who is the nearest and use it. OSM doesn't have any good documentation of using it with C# ASP.NET. All i could find were some libraries with no or very few documentation. I found OSMSharp to be on the wiki page of OSM.</p>
<p>As It is already in the headings, i am only considering which users are nearest. I want to use Djikstra Algorithm on the populated graph to calculate shortest path(my consideration is only weight of that path).</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-asp.net" rel="tag" title="see questions tagged &#39;asp.net&#39;">asp.net</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 May '16, 11:31</strong></p>
<img src="https://secure.gravatar.com/avatar/eaac69e9a846dbadf2b4eccfffba5c88?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zetaxavier&#39;s gravatar image" />
<p><span>zetaxavier</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zetaxavier has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-49699" class="comments-container">
<span id="49700"></span>
<div id="comment-49700" class="comment">
<div id="post-49700-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Hi zetaxavier, I don’t think that the who’s nearest list is made for external studies, they’re meant for use amongst mappers. So there might be some privacy issues ! I personally will not be glad to find my specs elsewhere; they are just available amongst OSM'rs.</p>
</div>
<div id="comment-49700-info" class="comment-info">
<span class="comment-age">(15 May '16, 12:48)</span> <span class="comment-user userinfo">Hendrikklaas</span>
</div>
</div>
<span id="49702"></span>
<div id="comment-49702" class="comment">
<div id="post-49702-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your concern. But i am following the privacy guidelines here. Every user is given terms and condition. And then after that we're only taking data of the users who are willing to give data.</p>
</div>
<div id="comment-49702-info" class="comment-info">
<span class="comment-age">(15 May '16, 16:13)</span> <span class="comment-user userinfo">zetaxavier</span>
</div>
</div>
</div>
<div id="comment-tools-49699" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49699-form-container" class="comment-form-container">
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

<span id="56532"></span>

<div id="answer-container-56532" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56532-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56532-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-56532-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Sorry I'm little bit late, but you can use this software</p>
<p><a href="https://github.com/rovaniemi/osm-graph-parser">https://github.com/rovaniemi/osm-graph-parser</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Jun '17, 13:43</strong></p>
<img src="https://secure.gravatar.com/avatar/254b7f3976f5e610bd9d2bf9c2d08075?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vanhapanda&#39;s gravatar image" />
<p><span>vanhapanda</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vanhapanda has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-56532" class="comments-container">
&#10;</div>
<div id="comment-tools-56532" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56532-form-container" class="comment-form-container">
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


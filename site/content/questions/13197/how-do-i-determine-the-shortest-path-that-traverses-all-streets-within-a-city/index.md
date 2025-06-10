+++
type = "question"
title = "How do I determine the shortest path that traverses all streets within a city?"
description = '''In order to meet a particular challenge (to run all of Redlands&#x27; city streets—excluding freeways [and ramps] and Redlands property not contiguous to the city center—in the shortest distance and following one unbroken path) I need to determine 1) how many miles of public roads within a particular cit...'''
date = "2012-06-01T18:00:00Z"
lastmod = "2012-06-11T19:45:00Z"
weight = 13197
keywords = [ "city", "streets", "routing", "path" ]
aliases = [ "/questions/13197" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How do I determine the shortest path that traverses all streets within a city?](/questions/13197/how-do-i-determine-the-shortest-path-that-traverses-all-streets-within-a-city)

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
<span id="post-13197-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13197-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-13197-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In order to meet a particular challenge (to run all of Redlands' city streets—excluding freeways [and ramps] and Redlands property not contiguous to the city center—in the shortest distance and following one unbroken path) I need to determine 1) how many miles of public roads within a particular city (Redlands, CA), and 2) the most efficient (shortest number of miles) path for covering the complete distance. The second challenge is likely more difficult than the first, but perhaps there is some software I could access. I want to run all the roads (no freeway on or off ramps, and no private roads). I understand that there will necessarily be some doubling of distance (for all cul-de-sacs), and I expect that some of the roads that cross over outside the city limits may need to be travelled in order to get over to the adjacent road (in the name of minimizing the overall distance). It's like finding the shortest distance to cover all the roads without lifting up the pencil.</p>
<p>Any suggestions where to begin? I'm completely new to OSM and would appreciate finding a tutorial or two for my project.</p>
<p>Thanks for any and all suggestions, Paul</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-city" rel="tag" title="see questions tagged &#39;city&#39;">city</span> <span class="post-tag tag-link-streets" rel="tag" title="see questions tagged &#39;streets&#39;">streets</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span> <span class="post-tag tag-link-path" rel="tag" title="see questions tagged &#39;path&#39;">path</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Jun '12, 18:00</strong></p>
<img src="https://secure.gravatar.com/avatar/461c210f1870b2588ef49b83b4e6b47b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pmbooks&#39;s gravatar image" />
<p><span>pmbooks</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pmbooks has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Jun '12, 18:21</strong> </span></p>
</div>
</div>
<div id="comments-container-13197" class="comments-container">
&#10;</div>
<div id="comment-tools-13197" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13197-form-container" class="comment-form-container">
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

<span id="13262"></span>

<div id="answer-container-13262" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13262-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13262-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-13262-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>GRASS GIS has a travelling saleman implementation, but I don't know if you can apply it to roads. Afaik it takes a point layer and a network layer as input, but you might try and see</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Jun '12, 08:43</strong></p>
<img src="https://secure.gravatar.com/avatar/30b87850d86c99d1c4f1f72c9abaeb52?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="frabron&#39;s gravatar image" />
<p><span>frabron</span><br />
<span class="score" title="361 reputation points">361</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="frabron has 2 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-13262" class="comments-container">
&#10;</div>
<div id="comment-tools-13262" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13262-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="13300"></span>

<div id="answer-container-13300" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13300-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13300-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-13300-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi,</p>
<p>this is not the TSP problem, in TSP you find the shortest path that connect different nodes in a graph. Paul is asking for an algorithm that visits all edges in a graph with minimum repetition, this is the CPP - Chinese Postman Problem. You will fins information at <a href="http://en.wikipedia.org/wiki/Chinese_postman_problem">wikipedia</a></p>
<p>You will have some challenges at 'cul-de-sacs'. And no, there is no relation with TSP.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Jun '12, 10:27</strong></p>
<img src="https://secure.gravatar.com/avatar/e678d09d1a379afe93b7040529e9ffdd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaume%20Figueras&#39;s gravatar image" />
<p><span>Jaume Figueras</span><br />
<span class="score" title="55 reputation points">55</span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaume Figueras has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-13300" class="comments-container">
<span id="13306"></span>
<div id="comment-13306" class="comment">
<div id="post-13306-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for your comment, Juame.</p>
<p>I read the wiki entry and I agree the problem is less TSP than CPP. It appears, since my problem cannot be solved without some repetition (cul-de-sacs, and likely some out-and-back for some roads extending beyond the city's perimeter), it will not be a Eulerian path or circuit. However, having said that, it would be possible to provide a program with a graph of the streets excluding the cul-de-sacs.</p>
<p>Again, thanks for reflecting on my challenge. My plan is to complete the course over several days; although my desire is to complete it as quickly as possible (thus a run), I will break for some sleep each day.</p>
</div>
<div id="comment-13306-info" class="comment-info">
<span class="comment-age">(07 Jun '12, 18:55)</span> <span class="comment-user userinfo">pmbooks</span>
</div>
</div>
<span id="13310"></span>
<div id="comment-13310" class="comment">
<div id="post-13310-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>BTW, I live in Redlands, home to ESRI. You might expect I would know someone there who could help solve this, but I don't.</p>
</div>
<div id="comment-13310-info" class="comment-info">
<span class="comment-age">(07 Jun '12, 19:11)</span> <span class="comment-user userinfo">pmbooks</span>
</div>
</div>
</div>
<div id="comment-tools-13300" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13300-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="13209"></span>

<div id="answer-container-13209" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13209-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13209-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-13209-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You're trying to solve a <a href="http://en.wikipedia.org/wiki/Travelling_salesman_problem">classic problem of computer science</a> which has no easy answers. Good luck :p</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Jun '12, 22:28</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-13209" class="comments-container">
<span id="13211"></span>
<div id="comment-13211" class="comment">
<div id="post-13211-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Nice, thank you for the link, Vincent. It is, as you point out, a classic problem (The Travelling Salesman Problem). I would think that there must be some mapping software out there for this problem. (I'm think of trash pick-up and mail delivery being a couple of instances where the route needs this optimization.</p>
</div>
<div id="comment-13211-info" class="comment-info">
<span class="comment-age">(02 Jun '12, 22:54)</span> <span class="comment-user userinfo">pmbooks</span>
</div>
</div>
<span id="13214"></span>
<div id="comment-13214" class="comment">
<div id="post-13214-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yet, one variation between the traveling salesman's problem and my own is that the former concerns hitting points (cities) that must be connected via the shortest distance, while my problem covers roads that must be traversed. There may be 300 miles of roads in the city, but with cul-de-sacs, etc., there will necessarily be more distance covered. I can start at any point in the city, and I will take breaks along the way (I will need to return to the point where I left the "course."</p>
</div>
<div id="comment-13214-info" class="comment-info">
<span class="comment-age">(03 Jun '12, 05:56)</span> <span class="comment-user userinfo">pmbooks</span>
</div>
</div>
<span id="13260"></span>
<div id="comment-13260" class="comment">
<div id="post-13260-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Going through the roads is the exact same problem in term of description by graph theory. Your problem is just the Traveling Salesman as applied to the <a href="http://en.wikipedia.org/wiki/Seven_Bridges_of_K%C3%B6nigsberg">Seven Bridges of Königsberg</a>.</p>
</div>
<div id="comment-13260-info" class="comment-info">
<span class="comment-age">(05 Jun '12, 04:26)</span> <span class="comment-user userinfo">Circeus</span>
</div>
</div>
<span id="13375"></span>
<div id="comment-13375" class="comment">
<div id="post-13375-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>So, are Euler's "bridges" equivalent to the lengths of street between intersections?</p>
</div>
<div id="comment-13375-info" class="comment-info">
<span class="comment-age">(09 Jun '12, 14:17)</span> <span class="comment-user userinfo">pmbooks</span>
</div>
</div>
<span id="13435"></span>
<div id="comment-13435" class="comment">
<div id="post-13435-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>No, the bridges are not equivalent to length. If you want to model a network into a graph, the bridges are the edges and the connection between bridges are the nodes. In Königsberg problem, the classic modeling of the network does not take into account distances because the problem does not depend on distances. You try to find a circuit independently of the distances. In CPP you should take into account oneways (directed graph) and distances (marking of the edges)</p>
</div>
<div id="comment-13435-info" class="comment-info">
<span class="comment-age">(11 Jun '12, 19:45)</span> <span class="comment-user userinfo">Jaume Figueras</span>
</div>
</div>
</div>
<div id="comment-tools-13209" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13209-form-container" class="comment-form-container">
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


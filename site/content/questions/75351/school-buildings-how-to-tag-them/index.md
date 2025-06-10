+++
type = "question"
title = "School Buildings; How to tag them?"
description = '''I&#x27;m currently working on adding school buildings to the map, but I am not sure how to mark buildings that are cafeterias, for administration, for a certain subject (eg. Math), or auditoriums. Help?'''
date = "2020-06-16T05:17:00Z"
lastmod = "2020-06-16T08:27:00Z"
weight = 75351
keywords = [ "school", "cafeteria", "buildings", "tags", "auditoriums" ]
aliases = [ "/questions/75351" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [School Buildings; How to tag them?](/questions/75351/school-buildings-how-to-tag-them)

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
<span id="post-75351-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75351-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75351-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm currently working on adding school buildings to the map, but I am not sure how to mark buildings that are cafeterias, for administration, for a certain subject (eg. Math), or auditoriums. Help?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-school" rel="tag" title="see questions tagged &#39;school&#39;">school</span> <span class="post-tag tag-link-cafeteria" rel="tag" title="see questions tagged &#39;cafeteria&#39;">cafeteria</span> <span class="post-tag tag-link-buildings" rel="tag" title="see questions tagged &#39;buildings&#39;">buildings</span> <span class="post-tag tag-link-tags" rel="tag" title="see questions tagged &#39;tags&#39;">tags</span> <span class="post-tag tag-link-auditoriums" rel="tag" title="see questions tagged &#39;auditoriums&#39;">auditoriums</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Jun '20, 05:17</strong></p>
<img src="https://secure.gravatar.com/avatar/b3c43e68353fb119848cbad80c687109?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TheAdventurer64&#39;s gravatar image" />
<p><span>TheAdventurer64</span><br />
<span class="score" title="139 reputation points">139</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TheAdventurer64 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Jun '20, 05:26</strong> </span></p>
</div>
</div>
<div id="comments-container-75351" class="comments-container">
&#10;</div>
<div id="comment-tools-75351" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75351-form-container" class="comment-form-container">
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

<span id="75354"></span>

<div id="answer-container-75354" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75354-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75354-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75354-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="TheAdventurer64 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Read around <a href="https://wiki.openstreetmap.org/wiki/Tag:amenity%3Duniversity"><code>amenity=university</code></a> and <a href="https://wiki.openstreetmap.org/wiki/Tag:amenity=school"><code>amenity=school</code></a> a bit.</p>
<p>A building for subjects could be mapped by <code>department=mathematics</code> or <code>department=English Literture</code>. Alternatively use <code>faculty=</code>. Have a look at taginfo to see what values others have used: <a href="https://taginfo.openstreetmap.org/keys/?key=department#values">department</a>, <a href="https://taginfo.openstreetmap.org/keys/?key=faculty#values">faculty</a>.</p>
<p>A cafeteria is mapped by <a href="https://wiki.openstreetmap.org/wiki/Tag:amenity%3Dcafe"><code>amenity=cafe</code></a>, <a href="https://wiki.openstreetmap.org/wiki/Tag:amenity%3Drestaurant"><code>amenity=restaurant</code></a> or <a href="https://wiki.openstreetmap.org/wiki/Tag:amenity%3Dfast_food"><code>amenity=fast_food</code></a>. If the public is not permitted add <code>access=private</code>.</p>
<p>If a whole building is an auditorium you can use <code>building=auditorium</code>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Jun '20, 08:27</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Jun '20, 09:50</strong> </span></p>
</div>
</div>
<div id="comments-container-75354" class="comments-container">
&#10;</div>
<div id="comment-tools-75354" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75354-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="75352"></span>

<div id="answer-container-75352" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75352-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75352-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-75352-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="https://wiki.openstreetmap.org/wiki/Tag:amenity=school#How%20to%20map">Please have a look here</a> and <a href="https://wiki.openstreetmap.org/wiki/Tag:building%3Dschool">here</a>.</p>
<p>If each specific building is to be mapped, then the <code>name</code> tag should reflect the name of the building. However, this method of mapping may not work for a building with multiple facilities, you may want (complexly) to use the <code>building:part</code> tag.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Jun '20, 06:28</strong></p>
<img src="https://secure.gravatar.com/avatar/de7b93bd537287f5af7e862bf4cd2fec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AkuAnakTimur&#39;s gravatar image" />
<p><span>AkuAnakTimur</span><br />
<span class="score" title="1070 reputation points"><span>1.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="31 badges"><span class="bronze">●</span><span class="badgecount">31</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AkuAnakTimur has one accepted answer">6%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Jun '20, 06:35</strong> </span></p>
</div>
</div>
<div id="comments-container-75352" class="comments-container">
<span id="75353"></span>
<div id="comment-75353" class="comment">
<div id="post-75353-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>On those pages, it mentions that I should tag each building with the appropriate tags. I'm looking for tags that can be used for the exact facility. (Eg. fast_food=cafeteria).</p>
</div>
<div id="comment-75353-info" class="comment-info">
<span class="comment-age">(16 Jun '20, 07:43)</span> <span class="comment-user userinfo">TheAdventurer64</span>
</div>
</div>
</div>
<div id="comment-tools-75352" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75352-form-container" class="comment-form-container">
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


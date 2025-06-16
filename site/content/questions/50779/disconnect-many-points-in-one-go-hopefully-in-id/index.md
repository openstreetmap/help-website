+++
type = "question"
title = "Disconnect many points in one go (hopefully in iD)"
description = '''Based on this answer and to help me in my mapping of walls, particularly in Yorkshire. I have come across several places where a road and the surrounding farmland share nodes, I then have to disconnect each of the points individually and drag the edge of the farmland away to the line of the wall and...'''
date = "2016-07-10T11:11:00Z"
lastmod = "2016-07-11T11:30:00Z"
weight = 50779
keywords = [ "nodes", "editing", "road", "area" ]
aliases = [ "/questions/50779" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Disconnect many points in one go (hopefully in iD)](/questions/50779/disconnect-many-points-in-one-go-hopefully-in-id)

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
<span id="post-50779-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50779-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-50779-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Based on <a href="/questions/17501/when-mapping-polygons-surrounded-by-streets-should-they-share-nodes-or-be-traced-separately/17505">this answer</a> and to help me in my mapping of walls, particularly in Yorkshire. I have come across several places where a road and the surrounding farmland share nodes, I then have to disconnect each of the points individually and drag the edge of the farmland away to the line of the wall and then add my wall.</p>
<p>What I am interested to now is: Is there any way to disconnect all of an area and a lines shared points in on go to speed up the first stage of this process? I currently only have experience with iD so if it's possible there that would be great however I am willing to work with the other editors if necessary.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-editing" rel="tag" title="see questions tagged &#39;editing&#39;">editing</span> <span class="post-tag tag-link-road" rel="tag" title="see questions tagged &#39;road&#39;">road</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Jul '16, 11:11</strong></p>
<img src="https://secure.gravatar.com/avatar/b372136094bdbf5901a66c8fe1b3a548?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BarnsleyOli&#39;s gravatar image" />
<p><span>BarnsleyOli</span><br />
<span class="score" title="91 reputation points">91</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BarnsleyOli has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-50779" class="comments-container">
<span id="50780"></span>
<div id="comment-50780" class="comment">
<div id="post-50780-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>(not a direct answer to the question but)</p>
<p>In the case of streets (as that <a href="/questions/17501/when-mapping-polygons-surrounded-by-streets-should-they-share-nodes-or-be-traced-separately/17505">answer</a> says) I wouldn't share nodes between linear features like roads and the surrounding farmland.</p>
<p>However, in the case of farmland and walls, if the farmland really does end at the wall I'd see no problem with farmland and wall sharing nodes, and if it doesn't I'd see no problem with the two being separate. Where I am (Derbyshire) farmland tends to exactly terminate at a wall, though further east it often stops, then there's "nothing much" for a bit, and then the hedge or wall.</p>
</div>
<div id="comment-50780-info" class="comment-info">
<span class="comment-age">(10 Jul '16, 11:32)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="50781"></span>
<div id="comment-50781" class="comment">
<div id="post-50781-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a> Thanks I was almost certain that this was what needed doing, so thanks for clarifying. I just wouldn't mind being able to correct instances where this hasn't been done more quickly. Hence the question. Thanks though!</p>
</div>
<div id="comment-50781-info" class="comment-info">
<span class="comment-age">(10 Jul '16, 11:43)</span> <span class="comment-user userinfo">BarnsleyOli</span>
</div>
</div>
</div>
<div id="comment-tools-50779" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50779-form-container" class="comment-form-container">
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

<span id="50782"></span>

<div id="answer-container-50782" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-50782-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50782-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-50782-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="BarnsleyOli has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Not sure if this helps...<br />
In JOSM, you can select the farmland boundary, select the nodes at each end of the section you want to alter, then Tools &gt; Split Boundary.<br />
Select that portion, then Edit &gt; Duplicate and a copy of that portion appears nearby. Select the problem portion, then Edit &gt; Delete.<br />
Drag the duplicate to where you want it to be and join the ends to the ends of the original portion you left.<br />
This method may be better if disconnecting a large boundary.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Jul '16, 12:19</strong></p>
<img src="https://secure.gravatar.com/avatar/e5674dd96938593e0af5130dfffe0f90?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nevw&#39;s gravatar image" />
<p><span>nevw</span><br />
<span class="score" title="9843 reputation points"><span>9.8k</span></span><span title="26 badges"><span class="badge1">●</span><span class="badgecount">26</span></span><span title="90 badges"><span class="silver">●</span><span class="badgecount">90</span></span><span title="178 badges"><span class="bronze">●</span><span class="badgecount">178</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nevw has 32 accepted answers">9%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Jul '16, 12:28</strong> </span></p>
</div>
</div>
<div id="comments-container-50782" class="comments-container">
&#10;</div>
<div id="comment-tools-50782" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50782-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="50783"></span>

<div id="answer-container-50783" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-50783-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50783-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-50783-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Since your willngly to try other editors try JOSM, select the way and hit G, that works fine to isolate a whole area surrounded by whatever. Remember to connect all the nodes afterwords. Nevw method works for a few, less work.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Jul '16, 12:42</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span> </br></br></p>
</div>
</div>
<div id="comments-container-50783" class="comments-container">
<span id="50811"></span>
<div id="comment-50811" class="comment">
<div id="post-50811-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You can also select the way and some of its node before hiting G, if not all nodes need to be unglued. Free-form selection is often the fastest way to do this.</p>
</div>
<div id="comment-50811-info" class="comment-info">
<span class="comment-age">(11 Jul '16, 11:30)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
</div>
<div id="comment-tools-50783" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50783-form-container" class="comment-form-container">
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


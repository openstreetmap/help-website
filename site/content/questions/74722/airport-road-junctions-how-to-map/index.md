+++
type = "question"
title = "Airport road junctions; How to map?"
description = '''So, I am currently adding information to the Daniel K. Inouye International Airport. Currently, the plan is to work on the road junction info. However, I do not have any idea how to map a junction like this: Picture Any ideas?'''
date = "2020-05-11T06:36:00Z"
lastmod = "2020-06-15T23:11:00Z"
weight = 74722
keywords = [ "airport", "motorway_junction", "freeway_exit" ]
aliases = [ "/questions/74722" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Airport road junctions; How to map?](/questions/74722/airport-road-junctions-how-to-map)

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
<span id="post-74722-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74722-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74722-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>So, I am currently adding information to the Daniel K. Inouye International Airport. Currently, the plan is to work on the road junction info. However, I do not have any idea how to map a junction like this:</p>
<p><a href="https://www.dropbox.com/s/v5tek8ocym5r760/fourm.png?dl=0" title="title">Picture</a></p>
<p>Any ideas?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-airport" rel="tag" title="see questions tagged &#39;airport&#39;">airport</span> <span class="post-tag tag-link-motorway_junction" rel="tag" title="see questions tagged &#39;motorway_junction&#39;">motorway_junction</span> <span class="post-tag tag-link-freeway_exit" rel="tag" title="see questions tagged &#39;freeway_exit&#39;">freeway_exit</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 May '20, 06:36</strong></p>
<img src="https://secure.gravatar.com/avatar/b3c43e68353fb119848cbad80c687109?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TheAdventurer64&#39;s gravatar image" />
<p><span>TheAdventurer64</span><br />
<span class="score" title="139 reputation points">139</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TheAdventurer64 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 May '20, 09:21</strong> </span></p>
</div>
</div>
<div id="comments-container-74722" class="comments-container">
&#10;</div>
<div id="comment-tools-74722" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74722-form-container" class="comment-form-container">
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

<span id="74742"></span>

<div id="answer-container-74742" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74742-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74742-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74742-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="TheAdventurer64 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Are you asking about the destination signing?</p>
<p>On the approach to the junction you can use <a href="https://wiki.openstreetmap.org/wiki/Lanes">lane tagging</a>. It could look like something like this:<br />
oneway=yes<br />
lanes=3<br />
turn:lanes=through|through|slight_right<br />
destination:lanes=Terminals 1, 2, 3; Departures;Parking|Terminals 1, 2, 3; Departures;Parking|Terminals 1, 2; Arrivals;Rental Car Return<br />
destination:ref:lanes=1;2;3|1;2;3|1;2</p>
<p>On the ways after the actual split you can tag the destination directly e.g. for the right hand road:<br />
oneway=yes<br />
destination=Terminals 1, 2; Arrivals;Rental Car Return<br />
destination:ref=1;2</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 May '20, 17:26</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 May '20, 04:30</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span></br></p>
</div>
</div>
<div id="comments-container-74742" class="comments-container">
<span id="74746"></span>
<div id="comment-74746" class="comment">
<div id="post-74746-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What is it you are unsure about? The highway tag? Could you point to the point on the map?</p>
</div>
<div id="comment-74746-info" class="comment-info">
<span class="comment-age">(11 May '20, 21:15)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="75340"></span>
<div id="comment-75340" class="comment">
<div id="post-75340-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Alright. While the tags work okay, I still don't know how to map a junction like this: <a href="https://www.dropbox.com/s/xo7bw56t6m6noiq/Screenshot%202020-06-15%2010.05.25.png?dl=0">https://www.dropbox.com/s/xo7bw56t6m6noiq/Screenshot%202020-06-15%2010.05.25.png?dl=0</a></p>
</div>
<div id="comment-75340-info" class="comment-info">
<span class="comment-age">(15 Jun '20, 21:16)</span> <span class="comment-user userinfo">TheAdventurer64</span>
</div>
</div>
<span id="75342"></span>
<div id="comment-75342" class="comment">
<div id="post-75342-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I repeat my question: What do you have difficulties with? Can you be a bit more specific?</p>
</div>
<div id="comment-75342-info" class="comment-info">
<span class="comment-age">(15 Jun '20, 21:44)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="75344"></span>
<div id="comment-75344" class="comment">
<div id="post-75344-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I am having difficulty understanding how to mark the turn lanes and how to use destination:ref:lanes.</p>
</div>
<div id="comment-75344-info" class="comment-info">
<span class="comment-age">(15 Jun '20, 22:33)</span> <span class="comment-user userinfo">TheAdventurer64</span>
</div>
</div>
<span id="75350"></span>
<div id="comment-75350" class="comment">
<div id="post-75350-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Please post a link to the location on OpenStreetMap.org. Klick the "share" button on the right and place a marker at the specific intersection.</p>
</div>
<div id="comment-75350-info" class="comment-info">
<span class="comment-age">(15 Jun '20, 23:11)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
</div>
<div id="comment-tools-74742" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74742-form-container" class="comment-form-container">
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


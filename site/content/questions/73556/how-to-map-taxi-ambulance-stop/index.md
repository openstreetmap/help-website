+++
type = "question"
title = "How to map Taxi &amp; Ambulance stop"
description = '''there is a Parking spot for Taxi and ambulance, it&#x27;s intended for both, and clearly say so, it&#x27;s painted spot. I marked it like this: amenity=Taxi, ambulance capacity==1 name=Taxi og Ambulanse name:en=Taxi and Ambulanse https://www.openstreetmap.org/way/781964506 is this correct?  or should I change...'''
date = "2020-03-17T02:16:00Z"
lastmod = "2020-03-17T07:55:00Z"
weight = 73556
keywords = [ "taxi", "parking", "ambulance" ]
aliases = [ "/questions/73556" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to map Taxi & Ambulance stop](/questions/73556/how-to-map-taxi-ambulance-stop)

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
<span id="post-73556-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73556-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73556-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>there is a Parking spot for Taxi and ambulance, it's intended for both, and clearly say so, it's painted spot.</p>
<p>I marked it like this: amenity=Taxi, ambulance capacity==1 name=Taxi og Ambulanse name:en=Taxi and Ambulanse</p>
<p><a href="https://www.openstreetmap.org/way/781964506">https://www.openstreetmap.org/way/781964506</a></p>
<p>is this correct? or should I change it? is there a feature coming for this type stop?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-taxi" rel="tag" title="see questions tagged &#39;taxi&#39;">taxi</span> <span class="post-tag tag-link-parking" rel="tag" title="see questions tagged &#39;parking&#39;">parking</span> <span class="post-tag tag-link-ambulance" rel="tag" title="see questions tagged &#39;ambulance&#39;">ambulance</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Mar '20, 02:16</strong></p>
<img src="https://secure.gravatar.com/avatar/36fe123bbb61e49a67eae244eddcca16?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtbboy1993&#39;s gravatar image" />
<p><span>mtbboy1993</span><br />
<span class="score" title="40 reputation points">40</span><span title="38 badges"><span class="badge1">●</span><span class="badgecount">38</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="45 badges"><span class="bronze">●</span><span class="badgecount">45</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtbboy1993 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-73556" class="comments-container">
&#10;</div>
<div id="comment-tools-73556" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73556-form-container" class="comment-form-container">
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

<span id="73559"></span>

<div id="answer-container-73559" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73559-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73559-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-73559-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="mtbboy1993 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<ol>
<li><code>amenity=taxi</code> manes a taxi stand. Multi-value should be separated by a colon <code>;</code>, and yet there is not really <code>amenity=ambulance</code>. You should use <code>amenity=parking_space</code> with firstly <code>taxi=yes</code>. There's <code>ambulance=yes</code> at 2-digit use, but <code>motor_vehicle:conditional=yes @ (ambulance)</code> would be more general (there are many ambulance vehicle types) and meaningful (same issue with <code>emergency=</code> as a legal access restriction - would it be built specifically to receive ambulance as a facility, more than about ambulance use only?).</li>
<li>Don't tag these as <code>name=</code>. Use <code>description=</code>.</li>
</ol>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Mar '20, 05:01</strong></p>
<img src="https://secure.gravatar.com/avatar/76ffbb56c811e8a8ccdd4c28f122399f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kovoschiz&#39;s gravatar image" />
<p><span>Kovoschiz</span><br />
<span class="score" title="2434 reputation points"><span>2.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kovoschiz has 22 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Mar '20, 05:25</strong> </span></p>
</div>
</div>
<div id="comments-container-73559" class="comments-container">
<span id="73565"></span>
<div id="comment-73565" class="comment">
<div id="post-73565-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thx, I fixed it.</p>
</div>
<div id="comment-73565-info" class="comment-info">
<span class="comment-age">(17 Mar '20, 07:10)</span> <span class="comment-user userinfo">mtbboy1993</span>
</div>
</div>
<span id="73569"></span>
<div id="comment-73569" class="comment">
<div id="post-73569-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Very sorry, I forgot to mention you should use <code>vehicle=no</code> to forbid all other vehicles.</p>
</div>
<div id="comment-73569-info" class="comment-info">
<span class="comment-age">(17 Mar '20, 07:55)</span> <span class="comment-user userinfo">Kovoschiz</span>
</div>
</div>
</div>
<div id="comment-tools-73559" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73559-form-container" class="comment-form-container">
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


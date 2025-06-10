+++
type = "question"
title = "how to upload waypoints"
description = '''Looking at the FAQ I get no answer on my question. Please answer directly. (I&#x27;ve hád it with FAQ&#x27;s.)'''
date = "2019-09-29T16:56:00Z"
lastmod = "2019-09-30T07:47:00Z"
weight = 70957
keywords = [ "waypoints" ]
aliases = [ "/questions/70957" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how to upload waypoints](/questions/70957/how-to-upload-waypoints)

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
<span id="post-70957-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70957-score" class="post-score" title="current number of votes">
-2
</div>
<span id="post-70957-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Looking at the FAQ I get no answer on my question. Please answer directly. (I've hád it with FAQ's.)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-waypoints" rel="tag" title="see questions tagged &#39;waypoints&#39;">waypoints</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Sep '19, 16:56</strong></p>
<img src="https://secure.gravatar.com/avatar/719595584d81b40dff8fca01babea06a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Chuparuedas&#39;s gravatar image" />
<p><span>Chuparuedas</span><br />
<span class="score" title="34 reputation points">34</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Chuparuedas has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-70957" class="comments-container">
<span id="70959"></span>
<div id="comment-70959" class="comment">
<div id="post-70959-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Can you explain in a bit more detail what your question actually is? "how to upload waypoints" can mean one of many different things ("waypoints" can have several meanings, and you haven't said "upload to what").</p>
</div>
<div id="comment-70959-info" class="comment-info">
<span class="comment-age">(29 Sep '19, 17:10)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-70957" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70957-form-container" class="comment-form-container">
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

<span id="70964"></span>

<div id="answer-container-70964" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70964-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70964-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70964-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'm assuming you are trying to upload those waypoints (WPs) in order to add POIs to OSM. That's the only valid reason for wanting to do what you're asking. Do not add WPs to OSM if they are your personal WPs, for example, "My house", Carol's shop", etc.</p>
<p>Because OSM will not accept a GPX file containing only waypoints, I "trick" JOSM into doing this as follows, (I don't know if iD or Potlatch allow this). I upload a GPS trace, any trace will do, along with the waypoints. The trace need not be related to the WPs. To do that I "export" the WPs and the trace in one GPX file using Garmin's Basecamp program by selecting the WP's and the trace before the Export step. Once the file is uploaded using the Open command in JOSM I use the photo_geotagging plugin to utilize the WP data. The waypoints ("markers") will be in a separate layer named "Markers from Selected data ..." and you can jump from one to the other by right-clicking on that layer and choosing Jump to next, Jump to previous. Do not convert the Marker layer to a Data Layer because you will only be using it temporarily as a way to add actual OSM data.</p>
<p>After adding the OSM data represented by the WPs I delete the trace and the Marker layers.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Sep '19, 01:28</strong></p>
<img src="https://secure.gravatar.com/avatar/04dddf6f5ffde333747d385af3ce5829?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AlaskaDave&#39;s gravatar image" />
<p><span>AlaskaDave</span><br />
<span class="score" title="5415 reputation points"><span>5.4k</span></span><span title="76 badges"><span class="badge1">●</span><span class="badgecount">76</span></span><span title="107 badges"><span class="silver">●</span><span class="badgecount">107</span></span><span title="164 badges"><span class="bronze">●</span><span class="badgecount">164</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AlaskaDave has 17 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Sep '19, 01:30</strong> </span></p>
</div>
</div>
<div id="comments-container-70964" class="comments-container">
<span id="70966"></span>
<div id="comment-70966" class="comment">
<div id="post-70966-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>inaddition see <a href="https://help.openstreetmap.org/questions/24299/how-to-use-waypoints-which-have-been-collected-by-gps-for-mapping">https://help.openstreetmap.org/questions/24299/how-to-use-waypoints-which-have-been-collected-by-gps-for-mapping</a></p>
</div>
<div id="comment-70966-info" class="comment-info">
<span class="comment-age">(30 Sep '19, 07:47)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
</div>
<div id="comment-tools-70964" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70964-form-container" class="comment-form-container">
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


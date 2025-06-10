+++
type = "question"
title = "how to use overpass with spatial database"
description = '''Hi, i want to develop a routing application for openstreetmap which will use overpass api, post gis as database and android toolkit like mapbox. I have read all about Query Language for overpass api but unable to understand more about it even don&#x27;t know that how overpass turbo data will link with pg...'''
date = "2016-10-23T14:01:00Z"
lastmod = "2016-10-28T07:11:00Z"
weight = 52648
keywords = [ "overpass", "api", "overpass-turbo" ]
aliases = [ "/questions/52648" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how to use overpass with spatial database](/questions/52648/how-to-use-overpass-with-spatial-database)

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
<span id="post-52648-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52648-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-52648-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, i want to develop a routing application for openstreetmap which will use overpass api, post gis as database and android toolkit like mapbox. I have read all about Query Language for overpass api but unable to understand more about it even don't know that how overpass turbo data will link with pgadmin III. help me out that from where i can start for overpass api. I just have 1 more week to show my project. I am feeling helpless.Do help me out.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Oct '16, 14:01</strong></p>
<img src="https://secure.gravatar.com/avatar/7781bb3b1d47cf3524b7491c2ca093bd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="samar&#39;s gravatar image" />
<p><span>samar</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="samar has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-52648" class="comments-container">
&#10;</div>
<div id="comment-tools-52648" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52648-form-container" class="comment-form-container">
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

<span id="52653"></span>

<div id="answer-container-52653" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52653-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52653-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-52653-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Do not use Overpass. Download an .osm.pbf file covering your region of interest, then use osm2pgsql or osm2pgrouting to import your data into PostGIS or PostgreSQL. Then you can access the data in your database.</p>
<p>Be advised that this will only allow you to build a very basic routing engine "proof of concept". Writing a good routing engine is far, far more complex than can be solved in a one-week student project.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Oct '16, 18:57</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-52653" class="comments-container">
<span id="52654"></span>
<div id="comment-52654" class="comment">
<div id="post-52654-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you very much sir for your kind help.i hope now i can do my work in a better way.</p>
</div>
<div id="comment-52654-info" class="comment-info">
<span class="comment-age">(24 Oct '16, 05:00)</span> <span class="comment-user userinfo">samar</span>
</div>
</div>
<span id="52711"></span>
<div id="comment-52711" class="comment">
<div id="post-52711-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>can spatialite be used for same and what flexibility does spatialite api would provide?</p>
</div>
<div id="comment-52711-info" class="comment-info">
<span class="comment-age">(27 Oct '16, 09:33)</span> <span class="comment-user userinfo">samar</span>
</div>
</div>
<span id="52712"></span>
<div id="comment-52712" class="comment">
<div id="post-52712-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>There's a tool called osm2spatialite but it is not widely used. You can try...</p>
</div>
<div id="comment-52712-info" class="comment-info">
<span class="comment-age">(27 Oct '16, 10:03)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="52723"></span>
<div id="comment-52723" class="comment">
<div id="post-52723-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thankz a bunch for ur replies.</p>
</div>
<div id="comment-52723-info" class="comment-info">
<span class="comment-age">(28 Oct '16, 07:11)</span> <span class="comment-user userinfo">samar</span>
</div>
</div>
</div>
<div id="comment-tools-52653" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52653-form-container" class="comment-form-container">
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


+++
type = "question"
title = "can we use a single postrges DB to serve several OSM services?"
description = '''Hi All,  First post here. I would like to start by thanking the fantastic OSM community. I started getting interested in GIS relatively recently, and I must say that I have a lot of fun doing geospatial analysis so far. This is mostly permitted thanks to your awesome work! Please be forgiving if my ...'''
date = "2020-11-30T17:14:00Z"
lastmod = "2020-11-30T19:21:00Z"
weight = 77811
keywords = [ "services", "docker", "server" ]
aliases = [ "/questions/77811" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [can we use a single postrges DB to serve several OSM services?](/questions/77811/can-we-use-a-single-postrges-db-to-serve-several-osm-services)

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
<span id="post-77811-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77811-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77811-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi All,</p>
<p>First post here. I would like to start by thanking the fantastic OSM community. I started getting interested in GIS relatively recently, and I must say that I have a lot of fun doing geospatial analysis so far. This is mostly permitted thanks to your awesome work!</p>
<p>Please be forgiving if my question is a bit naive, but I would love to hear your thoughts on the following. I am working on a project that relies extensively on various geospatial services, I am therefore considering setting up my own instance of OSM with the following services</p>
<ul>
<li>geocoding and reverse geocoding</li>
<li>POIs retrieval</li>
<li>routing</li>
</ul>
<p>I am able to find docker images for each service, which is great, but as far as I understood, each service is independent of the others. For example, if I want to set up those services for Luxembourg, I would need to do three different data ingestions into three different containers running each their own database.</p>
<p>What I would ideally like to achieve is to have a single Postgres DB that can be used by each service. I did a bit of googling but, to my surprise, this didn't seem to be a very common use-case. So now I am wondering if this is actually doable? If yes, any pointers to the relevant resources will be highly appreciated :)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-services" rel="tag" title="see questions tagged &#39;services&#39;">services</span> <span class="post-tag tag-link-docker" rel="tag" title="see questions tagged &#39;docker&#39;">docker</span> <span class="post-tag tag-link-server" rel="tag" title="see questions tagged &#39;server&#39;">server</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Nov '20, 17:14</strong></p>
<img src="https://secure.gravatar.com/avatar/6502c95828abba0ec99e7a13d550e962?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fatgere&#39;s gravatar image" />
<p><span>fatgere</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fatgere has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-77811" class="comments-container">
&#10;</div>
<div id="comment-tools-77811" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77811-form-container" class="comment-form-container">
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

<span id="77813"></span>

<div id="answer-container-77813" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77813-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77813-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77813-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>No. There is some <a href="https://github.com/openstreetmap/osm2pgsql/issues/1311#issuecomment-733707688">work related to a single database for geocoding and rendering</a> that could help, but most routing engines don't use a general purpose database but instead run something specialized.</p>
<p>Where a general purpose database like PostgreSQL is used there are a wide assortment of schemas to put the data into, and</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Nov '20, 18:04</strong></p>
<img src="https://secure.gravatar.com/avatar/5634c46072077e10f5b7c0da9b4bbb62?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pnorman&#39;s gravatar image" />
<p><span>pnorman</span><br />
<span class="score" title="2352 reputation points"><span>2.4k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="21 badges"><span class="silver">●</span><span class="badgecount">21</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pnorman has 9 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-77813" class="comments-container">
<span id="77817"></span>
<div id="comment-77817" class="comment">
<div id="post-77817-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks <a href="https://help.openstreetmap.org/users/290/pnorman">@pnorman</a> for your reply. Really helpful to know that this is actually not possible. I think your reply got cut at some points, would be interested to read the last part though :)</p>
</div>
<div id="comment-77817-info" class="comment-info">
<span class="comment-age">(30 Nov '20, 19:21)</span> <span class="comment-user userinfo">fatgere</span>
</div>
</div>
</div>
<div id="comment-tools-77813" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77813-form-container" class="comment-form-container">
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


+++
type = "question"
title = "Install both nominatim and postgres in Docker container (microservice)"
description = '''Hi everyone. I have used Nominatim on my machine already through a docker installation: installed docker image and installed PostgreSQL + postgis on my machine. My next goal is to make Nominatim independent of my machine and install both the database it is using and the nominatim instance itself in ...'''
date = "2021-08-09T09:07:00Z"
lastmod = "2021-08-12T09:05:00Z"
weight = 81239
keywords = [ "microservice", "docker", "nominatim", "combine", "postgres" ]
aliases = [ "/questions/81239" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Install both nominatim and postgres in Docker container (microservice)](/questions/81239/install-both-nominatim-and-postgres-in-docker-container-microservice)

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
<span id="post-81239-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81239-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81239-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi everyone. I have used Nominatim on my machine already through a docker installation: installed docker image and installed PostgreSQL + postgis on my machine. My next goal is to make Nominatim independent of my machine and install both the database it is using and the nominatim instance itself in a docker container / or two separate containers.</p>
<p>So I'm thinking either of having two docker containers: one having nominatim and one having the database. Then tell nominatim that it can find the database in the docker container. Both containers have to be started and run at the same time.</p>
<p>So when I installed Nominatim on my machine, I used this guide: <a href="https://hub.docker.com/r/stefanreuter/nominatim">https://hub.docker.com/r/stefanreuter/nominatim</a></p>
<p>Now the main question would be how to change this part: docker run -t -v <em>/home/me/nominatimdata:/data nominatim</em> sh /app/init.sh /data/merged.osm.pbf postgresdata 4. The italic part is where I specify where to save the data that will be created for nominatim. I want this to be in the docker image of the database.</p>
<p>Has anyone tried combining the db and Nominatim using docker compose?</p>
<p>Has anyone ever tried this and can share information on how to do this or is this not possible because of some reasons?</p>
<p>I would love to hear your thoughts! Arusha</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-microservice" rel="tag" title="see questions tagged &#39;microservice&#39;">microservice</span> <span class="post-tag tag-link-docker" rel="tag" title="see questions tagged &#39;docker&#39;">docker</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-combine" rel="tag" title="see questions tagged &#39;combine&#39;">combine</span> <span class="post-tag tag-link-postgres" rel="tag" title="see questions tagged &#39;postgres&#39;">postgres</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Aug '21, 09:07</strong></p>
<img src="https://secure.gravatar.com/avatar/7128510c49d32bd84794a8ddc39a5de9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Arusha29&#39;s gravatar image" />
<p><span>Arusha29</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Arusha29 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Aug '21, 11:35</strong> </span></p>
</div>
</div>
<div id="comments-container-81239" class="comments-container">
&#10;</div>
<div id="comment-tools-81239" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81239-form-container" class="comment-form-container">
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

<span id="81244"></span>

<div id="answer-container-81244" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81244-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81244-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-81244-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="https://github.com/mediagis/nominatim-docker">https://github.com/mediagis/nominatim-docker</a> is well maintained and you can ask questions in their issue tracker. <a href="https://github.com/mediagis/nominatim-docker/issues?q=docker-compose">https://github.com/mediagis/nominatim-docker/issues?q=docker-compose</a> It's much easier to have a separate database container.</p>
<p>In your docker compose configuration file you'd do something like</p>
<p><code>services: nominatim: image: ... ... depends_on: - db db: image: ... ...</code></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Aug '21, 13:30</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-81244" class="comments-container">
&#10;</div>
<div id="comment-tools-81244" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81244-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="81282"></span>

<div id="answer-container-81282" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81282-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81282-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81282-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Thanks for your reply, I hadn't seen there were issues already open for docker-compose on GitHub (Google didn't direct me there..) I will try this!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Aug '21, 09:05</strong></p>
<img src="https://secure.gravatar.com/avatar/7128510c49d32bd84794a8ddc39a5de9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Arusha29&#39;s gravatar image" />
<p><span>Arusha29</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Arusha29 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-81282" class="comments-container">
&#10;</div>
<div id="comment-tools-81282" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81282-form-container" class="comment-form-container">
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


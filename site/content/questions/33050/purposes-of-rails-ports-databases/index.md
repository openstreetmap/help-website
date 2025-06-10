+++
type = "question"
title = "Purposes of Rails Ports databases"
description = '''Hi there! I&#x27;ve installed openstreetmap&#x27;s Rails Port to check it out and there&#x27;s something related to the 3 databases it uses that I don&#x27;t understand. The INSTALL.md files indicates that this port uses 3 databases, one for development (openstreetmap), one for testing (osm_test) and one for production...'''
date = "2014-05-09T17:40:00Z"
lastmod = "2014-05-10T04:24:00Z"
weight = 33050
keywords = [ "website", "postgresql", "help", "database" ]
aliases = [ "/questions/33050" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Purposes of Rails Ports databases](/questions/33050/purposes-of-rails-ports-databases)

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
<span id="post-33050-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33050-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-33050-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi there!</p>
<p>I've installed openstreetmap's Rails Port to check it out and there's something related to the 3 databases it uses that I don't understand.</p>
<p>The INSTALL.md files indicates that this port uses 3 databases, one for development (openstreetmap), one for testing (osm_test) and one for production (osm), and the 3 databases should be created during the rake db:create step. This step successfully created the first two in my case (openstreetmap and osm_test) but the "osm" production database is not there. The rake run didn't gave any errors so I'd like to know if this is normal or there's something I'm missing.</p>
<p>Also, I'd like to know exactly what's the purpose of each database this port uses? I've looked here, the wiki and the web but it's not clear to me what's what because I've read many things, from slippy maps to mapnik rendered databases to database replicas.</p>
<p>If anyone could point me in the right direction or provide me with a link to understand better this setup I'd appreciate it very much.</p>
<p>Thanks in advance!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-website" rel="tag" title="see questions tagged &#39;website&#39;">website</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-help" rel="tag" title="see questions tagged &#39;help&#39;">help</span> <span class="post-tag tag-link-database" rel="tag" title="see questions tagged &#39;database&#39;">database</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 May '14, 17:40</strong></p>
<img src="https://secure.gravatar.com/avatar/d842faa4122aa24ed2d2486dc9967d52?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="edmv&#39;s gravatar image" />
<p><span>edmv</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="edmv has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-33050" class="comments-container">
&#10;</div>
<div id="comment-tools-33050" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33050-form-container" class="comment-form-container">
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

<span id="33051"></span>

<div id="answer-container-33051" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-33051-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33051-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-33051-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It's normal to find only the development and test databases created, since those are the ones you normally need when developing the software. In a production system you set the RAILS_ENV to production, and it'll create the only the production database.</p>
<p>This is a standard setup for Ruby on Rails apps, so there's little need for any documentation about it that's OpenStreetMap-specific. You'll find general information about Ruby on Rails and the database setup in guides and tutorials all over the web.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 May '14, 18:55</strong></p>
<img src="https://secure.gravatar.com/avatar/c3743b1b368f5e209eb8aad30164acc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Allan&#39;s gravatar image" />
<p><span>Andy Allan</span><br />
<span class="score" title="12456 reputation points"><span>12.5k</span></span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="128 badges"><span class="silver">●</span><span class="badgecount">128</span></span><span title="153 badges"><span class="bronze">●</span><span class="badgecount">153</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andy Allan has 46 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-33051" class="comments-container">
<span id="33062"></span>
<div id="comment-33062" class="comment">
<div id="post-33062-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Oh, that makes sense... so it's basically the same database as the others (schema, tables, etc...) am I right?</p>
<p>Thanks!</p>
</div>
<div id="comment-33062-info" class="comment-info">
<span class="comment-age">(10 May '14, 04:24)</span> <span class="comment-user userinfo">edmv</span>
</div>
</div>
</div>
<div id="comment-tools-33051" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33051-form-container" class="comment-form-container">
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


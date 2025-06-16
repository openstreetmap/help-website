+++
type = "question"
title = "OpenMapServer - all in own location installed - Ubuntu 12.4"
description = '''hi, I&#x27;am trying to import much data to map,  so not good idea to upload public map and jam system. I have Ubuntu 12.4 lts and installed openstreetmap software as well potlatch2. Openstreet ware need&#x27;s for potlatch2 at least oauth,... what else, is there instructions ? As undesrtood potlatch2 can onl...'''
date = "2013-07-29T11:16:00Z"
lastmod = "2013-08-01T11:37:00Z"
weight = 24679
keywords = [ "potlatch2", "precise", "private_server", "oauth", "ubuntu" ]
aliases = [ "/questions/24679" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [OpenMapServer - all in own location installed - Ubuntu 12.4](/questions/24679/openmapserver-all-in-own-location-installed-ubuntu-124)

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
<span id="post-24679-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24679-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-24679-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>hi,</p>
<p>I'am trying to import much data to map, so not good idea to upload public map and jam system.</p>
<p>I have Ubuntu 12.4 lts and installed openstreetmap software as well potlatch2.</p>
<p>Openstreet ware need's for potlatch2 at least oauth,... what else, is there instructions ? As undesrtood potlatch2 can only edit data at public server but not at own if not build for it, I figured out that oauth must be installed what elese?</p>
<p><a href="https://wiki.openstreetmap.org/wiki/Potlatch_2/Deploying_Potlatch_2">https://wiki.openstreetmap.org/wiki/Potlatch_2/Deploying_Potlatch_2</a></p>
<p>Also intrested to search by street name or object!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-potlatch2" rel="tag" title="see questions tagged &#39;potlatch2&#39;">potlatch2</span> <span class="post-tag tag-link-precise" rel="tag" title="see questions tagged &#39;precise&#39;">precise</span> <span class="post-tag tag-link-private_server" rel="tag" title="see questions tagged &#39;private_server&#39;">private_server</span> <span class="post-tag tag-link-oauth" rel="tag" title="see questions tagged &#39;oauth&#39;">oauth</span> <span class="post-tag tag-link-ubuntu" rel="tag" title="see questions tagged &#39;ubuntu&#39;">ubuntu</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Jul '13, 11:16</strong></p>
<img src="https://secure.gravatar.com/avatar/3ae465745919445d8b59aaa2075b7370?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="boy007&#39;s gravatar image" />
<p><span>boy007</span><br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="boy007 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Aug '13, 11:38</strong> </span></p>
</div>
</div>
<div id="comments-container-24679" class="comments-container">
&#10;</div>
<div id="comment-tools-24679" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24679-form-container" class="comment-form-container">
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

<span id="24718"></span>

<div id="answer-container-24718" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-24718-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24718-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-24718-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>hi,</p>
<p>Not working yet but,.. At least I/you need:</p>
<h1 id="oauth--">Oauth -</h1>
<p>sudo apt-get sqlite3 sudo apt-get install sqlite3 sudo apt-get install php5</p>
<p>svn co <a href="https://github.com/fkooman/oauth-install-all">https://github.com/fkooman/oauth-install-all</a></p>
<p>sudo mkdir /var/www/oauth sudo chown YOU:www-data /var/www/oauth cd oauth-install-all ./oauth-install-all /var/www/html/oauth <a href="http://mpi1/oauth">http://mpi1/oauth</a> sudo /etc/init.d/apache2 restart</p>
<h1 id="openlayers--">Openlayers -</h1>
<p><a href="http://openlayers.org/">http://openlayers.org/</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Jul '13, 09:41</strong></p>
<img src="https://secure.gravatar.com/avatar/3ae465745919445d8b59aaa2075b7370?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="boy007&#39;s gravatar image" />
<p><span>boy007</span><br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="boy007 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-24718" class="comments-container">
&#10;</div>
<div id="comment-tools-24718" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24718-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="24719"></span>

<div id="answer-container-24719" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-24719-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24719-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-24719-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<pre><code>To get Oauth work , who know&#39;s correct parameters:</code></pre>
<p>Here is incorrect settings:</p>
<h1 id="varwwwosmpotlatch2.html">/var/www/osm/potlatch2.html</h1>
<pre><code> args[&quot;api&quot;] = &quot;http://mpi1/api/0.6/&quot;;
      args[&quot;policy&quot;] = &quot;http://mpi1/oauth/php-grades-rs/api.php&quot;;
      args[&quot;connection&quot;] = &quot;XML&quot;;
      args[&quot;oauth_policy&quot;] = &quot;http://mpi1/oauth/php-oauth/introspect.php&quot;;
      args[&quot;oauth_request_url&quot;] = http://mpi1/oauth/php-oauth/token.php;
      args[&quot;oauth_access_url&quot;] = &quot;http://mpi1/oauth/php-oauth/token.php&quot;;
      args[&quot;oauth_auth_url&quot;] = &quot;http://mpi1/oauth/php-oauth/authorize.php&quot;;</code></pre>
<p>==== Here is <a href="http://mpi1/oauth/:">http://mpi1/oauth/:</a></p>
<pre><code>Service Information
URI     Description
Authorization Server [SRC]
http://mpi1/oauth/php-oauth/authorize.php   Authorize Endpoint
http://mpi1/oauth/php-oauth/token.php           Token Endpoint
http://mpi1/oauth/php-oauth/introspect.php  Introspection Endpoint, see Introspection Documentation
Resource Servers
http://mpi1/oauth/php-grades-rs/api.php     Grades API (documentation)</code></pre>
<p>If I get this worked out I add installation notes to <a href="http://boy007.dy.fi">http://boy007.dy.fi</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Jul '13, 09:51</strong></p>
<img src="https://secure.gravatar.com/avatar/3ae465745919445d8b59aaa2075b7370?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="boy007&#39;s gravatar image" />
<p><span>boy007</span><br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="boy007 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-24719" class="comments-container">
&#10;</div>
<div id="comment-tools-24719" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24719-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="24784"></span>

<div id="answer-container-24784" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-24784-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24784-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-24784-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>hi,</p>
<p>I'am stuck whit OAUTH,... can not ubnderstand which parameter at oauth match to one at potclatch2 !!!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Aug '13, 11:37</strong></p>
<img src="https://secure.gravatar.com/avatar/3ae465745919445d8b59aaa2075b7370?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="boy007&#39;s gravatar image" />
<p><span>boy007</span><br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="boy007 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-24784" class="comments-container">
&#10;</div>
<div id="comment-tools-24784" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24784-form-container" class="comment-form-container">
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


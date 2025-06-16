+++
type = "question"
title = "Two different nominatim setup on same server"
description = '''Hi All I need two different nominatim setup on same server with two difference database and different nominatim front end. Can it be possible. If yes then please guide me how to do this.'''
date = "2016-12-15T10:40:00Z"
lastmod = "2016-12-15T14:20:00Z"
weight = 53558
keywords = [ "nominatim" ]
aliases = [ "/questions/53558" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Two different nominatim setup on same server](/questions/53558/two-different-nominatim-setup-on-same-server)

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
<span id="post-53558-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53558-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-53558-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi All I need two different nominatim setup on same server with two difference database and different nominatim front end. Can it be possible. If yes then please guide me how to do this.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Dec '16, 10:40</strong></p>
<img src="https://secure.gravatar.com/avatar/67b647d369779ba2d1295917b920faae?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="himsashu&#39;s gravatar image" />
<p><span>himsashu</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="himsashu has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-53558" class="comments-container">
&#10;</div>
<div id="comment-tools-53558" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53558-form-container" class="comment-form-container">
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

<span id="53563"></span>

<div id="answer-container-53563" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53563-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53563-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-53563-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I assume you run the stable version 2.5.0 or 2.5.1 (<a href="http://www.nominatim.org/)">http://www.nominatim.org/)</a></p>
<ul>
<li><p>install the second Nominatim in a new (different) directory. See <a href="https://wiki.openstreetmap.org/wiki/Nominatim/Installation">https://wiki.openstreetmap.org/wiki/Nominatim/Installation</a></p></li>
<li><p>In the step "Customization of the Installation" use different settings: In <code>settings/local.php</code> change <code>CONST_Database_DSN</code> to use different database, for example <span><code>pgsql://postgres</code></span><code>@localhost:5432/nominatim_2</code> (see <code>settings.php</code> for the default value).</p></li>
<li><p>When you start the data import from the new directory it will read the settings.php and local.php file and write to that database. If the database name already exists it will NOT overwrite it (that's good).</p></li>
<li><p>You need two configurations in your Apache configuration. It should be enough to copy the existing block and change the URL path and installation directory.</p></li>
<li><p>In the <code>local.php</code> set the <code>CONST_Website_BaseURL</code> to the URL you set in the Apache configuration.</p></li>
</ul>
<p>If that doesn't work report problems to <a href="https://github.com/twain47/Nominatim/issues">https://github.com/twain47/Nominatim/issues</a></p>
<p>P.S. it's possible to merge two countries and use one installation, that might be easier <a href="/questions/48843/merging-two-or-more-geographical-areas-to-import-two-or-more-osm-files-in-nominatim">https://help.openstreetmap.org/questions/48843/merging-two-or-more-geographical-areas-to-import-two-or-more-osm-files-in-nominatim</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Dec '16, 14:20</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-53563" class="comments-container">
&#10;</div>
<div id="comment-tools-53563" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53563-form-container" class="comment-form-container">
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


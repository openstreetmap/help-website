+++
type = "question"
title = "How to keep a local modified database in sync with osm database"
description = '''I imported a planet pbf into my local PostgreSQL database and need to do some private update (creation, modification and deletion) because of my business needs. However, I want to keep the local database in sync with osm official database periodically. It can be weekly, even monthly. Is there any be...'''
date = "2018-07-04T07:39:00Z"
lastmod = "2018-07-04T10:17:00Z"
weight = 64519
keywords = [ "import", "merge", "postgresql", "database" ]
aliases = [ "/questions/64519" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to keep a local modified database in sync with osm database](/questions/64519/how-to-keep-a-local-modified-database-in-sync-with-osm-database)

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
<span id="post-64519-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64519-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-64519-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I imported a planet pbf into my local PostgreSQL database and need to do some private update (creation, modification and deletion) because of my business needs. However, I want to keep the local database in sync with osm official database periodically. It can be weekly, even monthly. Is there any best way to do that?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-merge" rel="tag" title="see questions tagged &#39;merge&#39;">merge</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-database" rel="tag" title="see questions tagged &#39;database&#39;">database</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Jul '18, 07:39</strong></p>
<img src="https://secure.gravatar.com/avatar/da3884db18af886e3d0c0a692e35b788?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hanson&#39;s gravatar image" />
<p><span>Hanson</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hanson has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Jul '18, 07:44</strong> </span></p>
</div>
</div>
<div id="comments-container-64519" class="comments-container">
<span id="64522"></span>
<div id="comment-64522" class="comment">
<div id="post-64522-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Please clarify how you want to proceed in these cases:</p>
<ul>
<li>An object you deleted locally has been modified in OSM?</li>
<li>An object you created locally has meanwhile also been created in OSM?</li>
<li>An object you modified locally has been modified in a different way in OSM?</li>
</ul>
</div>
<div id="comment-64522-info" class="comment-info">
<span class="comment-age">(04 Jul '18, 07:57)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="64526"></span>
<div id="comment-64526" class="comment">
<div id="post-64526-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/104/frederik-ramm"></a><a href="https://help.openstreetmap.org/users/104/frederik-ramm"></a><a href="https://help.openstreetmap.org/users/104/frederik-ramm">@Frederik Ramm</a> ♦ Thank you for your reminder. It will include these cases:</p>
<ol>
<li>An object deleted locally has been modified in OSM</li>
<li>An object created locally but does not exist in OSM</li>
<li>An object modified locally has been modified in a different way in OSM</li>
<li>An object created locally and its id maybe conflict with another new object in OSM, but they are different completely</li>
</ol>
</div>
<div id="comment-64526-info" class="comment-info">
<span class="comment-age">(04 Jul '18, 10:17)</span> <span class="comment-user userinfo">Hanson</span>
</div>
</div>
</div>
<div id="comment-tools-64519" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64519-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>


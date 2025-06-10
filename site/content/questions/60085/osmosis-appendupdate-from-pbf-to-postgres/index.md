+++
type = "question"
title = "Osmosis append/update from .pbf to Postgres"
description = '''I don&#x27;t known if I&#x27;m using Osmosis right, but I wan&#x27;t to import only some countries from geofabrik ( .osm.pbf ) The first import work great, but when trying another country, Osmosis raise an error about duplicated primary key  StatementCallback; SQL [ALTER TABLE ONLY nodes ADD CONSTRAINT pk_nodes PR...'''
date = "2017-10-12T12:06:00Z"
lastmod = "2017-10-12T12:06:00Z"
weight = 60085
keywords = [ "import", "postgresql", "osmosis" ]
aliases = [ "/questions/60085" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Osmosis append/update from .pbf to Postgres](/questions/60085/osmosis-appendupdate-from-pbf-to-postgres)

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
<span id="post-60085-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60085-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-60085-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I don't known if I'm using Osmosis right, but I wan't to import only some countries from geofabrik ( .osm.pbf )</p>
<p>The first import work great, but when trying another country, Osmosis raise an error about duplicated primary key</p>
<p><code>StatementCallback; SQL [ALTER TABLE ONLY nodes ADD CONSTRAINT pk_nodes PRIMARY KEY (id)]; ERROR: could not create unique index "pk_nodes" Detail: Key (id)=(4077266959) is duplicated.; nested exception is org.postgresql.util.PSQLException: ERROR: could not create unique index "pk_nodes"</code></p>
<p>I searched about append/update data to Postgres but I found nothing and I wonder if I can achieve that with osmosis ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Oct '17, 12:06</strong></p>
<img src="https://secure.gravatar.com/avatar/4ccf71625ef04731439310cc1cecabbc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="m4tmat&#39;s gravatar image" />
<p><span>m4tmat</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="m4tmat has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-60085" class="comments-container">
&#10;</div>
<div id="comment-tools-60085" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60085-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>


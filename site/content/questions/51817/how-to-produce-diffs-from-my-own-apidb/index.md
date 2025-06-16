+++
type = "question"
title = "How to  produce diffs from my own apidb?"
description = '''I have asked a question here. I want edit my owm map, and i know that when i saved the edit, the changeset saved in the rails port database, if i want to see the changeset on the tile server, i should produce diffs from my own apidb and consume them on the postgis db. I run the followed command, and...'''
date = "2016-08-30T10:22:00Z"
lastmod = "2016-08-30T10:22:00Z"
weight = 51817
keywords = [ "osmosis" ]
aliases = [ "/questions/51817" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to produce diffs from my own apidb?](/questions/51817/how-to-produce-diffs-from-my-own-apidb)

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
<span id="post-51817-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51817-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-51817-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have asked a question <a href="/questions/51645/whats-the-relationship-between-database-used-in-the-rails-port-database-used-in-the-tile-server-and-datavase-used-in-the-nominatim">here</a>. I want edit my owm map, and i know that when i saved the edit, the changeset saved in the rails port database, if i want to see the changeset on the tile server, i should produce diffs from my own apidb and consume them on the postgis db. I run the followed command, and i can see the changes in the tile server.</p>
<p><strong>1)./osmosis-latest/bin/osmosis --read-apidb host="localhost" database="openstreetmap" user="osm" password="buaanlp" --write-pbf file="beijing.osm.pbf" 2)./osmosis-latest/bin/osmosis --read-pbf file="beijing.osm.pbf" --read-pbf file="planet/beijing_china.osm.pbf" --derive-change --write-pbf-change file="diff1.osc" 3)./osmosis-latest/bin/osmosis --read-pbf file="beijing.osm.pbf" --read-pbf file="planet/beijing_china.osm.pbf" --derive-change --write-xml-change file="diff1.osc" 4}osm2pgsql --append --slim -d gis -C 160 --number-processes 3 diff1.osc</strong></p>
<p>But i think the progress is time-consuming, each time i make a edit then i need to run these four command. So can someone teach me more appropriate method instead? thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Aug '16, 10:22</strong></p>
<img src="https://secure.gravatar.com/avatar/3522efac952d508cf251cd2590e68ca5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yuyy&#39;s gravatar image" />
<p><span>yuyy</span><br />
<span class="score" title="236 reputation points">236</span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="31 badges"><span class="bronze">●</span><span class="badgecount">31</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yuyy has one accepted answer">20%</span></p>
</div>
</div>
<div id="comments-container-51817" class="comments-container">
&#10;</div>
<div id="comment-tools-51817" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51817-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>


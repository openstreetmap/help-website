+++
type = "question"
title = "Nominatim Installation"
description = '''Hi, I try to install nominatim server by this tutorial . My hardware Ubuntu 14.04, 32bit, 4gbram, 488gbmemory. But i have faced with this problem :  osm2pgsql SVN version 0.89.0-dev (64bit id space)  Using projection SRS 4326 (Latlong) NOTICE: table &quot;place&quot; does not exist, skipping Allocating memory...'''
date = "2017-02-19T11:11:00Z"
lastmod = "2017-02-19T14:41:00Z"
weight = 54717
keywords = [ "installation", "nominatim", "osm" ]
aliases = [ "/questions/54717" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Nominatim Installation](/questions/54717/nominatim-installation)

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
<span id="post-54717-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54717-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-54717-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I try to install nominatim server by this <a href="http://wiki.openstreetmap.org/wiki/Nominatim/Installation">tutorial</a> . My hardware Ubuntu 14.04, 32bit, 4gbram, 488gbmemory. But i have faced with this problem : osm2pgsql SVN version 0.89.0-dev (64bit id space)</p>
<blockquote>
<p>Using projection SRS 4326 (Latlong) NOTICE: table "place" does not exist, skipping Allocating memory for sparse node cache Node-cache: cache=18000MB, maxblocks=0*2304000, allocation method=8192 Mid: loading persistent node cache from /home/agentmonitoring/Desktop/Nominatim-2.5.1/CONST_Osm2pgsql_Flatnode_File Failed to allocate space for node cache file: Internal error 22 Error occurred, cleaning up ERROR: Error executing external command: /home/agentmonitoring/Desktop/Nominatim-2.5.1/osm2pgsql/osm2pgsql --flat-nodes /home/agentmonitoring/Desktop/Nominatim-2.5.1/CONST_Osm2pgsql_Flatnode_File -lsc -O gazetteer --hstore --number-processes 1 -C 18000 -P 5432 -d nominatim /home/agentmonitoring/Desktop/planet-latest.osm.pbf Error executing external command: /home/agentmonitoring/Desktop/Nominatim-2.5.1/osm2pgsql/osm2pgsql --flat-nodes /home/agentmonitoring/Desktop/Nominatim-2.5.1/CONST_Osm2pgsql_Flatnode_File -lsc -O gazetteer --hstore --number-processes 1 -C 18000 -P 5432 -d nominatim /home/agentmonitoring/Desktop/planet-latest.osm.pbf</p>
</blockquote>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-installation" rel="tag" title="see questions tagged &#39;installation&#39;">installation</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Feb '17, 11:11</strong></p>
<img src="https://secure.gravatar.com/avatar/25789a7efda8d55334d42f0d07916edf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kilik94&#39;s gravatar image" />
<p><span>kilik94</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kilik94 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-54717" class="comments-container">
&#10;</div>
<div id="comment-tools-54717" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54717-form-container" class="comment-form-container">
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

<span id="54723"></span>

<div id="answer-container-54723" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-54723-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54723-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-54723-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Your machine is underpowered. For the full planet 32GB RAM and 800GB disk space is recommended. <a href="https://wiki.openstreetmap.org/wiki/Nominatim/Installation#Hardware">https://wiki.openstreetmap.org/wiki/Nominatim/Installation#Hardware</a> If you see further installation problems you can contact <a href="https://github.com/twain47/Nominatim/issues">https://github.com/twain47/Nominatim/issues</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Feb '17, 14:09</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-54723" class="comments-container">
<span id="54724"></span>
<div id="comment-54724" class="comment">
<div id="post-54724-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have same error when i try to install luxembourg.osb.pbf</p>
</div>
<div id="comment-54724-info" class="comment-info">
<span class="comment-age">(19 Feb '17, 14:13)</span> <span class="comment-user userinfo">kilik94</span>
</div>
</div>
<span id="54727"></span>
<div id="comment-54727" class="comment">
<div id="post-54727-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>When you run the setup.php command with <code>--osm2pgsql-cache 18000</code> it will try to allocate 18GB of RAM. You can try <code>--osm2pgsql-cache 3000</code> or maybe 2000.</p>
</div>
<div id="comment-54727-info" class="comment-info">
<span class="comment-age">(19 Feb '17, 14:41)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
</div>
<div id="comment-tools-54723" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54723-form-container" class="comment-form-container">
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


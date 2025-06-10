+++
type = "question"
title = "How to find the neighbouring nodes of a particular node"
description = '''I have imported the osm file into postgresql. The tables I have are planet_osm_ndes,planet_osm_ways, planet_osm_point. planet_osm_roads etc. But no table contains the information of neighbouring nodes of a node. I tried connecting to the database using java and tried finding the neighbours, but the ...'''
date = "2018-02-12T03:21:00Z"
lastmod = "2018-02-12T09:54:00Z"
weight = 62052
keywords = [ "postgresql", "postgis", "sql" ]
aliases = [ "/questions/62052" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to find the neighbouring nodes of a particular node](/questions/62052/how-to-find-the-neighbouring-nodes-of-a-particular-node)

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
<span id="post-62052-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62052-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62052-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have imported the osm file into postgresql. The tables I have are planet_osm_ndes,planet_osm_ways, planet_osm_point. planet_osm_roads etc. But no table contains the information of neighbouring nodes of a node. I tried connecting to the database using java and tried finding the neighbours, but the code runs for hrs and still no output. Is there a easy way to do it</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span> <span class="post-tag tag-link-sql" rel="tag" title="see questions tagged &#39;sql&#39;">sql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Feb '18, 03:21</strong></p>
<img src="https://secure.gravatar.com/avatar/f127cb55254ea987afe0545099b25f87?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="batraj&#39;s gravatar image" />
<p><span>batraj</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="batraj has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Feb '18, 03:22</strong> </span></p>
</div>
</div>
<div id="comments-container-62052" class="comments-container">
&#10;</div>
<div id="comment-tools-62052" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62052-form-container" class="comment-form-container">
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

<span id="62053"></span>

<div id="answer-container-62053" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-62053-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62053-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-62053-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The osm2pgsql database schema is optimised for drawing maps; for this use case, neighbouring nodes are uninteresting. If you have used the <code>--slim</code> flag on osm2pgsql (which you apparently have since you mention planet_osm_nodes), you <em>can</em> look at the "nodes" array of ways in planet_osm_ways (step 1: find out which ways contain your node of interest, step 2: find out where in the node list your node occurs, step 3: find the nodes before and after, if applicable). However, it sounds as if your use case might warrant a different kind of database import that gives you easier access to the node/way connections, for example check out the "ApiDB" import offered by Osmosis.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Feb '18, 09:54</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-62053" class="comments-container">
&#10;</div>
<div id="comment-tools-62053" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62053-form-container" class="comment-form-container">
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


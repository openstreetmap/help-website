+++
type = "question"
title = "Node exists on OSM, but Nominatim lookup returns empty"
description = '''Hello - Thanks in advance for any light you can shed on this issue.  I&#x27;ve encountered an issue pulling down node metadata from Nominatim:  Node exists -&amp;gt; https://www.openstreetmap.org/node/1984103891 Node metadata exists -&amp;gt; https://www.openstreetmap.org/api/0.6/node/1984103891 Place exists in ...'''
date = "2018-11-01T12:54:00Z"
lastmod = "2018-11-01T14:47:00Z"
weight = 66613
keywords = [ "reversegeocoding", "nodes", "nominatim", "lookup" ]
aliases = [ "/questions/66613" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Node exists on OSM, but Nominatim lookup returns empty](/questions/66613/node-exists-on-osm-but-nominatim-lookup-returns-empty)

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
<span id="post-66613-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66613-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-66613-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello - Thanks in advance for any light you can shed on this issue.</p>
<p>I've encountered an issue pulling down node metadata from Nominatim:</p>
<ol>
<li>Node exists -&gt; <a href="https://www.openstreetmap.org/node/1984103891">https://www.openstreetmap.org/node/1984103891</a></li>
<li>Node metadata exists -&gt; <a href="https://www.openstreetmap.org/api/0.6/node/1984103891">https://www.openstreetmap.org/api/0.6/node/1984103891</a></li>
<li>Place exists in Nominatim, referencing the node: <a href="https://nominatim.openstreetmap.org/lookup?place_id=20053249">https://nominatim.openstreetmap.org/lookup?place_id=20053249</a></li>
<li>BUT nothing returned from a node lookup Nominatim -&gt;<a href="https://nominatim.openstreetmap.org/lookup?osm_ids=N1984103891">https://nominatim.openstreetmap.org/lookup?osm_ids=N1984103891</a></li>
</ol>
<p>What am I doing missing here?</p>
<p>Thanks again!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-reversegeocoding" rel="tag" title="see questions tagged &#39;reversegeocoding&#39;">reversegeocoding</span> <span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-lookup" rel="tag" title="see questions tagged &#39;lookup&#39;">lookup</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Nov '18, 12:54</strong></p>
<img src="https://secure.gravatar.com/avatar/c4b5c8009c3481019d2776407d63b80f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tlsfm&#39;s gravatar image" />
<p><span>tlsfm</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tlsfm has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-66613" class="comments-container">
&#10;</div>
<div id="comment-tools-66613" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66613-form-container" class="comment-form-container">
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

<span id="66614"></span>

<div id="answer-container-66614" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66614-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66614-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-66614-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>With (3) the URL actually returns to an empty result.</p>
<p>Nominatim links place nodes and relations together when they represent the same. It looks at relation role admin_centre. In this case it gets linked to <a href="https://nominatim.openstreetmap.org/details.php?osmtype=R&amp;osmid=5996511&amp;class=boundary">https://nominatim.openstreetmap.org/details.php?osmtype=R&amp;osmid=5996511&amp;class=boundary</a> On the small map you can see the center point is not the geographical center of the polygon but the coordinate of the linked node.</p>
<p>The /lookup endpoint doesn't seem to follow the link when querying by OSM type and OSM id. Or maybe it shouldn't because it would then return another OSM object (the relation).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Nov '18, 13:30</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-66614" class="comments-container">
<span id="66615"></span>
<div id="comment-66615" class="comment">
<div id="post-66615-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I'd definitely call this a bug. Please report it on <a href="https://github.com/openstreetmap/Nominatim/issues">https://github.com/openstreetmap/Nominatim/issues</a></p>
</div>
<div id="comment-66615-info" class="comment-info">
<span class="comment-age">(01 Nov '18, 13:33)</span> <span class="comment-user userinfo">lonvia</span>
</div>
</div>
<span id="66616"></span>
<div id="comment-66616" class="comment">
<div id="post-66616-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the quick responses.</p>
<p>I'm still a little lost about why XML is missing in Nominatim... bear with me ....</p>
<p>So, I want the metadata for this node (Kyaukpyu)</p>
<p>1984103891</p>
<p>In OSM this defined as the admin centre of both Kyaukpyu District and Kyaukpyu Township. Might this be a problem?</p>
</div>
<div id="comment-66616-info" class="comment-info">
<span class="comment-age">(01 Nov '18, 14:16)</span> <span class="comment-user userinfo">tlsfm</span>
</div>
</div>
<span id="66617"></span>
<div id="comment-66617" class="comment">
<div id="post-66617-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Nominatim has the full data of the node in its database. It's a bug if no result is returned for a direct /lookup query.</p>
</div>
<div id="comment-66617-info" class="comment-info">
<span class="comment-age">(01 Nov '18, 14:21)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
<span id="66618"></span>
<div id="comment-66618" class="comment">
<div id="post-66618-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>OK, thanks <a href="https://help.openstreetmap.org/users/150/mtmail">@mtmail</a> <a href="https://help.openstreetmap.org/users/2921/lonvia">@lonvia</a>... over to the issue queue I go.</p>
</div>
<div id="comment-66618-info" class="comment-info">
<span class="comment-age">(01 Nov '18, 14:27)</span> <span class="comment-user userinfo">tlsfm</span>
</div>
</div>
<span id="66619"></span>
<div id="comment-66619" class="comment">
<div id="post-66619-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Tracking it here: <a href="https://github.com/openstreetmap/Nominatim/issues/1222">https://github.com/openstreetmap/Nominatim/issues/1222</a></p>
</div>
<div id="comment-66619-info" class="comment-info">
<span class="comment-age">(01 Nov '18, 14:47)</span> <span class="comment-user userinfo">tlsfm</span>
</div>
</div>
</div>
<div id="comment-tools-66614" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66614-form-container" class="comment-form-container">
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


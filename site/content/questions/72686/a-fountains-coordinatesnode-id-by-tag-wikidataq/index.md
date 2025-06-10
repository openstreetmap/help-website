+++
type = "question"
title = "a fountain&#x27;s coordinates/node id by tag wikidata=Q..."
description = '''sorry for the newbie question. What would be the overpass query to get the following: For example https://www.openstreetmap.org/node/7158766201 it should be found by solely handing over &quot;Q83630092&quot; and the query should return the &quot;Location&quot; coordinates and optionally also &#x27;7158766201&#x27; as a collatera...'''
date = "2020-01-26T09:03:00Z"
lastmod = "2020-01-26T11:19:00Z"
weight = 72686
keywords = [ "overpass", "wikidata" ]
aliases = [ "/questions/72686" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [a fountain's coordinates/node id by tag wikidata=Q...](/questions/72686/a-fountains-coordinatesnode-id-by-tag-wikidataq)

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
<span id="post-72686-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72686-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-72686-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>sorry for the newbie question.</p>
<p>What would be the overpass query to get the following:</p>
<p>For example <a href="https://www.openstreetmap.org/node/7158766201">https://www.openstreetmap.org/node/7158766201</a></p>
<p>it should be found by solely handing over "Q83630092" and the query should return the "Location" coordinates and optionally also '7158766201'</p>
<p>as a collateral, we might restrict the results to amentiy "fountain" or "drinking_water" .</p>
<p>Any help would be highly appreciated.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-wikidata" rel="tag" title="see questions tagged &#39;wikidata&#39;">wikidata</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Jan '20, 09:03</strong></p>
<img src="https://secure.gravatar.com/avatar/802d4b8327c309d72d4136f72d17aef1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ralfhauser&#39;s gravatar image" />
<p><span>ralfhauser</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ralfhauser has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Jan '20, 10:30</strong> </span></p>
</div>
</div>
<div id="comments-container-72686" class="comments-container">
&#10;</div>
<div id="comment-tools-72686" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72686-form-container" class="comment-form-container">
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

<span id="72687"></span>

<div id="answer-container-72687" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72687-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72687-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-72687-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi</p>
<p>This is the correct place for newbie questions.</p>
<p>This will return what you want:</p>
<pre><code>node[amenity=fountain][wikidata=Q83630092];
out center;</code></pre>
<p><a href="https://overpass-turbo.eu/s/Q62">https://overpass-turbo.eu/s/Q62</a></p>
<p>If you don't know if the entity was mapped as a single point, swap <code>node</code> for <code>nwr</code> (Node, Way, Relation),</p>
<p>If you want to search for all in area of visible screen:</p>
<pre><code>[bbox:{{bbox}}];
nwr[amenity=fountain][wikidata];
out geom;</code></pre>
<p><a href="https://overpass-turbo.eu/s/Q64">https://overpass-turbo.eu/s/Q64</a></p>
<p>You should be able to work out how to filter for <code>drinking_water</code> from these examples.</p>
<p>If you want to output as a CSV list, add <code>[out:csv(::id, "name", "wikidata"; false; ",")]</code> as line one.</p>
<p>To tie in with your other posted question - to find entities which don't have <code>name</code> (or <code>wikipedia</code>) tags add an exclamation mark:</p>
<pre><code>[bbox:{{bbox}}];
nwr[amenity=fountain][wikidata][!name];
out geom;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Jan '20, 11:19</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Jan '20, 11:43</strong> </span></p>
</div>
</div>
<div id="comments-container-72687" class="comments-container">
&#10;</div>
<div id="comment-tools-72687" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72687-form-container" class="comment-form-container">
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


+++
type = "question"
title = "Addresses as nodes and addresses with buildings"
description = '''So, there&#x27;s recently been a big address information import from the local geo-agency into OSM (LINZ in New Zealand, Christchurch area). THose are all imported as simple nodes (addr:housenumber; addr:street; addr:suburb; ref:linz:address_id). Time by time I&#x27;m adding buildings, places etc. to the map ...'''
date = "2018-02-16T04:53:00Z"
lastmod = "2018-02-18T07:28:00Z"
weight = 62134
keywords = [ "merge", "nodes", "editing", "buildings", "address" ]
aliases = [ "/questions/62134" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Addresses as nodes and addresses with buildings](/questions/62134/addresses-as-nodes-and-addresses-with-buildings)

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
<span id="post-62134-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62134-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-62134-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
2
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>So, there's recently been a big address information import from the local geo-agency into OSM (LINZ in New Zealand, Christchurch area). THose are all imported as simple nodes (addr:housenumber; addr:street; addr:suburb; ref:linz:address_id).</p>
<p>Time by time I'm adding buildings, places etc. to the map and I'm now wondering, what should I do now, in the case I'm either adding a new building and addressing it or adding an address to an existing building. Should I delete the separate address node (in this case I would simply merge the building and the address node, effectively adding the node info to the building and deleting the node) or leave it be?</p>
<p>If I leave them, it does create duplicate addresses on the map and adds clutter to it. But if I delete them, that could create a situation where the address information could be lost after building it was associated with gets demolished or removed for other reasons.</p>
<p>Example area on map: <a href="https://www.openstreetmap.org/#map=19/-43.50715/172.72978">https://www.openstreetmap.org/#map=19/-43.50715/172.72978</a> How it looks in edit mode: <img src="https://i.imgur.com/QLU19xN.jpg" alt="edit mode" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-merge" rel="tag" title="see questions tagged &#39;merge&#39;">merge</span> <span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-editing" rel="tag" title="see questions tagged &#39;editing&#39;">editing</span> <span class="post-tag tag-link-buildings" rel="tag" title="see questions tagged &#39;buildings&#39;">buildings</span> <span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Feb '18, 04:53</strong></p>
<img src="https://secure.gravatar.com/avatar/83a407005b50f4aec7b7ab0769089d5c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ivss_xx&#39;s gravatar image" />
<p><span>ivss_xx</span><br />
<span class="score" title="311 reputation points">311</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ivss_xx has 2 accepted answers">25%</span></p>
</img>
</div>
</div>
<div id="comments-container-62134" class="comments-container">
&#10;</div>
<div id="comment-tools-62134" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62134-form-container" class="comment-form-container">
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

<span id="62140"></span>

<div id="answer-container-62140" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-62140-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62140-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-62140-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ivss_xx has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you have more than one address associated with a building the current consensus is to map these as nodes inside the building outline, in the case of a single address there are (some time heated) arguments both ways.</p>
<p>In the end, because both models are popular (41 million nodes vs 35 million on polygons), any data consumer needs to be able to deal with both, and so really it boils down to a matter of taste and local convention.</p>
<p>Personalty given that the nodes were imported I would leave them like that.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Feb '18, 09:36</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Feb '18, 09:38</strong> </span></p>
</div>
</div>
<div id="comments-container-62140" class="comments-container">
<span id="62180"></span>
<div id="comment-62180" class="comment">
<div id="post-62180-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>So, I guess, in the case when I'm adding a building to the map or simply adding information to an existing one, I'll just add the address to the building polygon and leave the the address node there as well.</p>
</div>
<div id="comment-62180-info" class="comment-info">
<span class="comment-age">(18 Feb '18, 07:28)</span> <span class="comment-user userinfo">ivss_xx</span>
</div>
</div>
</div>
<div id="comment-tools-62140" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62140-form-container" class="comment-form-container">
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


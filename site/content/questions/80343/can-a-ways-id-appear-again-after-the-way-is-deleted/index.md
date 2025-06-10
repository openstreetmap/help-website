+++
type = "question"
title = "Can a way&#x27;s ID appear again after the way is deleted?"
description = '''I already know the ID of a node can reappear after the node has been deleted. For example, node 1 has travelled across the world, being located at all kinds of locations at various times. But I couldn&#x27;t find such an example for ways. Can it occur that the ID of a deleted way is used again for a newl...'''
date = "2021-05-28T14:41:00Z"
lastmod = "2021-05-31T10:29:00Z"
weight = 80343
keywords = [ "ways", "id", "osm_id", "location", "delete" ]
aliases = [ "/questions/80343" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Can a way's ID appear again after the way is deleted?](/questions/80343/can-a-ways-id-appear-again-after-the-way-is-deleted)

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
<span id="post-80343-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80343-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-80343-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I already know the ID of a node can reappear after the node has been deleted. For example, <a href="https://pewu.github.io/osm-history/#/node/1">node 1 has travelled across the world</a>, being located at all kinds of locations at various times.</p>
<p>But I couldn't find such an example for ways. Can it occur that the ID of a deleted way is used again for a newly created way? Did this happen in the past and can it happen again in the future?</p>
<p>Or is there any example of a way ID being used at different times at very different locations in the world (with or without a deletion in between)?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span> <span class="post-tag tag-link-id" rel="tag" title="see questions tagged &#39;id&#39;">id</span> <span class="post-tag tag-link-osm_id" rel="tag" title="see questions tagged &#39;osm_id&#39;">osm_id</span> <span class="post-tag tag-link-location" rel="tag" title="see questions tagged &#39;location&#39;">location</span> <span class="post-tag tag-link-delete" rel="tag" title="see questions tagged &#39;delete&#39;">delete</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 May '21, 14:41</strong></p>
<img src="https://secure.gravatar.com/avatar/6ddb3ffa68da77e22f967daac3e2ea40?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="flogoe&#39;s gravatar image" />
<p><span>flogoe</span><br />
<span class="score" title="76 reputation points">76</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="flogoe has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 May '21, 14:44</strong> </span></p>
</div>
</div>
<div id="comments-container-80343" class="comments-container">
&#10;</div>
<div id="comment-tools-80343" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80343-form-container" class="comment-form-container">
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

<span id="80346"></span>

<div id="answer-container-80346" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80346-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80346-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-80346-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="flogoe has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I've seen POI nodes relocated when, for instance, a restaurant moves -- sometimes a mapper will simply drag the node from the old location to the new location, keeping all the same tags (other than address, hopefully, if the original node had address tags.) And one could imagine a deletion in between, ie, one mapper notices a restaurant is closd and deletes its node, and another mapper reverts the deletion then moves the node to the new location.</p>
<p>This same process could happen to a restaurant mapped as way -- as a building, for instance. It could be deleted, the deletion could be reverted, and the way could be moved to another location. Sometimes buildings do move (generally not all the way across the globe of course) and if so this might actually be the preferred way to map that. A mapper might also choose to do this so that the <a href="https://www.openstreetmap.org/way/ID#">https://www.openstreetmap.org/way/ID#</a> link to the previous location would still work for the new location.</p>
<p>I don't know of any examples.</p>
<p>But in short: Yes, any deleted way can be reused by reverting the deletion, and might also change location. This probably won't happen, though, unless a mapper is doing it intentionally. It won't happen "naturally" when a new way is created.</p>
<p>[Edit - it's important to remember that ways don't actually have a location, only nodes do. Ways simply have an ordered list of nodes. So if nodes can move across the globe, you should assume that ways can too.]</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 May '21, 22:12</strong></p>
<img src="https://secure.gravatar.com/avatar/977d95e2184a885d9a01fb3297225872?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jmapb&#39;s gravatar image" />
<p><span>jmapb</span><br />
<span class="score" title="3387 reputation points"><span>3.4k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="61 badges"><span class="bronze">●</span><span class="badgecount">61</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jmapb has 22 accepted answers">22%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 May '21, 23:24</strong> </span></p>
</div>
</div>
<div id="comments-container-80346" class="comments-container">
&#10;</div>
<div id="comment-tools-80346" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80346-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="80344"></span>

<div id="answer-container-80344" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80344-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80344-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-80344-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Technically, there's no reason why it couldn't happen with ways (or relations) too, but I don't know of any examples.</p>
<p>Nodes get "reused" for one of two reasons - deliberately (in the case of node 1 and some other low-numbered nodes) and by accident. "By accident" typically happens when someone messes up object IDs in JOSM when doing an import, and it can cause features to "be resurrected" or to "jump across the world". Sometimes people update multiple OSM servers (the "real" one and dev server used for test edits at <a href="https://api06.dev.openstreetmap.org"></a><a href="https://api06.dev.openstreetmap.org">https://api06.dev.openstreetmap.org</a> , for example) and if edits supposed to go to one go to the other by mistake then objects can "move" by mstake.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 May '21, 14:52</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-80344" class="comments-container">
<span id="80347"></span>
<div id="comment-80347" class="comment">
<div id="post-80347-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>To clarify this a bit:</p>
<ul>
<li>the API does not reuse ids of its own accord, including those of deleted or redacted objects,</li>
<li>a user/editing app can however reuse an id that it knows of, creating a new version that has no direct relationship with the previous one (regardless of the current state of the element).</li>
</ul>
<p>The later can happen due to issues with the app, issues with the data (uploading objects with conflicting ids), and naturally by the user forcing it (for fun or maliciously).</p>
</div>
<div id="comment-80347-info" class="comment-info">
<span class="comment-age">(29 May '21, 08:46)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-80344" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80344-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="80359"></span>

<div id="answer-container-80359" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80359-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80359-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-80359-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I eventually found an example of a way that has moved significantly (from Romania to Germany): <a href="https://pewu.github.io/osm-history/#/way/23319192">https://pewu.github.io/osm-history/#/way/23319192</a></p>
<p>Adding it here in case it proves useful to someone. Thanks for the other answers!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 May '21, 10:29</strong></p>
<img src="https://secure.gravatar.com/avatar/6ddb3ffa68da77e22f967daac3e2ea40?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="flogoe&#39;s gravatar image" />
<p><span>flogoe</span><br />
<span class="score" title="76 reputation points">76</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="flogoe has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-80359" class="comments-container">
&#10;</div>
<div id="comment-tools-80359" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80359-form-container" class="comment-form-container">
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


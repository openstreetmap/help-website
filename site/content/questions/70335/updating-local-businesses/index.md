+++
type = "question"
title = "updating local businesses"
description = '''I would like to update many businesses in my neighborhood as it appears most of the town hasn&#x27;t been updated for a while.  In looking up best practices, I saw that a good suggestion was to move businesses that had moved to their new location (from: https://help.openstreetmap.org/questions/29089/how-...'''
date = "2019-08-07T17:01:00Z"
lastmod = "2019-08-09T15:56:00Z"
weight = 70335
keywords = [ "moving", "businesses", "bestpractice", "business", "old_name" ]
aliases = [ "/questions/70335" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [updating local businesses](/questions/70335/updating-local-businesses)

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
<span id="post-70335-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70335-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-70335-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I would like to update many businesses in my neighborhood as it appears most of the town hasn't been updated for a while.</p>
<p>In looking up best practices, I saw that a good suggestion was to move businesses that had moved to their new location (from: <a href="https://help.openstreetmap.org/questions/29089/how-to-indicate-that-restaurant-moved">https://help.openstreetmap.org/questions/29089/how-to-indicate-that-restaurant-moved</a>). At this point, I have perhaps 50-100+ (maybe far more) deprecated shops and amenities that show up on OSM. I don't know where most of them went.</p>
<p>My plan is to change the information to the new businesses and use 'old_name=*' tag to show the shop/amenity that used to be there.</p>
<p>Does it make sense to do it this way? I found it quite difficult to individually look up where the old businesses had gone or whether they had simply closed their doors for good.</p>
<p>any and all tips would be helpful. I am simply trying to keep my home updated in OSM.</p>
<p>As an aside, I am planning on using a combination of JOSM, ID, and Vespucci to accomplish this with Outside personal surveying. Does anyone have any suggestions on the best way to accomplish this?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-moving" rel="tag" title="see questions tagged &#39;moving&#39;">moving</span> <span class="post-tag tag-link-businesses" rel="tag" title="see questions tagged &#39;businesses&#39;">businesses</span> <span class="post-tag tag-link-bestpractice" rel="tag" title="see questions tagged &#39;bestpractice&#39;">bestpractice</span> <span class="post-tag tag-link-business" rel="tag" title="see questions tagged &#39;business&#39;">business</span> <span class="post-tag tag-link-old_name" rel="tag" title="see questions tagged &#39;old_name&#39;">old_name</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Aug '19, 17:01</strong></p>
<img src="https://secure.gravatar.com/avatar/0b69645766408b3d054bc586362170d7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="OSMWeekly&#39;s gravatar image" />
<p><span>OSMWeekly</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="OSMWeekly has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-70335" class="comments-container">
&#10;</div>
<div id="comment-tools-70335" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70335-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="70356"></span>

<div id="answer-container-70356" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70356-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70356-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-70356-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="OSMWeekly has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>When a business mapped as a node (aka point) moves, there are two schools of thought:</p>
<ol>
<li>The node represents the business itself. If the business has moved, move the node to the new location.</li>
<li>The node represents the premises. Keep the node in place and remove the tags specific for that business. If the old location now houses a new business, reuse the node for that -- otherwise use the <code>"disused:"</code> <a href="https://wiki.openstreetmap.org/wiki/Comparison_of_life_cycle_concepts#Lifecycle_prefix_.28.3Cstatus.3E:.3Ckey.3E_.3D_.3Cvalue.3E.29">lifecycle prefix</a>. If you know where the old business has moved, map it as a new node in the new location.</li>
</ol>
<p>Both have their advantages. The main advantage of #1 is that an old URL link to the business in question will still work, and will show the updated location. The main advantage of #2 is that the history of a particular location is preserved, so you can easily look back through the changes and see the various businesses that have occupied that spot. ("<a href="https://wiki.openstreetmap.org/wiki/Keep_the_history">Keep the History</a>" is also considered good practice.)</p>
<p>Usually I end up going with option #2, because there are several situations where #1 won't work well:</p>
<ul>
<li>You don't know where the new location is, or if there even is one (sounds like this is your situation.)</li>
<li>The business was mapped as tags directly on a building (generally only done when it occupies the entire building.) Moving nodes makes sense but moving buildings usually doesn't. (Of course buildings do physically move sometimes!) A variation on this is when the <em>new</em> location occupies an entire building and might be better mapped directly on the building.</li>
<li>The business is located in a building with multiple addresses, and is tagged with an address. Moving the node elsewhere would remove that address from the building. (Though you could still do option #1 by removing the incorrect address tags from the old node and adding a new address node with the old address in the old location.)</li>
</ul>
<p>Frederik suggests simply deleting the nodes, which is also fine (as long as they're not the only thing tagged with that address in a multi-address building!) but doesn't have the advantages of #1 or #2. It does have the advantage of simplicity though. Personally I don't tend to delete them unless it's an unusual situation. For example, if two neighboring shops mapped as nodes were combined into a single shop with a single address, I'd probably reuse one node and delete the other one.</p>
<p>I definitely agree that using "<code>old_name</code>" probably isn't necessary or helpful. It's meant for situations where people still refer to something by its previous name, so unless you have evidence of this, leave it off. As long as you don't delete the node, the previous name will be there in its history.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Aug '19, 15:56</strong></p>
<img src="https://secure.gravatar.com/avatar/977d95e2184a885d9a01fb3297225872?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jmapb&#39;s gravatar image" />
<p><span>jmapb</span><br />
<span class="score" title="3387 reputation points"><span>3.4k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="61 badges"><span class="bronze">●</span><span class="badgecount">61</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jmapb has 22 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-70356" class="comments-container">
&#10;</div>
<div id="comment-tools-70356" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70356-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="70337"></span>

<div id="answer-container-70337" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70337-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70337-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-70337-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>My recommendation would be to, if the shop isn't there anymore and you don't know where it went, delete it. I would reserve <code>old_name</code> for situations where the shop exists, but has been renamed, and people occasionally still use the old name - not to document that a certain shop was once here but is now gone.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Aug '19, 17:05</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-70337" class="comments-container">
&#10;</div>
<div id="comment-tools-70337" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70337-form-container" class="comment-form-container">
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


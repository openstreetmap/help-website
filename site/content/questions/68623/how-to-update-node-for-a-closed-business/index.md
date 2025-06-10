+++
type = "question"
title = "How to update node for a Closed Business"
description = '''So, I&#x27;ve gone through the wiki, read this site, still confused on how to update a closed business to denote that it&#x27;s closed, and refresh the info to the business currently occupying the location. Example: There is a bank in a building. An amenity=bank node has the name Citibank. Citi has closed, an...'''
date = "2019-04-03T15:29:00Z"
lastmod = "2019-04-04T09:49:00Z"
weight = 68623
keywords = [ "businesses", "tagging", "poi" ]
aliases = [ "/questions/68623" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to update node for a Closed Business](/questions/68623/how-to-update-node-for-a-closed-business)

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
<span id="post-68623-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68623-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-68623-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>So, I've gone through the wiki, read this site, still confused on how to update a closed business to denote that it's closed, and refresh the info to the business currently occupying the location.</p>
<p>Example: There is a bank in a building. An amenity=bank node has the name Citibank. Citi has closed, and a new bank (Chase) has opened in the same location.</p>
<p>1.a: Do we add another amenity=bank node (preserving the old one)? Or edit (overwrite) the old one with new updated info?</p>
<p>1.b: Is there value in keeping the historical information? That is, in the Citi node, use disused:amenity=bank? Some maps will still display the name; do we add "disused:" to every tag (name, etc.) referring to the closed bank? Do we then add the same fields with the updated info in the same node, or make a new node (I guess this is similar to 1.a).</p>
<p>1.c: Is there not a preferred way to add a tag of "status:closed" or something referring to the business being gone? a Closed_date field? Something to allow time windows? Or is this just not needed?</p>
<p>Example 2: Restaurant in location changes it's name and owner.<br />
2.a: do we keep the old name as disused:name and just add the new name?</p>
<p>2.b for other tags like cuisine, do we just overwrite, or put disused: and repeat the tag with the new value, or just make a new node? If a restaurant keeps changing (same location, different restaurants as each folds, including that favorite one you loved!), over time, there will just be a tag soup. It seems that we'd want to keep the node referring to the old one as information, put disused: for every field referring to the old restaurant, and make a new node with the updated info... but I am too new to know.</p>
<p>2.c Like above, don't we want a date range to understand when things were in operation vs. nonexistent or closed?</p>
<p>Suggestions appreciated. Newbie wanting to do right...</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-businesses" rel="tag" title="see questions tagged &#39;businesses&#39;">businesses</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-poi" rel="tag" title="see questions tagged &#39;poi&#39;">poi</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Apr '19, 15:29</strong></p>
<img src="https://secure.gravatar.com/avatar/5f4c2cebc6050ddee65433f37990455e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mwexler&#39;s gravatar image" />
<p><span>mwexler</span><br />
<span class="score" title="40 reputation points">40</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mwexler has no accepted answers">0%</span> </br></p>
</div>
</div>
<div id="comments-container-68623" class="comments-container">
&#10;</div>
<div id="comment-tools-68623" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68623-form-container" class="comment-form-container">
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

<span id="68624"></span>

<div id="answer-container-68624" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68624-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68624-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-68624-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Generally, the verifiability constraint precludes historical data. There is a separate project for historical information.</p>
<p>If the disused amenity still has the old signs up then it is still generally acceptable to maintain the name=* tag as is. If something is still widely referred to by the old name, but the name displayed has changed then old_name=* can be used to show it.</p>
<p>The disused: prefix is normally used if the old purposes is still visible but clearly not current.</p>
<p>In your e.g. 1 a simple change of name would normally be OK, but if the old name is still referred to frequently I'd normally keep the old name as old_name. This would apply to the existing object.</p>
<p>In e.g. 2 a similar approach would be used. Change the tags that are no longer relevant and delete those no longer applicable (unless you can see the 'scars'). The changeset history contains the old info if someone really wants to go digging.</p>
<p>One case often accepted as an exception to the above is if satallite or e.g. Mapillary imagery shows out of date info that may be re-added by 'armchair' mappers. Here the residual data with lifecycle prefixes is often accepted as preferable to a potential edit war. (NB this is usually more applicable to demolished:building=* as the foundations may be overgrown long before the imagery updates.)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Apr '19, 17:57</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Apr '19, 17:59</strong> </span></p>
</div>
</div>
<div id="comments-container-68624" class="comments-container">
<span id="68627"></span>
<div id="comment-68627" class="comment">
<div id="post-68627-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>to add a few cases: if the old bank or restaurant moved to a different place I'd moved the node to that new place (only if the amenity was mapped as a node, I wouldn't move a building) and then create a new node for the business that moved in.</p>
<p>If the location was just vacated without a new tenant moving in and if it was still identifiable as to its old purpose I would use the disused: prefix and probably remove the name tag, e.g. disused:amenity=restaurant.</p>
<p>I would never leave the old business in the location if it was replaced by a new one except for the case where InsertUser mentioned moving the name to old_name.</p>
</div>
<div id="comment-68627-info" class="comment-info">
<span class="comment-age">(03 Apr '19, 21:09)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="68629"></span>
<div id="comment-68629" class="comment">
<div id="post-68629-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ok. Sounds like overwrite is the preferred approach in most cases over some type of historical tracking. Thanks much for all the feedback.</p>
</div>
<div id="comment-68629-info" class="comment-info">
<span class="comment-age">(04 Apr '19, 03:55)</span> <span class="comment-user userinfo">mwexler</span>
</div>
</div>
<span id="68633"></span>
<div id="comment-68633" class="comment">
<div id="post-68633-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Please accept the answer if it satisfies you.</p>
</div>
<div id="comment-68633-info" class="comment-info">
<span class="comment-age">(04 Apr '19, 09:49)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
</div>
<div id="comment-tools-68624" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68624-form-container" class="comment-form-container">
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


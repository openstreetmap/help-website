+++
type = "question"
title = "Differentiating highway:unclassified highway:service"
description = '''I am new to OpenStreetMap and I am trying to fill in the details of the various local tracks and roads. These are nearly all based on the cadastral map of the area with no information on surface, access etc. I have a problem with highway:unclassified and highway:service. In two of the local areas, t...'''
date = "2022-02-18T17:14:00Z"
lastmod = "2022-02-23T10:31:00Z"
weight = 83525
keywords = [ "ways", "unclassified", "service" ]
aliases = [ "/questions/83525" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Differentiating highway:unclassified highway:service](/questions/83525/differentiating-highwayunclassified-highwayservice)

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
<span id="post-83525-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83525-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-83525-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am new to OpenStreetMap and I am trying to fill in the details of the various local tracks and roads. These are nearly all based on the cadastral map of the area with no information on surface, access etc. I have a problem with highway:unclassified and highway:service. In two of the local areas, the senses of unclassified and service roads seem to be swapped. For example, around Chaumussay there are many roads tagged as highway=service (e.g. <a href="https://www.openstreetmap.org/way/59916926">https://www.openstreetmap.org/way/59916926</a>) even though these are quite normal (if minor) public highways linking or leading to remote farmhouses or hamlets. On the other hand, around le Grand-Pressigny, there are “no through” (dead end) roads tagged as highway=unclassified that could be considered as a “service road leading to a residence, property or place of business” (as defined in the wiki) from a highway to a farm (e.g. <a href="https://www.openstreetmap.org/way/606148747">https://www.openstreetmap.org/way/606148747</a>). An implication of the examples of highway=service in the wiki are that these are in the private domain, although there may be an implicit public access permission, but this is nowhere stated.</p>
<p>The usage must be wrong in one or both areas but before I even think of changing one of the areas, I would like to be sure that I know what I am doing!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span> <span class="post-tag tag-link-unclassified" rel="tag" title="see questions tagged &#39;unclassified&#39;">unclassified</span> <span class="post-tag tag-link-service" rel="tag" title="see questions tagged &#39;service&#39;">service</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Feb '22, 17:14</strong></p>
<img src="https://secure.gravatar.com/avatar/aeb58377a8e6a08a91ccbe94158bad82?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TinyTrouble&#39;s gravatar image" />
<p><span>TinyTrouble</span><br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TinyTrouble has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-83525" class="comments-container">
&#10;</div>
<div id="comment-tools-83525" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83525-form-container" class="comment-form-container">
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

<span id="83526"></span>

<div id="answer-container-83526" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83526-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83526-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-83526-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi.</p>
<p>The first step is to contact the mapper. He still map these days, so he might answer (he never did publicly, check <a href="http://hdyc.neis-one.org/">http://hdyc.neis-one.org/</a>).. He seems really experimented, so maybe he has a good reason.</p>
<p>It might also be a case of tagging for the renderer, <code>highway=service</code> render thiner, the roads are not wide, so he goes for service. You might want to remind him that's not the point of the <code>highway=</code> classification.</p>
<p>If you have no answer, change the classification yourself. The first example is quite clear. Maybe double-check, ideally on the ground or with ground-level imagery (mapillary), to add relevant tags (<code>surface</code>, <code>width</code>, <code>lanes</code>) so that routers won't go through little roads if possible...</p>
<p>I quite agree with your reasoning, in another country it might have been a mapping style difference, but in France I'm pretty sure the wiki definition applies. I usually don't use service for farm access, but I don't really know why.</p>
<p>If things goes wrong (angry reply, revert of your changes, etc.) contact the DWG for mediation.</p>
<p>Just a note, don't trust the cadastre, track or even roads might have been reclaimed by neighboring farmers, gone into disrepair...</p>
<p>In some country, the default access value for service roads is defined on this <a href="https://wiki.openstreetmap.org/wiki/OSM_tags_for_routing/Access_restrictions#France">page</a>, but not in France, neither worldwide.</p>
<p>So if it is not publicly accessible, use relevant <code>access=</code> tags. In France, usually, access roads to farms and hamlets are public domain. Trust the signs.</p>
<p>Hope this helps, happy mapping !</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Feb '22, 19:26</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-83526" class="comments-container">
<span id="83530"></span>
<div id="comment-83530" class="comment">
<div id="post-83530-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi H_mlet</p>
<p>Thanks for your suggestions. Being a complete novice mapper I was not quite sure how to approach the question. Your comment "In France, usually, access roads to farms and hamlets are public domain" is the reason that I think that they should stay highway=unclassified - as far as the communes are concerned the access roads (even if they are dirt tracks) are part of the road network. But our commune has been asking farmers if they wish to adopt "their" access roads. For the moment I do not intend to change the status of any way I have not walked along. But, for farm access roads, I might change the status to highway=service if the commune confirms that the road is now private. This should not affect routing. I shall keep an eye out for "défense d'entrer" on access roads.</p>
<p>So far I have only added ways and tags, it is rather rude to change someone else's contributions without consulting them first. I shall contact the mappers.</p>
<p>Thank you</p>
</div>
<div id="comment-83530-info" class="comment-info">
<span class="comment-age">(19 Feb '22, 08:45)</span> <span class="comment-user userinfo">TinyTrouble</span>
</div>
</div>
<span id="83557"></span>
<div id="comment-83557" class="comment">
<div id="post-83557-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi</p>
<p>I have not yet visited the mairie in Chaumussay to recover a list or map of the communal roads, but I have checked the cadastre. All the roads marked "highway:service" are are in "empty" parcels (no number) and are, therefore, part of the public road network.</p>
<p>Tiny</p>
</div>
<div id="comment-83557-info" class="comment-info">
<span class="comment-age">(23 Feb '22, 10:31)</span> <span class="comment-user userinfo">TinyTrouble</span>
</div>
</div>
</div>
<div id="comment-tools-83526" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83526-form-container" class="comment-form-container">
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


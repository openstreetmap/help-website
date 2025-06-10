+++
type = "question"
title = "POI and address node: single node?"
description = '''Hello, there. My question is simple, but I can&#x27;t find a simple answer: when mapping POI such as shops on a zone where street numbers already exist, should I map the POI on the street number node or map the POI on a separate node at the same location? My question seems rather trivial, but, strangely,...'''
date = "2015-12-15T14:14:00Z"
lastmod = "2015-12-17T09:42:00Z"
weight = 47166
keywords = [ "housenumbers", "street", "nodes", "address", "poi" ]
aliases = [ "/questions/47166" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [POI and address node: single node?](/questions/47166/poi-and-address-node-single-node)

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
<span id="post-47166-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47166-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-47166-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, there.</p>
<p>My question is simple, but I can't find a simple answer: when mapping POI such as shops on a zone where street numbers already exist, should I map the POI on the street number node or map the POI on a separate node at the same location? My question seems rather trivial, but, strangely, I couldn't find any similar questions, so, if I missed them, please don't hit too hard.</p>
<p>Awaiting your answers,</p>
<p>Regards.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-housenumbers" rel="tag" title="see questions tagged &#39;housenumbers&#39;">housenumbers</span> <span class="post-tag tag-link-street" rel="tag" title="see questions tagged &#39;street&#39;">street</span> <span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span> <span class="post-tag tag-link-poi" rel="tag" title="see questions tagged &#39;poi&#39;">poi</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Dec '15, 14:14</strong></p>
<img src="https://secure.gravatar.com/avatar/03b6014ac927da400a55374bbbe5152a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Penegal&#39;s gravatar image" />
<p><span>Penegal</span><br />
<span class="score" title="631 reputation points">631</span><span title="31 badges"><span class="badge1">●</span><span class="badgecount">31</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Penegal has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-47166" class="comments-container">
&#10;</div>
<div id="comment-tools-47166" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47166-form-container" class="comment-form-container">
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

<span id="47168"></span>

<div id="answer-container-47168" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47168-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47168-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-47168-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Penegal has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Your question is not trivial :) As far as I know there is no one definitive answer, but my take would be:</p>
<ul>
<li>If a POI is the only "object of note" at a given address (i.e. if given POI is only thing worth tagging at that address), then tag the address node with the POI tags. This is essentially the <a href="http://wiki.openstreetmap.org/wiki/One_feature,_one_OSM_element">one object, one element</a> guideline, and helps to clearly associate a POI with that street address.</li>
<li>If there could be several POIs associated with a particular address (e.g. a building with several shops in it), then tag the POI as a separate node.</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Dec '15, 15:38</strong></p>
<img src="https://secure.gravatar.com/avatar/390c3a1e9ea7b1f10deea61828ad66eb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lightsider&#39;s gravatar image" />
<p><span>Lightsider</span><br />
<span class="score" title="1540 reputation points"><span>1.5k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="21 badges"><span class="silver">●</span><span class="badgecount">21</span></span><span title="29 badges"><span class="bronze">●</span><span class="badgecount">29</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lightsider has 9 accepted answers">42%</span></p>
</div>
</div>
<div id="comments-container-47168" class="comments-container">
<span id="47169"></span>
<div id="comment-47169" class="comment">
<div id="post-47169-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Does the second possibility include shared buildings? I mean, at least here in France, downtown buildings often have a shop at the ground floor and apartments above, but, then, shop and apartments share the same address; should I anyway map the POI on a different node?</p>
</div>
<div id="comment-47169-info" class="comment-info">
<span class="comment-age">(15 Dec '15, 16:15)</span> <span class="comment-user userinfo">Penegal</span>
</div>
</div>
<span id="47172"></span>
<div id="comment-47172" class="comment">
<div id="post-47172-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Besides, if the POI is on a different node, how do I map its address? Wouldn't it create a duplicate content?</p>
</div>
<div id="comment-47172-info" class="comment-info">
<span class="comment-age">(15 Dec '15, 19:41)</span> <span class="comment-user userinfo">Penegal</span>
</div>
</div>
<span id="47178"></span>
<div id="comment-47178" class="comment">
<div id="post-47178-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I would suppose these have different subaddresses then, but the wiki pages say nothing about mapping subaddresses. If there really is only one adress for the building, with several POIs inside, wouldn't it be an option to tag the address to just the building?</p>
</div>
<div id="comment-47178-info" class="comment-info">
<span class="comment-age">(16 Dec '15, 07:30)</span> <span class="comment-user userinfo">joost schouppe</span>
</div>
</div>
<span id="47184"></span>
<div id="comment-47184" class="comment">
<div id="post-47184-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If the addr:housenumber is a separate node I do not need to add address tags on the shop/amenity, this is usually the case when the building and the shop has different entrances. So if the only entrance to the building is through the shop I map the address tag on the shop.</p>
</div>
<div id="comment-47184-info" class="comment-info">
<span class="comment-age">(16 Dec '15, 13:24)</span> <span class="comment-user userinfo">emj</span>
</div>
</div>
<span id="47186"></span>
<div id="comment-47186" class="comment not_top_scorer">
<div id="post-47186-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>But, by not tagging the shop on the same node that its address, the link between the address and the shop would not be established, and that's whats bothers me; OSM allows one to add shops addresses, phone numbers and websites, but the postal address cannot be added if the building is shared? Sounds strange to me.</p>
</div>
<div id="comment-47186-info" class="comment-info">
<span class="comment-age">(16 Dec '15, 14:05)</span> <span class="comment-user userinfo">Penegal</span>
</div>
</div>
<span id="47195"></span>
<div id="comment-47195" class="comment">
<div id="post-47195-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Some software (e.g. Nominatim) can extract the address from the building (area) and assign it to the POIs inside. Other software does not do this. You can always duplicate the address information on the node of the POI. I wouldn't tag the address info on a node when it applies to the whole building, but in some countries you are not supposed to do this (e.g. Denmark)</p>
<p>You could of course have an address node and a separate POI node with the same address in 1 building, if needed.</p>
</div>
<div id="comment-47195-info" class="comment-info">
<span class="comment-age">(17 Dec '15, 08:23)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="47196"></span>
<div id="comment-47196" class="comment not_top_scorer">
<div id="post-47196-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Then I'll map the POI address in its node in addition of the address node, but I'll only put the address node in the street relation, not the POI node. Thanks for your help.</p>
</div>
<div id="comment-47196-info" class="comment-info">
<span class="comment-age">(17 Dec '15, 09:42)</span> <span class="comment-user userinfo">Penegal</span>
</div>
</div>
</div>
<div id="comment-tools-47168" class="comment-tools">
<span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-47168-form-container" class="comment-form-container">
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


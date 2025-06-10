+++
type = "question"
title = "Bus stop description"
description = '''I encounter some problem to create a bus stop. I saw that some people use the key&#x27;name&#x27; to describle the line and the direction. I suggest to create a key for the line as &#x27;line&#x27; for the number of the line and another key to describe the direction like a relation &#x27;from&#x27;=&#x27;name&#x27; (= bus stop start) &#x27;to&#x27;...'''
date = "2012-06-20T21:34:00Z"
lastmod = "2012-06-21T13:53:00Z"
weight = 13668
keywords = [ "bus", "stop", "description" ]
aliases = [ "/questions/13668" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Bus stop description](/questions/13668/bus-stop-description)

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
<span id="post-13668-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13668-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-13668-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I encounter some problem to create a bus stop. I saw that some people use the key'name' to describle the line and the direction. I suggest to create a key for the line as 'line' for the number of the line and another key to describe the direction like a relation 'from'='name' (= bus stop start) 'to'='name' (=bus stop arrival). I don't know if it's the correct way to send my idea so please give me the correction if it's the wrong way. Thank you. Best regards.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-bus" rel="tag" title="see questions tagged &#39;bus&#39;">bus</span> <span class="post-tag tag-link-stop" rel="tag" title="see questions tagged &#39;stop&#39;">stop</span> <span class="post-tag tag-link-description" rel="tag" title="see questions tagged &#39;description&#39;">description</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Jun '12, 21:34</strong></p>
<img src="https://secure.gravatar.com/avatar/b28ca8ba2441402a0b89d506b036ca91?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DOM91&#39;s gravatar image" />
<p><span>DOM91</span><br />
<span class="score" title="56 reputation points">56</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DOM91 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-13668" class="comments-container">
<span id="13670"></span>
<div id="comment-13670" class="comment">
<div id="post-13670-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I would like add to be complete that the key 'name' should be use to indicate the correct name of the the bus stop. Finaly it miss the attribut 'bus shelter' for the key 'building'= Thanks for your understanding.</p>
</div>
<div id="comment-13670-info" class="comment-info">
<span class="comment-age">(20 Jun '12, 21:48)</span> <span class="comment-user userinfo">DOM91</span>
</div>
</div>
</div>
<div id="comment-tools-13668" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13668-form-container" class="comment-form-container">
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

<span id="13672"></span>

<div id="answer-container-13672" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13672-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13672-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-13672-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As already mentioned by Paul, there is a <a href="http://wiki.openstreetmap.org/wiki/Relation:route#Bus_routes_.28also_trolley_bus.29">route relation</a> for buses and the wiki page also lists an <a href="http://www.openstreetmap.org/browse/relation/37415">example</a> of an already mapped bus route. The name is just for the bus stop and should not be abused for anything other as you correctly pointed out.</p>
<p>The bus shelter you mentioned can be simply added by using the <a href="http://wiki.openstreetmap.org/wiki/Key:shelter">shelter=*</a> key, as mentioned on the <a href="http://wiki.openstreetmap.org/wiki/Tag:highway%3Dbus_stop">highway=bus_stop</a> page. JOSM already supports it in the bus stop preset, I don't know if Potlatch does.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Jun '12, 05:33</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-13672" class="comments-container">
<span id="13675"></span>
<div id="comment-13675" class="comment">
<div id="post-13675-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks a lot for this clear explanation with the link. I will take more attention by reading carefuly wiki page.</p>
</div>
<div id="comment-13675-info" class="comment-info">
<span class="comment-age">(21 Jun '12, 08:38)</span> <span class="comment-user userinfo">DOM91</span>
</div>
</div>
</div>
<div id="comment-tools-13672" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13672-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="13685"></span>

<div id="answer-container-13685" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13685-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13685-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-13685-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you want to tag the bus routes using a bus stop, you can use the <code>route_ref=</code> tag. For this tag, you can list the bus numbers, separated by semi-colons, eg <code>route_ref=5;8;28A</code></p>
<p>Though as scai and Paul say, where possible, bus routes should be mapped with relations, and the bus stops added as members. In this case, the route_ref tags on each stop are unnecessary.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Jun '12, 13:53</strong></p>
<img src="https://secure.gravatar.com/avatar/aa505c046b1c010e997a7849c6f3dbbe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vclaw&#39;s gravatar image" />
<p><span>Vclaw</span><br />
<span class="score" title="9217 reputation points"><span>9.2k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="95 badges"><span class="silver">●</span><span class="badgecount">95</span></span><span title="141 badges"><span class="bronze">●</span><span class="badgecount">141</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vclaw has 41 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-13685" class="comments-container">
&#10;</div>
<div id="comment-tools-13685" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13685-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="13671"></span>

<div id="answer-container-13671" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13671-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13671-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-13671-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Add the stop to the relation for the bus route as a "stop" member.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Jun '12, 22:09</strong></p>
<img src="https://secure.gravatar.com/avatar/666698a7b13e402aba7e1e0f6de7c1d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Baloo%20Uriza&#39;s gravatar image" />
<p><span>Baloo Uriza</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="61 badges"><span class="bronze">●</span><span class="badgecount">61</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Baloo Uriza has 12 accepted answers">9%</span></p>
</div>
</div>
<div id="comments-container-13671" class="comments-container">
&#10;</div>
<div id="comment-tools-13671" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13671-form-container" class="comment-form-container">
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


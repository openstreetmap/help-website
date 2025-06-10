+++
type = "question"
title = "Am I wrong or there is a Bug on Turn Restriction on iD ?"
description = '''I think I found a bug on setting turn restrictions on iD in a particular point. The point is {Node id=1425835107 version=1 V lat=-8.0672848,lon=-34.8937994} The origin way of the restriction is {Way id=315073917 version=1 VT nodes=[{Node id=1425835107 version=1 V lat=-8.0672848,lon=-34.8937994}, {No...'''
date = "2014-11-29T23:38:00Z"
lastmod = "2019-07-10T17:35:00Z"
weight = 38946
keywords = [ "ideditor", "turn_restrictions" ]
aliases = [ "/questions/38946" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Am I wrong or there is a Bug on Turn Restriction on iD ?](/questions/38946/am-i-wrong-or-there-is-a-bug-on-turn-restriction-on-id)

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
<span id="post-38946-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38946-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-38946-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I think I found a bug on setting turn restrictions on iD in a particular point.</p>
<p>The point is {Node id=1425835107 version=1 V lat=-8.0672848,lon=-34.8937994}</p>
<p>The origin way of the restriction is {Way id=315073917 version=1 VT nodes=[{Node id=1425835107 version=1 V lat=-8.0672848,lon=-34.8937994}, {Node id=1425835109 version=1 V lat=-8.0671797,lon=-34.8940289}]}</p>
<p>The destination way is {Way id=315073914 version=1 VT&gt; nodes=[{Node id=1425835107 version=1 V lat=-8.0672848,lon=-34.8937994}, {Node id=1425835097 version=1 V lat=-8.0667292,lon=-34.8935357}, {Node id=1425830470 version=1 V lat=-8.0662714,lon=-34.8933326}]}</p>
<p>The wrong way is {Way id=315073913 version=1 VT&gt; nodes=[{Node id=1425835109 version=1 V lat=-8.0671797,lon=-34.8940289}, {Node id=1425835103 version=1 V lat=-8.0675578,lon=-34.8942197}, {Node id=1425835101 version=1 V lat=-8.06768,lon=-34.8942707}, {Node id=1425835082 version=1 V lat=-8.0677632,lon=-34.8942329}, {Node id=1425835088 version=1 V lat=-8.0678048,lon=-34.8941151}, {Node id=1425835108 version=1 V lat=-8.0677792,lon=-34.8940317}, {Node id=1425835107 version=1 V lat=-8.0672848,lon=-34.8937994}]}</p>
<p>Every time I try to select the orign way and set the prohibition to turn to destination way, the iD selects the wrong way, so I can't set the restriction.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ideditor" rel="tag" title="see questions tagged &#39;ideditor&#39;">ideditor</span> <span class="post-tag tag-link-turn_restrictions" rel="tag" title="see questions tagged &#39;turn_restrictions&#39;">turn_restrictions</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Nov '14, 23:38</strong></p>
<img src="https://secure.gravatar.com/avatar/39df65f017c23b0fc33d0aa7d7feb23e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TrvrHldr&#39;s gravatar image" />
<p><span>TrvrHldr</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TrvrHldr has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Nov '14, 00:04</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-38946" class="comments-container">
<span id="69970"></span>
<div id="comment-69970" class="comment">
<div id="post-69970-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I had to ask a similar related question. But for clarification and also to see if it's the same issue:</p>
<p>Now looking at the current map without looking at the streetview or any current turn restrictions, if you're traveling eastbound on Rua Francisco Alves, you can turn right on Miguel de Cervantes, but not right on Praça Miguel Cervantes (left is okay).</p>
<p>Likewise westbound on Rua Francisco Alves, you can turn right on Praça Miguel Cervantes but not on Miguel de Cervantes (left is okay).</p>
<p>Are these observations correct -- and if they are, it would imply that turn restrictions aren't needed because I can deduce them by looking at the map. I think that iD also prohibits adding these restrictions even if there is a sign on the street. Hopefully there's some clarification if a restriction or other annotation is needed in OSM for this situation.</p>
</div>
<div id="comment-69970-info" class="comment-info">
<span class="comment-age">(10 Jul '19, 17:35)</span> <span class="comment-user userinfo">gpserror</span>
</div>
</div>
</div>
<div id="comment-tools-38946" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38946-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>


+++
type = "question"
title = "Where to put addr:city, addr:postcode, etc. when using associatedStreet relations"
description = '''Where should addr:city, addr:postcode, addr:country, ... be set, when using associatedStreet relations instead of addr:street tags? It doesn&#x27;t make much sense to set them on the nodes, as on of the primary benefits from using relations - not repeating the same addr:street over and over again - would...'''
date = "2012-10-06T14:50:00Z"
lastmod = "2012-10-06T15:56:00Z"
weight = 16704
keywords = [ "city", "associatedstreet", "postcode" ]
aliases = [ "/questions/16704" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Where to put addr:city, addr:postcode, etc. when using associatedStreet relations](/questions/16704/where-to-put-addrcity-addrpostcode-etc-when-using-associatedstreet-relations)

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
<span id="post-16704-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16704-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-16704-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Where should addr:city, addr:postcode, addr:country, ... be set, when using associatedStreet relations instead of addr:street tags? It doesn't make much sense to set them on the nodes, as on of the primary benefits from using relations - not repeating the same addr:street over and over again - would be busted... But as far as I read the wiki, the associatedStreet relation itself is also not meant to hold address information.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-city" rel="tag" title="see questions tagged &#39;city&#39;">city</span> <span class="post-tag tag-link-associatedstreet" rel="tag" title="see questions tagged &#39;associatedstreet&#39;">associatedstreet</span> <span class="post-tag tag-link-postcode" rel="tag" title="see questions tagged &#39;postcode&#39;">postcode</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Oct '12, 14:50</strong></p>
<img src="https://secure.gravatar.com/avatar/eca34689e074411e0daca0d994f532b3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tyr_asd&#39;s gravatar image" />
<p><span>tyr_asd</span><br />
<span class="score" title="1196 reputation points"><span>1.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="19 badges"><span class="silver">●</span><span class="badgecount">19</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tyr_asd has 11 accepted answers">64%</span></p>
</div>
</div>
<div id="comments-container-16704" class="comments-container">
&#10;</div>
<div id="comment-tools-16704" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16704-form-container" class="comment-form-container">
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

<span id="16705"></span>

<div id="answer-container-16705" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-16705-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16705-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-16705-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="tyr_asd has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In theory addr:* tags shouldn't be needed on associatedStreet relations; the associatedStreet has a name (the addr:street equivalent) and is in a geographical database where city, country, country, etc should be possible to work out from the location (though see comments about postcodes below).</p>
<p>Having said that, I can see no harm in adding addr:* tags to the relation. The addr:city one in particular might be useful for a road somewhere roughly equidistant between two cities; though it depends on each data user whether they check for and use any such tags.</p>
<p>addr:postcode probably requires a country specific answer, as in many parts of the UK for example there are often more than one postcodes for a single street (such as one for one side of the road and one the other, and sometimes even another for new houses slotted in amongst older ones), so in the UK the addr:postcode tag would go on the individual addresses.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Oct '12, 15:03</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-16705" class="comments-container">
<span id="16706"></span>
<div id="comment-16706" class="comment">
<div id="post-16706-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>If houses on the same street have different postcodes, one could also use more associatedStreet-Relations, where the street is member in both.</p>
</div>
<div id="comment-16706-info" class="comment-info">
<span class="comment-age">(06 Oct '12, 15:56)</span> <span class="comment-user userinfo">Alexander Ro...</span>
</div>
</div>
</div>
<div id="comment-tools-16705" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16705-form-container" class="comment-form-container">
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


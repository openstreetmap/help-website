+++
type = "question"
title = "Major incorrect postcode returned on reversegeocode"
description = '''Hi! I have reverse searched a GPS co-ordinate: -27.37324,153.047182 and it returns: St Kevin&#x27;s Primary School, Deborah Street, North Chermside, Geebung, Brisbane, Queensland, 5055, Australia All information is correct with one exception. The postcode 5055 is wrong. In fact it is not even close. That...'''
date = "2019-03-04T05:03:00Z"
lastmod = "2019-03-05T21:42:00Z"
weight = 68241
keywords = [ "nominatim", "reversegeocoding", "postcode", "error" ]
aliases = [ "/questions/68241" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Major incorrect postcode returned on reversegeocode](/questions/68241/major-incorrect-postcode-returned-on-reversegeocode)

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
<span id="post-68241-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68241-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68241-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi! I have reverse searched a GPS co-ordinate: -27.37324,153.047182 and it returns: St Kevin's Primary School, Deborah Street, North Chermside, Geebung, Brisbane, Queensland, <strong>5055</strong>, Australia</p>
<p>All information is correct with one exception. The postcode <strong>5055</strong> is wrong. In fact it is not even close. That postcode comes from a totally different state in Australia at the other end of the country (specifically South Australia).</p>
<p>If I do a regular search for: St Kevin's Primary School, North Chermside it once again returns the correct information except for the <strong>wrong postcode</strong>: St Kevin's Primary School, Deborah Street, North Chermside, Geebung, Brisbane, Queensland, <strong>5055</strong>, Australia</p>
<p>If I do a regular search for: North Chermside It returns the <strong>correct postcode</strong> for that suburb: North Chermside, Chermside, Brisbane, Queensland, <strong>4032</strong>, Australia</p>
<p>A quick search indicates this incorrect 5055 postcode is returned for a handful of suburbs in the same physical vicinity (although these suburbs may have a slightly different postcode of their own).</p>
<p>It appears to be that geofencing for those suburbs is where the issue arises.</p>
<p>How does one go about reporting/repairing this information? Appreciate and feedback.</p>
<p>Cheers Todd</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-reversegeocoding" rel="tag" title="see questions tagged &#39;reversegeocoding&#39;">reversegeocoding</span> <span class="post-tag tag-link-postcode" rel="tag" title="see questions tagged &#39;postcode&#39;">postcode</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Mar '19, 05:03</strong></p>
<img src="https://secure.gravatar.com/avatar/c9ec508ab9a42dfa8940fd4d78ad073d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="todddixon&#39;s gravatar image" />
<p><span>todddixon</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="todddixon has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Mar '19, 11:21</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-68241" class="comments-container">
&#10;</div>
<div id="comment-tools-68241" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68241-form-container" class="comment-form-container">
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

<span id="68244"></span>

<div id="answer-container-68244" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68244-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68244-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-68244-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>According to this: <a href="https://nominatim.openstreetmap.org/details.php?place_id=80662662,">https://nominatim.openstreetmap.org/details.php?place_id=80662662,</a> the postcode is not in the OSM database, but is imported by Nominatim. There is no link next to a node or relation in OSM, which is typical for information that is not found in OSM.</p>
<p>I guess that you could report that on the <a href="https://github.com/openstreetmap/Nominatim/issues">Nominatim Github repository</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Mar '19, 11:11</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-68244" class="comments-container">
<span id="68247"></span>
<div id="comment-68247" class="comment">
<div id="post-68247-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Nightly Nominatim looks at postcodes and calculates a center point for each. The /details page can't link to a single OSM object here.</p>
</div>
<div id="comment-68247-info" class="comment-info">
<span class="comment-age">(04 Mar '19, 11:36)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
</div>
<div id="comment-tools-68244" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68244-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="68248"></span>

<div id="answer-container-68248" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68248-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68248-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-68248-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This place <a href="https://www.openstreetmap.org/node/2207501595">https://www.openstreetmap.org/node/2207501595</a> is mapped with postcode 5055. All others addresses in the neighborhood seem to be 4034. Once changed Nominatim will recalculate the 5055 position (once per night). Deleted the place now <a href="https://www.openstreetmap.org/changeset/67763854">https://www.openstreetmap.org/changeset/67763854</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Mar '19, 11:40</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Mar '19, 11:44</strong> </span></p>
</div>
</div>
<div id="comments-container-68248" class="comments-container">
<span id="68250"></span>
<div id="comment-68250" class="comment">
<div id="post-68250-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for your quick response. I notice that it picked up the 5055 from part of the phone number on that site. I don’t understand fully understand how Openstreetmap and Nominatim work under the bonnet but your explanation is at least a little insight in to it’s inner workings! I appreciate your help.</p>
<p>Cheers 😊</p>
</div>
<div id="comment-68250-info" class="comment-info">
<span class="comment-age">(04 Mar '19, 12:22)</span> <span class="comment-user userinfo">todddixon</span>
</div>
</div>
<span id="68285"></span>
<div id="comment-68285" class="comment">
<div id="post-68285-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The nightly postcode recalculation worked on my worldwide setup, but I still see the issue on <a href="https://nominatim.osm.org/reverse.php?lat=-27.37324&amp;lon=153.047182">https://nominatim.osm.org/reverse.php?lat=-27.37324&amp;lon=153.047182</a> You might have to open an issue on <a href="https://github.com/openstreetmap/Nominatim/issues">https://github.com/openstreetmap/Nominatim/issues</a> to have the administrators review that. I open reply to open issues there but don't have access to the Openstreetmap foundation servers.</p>
</div>
<div id="comment-68285-info" class="comment-info">
<span class="comment-age">(05 Mar '19, 21:42)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
</div>
<div id="comment-tools-68248" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68248-form-container" class="comment-form-container">
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


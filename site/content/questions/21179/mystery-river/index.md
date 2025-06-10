+++
type = "question"
title = "Mystery river"
description = '''I noticed a weird data problem in my area on certain OSM tile renderings See here (CloudMade): http://maps.cloudmade.com/?lat=51.088692&amp;amp;lng=-0.730231&amp;amp;zoom=18&amp;amp;styleId=1&amp;amp;opened_tab=0 and here (Cycle map): http://osm.org/go/eupuylG00--?layers=C If you look at the area of park between Li...'''
date = "2013-04-04T12:55:00Z"
lastmod = "2013-04-04T15:19:00Z"
weight = 21179
keywords = [ "river", "data", "bugs" ]
aliases = [ "/questions/21179" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Mystery river](/questions/21179/mystery-river)

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
<span id="post-21179-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21179-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-21179-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I noticed a weird data problem in my area on certain OSM tile renderings</p>
<p>See here (CloudMade): <a href="http://maps.cloudmade.com/?lat=51.088692&amp;lng=-0.730231&amp;zoom=18&amp;styleId=1&amp;opened_tab=0" title="Cloudmade rendering"></a><a href="http://maps.cloudmade.com/?lat=51.088692&amp;lng=-0.730231&amp;zoom=18&amp;styleId=1&amp;opened_tab=0">http://maps.cloudmade.com/?lat=51.088692&amp;lng=-0.730231&amp;zoom=18&amp;styleId=1&amp;opened_tab=0</a></p>
<p>and here (Cycle map): <a href="http://osm.org/go/eupuylG00--?layers=C" title="Cycle map"></a><a href="http://osm.org/go/eupuylG00--?layers=C">http://osm.org/go/eupuylG00--?layers=C</a></p>
<p>If you look at the area of park between Lion Lane and Wey Springs, you will see the River Tigris labelled at the closest zoom level. The Tigris is a large river in the Middle East and definitely does not pass through my little town in Surrey, so something is wrong. I've had a look at the surrounding objects in Potlatch and also tried exporting that area as XML and searching for Tigris, but I can't see where this label comes from and that's as far as my OSM data knowledge goes.</p>
<p>Any suggestions for finding out where this is coming from? I have only seen it on those two renderings.</p>
<p>Thanks Helen</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-river" rel="tag" title="see questions tagged &#39;river&#39;">river</span> <span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span> <span class="post-tag tag-link-bugs" rel="tag" title="see questions tagged &#39;bugs&#39;">bugs</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Apr '13, 12:55</strong></p>
<img src="https://secure.gravatar.com/avatar/96d53e36bdf6c64297444c24ee9adf67?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helenst&#39;s gravatar image" />
<p><span>helenst</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helenst has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-21179" class="comments-container">
&#10;</div>
<div id="comment-tools-21179" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21179-form-container" class="comment-form-container">
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

<span id="21189"></span>

<div id="answer-container-21189" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-21189-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21189-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-21189-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I dug around a little, and the playground appears to have been added to the Tigris multipolygon relation in October 2011 - <a href="http://www.openstreetmap.org/browse/relation/143/history">this</a> is the relation in question. Not sure how that might have happened - either an editor bug, or clicking 'Add to relation' then 'Load relation' and typing 143 (though that seems unlikely!).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Apr '13, 15:14</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-21189" class="comments-container">
&#10;</div>
<div id="comment-tools-21189" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21189-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="21181"></span>

<div id="answer-container-21181" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-21181-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21181-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-21181-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Looking at the raw data (through an editor or the data layer) is indeed a good way to make sure one hasn't overlooked something. If a feature appears neither in the raw data nor in the default map then it is very likely that it has long been deleted, and less-frequently-updating maps simply carry an afterglow of the object that once was there. (I briefly checked the edit history for the area and couldn't find any trace of that "river", but a thorough check involving a full history file could unearth the source of that label on the map.)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Apr '13, 13:59</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-21181" class="comments-container">
<span id="21182"></span>
<div id="comment-21182" class="comment">
<div id="post-21182-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I think you'll find the cycle map has also rerendered and doesn't show it any more, if you clear your local cache.</p>
</div>
<div id="comment-21182-info" class="comment-info">
<span class="comment-age">(04 Apr '13, 14:10)</span> <span class="comment-user userinfo">EdLoach ♦</span>
</div>
</div>
<span id="21185"></span>
<div id="comment-21185" class="comment">
<div id="post-21185-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks. Yes, it seems to have disappeared from the cycle map - I guess I'll wait a few days to see if it disappears from the other one too.</p>
</div>
<div id="comment-21185-info" class="comment-info">
<span class="comment-age">(04 Apr '13, 14:53)</span> <span class="comment-user userinfo">helenst</span>
</div>
</div>
<span id="21191"></span>
<div id="comment-21191" class="comment">
<div id="post-21191-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I'd give the Cloudmade one more than a few days - edits I've made weeks ago don't seem to show there, so perhaps they are still using CCBYSA data as they claim. I don't know how often they update their copy of the data.</p>
</div>
<div id="comment-21191-info" class="comment-info">
<span class="comment-age">(04 Apr '13, 15:19)</span> <span class="comment-user userinfo">EdLoach ♦</span>
</div>
</div>
</div>
<div id="comment-tools-21181" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21181-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="21187"></span>

<div id="answer-container-21187" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-21187-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21187-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-21187-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In addition to Frederick's answer, If you are using potlatch2 and want to find and contact the mapper you can. While in edit mode click on the way (or stream in this case) then click on advanced tab, it's at the bottom on tag box, then click on way number which is at the top of tag box and you will see some info about the way including the mapper click on the name and you get more info and you can send a message to them if you wish.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Apr '13, 15:05</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</div>
</div>
<div id="comments-container-21187" class="comments-container">
<span id="21188"></span>
<div id="comment-21188" class="comment">
<div id="post-21188-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Using JOSM it's even simpler</p>
</div>
<div id="comment-21188-info" class="comment-info">
<span class="comment-age">(04 Apr '13, 15:06)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="21190"></span>
<div id="comment-21190" class="comment">
<div id="post-21190-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Except in this case whatever was causing it seems to be deleted, or at least none of the objects in the immediate vicinity of the label have such a name in their history. Using taginfo and JOSM all such labels are correctly assigned to the river. Potlatch 1 doesn't seem to show anything in the area as a deleted way either. I'm guessing it may have been relation related at some point as the area tagged as a slide seems to have rendered as an area of water.</p>
</div>
<div id="comment-21190-info" class="comment-info">
<span class="comment-age">(04 Apr '13, 15:16)</span> <span class="comment-user userinfo">EdLoach ♦</span>
</div>
</div>
</div>
<div id="comment-tools-21187" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21187-form-container" class="comment-form-container">
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


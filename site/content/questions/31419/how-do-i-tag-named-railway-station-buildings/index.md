+++
type = "question"
title = "How do I tag named railway station buildings?"
description = '''In some areas, the name of a railway station is not the same as the name of the stop on the rail line; for instance, in Atlanta, Georgia, USA, the passenger rail station is known as &quot;Peachtree Station&quot;, but of course as a stop on the Amtrak network it should be labelled as &quot;Atlanta&quot;. I&#x27;m looking thr...'''
date = "2014-03-10T01:51:00Z"
lastmod = "2014-03-10T12:16:00Z"
weight = 31419
keywords = [ "railway", "station", "ref", "public_transport", "name" ]
aliases = [ "/questions/31419" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How do I tag named railway station buildings?](/questions/31419/how-do-i-tag-named-railway-station-buildings)

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
<span id="post-31419-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31419-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-31419-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In some areas, the name of a railway station is not the same as the name of the stop on the rail line; for instance, in Atlanta, Georgia, USA, the passenger rail station is known as "Peachtree Station", but of course as a stop on the Amtrak network it should be labelled as "Atlanta". I'm looking through the wiki pages on <code>public_transport=*</code> and <code>railway=*</code> and having a hard time understanding which parts are recommended, which are deprecated, and in general what I'm supposed to do here.</p>
<p>The best I've come up with so far is: an area outline for the station building itself, tagged with <code>building=train_station</code>, <code>name=Peachtree Station</code>, <code>public_transport=station</code>, and <code>railway=station</code>; and a node on the rail line with <code>public_transport=stop_position</code>, <code>train=yes</code>, and <code>name=Atlanta</code>. But should I be using <code>ref=*</code> for some of these? Is there a different set of tags I need?</p>
<p>(I should maybe add that the former tagging was a single node, next to the tracks, with <code>railway=station</code> and <code>name=Atlanta</code>.)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-railway" rel="tag" title="see questions tagged &#39;railway&#39;">railway</span> <span class="post-tag tag-link-station" rel="tag" title="see questions tagged &#39;station&#39;">station</span> <span class="post-tag tag-link-ref" rel="tag" title="see questions tagged &#39;ref&#39;">ref</span> <span class="post-tag tag-link-public_transport" rel="tag" title="see questions tagged &#39;public_transport&#39;">public_transport</span> <span class="post-tag tag-link-name" rel="tag" title="see questions tagged &#39;name&#39;">name</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Mar '14, 01:51</strong></p>
<img src="https://secure.gravatar.com/avatar/4a4c8a91603aa21e05f5a441d5c13f26?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="blahedo&#39;s gravatar image" />
<p><span>blahedo</span><br />
<span class="score" title="736 reputation points">736</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="19 badges"><span class="silver">●</span><span class="badgecount">19</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="blahedo has 2 accepted answers">50%</span></p>
</div>
</div>
<div id="comments-container-31419" class="comments-container">
&#10;</div>
<div id="comment-tools-31419" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31419-form-container" class="comment-form-container">
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

<span id="31421"></span>

<div id="answer-container-31421" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-31421-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31421-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-31421-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Maybe it's useful to use also/instead an addr:housename=* tag because for me the tag is more for a building than for a more general aspect.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Mar '14, 09:28</strong></p>
<img src="https://secure.gravatar.com/avatar/49a7d0e0408e9cf2f698faac0f4d837a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iii&#39;s gravatar image" />
<p><span>iii</span><br />
<span class="score" title="4892 reputation points"><span>4.9k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="82 badges"><span class="bronze">●</span><span class="badgecount">82</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iii has 16 accepted answers">10%</span></p>
</div>
</div>
<div id="comments-container-31421" class="comments-container">
<span id="31422"></span>
<div id="comment-31422" class="comment">
<div id="post-31422-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>"addr:housename" is for addressing a named house where the addr:number doesn't exist. Surely not something to distinguish a railway station name to its stop name.</p>
</div>
<div id="comment-31422-info" class="comment-info">
<span class="comment-age">(10 Mar '14, 12:16)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
</div>
<div id="comment-tools-31421" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31421-form-container" class="comment-form-container">
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


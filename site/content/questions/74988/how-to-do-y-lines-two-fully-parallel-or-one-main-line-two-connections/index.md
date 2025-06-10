+++
type = "question"
title = "How to do Y lines: two fully parallel or one main line + two connections?"
description = '''Hamburg public transport (HVV) shows two variants on relations for subway/lightrail lines splitting into a &quot;Y&quot; (three endpoints):  S1 (Relation 1660624): starts in Wedel goes via Ohlsdorf and then either continues to end in Poppenbüttel or Airport(Flughafen). U1 (Relation 1687370): starts in Norders...'''
date = "2020-05-25T07:59:00Z"
lastmod = "2020-05-25T10:16:00Z"
weight = 74988
keywords = [ "overpass", "hvv", "y-lines", "subway", "hamburg" ]
aliases = [ "/questions/74988" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to do Y lines: two fully parallel or one main line + two connections?](/questions/74988/how-to-do-y-lines-two-fully-parallel-or-one-main-line-two-connections)

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
<span id="post-74988-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74988-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74988-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hamburg public transport (HVV) shows two variants on relations for subway/lightrail lines splitting into a "Y" (three endpoints):</p>
<ul>
<li>S1 (<a href="https://www.openstreetmap.org/relation/1660624">Relation 1660624</a>): starts in Wedel goes via Ohlsdorf and then either continues to end in Poppenbüttel or Airport(Flughafen).</li>
<li>U1 (<a href="https://www.openstreetmap.org/relation/1687370">Relation 1687370</a>): starts in Norderstedt Mitte goes via Volksdorf and then either continues to end in Ohlstedt or Großhansdorf.</li>
</ul>
<p>Maybe there is subtle differentiation here (which I don't see) on how these trains serve the alternative endpoints by splitting (front/back) at Ohlsdorf/Volksdorf or alternating full trains serving alterative routes (S1 splits in Ohlsdorf), but I would like to understand the reasoning behind mapping S1 as two fully parallel lines starting in Wedel (four relations) and U1 having one main line until Volksdorf plus two connecting lines (six relations).</p>
<p>Both variants show up very differently in Overpass (<a href="https://overpass-api.de/api/sketch-line?network=HVV&amp;ref=U1">U1</a> <a href="https://overpass-api.de/api/sketch-line?network=HVV&amp;ref=S1">S1</a>). I would consider S1 Overpass the correct way to display such a Y-line. But I'm not sure if the difference in relation-style explains this and needs to be fixed.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-hvv" rel="tag" title="see questions tagged &#39;hvv&#39;">hvv</span> <span class="post-tag tag-link-y-lines" rel="tag" title="see questions tagged &#39;y-lines&#39;">y-lines</span> <span class="post-tag tag-link-subway" rel="tag" title="see questions tagged &#39;subway&#39;">subway</span> <span class="post-tag tag-link-hamburg" rel="tag" title="see questions tagged &#39;hamburg&#39;">hamburg</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 May '20, 07:59</strong></p>
<img src="https://secure.gravatar.com/avatar/6c96e1eccad03a6c6a0d2169a3a9e97a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Aeroid&#39;s gravatar image" />
<p><span>Aeroid</span><br />
<span class="score" title="10 reputation points">10</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Aeroid has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-74988" class="comments-container">
&#10;</div>
<div id="comment-tools-74988" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74988-form-container" class="comment-form-container">
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

<span id="74991"></span>

<div id="answer-container-74991" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74991-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74991-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74991-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The graphical representation with Overpass seems to be misleading. Have a look at these alternative graphs: <a href="http://www.roeltgen.com/gpx/ibro_ol4ptest.html?pt=tag,box&amp;ids=1660624&amp;idm=1660624">S1</a>, <a href="http://www.roeltgen.com/gpx/ibro_ol4ptest.html?pt=tag,box&amp;ids=1687370&amp;idm=1687370">U1</a>. You can switch on/off the individual branches through the menu under the "LS" button on the top right.</p>
<p>Both ways of mapping are used. I tend to follow the S1 way and I think that is what is mostly done in my local Verkehrsverbund but the U1 way is quicker to do as you don't have to repeat everything for the common section.</p>
<p>As long as we don't have timetable information in our data it doesn't really matter which way is followed.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 May '20, 08:46</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 May '20, 09:06</strong> </span></p>
</div>
</div>
<div id="comments-container-74991" class="comments-container">
<span id="74992"></span>
<div id="comment-74992" class="comment">
<div id="post-74992-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, but I guess the 6-relation-variant (U1) has the general disadvantage of not differentiating between the two "leaves" and the "trunk". That Overpass chooses the "joint" as a starting point out of the four options is certainly the worse case, which S1 avoids by not offering the "joint" as an end point.</p>
</div>
<div id="comment-74992-info" class="comment-info">
<span class="comment-age">(25 May '20, 10:16)</span> <span class="comment-user userinfo">Aeroid</span>
</div>
</div>
</div>
<div id="comment-tools-74991" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74991-form-container" class="comment-form-container">
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


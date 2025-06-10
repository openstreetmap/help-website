+++
type = "question"
title = "two unidirectional cycle lanes"
description = '''How do I tag a one-way road with two cycle lanes on the left, and both travelling in the same direction? Should I treat it like a single cycle lane?'''
date = "2018-04-18T09:45:00Z"
lastmod = "2018-04-20T01:53:00Z"
weight = 63021
keywords = [ "lane", "oneway", "bicycle", "tagging", "cycleway" ]
aliases = [ "/questions/63021" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [two unidirectional cycle lanes](/questions/63021/two-unidirectional-cycle-lanes)

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
<span id="post-63021-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63021-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63021-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How do I tag a one-way road with two cycle lanes on the left, and both travelling in the same direction? Should I treat it like a single cycle lane?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-lane" rel="tag" title="see questions tagged &#39;lane&#39;">lane</span> <span class="post-tag tag-link-oneway" rel="tag" title="see questions tagged &#39;oneway&#39;">oneway</span> <span class="post-tag tag-link-bicycle" rel="tag" title="see questions tagged &#39;bicycle&#39;">bicycle</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-cycleway" rel="tag" title="see questions tagged &#39;cycleway&#39;">cycleway</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Apr '18, 09:45</strong></p>
<img src="https://secure.gravatar.com/avatar/3d0cd8219bcdca4ba0d07d7878a1ce11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Plattypus&#39;s gravatar image" />
<p><span>Plattypus</span><br />
<span class="score" title="81 reputation points">81</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Plattypus has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Apr '18, 09:49</strong> </span></p>
</div>
</div>
<div id="comments-container-63021" class="comments-container">
<span id="63024"></span>
<div id="comment-63024" class="comment">
<div id="post-63024-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Are these cycle lanes (i.e. just painted delineation from cars) or tracks (physical segregation)?</p>
</div>
<div id="comment-63024-info" class="comment-info">
<span class="comment-age">(18 Apr '18, 13:30)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="63036"></span>
<div id="comment-63036" class="comment">
<div id="post-63036-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, that's right. The cycle lanes are marked with dashed white lines, but there's also a solid yellow line separating the car lanes from the bike lanes.</p>
</div>
<div id="comment-63036-info" class="comment-info">
<span class="comment-age">(19 Apr '18, 05:21)</span> <span class="comment-user userinfo">Plattypus</span>
</div>
</div>
</div>
<div id="comment-tools-63021" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63021-form-container" class="comment-form-container">
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

<span id="63035"></span>

<div id="answer-container-63035" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63035-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63035-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63035-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If they are indeed only separated by paint from the area where the car drives:</p>
<ul>
<li>cycleway:left=lane (or cycleway:right=lane depending on the orientation of the OSM-way)</li>
<li>oneway:bicycle=no</li>
</ul>
<p>replace lane with track in case there is a physical separator such as a kerb, grass, etc.</p>
<p>More information can be found on the <a href="https://wiki.openstreetmap.org/wiki/Bicycle">Bicycle</a> wiki page, where the case you describe is depicted as L1b I think</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Apr '18, 04:20</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-63035" class="comments-container">
<span id="63037"></span>
<div id="comment-63037" class="comment">
<div id="post-63037-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This wouldn't work as the cycle lanes are not going in opposite directions. It is a one-way road for bicycles. I couldn't find this case on the wiki page - that's why I posted here. I suppose it's a fairly unusual arrangement - I'm not sure why the city designed the lanes like that.</p>
</div>
<div id="comment-63037-info" class="comment-info">
<span class="comment-age">(19 Apr '18, 05:26)</span> <span class="comment-user userinfo">Plattypus</span>
</div>
</div>
<span id="63038"></span>
<div id="comment-63038" class="comment">
<div id="post-63038-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>then you can solve that with the lanes tag.</p>
<p>lanes = 1 (normally only lanes for motorized traffic are counted, so not the bicycle lanes, some people will map this as 3 though)</p>
<p>lanes:bicycle = no|designated|designated (this can have more lanes than mentioned in the lanes tag, though many QA tools will complain).</p>
</div>
<div id="comment-63038-info" class="comment-info">
<span class="comment-age">(19 Apr '18, 06:37)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="63042"></span>
<div id="comment-63042" class="comment">
<div id="post-63042-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Ah ok! Thank you. So I've tagged it now with "lanes=4 + bicycle:lanes=designated|designated|| + motorcycle:lanes=designated|designated||".</p>
</div>
<div id="comment-63042-info" class="comment-info">
<span class="comment-age">(19 Apr '18, 08:46)</span> <span class="comment-user userinfo">Plattypus</span>
</div>
</div>
<span id="63054"></span>
<div id="comment-63054" class="comment">
<div id="post-63054-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm definitely in favor of the "count all the lanes" not just "count only the motorized lanes". Cyclists need lane information, too, and having a complete picture of all the lanes, including cycle lanes, provides better lane guidance for motorists as well.</p>
</div>
<div id="comment-63054-info" class="comment-info">
<span class="comment-age">(20 Apr '18, 01:53)</span> <span class="comment-user userinfo">Baloo Uriza</span>
</div>
</div>
</div>
<div id="comment-tools-63035" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63035-form-container" class="comment-form-container">
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


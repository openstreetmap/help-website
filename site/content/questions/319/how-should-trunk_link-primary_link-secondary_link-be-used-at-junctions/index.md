+++
type = "question"
title = "How should trunk_link, primary_link, secondary_link be used at junctions?"
description = '''Should a *_link road be the same &#x27;rank&#x27; as the most important road involved in the junction? Or should it try to indicate the type of road that it leads to? For example, if a trunk road has a one-way slip road off onto a primary road, then should that road be tagged as a &quot;trunk_link&quot;, as it is a lin...'''
date = "2010-07-19T11:30:00Z"
lastmod = "2010-07-19T20:44:00Z"
weight = 319
keywords = [ "roads", "junction", "tagging" ]
aliases = [ "/questions/319" ]
osqa_answers = 4
osqa_accepted = true
+++

<div class="headNormal">

# [How should trunk_link, primary_link, secondary_link be used at junctions?](/questions/319/how-should-trunk_link-primary_link-secondary_link-be-used-at-junctions)

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
<span id="post-319-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-319-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-319-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
2
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Should a <code>*_link</code> road be the same 'rank' as the most important road involved in the junction?<br />
Or should it try to indicate the type of road that it leads to?</p>
<p>For example, if a <code>trunk</code> road has a one-way slip road off onto a <code>primary</code> road, then should that road be tagged as a "<code>trunk_link</code>", as it is a link <em>from</em> a <code>trunk</code> (and <code>trunk</code> road rules may still apply); or should it be a "<code>primary_link</code>", as it is a link <em>to</em> a <code>primary</code> road?</p>
<p>And should the link be marked with the <code>ref</code> of the road that it leads to, or just left blank?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-roads" rel="tag" title="see questions tagged &#39;roads&#39;">roads</span> <span class="post-tag tag-link-junction" rel="tag" title="see questions tagged &#39;junction&#39;">junction</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Jul '10, 11:30</strong></p>
<img src="https://secure.gravatar.com/avatar/f61876d1f1d2de794259119cdd596316?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GrahamS&#39;s gravatar image" />
<p><span>GrahamS</span><br />
<span class="score" title="3635 reputation points"><span>3.6k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="45 badges"><span class="silver">●</span><span class="badgecount">45</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GrahamS has 7 accepted answers">28%</span> </br></p>
</div>
</div>
<div id="comments-container-319" class="comments-container">
&#10;</div>
<div id="comment-tools-319" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-319-form-container" class="comment-form-container">
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

4 Answers:

</div>

</div>

<span id="326"></span>

<div id="answer-container-326" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-326-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-326-score" class="post-score" title="current number of votes">
7
</div>
<span id="post-326-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="GrahamS has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You should use the link type which reflects the set of rules that apply to that road. If the link is under motorway rules, use <code>highway=motorway_link</code>; if it's under trunk road rules (for your country) use <code>highway=trunk_link</code>, and so on. This is where the meaning in <code>*_link</code> highway types comes from.</p>
<p>If there's no explicit designation for a link road, you can deduce the rules in place from clues like where the speed limit changes, any roadside markings, or any other roadsigns (such as No Stopping) signs. It may not always be the designation for the higher of the two roads it connects.</p>
<p>The <code>ref=*</code> should be omitted unless the link road itself has a route reference.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Jul '10, 14:22</strong></p>
<img src="https://secure.gravatar.com/avatar/9fe361843971cf8b23dc93517f00b996?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jonathan%20Bennett&#39;s gravatar image" />
<p><span>Jonathan Ben...</span><br />
<span class="score" title="8261 reputation points"><span>8.3k</span></span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="85 badges"><span class="silver">●</span><span class="badgecount">85</span></span><span title="108 badges"><span class="bronze">●</span><span class="badgecount">108</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jonathan Bennett has 21 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Sep '10, 23:43</strong> </span></p>
</div>
</div>
<div id="comments-container-326" class="comments-container">
<span id="335"></span>
<div id="comment-335" class="comment">
<div id="post-335-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks. Indicating the rules of the road makes sense to me. I guess the remaining vagueness is where the rules don't change. i.e. In the UK there is no real difference between a trunk and primary (as used by OSM) so I think in that situation we may have to fall back on what looks the best.</p>
</div>
<div id="comment-335-info" class="comment-info">
<span class="comment-age">(19 Jul '10, 20:44)</span> <span class="comment-user userinfo">GrahamS</span>
</div>
</div>
</div>
<div id="comment-tools-326" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-326-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="331"></span>

<div id="answer-container-331" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-331-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-331-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-331-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The link should always be tagged with the "higher" link road class. So a connection between a motorway and a trunks gets motorway_link etc. The reason is not only that it looks better, it also reflects reality in that the "higher" the road class the more restrictions regarding the type of traffic there usually are. And on and off ramps must obviously have the same kind of restrictions as the main road. There are no bicycles allowed on the motorway on-ramp because it leads to a motorway that doesn't allow bicycles.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Jul '10, 14:46</strong></p>
<img src="https://secure.gravatar.com/avatar/2d4dfcdcde73aa5e2ffa4a9b3a7cb51d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jochen%20Topf&#39;s gravatar image" />
<p><span>Jochen Topf</span><br />
<span class="score" title="5244 reputation points"><span>5.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jochen Topf has 32 accepted answers">31%</span></p>
</div>
</div>
<div id="comments-container-331" class="comments-container">
&#10;</div>
<div id="comment-tools-331" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-331-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="329"></span>

<div id="answer-container-329" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-329-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-329-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-329-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The rule has always been to use the highest classification - so a link road between a motorway and any other sort of road is motorway_link, a link road between a trunk road and anything that isn't a motorway is trunk_link and so on.</p>
<p>I don't normally apply a ref or name to a link road, but some people do.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Jul '10, 14:35</strong></p>
<img src="https://secure.gravatar.com/avatar/dee41dcf0aa0c08cf6b0eb935b7504b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TomH&#39;s gravatar image" />
<p><span>TomH ♦♦</span><br />
<span class="score" title="3325 reputation points"><span>3.3k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="43 badges"><span class="bronze">●</span><span class="badgecount">43</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TomH has 9 accepted answers">20%</span></p>
</div>
</div>
<div id="comments-container-329" class="comments-container">
&#10;</div>
<div id="comment-tools-329" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-329-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="320"></span>

<div id="answer-container-320" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-320-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-320-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-320-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There's no consensus on whether to use the higher or lower classification. I personally use the higher if it's a complicated interchange but the lower if it's a simple intersection bypass. Other people always use the lower or the higher. Since the type of link (other than motorway_link, which comes with restrictions) has no real-world meaning, the only consideration is how it looks when rendered, and different people have different preferences.</p>
<p>In my opinion and experience, links should not be tagged with refs unless they actually carry a route. There's no benefit in adding the ref and the potential exists for confusion. But some countries may have a different default (I think Germany does include a ref; I'm not sure how they treat a link that splits for multiple roads).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Jul '10, 11:52</strong></p>
<img src="https://secure.gravatar.com/avatar/0c334b9f230e39c1e73a2b0322a23fb3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NE2&#39;s gravatar image" />
<p><span>NE2</span><br />
<span class="score" title="1359 reputation points"><span>1.4k</span></span><span title="33 badges"><span class="badge1">●</span><span class="badgecount">33</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NE2 has one accepted answer">9%</span></p>
</div>
</div>
<div id="comments-container-320" class="comments-container">
&#10;</div>
<div id="comment-tools-320" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-320-form-container" class="comment-form-container">
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


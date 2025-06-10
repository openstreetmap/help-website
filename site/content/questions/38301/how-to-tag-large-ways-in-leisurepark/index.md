+++
type = "question"
title = "How to tag large ways in leisure=park?"
description = '''Normally, we tag the ways in a public park as highway=footway. However, in many parks the ways are very large or even large areas, especially in &quot;french&quot; style parks as seen here. Tagging these surfaces as closed ways with highway=footway is disadvised by the wiki. So, what would be the good way to ...'''
date = "2014-11-04T09:16:00Z"
lastmod = "2014-11-04T11:45:00Z"
weight = 38301
keywords = [ "park", "tagging", "leisure", "area" ]
aliases = [ "/questions/38301" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to tag large ways in leisure=park?](/questions/38301/how-to-tag-large-ways-in-leisurepark)

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
<span id="post-38301-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38301-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-38301-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Normally, we tag the ways in a public park as highway=footway. However, in many parks the ways are very large or even large areas, especially in "french" style parks as seen <span>here</span>. Tagging these surfaces as closed ways with highway=footway is disadvised by the <span>wiki</span>. So, what would be the good way to tag these areas?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-park" rel="tag" title="see questions tagged &#39;park&#39;">park</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-leisure" rel="tag" title="see questions tagged &#39;leisure&#39;">leisure</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Nov '14, 09:16</strong></p>
<img src="https://secure.gravatar.com/avatar/71c1ae65b2c4cb9d6603635965a86fe1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rainerU&#39;s gravatar image" />
<p><span>rainerU</span><br />
<span class="score" title="106 reputation points">106</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rainerU has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Nov '14, 12:45</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-38301" class="comments-container">
&#10;</div>
<div id="comment-tools-38301" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38301-form-container" class="comment-form-container">
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

<span id="38302"></span>

<div id="answer-container-38302" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-38302-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38302-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-38302-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In this case drawing a closed way with <em><a href="http://wiki.openstreetmap.org/wiki/Tag:highway%3Dpedestrian">highway=pedestrian</a></em> and <em>area=yes</em> seems fine to me. If bicycles are allowed then add <em>bicycle=yes</em>, too.</p>
<p>Alternatively there is a <a href="https://wiki.openstreetmap.org/wiki/Proposed_features/area:highway"><em>area:highway</em> proposal</a> which suggests to use the tag <em>area:highway=footway</em> without(!) an additional <em>highway</em> tag. This isn't currently rendered anywhere as far as I know.</p>
<p>Note that you can always specify the <a href="http://wiki.openstreetmap.org/wiki/Key:width">width</a> of a way, although it won't get rendered at the standard layers at the moment.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Nov '14, 09:35</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Nov '14, 10:10</strong> </span></p>
</div>
</div>
<div id="comments-container-38302" class="comments-container">
<span id="38306"></span>
<div id="comment-38306" class="comment">
<div id="post-38306-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>highway=pedestrian is the appropriate tag for downtown shopping areas but seems not to fit for ways and areas in recreational parks. area:highway seems the better solution. According ti tagwatch it is used 12.400 times, and will hopefully be rendered some day on the major maps.</p>
</div>
<div id="comment-38306-info" class="comment-info">
<span class="comment-age">(04 Nov '14, 11:34)</span> <span class="comment-user userinfo">rainerU</span>
</div>
</div>
<span id="38307"></span>
<div id="comment-38307" class="comment">
<div id="post-38307-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>In my opinion highway=pedestrian should not be restricted to shopping areas. Shopping areas are just an example where highway=pedestrian can often be found.</p>
</div>
<div id="comment-38307-info" class="comment-info">
<span class="comment-age">(04 Nov '14, 11:45)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-38302" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38302-form-container" class="comment-form-container">
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


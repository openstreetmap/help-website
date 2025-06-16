+++
type = "question"
title = "What is the meaning of railway=station on a closed way?"
description = '''I wonder what is the meaning of railway=station on a closed way. In my area mappers have started to tag the whole area of the station (including tracks and outdoor areas) like this. This seems logical to me, but it renders the whole area like a building in Mapnik (i.e. Mapnik makers say that buildin...'''
date = "2011-03-22T18:46:00Z"
lastmod = "2016-03-01T17:47:00Z"
weight = 3989
keywords = [ "railway", "station", "tagging", "area" ]
aliases = [ "/questions/3989" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [What is the meaning of railway=station on a closed way?](/questions/3989/what-is-the-meaning-of-railwaystation-on-a-closed-way)

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
<span id="post-3989-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3989-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-3989-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I wonder what is the meaning of <code>railway=station</code> on a closed way. In my area mappers have started to tag the whole area of the station (including tracks and outdoor areas) like this. This seems logical to me, but it renders the whole area like a building in Mapnik (i.e. Mapnik makers say that <code>building=station</code> and <code>railway=station</code> are the same). Is there a better way to map the actual area of a railway station? (I'd exclude <code>landuse=railway</code> because this is for all railway areas including but not limited to stations).</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-railway" rel="tag" title="see questions tagged &#39;railway&#39;">railway</span> <span class="post-tag tag-link-station" rel="tag" title="see questions tagged &#39;station&#39;">station</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Mar '11, 18:46</strong></p>
<img src="https://secure.gravatar.com/avatar/f09c0b7a655fed386e070e036e2da248?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dieterdreist&#39;s gravatar image" />
<p><span>dieterdreist</span><br />
<span class="score" title="3677 reputation points"><span>3.7k</span></span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="67 badges"><span class="bronze">●</span><span class="badgecount">67</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dieterdreist has 4 accepted answers">3%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Mar '11, 11:50</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/dee41dcf0aa0c08cf6b0eb935b7504b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TomH&#39;s gravatar image" />
<p><span>TomH ♦♦</span><br />
<span class="score" title="3325 reputation points"><span>3.3k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="43 badges"><span class="bronze">●</span><span class="badgecount">43</span></span></p>
</div>
</div>
<div id="comments-container-3989" class="comments-container">
&#10;</div>
<div id="comment-tools-3989" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3989-form-container" class="comment-form-container">
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

<span id="3991"></span>

<div id="answer-container-3991" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-3991-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3991-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-3991-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="dieterdreist has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Nothing in OSM has an inherent meaning; tags are just combinations of letters. Meaning arises in the heads of people who work with the data. If you want to do a poll, then this is the wrong forum; maybe you should randomly select a number of people who have used the tags in question and ask them what they meant with that!</p>
<p>If you have an issue with the standard Mapnik stylesheet, then <a href="http://trac.openstreetmap.org">Trac</a> is the right place to submit a change request. If you'd rather discuss the issue with fellow mappers, choose one of the mailing lists or the forum.</p>
<p>Generally, I think that many people assume that when they draw a building instead of a POI node, they can transfer the node's tags to the building. That's probably the reason why our cartographers have decided to treat <code>railway=station</code> like a building.</p>
<p>Maybe you could tag the wider area as <code>landuse=railway</code> (because how will you know if something is still part of the station or part of some other railway area?) and then tag the actual building as <code>railway=station</code>?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Mar '11, 19:46</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Mar '11, 22:36</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/9fe361843971cf8b23dc93517f00b996?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jonathan%20Bennett&#39;s gravatar image" />
<p><span>Jonathan Ben...</span><br />
<span class="score" title="8261 reputation points"><span>8.3k</span></span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="85 badges"><span class="silver">●</span><span class="badgecount">85</span></span><span title="108 badges"><span class="bronze">●</span><span class="badgecount">108</span></span></p>
</div>
</div>
<div id="comments-container-3991" class="comments-container">
<span id="4004"></span>
<div id="comment-4004" class="comment">
<div id="post-4004-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I agree with your initial statement, and agree that landuse=railway could be used on the station as well as it is used on the rest of the areas used by the railways, but it is not an alternative to tag the limits of the station. With building=station already in use I don't see a point in tagging only the railway building with railway=station. Also the nodes formerly tagged with railway=station have been part of the tracks themselves, so they have not been buildings in the beginning, and logically it makes no sense to make them buildings now.</p>
</div>
<div id="comment-4004-info" class="comment-info">
<span class="comment-age">(23 Mar '11, 10:29)</span> <span class="comment-user userinfo">dieterdreist</span>
</div>
</div>
</div>
<div id="comment-tools-3991" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3991-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="48436"></span>

<div id="answer-container-48436" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48436-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48436-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-48436-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>When I've been working with stations locally the buildings are oftern a small part so the platforms are marked oftern as seperate areas indepenant to the buildings and often a old poi tags acts like a village indicator and floats, or is bound to one of the lines (probably from when there where no features mapped.</p>
<p>Some sites have been resolved with a neat multipolygon relation that works really well in most places as the name can then cover the site sensibly for verious scales in the renderer. especialy on complex sites.</p>
<p>I think over time that is what our local staions will be converted to and all the platfoms and small features like boths, info points toilets and so on can be rendered well (on large sites when showing small features font sizes can sensibly be adjusted to fit and showing the promernace and coverage) - these appearing a renderer specific but giving a renderer writer an easy task is always helpful to getting things implemented :)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Mar '16, 17:36</strong></p>
<img src="https://secure.gravatar.com/avatar/30d90feb3a40fa6255767f95a8cd7943?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Govanus&#39;s gravatar image" />
<p><span>Govanus</span><br />
<span class="score" title="154 reputation points">154</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Govanus has one accepted answer">3%</span></p>
</div>
</div>
<div id="comments-container-48436" class="comments-container">
<span id="48438"></span>
<div id="comment-48438" class="comment">
<div id="post-48438-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://www.openstreetmap.org/#map=18/48.84448/2.37561">https://www.openstreetmap.org/#map=18/48.84448/2.37561</a> has a lot of indoor features <a href="https://www.openstreetmap.org/relation/5695079">https://www.openstreetmap.org/relation/5695079</a> a relation example complecated by being a multi use shed site</p>
</div>
<div id="comment-48438-info" class="comment-info">
<span class="comment-age">(01 Mar '16, 17:43)</span> <span class="comment-user userinfo">Govanus</span>
</div>
</div>
<span id="48439"></span>
<div id="comment-48439" class="comment">
<div id="post-48439-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://www.openstreetmap.org/way/333666174#map=18/51.61749/-1.24608">https://www.openstreetmap.org/way/333666174#map=18/51.61749/-1.24608</a> shows a way one renderer handels the small to large scal transition but it is a pure render choice</p>
</div>
<div id="comment-48439-info" class="comment-info">
<span class="comment-age">(01 Mar '16, 17:47)</span> <span class="comment-user userinfo">Govanus</span>
</div>
</div>
</div>
<div id="comment-tools-48436" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48436-form-container" class="comment-form-container">
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


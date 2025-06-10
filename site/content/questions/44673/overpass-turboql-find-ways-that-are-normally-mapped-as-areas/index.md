+++
type = "question"
title = "Overpass Turbo/QL Find ways that are normally mapped as areas"
description = '''Hi I wish to use Overpass Turbo to search for ways that should normally be mapped as areas but are erroneously not joined ie landuse=residential. I&#x27;ve looked through the (not very clear) help but can see nothing related to my query. I assume it must be possible because OT displays such ways in the t...'''
date = "2015-08-09T13:40:00Z"
lastmod = "2015-08-09T15:46:00Z"
weight = 44673
keywords = [ "overpass", "overpass-turbo", "overpass-ql", "area" ]
aliases = [ "/questions/44673" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Overpass Turbo/QL Find ways that are normally mapped as areas](/questions/44673/overpass-turboql-find-ways-that-are-normally-mapped-as-areas)

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
<span id="post-44673-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44673-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-44673-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi</p>
<p>I wish to use Overpass Turbo to search for ways that should normally be mapped as areas but are erroneously not joined ie landuse=residential.</p>
<p>I've looked through the (not very clear) help but can see nothing related to my query. I assume it must be possible because OT displays such ways in the thicker blue line than if they're joined?</p>
<p>Thanks Dave F.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-overpass-ql" rel="tag" title="see questions tagged &#39;overpass-ql&#39;">overpass-ql</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Aug '15, 13:40</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Feb '19, 09:06</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-44673" class="comments-container">
&#10;</div>
<div id="comment-tools-44673" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44673-form-container" class="comment-form-container">
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

<span id="44674"></span>

<div id="answer-container-44674" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44674-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44674-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-44674-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="DaveF has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Overpass API and overpass turbo really are not the right tools for this job, as you cannot query yet for any non-closed areas in the first place (it's not implemented yet). This makes the whole endeavour very challenging.</p>
<p>What you see in overpass turbo originates from the internal OSM -&gt; GeoJSON conversion, but it's not possible to take that logic into account for any kind of query.</p>
<p>I suggest to take a look at keep right! instead. It has a "non-closed area" detection. Osmose QA probably has something similar.</p>
<p>Example: <a href="http://keepright.at/report_map.php?zoom=17&amp;lat=48.15152&amp;lon=16.29759&amp;layers=B0T&amp;ch=0%2C30&amp;show_ign=1&amp;show_tmpign=1">Keep right! example</a> -&gt; will mark the following <a href="http://www.openstreetmap.org/way/349493111">way</a> as erroneous.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Aug '15, 14:30</strong></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmd has 44 accepted answers">37%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Aug '15, 14:45</strong> </span></p>
</div>
</div>
<div id="comments-container-44674" class="comments-container">
<span id="44675"></span>
<div id="comment-44675" class="comment">
<div id="post-44675-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It's a shame overpass isn't able to make that distinction, but Keep Right does an adequate job for what I want in this instance.</p>
<p>Thank you for your reply. Dave F.</p>
</div>
<div id="comment-44675-info" class="comment-info">
<span class="comment-age">(09 Aug '15, 15:36)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
<span id="44676"></span>
<div id="comment-44676" class="comment">
<div id="post-44676-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Well, I guess nobody requested this feature so far --&gt; <a href="https://github.com/drolbr/Overpass-API/issues">https://github.com/drolbr/Overpass-API/issues</a></p>
</div>
<div id="comment-44676-info" class="comment-info">
<span class="comment-age">(09 Aug '15, 15:46)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
</div>
<div id="comment-tools-44674" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44674-form-container" class="comment-form-container">
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


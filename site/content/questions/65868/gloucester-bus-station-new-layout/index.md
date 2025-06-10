+++
type = "question"
title = "Gloucester Bus Station new layout"
description = '''Gloucester Bus Station will be moving to a new layout mid October but the old layout will show until that point. How can I temporarily show both layouts or am I able to download the new layout myself?'''
date = "2018-09-12T12:20:00Z"
lastmod = "2018-09-12T17:08:00Z"
weight = 65868
keywords = [ "datadisplay", "station", "layout", "busstops", "gloucester" ]
aliases = [ "/questions/65868" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Gloucester Bus Station new layout](/questions/65868/gloucester-bus-station-new-layout)

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
<span id="post-65868-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65868-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65868-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Gloucester Bus Station will be moving to a new layout mid October but the old layout will show until that point. How can I temporarily show both layouts or am I able to download the new layout myself?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-datadisplay" rel="tag" title="see questions tagged &#39;datadisplay&#39;">datadisplay</span> <span class="post-tag tag-link-station" rel="tag" title="see questions tagged &#39;station&#39;">station</span> <span class="post-tag tag-link-layout" rel="tag" title="see questions tagged &#39;layout&#39;">layout</span> <span class="post-tag tag-link-busstops" rel="tag" title="see questions tagged &#39;busstops&#39;">busstops</span> <span class="post-tag tag-link-gloucester" rel="tag" title="see questions tagged &#39;gloucester&#39;">gloucester</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Sep '18, 12:20</strong></p>
<img src="https://secure.gravatar.com/avatar/e766af1787b1b1a67960f2ef9985f2c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tashia-traveline%20Gloucester&#39;s gravatar image" />
<p><span>Tashia-trave...</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tashia-traveline Gloucester has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-65868" class="comments-container">
&#10;</div>
<div id="comment-tools-65868" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65868-form-container" class="comment-form-container">
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

<span id="65869"></span>

<div id="answer-container-65869" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65869-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65869-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-65869-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In general OSM only allows one view of the data, which should be as close to what is currently on the ground as mapping contributions allow. Therefore the current active layout should be retained.</p>
<p>Many changes can be mapped using the construction tag in association with landuse and highway, e.g., construction=service and highway=construction. This allows the new configuration to be mapped quickly once it goes live.</p>
<p>If you want to map the new configuration for your own purposes than you could do that off-line using the JOSM desktop editor. Potentially such mapping could be merged with the main database when the new bus station opens.</p>
<p>In general there is considerable experience within OSM of tracking changes to public transport infrastructure so as to show the new facilities from day one (notably with new tram and metro lines). So there are people who can provide very specific advice.</p>
<p>I'm presuming this is Gloucester, England on the basis of <a href="https://www.gloucestershirelive.co.uk/news/gloucester-news/exact-date-gloucesters-new-multi-1832944">this article</a>, and your edits(!). I also presume that the shops at Grovsenor House have gone (at least in part), and that, because the new building overlaps, the building itself is (partially) demolished). So my minium recommendations would be:</p>
<ul>
<li>Delineate the current construction area with landuse=construction</li>
<li>Remove or (better) change the tagging of any demolished buildings (e.g. change building to demolished:building). The latter is better because it shows to other mappers that the building is gone. It is not unknown for people to assume more up-to-date data is actually older than the aerial images.</li>
<li>Mark any access footways which are currently obstructed as access=private.</li>
<li>Some new information can be added, for instance location of new bus stops, but use the highway=construction, construction=bus_stop approach.</li>
</ul>
<p>HTH</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Sep '18, 17:08</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-65869" class="comments-container">
&#10;</div>
<div id="comment-tools-65869" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65869-form-container" class="comment-form-container">
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


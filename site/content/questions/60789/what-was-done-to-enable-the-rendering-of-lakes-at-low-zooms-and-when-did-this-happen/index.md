+++
type = "question"
title = "What was done to enable the rendering of lakes at low zooms? And when did this happen?"
description = '''I just noticed that the Great Lakes of Canada and the US now show up at all zoom levels, and then noticed that this seems to be true of all lakes. I&#x27;d thought that there was a technical reason making this very resource intensive, and so wasn&#x27;t done. (There was some discussion about this a year or tw...'''
date = "2017-11-26T02:10:00Z"
lastmod = "2017-11-26T05:50:00Z"
weight = 60789
keywords = [ "osm-carto", "rendering", "waterbody", "lake", "mapnik" ]
aliases = [ "/questions/60789" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [What was done to enable the rendering of lakes at low zooms? And when did this happen?](/questions/60789/what-was-done-to-enable-the-rendering-of-lakes-at-low-zooms-and-when-did-this-happen)

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
<span id="post-60789-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60789-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-60789-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I just noticed that the Great Lakes of Canada and the US now show up at all zoom levels, and then noticed that this seems to be true of all lakes.</p>
<p>I'd thought that there was a technical reason making this very resource intensive, and so wasn't done. (There was some discussion about this a year or two back, when the Great Lakes were tagged as Lakes, having been tagged as sea for an extended period)</p>
<p>Has somebody come up with something clever, are the rendering servers just allocating more rendering resources for this task, or is something else going on?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm-carto" rel="tag" title="see questions tagged &#39;osm-carto&#39;">osm-carto</span> <span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-waterbody" rel="tag" title="see questions tagged &#39;waterbody&#39;">waterbody</span> <span class="post-tag tag-link-lake" rel="tag" title="see questions tagged &#39;lake&#39;">lake</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Nov '17, 02:10</strong></p>
<img src="https://secure.gravatar.com/avatar/f88a467aa884aeb760041004f62448ee?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="keithonearth&#39;s gravatar image" />
<p><span>keithonearth</span><br />
<span class="score" title="2939 reputation points"><span>2.9k</span></span><span title="56 badges"><span class="badge1">●</span><span class="badgecount">56</span></span><span title="76 badges"><span class="silver">●</span><span class="badgecount">76</span></span><span title="108 badges"><span class="bronze">●</span><span class="badgecount">108</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="keithonearth has 3 accepted answers">13%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Nov '17, 02:42</strong> </span></p>
</div>
</div>
<div id="comments-container-60789" class="comments-container">
&#10;</div>
<div id="comment-tools-60789" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60789-form-container" class="comment-form-container">
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

<span id="60791"></span>

<div id="answer-container-60791" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60791-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60791-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-60791-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You probably mean standard tile layer powered by osm-carto style? Yes, it was related to heavy database requests, but I've found that we can limit them a lot without big visual consequences:</p>
<p><a href="https://github.com/gravitystorm/openstreetmap-carto/pull/2873">https://github.com/gravitystorm/openstreetmap-carto/pull/2873</a></p>
<p>It has been released with v4.4.0 (2017-10-20) and soon deployed on OSMF servers.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Nov '17, 02:46</strong></p>
<img src="https://secure.gravatar.com/avatar/e228dd20b7da2a6c8f559e2118ce08d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kocio&#39;s gravatar image" />
<p><span>kocio</span><br />
<span class="score" title="2054 reputation points"><span>2.1k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kocio has 14 accepted answers">20%</span></p>
</div>
</div>
<div id="comments-container-60791" class="comments-container">
<span id="60795"></span>
<div id="comment-60795" class="comment">
<div id="post-60795-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks Kocio! Good to get the info straight from you.</p>
<p>Yes, you're right I meant osm-carto style, I could have made that more clear.</p>
<p>I was especially impressed by how Canada looks now that the lakes are getting rendered. I forget how many lakes they have in Eastern Canada.</p>
<p>Looks great!</p>
</div>
<div id="comment-60795-info" class="comment-info">
<span class="comment-age">(26 Nov '17, 04:53)</span> <span class="comment-user userinfo">keithonearth</span>
</div>
</div>
<span id="60796"></span>
<div id="comment-60796" class="comment">
<div id="post-60796-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>North of Europe is pretty similar too... =}</p>
<p>Currently we plan to filter out some smaller lakes on low zoom levels, because they just make noise, but it should only increase readability without loosing general feeling:</p>
<p><a href="https://github.com/gravitystorm/openstreetmap-carto/pull/2952">https://github.com/gravitystorm/openstreetmap-carto/pull/2952</a></p>
</div>
<div id="comment-60796-info" class="comment-info">
<span class="comment-age">(26 Nov '17, 04:59)</span> <span class="comment-user userinfo">kocio</span>
</div>
</div>
<span id="60798"></span>
<div id="comment-60798" class="comment">
<div id="post-60798-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the link!</p>
<p>In all honesty I kind of like it the way it is. Or at least 32px seems a bit large to filter. Smaller than 2-4px seems more reasonable to me. But then you can't make everyone happy.</p>
<p>Whatever happens with rendering lakes at low zooms I do appreciate all the work you do on the rendering. The gray parking-lots are pretty cool. :-)</p>
</div>
<div id="comment-60798-info" class="comment-info">
<span class="comment-age">(26 Nov '17, 05:42)</span> <span class="comment-user userinfo">keithonearth</span>
</div>
</div>
<span id="60800"></span>
<div id="comment-60800" class="comment">
<div id="post-60800-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Fixed 32 px filter was just an initial proposition - look at the softer "progressive" filtering demo, which I hope we will merge eventually:</p>
<p><a href="http://bl.ocks.org/math1985/raw/af7a602c222dbf1ff1a2c0d84ed755b7/#6.00/62.408/-102.033">http://bl.ocks.org/math1985/raw/af7a602c222dbf1ff1a2c0d84ed755b7/#6.00/62.408/-102.033</a></p>
<p>And if you like new parking lots, just look at the center of Detroit now and try to imagine it in previous yellow version... =} :</p>
<p><a href="http://www.openstreetmap.org/#map=16/42.3339/-83.0492">http://www.openstreetmap.org/#map=16/42.3339/-83.0492</a></p>
</div>
<div id="comment-60800-info" class="comment-info">
<span class="comment-age">(26 Nov '17, 05:50)</span> <span class="comment-user userinfo">kocio</span>
</div>
</div>
</div>
<div id="comment-tools-60791" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60791-form-container" class="comment-form-container">
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


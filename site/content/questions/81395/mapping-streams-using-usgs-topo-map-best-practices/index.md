+++
type = "question"
title = "Mapping Streams using USGS Topo map, best practices"
description = '''I&#x27;d like to map some streams in my area and I&#x27;m looking for best practices. They&#x27;re not accessible to track using GPS so I was going to use imagery to map them. The streams are visible on some of the Bing Aerial imagery but not always, but the USGS Topographic maps are very accurate. Is it considere...'''
date = "2021-08-20T15:54:00Z"
lastmod = "2021-08-21T11:20:00Z"
weight = 81395
keywords = [ "topographic", "streams", "usgs", "practices" ]
aliases = [ "/questions/81395" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Mapping Streams using USGS Topo map, best practices](/questions/81395/mapping-streams-using-usgs-topo-map-best-practices)

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
<span id="post-81395-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81395-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-81395-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'd like to map some streams in my area and I'm looking for best practices. They're not accessible to track using GPS so I was going to use imagery to map them. The streams are visible on some of the Bing Aerial imagery but not always, but the USGS Topographic maps are very accurate. Is it considered "ok" to use the Topo imagery to trace the streams? Are there best practices with regard to doing so?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-topographic" rel="tag" title="see questions tagged &#39;topographic&#39;">topographic</span> <span class="post-tag tag-link-streams" rel="tag" title="see questions tagged &#39;streams&#39;">streams</span> <span class="post-tag tag-link-usgs" rel="tag" title="see questions tagged &#39;usgs&#39;">usgs</span> <span class="post-tag tag-link-practices" rel="tag" title="see questions tagged &#39;practices&#39;">practices</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Aug '21, 15:54</strong></p>
<img src="https://secure.gravatar.com/avatar/dfbf4141bd05182318d157ff3d1f0b04?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mccarbc&#39;s gravatar image" />
<p><span>mccarbc</span><br />
<span class="score" title="31 reputation points">31</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mccarbc has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-81395" class="comments-container">
&#10;</div>
<div id="comment-tools-81395" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81395-form-container" class="comment-form-container">
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

<span id="81396"></span>

<div id="answer-container-81396" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81396-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81396-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-81396-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>USGS topographic maps are okay to use as a source (that type of US government publication is public domain).</p>
<p>In my semi-arid area I use the USGS maps (selected in the JOSM "imagery" pulldown) for three things when mapping waterways:</p>
<ol>
<li><p>To see if the waterway is considered big enough to map (I also look at available aerial imagery). There are lots of dry gullies around here that may have a visible ephemeral water course that carries so little water so rarely that it is debatable if it counts or not. But if the USGS thought it counted then I figure that is an indication that OSM might be interested in it.</p></li>
<li><p>To see if the waterway has a name.</p></li>
<li><p>To roughly draw the waterway in.</p></li>
</ol>
<p>I find that the USGS topo imagery layer in JOSM (which uses the older maps) to have a fair number of errors in location. So once I get the waterway drawn in per the USGS topos I then adjust it based on imagery to get a better location.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Aug '21, 16:30</strong></p>
<img src="https://secure.gravatar.com/avatar/f60af53a4eba0c21f25c22674fb4a8cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="n76&#39;s gravatar image" />
<p><span>n76</span><br />
<span class="score" title="10839 reputation points"><span>10.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="82 badges"><span class="silver">●</span><span class="badgecount">82</span></span><span title="172 badges"><span class="bronze">●</span><span class="badgecount">172</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="n76 has 48 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-81396" class="comments-container">
<span id="81397"></span>
<div id="comment-81397" class="comment">
<div id="post-81397-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, your answer was very helpful. I plan to do as you mentioned, first map using the USGS Topo layer then adjust using the Bing imagery.</p>
</div>
<div id="comment-81397-info" class="comment-info">
<span class="comment-age">(20 Aug '21, 18:01)</span> <span class="comment-user userinfo">mccarbc</span>
</div>
</div>
<span id="81404"></span>
<div id="comment-81404" class="comment">
<div id="post-81404-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I think the big thing to be aware of with USGS topos (as with NHD data) is that sometimes the survey data is quite a way in the past, but as an aid in conjunction with recent imagery they are invaluable.</p>
</div>
<div id="comment-81404-info" class="comment-info">
<span class="comment-age">(21 Aug '21, 11:20)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-81396" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81396-form-container" class="comment-form-container">
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


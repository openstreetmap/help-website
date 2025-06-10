+++
type = "question"
title = "Should I update existing administrative boundaries to reflect latest OS data?"
description = '''I recently added ward boundaries for the Manchester City Council district area to OSM, which were derived from OS Boundary-Line data (latest update October 2018). I checked that the outer perimeter of all the ward boundaries is coincident with the overall district boundary for Manchester in the same...'''
date = "2018-12-05T12:15:00Z"
lastmod = "2018-12-06T09:05:00Z"
weight = 67073
keywords = [ "admin_boundary", "ordnancesurvey" ]
aliases = [ "/questions/67073" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Should I update existing administrative boundaries to reflect latest OS data?](/questions/67073/should-i-update-existing-administrative-boundaries-to-reflect-latest-os-data)

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
<span id="post-67073-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67073-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-67073-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I recently added ward boundaries for the Manchester City Council district area to OSM, which were derived from <a href="https://www.ordnancesurvey.co.uk/business-and-government/products/boundaryline.html">OS Boundary-Line</a> data (latest update October 2018).<br />
I checked that the outer perimeter of all the ward boundaries is coincident with the overall district boundary for Manchester in the same dataset, and it is. However this current Ordnance Survey boundary seems to have numerous (small) discrepancies from the current OSM administrative (level 8) city boundary (<a href="https://www.openstreetmap.org/relation/146656">relation 146656</a>). This could be because:</p>
<ul>
<li>The current OSM boundary is from a different source than the OS (in which case, which has precedence?)</li>
<li>The boundary has been legally changed since the OSM boundary was uploaded</li>
<li>Various boundary nodes have at some point been moved (accidentally or otherwise)</li>
</ul>
<p>So does the latest OS data for such boundaries take precedence over existing OSM data? Would I be justified in creating new admin boundary relation(s) from the OS data, copying the tags, and deleting the current boundary relations? Alternatively if I leave everything as is, then according to the current OSM model there are small slivers of land dotted around Manchester which are apparently in Manchester but not in a Manchester ward, or vice versa - which seems rather unsatisfactory.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-admin_boundary" rel="tag" title="see questions tagged &#39;admin_boundary&#39;">admin_boundary</span> <span class="post-tag tag-link-ordnancesurvey" rel="tag" title="see questions tagged &#39;ordnancesurvey&#39;">ordnancesurvey</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Dec '18, 12:15</strong></p>
<img src="https://secure.gravatar.com/avatar/99265127a23e440720864dbe51e0b48f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Libarch&#39;s gravatar image" />
<p><span>Libarch</span><br />
<span class="score" title="31 reputation points">31</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Libarch has no accepted answers">0%</span> </br></p>
</div>
</div>
<div id="comments-container-67073" class="comments-container">
&#10;</div>
<div id="comment-tools-67073" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67073-form-container" class="comment-form-container">
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

<span id="67080"></span>

<div id="answer-container-67080" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67080-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67080-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-67080-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In general such questions are not really a good fit for the help site because</p>
<ul>
<li>these are issues that you need to discuss with at least the national OSM community (see <a href="https://lists.openstreetmap.org/listinfo/talk-gb">talk-gb</a>) and even better the local mappers.</li>
<li>a determination if the OS licence in question is compatible with the terms we require needs to be made (aka somebody has to do research on the matter)</li>
<li>and requires specialist knowledge (as to the quality and provenance of the OS data)</li>
<li>you should be at least consulting the <a href="https://wiki.openstreetmap.org/wiki/Import/Guidelines">import guidelines</a> in any case.</li>
</ul>
<p>What I can say is that you should, when reasonably possible, modify existing objects in OSM for updates and not delete them and create newly.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Dec '18, 09:05</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Dec '18, 09:08</strong> </span></p>
</div>
</div>
<div id="comments-container-67080" class="comments-container">
&#10;</div>
<div id="comment-tools-67080" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67080-form-container" class="comment-form-container">
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


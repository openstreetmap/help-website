+++
type = "question"
title = "Upload a list of POIs with addresses"
description = '''I have a list/csv of POIs (letter boxes) with their addresses as street + number. What is the recommended method to upload these to OSM? Since the address database in OSM is very incomplete I was thinking of getting the geographical coordinates from Google maps first.'''
date = "2019-10-03T20:15:00Z"
lastmod = "2019-10-03T20:38:00Z"
weight = 71026
keywords = [ "upload" ]
aliases = [ "/questions/71026" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Upload a list of POIs with addresses](/questions/71026/upload-a-list-of-pois-with-addresses)

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
<span id="post-71026-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71026-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-71026-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a list/csv of POIs (letter boxes) with their addresses as street + number. What is the recommended method to upload these to OSM?</p>
<p>Since the address database in OSM is very incomplete I was thinking of getting the geographical coordinates from Google maps first.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-upload" rel="tag" title="see questions tagged &#39;upload&#39;">upload</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Oct '19, 20:15</strong></p>
<img src="https://secure.gravatar.com/avatar/d9cec5587e4334622b0e1c368534e119?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="%D0%BC%D0%B8%D1%82%D0%BA%D0%BE&#39;s gravatar image" />
<p><span>митко</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="митко has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-71026" class="comments-container">
&#10;</div>
<div id="comment-tools-71026" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71026-form-container" class="comment-form-container">
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

<span id="71028"></span>

<div id="answer-container-71028" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71028-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71028-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-71028-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>We have a few rules on data imports - see <a href="https://wiki.openstreetmap.org/wiki/Import">https://wiki.openstreetmap.org/wiki/Import</a> for details. One of the steps of a successful import is that you must discuss your import with the community, and part of that is a thorough check of the license (i.e. whether we are allowed to use the data). If you geocode your locations with Google, then:</p>
<ol>
<li>The resulting data set is derived from Google and therefore not "clean" from a license point of view; it cannot be imported to OSM.</li>
<li>Even if this was not an issue, the coordinates that Google will give you for the post boxes will very likely not match the OSM map, leading to some letter boxes placed in the middle of (or on the wrong side of) a road, inside buildings, on lakes, and so on. A manual correction would be required BEFORE you import.</li>
<li>Even if all coordinates were perfectly matching OSM, you'd still be faces with situations where OSM already has a post box and you must avoid creating duplicates.</li>
</ol>
<p>A tool to help with the technical aspects of such an import (but not the community and legal aspects) is the "OSM Conflator": <a href="https://wiki.openstreetmap.org/wiki/OSM_Conflator">https://wiki.openstreetmap.org/wiki/OSM_Conflator</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Oct '19, 20:38</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Oct '19, 20:38</strong> </span></p>
</div>
</div>
<div id="comments-container-71028" class="comments-container">
&#10;</div>
<div id="comment-tools-71028" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71028-form-container" class="comment-form-container">
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


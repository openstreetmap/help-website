+++
type = "question"
title = "source data license compatibility"
description = '''Is it permissible to use boulder county open data to create open street map features? If so I intend to process the shapefiles with GDAL and gpsbabel to create gpx tracks to add missing ways to open street maps. https://www.bouldercounty.org/government/open-data/terms-of-use/  License cc4 licenseBou...'''
date = "2018-04-26T14:20:00Z"
lastmod = "2018-04-26T21:05:00Z"
weight = 63170
keywords = [ "license" ]
aliases = [ "/questions/63170" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [source data license compatibility](/questions/63170/source-data-license-compatibility)

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
<span id="post-63170-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63170-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63170-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is it permissible to use boulder county open data to create open street map features? If so I intend to process the shapefiles with GDAL and gpsbabel to create gpx tracks to add missing ways to open street maps.</p>
<p><a href="https://www.bouldercounty.org/government/open-data/terms-of-use/">https://www.bouldercounty.org/government/open-data/terms-of-use/</a></p>
<blockquote>
<p>License</p>
<p>cc4 licenseBoulder County grants you a world-wide, royalty-free, non-exclusive license to use, modify, and distribute the datasets in all current and future media and formats for any lawful purpose. The Boulder County Open Data Catalog provides open data licensed under the Creative Commons Attribution 4.0 International License (CC0 4.0) unless noted otherwise. Attribution</p>
<p>You are free to copy, distribute, transmit and adapt the data without attribution. When using or citing the data sets provided herein, you should not imply endorsement by Boulder County.</p>
</blockquote>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-license" rel="tag" title="see questions tagged &#39;license&#39;">license</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Apr '18, 14:20</strong></p>
<img src="https://secure.gravatar.com/avatar/e1ff39b44a638e18af0ea0929a12aa21?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tsteven4&#39;s gravatar image" />
<p><span>tsteven4</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tsteven4 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-63170" class="comments-container">
&#10;</div>
<div id="comment-tools-63170" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63170-form-container" class="comment-form-container">
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

<span id="63184"></span>

<div id="answer-container-63184" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63184-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63184-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-63184-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The web site you are quoting contradicts itself by claiming that it was using the "Creative Commons <strong>Attribution</strong> International License" (and showing the matching logo for that license, shorthand "CC-BY") and then using the substantially different term "CC0" in the text and writing "You are free to ... without attribution". CC-BY is not automatically OSM compatible and requires a special attribution waiver, whereas CC0 is compatible.</p>
<p>Assuming that the latter (CC0 - "without attribution") is correct, then you can us their data for OSM without legal issues. As long as you simply use their data to help you in your manual mapping, it's enough to specify a proper source with your changeset (Boulder don't require that but OSM recommends it). If you, however, are thinking about <em>importing</em> data outright (e.g. by loading the shape file in JOSM and converting shape file objects to OSM and uploading them), then a prior discussion on the imports mailing list would be required by our import guidelines.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Apr '18, 21:05</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-63184" class="comments-container">
&#10;</div>
<div id="comment-tools-63184" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63184-form-container" class="comment-form-container">
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


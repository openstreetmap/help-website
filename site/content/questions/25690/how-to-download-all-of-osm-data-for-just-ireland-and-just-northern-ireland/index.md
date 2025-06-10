+++
type = "question"
title = "How to download all of OSM data for just ireland and just northern Ireland?"
description = '''Hello all, I have downloaded data for Great Britain and Ireland from Geofabrik. However, Ireland data includes northern Ireland. How do I get those two seperately? Cloudmade has the data seperated but it looks to be different (less data there, i.e. rivers, residential streets, etc...) even thought t...'''
date = "2013-08-23T16:12:00Z"
lastmod = "2013-08-23T17:10:00Z"
weight = 25690
keywords = [ "download", "uk", "geofabrik", "ireland", "cloudmade" ]
aliases = [ "/questions/25690" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to download all of OSM data for just ireland and just northern Ireland?](/questions/25690/how-to-download-all-of-osm-data-for-just-ireland-and-just-northern-ireland)

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
<span id="post-25690-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25690-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-25690-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello all, I have downloaded data for Great Britain and Ireland from Geofabrik. However, Ireland data includes northern Ireland. How do I get those two seperately? Cloudmade has the data seperated but it looks to be different (less data there, i.e. rivers, residential streets, etc...) even thought the data I downloaded from Geofabrik is much older. So, I really not sure I can trust that data since I been downloading from Geofabrik all this time.</p>
<p>I realize I can do some stuff programatically to look for data within a boundary to seperate ireland and northern ireland. However, I am not setup that way right now. I am setup to process data one country at a time. Northern Ireland should really be a part of UK, shouldn't it?</p>
<p>Any help would be appreciated.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-download" rel="tag" title="see questions tagged &#39;download&#39;">download</span> <span class="post-tag tag-link-uk" rel="tag" title="see questions tagged &#39;uk&#39;">uk</span> <span class="post-tag tag-link-geofabrik" rel="tag" title="see questions tagged &#39;geofabrik&#39;">geofabrik</span> <span class="post-tag tag-link-ireland" rel="tag" title="see questions tagged &#39;ireland&#39;">ireland</span> <span class="post-tag tag-link-cloudmade" rel="tag" title="see questions tagged &#39;cloudmade&#39;">cloudmade</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Aug '13, 16:12</strong></p>
<img src="https://secure.gravatar.com/avatar/343237842fce1f7a82f69ebf7a92f6b6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kcjailbirds&#39;s gravatar image" />
<p><span>kcjailbirds</span><br />
<span class="score" title="141 reputation points">141</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kcjailbirds has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-25690" class="comments-container">
&#10;</div>
<div id="comment-tools-25690" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25690-form-container" class="comment-form-container">
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

<span id="25692"></span>

<div id="answer-container-25692" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-25692-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25692-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-25692-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Geofabrik extracts tend to go by geography rather than politics (hence various overseas territories having their own files, or things like "South Africa and Lesotho"). It's useful to some and less useful to others. If you can't be bothered to set up your own splitting (which would require one of the programs osmosis or osmconvert, as well as two country polygons to use for cutting - you'd want to make them overlap a bit in along the border) then you might want to try the <a href="http://extract.bbbike.org/">bbbike extract service</a> where you can doodle an area onto the map and then have exactly that cut out for you.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Aug '13, 16:46</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-25692" class="comments-container">
<span id="25695"></span>
<div id="comment-25695" class="comment">
<div id="post-25695-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you Frederik. I was hoping I did not have to do that but seems like I must!</p>
</div>
<div id="comment-25695-info" class="comment-info">
<span class="comment-age">(23 Aug '13, 17:10)</span> <span class="comment-user userinfo">kcjailbirds</span>
</div>
</div>
</div>
<div id="comment-tools-25692" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25692-form-container" class="comment-form-container">
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


+++
type = "question"
title = "Can I download only a subset of data in JOSM?"
description = '''Is there any way to filter the data before it is downloaded into JOSM? Suppose, for example, I wanted to see all the power lines in the state of Vermont. I can&#x27;t download the entire state and then use the filters in JOSM because it&#x27;s too much data to work with. But if I could download only the ways ...'''
date = "2010-10-09T16:09:00Z"
lastmod = "2019-11-06T10:15:00Z"
weight = 1087
keywords = [ "josm", "filtering" ]
aliases = [ "/questions/1087" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Can I download only a subset of data in JOSM?](/questions/1087/can-i-download-only-a-subset-of-data-in-josm)

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
<span id="post-1087-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1087-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-1087-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
2
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is there any way to filter the data <em>before</em> it is downloaded into JOSM? Suppose, for example, I wanted to see all the power lines in the state of Vermont. I can't download the entire state and then use the filters in JOSM because it's too much data to work with. But if I could download only the ways with the tag <code>"power=line"</code>, the amount of data would be very much smaller and they could easily be worked with. But I don't see any way to do this. Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-filtering" rel="tag" title="see questions tagged &#39;filtering&#39;">filtering</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Oct '10, 16:09</strong></p>
<img src="https://secure.gravatar.com/avatar/a5ad728cbc8ae89b774c8c61fbeb20f9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="OceanVortex&#39;s gravatar image" />
<p><span>OceanVortex</span><br />
<span class="score" title="156 reputation points">156</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="OceanVortex has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-1087" class="comments-container">
&#10;</div>
<div id="comment-tools-1087" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1087-form-container" class="comment-form-container">
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

<span id="1097"></span>

<div id="answer-container-1097" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1097-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1097-score" class="post-score" title="current number of votes">
9
</div>
<span id="post-1097-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Be very careful when working with filtered data in an offline editor because you will not be able to see whether other objects share some of the data you have downloaded. Here are some of the problems that might arise:</p>
<ul>
<li>You have downloaded only power lines. You move a power line according to an aerial image. You accidentally move a power pole into a house, or a river, or a road, which you hadn't downloaded and so you didn't notice.</li>
<li>You have downloaded only railways. You simplify a railway line by deleting some of the nodes, unaware that one of the nodes is indeed a level crossing shared by a footway which you haven't downloaded. Your upload will fail.</li>
<li>You have downloaded only roads. You move one highway's nodes about to improve the geometry, not seeing that one node was actually also used by an administrative boundary running across the road; your upload will work but you have created an ugly dent in the boundary.</li>
</ul>
<p>At the very least, when using filtered data, have a fully rendered OSM map displayed in the background so you are alerted to potential trouble spots.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Oct '10, 18:36</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Oct '10, 08:46</strong> </span></p>
</div>
</div>
<div id="comments-container-1097" class="comments-container">
<span id="1100"></span>
<div id="comment-1100" class="comment">
<div id="post-1100-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks, these are very good caveats to be aware of.</p>
</div>
<div id="comment-1100-info" class="comment-info">
<span class="comment-age">(09 Oct '10, 20:19)</span> <span class="comment-user userinfo">OceanVortex</span>
</div>
</div>
<span id="9699"></span>
<div id="comment-9699" class="comment">
<div id="post-9699-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Does JOSM provide any level of protection against some of these potential problems? If not, maybe something could be implemented.</p>
</div>
<div id="comment-9699-info" class="comment-info">
<span class="comment-age">(30 Dec '11, 10:02)</span> <span class="comment-user userinfo">Kozuch</span>
</div>
</div>
</div>
<div id="comment-tools-1097" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1097-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="1093"></span>

<div id="answer-container-1093" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1093-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1093-score" class="post-score" title="current number of votes">
8
</div>
<span id="post-1093-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Take a look at <a href="http://wiki.openstreetmap.org/wiki/Xapi">XApi</a>. It is an eXtended API that allows you to filter the downloads. You can open the url in josm by selecting File-&gt;Open Location...</p>
<p>You can for example use <a href="http://www.informationfreeway.org/api/0.6/way%5Bbbox=11.54,48.14,11.543,48.145%5D%5Bpower=line%5D">http://www.informationfreeway.org/api/0.6/way[bbox=11.54,48.14,11.543,48.145][power=line]</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Oct '10, 17:54</strong></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gnonthgol has 57 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-1093" class="comments-container">
<span id="1101"></span>
<div id="comment-1101" class="comment">
<div id="post-1101-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Thanks, that's exactly what I needed.</p>
</div>
<div id="comment-1101-info" class="comment-info">
<span class="comment-age">(09 Oct '10, 20:21)</span> <span class="comment-user userinfo">OceanVortex</span>
</div>
</div>
<span id="71477"></span>
<div id="comment-71477" class="comment">
<div id="post-71477-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Is XApi still the recommended solution to download only a subset of data from OSM and avoid being overwhelmed, or is there a better way?</p>
</div>
<div id="comment-71477-info" class="comment-info">
<span class="comment-age">(05 Nov '19, 23:44)</span> <span class="comment-user userinfo">Shohreh</span>
</div>
</div>
<span id="71478"></span>
<div id="comment-71478" class="comment">
<div id="post-71478-score" class="comment-score">
2
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/3711/shohreh">@Shohreh</a>: You can export data from Overpass Turbo into JOSM. JOSM also has methods to download from Overpass itself, as well as Sophox. As fas as I can see XAPI is no longer supported by default. I assume Overpass is the preferred method nowadays.</p>
</div>
<div id="comment-71478-info" class="comment-info">
<span class="comment-age">(06 Nov '19, 04:12)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="71479"></span>
<div id="comment-71479" class="comment">
<div id="post-71479-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you. I'll check if there are any traps/drawbacks when downloading just a subset through Overpass Turbo.</p>
</div>
<div id="comment-71479-info" class="comment-info">
<span class="comment-age">(06 Nov '19, 10:15)</span> <span class="comment-user userinfo">Shohreh</span>
</div>
</div>
</div>
<div id="comment-tools-1093" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1093-form-container" class="comment-form-container">
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


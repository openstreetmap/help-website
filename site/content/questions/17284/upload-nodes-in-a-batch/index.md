+++
type = "question"
title = "upload nodes in a batch"
description = '''I have a list of points with Lat, Lon, Names, and other tags. There are over 100 points, so I do not wish to create them one at a time. How can I upload them as a batch? Thanks!'''
date = "2012-10-30T02:21:00Z"
lastmod = "2012-10-30T09:32:00Z"
weight = 17284
keywords = [ "node", "upload" ]
aliases = [ "/questions/17284" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [upload nodes in a batch](/questions/17284/upload-nodes-in-a-batch)

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
<span id="post-17284-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17284-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-17284-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a list of points with Lat, Lon, Names, and other tags. There are over 100 points, so I do not wish to create them one at a time. How can I upload them as a batch?</p>
<p>Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-node" rel="tag" title="see questions tagged &#39;node&#39;">node</span> <span class="post-tag tag-link-upload" rel="tag" title="see questions tagged &#39;upload&#39;">upload</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Oct '12, 02:21</strong></p>
<img src="https://secure.gravatar.com/avatar/37ba751d7577501fae22639990776ae3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JMcA&#39;s gravatar image" />
<p><span>JMcA</span><br />
<span class="score" title="41 reputation points">41</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JMcA has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-17284" class="comments-container">
<span id="17285"></span>
<div id="comment-17285" class="comment">
<div id="post-17285-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Have you verified that there won't be any duplicated entries after uploading?</p>
</div>
<div id="comment-17285-info" class="comment-info">
<span class="comment-age">(30 Oct '12, 06:36)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-17284" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17284-form-container" class="comment-form-container">
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

<span id="17288"></span>

<div id="answer-container-17288" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17288-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17288-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-17288-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are various programs that would convert a list of nodes into an .osm file that you could then upload with an editor like JOSM. (Involving an editor has the advantage of giving you a visual check on whether the data you're planning to upload matches - good - or duplicates - bad - what's already there.) Here's a very simple one that requires some Perl knowledge to make the necessary modifications:</p>
<p><a href="http://textual.ru/vybory2011/osmres/csv2osm.pl">http://textual.ru/vybory2011/osmres/csv2osm.pl</a></p>
<p>However, please note that data imports are not universally welcome in OpenStreetMap, and usually require prior discussion on the "imports" mailing list. I guess if the number of points you have is small and you have manually collected them e.g. was waypoints in your GPS or so, then what you're planning to do is not much different from a manual edit, but if the list of points is in any way auto-generated or converted from another data source then it is definitely an import and you'll have to check with the community before you go ahead.</p>
<p>The reason for this requirement is mainly that there have been lots of bad imports in the past, where people - always with the best intention - imported duplicate or useless data, data with wrongly converted coordinates, unnecessary or badly converted third-party tags and other stuff, and due to the "mass data processing" nature that imports often have, the impact of a mistake in an import procedure can be much greater than the impact of a mistake made by a human mapper!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Oct '12, 09:21</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-17288" class="comments-container">
&#10;</div>
<div id="comment-tools-17288" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17288-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="17290"></span>

<div id="answer-container-17290" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17290-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17290-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-17290-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Please read the <a href="http://wiki.openstreetmap.org/wiki/Import/Guidelines">import guidelines</a> before proceeding any further, since it sounds like your points are comming from an external source and there are certain preparations to do in that case (main 3 beeing: double-check the licence, announce your import to the local community, and QA-check the actual data).</p>
<p>Once that's done (or if your data doesn't qualify as an "import"), it really depends what format your data is in to begin with. Assuming your data is a csv and you have some basic scripting skills, the simplest way is probably to transform your csv into an <a href="http://wiki.openstreetmap.org/wiki/Osm_format">osm xml</a> file, load that file in JOSM, QA-check it, and upload. If those assumtions wetre wrong, you need to give us more details.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Oct '12, 09:32</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-17290" class="comments-container">
&#10;</div>
<div id="comment-tools-17290" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17290-form-container" class="comment-form-container">
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


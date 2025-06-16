+++
type = "question"
title = "JOSM - move POI data to building outlines"
description = '''Is there an easy way to move POI&#x27;s into the building outlines with JOSM? The reason: in my area are a lot of POI&#x27;s and Address Nodes that are placed in the middle of the building. I would like to change that (with reasonable low effort...) according to the policy and to make editing more clear. (Not...'''
date = "2016-06-27T14:18:00Z"
lastmod = "2017-09-30T05:21:00Z"
weight = 50483
keywords = [ "building", "josm", "poi" ]
aliases = [ "/questions/50483" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [JOSM - move POI data to building outlines](/questions/50483/josm-move-poi-data-to-building-outlines)

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
<span id="post-50483-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50483-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-50483-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is there an easy way to move POI's into the building outlines with JOSM?</p>
<p>The reason: in my area are a lot of POI's and Address Nodes that are placed in the middle of the building. I would like to change that (with reasonable low effort...) according to the policy and to make editing more clear. (Not so many points)</p>
<p>Discussed here for POtlach:</p>
<p><a href="/questions/4260/how-can-i-copy-all-metadata-from-a-poi-into-an-area-in-potlatch-2">https://help.openstreetmap.org/questions/4260/how-can-i-copy-all-metadata-from-a-poi-into-an-area-in-potlatch-2</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-building" rel="tag" title="see questions tagged &#39;building&#39;">building</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-poi" rel="tag" title="see questions tagged &#39;poi&#39;">poi</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Jun '16, 14:18</strong></p>
<img src="https://secure.gravatar.com/avatar/35277bd93ca2ca9ac929093e76bd7d26?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="freakyuser&#39;s gravatar image" />
<p><span>freakyuser</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="freakyuser has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-50483" class="comments-container">
<span id="50484"></span>
<div id="comment-50484" class="comment">
<div id="post-50484-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Don't move tags from nodes to the building outline unless you are sure that these tags apply to the whole building (or at least most part of the building). This often requires local knowledge.</p>
</div>
<div id="comment-50484-info" class="comment-info">
<span class="comment-age">(27 Jun '16, 14:43)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="50485"></span>
<div id="comment-50485" class="comment">
<div id="post-50485-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Yes, there are several ways.</p>
<p>I'd like to know what policy you are referring to. I don't know any saying "Map buildings, not nodes". Both ways to map are correct.<br />
A link to the region you refer to would also be helpful.</p>
</div>
<div id="comment-50485-info" class="comment-info">
<span class="comment-age">(27 Jun '16, 14:45)</span> <span class="comment-user userinfo">malenki</span>
</div>
</div>
<span id="50486"></span>
<div id="comment-50486" class="comment">
<div id="post-50486-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I live country sideish, so it's pretty easy to have a ''general knowledge'' of the area.</p>
<p>Well, that's how I interpret the One feature, one element ''rule'' https://wiki.openstreetmap.org/wiki/One_feature,_one_OSM_element</p>
<p>A city, where most addresses and POI's are in Nodes instead of the corresponding buildings is Furtwangen: <a href="https://www.openstreetmap.org/node/240071322#map=16/48.0489/8.2035">https://www.openstreetmap.org/node/240071322#map=16/48.0489/8.2035</a></p>
</div>
<div id="comment-50486-info" class="comment-info">
<span class="comment-age">(27 Jun '16, 14:56)</span> <span class="comment-user userinfo">freakyuser</span>
</div>
</div>
<span id="50490"></span>
<div id="comment-50490" class="comment">
<div id="post-50490-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>"One feature, one element" still holds when tagging the POI as a single node inside a building as long as the POI tags aren't present on both the POI and the building.</p>
</div>
<div id="comment-50490-info" class="comment-info">
<span class="comment-age">(27 Jun '16, 16:47)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="50491"></span>
<div id="comment-50491" class="comment">
<div id="post-50491-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the clarification with the POI's</p>
<p>But I still think, that at least addresses belong into outlines instead of nodes. Especially if the outlines are already drawn.</p>
</div>
<div id="comment-50491-info" class="comment-info">
<span class="comment-age">(27 Jun '16, 18:49)</span> <span class="comment-user userinfo">freakyuser</span>
</div>
</div>
<span id="59810"></span>
<div id="comment-59810" class="comment not_top_scorer">
<div id="post-59810-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/12474/freakyuser">@freakyuser</a>: if the building has an entrance (main entrance) mapped, I'd say it is ok if that entrance is mapped with an address (given that some big buildings may have multiple numbers and it may be hard to separate them. But for cottages, yes they probably should have the address in the outline.</p>
</div>
<div id="comment-59810-info" class="comment-info">
<span class="comment-age">(23 Sep '17, 22:49)</span> <span class="comment-user userinfo">tomato42</span>
</div>
</div>
</div>
<div id="comment-tools-50483" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-50483-form-container" class="comment-form-container">
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

<span id="50492"></span>

<div id="answer-container-50492" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-50492-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50492-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-50492-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="freakyuser has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In JOSM, select both the point and the polygon then under "More Tools" choose "Replace Geometry". If there is a conflict on the tagging, (e.g. the polygon already contains a the same tag) you will get a dialog box asking you which value to choose.</p>
<p>As mentioned in the comments on the original question, only do this if all the tags on the point are appropriate for the polygon. If not all tags are appropriate, then individual copy and paste of the tags is probably your best course of action.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Jun '16, 19:40</strong></p>
<img src="https://secure.gravatar.com/avatar/f60af53a4eba0c21f25c22674fb4a8cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="n76&#39;s gravatar image" />
<p><span>n76</span><br />
<span class="score" title="10839 reputation points"><span>10.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="82 badges"><span class="silver">●</span><span class="badgecount">82</span></span><span title="172 badges"><span class="bronze">●</span><span class="badgecount">172</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="n76 has 48 accepted answers">17%</span> </br></p>
</div>
</div>
<div id="comments-container-50492" class="comments-container">
<span id="50493"></span>
<div id="comment-50493" class="comment">
<div id="post-50493-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks! That's what I was looking for.</p>
</div>
<div id="comment-50493-info" class="comment-info">
<span class="comment-age">(27 Jun '16, 20:12)</span> <span class="comment-user userinfo">freakyuser</span>
</div>
</div>
<span id="50494"></span>
<div id="comment-50494" class="comment">
<div id="post-50494-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Note that the "Replace Geometry" menu item is part of the <a href="https://josm.openstreetmap.de/wiki/Help/Plugin/UtilsPlugin2">UtilsPlugin2</a>.</p>
</div>
<div id="comment-50494-info" class="comment-info">
<span class="comment-age">(27 Jun '16, 20:30)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
<span id="50495"></span>
<div id="comment-50495" class="comment">
<div id="post-50495-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Good point, I installed the UtilsPlugin extensions so long ago that I'm not really sure which functionality is associated with each plug-in.</p>
</div>
<div id="comment-50495-info" class="comment-info">
<span class="comment-age">(27 Jun '16, 20:32)</span> <span class="comment-user userinfo">n76</span>
</div>
</div>
<span id="50497"></span>
<div id="comment-50497" class="comment">
<div id="post-50497-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>"individual copy and paste of the tags" = ctrl+c to copy and ctrl+shift+v to paste</p>
</div>
<div id="comment-50497-info" class="comment-info">
<span class="comment-age">(27 Jun '16, 23:36)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="59891"></span>
<div id="comment-59891" class="comment">
<div id="post-59891-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This is news to me too! a good thing to know, I'd always done copy and ctrl+shift+v.</p>
</div>
<div id="comment-59891-info" class="comment-info">
<span class="comment-age">(30 Sep '17, 05:21)</span> <span class="comment-user userinfo">keithonearth</span>
</div>
</div>
</div>
<div id="comment-tools-50492" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50492-form-container" class="comment-form-container">
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


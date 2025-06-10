+++
type = "question"
title = "Should farmland details be in OSM?"
description = '''Is farmland details (such as the company owner and field id etc.) relevant to OSM.  I mean, I want to develop an app which will use this data. I thought that instead of store this data only for me, it will shared to the community. If it makes sense, which field I can use to store this data. The data...'''
date = "2018-04-08T17:11:00Z"
lastmod = "2018-04-08T19:37:00Z"
weight = 62947
keywords = [ "farmland", "tagging", "ownership" ]
aliases = [ "/questions/62947" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Should farmland details be in OSM?](/questions/62947/should-farmland-details-be-in-osm)

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
<span id="post-62947-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62947-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-62947-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is farmland details (such as the company owner and field id etc.) relevant to OSM.</p>
<p>I mean, I want to develop an app which will use this data. I thought that instead of store this data only for me, it will shared to the community. If it makes sense, which field I can use to store this data.</p>
<p>The data will inserted by the owner itself, of course.</p>
<p>Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-farmland" rel="tag" title="see questions tagged &#39;farmland&#39;">farmland</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-ownership" rel="tag" title="see questions tagged &#39;ownership&#39;">ownership</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Apr '18, 17:11</strong></p>
<img src="https://secure.gravatar.com/avatar/3d721f4c46282afc254f3ea0cd05df30?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="moshfeu&#39;s gravatar image" />
<p><span>moshfeu</span><br />
<span class="score" title="46 reputation points">46</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="moshfeu has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Apr '18, 19:44</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/f882e7865ffe23339fbaa71c9f576065?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="FredrikLindseth&#39;s gravatar image" />
<p><span>FredrikLindseth</span><br />
<span class="score" title="815 reputation points">815</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="35 badges"><span class="bronze">●</span><span class="badgecount">35</span></span></p>
</div>
</div>
<div id="comments-container-62947" class="comments-container">
&#10;</div>
<div id="comment-tools-62947" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62947-form-container" class="comment-form-container">
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

<span id="62953"></span>

<div id="answer-container-62953" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-62953-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62953-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-62953-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'm sure there is a place for this if you add the data in a "good" way. You should try to create a conversion table for the data you have into OSM-tags.</p>
<p>I.e. if you look at <a href="https://wiki.openstreetmap.org/wiki/Tag:landuse=farmland">https://wiki.openstreetmap.org/wiki/Tag:landuse=farmland</a> there are some suggested tags that can be used</p>
<ul>
<li>name=* (if the field has a NAME, not the operator, or the produce or the id, only if the field has a real name)</li>
<li>crop=*</li>
<li>produce=*</li>
</ul>
<p>The "company owner" can be inputted as operator=<em>, the field id can be some form of ref=</em> (see <a href="https://wiki.openstreetmap.org/wiki/Key:ref">https://wiki.openstreetmap.org/wiki/Key:ref</a> or possibly create a unique ref for this data)</p>
<p>You could always ask on the email lists <a href="https://lists.openstreetmap.org/listinfo/talk">talk</a> or <a href="https://lists.openstreetmap.org/listinfo/tagging">tagging</a> to see if your final tagging plan makes sense to the community.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Apr '18, 19:37</strong></p>
<img src="https://secure.gravatar.com/avatar/f882e7865ffe23339fbaa71c9f576065?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="FredrikLindseth&#39;s gravatar image" />
<p><span>FredrikLindseth</span><br />
<span class="score" title="815 reputation points">815</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="35 badges"><span class="bronze">●</span><span class="badgecount">35</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="FredrikLindseth has 2 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-62953" class="comments-container">
&#10;</div>
<div id="comment-tools-62953" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62953-form-container" class="comment-form-container">
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


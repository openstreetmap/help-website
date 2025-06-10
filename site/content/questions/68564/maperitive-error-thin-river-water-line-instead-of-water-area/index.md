+++
type = "question"
title = "maperitive: error thin river water line instead of water area"
description = '''When I open my OSM file exported form Openstreetmaps in Maperitive - in one part of the river there is only thin water line instead of water area. How can I fix this? Thanks Screenshot: https://ibb.co/wcWcZPC OSM file: https://we.tl/t-mvYlwcnSIY'''
date = "2019-03-31T17:23:00Z"
lastmod = "2019-04-03T07:49:00Z"
weight = 68564
keywords = [ "water", "maperitive" ]
aliases = [ "/questions/68564" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [maperitive: error thin river water line instead of water area](/questions/68564/maperitive-error-thin-river-water-line-instead-of-water-area)

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
<span id="post-68564-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68564-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-68564-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>When I open my OSM file exported form Openstreetmaps in Maperitive - in one part of the river there is only thin water line instead of water area. How can I fix this? Thanks</p>
<p>Screenshot: <a href="https://ibb.co/wcWcZPC">https://ibb.co/wcWcZPC</a></p>
<p>OSM file: <a href="https://we.tl/t-mvYlwcnSIY">https://we.tl/t-mvYlwcnSIY</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-water" rel="tag" title="see questions tagged &#39;water&#39;">water</span> <span class="post-tag tag-link-maperitive" rel="tag" title="see questions tagged &#39;maperitive&#39;">maperitive</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Mar '19, 17:23</strong></p>
<img src="https://secure.gravatar.com/avatar/2de161edcaefe887c7dc035ffd43fec9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="thierrybb&#39;s gravatar image" />
<p><span>thierrybb</span><br />
<span class="score" title="41 reputation points">41</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="thierrybb has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-68564" class="comments-container">
&#10;</div>
<div id="comment-tools-68564" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68564-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="68619"></span>

<div id="answer-container-68619" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68619-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68619-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-68619-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is happening because the exported OSM data file you have doesn't contain all of the necessary objects to display the river area.</p>
<p>The river area (waterway=riverbank) is mapped using multipolygon relations, with the missing section in question being <a href="https://www.openstreetmap.org/relation/2740094">a relation</a> containing five separate ways. Since at least one of those ways falls outside of the exported area, the multipolygon area is no longer complete and the area can't be properly displayed by Maperitive. The thin line that is displayed is the separate waterway=river way representing the main flow of the river.</p>
<p>To get around this, you could export a larger area than you need, which would hopefully pick up all of the other objects that are relevant to the ones that fall inside your area of interest. Depending on the tools you use, you may also be able to simply download the additional objects you need and add them to your existing OSM file.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Apr '19, 23:00</strong></p>
<img src="https://secure.gravatar.com/avatar/087bb38ba920baadf1df9dfc473208ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alester&#39;s gravatar image" />
<p><span>alester</span><br />
<span class="score" title="6631 reputation points"><span>6.6k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alester has 37 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-68619" class="comments-container">
&#10;</div>
<div id="comment-tools-68619" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68619-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="68592"></span>

<div id="answer-container-68592" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68592-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68592-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68592-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>A link to openstreetmap with coordinates (Like this one <a href="https://www.openstreetmap.org/#map=18/52.33018/-0.17340">https://www.openstreetmap.org/#map=18/52.33018/-0.17340</a> ) would be useful. The screenshot looks like the river bank polygon is either unmapped or is broken. To fix this you will need to learn how to map river bank polygons. How to do this is all explained in the wiki, it isn't too hard to do, if good aerial is available, but will take some time for long sections of waterway. If you supply a link and the fault is just a broken polygon i'm sure someone will fix it.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Apr '19, 21:41</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Apr '19, 21:50</strong> </span></p>
</div>
</div>
<div id="comments-container-68592" class="comments-container">
&#10;</div>
<div id="comment-tools-68592" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68592-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="68598"></span>

<div id="answer-container-68598" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68598-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68598-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68598-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi, the polygon for the river bank had the tags changed to include water=river, waterway=river, (this introduced a flow direction to the river bank). I've removed these tags and added the tag waterway=riverbank. It should be OK now.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Apr '19, 07:31</strong></p>
<img src="https://secure.gravatar.com/avatar/e3283a6b5f83e16214ec39a1478f64f0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BCNorwich&#39;s gravatar image" />
<p><span>BCNorwich</span><br />
<span class="score" title="6299 reputation points"><span>6.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="44 badges"><span class="silver">●</span><span class="badgecount">44</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BCNorwich has 44 accepted answers">20%</span></p>
</div>
</div>
<div id="comments-container-68598" class="comments-container">
<span id="68599"></span>
<div id="comment-68599" class="comment">
<div id="post-68599-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Forgot to mention this is the way <a href="https://www.openstreetmap.org/way/515061721">https://www.openstreetmap.org/way/515061721</a></p>
</div>
<div id="comment-68599-info" class="comment-info">
<span class="comment-age">(02 Apr '19, 07:33)</span> <span class="comment-user userinfo">BCNorwich</span>
</div>
</div>
<span id="68615"></span>
<div id="comment-68615" class="comment">
<div id="post-68615-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>That's the Thames, but the area in question appears to be in the Bratislava area on the Danube/Donau/Dunaj.</p>
</div>
<div id="comment-68615-info" class="comment-info">
<span class="comment-age">(02 Apr '19, 16:56)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="68620"></span>
<div id="comment-68620" class="comment">
<div id="post-68620-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/2925/bcnorwich">@BCNorwich</a>, while you are here could you please comment the change here <a href="https://osm.org/go/0EENoe1I--?way=515061721.">https://osm.org/go/0EENoe1I--?way=515061721.</a> Apart from the small rendering fail, you have used the bezier=no tag. Of cause then you could equally use bezier=yes as well. Does this mean that we have in OSM (WIKI) a new data type - smooth/polynomial line?</p>
</div>
<div id="comment-68620-info" class="comment-info">
<span class="comment-age">(03 Apr '19, 07:09)</span> <span class="comment-user userinfo">sanser</span>
</div>
</div>
<span id="68621"></span>
<div id="comment-68621" class="comment">
<div id="post-68621-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi sanser, alester, First my apologies for commenting to the wrong river, I was editing problems with one river while reading about problems on a different river, my post crossed over. I did comment on the Thames river edit here :-<a href="https://www.openstreetmap.org/changeset/68753453">https://www.openstreetmap.org/changeset/68753453</a></p>
</div>
<div id="comment-68621-info" class="comment-info">
<span class="comment-age">(03 Apr '19, 07:49)</span> <span class="comment-user userinfo">BCNorwich</span>
</div>
</div>
</div>
<div id="comment-tools-68598" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68598-form-container" class="comment-form-container">
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


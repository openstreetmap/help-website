+++
type = "question"
title = "Reverse geocoding yields wrong address"
description = '''I have a similar problem as before:  Here is a address: 195, Caroni Savannah Rd, San Fernando, Trinidad and Tobago &quot;San Fernando&quot; in this case, (and it appears all over Trinidad) is not correct. It simply not supposed to be there. What can I do to make these changes? If not, can someone do it? Pleas...'''
date = "2012-06-20T02:12:00Z"
lastmod = "2012-06-20T11:53:00Z"
weight = 13644
keywords = [ "corrections", "errors" ]
aliases = [ "/questions/13644" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Reverse geocoding yields wrong address](/questions/13644/reverse-geocoding-yields-wrong-address)

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
<span id="post-13644-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13644-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-13644-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a similar problem as before:</p>
<p>Here is a address:</p>
<p>195, Caroni Savannah Rd, San Fernando, Trinidad and Tobago</p>
<p>"San Fernando" in this case, (and it appears all over Trinidad) is not correct. It simply not supposed to be there.</p>
<p>What can I do to make these changes?</p>
<p>If not, can someone do it?</p>
<p>Please advise.</p>
<p>Jai</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-corrections" rel="tag" title="see questions tagged &#39;corrections&#39;">corrections</span> <span class="post-tag tag-link-errors" rel="tag" title="see questions tagged &#39;errors&#39;">errors</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Jun '12, 02:12</strong></p>
<img src="https://secure.gravatar.com/avatar/3ae310b7b9c595a1f01a5fea0dfa1069?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dejaiman&#39;s gravatar image" />
<p><span>dejaiman</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dejaiman has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-13644" class="comments-container">
&#10;</div>
<div id="comment-tools-13644" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13644-form-container" class="comment-form-container">
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

<span id="13647"></span>

<div id="answer-container-13647" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13647-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13647-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-13647-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can use <a href="http://wiki.openstreetmap.org/wiki/Nominatim">Nominatim</a> to <a href="http://nominatim.openstreetmap.org/search.php?q=195%2C+Caroni+Savannah+Rd%2C+Trinidad+and+Tobago&amp;viewbox=-61.46%2C10.58%2C-61.37%2C10.53">search</a> for this address. Then, click on the little grey <a href="http://nominatim.openstreetmap.org/details.php?place_id=15918661">details</a> link of the first search result. This is Nominatim's view of this object, you can clearly see how the address is build. It also includes San Fernando as a <a href="http://www.openstreetmap.org/browse/node/1110779940">node</a> tagged with <em>place=city</em>.</p>
<p>San Fernando seems to be the next closest city Nominatim can find, so it assumes that Caroni Savannah Rd belongs to San Fernando. It cannot know better because there is no <a href="http://wiki.openstreetmap.org/wiki/Tag:boundary%3Dadministrative">boundary</a> relation for San Fernando and the other cities. You have to add such a relation with a correct <a href="http://wiki.openstreetmap.org/wiki/Key:admin_level#admin_level">admin_level</a> tag (something between admin_level=7 and admin_level=10, the wiki page will tell you) so that Nominatim can know which place belongs to which city.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Jun '12, 05:42</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Jun '12, 11:53</strong> </span></p>
</div>
</div>
<div id="comments-container-13647" class="comments-container">
<span id="13655"></span>
<div id="comment-13655" class="comment">
<div id="post-13655-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>How and where do you change the admin levels?</p>
<p>Jai</p>
</div>
<div id="comment-13655-info" class="comment-info">
<span class="comment-age">(20 Jun '12, 11:10)</span> <span class="comment-user userinfo">dejaiman</span>
</div>
</div>
<span id="13657"></span>
<div id="comment-13657" class="comment">
<div id="post-13657-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>First you have to find a compatible source for the boundary and then add it to OSM by creating a <a href="http://wiki.openstreetmap.org/wiki/Relation:boundary">boundary relation</a> using your <a href="http://wiki.openstreetmap.org/wiki/Editor#Top_two">favourite editor</a>.</p>
<p>This isn't an easy task for a beginner, maybe someone will help you. You can try to contact local mappers via the <a href="http://lists.openstreetmap.org/listinfo">mailing lists</a> for example.</p>
</div>
<div id="comment-13657-info" class="comment-info">
<span class="comment-age">(20 Jun '12, 11:53)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-13647" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13647-form-container" class="comment-form-container">
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


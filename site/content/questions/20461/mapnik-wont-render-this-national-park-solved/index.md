+++
type = "question"
title = "[closed] mapnik won&#x27;t render this national park [solved]"
description = '''Can anyone explain why this NP still isn&#x27;t rendered after one month? https://www.openstreetmap.org/browse/relation/2750441 Other Np&#x27;s with the same tags are rendered fine but this one doesn&#x27;t.'''
date = "2013-03-03T13:38:00Z"
lastmod = "2013-03-06T08:23:00Z"
weight = 20461
keywords = [ "national_park", "boundary", "relation", "mapnik" ]
aliases = [ "/questions/20461" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] mapnik won't render this national park \[solved\]](/questions/20461/mapnik-wont-render-this-national-park-solved)

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
<span id="post-20461-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20461-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-20461-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Can anyone explain why this NP still isn't rendered after one month? <a href="https://www.openstreetmap.org/browse/relation/2750441">https://www.openstreetmap.org/browse/relation/2750441</a></p>
<p>Other Np's with the same tags are rendered fine but this one doesn't.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-national_park" rel="tag" title="see questions tagged &#39;national_park&#39;">national_park</span> <span class="post-tag tag-link-boundary" rel="tag" title="see questions tagged &#39;boundary&#39;">boundary</span> <span class="post-tag tag-link-relation" rel="tag" title="see questions tagged &#39;relation&#39;">relation</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Mar '13, 13:38</strong></p>
<img src="https://secure.gravatar.com/avatar/0f5ffc3756c4662b9dfad80b7665ac6c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ligfietser&#39;s gravatar image" />
<p><span>ligfietser</span><br />
<span class="score" title="2894 reputation points"><span>2.9k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="27 badges"><span class="silver">●</span><span class="badgecount">27</span></span><span title="57 badges"><span class="bronze">●</span><span class="badgecount">57</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ligfietser has 8 accepted answers">11%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>06 Mar '13, 08:26</strong> </span></p>
</div>
</div>
<div id="comments-container-20461" class="comments-container">
&#10;</div>
<div id="comment-tools-20461" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20461-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "The question is answered, right answer was accepted" by ligfietser 06 Mar '13, 08:26

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="20511"></span>

<div id="answer-container-20511" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-20511-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20511-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-20511-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If (as sugested by a comment to scai's answer) this was a database problem, it could have been related to the rendering problem that occured after the node numbers reached the signed/unsigned 32 bit boundary. The nodes in the ways making up the boundary were created just after this occured (10 Feb 2013) so their tiles may have been affected in the same way that some of mine were. ( see <a href="https://www.openstreetmap.org/user/pieleric/diary/18588#comments">https://www.openstreetmap.org/user/pieleric/diary/18588#comments</a> )</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Mar '13, 14:59</strong></p>
<img src="https://secure.gravatar.com/avatar/6edb4957e57770118c3b8022cfce68a8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="srbrook&#39;s gravatar image" />
<p><span>srbrook</span><br />
<span class="score" title="993 reputation points">993</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="srbrook has 3 accepted answers">13%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Mar '13, 14:59</strong> </span></p>
</div>
</div>
<div id="comments-container-20511" class="comments-container">
<span id="20517"></span>
<div id="comment-20517" class="comment">
<div id="post-20517-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, it was probably a database problem, with type=boundary it still renders.</p>
</div>
<div id="comment-20517-info" class="comment-info">
<span class="comment-age">(06 Mar '13, 08:23)</span> <span class="comment-user userinfo">ligfietser</span>
</div>
</div>
</div>
<div id="comment-tools-20511" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20511-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="20466"></span>

<div id="answer-container-20466" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-20466-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20466-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-20466-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As far as I can tell boundary <em>names</em> are only rendered on zoom levels <a href="https://github.com/openstreetmap/mapnik-stylesheets/blob/master/osm.xml#L3324">8-11</a>. Your area seems to be rather small so maybe the text just doesn't fit on the map. But this is just a guess.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Mar '13, 16:44</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-20466" class="comments-container">
<span id="20469"></span>
<div id="comment-20469" class="comment">
<div id="post-20469-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This one is even smaller, and even the tiny polygon gets a name <a href="https://www.openstreetmap.org/?lat=52.378&amp;lon=6.344&amp;zoom=11&amp;layers=M&amp;relation=2745874">https://www.openstreetmap.org/?lat=52.378&amp;lon=6.344&amp;zoom=11&amp;layers=M&amp;relation=2745874</a></p>
</div>
<div id="comment-20469-info" class="comment-info">
<span class="comment-age">(03 Mar '13, 18:24)</span> <span class="comment-user userinfo">ligfietser</span>
</div>
</div>
<span id="20470"></span>
<div id="comment-20470" class="comment">
<div id="post-20470-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Then it could be a problem with the data in the database. Try touching it to upload a new version. This might fix the problem.</p>
</div>
<div id="comment-20470-info" class="comment-info">
<span class="comment-age">(03 Mar '13, 18:26)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="20471"></span>
<div id="comment-20471" class="comment">
<div id="post-20471-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ok, lets see.. I changed the type=boundary into type=multipolgon, maybe this helps?</p>
</div>
<div id="comment-20471-info" class="comment-info">
<span class="comment-age">(03 Mar '13, 18:32)</span> <span class="comment-user userinfo">ligfietser</span>
</div>
</div>
<span id="20473"></span>
<div id="comment-20473" class="comment">
<div id="post-20473-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Now it renders. I hope this change was really necessary and not just <a href="https://wiki.openstreetmap.org/wiki/Tagging_for_the_renderer">tagging for the renderer</a>.</p>
</div>
<div id="comment-20473-info" class="comment-info">
<span class="comment-age">(04 Mar '13, 07:05)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="20478"></span>
<div id="comment-20478" class="comment not_top_scorer">
<div id="post-20478-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks Scai, I can try to reset it back to type=boundary to see if it still renders.</p>
</div>
<div id="comment-20478-info" class="comment-info">
<span class="comment-age">(04 Mar '13, 10:36)</span> <span class="comment-user userinfo">ligfietser</span>
</div>
</div>
<span id="20494"></span>
<div id="comment-20494" class="comment not_top_scorer">
<div id="post-20494-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Maybe it's good to add a note to the object saying "retagged, see &lt;link to="" this="" question=""&gt;".</p>
</div>
<div id="comment-20494-info" class="comment-info">
<span class="comment-age">(04 Mar '13, 20:22)</span> <span class="comment-user userinfo">gormo</span>
</div>
</div>
<span id="20501"></span>
<div id="comment-20501" class="comment">
<div id="post-20501-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>It still renders after you changed it back to type=boundary so it seems like there was a problem in the database.</p>
</div>
<div id="comment-20501-info" class="comment-info">
<span class="comment-age">(05 Mar '13, 07:29)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-20466" class="comment-tools">
<span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-20466-form-container" class="comment-form-container">
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


+++
type = "question"
title = "England boundary relation (58447) - possible major problem?"
description = '''I am fairly new to OpenStreetMap, so it may be that I am missing something, but I have hit what seems to be a major problem while trying to process the administrative boundary relation for England. My code is reporting 41 ways that are referenced as members of relation 58447, but that do not exist i...'''
date = "2012-09-04T11:00:00Z"
lastmod = "2012-09-04T11:40:00Z"
weight = 15791
keywords = [ "ways", "relation", "boundary", "england" ]
aliases = [ "/questions/15791" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [England boundary relation (58447) - possible major problem?](/questions/15791/england-boundary-relation-58447-possible-major-problem)

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
<span id="post-15791-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15791-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-15791-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am fairly new to OpenStreetMap, so it may be that I am missing something, but I have hit what seems to be a major problem while trying to process the administrative boundary relation for England.</p>
<p>My code is reporting 41 ways that are referenced as members of relation 58447, but that do not exist in the england.osm file I downloaded from Geofabrik. This same code has successfully processed the administrative boundaries for other countries.</p>
<p>An example of these problem ways is way 10488014. On the <a href="http://www.openstreetmap.org/browse/relation/58447">relation webpage</a>, way 10488014 is listed as "Way 10488014 as outer". I click on <a href="http://www.openstreetmap.org/api/0.6/relation/58447">Download XML</a>, and there is no reference to way 10488014.</p>
<p>Am I missing something basic?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span> <span class="post-tag tag-link-relation" rel="tag" title="see questions tagged &#39;relation&#39;">relation</span> <span class="post-tag tag-link-boundary" rel="tag" title="see questions tagged &#39;boundary&#39;">boundary</span> <span class="post-tag tag-link-england" rel="tag" title="see questions tagged &#39;england&#39;">england</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Sep '12, 11:00</strong></p>
<img src="https://secure.gravatar.com/avatar/9b6b142985091a1566e3f91e1902284d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dave&#39;s gravatar image" />
<p><span>Dave</span><br />
<span class="score" title="86 reputation points">86</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dave has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-15791" class="comments-container">
&#10;</div>
<div id="comment-tools-15791" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15791-form-container" class="comment-form-container">
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

<span id="15792"></span>

<div id="answer-container-15792" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-15792-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15792-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-15792-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Geofabrik uses a simplifyed boundary polygon for its extracts. Because of this ways that are on the border may or may not be included in the extract.</p>
<p>The <a href="http://www.openstreetmap.org/api/0.6/relation/58447">http://www.openstreetmap.org/api/0.6/relation/58447</a> url only includes the relation and none of the objects it refers to. There is a referance to way 10488014 there, but that way is not included. If you want all the objects the relation refers to and the ones that those refers to and so on, you might want to try <a href="http://www.openstreetmap.org/api/0.6/relation/58447/full">http://www.openstreetmap.org/api/0.6/relation/58447/full</a> (warning, may take a long time to process).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Sep '12, 11:19</strong></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gnonthgol has 57 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-15792" class="comments-container">
<span id="15794"></span>
<div id="comment-15794" class="comment">
<div id="post-15794-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks very much Gnonthgol, that full link looks like exactly what I need!</p>
<p>Looks like I will need to manually create my own extracts for boundaries by downloading relations for individual countries, and just use the Geofabrik extracts for mapping features of interest onto them.</p>
</div>
<div id="comment-15794-info" class="comment-info">
<span class="comment-age">(04 Sep '12, 11:40)</span> <span class="comment-user userinfo">Dave</span>
</div>
</div>
</div>
<div id="comment-tools-15792" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15792-form-container" class="comment-form-container">
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


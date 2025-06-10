+++
type = "question"
title = "Merge months old OSM files with community version of the maps"
description = '''We maintain our OSM files locally for some months now and start to see roads that moved between our copy (Using Overpass turbo) and the online version. Those were indeed misaligned with aerial data. How can we catchup with the changes done by the community ? We are looking for a solution to merge ou...'''
date = "2018-08-23T10:55:00Z"
lastmod = "2018-08-24T11:08:00Z"
weight = 65528
keywords = [ "update", "osmosis", "local-copy" ]
aliases = [ "/questions/65528" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Merge months old OSM files with community version of the maps](/questions/65528/merge-months-old-osm-files-with-community-version-of-the-maps)

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
<span id="post-65528-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65528-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65528-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>We maintain our OSM files locally for some months now and start to see roads that moved between our copy (Using Overpass turbo) and the online version. Those were indeed misaligned with aerial data. How can we catchup with the changes done by the community ?</p>
<p>We are looking for a solution to merge our OSM files with the changes done on the map by the community. How can we do that ? Is there automated tools for that ?</p>
<p>The only thing we changed on the maps is adding an attribute to some streets.</p>
<p>We tried Osmosis but it doesn't merge, it only adds the changes to the layer.</p>
<p>Thanks a lot !</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-update" rel="tag" title="see questions tagged &#39;update&#39;">update</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span> <span class="post-tag tag-link-local-copy" rel="tag" title="see questions tagged &#39;local-copy&#39;">local-copy</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Aug '18, 10:55</strong></p>
<img src="https://secure.gravatar.com/avatar/6564074da82fb03a61dd6f73e4ea31e5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gp2mv3&#39;s gravatar image" />
<p><span>Gp2mv3</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gp2mv3 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-65528" class="comments-container">
&#10;</div>
<div id="comment-tools-65528" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65528-form-container" class="comment-form-container">
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

<span id="65539"></span>

<div id="answer-container-65539" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65539-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65539-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-65539-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you have the data in an osm2pgsql database you can add triggers that will add back your property to changed ways during a conventional update with diffs. But I suspect simply generating a list of the ways that you have changed and reapplying the change after a re-import would be simpler. In any case you will need to look at deletion and additions too.</p>
<p>Perhaps a better approach would be to use <a href="https://github.com/sharedstreets/sharedstreets-ref-system">https://github.com/sharedstreets/sharedstreets-ref-system</a> or OSMLR references for your attributes which then could be reapplied after updating and which would be immune to geometry operations that cause issues (splits, new ways and so on).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Aug '18, 09:35</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-65539" class="comments-container">
<span id="65540"></span>
<div id="comment-65540" class="comment">
<div id="post-65540-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>"<code>generating a list of the ways that you have changed and reapplying the change after a re-import would be simpler</code>" How can we do that ? It was indeed my idea at the beginning.</p>
</div>
<div id="comment-65540-info" class="comment-info">
<span class="comment-age">(24 Aug '18, 09:56)</span> <span class="comment-user userinfo">Gp2mv3</span>
</div>
</div>
<span id="65541"></span>
<div id="comment-65541" class="comment">
<div id="post-65541-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Well in what format/database schema do you have the data locally?</p>
</div>
<div id="comment-65541-info" class="comment-info">
<span class="comment-age">(24 Aug '18, 11:08)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-65539" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65539-form-container" class="comment-form-container">
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


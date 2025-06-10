+++
type = "question"
title = "Overpass question: is it possible to find the date a certain tag was added, and by whom, for all ways in a bbox?"
description = '''Hello all,  I&#x27;m working on a time lapse animation that shows when sidewalk tags were added in the Portland, OR, metro area. I can use overpass to get the streets that have sidewalk tags and use their last edit time stamp, but a lot of them have been modified again since the initial addition of the s...'''
date = "2016-08-12T20:01:00Z"
lastmod = "2016-08-12T22:07:00Z"
weight = 51377
keywords = [ "attic", "overpass", "version" ]
aliases = [ "/questions/51377" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass question: is it possible to find the date a certain tag was added, and by whom, for all ways in a bbox?](/questions/51377/overpass-question-is-it-possible-to-find-the-date-a-certain-tag-was-added-and-by-whom-for-all-ways-in-a-bbox)

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
<span id="post-51377-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51377-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-51377-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello all,</p>
<p>I'm working on a time lapse animation that shows when sidewalk tags were added in the Portland, OR, metro area. I can use overpass to get the streets that have sidewalk tags and use their last edit time stamp, but a lot of them have been modified again since the initial addition of the sidewalk=* tag. I'm wondering if it is possible to query the attic data to learn when a particular key was first added to each street in the area, and by whom. I've spent a good amount of time examining the documentation, but have been unable to find any examples like this. Is it possible?</p>
<p>Thank you very much,</p>
<p>Madeline</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-attic" rel="tag" title="see questions tagged &#39;attic&#39;">attic</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-version" rel="tag" title="see questions tagged &#39;version&#39;">version</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Aug '16, 20:01</strong></p>
<img src="https://secure.gravatar.com/avatar/a99958ffb04613a8ca73e65f3d76c2d1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mosteele&#39;s gravatar image" />
<p><span>mosteele</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mosteele has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Aug '16, 23:03</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-51377" class="comments-container">
&#10;</div>
<div id="comment-tools-51377" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51377-form-container" class="comment-form-container">
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

<span id="51379"></span>

<div id="answer-container-51379" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-51379-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51379-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-51379-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There's no direct way in Overpass to examine differences between versions of an object. There also is not a way to directly ask for a specific version of an object (I say direct because with enough date queries it should be possible to retrieve all of the versions you are interested in). You would need to fetch the objects you are interested in and then fetch the history for each one from the OSM API or pull them out of a history dump.</p>
<p>There are some existing tools for building history animations:</p>
<p><a href="https://github.com/MaZderMind/osm-history-renderer/blob/master/TUTORIAL.md">https://github.com/MaZderMind/osm-history-renderer/blob/master/TUTORIAL.md</a></p>
<p>Maybe that would be an alternative place to start.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Aug '16, 21:35</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Aug '16, 21:36</strong> </span></p>
</div>
</div>
<div id="comments-container-51379" class="comments-container">
<span id="51381"></span>
<div id="comment-51381" class="comment">
<div id="post-51381-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>There's already an enhancement request to request a specific version of an object, see: <a href="https://github.com/drolbr/Overpass-API/issues/282.">https://github.com/drolbr/Overpass-API/issues/282.</a></p>
<p>Full history processing is not for the faint-hearted, it needs a 51 GB (!) download to start with, unless you find an up to date history extract for your area. MaZderMind used to provide some of these for a few areas, but they don't seem to get updated anymore since at least a year now.</p>
</div>
<div id="comment-51381-info" class="comment-info">
<span class="comment-age">(12 Aug '16, 22:07)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
</div>
<div id="comment-tools-51379" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51379-form-container" class="comment-form-container">
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


+++
type = "question"
title = "Building height for big cities in United States"
description = '''Hi, I am trying to create a heat map of the footprints of buildings. The color representing the height of the buildings. I am looking for big cities such as New York, Chicago, Seattle, or San Francisco. Is there any way I can get a data or map that I am looking for?'''
date = "2020-08-28T17:02:00Z"
lastmod = "2020-09-02T08:36:00Z"
weight = 76341
keywords = [ "building", "height" ]
aliases = [ "/questions/76341" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Building height for big cities in United States](/questions/76341/building-height-for-big-cities-in-united-states)

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
<span id="post-76341-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76341-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-76341-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I am trying to create a heat map of the footprints of buildings. The color representing the height of the buildings. I am looking for big cities such as New York, Chicago, Seattle, or San Francisco. Is there any way I can get a data or map that I am looking for?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-building" rel="tag" title="see questions tagged &#39;building&#39;">building</span> <span class="post-tag tag-link-height" rel="tag" title="see questions tagged &#39;height&#39;">height</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Aug '20, 17:02</strong></p>
<img src="https://secure.gravatar.com/avatar/ee8656bc73c83ad1b3c2fc837b3bdac9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Yong&#39;s gravatar image" />
<p><span>Yong</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Yong has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-76341" class="comments-container">
&#10;</div>
<div id="comment-tools-76341" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76341-form-container" class="comment-form-container">
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

<span id="76390"></span>

<div id="answer-container-76390" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76390-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76390-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-76390-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Openstreetmap does have means to record building heights. The most generic approach is to fill a tag <a href="https://wiki.openstreetmap.org/wiki/Key:height#Height_of_buildings"><code>height=</code></a> on the building. There is a more detailed way of mapping/tagging more complex building shapes <a href="https://wiki.openstreetmap.org/wiki/Simple_3D_buildings">described on the wiki</a>. In some instances you might be able to estimate heights based on other information like building levels.</p>
<p>Having that said, recording height data is mostly on the lower end of the priority list of most mappers. The chance is good to find such data on landmark buildings and in the more prominent parts of cities but height data will be missing on the majority of buildings worldwide. You would need to check for yourself how sufficiently height data are recorded in your areas of interest. You can probably write a quick <a href="https://wiki.openstreetmap.org/wiki/Overpass_turbo">Overpass Turbo query</a> to get started with that.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Sep '20, 08:48</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-76390" class="comments-container">
<span id="76393"></span>
<div id="comment-76393" class="comment">
<div id="post-76393-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>An alternative to the exact height could be the <a href="https://wiki.openstreetmap.org/wiki/Key:building:levels"><code>building:levels</code></a> tag, which indicates the number of floors in a building. While also not frequently used, it's used much more often than <code>height</code> because it's easier to determine from street level. It could be used as an approximation for the building's height if you choose an average floor height and multiply by the number of floors.</p>
</div>
<div id="comment-76393-info" class="comment-info">
<span class="comment-age">(01 Sep '20, 18:18)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="76402"></span>
<div id="comment-76402" class="comment">
<div id="post-76402-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I got curious now. For downtown Chicago only few buildings have a height information (red) but the majority has building:levels tagged (green): <a href="http://overpass-turbo.eu/s/XC4">http://overpass-turbo.eu/s/XC4</a></p>
</div>
<div id="comment-76402-info" class="comment-info">
<span class="comment-age">(02 Sep '20, 08:36)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
</div>
<div id="comment-tools-76390" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76390-form-container" class="comment-form-container">
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


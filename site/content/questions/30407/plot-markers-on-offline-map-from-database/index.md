+++
type = "question"
title = "plot markers on offline map from database"
description = '''  I am trying to make a android application that display a map when application run without using any internet connection ie. offline map show.On map i want to plot some latitude and longitude that are stored in my database.Basically i want plot a offline map and on map i need to display some marker...'''
date = "2014-02-03T10:32:00Z"
lastmod = "2016-05-20T06:04:00Z"
weight = 30407
keywords = [ "marker", "development", "android", "offline" ]
aliases = [ "/questions/30407" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [plot markers on offline map from database](/questions/30407/plot-markers-on-offline-map-from-database)

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
<span id="post-30407-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30407-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-30407-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<pre><code></code></pre>
<p>I am trying to make a android application that display a map when application run without using any internet connection ie. offline map show.On map i want to plot some latitude and longitude that are stored in my database.Basically i want plot a offline map and on map i need to display some marker from my database.But i could not plot offline map and marker.I searched more on Google but i could not found any better solution. please help me to make my offline map app. Thank You</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-marker" rel="tag" title="see questions tagged &#39;marker&#39;">marker</span> <span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-android" rel="tag" title="see questions tagged &#39;android&#39;">android</span> <span class="post-tag tag-link-offline" rel="tag" title="see questions tagged &#39;offline&#39;">offline</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Feb '14, 10:32</strong></p>
<img src="https://secure.gravatar.com/avatar/1458890eb6e97ccc3eb83e3dec353fef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Aakash&#39;s gravatar image" />
<p><span>Aakash</span><br />
<span class="score" title="10 reputation points">10</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Aakash has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 May '16, 22:52</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-30407" class="comments-container">
<span id="49750"></span>
<div id="comment-49750" class="comment">
<div id="post-49750-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi Aakash!! Please I would like to know if you were finally able to plot makers on offline map from Database.If so please could let me know the step you followed to do that thank you Sonia my regards</p>
</div>
<div id="comment-49750-info" class="comment-info">
<span class="comment-age">(20 May '16, 01:32)</span> <span class="comment-user userinfo">kouayep</span>
</div>
</div>
</div>
<div id="comment-tools-30407" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30407-form-container" class="comment-form-container">
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

<span id="30411"></span>

<div id="answer-container-30411" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-30411-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30411-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-30411-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are two ways to get offline map data onto the device, either as raster data or as vector data. You then need a piece of software that takes the raster tiles and displays them, or loads the vector data and draws it. I suggest that you peruse the <a href="https://wiki.openstreetmap.org/wiki/Android">Android</a> software list on our Wiki and check out some of the existing programs. Many are open-source so you can inspect the source code. There's a table at the bottom of the page detailing whether the software has bitmap or vector data, and supports offline maps.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Feb '14, 11:06</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-30411" class="comments-container">
&#10;</div>
<div id="comment-tools-30411" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30411-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="49751"></span>

<div id="answer-container-49751" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-49751-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49751-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-49751-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>While not the only choice you can use <a href="https://github.com/mapsforge/mapsforge">https://github.com/mapsforge/mapsforge</a> for offline rendering of OSM data, or extract the rendering engine from one of the applications that already do so (osmand, maps.me).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 May '16, 06:04</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-49751" class="comments-container">
&#10;</div>
<div id="comment-tools-49751" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49751-form-container" class="comment-form-container">
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


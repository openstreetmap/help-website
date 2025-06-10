+++
type = "question"
title = "How to edit the map boundaries for local OSM server?"
description = '''Hi, I have a local OSM map server setup using ModTile and Renderd. I have two requirements:  How to edit the administrative boundaries of a country? How can I change color of boundary? '''
date = "2017-07-12T10:21:00Z"
lastmod = "2018-07-19T18:36:00Z"
weight = 57031
keywords = [ "boundary" ]
aliases = [ "/questions/57031" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to edit the map boundaries for local OSM server?](/questions/57031/how-to-edit-the-map-boundaries-for-local-osm-server)

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
<span id="post-57031-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57031-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-57031-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I have a local OSM map server setup using ModTile and Renderd. I have two requirements:</p>
<ol>
<li>How to edit the administrative boundaries of a country?</li>
<li>How can I change color of boundary?</li>
</ol>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-boundary" rel="tag" title="see questions tagged &#39;boundary&#39;">boundary</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Jul '17, 10:21</strong></p>
<img src="https://secure.gravatar.com/avatar/1a9eea008bc0c9a26985aa042d9b8ac2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Reshma%20Maner&#39;s gravatar image" />
<p><span>Reshma Maner</span><br />
<span class="score" title="235 reputation points">235</span><span title="30 badges"><span class="badge1">●</span><span class="badgecount">30</span></span><span title="31 badges"><span class="silver">●</span><span class="badgecount">31</span></span><span title="36 badges"><span class="bronze">●</span><span class="badgecount">36</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Reshma Maner has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-57031" class="comments-container">
&#10;</div>
<div id="comment-tools-57031" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57031-form-container" class="comment-form-container">
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

<span id="57049"></span>

<div id="answer-container-57049" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-57049-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57049-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-57049-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are a number of ways that I can think of to do what you want, plus more that I haven't though of:</p>
<ul>
<li>don't use any borders directly from OSM by disabling the entry in your style, extract the boundaries from your DB in to, say a .SHP file, edit with QGIS, add shapefile as a separate layer to the style, with whatever styling your want.</li>
<li>just replace the border in question by not rendering it specifically (modify the query in the style), and then add a modified boundary as above (note: this will be a bit wobbly as OSM IDs are not stable, and will likely be ugly as other borders will not match up)</li>
</ul>
<p>Changing the colour requires changing the style for the specific border.</p>
<p>As said there are probably other ways of doing this, but as you can see, none of them are likely to be super simple.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Jul '17, 09:39</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Jul '18, 13:26</strong> </span></p>
</div>
</div>
<div id="comments-container-57049" class="comments-container">
<span id="64796"></span>
<div id="comment-64796" class="comment">
<div id="post-64796-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>don't use any borders directly from OSM by disabling the entry in your style</p>
<p>Can you help me how to implement this? Which file exactly to modify?</p>
</div>
<div id="comment-64796-info" class="comment-info">
<span class="comment-age">(19 Jul '18, 12:33)</span> <span class="comment-user userinfo">Reshma Maner</span>
</div>
</div>
<span id="64797"></span>
<div id="comment-64797" class="comment">
<div id="post-64797-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Which style are you currently using?</p>
</div>
<div id="comment-64797-info" class="comment-info">
<span class="comment-age">(19 Jul '18, 13:27)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="64804"></span>
<div id="comment-64804" class="comment">
<div id="post-64804-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>GIven your other question you probably want to read this post by PlaneMad: <a href="https://www.openstreetmap.org/user/PlaneMad/diary/38176.">https://www.openstreetmap.org/user/PlaneMad/diary/38176.</a></p>
<p>There are also multiple other questions on this site relating to Jammu and Kashmir. Most of the answers are still applicable and may be of help to you.</p>
</div>
<div id="comment-64804-info" class="comment-info">
<span class="comment-age">(19 Jul '18, 18:36)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-57049" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57049-form-container" class="comment-form-container">
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


+++
type = "question"
title = "&quot;Best&quot;/&quot;quickest&quot; way to build a layer"
description = '''Hey, I am sorry to ask, but I am new to OSM. I am reading and searching the web for 2 hours now to find the best way to draw a map. Basically I need to add a new layer to an existing map (I guess). I want to support my hometown by drawing allowed fishing regions to a river. There are some special th...'''
date = "2014-06-22T11:23:00Z"
lastmod = "2014-06-22T16:47:00Z"
weight = 34243
keywords = [ "layers", "editor", "beginner" ]
aliases = [ "/questions/34243" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# ["Best"/"quickest" way to build a layer](/questions/34243/bestquickest-way-to-build-a-layer)

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
<span id="post-34243-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34243-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-34243-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hey,</p>
<p>I am sorry to ask, but I am new to OSM. I am reading and searching the web for 2 hours now to find the best way to draw a map. Basically I need to add a new layer to an existing map (I guess). I want to support my hometown by drawing allowed fishing regions to a river. There are some special thinks where you are allowed to draw from within the river, but not from the landing sides and all of that.</p>
<p>I hoped to find an easy solution to basically draw in different colors areas on the water and at the water borders ...</p>
<p>Once again, please excuse if this question is too easy, but I only found ways where I either need to code something up (end result is an export to a bigger PNG file), or where I would contribute to the OSM map (which is not requested I guess). The map itself can be public really ...</p>
<p>Any help would be appreciated. Thanks agin.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-layers" rel="tag" title="see questions tagged &#39;layers&#39;">layers</span> <span class="post-tag tag-link-editor" rel="tag" title="see questions tagged &#39;editor&#39;">editor</span> <span class="post-tag tag-link-beginner" rel="tag" title="see questions tagged &#39;beginner&#39;">beginner</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Jun '14, 11:23</strong></p>
<img src="https://secure.gravatar.com/avatar/2f7fdbcee61fd393ffcdbbcd2f4352ff?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iamherefor&#39;s gravatar image" />
<p><span>iamherefor</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iamherefor has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Jun '14, 11:45</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span></p>
</div>
</div>
<div id="comments-container-34243" class="comments-container">
&#10;</div>
<div id="comment-tools-34243" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-34243-form-container" class="comment-form-container">
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

<span id="34244"></span>

<div id="answer-container-34244" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-34244-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34244-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-34244-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If the data is not in OSM and you simply want to draw the areas in question then you could for example use umap.openstreetmap.fr and use a suitable basemap from the collection available.</p>
<p>If the data -is- available in OSM, you could again use umap and simply add a query to get the specific data from the overpass api and display it.</p>
<p>As nearly always in OSM there are many many ways to skin the cat.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Jun '14, 11:48</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-34244" class="comments-container">
<span id="34250"></span>
<div id="comment-34250" class="comment">
<div id="post-34250-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks</p>
<p>yes that gets pretty close to what I need really. As you said, there might be too many ways for new starters ;). Thanks for helping me</p>
</div>
<div id="comment-34250-info" class="comment-info">
<span class="comment-age">(22 Jun '14, 16:47)</span> <span class="comment-user userinfo">iamherefor</span>
</div>
</div>
</div>
<div id="comment-tools-34244" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-34244-form-container" class="comment-form-container">
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


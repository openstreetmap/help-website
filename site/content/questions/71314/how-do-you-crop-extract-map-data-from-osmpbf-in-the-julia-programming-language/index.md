+++
type = "question"
title = "how do you crop / extract map data from .osm.pbf in the Julia programming language"
description = '''My goal is to obtain the driving road network of a certain area using open street map data. Reference link: What&#x27;s the general algorithm to draw a road network of a certain area? I&#x27;m using Julia package OpenStreetMapX. In the function call get_map_data, I realized that there is the other function Op...'''
date = "2019-10-24T10:39:00Z"
lastmod = "2019-10-28T14:43:00Z"
weight = 71314
keywords = [ "julia", "crop" ]
aliases = [ "/questions/71314" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how do you crop / extract map data from .osm.pbf in the Julia programming language](/questions/71314/how-do-you-crop-extract-map-data-from-osmpbf-in-the-julia-programming-language)

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
<span id="post-71314-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71314-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-71314-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>My goal is to obtain the driving road network of a certain area using open street map data. Reference link: What's the general algorithm to draw a road network of a certain area? I'm using Julia package OpenStreetMapX. In the function call <code>get_map_data</code>, I realized that there is the other function <code>OpenStreetMapX.crop!(osmdata, crop_relations = false)</code>. I understand that the purpose of this function is to crop the nodes, ways, relations based on a given bounds. I'm confused about these two different methods.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-julia" rel="tag" title="see questions tagged &#39;julia&#39;">julia</span> <span class="post-tag tag-link-crop" rel="tag" title="see questions tagged &#39;crop&#39;">crop</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Oct '19, 10:39</strong></p>
<img src="https://secure.gravatar.com/avatar/1f2484650afc45030bf68ad06b8ff6af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="good0&#39;s gravatar image" />
<p><span>good0</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="good0 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Oct '19, 14:24</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span></p>
</div>
</div>
<div id="comments-container-71314" class="comments-container">
&#10;</div>
<div id="comment-tools-71314" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71314-form-container" class="comment-form-container">
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

<span id="71341"></span>

<div id="answer-container-71341" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71341-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71341-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-71341-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I had a quick look at the repo and there didn't seem to be a crop function to start with, see <a href="https://pszufe.github.io/OpenStreetMapX.jl/latest/reference/">https://pszufe.github.io/OpenStreetMapX.jl/latest/reference/</a> Further I didn't see any PBF format support, just OSM xml format.</p>
<p>I would suggest asking the author for support as it is rather unlikely anybody here will be able to help you.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Oct '19, 14:33</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-71341" class="comments-container">
<span id="71345"></span>
<div id="comment-71345" class="comment">
<div id="post-71345-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The crop function is here: <a href="https://github.com/pszufe/OpenStreetMapX.jl/blob/master/src/crop.jl">https://github.com/pszufe/OpenStreetMapX.jl/blob/master/src/crop.jl</a> The .osm file is supported as the following: using OpenStreetMapX map_data = get_map_data("/home/ubuntu/mymap.osm"); println("The map contains $(length(map_data.nodes)) nodes")</p>
</div>
<div id="comment-71345-info" class="comment-info">
<span class="comment-age">(28 Oct '19, 12:33)</span> <span class="comment-user userinfo">good0</span>
</div>
</div>
<span id="71350"></span>
<div id="comment-71350" class="comment">
<div id="post-71350-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If just doesn't turn up in the documentation.</p>
</div>
<div id="comment-71350-info" class="comment-info">
<span class="comment-age">(28 Oct '19, 14:43)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-71341" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71341-form-container" class="comment-form-container">
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


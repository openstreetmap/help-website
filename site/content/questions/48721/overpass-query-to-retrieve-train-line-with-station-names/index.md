+++
type = "question"
title = "[closed] Overpass query to retrieve train line with station names?"
description = '''I&#x27;m no OSM/Overpass expert, and need to draw a map on Umap by retrieving train lines from OSM, along with the names of the stations. I googled for this, searched the archives, but still can&#x27;t figure out how to build the right query in OverpassTurbo. How should I edit the following query to include s...'''
date = "2016-03-17T12:48:00Z"
lastmod = "2016-03-17T22:24:00Z"
weight = 48721
keywords = [ "overpass-turbo" ]
aliases = [ "/questions/48721" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] Overpass query to retrieve train line with station names?](/questions/48721/overpass-query-to-retrieve-train-line-with-station-names)

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
<span id="post-48721-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48721-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-48721-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm no OSM/Overpass expert, and need to draw a map on Umap by retrieving train lines from OSM, along with the names of the stations.</p>
<p>I googled for this, searched the archives, but still can't figure out how to build the right query in OverpassTurbo.</p>
<p>How should I edit the following query to include station names?</p>
<pre><code>[out:json][timeout:25];
(
  relation[&quot;network&quot;=&quot;SomeTrainNetwork&quot;][&quot;ref&quot;=&quot;TrainLineReference&quot;]({{bbox}});
);
&#10;out body;
&gt;;
out skel qt;</code></pre>
<p>Thank you.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Mar '16, 12:48</strong></p>
<img src="https://secure.gravatar.com/avatar/222fc1ad4f1993620a21cb57fa816f16?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Shohreh&#39;s gravatar image" />
<p><span>Shohreh</span><br />
<span class="score" title="85 reputation points">85</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Shohreh has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>17 Mar '16, 22:29</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-48721" class="comments-container">
<span id="48725"></span>
<div id="comment-48725" class="comment">
<div id="post-48725-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Crossposting from <a href="http://forum.openstreetmap.org/viewtopic.php?id=54031">http://forum.openstreetmap.org/viewtopic.php?id=54031</a></p>
<p>Be aware that crossposting is lowering the chance of getting good answers!</p>
<p>What did you try from that forum answer????</p>
</div>
<div id="comment-48725-info" class="comment-info">
<span class="comment-age">(17 Mar '16, 16:32)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
<span id="48726"></span>
<div id="comment-48726" class="comment">
<div id="post-48726-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Not much, because it makes no sense to a newbie like me. Which is why I asked here too. What's wrong with that?</p>
</div>
<div id="comment-48726-info" class="comment-info">
<span class="comment-age">(17 Mar '16, 21:17)</span> <span class="comment-user userinfo">Shohreh</span>
</div>
</div>
<span id="48727"></span>
<div id="comment-48727" class="comment">
<div id="post-48727-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>meta <a href="http://help.openstreetmap.org/users/3711/shohreh"></a><a href="http://help.openstreetmap.org/users/3711/shohreh">@Shohreh</a>: crossposting wastes resources (the people who are spending their time to help) because of dulicate work and scatters the collected information/answers across several places (relevant for others in the future with the same question). Please do not do it (unless for very special reason with clear links between each post).</p>
</div>
<div id="comment-48727-info" class="comment-info">
<span class="comment-age">(17 Mar '16, 22:24)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-48721" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48721-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Duplicate Question. Please stay at the original location and continue there." by aseerel4c26 17 Mar '16, 22:29

</div>

</div>

</div>


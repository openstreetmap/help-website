+++
type = "question"
title = "Speed limit nodes: keep or delete?"
description = '''Someone in my area added speed limit signs along major roads as nodes. They are tagged: maxspeed=55 mph source=usgs_imagery;survey;image source_ref=* Someone, possibly the same person, has updated the maxspeed tag on the roads themselves, possibly using the nodes as guidance. I am wondering if I sho...'''
date = "2011-02-13T07:29:00Z"
lastmod = "2011-07-26T16:24:00Z"
weight = 2997
keywords = [ "nodes", "speed", "fixup" ]
aliases = [ "/questions/2997" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Speed limit nodes: keep or delete?](/questions/2997/speed-limit-nodes-keep-or-delete)

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
<span id="post-2997-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2997-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-2997-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Someone in my area added speed limit signs along major roads as nodes. They are tagged:</p>
<p>maxspeed=55 mph<br />
source=usgs_imagery;survey;image<br />
source_ref=*</p>
<p>Someone, possibly the same person, has updated the maxspeed tag on the roads themselves, possibly using the nodes as guidance.</p>
<p>I am wondering if I should delete the nodes now that they have served their useful purpose and appear to contain duplicate information (I am taking upon myself general cleanup of the area) or leave them alone since they represent valid physical objects - speed limit signs. The nodes were created in May 2010, so I don't think it's a work in progress.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-speed" rel="tag" title="see questions tagged &#39;speed&#39;">speed</span> <span class="post-tag tag-link-fixup" rel="tag" title="see questions tagged &#39;fixup&#39;">fixup</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Feb '11, 07:29</strong></p>
<img src="https://secure.gravatar.com/avatar/c23c2891306229bb036de7ce63bb8c9b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ponzu&#39;s gravatar image" />
<p><span>ponzu</span><br />
<span class="score" title="2104 reputation points"><span>2.1k</span></span><span title="49 badges"><span class="badge1">●</span><span class="badgecount">49</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="83 badges"><span class="bronze">●</span><span class="badgecount">83</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ponzu has no accepted answers">0%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Feb '11, 07:30</strong> </span></p>
</div>
</div>
<div id="comments-container-2997" class="comments-container">
<span id="6559"></span>
<div id="comment-6559" class="comment">
<div id="post-6559-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The trouble with speedlimit nodes is that they don't tell which direction the speed limit applies in. (That JOSM renders them all as "60" doesn't help either). I tend to treat speed limit nodes as temporary: when I've surveyed the area (in practice, this means determining the closure of roads where the &lt;NSL applies), I delete them and apply the maxspeed= to the ways.</p>
</div>
<div id="comment-6559-info" class="comment-info">
<span class="comment-age">(26 Jul '11, 12:15)</span> <span class="comment-user userinfo">mwbg</span>
</div>
</div>
<span id="6566"></span>
<div id="comment-6566" class="comment">
<div id="post-6566-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@mwbg</span> you really shouldn't delete them, the positions of the signs are very helpful when mapping and verifying maxspeeds. There is a mappaint style you can add to your JOSM-configuration to display the actual numbers (you can find it in the prefs). It currently doesn't work for speed limits in mph but you can easily extend it to do this. The solution for the direction is to put the nodes besides the road (this is usually at their position) rather than on it. There is also documentation on the wiki: <a href="https://wiki.openstreetmap.org/wiki/Key:source:maxspeed">https://wiki.openstreetmap.org/wiki/Key:source:maxspeed</a></p>
</div>
<div id="comment-6566-info" class="comment-info">
<span class="comment-age">(26 Jul '11, 16:22)</span> <span class="comment-user userinfo">dieterdreist</span>
</div>
</div>
</div>
<div id="comment-tools-2997" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2997-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="2999"></span>

<div id="answer-container-2999" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-2999-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2999-score" class="post-score" title="current number of votes">
7
</div>
<span id="post-2999-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ponzu has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OpenStreetMap stores full history information for all objects. This means that you can easily find out who placed the objects, and who updated the maxspeed tags - no need for speculation a la "someone, possibly the same person". Some editors can show the object history at a keystroke; but you can also access the history by simply zooming into the area of interest on <a href="http://www.openstreetmap.org">www.openstreetmap.org</a> and then select the "data" layer from the layer drop-down behind the "+" button on the top right. Select the road, or sign, in question on the map, then click "Show History".</p>
<p>The best course of action is to discuss the matter with whoever placed the signs and agree on how to deal with the signs. There are reasons for keeping them (one might want to draw a hyper-detailed map that shows the actual sign locations; one might want to count the number of signs in the city; redundancy is sometimes good because it helps find discrepancies), but your point that they might be obsolete now isn't wrong either.</p>
<p>The worst thing that could happen is you deleting them while someone else thinks they are still relevant!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Feb '11, 10:21</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-2999" class="comments-container">
&#10;</div>
<div id="comment-tools-2999" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2999-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="3031"></span>

<div id="answer-container-3031" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-3031-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3031-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-3031-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I would keep them. These are often landmarks of reference for casual directions, too. "Turn right into the first driveway after the speed limit sign."</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Feb '11, 01:11</strong></p>
<img src="https://secure.gravatar.com/avatar/666698a7b13e402aba7e1e0f6de7c1d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Baloo%20Uriza&#39;s gravatar image" />
<p><span>Baloo Uriza</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="61 badges"><span class="bronze">●</span><span class="badgecount">61</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Baloo Uriza has 12 accepted answers">9%</span></p>
</div>
</div>
<div id="comments-container-3031" class="comments-container">
&#10;</div>
<div id="comment-tools-3031" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3031-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="6567"></span>

<div id="answer-container-6567" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-6567-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6567-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-6567-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You name it: "leave them alone since they represent valid physical objects - speed limit signs." I'd keep them.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Jul '11, 16:24</strong></p>
<img src="https://secure.gravatar.com/avatar/f09c0b7a655fed386e070e036e2da248?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dieterdreist&#39;s gravatar image" />
<p><span>dieterdreist</span><br />
<span class="score" title="3677 reputation points"><span>3.7k</span></span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="67 badges"><span class="bronze">●</span><span class="badgecount">67</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dieterdreist has 4 accepted answers">3%</span></p>
</div>
</div>
<div id="comments-container-6567" class="comments-container">
&#10;</div>
<div id="comment-tools-6567" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6567-form-container" class="comment-form-container">
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


+++
type = "question"
title = "POIs: Nodes vs. outlines"
description = '''A POI is traditionally defined as a node. However, many POIs being buildings and grounds, it is possible to trace an outline and assign the same metadata to it as one would to a traditional POI. For the variety of current and conceivable uses of OSM, what is the best practice when mapping POIs?  Tra...'''
date = "2011-02-11T18:31:00Z"
lastmod = "2011-02-11T22:00:00Z"
weight = 2958
keywords = [ "poi" ]
aliases = [ "/questions/2958" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [POIs: Nodes vs. outlines](/questions/2958/pois-nodes-vs-outlines)

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
<span id="post-2958-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2958-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-2958-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
5
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>A POI is traditionally defined as a node. However, many POIs being buildings and grounds, it is possible to trace an outline and assign the same metadata to it as one would to a traditional POI. For the variety of current and conceivable uses of OSM, what is the best practice when mapping POIs?</p>
<ol>
<li>Trace the building or grounds, name it, assign meta as you would to a POI, do not create a POI node.<br />
Pros: Single set of meta, most accurate representation of the physical shape of a POI.<br />
Cons: Some applications only retrieve nodes as POIs.</li>
<li>Trace the building or grounds, assign meta as you would to a POI. Create a POI node, assign the same meta.<br />
Pros: Covers all possible current and future uses of OSM.<br />
Cons: Duplicated meta (more effort, more room for discrepancy if one set of data gets changed and the other does not). The applications (e.g., map renderes) that look for both nodes and shapes as POIs may end up showing two POIs with the same name.</li>
<li>Trace the building or grounds, enter minimal meta to ensure proper rendering (shading). Create a POI node and assign all applicable meta.<br />
Pros: Most renderers should show both the POI as a point and the shading of the outline, without duplicate names appearing on the map.<br />
Cons: Meta is somewhat arbitrarily distributed between the outline and the node. Compromising (limiting) data in favor of the "lazier" existing users. The assumption about some data users (renderers, etc.) being unaware of outline POIs may be an incorrect one.</li>
</ol>
<p>I would lean towards 1. Is there a consensus? A wiki article would be nice.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-poi" rel="tag" title="see questions tagged &#39;poi&#39;">poi</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Feb '11, 18:31</strong></p>
<img src="https://secure.gravatar.com/avatar/c23c2891306229bb036de7ce63bb8c9b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ponzu&#39;s gravatar image" />
<p><span>ponzu</span><br />
<span class="score" title="2104 reputation points"><span>2.1k</span></span><span title="49 badges"><span class="badge1">●</span><span class="badgecount">49</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="83 badges"><span class="bronze">●</span><span class="badgecount">83</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ponzu has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-2958" class="comments-container">
&#10;</div>
<div id="comment-tools-2958" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2958-form-container" class="comment-form-container">
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

<span id="2967"></span>

<div id="answer-container-2967" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-2967-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2967-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-2967-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ponzu has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The first option is preferred, where possible. See the wiki pages on <a href="https://wiki.openstreetmap.org/wiki/Good_practice">Good practice</a> and <a href="https://wiki.openstreetmap.org/wiki/One_feature,_one_OSM_element">One feature, one OSM element</a>. Basically if there is only one feature on the ground, then only one object in OSM should be tagged as that.</p>
<p>Its true that this causes some applications or renderers to not show some features mapped as areas. But that is a bug with the application/renderer, which should be reported and fixed. If necessary, you could do pre-processing of the OSM data, to convert features mapped as areas into nodes, before rendering the map. With your options 2 or 3, this would cause duplicate objects on the map.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Feb '11, 21:50</strong></p>
<img src="https://secure.gravatar.com/avatar/aa505c046b1c010e997a7849c6f3dbbe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vclaw&#39;s gravatar image" />
<p><span>Vclaw</span><br />
<span class="score" title="9217 reputation points"><span>9.2k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="95 badges"><span class="silver">●</span><span class="badgecount">95</span></span><span title="141 badges"><span class="bronze">●</span><span class="badgecount">141</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vclaw has 41 accepted answers">22%</span> </br></br></p>
</div>
</div>
<div id="comments-container-2967" class="comments-container">
<span id="2968"></span>
<div id="comment-2968" class="comment">
<div id="post-2968-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the links. I wish someone would update the POI article on wiki to say what you said. I do not consider myself sufficiently experienced in the ways of OSM (or wiki) to take it upon myself.</p>
</div>
<div id="comment-2968-info" class="comment-info">
<span class="comment-age">(11 Feb '11, 22:00)</span> <span class="comment-user userinfo">ponzu</span>
</div>
</div>
</div>
<div id="comment-tools-2967" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2967-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="2963"></span>

<div id="answer-container-2963" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-2963-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2963-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-2963-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'm not sure there is a consensus but I've always believed best practice to be the first method, rather than having duplicated information in the database. I'm sure I read it somewhere, and thanks to Google I found <a href="http://forum.openstreetmap.org/viewtopic.php?id=5115">http://forum.openstreetmap.org/viewtopic.php?id=5115</a> which seems to agree with this view. I failed to find anything in the wiki other than a Car Park discussion which again seems to support option 1 (without concensus).</p>
<p>Having said that I did recently add place nodes back because Mapnik didn't render the place names on areas at the same zoom levels and typeface as it does the nodes, and it just looked wrong to have all the place names effectively disappearing from the map.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Feb '11, 20:27</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span> </br></br></p>
</div>
</div>
<div id="comments-container-2963" class="comments-container">
&#10;</div>
<div id="comment-tools-2963" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2963-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="2965"></span>

<div id="answer-container-2965" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-2965-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2965-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-2965-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Basically anything but option 1 well totally wrong from my point of view and luckily it is the consensus in Openstreetmap as far as I can tell.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Feb '11, 20:48</strong></p>
<img src="https://secure.gravatar.com/avatar/465f344e31e8ba1be0e0401414815db0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="petschge&#39;s gravatar image" />
<p><span>petschge</span><br />
<span class="score" title="8279 reputation points"><span>8.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="73 badges"><span class="silver">●</span><span class="badgecount">73</span></span><span title="98 badges"><span class="bronze">●</span><span class="badgecount">98</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="petschge has 29 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-2965" class="comments-container">
&#10;</div>
<div id="comment-tools-2965" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2965-form-container" class="comment-form-container">
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


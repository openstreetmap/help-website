+++
type = "question"
title = "smooth curved ways"
description = '''Hi there are times when I would like to be able to select a length of a bendy way and apply a bezier function to smooth and then allow me to make further adjustments as necessary. Currently I add extra points drag around until satisfied. Creeks are a prime target that I can see in my area. Is this a...'''
date = "2013-10-04T14:57:00Z"
lastmod = "2013-10-07T01:05:00Z"
weight = 26948
keywords = [ "bezier", "editors", "smooth-curves" ]
aliases = [ "/questions/26948" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [smooth curved ways](/questions/26948/smooth-curved-ways)

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
<span id="post-26948-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26948-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-26948-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi there are times when I would like to be able to select a length of a bendy way and apply a bezier function to smooth and then allow me to make further adjustments as necessary. Currently I add extra points drag around until satisfied. Creeks are a prime target that I can see in my area. Is this available in any of the editors for me to try. I am using JOSM and it seems not to have this feature or a plugin. I guess drawbacks may be that such functions would tend to add far more nodes that necessary and some may find it difficult to resist 'prettying' up their map and losing authenticity. I should add that I am not that familiar with doing this practically with mapping, so feel free to express contrary views to such a feature.</p>
<hr />
<p>edit: just found further info <a href="https://wiki.openstreetmap.org/wiki/Bezier_curves">bezier curves osm</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-bezier" rel="tag" title="see questions tagged &#39;bezier&#39;">bezier</span> <span class="post-tag tag-link-editors" rel="tag" title="see questions tagged &#39;editors&#39;">editors</span> <span class="post-tag tag-link-smooth-curves" rel="tag" title="see questions tagged &#39;smooth-curves&#39;">smooth-curves</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Oct '13, 14:57</strong></p>
<img src="https://secure.gravatar.com/avatar/e5674dd96938593e0af5130dfffe0f90?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nevw&#39;s gravatar image" />
<p><span>nevw</span><br />
<span class="score" title="9843 reputation points"><span>9.8k</span></span><span title="26 badges"><span class="badge1">●</span><span class="badgecount">26</span></span><span title="90 badges"><span class="silver">●</span><span class="badgecount">90</span></span><span title="178 badges"><span class="bronze">●</span><span class="badgecount">178</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nevw has 32 accepted answers">9%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Oct '13, 15:17</strong> </span></p>
</div>
</div>
<div id="comments-container-26948" class="comments-container">
&#10;</div>
<div id="comment-tools-26948" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26948-form-container" class="comment-form-container">
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

<span id="26952"></span>

<div id="answer-container-26952" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-26952-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26952-score" class="post-score" title="current number of votes">
9
</div>
<span id="post-26952-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Just add enough points so that the way follows the shape of the feature, and don't worry too much about making it smooth. Renderers can smooth out the curves later. For example, have a look at:</p>
<ul>
<li><a href="https://www.openstreetmap.org/#map=18/56.31251/-4.72841">https://www.openstreetmap.org/#map=18/56.31251/-4.72841</a> - raw OSM data</li>
<li><a href="http://www.opencyclemap.org/?zoom=17&amp;lat=56.31223&amp;lon=-4.728&amp;layers=000B">http://www.opencyclemap.org/?zoom=17&amp;lat=56.31223&amp;lon=-4.728&amp;layers=000B</a> - smoothed rivers and railways on my Outdoors layer.</li>
</ul>
<p>There's always plenty more things to map rather than spending excessive time on one particular feature! My rule of thumb is that if there's enough nodes that the edges stay within the width of the road on background imagery, that's enough. Alternatively, if the displacement of the midpoint of each pair of nodes from the real feature is less than 2 metres, that's enough too. Beyond that is usually just adding nodes without adding any real information.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Oct '13, 16:29</strong></p>
<img src="https://secure.gravatar.com/avatar/c3743b1b368f5e209eb8aad30164acc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Allan&#39;s gravatar image" />
<p><span>Andy Allan</span><br />
<span class="score" title="12456 reputation points"><span>12.5k</span></span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="128 badges"><span class="silver">●</span><span class="badgecount">128</span></span><span title="153 badges"><span class="bronze">●</span><span class="badgecount">153</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andy Allan has 46 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-26952" class="comments-container">
&#10;</div>
<div id="comment-tools-26952" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26952-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="26971"></span>

<div id="answer-container-26971" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-26971-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26971-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-26971-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The utilsplugin2 JOSM plugin has a "circle arc" feature in the "More Tools" menu. See this page on the JOSM wiki for how to use it:</p>
<p><a href="http://josm.openstreetmap.de/wiki/Help/Action/CreateCircleArc">http://josm.openstreetmap.de/wiki/Help/Action/CreateCircleArc</a></p>
<p>Also, do you know about the "w" mode in JOSM? I don't see it actually mentioned in the menus anywhere... It lets you select a way and then either move existing nodes, create new nodes (by holding CTRL) or delete nodes (by holding ALT) just by clicking.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Oct '13, 01:05</strong></p>
<img src="https://secure.gravatar.com/avatar/43ae79d3345e19f30ea5f2ea64a9f7bc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ToeBee&#39;s gravatar image" />
<p><span>ToeBee</span><br />
<span class="score" title="976 reputation points">976</span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ToeBee has 6 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-26971" class="comments-container">
&#10;</div>
<div id="comment-tools-26971" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26971-form-container" class="comment-form-container">
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

</hr>

</div>

</div>


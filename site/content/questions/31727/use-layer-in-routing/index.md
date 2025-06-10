+++
type = "question"
title = "Use Layer in Routing?"
description = '''Is it possible to create a layer and then use its data for routing? For example, let&#x27;s say I create a Crash Layer. Then I would like to avoid any Crash Markers from that layer when routing. Is this possible?'''
date = "2014-03-20T22:03:00Z"
lastmod = "2014-03-23T18:54:00Z"
weight = 31727
keywords = [ "avoid_areas", "routing" ]
aliases = [ "/questions/31727" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Use Layer in Routing?](/questions/31727/use-layer-in-routing)

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
<span id="post-31727-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31727-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-31727-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is it possible to create a layer and then use its data for routing?</p>
<p>For example, let's say I create a Crash Layer. Then I would like to avoid any Crash Markers from that layer when routing.</p>
<p>Is this possible?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-avoid_areas" rel="tag" title="see questions tagged &#39;avoid_areas&#39;">avoid_areas</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Mar '14, 22:03</strong></p>
<img src="https://secure.gravatar.com/avatar/722ff1c1ab33ba7f87d17fbbc624b52f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mikepatt77&#39;s gravatar image" />
<p><span>mikepatt77</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mikepatt77 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Mar '14, 00:21</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-31727" class="comments-container">
<span id="31728"></span>
<div id="comment-31728" class="comment">
<div id="post-31728-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You mean you want to tell a routing algorithm to <em>avoid</em> specific locations? Or what do you think a "layer" is? Or do you want to know if and how we can add such "crashes" to the OSM data?</p>
</div>
<div id="comment-31728-info" class="comment-info">
<span class="comment-age">(20 Mar '14, 22:29)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="31729"></span>
<div id="comment-31729" class="comment">
<div id="post-31729-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes I would like to avoid specific locations. My understanding of a layer is that it is a set of markers that can go on top of a map view. Is that wrong?</p>
</div>
<div id="comment-31729-info" class="comment-info">
<span class="comment-age">(20 Mar '14, 23:03)</span> <span class="comment-user userinfo">mikepatt77</span>
</div>
</div>
<span id="31731"></span>
<div id="comment-31731" class="comment">
<div id="post-31731-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Okay, no, that is not wrong, but likely not something which should be in the OMS data. It should only be fed privately to your routing engine. See SomeoneElse below.</p>
</div>
<div id="comment-31731-info" class="comment-info">
<span class="comment-age">(21 Mar '14, 00:05)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-31727" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31727-form-container" class="comment-form-container">
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

<span id="31730"></span>

<div id="answer-container-31730" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-31730-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31730-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-31730-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="mikepatt77 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<h2 id="tldr-answer">tl;dr answer:</h2>
<p>I don't know but probably, and you'd have to do quite a lot of work yourself.</p>
<h2 id="slightly-more-in-depth-non-answer">Slightly more in-depth non-answer:</h2>
<p>OpenStreetMap is essentially just lots and lots of data. A "renderer" turns that data (usually stored in some sort of database) into a map, and other software (such as "Leaflet", used on osm.org) display those maps to the user, and can display other information overlaid over the top as extra layers (as happens on the OSM site when you show notes or data).</p>
<p>Routers work with the data in a different way to calculate routes. They don't work with a graphical representation (the "map") but with an internal representation of the data that's designed so that they can make route calculations quickly. If you want those calculations to include some specific locations ("crash markers") you're going to have to include those locations in in the routing data that the router uses for its calculations.<br />
</p>
<p>Various routers that can work with OSM data are described <a href="http://wiki.openstreetmap.org/wiki/Routing">here</a>. Each of these typically has more information available about it; I'd start by reading that. For example, you might find the technical information on <a href="https://github.com/graphhopper/graphhopper/wiki/Developers">this GraphHopper page</a> useful.</p>
</div>
<div class="answer-controls post-controls">
<div class="community-wiki">
This answer is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Mar '14, 23:25</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> wikified <strong>20 Mar '14, 23:25</strong> </span></p>
</div>
</div>
<div id="comments-container-31730" class="comments-container">
<span id="31734"></span>
<div id="comment-31734" class="comment">
<div id="post-31734-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>So my understanding is that there's an underlying graph representation for the routers. This representation then has weights on the edges. Is there a way for me to modify the weights?</p>
</div>
<div id="comment-31734-info" class="comment-info">
<span class="comment-age">(21 Mar '14, 07:33)</span> <span class="comment-user userinfo">mikepatt77</span>
</div>
</div>
<span id="31735"></span>
<div id="comment-31735" class="comment">
<div id="post-31735-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Yes there is an underlying graph representation for the routers. But OSM doesn't contain this graph, it contains only the raw data needed to generate it. Each router calculates its own graph. Consequently there is no general answer to your question because it depends on the specific router you are interested in. But with most open source routers it should be possible to add such a "layer".</p>
</div>
<div id="comment-31735-info" class="comment-info">
<span class="comment-age">(21 Mar '14, 07:38)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="31800"></span>
<div id="comment-31800" class="comment">
<div id="post-31800-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Searching this help facility for "network" or "graph" should get you some info about how to build such a graph from OSM data.</p>
</div>
<div id="comment-31800-info" class="comment-info">
<span class="comment-age">(23 Mar '14, 18:54)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-31730" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31730-form-container" class="comment-form-container">
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


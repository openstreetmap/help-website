+++
type = "question"
title = "Parks are going less green?"
description = '''Over the past year or two, several parks in my area have lost their green shading and just render the same as most of the other land. Example: https://www.openstreetmap.org/relation/1153480 This entire park [Lynn Woods] and several others near it used to be the typical green shading, and evidently s...'''
date = "2022-06-19T03:51:00Z"
lastmod = "2022-06-19T23:56:00Z"
weight = 84812
keywords = [ "landuse", "green" ]
aliases = [ "/questions/84812" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Parks are going less green?](/questions/84812/parks-are-going-less-green)

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
<span id="post-84812-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84812-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-84812-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Over the past year or two, several parks in my area have lost their green shading and just render the same as most of the other land. Example: <a href="https://www.openstreetmap.org/relation/1153480">https://www.openstreetmap.org/relation/1153480</a></p>
<p>This entire park [Lynn Woods] and several others near it used to be the typical green shading, and evidently someone has changed the "landuse" or whatever tag affects that over time and now they don't render that way. I've tried to look at the feature history but that doesn't really tell me anything, there's nothing I see that allows me to <strong>look at</strong> an old version of a feature and figure out where the delta was.</p>
<p>So, two questions: <strong>1&gt;</strong> why is this being done to the parks, it makes them much harder to spot as parks, and <strong>2&gt;</strong> what exactly is the tag set that forces the desired green rendering? I want to contact whoever's been un-greening them and find out how and why. I've looked in a lot of places and <strong>cannot</strong> find any doc on how this works.</p>
<p>_H*</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-landuse" rel="tag" title="see questions tagged &#39;landuse&#39;">landuse</span> <span class="post-tag tag-link-green" rel="tag" title="see questions tagged &#39;green&#39;">green</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Jun '22, 03:51</strong></p>
<img src="https://secure.gravatar.com/avatar/3031665c506b04f416a1af103cf8cf6e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="_Hobbit&#39;s gravatar image" />
<p><span>_Hobbit</span><br />
<span class="score" title="51 reputation points">51</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="_Hobbit has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-84812" class="comments-container">
&#10;</div>
<div id="comment-tools-84812" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84812-form-container" class="comment-form-container">
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

<span id="84816"></span>

<div id="answer-container-84816" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-84816-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84816-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-84816-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In the early days of OSM, any type of park would be tagged as <code>leisure=park</code> which would render with the solid green shading. As tagging has changed to be more precise, <code>leisure=park</code> has been restricted for use only on managed greenery areas - where the grass, trees and gardens are regularly maintained.</p>
<p>'Parks' or nature reserves with large areas set aside for natural or wild state are marked as <code>boundary=protected_area</code> + <code>protect_class=*</code> or <code>leisure=nature_reserve</code>. Because they are often much larger areas and can include multiple land use types, they are rendered with a green shaded outline instead of solid green. That allows more detailed land use tagging within the protected area.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Jun '22, 12:07</strong></p>
<img src="https://secure.gravatar.com/avatar/1dd5f61a81b99dd54ec6f33d96aa38b2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mike%20N&#39;s gravatar image" />
<p><span>Mike N</span><br />
<span class="score" title="2926 reputation points"><span>2.9k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mike N has 16 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-84816" class="comments-container">
<span id="84817"></span>
<div id="comment-84817" class="comment">
<div id="post-84817-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>So as more areas that used to be usefully green-shaded get their "park" tags stripped away, the harder it will become to spot large natural parks in a broad map overview? I do <strong>not</strong> see that as a useful trend. There are (or at least were) plenty of green-shaded areas with more detail inside, and it never seemed to be any sort of "problem". There really should still be a way to internally shade areas like that.</p>
<p>And again, how do I <em>view</em> historical snapshots on the OSM website, or get a visual of what existed as of a particular changeset?</p>
<p>_H*</p>
</div>
<div id="comment-84817-info" class="comment-info">
<span class="comment-age">(19 Jun '22, 12:40)</span> <span class="comment-user userinfo">_Hobbit</span>
</div>
</div>
<span id="84819"></span>
<div id="comment-84819" class="comment">
<div id="post-84819-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I checked the tagging history of Lynn Woods and it appears that it hadn't been using leisure=park, so the shading result is likely a change in the default rendering (Carto). There aren't any easy ways to view historical versions of Carto rendering that I'm aware of.</p>
</div>
<div id="comment-84819-info" class="comment-info">
<span class="comment-age">(19 Jun '22, 13:20)</span> <span class="comment-user userinfo">Mike N</span>
</div>
</div>
<span id="84821"></span>
<div id="comment-84821" class="comment">
<div id="post-84821-score" class="comment-score">
1
</div>
<div class="comment-text">
<blockquote>
<p>What I want is ...</p>
</blockquote>
<p>Create your own map.</p>
<p>That is the only way that you are going to get what you exactly want. You might not like that answer (you complained about having to go to github to create an issue in another question), but ultimately every map (available via osm.org and elsewhere) has someone designing it, and one of the questions that they have answered is "how green should parks be". They will have made their decision based on a whole bunch of conflicting goals (to be able to distinguish landuses, to not "make everything louder than everything else") in different areas.</p>
</div>
<div id="comment-84821-info" class="comment-info">
<span class="comment-age">(19 Jun '22, 14:36)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="84822"></span>
<div id="comment-84822" class="comment">
<div id="post-84822-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The real frustration has been trying to find what the best consensus is for these or any other issues, and that is an uphill battle when there's no clear starting point. I didn't know the Github path until I made a wild guess to ask here, but ultimately glad that what I identified was accepted. In comparing the (sorry) state of various parks in my area which render in wildly different ways, I'm trying to find a common set of tags which will make it all a bit more uniform. I don't want to just go wildly stomping things until I'm relatively sure it will do the right thing and not piss off the entire community and cause gratuitous overwriting of my changes.</p>
<p>Better that I do this research and asking-around before just diving in with a bunch of bull-in-china-shop edits, no?</p>
<p>_H*</p>
</div>
<div id="comment-84822-info" class="comment-info">
<span class="comment-age">(19 Jun '22, 15:05)</span> <span class="comment-user userinfo">_Hobbit</span>
</div>
</div>
<span id="84826"></span>
<div id="comment-84826" class="comment">
<div id="post-84826-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>"What I want is for parks (in our canonical US definition) to render far more visibly"</p>
<p>Perhaps the "OpenStreetMap Americana" renderer is closer to what you want? It generally aims to render a map more in line with what people used to U.S. mapping conventions would expect. I don't know specifically how their treatment of parks and nature reserves differs from OSM-Carto, but from a quick look, they do seem to apply green shading to Lynn Woods. Probably not surprising, as at least part of the issue here seems to be ongoing transatlantic differences about what exactly a "park" means. The wiki page for the renderer is here: <a href="https://wiki.openstreetmap.org/wiki/OpenStreetMap_Americana">https://wiki.openstreetmap.org/wiki/OpenStreetMap_Americana</a> (link to the map itself in the info box).</p>
<p>Also as a point of comparison, the Humanitarian style on the main OpenStreetMap page also shows Lynn Woods in green (although fairly faint in keeping with the generally muted colours of the style).</p>
</div>
<div id="comment-84826-info" class="comment-info">
<span class="comment-age">(19 Jun '22, 20:16)</span> <span class="comment-user userinfo">alan_gr</span>
</div>
</div>
<span id="84828"></span>
<div id="comment-84828" class="comment not_top_scorer">
<div id="post-84828-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have no idea how to "choose a renderer", unless that's the "layers" option on the main website? But for real life, I load a .obf into OSMAnd and let 'er rip, get similar results to what I see on the main website standard layer and figure that side of things is out of my control.</p>
<p>I've been comparing various parks with different looks and tags, and as pointed out many places in the wiki, it's a mess. "landuse=forest" seems to be a common denominator, though, maybe that's what they all need.</p>
<p>_H*</p>
</div>
<div id="comment-84828-info" class="comment-info">
<span class="comment-age">(19 Jun '22, 23:56)</span> <span class="comment-user userinfo">_Hobbit</span>
</div>
</div>
</div>
<div id="comment-tools-84816" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-84816-form-container" class="comment-form-container">
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


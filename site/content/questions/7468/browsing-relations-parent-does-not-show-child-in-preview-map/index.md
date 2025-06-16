+++
type = "question"
title = "Browsing relations - parent does not show child in preview map"
description = '''What are the current rules for showing a preview map on relations &quot;browse&quot; pages? Preview map for this relation does not show at all. How do I make it appear and make it show the contents of child relations with a blue line as usual for relations containing ways only? PS. I know relations are deprec...'''
date = "2011-08-31T11:02:00Z"
lastmod = "2011-09-10T20:03:00Z"
weight = 7468
keywords = [ "rendering", "relations" ]
aliases = [ "/questions/7468" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Browsing relations - parent does not show child in preview map](/questions/7468/browsing-relations-parent-does-not-show-child-in-preview-map)

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
<span id="post-7468-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7468-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-7468-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>What are the current rules for showing a preview map on relations "browse" pages? Preview map for <a href="https://www.openstreetmap.org/browse/relation/1717720">this relation</a> does not show at all. How do I make it appear and make it show the contents of child relations with a blue line as usual for relations containing ways only?</p>
<p>PS. I know relations are deprecated by power-users here, but since there is no reasonable service for plotting tag searches into a map, I think relatins still have their meaning at least untill such service is created. Also, relations save resources since no tag search needs to be done for showing content.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Aug '11, 11:02</strong></p>
<img src="https://secure.gravatar.com/avatar/7d327873d48d28e563c9ad7259853c35?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kozuch&#39;s gravatar image" />
<p><span>Kozuch</span><br />
<span class="score" title="1720 reputation points"><span>1.7k</span></span><span title="58 badges"><span class="badge1">●</span><span class="badgecount">58</span></span><span title="72 badges"><span class="silver">●</span><span class="badgecount">72</span></span><span title="85 badges"><span class="bronze">●</span><span class="badgecount">85</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kozuch has one accepted answer">8%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Sep '11, 21:22</strong> </span></p>
</div>
</div>
<div id="comments-container-7468" class="comments-container">
&#10;</div>
<div id="comment-tools-7468" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7468-form-container" class="comment-form-container">
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

<span id="7520"></span>

<div id="answer-container-7520" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7520-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7520-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-7520-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The browse page simply uses the API call /api/0.6/relation/(id)/full.</p>
<p>As you'll see from the <a href="https://wiki.openstreetmap.org/wiki/API_0.6#Full:_GET_.2Fapi.2F0.6.2F.5Bway.7Crelation.5D.2F.23id.2Ffull">API documentation</a>, this does not recurse down all levels of nested relations. It merely returns the 'top level' of relation members, and that's it.</p>
<p>This is clearly necessary to prevent overuse of the call boggling our servers. It's already been the case that people overusing the /full call has almost brought the API to its knees at times (notably when people started creating massive relations to contain the bounding boxes for Bing imagery in each country).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Sep '11, 21:51</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-7520" class="comments-container">
&#10;</div>
<div id="comment-tools-7520" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7520-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="7535"></span>

<div id="answer-container-7535" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7535-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7535-score" class="post-score" title="current number of votes">
-2
</div>
<span id="post-7535-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>"Relations deprecated by power users" ???</p>
<p>Huh... I had the exact inverse feeling that relations was the way to go, in order to better structure the data as soon as it becomes very rich and very difficult to find the related items (for example adminsitrative areas, that can be hierarchically structured, or not, and that have various levels of scalings, and impossible to edit reliably at low zoom levels.</p>
<p>Without relations, you end up creating many data duplicates, that become even harder to unify. Relations are a very powerful tool that certainly helps finding items in the database. With the "roles" that they support, you can associate items with different types, according to a convenient schema which becomes possible to create. with those relations, you can infer various selective layers of data, to show or hide local details.</p>
<p>Without relations, the OSM data will become a tricky bags full of knots that rapidly become impossible to structure in something that an be rendered correctly on a map (depending on the zoom level or what users want to see on a map, according to their preferences or what they are looking for).</p>
<p>Relations also allow checking the integrity of the map data, to avoid contradictions. It simplifies the corrections needed (in case of errors, or because the actual world has effectively changed due to humane work, accidents, or natural events, or must change in a near future, where planning of works for the changes we want to add as metadata requires some organization and searches of various items on the map, or because we need to add other metadata for mapping in progress or requiring more investigation due to missing data).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Sep '11, 01:49</strong></p>
<img src="https://secure.gravatar.com/avatar/b0ac3d0a15ce4f96f0d6b29172fca72a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Verdy_p&#39;s gravatar image" />
<p><span>Verdy_p</span><br />
<span class="score" title="141 reputation points">141</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Verdy_p has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-7535" class="comments-container">
<span id="7765"></span>
<div id="comment-7765" class="comment">
<div id="post-7765-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Who voted negatively to my comment above ? Plese add arguments instead of just this unexplained "thumb down". Because I gave arguments which outweight largely the small inconvenient (only superficially evoked above) about the performance of recursive queries on relations (which I think is a false problem: you don't need to recurse a relation, most of the time to use, i.e. search or render, what is defined by a relation).</p>
</div>
<div id="comment-7765-info" class="comment-info">
<span class="comment-age">(10 Sep '11, 04:12)</span> <span class="comment-user userinfo">Verdy_p</span>
</div>
</div>
<span id="7766"></span>
<div id="comment-7766" class="comment">
<div id="post-7766-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Relations have clear advantages, notably for structuring the dataset and allowing powerful searches, as well as for maintaining a consistency, and hopefully completeness (at least down to some level, even if some detailed levels are missing) of the database. Relations allow faster convergence of the dataset to a stable state, where only the smallest edits at the thinnest zoom level will be needed, without breaking the upper levels that remain unchanged (even if the number of their members may locally change).</p>
</div>
<div id="comment-7766-info" class="comment-info">
<span class="comment-age">(10 Sep '11, 04:12)</span> <span class="comment-user userinfo">Verdy_p</span>
</div>
</div>
<span id="7767"></span>
<div id="comment-7767" class="comment">
<div id="post-7767-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>And anyway the "power users" evoked above are only those that are imported data coming from other databases, which are already structured with relations and layers. If we don't have relations, those bots importing data will have lots of difficulties to find how to update a zone that has been updated in the source: they will frequently generate duplicates, because there's no reliable key to make the link between what is in the OSM dataset (which may have been modified by others or by concurrent bots importing their own datasets) and what is now in the updated data source.</p>
</div>
<div id="comment-7767-info" class="comment-info">
<span class="comment-age">(10 Sep '11, 04:15)</span> <span class="comment-user userinfo">Verdy_p</span>
</div>
</div>
<span id="7770"></span>
<div id="comment-7770" class="comment">
<div id="post-7770-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>If you were required to say what was wrong, you would be prompted with an input field to do so. There is absolutely no compulsion to give an explanation for a thumbs-down.</p>
<p>Also, there's a limit on this comment field for a reason. Circumventing it by making three posts defeats the point of the help system. If you want to have a debate, mailing lists are the right place, not <a href="http://help.osm.org">help.osm.org</a>.</p>
</div>
<div id="comment-7770-info" class="comment-info">
<span class="comment-age">(10 Sep '11, 07:55)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="7774"></span>
<div id="comment-7774" class="comment">
<div id="post-7774-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Three comments was only due to limitations of length for the reply. All of them are a single reply. They use distinct, clearly separated arguments. I clearly have different opinions than you, but you don't need to expose your "opinion" as a "fact".</p>
</div>
<div id="comment-7774-info" class="comment-info">
<span class="comment-age">(10 Sep '11, 20:03)</span> <span class="comment-user userinfo">Verdy_p</span>
</div>
</div>
</div>
<div id="comment-tools-7535" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7535-form-container" class="comment-form-container">
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


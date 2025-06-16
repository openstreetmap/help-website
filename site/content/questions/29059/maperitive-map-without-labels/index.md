+++
type = "question"
title = "Maperitive: Map without labels"
description = '''I&#x27;m a total noobcomer so please forgive what is probably a very simple request. I&#x27;m working on an application using MetOffice information, and I want to overlay the images they produce onto a map of the correct corresponding dimensions. The geographical dimensions are 12W, 61N, 5E, 48N. The graphic ...'''
date = "2013-12-14T13:45:00Z"
lastmod = "2013-12-14T22:14:00Z"
weight = 29059
keywords = [ "rules", "maperitive", "labels", "export", "overlay" ]
aliases = [ "/questions/29059" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Maperitive: Map without labels](/questions/29059/maperitive-map-without-labels)

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
<span id="post-29059-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29059-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-29059-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm a total noobcomer so please forgive what is probably a very simple request.</p>
<p>I'm working on an application using <a href="http://www.metoffice.gov.uk/">MetOffice</a> information, and I want to overlay the images they produce onto a map of the correct corresponding dimensions.</p>
<p>The geographical dimensions are 12W, 61N, 5E, 48N. The graphic they produce is 500x500px, so probably needs to be scaled to fit that shape.</p>
<p>My intention is to get a static map without any labels ("United Kingdom", "London" etc) and then overlay one png on top of the other. I want to use the Transport web map.</p>
<p>I've figured out how to get Maperitive to export an image of the right geographical area, but it still has labels.</p>
<p>So my first question is how do I get this (as an exported png) from Maperitive?</p>
<p>I tried doing <a href="/questions/1873/how-can-i-create-a-map-without-any-names-on-it/1879">this</a>. With the following commands:</p>
<pre><code>edit-rules 
//replace all occurrences of &#39;draw:text&#39; and &#39;draw : text&#39; with &#39;&#39;
//save as notext.mrules
use-ruleset location=rules\notext.mrules as-alias=notext
apply-ruleset
reload-ruleset</code></pre>
<p>This doesn't remove the labels.</p>
<p>Secondly, is this really the right strategy to solve this problem? I say this because it might, at some point be useful to put on certain place names, and it seems like a static file is then the wrong thing for the job.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rules" rel="tag" title="see questions tagged &#39;rules&#39;">rules</span> <span class="post-tag tag-link-maperitive" rel="tag" title="see questions tagged &#39;maperitive&#39;">maperitive</span> <span class="post-tag tag-link-labels" rel="tag" title="see questions tagged &#39;labels&#39;">labels</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-overlay" rel="tag" title="see questions tagged &#39;overlay&#39;">overlay</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Dec '13, 13:45</strong></p>
<img src="https://secure.gravatar.com/avatar/fd8b338f4d691481b78461a957cfc045?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fernbritton&#39;s gravatar image" />
<p><span>fernbritton</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fernbritton has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-29059" class="comments-container">
<span id="29066"></span>
<div id="comment-29066" class="comment">
<div id="post-29066-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>In case that you cannot get a sufficient answer about the ruleset of Maperitive: Have you already asked at the Maperitive googlegroup mailinglist?</p>
</div>
<div id="comment-29066-info" class="comment-info">
<span class="comment-age">(14 Dec '13, 17:27)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
<span id="29069"></span>
<div id="comment-29069" class="comment">
<div id="post-29069-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@stephan75</span> "Have you already asked at the Maperitive googlegroup mailinglist?" No, but I assumed that this site had members who could help since the question I linked was posted here. I might try if no joy here.</p>
</div>
<div id="comment-29069-info" class="comment-info">
<span class="comment-age">(14 Dec '13, 19:02)</span> <span class="comment-user userinfo">fernbritton</span>
</div>
</div>
</div>
<div id="comment-tools-29059" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29059-form-container" class="comment-form-container">
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

<span id="29075"></span>

<div id="answer-container-29075" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29075-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29075-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-29075-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>A common first-time user error with Maperitive is that people think the map displayed when they start the program is already the "product", the map they're working with and that is influenced by style choices.</p>
<p>It isn't.</p>
<p>The map you see when you fire up Maperitive is the map from www.openstreetmap.org and no amount of styling you do will change its looks. You need to load data first, and then (for clarity) disable the "background" map, to see something that Maperitive has rendered by itself. And then, once you've done that, you can apply different styling to it.</p>
<p>How do I know that you have made this mistake?</p>
<p>I know because Maperitive would never have been able to load such a large area! You must understand that data is not filtered server-side, so Maperitive will load all OSM data there is in that rectangle, including every lamppost and every bridleway. Even if you chose not to display them, they would still linger in memory and make it impossible to work with the data.</p>
<p>So, the answer to your question "is this the right strategy", is no. You could possibly get away with Maperitive if you were to pre-filter the data using Osmosis or so, leaving in only the bits you actually need, but that would be tedious.</p>
<p>Note that if you want to "simply combine bitmaps" they absolutely must be in the same map projection. I see that some Met Office products use the same Mercator projection that OSM does, but maybe not all do. Read the documentation carefully.</p>
<p>How much do you want to show on your map anyway? Perhaps the free shape files from naturalearthdata.com (which have just populated places, coastline, lakes, rivers, and a couple major roads) are already a sufficient data source for your task, then you could simply load them up in a GIS program of your choice and apply some basic styling to the different things. The advantage is that they have simplified data that is already prepared for using at the scale you want.</p>
<p>Another option is importing OSM data into a local PostgreSQL data base, and using a simple map style like "OSM bright" and the WYSIWYG style editor TileMill, render that into a PNG image. The advantage of the database approach is that while the database will have all OSM data for the UK, the rendering program can ask the database to hand out only what is required for the map being rendered.</p>
<p>Note that "I want to use the transport web map" makes no sense with any of these approaches including the one you tried initially; the rendering style for the transport web map could potentially work with TileMill (not Maperitive) but it not available for you to modify.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Dec '13, 22:14</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Dec '13, 22:30</strong> </span></p>
</div>
</div>
<div id="comments-container-29075" class="comments-container">
&#10;</div>
<div id="comment-tools-29075" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29075-form-container" class="comment-form-container">
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


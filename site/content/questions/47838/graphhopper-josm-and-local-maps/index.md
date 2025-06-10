+++
type = "question"
title = "Graphhopper, josm and local maps"
description = '''Hi, it&#x27;s the first time for me in this &quot;vast world&quot; and so I had to understand better a lot of concepts... MY GOAL - import a map in JOSM ==&amp;gt; okay - create new building ==&amp;gt; okay (I think...I&#x27;ve also populate some label: address, building, name...) - I save my modification locally in a OSM file...'''
date = "2016-02-02T23:56:00Z"
lastmod = "2016-02-03T08:50:00Z"
weight = 47838
keywords = [ "josm", "graphhopper" ]
aliases = [ "/questions/47838" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Graphhopper, josm and local maps](/questions/47838/graphhopper-josm-and-local-maps)

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
<span id="post-47838-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47838-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-47838-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, it's the first time for me in this "vast world" and so I had to understand better a lot of concepts...</p>
<p>MY GOAL - import a map in JOSM ==&gt; okay - create new building ==&gt; okay (I think...I've also populate some label: address, building, name...) - I save my modification locally in a OSM file ==&gt; Okay - Run GraphHopper as: java -jar graphhopper-web-0.5.0-with-dep.jar jetty.resourcebase=webapp config=config-example.properties osmreader.osm=mymap.osm</p>
<p>So, I see that for example if I modified in JOSM street nodes I see this modification in Graphhopper. But if I try i.e. to find in the search my new building (as address) I receive a "No area description found".</p>
<p>The same if for example I modify in JOSM the position of a build on the map.</p>
<p>What I misunderstanding? Every time I restart Graphhopper server and clear the "*-gh" directory... Is it because addressess / build name etc. are always taken "from the network" (from public servers)???</p>
<p>How to force GraphHopper to show and consider my modification?</p>
<p>I'm really confused... I'm sorry if this could be a dummy question :S :(</p>
<p>Thank you in advance.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-graphhopper" rel="tag" title="see questions tagged &#39;graphhopper&#39;">graphhopper</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Feb '16, 23:56</strong></p>
<img src="https://secure.gravatar.com/avatar/fd31b5bb300ca8f285da1e613c45bda3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="The%20Hammer&#39;s gravatar image" />
<p><span>The Hammer</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="The Hammer has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-47838" class="comments-container">
<span id="47842"></span>
<div id="comment-47842" class="comment">
<div id="post-47842-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Huh, you can get a Graphhoper java file and run it locally?</p>
</div>
<div id="comment-47842-info" class="comment-info">
<span class="comment-age">(03 Feb '16, 07:04)</span> <span class="comment-user userinfo">ivanatora</span>
</div>
</div>
<span id="47844"></span>
<div id="comment-47844" class="comment">
<div id="post-47844-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Yes, Graphhopper is Open Source. <a href="https://github.com/graphhopper/graphhopper">https://github.com/graphhopper/graphhopper</a></p>
</div>
<div id="comment-47844-info" class="comment-info">
<span class="comment-age">(03 Feb '16, 07:10)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-47838" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47838-form-container" class="comment-form-container">
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

<span id="47845"></span>

<div id="answer-container-47845" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47845-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47845-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-47845-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Graphhopper is <em>only</em> a routing engine. It finds shortest/best paths from A to B. It does not draw maps, and it does not search places. The Graphhopper example web site is a small web site that combines Graphhopper's routing with maps drawn by some other service on the web, and search provided by some other service on the web. If you want a 100% local solution, you will have to set up a search engine too (e.g. Nominatim), and a rendering engine (e.g. a tile server as discussed on switch2osm.org, or perhaps since your area is small enough to load in JOSM, you can render map tiles with Maperitive).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Feb '16, 07:14</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-47845" class="comments-container">
<span id="47849"></span>
<div id="comment-47849" class="comment">
<div id="post-47849-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi, thank you!</p>
<p>After post this question, I work (at night....) at the problem and I understood about Nominatim and all the infrstructure behind it and behind OSM.</p>
<p>I think (this is a personal consideration) that OSM is a tool too broad (but obviously also powerful) than what I propose to do (an indoor map with simple routing office by office).</p>
<p>So, it's the time to "put all the cards on the table" and decide which tool (open source) use for this project. ;)</p>
</div>
<div id="comment-47849-info" class="comment-info">
<span class="comment-age">(03 Feb '16, 08:50)</span> <span class="comment-user userinfo">The Hammer</span>
</div>
</div>
</div>
<div id="comment-tools-47845" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47845-form-container" class="comment-form-container">
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


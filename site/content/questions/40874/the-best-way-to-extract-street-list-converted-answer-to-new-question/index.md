+++
type = "question"
title = "The best way to extract street list [converted answer to new question]"
description = '''(converted from https://help.openstreetmap.org/questions/9816/the-best-way-to-extract-street-list/40874 ) There still doesn&#x27;t seem to be any simple way to get a proper Country-&amp;gt;Province/State-&amp;gt;Place-&amp;gt;Street hierarchy out. I need that for the entire US and UK to start.  A highway is an open ...'''
date = "2015-02-09T03:53:00Z"
lastmod = "2015-02-10T19:12:00Z"
weight = 40874
keywords = [ "hierarchy", "street", "list", "sql" ]
aliases = [ "/questions/40874" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [The best way to extract street list \[converted answer to new question\]](/questions/40874/the-best-way-to-extract-street-list-converted-answer-to-new-question)

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
<span id="post-40874-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40874-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-40874-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>(converted from <a href="/questions/9816/the-best-way-to-extract-street-list/40874">https://help.openstreetmap.org/questions/9816/the-best-way-to-extract-street-list/40874</a> )</p>
<p>There still doesn't seem to be any simple way to get a proper Country-&gt;Province/State-&gt;Place-&gt;Street hierarchy out. I need that for the entire US and UK to start.</p>
<p>A highway is an open Way polyline, and the others are closed Way polylines. The only relationship between them known to OSM is geographical, as far as I can tell. Converting this data to an address hierarchy requires a lot of polygon intersection tests to tell what's inside what.</p>
<p>Has anyone built a tool for that? I don't see capabilities for that in osmfilter or osmosis. Loading all that spatial data into an SQL database with spatial indices is possible, but most of those don't do spatial joins very well.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-hierarchy" rel="tag" title="see questions tagged &#39;hierarchy&#39;">hierarchy</span> <span class="post-tag tag-link-street" rel="tag" title="see questions tagged &#39;street&#39;">street</span> <span class="post-tag tag-link-list" rel="tag" title="see questions tagged &#39;list&#39;">list</span> <span class="post-tag tag-link-sql" rel="tag" title="see questions tagged &#39;sql&#39;">sql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Feb '15, 03:53</strong></p>
<img src="https://secure.gravatar.com/avatar/e2ea9651a3d3b41da4ae3240003d869f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="John_Nagle&#39;s gravatar image" />
<p><span>John_Nagle</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="John_Nagle has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> converted to question <strong>10 Feb '15, 17:16</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span></p>
</div>
</div>
<div id="comments-container-40874" class="comments-container">
&#10;</div>
<div id="comment-tools-40874" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40874-form-container" class="comment-form-container">
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

<span id="40936"></span>

<div id="answer-container-40936" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-40936-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40936-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-40936-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Have a look at the <a href="https://osm.wno-edv-service.de/boundaries/">web service</a> from OSM user Wambacher:</p>
<p>There you have a tree structure of all valid boundary relations on the planet. Can this be an entry point for you?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Feb '15, 17:18</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-40936" class="comments-container">
<span id="40937"></span>
<div id="comment-40937" class="comment">
<div id="post-40937-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>That will fetch the hierarchy for named places, but doesn't do anything with highway/Way info other than display it.</p>
<p>I just want Country-&gt;Province/State-&gt;Place-&gt;Street without the geometry, for the entire US. Calculating that from highway and region geometry is a big job. Someone must have done this already.</p>
</div>
<div id="comment-40937-info" class="comment-info">
<span class="comment-age">(10 Feb '15, 18:17)</span> <span class="comment-user userinfo">John_Nagle</span>
</div>
</div>
<span id="40942"></span>
<div id="comment-40942" class="comment">
<div id="post-40942-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>When I do this (I do OSM data extraction as a commercial service) I always run a number of more or less manual steps on an osm2pgsql import. Of course you can greatly speed up the osm2pgsql import by only importing the bits you're interested in. The difficult bit is that depending on the country you're running this in, a sizable proportion of streets will not have a full hierarchy (e.g. in the US, will be inside a state but not inside any county or street) - do you then omit them, or assign them to a virtual place called "other", or...?</p>
</div>
<div id="comment-40942-info" class="comment-info">
<span class="comment-age">(10 Feb '15, 19:12)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-40936" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40936-form-container" class="comment-form-container">
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


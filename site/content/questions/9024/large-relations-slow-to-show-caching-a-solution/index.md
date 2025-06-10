+++
type = "question"
title = "Large relations slow to show - caching a solution?"
description = '''I often work with large relations (like this). Currently, the preview maps at osm.org/browse/relation/[number] or at osm.org/?relation=[number] load painfully slowly. Can this be solved somehow? Is it possible to cache these so they would load instantly?'''
date = "2011-11-16T07:45:00Z"
lastmod = "2011-11-16T10:55:00Z"
weight = 9024
keywords = [ "cache", "relations" ]
aliases = [ "/questions/9024" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Large relations slow to show - caching a solution?](/questions/9024/large-relations-slow-to-show-caching-a-solution)

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
<span id="post-9024-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9024-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-9024-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I often work with large relations (like <a href="http://www.openstreetmap.org/browse/relation/1756854">this</a>). Currently, the preview maps at <a href="http://osm.org/browse/relation/%5Bnumber%5D">osm.org/browse/relation/[number]</a> or at <a href="http://osm.org/?relation=%5Bnumber%5D">osm.org/?relation=[number]</a> load painfully slowly. Can this be solved somehow? Is it possible to cache these so they would load instantly?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-cache" rel="tag" title="see questions tagged &#39;cache&#39;">cache</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Nov '11, 07:45</strong></p>
<img src="https://secure.gravatar.com/avatar/7d327873d48d28e563c9ad7259853c35?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kozuch&#39;s gravatar image" />
<p><span>Kozuch</span><br />
<span class="score" title="1720 reputation points"><span>1.7k</span></span><span title="58 badges"><span class="badge1">●</span><span class="badgecount">58</span></span><span title="72 badges"><span class="silver">●</span><span class="badgecount">72</span></span><span title="85 badges"><span class="bronze">●</span><span class="badgecount">85</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kozuch has one accepted answer">8%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Nov '11, 09:44</strong> </span></p>
</div>
</div>
<div id="comments-container-9024" class="comments-container">
&#10;</div>
<div id="comment-tools-9024" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9024-form-container" class="comment-form-container">
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

<span id="9026"></span>

<div id="answer-container-9026" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9026-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9026-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-9026-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The preview maps use the editing API to download all objects referenced by the relation. There are several problems with that:</p>
<ul>
<li>The API is meant for <em>editing</em> not browsing; the preview maps were a nice feature when they were introduced but being ever more heavily used they start to put undue strain on the servers. The relation/full call required will often time out for complex relations.</li>
<li>Because the API is for editing, it returns much more information than strictly needed for drawing a preview map (for example, all tags and metadata like last edit date for all nodes and ways that form the relation). All this information has to be fetched from the database, put into XML form, sent over the wire, decoded by the browser, and prepared for display in OpenLayers.</li>
<li>Even the largest relations are transmitted in full resolution, which may mean tens of thousands of coordinate pairs. This is of course overkill for a small preview map.</li>
</ul>
<p>There are many ways how this could be fixed. A simple caching of the XML response would ease the strain on the database but not solve the issue of a ton of unnecessary data being transmitted to the browser. An ideal solution would probably store the relation as a pure string of coordinates, with simplified geometry, and hand that out to the browser in KML form or so. The challenge for any caching solution would be to find out when to invalidate the cache.</p>
<p>All this could easily be implemented by a third party relying on diff updates loaded from the OSM server - a kind of "fast relation viewer" service.</p>
<p>I'm sure people would appreciate if someone built such a system they could then use. As is often the case in OSM, there's no lack of good ideas, just a lack of good people to put them into practice.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Nov '11, 08:22</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-9026" class="comments-container">
<span id="9027"></span>
<div id="comment-9027" class="comment">
<div id="post-9027-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanx for a complex answer. Do you think XAPI would be faster than API?</p>
</div>
<div id="comment-9027-info" class="comment-info">
<span class="comment-age">(16 Nov '11, 09:52)</span> <span class="comment-user userinfo">Kozuch</span>
</div>
</div>
<span id="9030"></span>
<div id="comment-9030" class="comment">
<div id="post-9030-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>From reading Frederik's reply, XAPI may be a little quicker for retrieving the information, but for the best performance you wouldn't want any of the tags or version information returning - just the member nodes of any ways in the relation, and for those nodes only their longitude and latitude. Which in an optimised custom database structure is the "pure string of coordinates" Frederik also mentions above, though he goes the one step further and simplifies the geometry; eg you probably don't need full details of the Mississippi riverbank if you are zoomed out far enough to see the whole river.</p>
</div>
<div id="comment-9030-info" class="comment-info">
<span class="comment-age">(16 Nov '11, 10:40)</span> <span class="comment-user userinfo">EdLoach ♦</span>
</div>
</div>
<span id="9031"></span>
<div id="comment-9031" class="comment">
<div id="post-9031-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Well, I think full details would still be nice - I mean to show all nodes of a relation in case you zoom in... It sounds like the biggest load does all the extra data fetched, so let us cut this only.</p>
</div>
<div id="comment-9031-info" class="comment-info">
<span class="comment-age">(16 Nov '11, 10:55)</span> <span class="comment-user userinfo">Kozuch</span>
</div>
</div>
</div>
<div id="comment-tools-9026" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9026-form-container" class="comment-form-container">
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


+++
type = "question"
title = "Flat numbers vs. House Numbers vs. Mapnik on osm.org"
description = '''Hi there.  I&#x27;ve got a couple of examples now where I think I&#x27;ve tagged things correctly; but the rendered view on osm.org is so weird it&#x27;s made me wonder. Am I doing it wrong; or is the renderer doing something unhelpful? There&#x27;s a new housing development - Walter Hancock Court, the entire building ...'''
date = "2019-02-11T11:48:00Z"
lastmod = "2019-02-12T00:15:00Z"
weight = 67965
keywords = [ "osm.org", "addressing", "addrhousenumber", "addrflats", "addrhousename" ]
aliases = [ "/questions/67965" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Flat numbers vs. House Numbers vs. Mapnik on osm.org](/questions/67965/flat-numbers-vs-house-numbers-vs-mapnik-on-osmorg)

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
<span id="post-67965-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67965-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-67965-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi there.</p>
<p>I've got a couple of examples now where I think I've tagged things correctly; but the rendered view on osm.org is so weird it's made me wonder. Am I doing it wrong; or is the renderer doing something unhelpful?</p>
<p>There's a new housing development - Walter Hancock Court, the entire building is at 1 McGrath Road. It has 26 flats. So I've tagged each flat with a node as follows:</p>
<ul>
<li>addr:flats=14 (etc.)</li>
<li>addr:housename=Walter Hancock Court</li>
<li>addr:housenumber=1</li>
<li>addr:street=McGrath Road</li>
<li>entrance=home</li>
</ul>
<p>(See changeset <a href="https://www.openstreetmap.org/changeset/67097020">https://www.openstreetmap.org/changeset/67097020</a> )</p>
<p>But osm.org shows all the entrances as "1 Walter Hancock Court". There's another example nearby at Granite Apartments, where all of the 100+ apartments render as 39 Granite Apartments. 39 is the housenumber of the entire block. (see <a href="https://osm.org/go/0EEQVYTyt?m=&amp;changeset=67097020">https://osm.org/go/0EEQVYTyt?m=&amp;changeset=67097020</a> )</p>
<p>Should I be tagging these differently, or reporting an issue to the mapnik maintainers?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm.org" rel="tag" title="see questions tagged &#39;osm.org&#39;">osm.org</span> <span class="post-tag tag-link-addressing" rel="tag" title="see questions tagged &#39;addressing&#39;">addressing</span> <span class="post-tag tag-link-addrhousenumber" rel="tag" title="see questions tagged &#39;addrhousenumber&#39;">addrhousenumber</span> <span class="post-tag tag-link-addrflats" rel="tag" title="see questions tagged &#39;addrflats&#39;">addrflats</span> <span class="post-tag tag-link-addrhousename" rel="tag" title="see questions tagged &#39;addrhousename&#39;">addrhousename</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Feb '19, 11:48</strong></p>
<img src="https://secure.gravatar.com/avatar/b5c5070032df7883181003f187eacae0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="spiregrain&#39;s gravatar image" />
<p><span>spiregrain</span><br />
<span class="score" title="183 reputation points">183</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="spiregrain has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Feb '19, 11:50</strong> </span></p>
</div>
</div>
<div id="comments-container-67965" class="comments-container">
&#10;</div>
<div id="comment-tools-67965" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67965-form-container" class="comment-form-container">
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

<span id="67971"></span>

<div id="answer-container-67971" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67971-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67971-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-67971-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The default style on OSM.org is called OSM Carto, Mapnik is just an engine this (and some other) style uses.</p>
<p>The problem you have just described has a separate ticket in OSM Carto bug tracker, if you need to discuss it further, please do it there:</p>
<p><a href="https://github.com/gravitystorm/openstreetmap-carto/issues/264">https://github.com/gravitystorm/openstreetmap-carto/issues/264</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Feb '19, 00:15</strong></p>
<img src="https://secure.gravatar.com/avatar/e228dd20b7da2a6c8f559e2118ce08d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kocio&#39;s gravatar image" />
<p><span>kocio</span><br />
<span class="score" title="2054 reputation points"><span>2.1k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kocio has 14 accepted answers">20%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Feb '19, 00:31</strong> </span></p>
</div>
</div>
<div id="comments-container-67971" class="comments-container">
&#10;</div>
<div id="comment-tools-67971" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67971-form-container" class="comment-form-container">
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


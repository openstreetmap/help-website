+++
type = "question"
title = "How to download a relation with the tidy elements?"
description = '''I am trying to download a bus route. I want to obtain the elements that compose this relation of a tidy way, as they appear originally in the relation.  https://www.openstreetmap.org/api/0.6/relation/3723432  But when I download the route in the osm resulting file the ways are not ordered. This compl...'''
date = "2014-05-08T12:29:00Z"
lastmod = "2014-05-11T12:26:00Z"
weight = 32980
keywords = [ "ways", "route", "api", "relation", "order" ]
aliases = [ "/questions/32980" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to download a relation with the tidy elements?](/questions/32980/how-to-download-a-relation-with-the-tidy-elements)

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
<span id="post-32980-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32980-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-32980-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to download a bus route. I want to obtain the elements that compose this relation of a tidy way, as they appear originally in the relation.</p>
<p><img src="/upfiles/Seleccion_023.png" alt="alt text" /></p>
<p><a href="https://www.openstreetmap.org/api/0.6/relation/3723432">https://www.openstreetmap.org/api/0.6/relation/3723432</a></p>
<p>But when I download the route in the osm resulting file the ways are not ordered. This complicates the analysis that I want to realize in a Geographic Information System (I need to extract the nodes that the route form of a correlative way, from beginning to end).</p>
<p><a href="https://www.openstreetmap.org/api/0.6/relation/3723432/full">https://www.openstreetmap.org/api/0.6/relation/3723432/full</a></p>
<p><strong>Is there any mode to get the real order of the ways of a route?</strong> Also it serves me in the worst case some way to identify the position of each arc.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span> <span class="post-tag tag-link-route" rel="tag" title="see questions tagged &#39;route&#39;">route</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-relation" rel="tag" title="see questions tagged &#39;relation&#39;">relation</span> <span class="post-tag tag-link-order" rel="tag" title="see questions tagged &#39;order&#39;">order</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 May '14, 12:29</strong></p>
<img src="https://secure.gravatar.com/avatar/c92dc509ff73f8cd596c5ca0a6a33d18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="egofer&#39;s gravatar image" />
<p><span>egofer</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="egofer has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-32980" class="comments-container">
&#10;</div>
<div id="comment-tools-32980" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32980-form-container" class="comment-form-container">
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

<span id="33083"></span>

<div id="answer-container-33083" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-33083-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33083-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-33083-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The file that you get when downloading the relation contains one <code>relation</code> element, several <code>way</code> elements, and several <code>node</code> elements. The <code>relation</code> element will contain references to the ways, in the right order - like</p>
<pre><code>&lt;member type=&quot;way&quot; ref=&quot;123&quot; /&gt;
&lt;member type=&quot;way&quot; ref=&quot;555&quot; /&gt;</code></pre>
<p>and so on. You will then have to extract the way elements from the file in this order, and the ways will in turn reference the nodes which again, you have to extract in the order given in the way.</p>
<p>This is something that will require just a few lines of code in a programming language of your choice. OSM itself doesn't provide a service that does this job for you. But you might want to check out the answers to <a href="/questions/18295/export-a-way-as-a-gpx">"Export a way as GPX"</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 May '14, 12:26</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-33083" class="comments-container">
&#10;</div>
<div id="comment-tools-33083" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33083-form-container" class="comment-form-container">
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


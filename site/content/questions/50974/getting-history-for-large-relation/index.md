+++
type = "question"
title = "getting history for large relation"
description = '''Hi, I need to find the original creator of a large relation. But osm.org always times out and OSM history viewer returns an error. Is there any other way to get the past editors of this object? (Context: this relation is part of the E2 walking path, but this part is identical with GR5 Vlaanderen, re...'''
date = "2016-07-19T08:14:00Z"
lastmod = "2016-07-19T09:26:00Z"
weight = 50974
keywords = [ "relations", "history" ]
aliases = [ "/questions/50974" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [getting history for large relation](/questions/50974/getting-history-for-large-relation)

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
<span id="post-50974-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50974-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-50974-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I need to find the original creator of <a href="https://www.openstreetmap.org/relation/3228572">a large relation</a>. But osm.org always times out and <a href="http://osmhv.openstreetmap.de/">OSM history viewer</a> returns an error. Is there any other way to get the past editors of this object?</p>
<p>(Context: this relation is part of the E2 walking path, but this part is identical with GR5 Vlaanderen, relation 3121667. So it would seem more logical to only map it once, and have relation 3228572 only contain the relation making GR5. But maybe there is some unknown reason they do need to be duplicated - and I'd like to ask the original creator about that)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span> <span class="post-tag tag-link-history" rel="tag" title="see questions tagged &#39;history&#39;">history</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Jul '16, 08:14</strong></p>
<img src="https://secure.gravatar.com/avatar/1df835d513b1282e0edd7405d29cd8d9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joost%20schouppe&#39;s gravatar image" />
<p><span>joost schouppe</span><br />
<span class="score" title="3427 reputation points"><span>3.4k</span></span><span title="24 badges"><span class="badge1">●</span><span class="badgecount">24</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="87 badges"><span class="bronze">●</span><span class="badgecount">87</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joost schouppe has 9 accepted answers">12%</span></p>
</div>
</div>
<div id="comments-container-50974" class="comments-container">
&#10;</div>
<div id="comment-tools-50974" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50974-form-container" class="comment-form-container">
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

<span id="50975"></span>

<div id="answer-container-50975" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-50975-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50975-score" class="post-score" title="current number of votes">
7
</div>
<span id="post-50975-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="joost schouppe has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are several approaches:</p>
<ul>
<li>Download a specific version yourself: Just use <a href="https://www.openstreetmap.org/api/0.6/relation/3228572/1">https://www.openstreetmap.org/api/0.6/relation/3228572/1</a> to download the first version of this relation. You can also directly access <a href="https://www.openstreetmap.org/api/0.6/relation/3228572">relation 3228572</a> to view the current version (currently 136) and then use <a href="https://www.openstreetmap.org/api/0.6/relation/3228572/135">https://www.openstreetmap.org/api/0.6/relation/3228572/135</a> to download the previous version.</li>
<li>Use JOSM to view the history. JOSM has no problems showing the history or individual versions of this relation. You can download the relation either using <em>File -&gt; Download object</em> and passing the relation ID or using <em>File -&gt; Open Location</em> and passing the URL to the relation. Then select the relation and go to <em>View -&gt; History</em> (Ctrl-H).</li>
<li>Download the history yourself: <a href="https://api.openstreetmap.org/api/0.6/relation/3228572/history.">https://api.openstreetmap.org/api/0.6/relation/3228572/history.</a> Beware, this file is large (&gt; 7 MB) and will likely make your system unusable if you try to view it in your browser and don't have enough RAM.</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Jul '16, 08:52</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Jul '16, 09:00</strong> </span></p>
</div>
</div>
<div id="comments-container-50975" class="comments-container">
<span id="50976"></span>
<div id="comment-50976" class="comment">
<div id="post-50976-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for this nice overview!</p>
</div>
<div id="comment-50976-info" class="comment-info">
<span class="comment-age">(19 Jul '16, 09:01)</span> <span class="comment-user userinfo">joost schouppe</span>
</div>
</div>
</div>
<div id="comment-tools-50975" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50975-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="50977"></span>

<div id="answer-container-50977" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-50977-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50977-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-50977-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>TL;DR: <code>geozeisig</code> is the user you are looking for (or at least, created version 1 of this relation).</p>
<ul>
<li>I have launched JOSM as <code>java -jar josm-latest.jar --debug</code> to capture the requests as they go across the network</li>
<li>downloaded the relation through File-Download Object,</li>
<li>selected and tried to load history.</li>
<li>JOSM timed out waiting for API to respond - but at least I got the URL from the exception: <a href="https://api.openstreetmap.org/api/0.6/relation/3228572/history">https://api.openstreetmap.org/api/0.6/relation/3228572/history</a></li>
<li>Downloaded that: <code>wget -O 3228572.osm </code><a href="https://api.openstreetmap.org/api/0.6/relation/3228572/history"><code>https://api.openstreetmap.org/api/0.6/relation/3228572/history</code></a></li>
<li><p>listed out the relation versions with <code>grep relation &lt; 3228572.osm</code>. First result:</p>
<p>relation id="3228572" changeset="18039456" timestamp="2013-09-26T06:28:02Z" version="1" visible="true" user="geozeisig" uid="66391"</p></li>
</ul>
<p>Here's a copy of the entire (7 MB) file as of today: <a href="http://osm.piskvor.org/3228572.osm">http://osm.piskvor.org/3228572.osm</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Jul '16, 09:26</strong></p>
<img src="https://secure.gravatar.com/avatar/8200fa5c0cc8feb096558c5972a6191c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Piskvor&#39;s gravatar image" />
<p><span>Piskvor</span><br />
<span class="score" title="1266 reputation points"><span>1.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="35 badges"><span class="bronze">●</span><span class="badgecount">35</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Piskvor has 9 accepted answers">37%</span></p>
</div>
</div>
<div id="comments-container-50977" class="comments-container">
&#10;</div>
<div id="comment-tools-50977" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50977-form-container" class="comment-form-container">
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


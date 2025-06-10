+++
type = "question"
title = "Import OSM Relation into Umap"
description = '''I&#x27;m trying to use OSM and UMap to create a custom map showing my organization&#x27;s region/territory. It&#x27;s described as a list of US Counties, plus an additional fixed distance beyond those counties. Ideally each county would show as its boundary, and then I could create lines for the additional distanc...'''
date = "2022-02-08T17:14:00Z"
lastmod = "2022-02-10T06:46:00Z"
weight = 83413
keywords = [ "umap", "osm", "import" ]
aliases = [ "/questions/83413" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Import OSM Relation into Umap](/questions/83413/import-osm-relation-into-umap)

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
<span id="post-83413-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83413-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-83413-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to use OSM and UMap to create a custom map showing my organization's region/territory. It's described as a list of US Counties, plus an additional fixed distance beyond those counties. Ideally each county would show as its boundary, and then I could create lines for the additional distance.</p>
<p>When I search in OSM for one of the counties (DuPage County), I get precisely what I'd like : <a href="https://www.openstreetmap.org/relation/1800060">https://www.openstreetmap.org/relation/1800060</a> . When I search for the same county in uMap, I just get a point marker at the city which contains the county seat of government. I don't see any way to bring up an associated boundary.</p>
<p>All my attempts to import data from OSM, in order to show county boundaries, have failed.</p>
<p>I'm probably in over my head trying to do this, but any hints would be appreciated.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-umap" rel="tag" title="see questions tagged &#39;umap&#39;">umap</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Feb '22, 17:14</strong></p>
<img src="https://secure.gravatar.com/avatar/876414122b45c9013a136c676465fc0f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Greater%20Chicago%20IWW&#39;s gravatar image" />
<p><span>Greater Chic...</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Greater Chicago IWW has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-83413" class="comments-container">
&#10;</div>
<div id="comment-tools-83413" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83413-form-container" class="comment-form-container">
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

<span id="83416"></span>

<div id="answer-container-83416" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83416-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83416-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-83416-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Greater Chicago IWW has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Search in uMap is fairly basic, and will give only markers.</p>
<p>But you can import linear data in two ways :</p>
<ol>
<li><a href="https://wiki.openstreetmap.org/wiki/UMap/Guide/Import_data_with_Overpass">Dynamically load data through overpass</a></li>
<li>Download your data otherwise, and import it once.</li>
</ol>
<p>In your case, as the data should never change, I would go on solution 2, to reduce the load on the servers.</p>
<p>Here are the details :</p>
<ol>
<li>Got to overpass-turbo, to build a query like <a href="http://overpass-turbo.eu/?Q=%5Bout%3Ajson%5D%5Btimeout%3A25%5D%3B%20%0A(%20%0A%20%20rel(1800060)%3B%0A)%3B%0A%0Aout%20body%3B%0A%3E%3B%0Aout%20skel%20qt%3B%0A&amp;C=41.83973;-88.08857;11">this one</a></li>
<li>I put only the county you cited, but you can add as many as you want with more <code>rel(#county_id);</code> in the parenthesizes, they create a union.</li>
<li>Then click Run, to check that it's what you want.</li>
<li>Click Export, then download (GPX is a fairly standard format, others are possible).</li>
<li>In uMap, click on the up arrow, in the right menu <img src="https://wiki.openstreetmap.org/w/images/5/5e/Icon-upload.png" alt="import data" /> (see this <a href="https://wiki.openstreetmap.org/wiki/UMap/Guide/Import_data_files">guide</a> for details), choose your file, the same format as when downloading, a new layer...</li>
<li>And click import !</li>
<li>Then you can change the settings of the layer, one useful with this kind of data is in "Advanced properties", "simplify", it will make displaying at lower zoom faster.</li>
</ol>
<p>Hope this helps, please ask if you need more assistance.</p>
<p>Regards.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Feb '22, 19:21</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</img>
</div>
</div>
<div id="comments-container-83416" class="comments-container">
<span id="83437"></span>
<div id="comment-83437" class="comment">
<div id="post-83437-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks for the well crafted answer H_mlet. Overpass-turbo really like a Rosetta Stone for my mapping needs.</p>
<p>Here's what I was able to get done in short order after your answer:</p>
<p><a href="http://u.osmfr.org/m/715212/">http://u.osmfr.org/m/715212/</a></p>
</div>
<div id="comment-83437-info" class="comment-info">
<span class="comment-age">(10 Feb '22, 00:41)</span> <span class="comment-user userinfo">Greater Chic...</span>
</div>
</div>
<span id="83438"></span>
<div id="comment-83438" class="comment">
<div id="post-83438-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Yeah, uMap is pretty neat. Sometime a bit quirky, and sadly unmaintained, but still great!</p>
</div>
<div id="comment-83438-info" class="comment-info">
<span class="comment-age">(10 Feb '22, 06:46)</span> <span class="comment-user userinfo">H_mlet</span>
</div>
</div>
</div>
<div id="comment-tools-83416" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83416-form-container" class="comment-form-container">
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


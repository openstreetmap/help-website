+++
type = "question"
title = "Creating Custom maps?"
description = '''Hi all Apologies if this appears to be a stupid question, but OSM is rather daunting when trying to find a place to start. I have a college project where I am looking to create a visualization of an area from the 1980&#x27;s. -I was hoping to use OSM&#x27;s xml data as my base  -Read this data into an editor ...'''
date = "2011-07-27T15:58:00Z"
lastmod = "2011-07-27T17:40:00Z"
weight = 6618
keywords = [ "mapping" ]
aliases = [ "/questions/6618" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Creating Custom maps?](/questions/6618/creating-custom-maps)

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
<span id="post-6618-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6618-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-6618-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all</p>
<p>Apologies if this appears to be a stupid question, but OSM is rather daunting when trying to find a place to start.</p>
<p>I have a college project where I am looking to create a visualization of an area from the 1980's.</p>
<p>-I was hoping to use OSM's xml data as my base</p>
<p>-Read this data into an editor (not sure if it will be <a href="http://esriosmeditor.codeplex.com/">http://esriosmeditor.codeplex.com/</a> or <a href="https://wiki.openstreetmap.org/wiki/JOSM/Guide)">https://wiki.openstreetmap.org/wiki/JOSM/Guide)</a></p>
<p>-Overlay Aerial ordinance survey images and adjust the map</p>
<p>-Export the xml data</p>
<p>-Import into CITY Engine and Generate the visualization.</p>
<p>This is the plan, but I am running into complications.</p>
<ol>
<li><p>I need to do the visualization on key locations in western europe. So exporting the XML from the site would be too time consuming, I was looking at downloading the global map just once and editing it directly? Advice on the best approach here would be great as it would save me considerable time learning the hard way.</p></li>
<li><p>Is it possible to overlay reference images in ARCGis or JOSM</p></li>
<li><p>Assuming i am able to do 1 &amp; 2. I would then hope to export the XML data in 2000m x 2000m blocks. So as to create the visualizations in CityEngine.</p></li>
</ol>
<p>Any general tips would be greatly appreciated and again apologies if this all seems a little simple and dumb, finding where to start this project is proving the most difficult aspect at times.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mapping" rel="tag" title="see questions tagged &#39;mapping&#39;">mapping</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Jul '11, 15:58</strong></p>
<img src="https://secure.gravatar.com/avatar/fd0a3666813d51f4c203b11640370c94?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BatmansDad&#39;s gravatar image" />
<p><span>BatmansDad</span><br />
<span class="score" title="15 reputation points">15</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BatmansDad has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-6618" class="comments-container">
&#10;</div>
<div id="comment-tools-6618" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6618-form-container" class="comment-form-container">
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

<span id="6627"></span>

<div id="answer-container-6627" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-6627-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6627-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-6627-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<ol>
<li><p>You can also get smaller, non-global extracts from other sources like <a href="http://www.geofabrik.de/en/data/download.html1.">geofabrik</a>. You shouldn't really try to get them from the main API whose use is restricted to mapping. Alternatively you can try your luck with one of the XAPIs (mapquest seems to be performant).</p></li>
<li><p>yes (technically, regardless license/copyright questions)</p></li>
</ol>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Jul '11, 17:40</strong></p>
<img src="https://secure.gravatar.com/avatar/f09c0b7a655fed386e070e036e2da248?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dieterdreist&#39;s gravatar image" />
<p><span>dieterdreist</span><br />
<span class="score" title="3677 reputation points"><span>3.7k</span></span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="67 badges"><span class="bronze">●</span><span class="badgecount">67</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dieterdreist has 4 accepted answers">3%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Jul '11, 17:42</strong> </span></p>
</div>
</div>
<div id="comments-container-6627" class="comments-container">
&#10;</div>
<div id="comment-tools-6627" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6627-form-container" class="comment-form-container">
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


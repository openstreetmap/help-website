+++
type = "question"
title = "Can&#x27;t get street names rendered"
description = '''Hello, I am trying to generate a map, which consists only of street names (none of the other features are rendered), and hoped to be able to apply osmrender, which comes with some example stylesheets. In this regard, I would greatly appreciate some discussion about the following. Is there a compendi...'''
date = "2012-03-07T11:45:00Z"
lastmod = "2012-03-13T03:03:00Z"
weight = 11037
keywords = [ "osm", "osmarender" ]
aliases = [ "/questions/11037" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Can't get street names rendered](/questions/11037/cant-get-street-names-rendered)

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
<span id="post-11037-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11037-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-11037-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I am trying to generate a map, which consists only of street names (none of the other features are rendered), and hoped to be able to apply osmrender, which comes with some example stylesheets. In this regard, I would greatly appreciate some discussion about the following.</p>
<p>Is there a compendium of the osmarender stylesheets, if yes, is there a description of what every stylesheet does, which stylesheet would be a good starting point for my purpose? At this point I can't seem to find a style sheet that would simply NOT omit the street names: for example, when I execute "java -cp xalan-j_2_7_1/xalan.jar org.apache.xalan.xslt.Process -in osmarender/stylesheets/osm-map-features-z17.xml -out map.svg" on the Manhattan's data.osm file, i get the map, but no street names (I need the opposite) -- at least looking at the svg file in Chrome or Adobe Illustrator. Other osmarender stylesheets produce errors.</p>
<p>Thanks in advance.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-osmarender" rel="tag" title="see questions tagged &#39;osmarender&#39;">osmarender</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Mar '12, 11:45</strong></p>
<img src="https://secure.gravatar.com/avatar/423ccc2d9d0c0d9cf1dfbfaf3f4337b2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="eight&#39;s gravatar image" />
<p><span>eight</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="eight has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Mar '12, 16:41</strong> </span></p>
</div>
</div>
<div id="comments-container-11037" class="comments-container">
<span id="11045"></span>
<div id="comment-11045" class="comment">
<div id="post-11045-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>40 something views and no answer.</p>
<p>Is this question out of this world? Why? Is the answer too obvious? Where do I read more about it?</p>
<p>--</p>
</div>
<div id="comment-11045-info" class="comment-info">
<span class="comment-age">(07 Mar '12, 21:29)</span> <span class="comment-user userinfo">eight</span>
</div>
</div>
<span id="11055"></span>
<div id="comment-11055" class="comment">
<div id="post-11055-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I cannot give you a hint for your concrete question, but if you cannot get any answer here, ask also at the OSM forum or one of the OSM mailing lists.</p>
</div>
<div id="comment-11055-info" class="comment-info">
<span class="comment-age">(08 Mar '12, 14:17)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
<span id="11058"></span>
<div id="comment-11058" class="comment">
<div id="post-11058-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Also specify if you really want streets names only or if you expect some lines or vectors for the street themselves (or just 'floating text')</p>
</div>
<div id="comment-11058-info" class="comment-info">
<span class="comment-age">(08 Mar '12, 15:28)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
<span id="11059"></span>
<div id="comment-11059" class="comment">
<div id="post-11059-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I may be interested in both: street names as a "text floating in space" or street names along some lines or vectors -- depending on what looks better.</p>
</div>
<div id="comment-11059-info" class="comment-info">
<span class="comment-age">(08 Mar '12, 15:51)</span> <span class="comment-user userinfo">eight</span>
</div>
</div>
</div>
<div id="comment-tools-11037" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11037-form-container" class="comment-form-container">
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

<span id="11153"></span>

<div id="answer-container-11153" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11153-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11153-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-11153-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I switched from xalan parser to xmlstarlet and rules started functioning as expected. Bad xalan!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Mar '12, 03:03</strong></p>
<img src="https://secure.gravatar.com/avatar/423ccc2d9d0c0d9cf1dfbfaf3f4337b2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="eight&#39;s gravatar image" />
<p><span>eight</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="eight has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-11153" class="comments-container">
&#10;</div>
<div id="comment-tools-11153" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11153-form-container" class="comment-form-container">
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


+++
type = "question"
title = "How do I embed a map in a CMS-based web site?"
description = '''I recently wrote an extension* for PunBB as I wanted an alternative option to Google Maps and very much liked the feel of OSM. However when I create a post A with an embeded map section XYZ with fixed longitude X1 and latitude Y2 I encounter unexpected behaviour after visiting OTHERS, ADDITIONAL pos...'''
date = "2012-01-05T08:22:00Z"
lastmod = "2012-01-12T02:59:00Z"
weight = 9811
keywords = [ "embed", "export", "slippymap" ]
aliases = [ "/questions/9811" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How do I embed a map in a CMS-based web site?](/questions/9811/how-do-i-embed-a-map-in-a-cms-based-web-site)

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
<span id="post-9811-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9811-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-9811-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I recently wrote an extension* for PunBB as I wanted an alternative option to Google Maps and very much liked the feel of OSM.</p>
<p>However when I create a post A with an embeded map section XYZ with fixed longitude X1 and latitude Y2 I encounter unexpected behaviour after visiting OTHERS, ADDITIONAL posts with other map sections with lon:X2 lat:Y3. The unexpected behaviour: The map shows whatever map section I was last browsing. Why?</p>
<p>Thanks for any ideas... * (<a href="http://punbb.informer.com/forums/topic/24786/extension-open-street-map/)">http://punbb.informer.com/forums/topic/24786/extension-open-street-map/)</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-embed" rel="tag" title="see questions tagged &#39;embed&#39;">embed</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-slippymap" rel="tag" title="see questions tagged &#39;slippymap&#39;">slippymap</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Jan '12, 08:22</strong></p>
<img src="https://secure.gravatar.com/avatar/bda13d177be7a41a7390466d4ef82e6f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KeyDog&#39;s gravatar image" />
<p><span>KeyDog</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KeyDog has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Jan '12, 09:39</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/9fe361843971cf8b23dc93517f00b996?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jonathan%20Bennett&#39;s gravatar image" />
<p><span>Jonathan Ben...</span><br />
<span class="score" title="8261 reputation points"><span>8.3k</span></span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="85 badges"><span class="silver">●</span><span class="badgecount">85</span></span><span title="108 badges"><span class="bronze">●</span><span class="badgecount">108</span></span></p>
</div>
</div>
<div id="comments-container-9811" class="comments-container">
&#10;</div>
<div id="comment-tools-9811" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9811-form-container" class="comment-form-container">
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

<span id="9814"></span>

<div id="answer-container-9814" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9814-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9814-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-9814-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Your extension doesn't embed a map - it embeds the whole of <a href="http://openstreetmap.org">openstreetmap.org</a> in an iframe. This isn't the correct way to include an OpenStreetMap-based map on a web page. Please use the <a href="https://wiki.openstreetmap.org/wiki/Export_tab">Export feature</a> or include your <a href="https://wiki.openstreetmap.org/wiki/Deploying_your_own_Slippy_Map">own slippy map using OpenLayers</a> to display a map.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Jan '12, 09:36</strong></p>
<img src="https://secure.gravatar.com/avatar/9fe361843971cf8b23dc93517f00b996?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jonathan%20Bennett&#39;s gravatar image" />
<p><span>Jonathan Ben...</span><br />
<span class="score" title="8261 reputation points"><span>8.3k</span></span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="85 badges"><span class="silver">●</span><span class="badgecount">85</span></span><span title="108 badges"><span class="bronze">●</span><span class="badgecount">108</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jonathan Bennett has 21 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-9814" class="comments-container">
&#10;</div>
<div id="comment-tools-9814" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9814-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="9908"></span>

<div id="answer-container-9908" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9908-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9908-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-9908-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is a good starting point for the question you are asking. Several examples already out there...</p>
<p><a href="https://wiki.openstreetmap.org/wiki/Deploying_your_own_Slippy_Map">https://wiki.openstreetmap.org/wiki/Deploying_your_own_Slippy_Map</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Jan '12, 02:59</strong></p>
<img src="https://secure.gravatar.com/avatar/167b15c0b88e15fe2c5907f9c699dd9c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20F&#39;s gravatar image" />
<p><span>Andy F</span><br />
<span class="score" title="46 reputation points">46</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andy F has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-9908" class="comments-container">
&#10;</div>
<div id="comment-tools-9908" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9908-form-container" class="comment-form-container">
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


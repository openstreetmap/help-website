+++
type = "question"
title = "Export osm map in embedded html"
description = '''Hi I&#x27;m implementing a webpage that embedded an openstreetmap map. I want to let the user select an area and export it to osm file from my webpage. Is this feasible ??'''
date = "2014-02-11T20:23:00Z"
lastmod = "2014-02-12T13:47:00Z"
weight = 30657
keywords = [ "development", "export" ]
aliases = [ "/questions/30657" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Export osm map in embedded html](/questions/30657/export-osm-map-in-embedded-html)

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
<span id="post-30657-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30657-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-30657-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi</p>
<p>I'm implementing a webpage that embedded an openstreetmap map. I want to let the user select an area and export it to osm file from my webpage. Is this feasible ??</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Feb '14, 20:23</strong></p>
<img src="https://secure.gravatar.com/avatar/4c26fa61e4166cbfaf01b3107e39833d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nour%20K&#39;s gravatar image" />
<p><span>Nour K</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nour K has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Feb '14, 01:05</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-30657" class="comments-container">
&#10;</div>
<div id="comment-tools-30657" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30657-form-container" class="comment-form-container">
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

<span id="30663"></span>

<div id="answer-container-30663" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-30663-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30663-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-30663-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Likely it is. You just need to extract the bounding box of the selection and then pass it to the <span>OSM API</span> (please, this way only if you have a low traffic, private webpage and it only works for small areas).</p>
<p>It may be useful to know which map library you are using (e.g. OpenLayers or Leaflet) or if you do not care. Probably the selection part is the harder part of your idea.</p>
<p>For OpenLayers <a href="http://trac.osgeo.org/openlayers/wiki/FrequentlyAskedQuestions#HowdoIgettheLonLatfromapixelorfromthecurrentpositionofthemouse">this FAQ entry</a> might help. You might also want to have a look at <span>www.osm.org</span> which does such a selection (uses Leaflet).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Feb '14, 01:09</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Feb '14, 13:48</strong> </span></p>
</div>
</div>
<div id="comments-container-30663" class="comments-container">
<span id="30677"></span>
<div id="comment-30677" class="comment">
<div id="post-30677-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>So it is feasible!! Thanks a lot. That's true the selection is the harder part. I'm using OpenLayers as my map library. I have succeed to embed the openstreetmap map into my webpage but I don't have any idea yet on how to implement the selection of an area from this map and the extraction of the bounding box of the selected area.</p>
</div>
<div id="comment-30677-info" class="comment-info">
<span class="comment-age">(12 Feb '14, 11:13)</span> <span class="comment-user userinfo">Nour K</span>
</div>
</div>
<span id="30683"></span>
<div id="comment-30683" class="comment">
<div id="post-30683-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I would suggest to make the pure "rectangular selection in OpenLayers by user" (for example by a box drawn by the user's mouse) question a new question as it is not specific to your export thing afterwards. And, maybe an OpenLayers forum (instead of this help site) would be more useful as it is not specific to OSM anymore. However, many <span>OpenLayers questions are on this help site</span> despite that.</p>
</div>
<div id="comment-30683-info" class="comment-info">
<span class="comment-age">(12 Feb '14, 13:47)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-30663" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30663-form-container" class="comment-form-container">
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


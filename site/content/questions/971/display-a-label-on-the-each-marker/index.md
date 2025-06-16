+++
type = "question"
title = "Display a label on the each marker"
description = '''Hi, Is we do&#x27;t have facility to add labels which will show some information of markers on page load load itself. like on page load of map I want to show image with one label, and the label will contain the same information what we have now in popup. I do&#x27;t want popup meassage I want label near by ma...'''
date = "2010-09-30T22:16:00Z"
lastmod = "2010-10-01T22:52:00Z"
weight = 971
keywords = [ "display" ]
aliases = [ "/questions/971" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Display a label on the each marker](/questions/971/display-a-label-on-the-each-marker)

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
<span id="post-971-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-971-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-971-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>Is we do't have facility to add labels which will show some information of markers on page load load itself.</p>
<p>like on page load of map I want to show image with one label, and the label will contain the same information what we have now in popup.</p>
<p>I do't want popup meassage I want label near by marker which will show the image information. I am giving one example <a href="http://econym.org.uk/gmap/example_elabel.htm">http://econym.org.uk/gmap/example_elabel.htm</a> here.</p>
<p>As in above example you can see one label is coming on page load of map which is providing information of the image.</p>
<p>the same above thing i want ot implement in open street map is that is possible?</p>
<p>Please provide me some example if you have.</p>
<p>thanks for your time and support.</p>
<p>Vivek</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-display" rel="tag" title="see questions tagged &#39;display&#39;">display</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Sep '10, 22:16</strong></p>
<img src="https://secure.gravatar.com/avatar/af488a6cddd21b91f3f2bee3c2e842e6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vivek%20Kumar&#39;s gravatar image" />
<p><span>Vivek Kumar</span><br />
<span class="score" title="15 reputation points">15</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vivek Kumar has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Oct '10, 19:22</strong> </span></p>
</div>
</div>
<div id="comments-container-971" class="comments-container">
&#10;</div>
<div id="comment-tools-971" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-971-form-container" class="comment-form-container">
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

<span id="980"></span>

<div id="answer-container-980" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-980-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-980-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-980-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It would help if you provided some more details of what you want to do. ie Do you want a map on your own website? And what do you mean by markers? Places in OSM, or some other waypoints?</p>
<p>The best option is probably to use <a href="https://wiki.openstreetmap.org/wiki/OpenLayers">OpenLayers</a>. This lets you show an OSM map, with markers overlaid, and popups when you click on them. There is a simple example of this here: <a href="https://wiki.openstreetmap.org/wiki/Openlayers_POI_layer_example">Openlayers POI layer example</a>. This needs the markers in a tab separated text file, so you will have to convert your markers to that format.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Oct '10, 16:05</strong></p>
<img src="https://secure.gravatar.com/avatar/aa505c046b1c010e997a7849c6f3dbbe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vclaw&#39;s gravatar image" />
<p><span>Vclaw</span><br />
<span class="score" title="9217 reputation points"><span>9.2k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="95 badges"><span class="silver">●</span><span class="badgecount">95</span></span><span title="141 badges"><span class="bronze">●</span><span class="badgecount">141</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vclaw has 41 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-980" class="comments-container">
<span id="984"></span>
<div id="comment-984" class="comment">
<div id="post-984-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>you've created a new answer instead of commenting on Vclaws answer. If you want to add a comment press "add new comment" beside the answer instead of using the form at the bottom of the page saying "your answer"</p>
</div>
<div id="comment-984-info" class="comment-info">
<span class="comment-age">(01 Oct '10, 18:30)</span> <span class="comment-user userinfo">Andy Allan</span>
</div>
</div>
</div>
<div id="comment-tools-980" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-980-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="993"></span>

<div id="answer-container-993" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-993-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-993-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-993-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes, you can show labels on the map in OpenLayers. See this example here: <a href="http://openlayers.org/dev/examples/vector-features-with-text.html">OpenLayers Labeled features example</a>. It shouldn't be too hard to modify that to show an OSM map instead, and change the markers and labels to what you want. You can probably find more details in the <a href="http://docs.openlayers.org/">OpenLayers Documentation</a></p>
<p>Alternatively, it is possible to show OSM maps in the Google Maps API. See <a href="https://wiki.openstreetmap.org/wiki/Google_Maps_Example">Google Maps example</a>. So you could modify that example map that you linked, to use OSM maps instead of Google.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Oct '10, 22:52</strong></p>
<img src="https://secure.gravatar.com/avatar/aa505c046b1c010e997a7849c6f3dbbe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vclaw&#39;s gravatar image" />
<p><span>Vclaw</span><br />
<span class="score" title="9217 reputation points"><span>9.2k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="95 badges"><span class="silver">●</span><span class="badgecount">95</span></span><span title="141 badges"><span class="bronze">●</span><span class="badgecount">141</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vclaw has 41 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-993" class="comments-container">
&#10;</div>
<div id="comment-tools-993" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-993-form-container" class="comment-form-container">
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


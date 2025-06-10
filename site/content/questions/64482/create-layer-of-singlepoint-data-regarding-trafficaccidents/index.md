+++
type = "question"
title = "create layer of singlepoint data regarding trafficaccidents"
description = '''Hi! I&#x27;ve got a fine extensive set of plain data about trafficaccidents and their respective GPS coords. What I&#x27;m doing is slurping it in an PERL HoH. Ultimate goal would be to make that data visuably in a way so that it is displayed in form of a map. Now I&#x27;m puzzling around with that issue cause it&#x27;...'''
date = "2018-07-02T18:02:00Z"
lastmod = "2018-07-04T22:09:00Z"
weight = 64482
keywords = [ "data", "singlepoint", "trafficaccident" ]
aliases = [ "/questions/64482" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [create layer of singlepoint data regarding trafficaccidents](/questions/64482/create-layer-of-singlepoint-data-regarding-trafficaccidents)

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
<span id="post-64482-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64482-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-64482-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi!</p>
<p>I've got a fine extensive set of plain data about trafficaccidents and their respective GPS coords. What I'm doing is slurping it in an PERL HoH. Ultimate goal would be to make that data visuably in a way so that it is displayed in form of a map. Now I'm puzzling around with that issue cause it's all about public accessibility.</p>
<p>Am I right in assuming that my best way to go for would be to parse the data into an OSMreadable .xml in order to ensure public access?</p>
<p>Any hints for tags concerning my singlepoint data welcome :)</p>
<p>thx Jochen</p>
<p>p.s.: Another neat posssibility I would like to have is to process the data myself through gle-graphics with a scaled map as background. I guess there isn't any (easy) way to make that work with OSM...? I'm imagening I would have to crop layerdata from existing maps then scripting it in my graphicstool?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span> <span class="post-tag tag-link-singlepoint" rel="tag" title="see questions tagged &#39;singlepoint&#39;">singlepoint</span> <span class="post-tag tag-link-trafficaccident" rel="tag" title="see questions tagged &#39;trafficaccident&#39;">trafficaccident</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Jul '18, 18:02</strong></p>
<img src="https://secure.gravatar.com/avatar/2f01f27729aeebf082673686e22f7a3a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="j_o_b_u&#39;s gravatar image" />
<p><span>j_o_b_u</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="j_o_b_u has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Jul '18, 18:13</strong> </span></p>
</div>
</div>
<div id="comments-container-64482" class="comments-container">
&#10;</div>
<div id="comment-tools-64482" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64482-form-container" class="comment-form-container">
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

<span id="64483"></span>

<div id="answer-container-64483" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64483-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64483-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-64483-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Try making a GeoJSON or KML file from your data, then you can display it on a web site using umap.openstreetmap.fr.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Jul '18, 18:31</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-64483" class="comments-container">
<span id="64486"></span>
<div id="comment-64486" class="comment">
<div id="post-64486-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>thx for the answer.</p>
<p>I don't have a public webserver accessible via internet at hand. So umap.openstreetmap.fr wouldn't be of any use in that case!? Sure I can write out an .kml though but then what?</p>
</div>
<div id="comment-64486-info" class="comment-info">
<span class="comment-age">(02 Jul '18, 20:00)</span> <span class="comment-user userinfo">j_o_b_u</span>
</div>
</div>
<span id="64538"></span>
<div id="comment-64538" class="comment">
<div id="post-64538-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I think that umap can either display a JSON file loaded from elsewhere, or import a JSON file which then doesn't have to be on a public web server. Have you tried it?</p>
</div>
<div id="comment-64538-info" class="comment-info">
<span class="comment-age">(04 Jul '18, 22:09)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-64483" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64483-form-container" class="comment-form-container">
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


+++
type = "question"
title = "Routing backend server Setup"
description = '''I am trying to setup my own routing server, Few days ago, I asked the following question: https://help.openstreetmap.org/questions/86871/routing-distance-from-openstreet-map-data So I downloaded the pbf file from Geofabrik.  As given in this link: https://github.com/Project-OSRM/osrm-backend, I ran ...'''
date = "2023-03-14T17:00:00Z"
lastmod = "2023-03-14T17:12:00Z"
weight = 86929
keywords = [ "hardwarerequirements", "osrm", "aws", "routing" ]
aliases = [ "/questions/86929" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Routing backend server Setup](/questions/86929/routing-backend-server-setup)

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
<span id="post-86929-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86929-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86929-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to setup my own routing server, Few days ago, I asked the following question: <span></span><a href="https://help.openstreetmap.org/questions/86871/routing-distance-from-openstreet-map-data">https://help.openstreetmap.org/questions/86871/routing-distance-from-openstreet-map-data</a></p>
<p>So I downloaded the pbf file from Geofabrik. As given in this link: <span></span><a href="https://github.com/Project-OSRM/osrm-backend">https://github.com/Project-OSRM/osrm-backend</a>, I ran the docker command to preprocess the extract(pbf file). When I ran it for smaller region like berlin, it was successfully executed within minutes. When I downloaded the pbf file for entire USA and tried to run, it gave an error: "insufficient memory. Please provide more swap space."</p>
<p>My system has Ubuntu, 12GB RAM, the download speed 41 MBps and upload speed are 21 MBps. By default, it was using swap space around 4GB. I increased the swap space to 20GB and 50 GB still same error. After when I increased the swap space to 100GB, it processed for around 160 hours(7 days), my system got heated up and shut down.</p>
<p>Now, the plan is to do this activity on the AWS server. AWS instances come in large variety with different features, For this activity I don't think there is a much need of network bandwidth in this case(not sure), all that is needed is RAM.</p>
<p>So the questions are:</p>
<p>1) Which AWS server is best for this activity?<br />
2) If lets say, I take some instance and run it for 15 days for the calculation(24 hours), what would be the cost?</p>
<p>Any experiences around the same would be appreciated.</p>
<p>Thanks your taking time to read and looking forward for further guidance.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-hardwarerequirements" rel="tag" title="see questions tagged &#39;hardwarerequirements&#39;">hardwarerequirements</span> <span class="post-tag tag-link-osrm" rel="tag" title="see questions tagged &#39;osrm&#39;">osrm</span> <span class="post-tag tag-link-aws" rel="tag" title="see questions tagged &#39;aws&#39;">aws</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Mar '23, 17:00</strong></p>
<img src="https://secure.gravatar.com/avatar/5ad7f3355e56126c366d8cabe7021aff?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vikas%20Singla&#39;s gravatar image" />
<p><span>Vikas Singla</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vikas Singla has no accepted answers">0%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Mar '23, 08:02</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-86929" class="comments-container">
&#10;</div>
<div id="comment-tools-86929" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86929-form-container" class="comment-form-container">
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

<span id="86930"></span>

<div id="answer-container-86930" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86930-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86930-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-86930-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>On an AWS machine with 128 GB of RAM you should be able to compute an US (car) routing graph in under 24 hours.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Mar '23, 17:12</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-86930" class="comments-container">
&#10;</div>
<div id="comment-tools-86930" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86930-form-container" class="comment-form-container">
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


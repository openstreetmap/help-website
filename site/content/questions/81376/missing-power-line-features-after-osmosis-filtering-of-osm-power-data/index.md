+++
type = "question"
title = "Missing power line features after Osmosis filtering of OSM power data"
description = '''After filtering OSM data using Osmosis, I&#x27;m missing a significant portion of the power lines in major countries like the US, Canada, Spain, China, India etc. The attached images show what I have for the US and India. I&#x27;ve abstracted my data as per the SciGrid model (https://www.power.scigrid.de/page...'''
date = "2021-08-19T21:07:00Z"
lastmod = "2021-08-19T21:48:00Z"
weight = 81376
keywords = [ "filter", "lines", "power", "osmosis", "missing" ]
aliases = [ "/questions/81376" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Missing power line features after Osmosis filtering of OSM power data](/questions/81376/missing-power-line-features-after-osmosis-filtering-of-osm-power-data)

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
<span id="post-81376-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81376-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81376-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>After filtering OSM data using Osmosis, I'm missing a significant portion of the power lines in major countries like the US, Canada, Spain, China, India etc. The attached images show what I have for the US and India. I've abstracted my data as per the SciGrid model (<a href="https://www.power.scigrid.de/pages/general-information.html)">https://www.power.scigrid.de/pages/general-information.html)</a> so that the lines are represented as the crow flies between nodes. It seems that OSM must have these missing lines somewhere because OpenInfraMap displays them: <a href="https://openinframap.org/#5.99/34.763/-115.582/P.">https://openinframap.org/#5.99/34.763/-115.582/P.</a></p>
<p>My process was that I filtered OSM data using Osmosis for all objects with key=power, value=* as well as objects with key=route, value=power to extract power lines and substations. During the abstraction process I kept only those lines with values: "line" or "cable", and only nodes with the following values: "substation", "sub_station", "station", "plant", or "generator". Having contacted the creator of OpenInfraMap, it seems that the absence of the "minor_line" value cannot explain many of the missing lines. What are some candidate reasons for why this might be happening?</p>
<p><img src="/upfiles/Screen_Shot_2021-08-19_at_3.58.52_PM.png" alt="alt text" /> <img src="/upfiles/Screen_Shot_2021-08-19_at_3.59.00_PM.png" alt="alt text" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-lines" rel="tag" title="see questions tagged &#39;lines&#39;">lines</span> <span class="post-tag tag-link-power" rel="tag" title="see questions tagged &#39;power&#39;">power</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span> <span class="post-tag tag-link-missing" rel="tag" title="see questions tagged &#39;missing&#39;">missing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Aug '21, 21:07</strong></p>
<img src="https://secure.gravatar.com/avatar/5d841264facb40ff2d18a6317ddac0c1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kev_7&#39;s gravatar image" />
<p><span>kev_7</span><br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kev_7 has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-81376" class="comments-container">
&#10;</div>
<div id="comment-tools-81376" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81376-form-container" class="comment-form-container">
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

<span id="81377"></span>

<div id="answer-container-81377" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81377-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81377-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81377-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>When filtering OSM data you always need to ensure that any referenced objects are also included, otherwise the geometry cannot be built. Is it possible that you have accidentally dropped the nodes from your data set that are required to build the power line geometry? In Osmosis you have to use the <code>--used-node</code> option to avoid that problem.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Aug '21, 21:34</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</img>
</div>
</div>
<div id="comments-container-81377" class="comments-container">
<span id="81378"></span>
<div id="comment-81378" class="comment">
<div id="post-81378-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have used the --used-node option though its possible I've misused it. The code is the following:</p>
<p>osmosis ^ --read-pbf file=D:\Kevin\EGC_Project\data\planet-210322.osm.pbf ^ --tag-filter accept-relations route=power ^ --used-way ^ --used-node ^ --buffer outPipe.0=route ^ --read-pbf file=D:\Kevin\EGC_Project\data\planet-210322.osm.pbf ^ --tag-filter accept-relations power= <em>^ --used-way ^ --used-node ^ --buffer outPipe.0=power ^ --read-pbf file=D:\Kevin\EGC_Project\data\planet-210322.osm.pbf ^ --tag-filter reject-relations ^ --tag-filter accept-ways power=</em> ^ --used-node ^ --buffer outPipe.0=pways ^ --read-pbf file=D:\Kevin\EGC_Project\data\planet-210322.osm.pbf ^ --tag-filter reject-relations ^ --tag-filter reject-ways ^ --tag-filter accept-nodes power=* ^ --buffer outPipe.0=pnodes ^ --merge inPipe.0=route inPipe.1=power ^ --buffer outPipe.0=mone ^ --merge inPipe.0=pways inPipe.1=pnodes ^ --buffer outPipe.0=mtwo ^ --merge inPipe.0=mone inPipe.1=mtwo ^ --write-pbf file=D:\Kevin\EGC_Project\data\global_power_210322.osm.pbf</p>
</div>
<div id="comment-81378-info" class="comment-info">
<span class="comment-age">(19 Aug '21, 21:48)</span> <span class="comment-user userinfo">kev_7</span>
</div>
</div>
</div>
<div id="comment-tools-81377" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81377-form-container" class="comment-form-container">
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


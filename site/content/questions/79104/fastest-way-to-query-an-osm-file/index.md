+++
type = "question"
title = "Fastest way to query an OSM file"
description = '''I am writing a code in Python to find bus stops inside of different rectangles that depend on incoming data.I am able to this with the overpass Api and the python module overpy but query time is usually around 5 seconds and I would like to have it under 1 second. Moreover, the limit of queries is re...'''
date = "2021-03-02T17:38:00Z"
lastmod = "2021-03-03T08:33:00Z"
weight = 79104
keywords = [ "python", "query", "busstops", "postgis", "optimize" ]
aliases = [ "/questions/79104" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Fastest way to query an OSM file](/questions/79104/fastest-way-to-query-an-osm-file)

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
<span id="post-79104-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79104-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-79104-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am writing a code in Python to find bus stops inside of different rectangles that depend on incoming data.I am able to this with the overpass Api and the python module overpy but query time is usually around 5 seconds and I would like to have it under 1 second. Moreover, the limit of queries is reached. My second attempt was to save a local osm copy and to cut the area of interest with osmosis, however, trimming the area takes nearly 2 minutes. What is the fastest way to accomplish this ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-python" rel="tag" title="see questions tagged &#39;python&#39;">python</span> <span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span> <span class="post-tag tag-link-busstops" rel="tag" title="see questions tagged &#39;busstops&#39;">busstops</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span> <span class="post-tag tag-link-optimize" rel="tag" title="see questions tagged &#39;optimize&#39;">optimize</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Mar '21, 17:38</strong></p>
<img src="https://secure.gravatar.com/avatar/a09dbb622f7d7cd28396951b306e2c60?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fragodec&#39;s gravatar image" />
<p><span>fragodec</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fragodec has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Mar '21, 17:44</strong> </span></p>
</div>
</div>
<div id="comments-container-79104" class="comments-container">
&#10;</div>
<div id="comment-tools-79104" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79104-form-container" class="comment-form-container">
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

<span id="79106"></span>

<div id="answer-container-79106" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-79106-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79106-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-79106-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="fragodec has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The command line tool <a href="https://osmcode.org/osmium-tool/">Osmium</a> can do all sorts of things like creating extracts. It is much faster than Osmosis. I recommend the following way of processing OSM data:</p>
<ol>
<li>Download a suitable extract from <a href="https://download.geofabrik.de/">Geofabrik</a></li>
<li>Use <code>osmium extract</code> to narrow this down to a smaller area if needed</li>
<li>Use <code>osmum tags-filter</code> to filter out roughly all the subject data you might need</li>
<li>Use your own Python script (possibly based on <a href="https://osmcode.org/pyosmium/">PyOsmium</a>) to do any specialized processing you need.</li>
</ol>
<p>Python code will be slower than the optimized C++ code of the Osmium command line tool, so it makes sense to do pre-filtering with the faster tool (step 2/3) and then use Python for the rest.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Mar '21, 20:46</strong></p>
<img src="https://secure.gravatar.com/avatar/2d4dfcdcde73aa5e2ffa4a9b3a7cb51d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jochen%20Topf&#39;s gravatar image" />
<p><span>Jochen Topf</span><br />
<span class="score" title="5244 reputation points"><span>5.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jochen Topf has 32 accepted answers">31%</span></p>
</div>
</div>
<div id="comments-container-79106" class="comments-container">
<span id="79110"></span>
<div id="comment-79110" class="comment">
<div id="post-79110-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thank you for your detailed answer. Two-follow up questions:</p>
<ol>
<li><p>I did some research and it seems quite difficult to install Osmium in Windows, is there a more or less straight-forward way of doing so?</p></li>
<li><p>The rectangles defining the current areas of interest are themselves generated in real-time with a Python code. Ideally I would like the code to call Osmium, do the extraction there and then recover the smaller osm file from Python. Is there a way to do this?</p></li>
</ol>
</div>
<div id="comment-79110-info" class="comment-info">
<span class="comment-age">(03 Mar '21, 07:55)</span> <span class="comment-user userinfo">fragodec</span>
</div>
</div>
<span id="79111"></span>
<div id="comment-79111" class="comment">
<div id="post-79111-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>to 1) No, unfortunately there isn't an easy way to install Osmium on Windows. You might be able to use WSL for this.</p>
<p>to 2) There is no special way for doing this, but you can run any program from Python with <code>os.system()</code>, so you can just build the right command line and run Osmium from it. You can run <code>osmium extract</code> with a bounding box on the command line or use a config file with many bounding boxes in it to efficiently create many extracts. So in your case it might make sense to create that config file from your Python script and then run <code>osmium extract</code> once.</p>
</div>
<div id="comment-79111-info" class="comment-info">
<span class="comment-age">(03 Mar '21, 08:33)</span> <span class="comment-user userinfo">Jochen Topf</span>
</div>
</div>
</div>
<div id="comment-tools-79106" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79106-form-container" class="comment-form-container">
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


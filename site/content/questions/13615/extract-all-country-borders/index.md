+++
type = "question"
title = "Extract all country borders"
description = '''What I would like to do is extract all country borders into 1 vector map. I have chosen OSM because of its regular updates and high resolution required for the project. Also will need to to extract major roads and rivers at some point into another vector map. How can I go about ding these things? Th...'''
date = "2012-06-19T09:42:00Z"
lastmod = "2015-07-03T14:21:00Z"
weight = 13615
keywords = [ "country", "borders", "extract" ]
aliases = [ "/questions/13615" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Extract all country borders](/questions/13615/extract-all-country-borders)

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
<span id="post-13615-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13615-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-13615-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>What I would like to do is extract all country borders into 1 vector map.</p>
<p>I have chosen OSM because of its regular updates and high resolution required for the project.</p>
<p>Also will need to to extract major roads and rivers at some point into another vector map.</p>
<p>How can I go about ding these things?</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-country" rel="tag" title="see questions tagged &#39;country&#39;">country</span> <span class="post-tag tag-link-borders" rel="tag" title="see questions tagged &#39;borders&#39;">borders</span> <span class="post-tag tag-link-extract" rel="tag" title="see questions tagged &#39;extract&#39;">extract</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Jun '12, 09:42</strong></p>
<img src="https://secure.gravatar.com/avatar/0dc847b1bc00d07449e18feb3772c0ae?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stuart576&#39;s gravatar image" />
<p><span>stuart576</span><br />
<span class="score" title="71 reputation points">71</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stuart576 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-13615" class="comments-container">
<span id="13618"></span>
<div id="comment-13618" class="comment">
<div id="post-13618-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have looked at the, 'Tag:boundary=administrative' wiki and I guess I should use that, but what programs can I use, I've had a little play with GRASS and Osmosis but I'm not really sure what I am doing. Any advice?</p>
</div>
<div id="comment-13618-info" class="comment-info">
<span class="comment-age">(19 Jun '12, 10:09)</span> <span class="comment-user userinfo">stuart576</span>
</div>
</div>
</div>
<div id="comment-tools-13615" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13615-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="13619"></span>

<div id="answer-container-13619" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13619-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13619-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-13619-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is not a trivial task and it would be much easier for you to use the ready-made polygons from <a href="http://naturalearthdata.com/.">http://naturalearthdata.com/.</a></p>
<p>If you really want to go down the OSM route then try the links presented in this blog article: <a href="https://www.openstreetmap.org/user/dbusse/diary/17043">https://www.openstreetmap.org/user/dbusse/diary/17043</a> - be aware that country borders will include maritime borders and that you need to intersect them with the coastline (try <a href="http://www.openstreetmapdata.com/">http://www.openstreetmapdata.com/</a> ) to get "proper" country outlines. We are talking about very detailed polygons, some with hundreds of thousands of points, so be warned that not every GIS program on every computer will simply process them.</p>
<p>A good tool to export OSM data to shape files is "osmjs" but it probably requires some OSM and Linux knowledge to operate.</p>
<p>The OSM wiki has a list of OSM businesses here: <a href="https://wiki.openstreetmap.org/wiki/Commercial_OSM_Software_and_Services">https://wiki.openstreetmap.org/wiki/Commercial_OSM_Software_and_Services</a> - some of them will be able to do this processing for you.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Jun '12, 10:15</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Jun '12, 14:37</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/c3743b1b368f5e209eb8aad30164acc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Allan&#39;s gravatar image" />
<p><span>Andy Allan</span><br />
<span class="score" title="12456 reputation points"><span>12.5k</span></span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="128 badges"><span class="silver">●</span><span class="badgecount">128</span></span><span title="153 badges"><span class="bronze">●</span><span class="badgecount">153</span></span></p>
</div>
</div>
<div id="comments-container-13619" class="comments-container">
<span id="13620"></span>
<div id="comment-13620" class="comment">
<div id="post-13620-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the help so far, I have managed to get Osmosis working, but I have been unable to remove all but country borders (admin_level=2) from my maps, my test maps are South America and Great Britain. I have tried these commands so far:</p>
</div>
<div id="comment-13620-info" class="comment-info">
<span class="comment-age">(19 Jun '12, 14:32)</span> <span class="comment-user userinfo">stuart576</span>
</div>
</div>
<span id="13621"></span>
<div id="comment-13621" class="comment">
<div id="post-13621-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Osmosisosmosis-0.40.1bin&gt;osmosis.bat --read-pbf "......MAP DataOSM PlanetSouth Americasouth-america .osm.pbf" --wkv keyValueList="admin_level=2" --used-node --write-xml output2.osm</p>
<p>Osmosisosmosis-0.40.1bin&gt;osmosis.bat --read-pbf "......MAP DataOSM PlanetSouth Americasouth-america .osm.pbf" --tf accept-ways boundary=administrative --tf reject-relations --used-node --write-xml output.osm</p>
<p>But neither leave me with what I want. Any advice on how to exclude everything except admin_level=2 ?</p>
</div>
<div id="comment-13621-info" class="comment-info">
<span class="comment-age">(19 Jun '12, 14:32)</span> <span class="comment-user userinfo">stuart576</span>
</div>
</div>
<span id="13623"></span>
<div id="comment-13623" class="comment">
<div id="post-13623-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You don't write what the problem with these approaches is. I believe the first fails because you need to write admin_level.2 not admin_level=2 in --wkv. Check this mailing list thread where the issue is discussed: <a href="http://www.mail-archive.com/dev@openstreetmap.org/msg15500.html">http://www.mail-archive.com/dev@openstreetmap.org/msg15500.html</a></p>
</div>
<div id="comment-13623-info" class="comment-info">
<span class="comment-age">(19 Jun '12, 14:44)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-13619" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13619-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="13747"></span>

<div id="answer-container-13747" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13747-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13747-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-13747-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Have a look at <a href="https://wiki.openstreetmap.org/wiki/Osmfilter">Osmfilter</a> ... you can reduce big country extracts to any elements you want by filtering.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Jun '12, 16:48</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-13747" class="comments-container">
&#10;</div>
<div id="comment-tools-13747" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13747-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="43960"></span>

<div id="answer-container-43960" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43960-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43960-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-43960-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If only the administrative boundary data is needed you can get it under <a href="http://download.geofabrik.de/">http://download.geofabrik.de/</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Jul '15, 14:21</strong></p>
<img src="https://secure.gravatar.com/avatar/bc6d0b055d631830f7891d3f89edb66b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="katpatuka&#39;s gravatar image" />
<p><span>katpatuka</span><br />
<span class="score" title="1041 reputation points"><span>1.0k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="36 badges"><span class="bronze">●</span><span class="badgecount">36</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="katpatuka has 2 accepted answers">12%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Jul '15, 14:24</strong> </span></p>
</div>
</div>
<div id="comments-container-43960" class="comments-container">
&#10;</div>
<div id="comment-tools-43960" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43960-form-container" class="comment-form-container">
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


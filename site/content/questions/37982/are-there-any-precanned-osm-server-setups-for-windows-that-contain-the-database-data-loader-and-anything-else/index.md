+++
type = "question"
title = "Are there any precanned OSM server setups for Windows that contain the database, data loader and anything else"
description = '''Hello, Are there any precanned OSM server setups that contain the database, data loader and anything else you need to get an open streetmap database up quickly? Im going to use the database to mainly generate tiles, but I also want to use the data for analysis if need be. Ive searched the internets,...'''
date = "2014-10-27T00:19:00Z"
lastmod = "2014-10-28T12:21:00Z"
weight = 37982
keywords = [ "windows", "postgres", "package" ]
aliases = [ "/questions/37982" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Are there any precanned OSM server setups for Windows that contain the database, data loader and anything else](/questions/37982/are-there-any-precanned-osm-server-setups-for-windows-that-contain-the-database-data-loader-and-anything-else)

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
<span id="post-37982-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37982-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-37982-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>Are there any precanned OSM server setups that contain the database, data loader and anything else you need to get an open streetmap database up quickly? Im going to use the database to mainly generate tiles, but I also want to use the data for analysis if need be.</p>
<p>Ive searched the internets, but alas I failed.</p>
<p>Hopefully someone can help me out.</p>
<p>If there are no packages, I would like just a good set of nonlinux set of instructions.</p>
<p>thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-postgres" rel="tag" title="see questions tagged &#39;postgres&#39;">postgres</span> <span class="post-tag tag-link-package" rel="tag" title="see questions tagged &#39;package&#39;">package</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Oct '14, 00:19</strong></p>
<img src="https://secure.gravatar.com/avatar/728321acc3469682288102302efc6341?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ajc2014&#39;s gravatar image" />
<p><span>ajc2014</span><br />
<span class="score" title="46 reputation points">46</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ajc2014 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Oct '14, 11:44</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-37982" class="comments-container">
&#10;</div>
<div id="comment-tools-37982" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37982-form-container" class="comment-form-container">
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

<span id="37998"></span>

<div id="answer-container-37998" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-37998-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37998-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-37998-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I suspect that the short answer on Windows is "no".</p>
<p>Given the state of Windows support of some of the tools (being worked on, but not quite there yet, resulting in issues including <a href="https://github.com/openstreetmap/osm2pgsql/issues/117">this one</a>) it'll certainly be easier to install Linux in a VM and work there.</p>
<p>For rendering slippymap tiles, I'd install Ubuntu 14.04 in a VM and then follow <a href="http://switch2osm.org/serving-tiles/">the switch2osm instructions</a>.</p>
<p>For Nominatim (address lookups) I believe that <a href="http://wiki.openstreetmap.org/wiki/Nominatim/Installation">these instructions</a> are the current ones, and I'd be tempted to do it in a different VM, which might make it easier to balance memory usage on the VM host.</p>
<p>If you really want to do it on Windows by all means have a go - there are various blog posts, SOTM presentations and bits of Github documentation that you'll need to draw on, so not really a "canned solution".</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Oct '14, 12:27</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-37998" class="comments-container">
<span id="38003"></span>
<div id="comment-38003" class="comment">
<div id="post-38003-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have to work with Redhat Linux, do these instructions apply to that flavor of Linux?</p>
</div>
<div id="comment-38003-info" class="comment-info">
<span class="comment-age">(27 Oct '14, 14:09)</span> <span class="comment-user userinfo">ajc2014</span>
</div>
</div>
<span id="38005"></span>
<div id="comment-38005" class="comment">
<div id="post-38005-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You'll need to follow the "manual" rather than a "packaged" instructions. The parts of the instructions that are likely to be Ubuntu specific are:</p>
<p>o Package installation. You'll need to locate equivalent Redhat packages to the Ubuntu ones specified. In some cases the name will be the same, in others a bit of web searching ("redhat equivalent to ubuntu X") might be needed.</p>
<p>o Apache config. I suspect you might need to tinker a bit here</p>
<p>o Other config file placement. Some scripts may need adjusting because files are in the Redhat default location not the Ubuntu one.</p>
</div>
<div id="comment-38005-info" class="comment-info">
<span class="comment-age">(27 Oct '14, 15:01)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-37998" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37998-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="38043"></span>

<div id="answer-container-38043" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-38043-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38043-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-38043-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Sam Larsen gave a talk about using OSM tools under Windows at SotM-13. See <a href="http://lanyrd.com/2013/sotm/scpkgp/">http://lanyrd.com/2013/sotm/scpkgp/</a>.</p>
<p>I have made use of OSM tools under Windows for around 5 years. I have experienced most problems with Osmosis and (more recently) with osm2pgsql. My general approach is to create a single bin directory for all these tools (osmosis,osm2pgsql,osmfilter,osmconvert,mkgmap,mapnik) and I usually run commands from that directory. Anything else seems to involve a mass of complications with paths etc which will get mangled by new software.</p>
<p>The OSGeo4W package from the OSGEO consortium is more or less essential. Attempting to install individual components such as ogr2ogr is just a recipe for pain. Cygwin is also very useful.</p>
<p>TileMill works well, but working with the default CartoCSS stylesheet is difficult because many tabs are <a href="https://github.com/mapbox/tilemill/issues/190">not accessible</a> and editing with a text editor can lead to code page problems.</p>
<p>PostgreSQL &amp; PostGIS are very easily installed from standard packages.</p>
<p>Broadly the osm2pgsql, PostGIS, TileMill &amp; mapnik chain works fine on Windows from XP through to Win 8.1. Some knowledge of PostgreSQL is useful on any platform even though people persist in treating it as a black box.</p>
<p>I still find it a shame how little thought is given to how OSM tools might run under Windows (for example, in the past at least one had "/" hard-coded as the directory separator).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Oct '14, 12:21</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-38043" class="comments-container">
&#10;</div>
<div id="comment-tools-38043" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38043-form-container" class="comment-form-container">
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


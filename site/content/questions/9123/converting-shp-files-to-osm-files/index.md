+++
type = "question"
title = "Converting shp files to osm files"
description = '''I am trying to use the python script ogr2osm to convert .shp files to .osm files to use with JOSM, by following the script at https://wiki.openstreetmap.org/wiki/Ogr2osm  When I try and run it, I get the error: &quot;ImportError: No module named ogr&quot;. I think it is due to not having the python-gdal bindin...'''
date = "2011-11-19T02:15:00Z"
lastmod = "2011-11-20T16:49:00Z"
weight = 9123
keywords = [ "python", ".shp.", "ogr2osm" ]
aliases = [ "/questions/9123" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Converting shp files to osm files](/questions/9123/converting-shp-files-to-osm-files)

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
<span id="post-9123-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9123-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-9123-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to use the python script ogr2osm to convert .shp files to .osm files to use with JOSM, by following the script at <a href="https://wiki.openstreetmap.org/wiki/Ogr2osm">https://wiki.openstreetmap.org/wiki/Ogr2osm</a></p>
<p>When I try and run it, I get the error: "ImportError: No module named ogr". I think it is due to not having the python-gdal bindings or osgeo/ogr python bindings installed but nowhere can I find a step by step explanation of how to do this correctly on a Windows 7 machine. I have installed the OSGeo4W shell using the download link given on the wiki page.</p>
<p>I have not used python before but am familiar with other languages and the use of the Command Prompt in Windows.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-python" rel="tag" title="see questions tagged &#39;python&#39;">python</span> <span class="post-tag tag-link-.shp." rel="tag" title="see questions tagged &#39;.shp.&#39;">.shp.</span> <span class="post-tag tag-link-ogr2osm" rel="tag" title="see questions tagged &#39;ogr2osm&#39;">ogr2osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Nov '11, 02:15</strong></p>
<img src="https://secure.gravatar.com/avatar/6edb4957e57770118c3b8022cfce68a8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="srbrook&#39;s gravatar image" />
<p><span>srbrook</span><br />
<span class="score" title="993 reputation points">993</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="srbrook has 3 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-9123" class="comments-container">
<span id="9134"></span>
<div id="comment-9134" class="comment">
<div id="post-9134-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>My mistake was not realising the OSGeo4W icon that had been installed on my desktop was a Command Prompt window with all the right linkages set up and that I should use that instead of the Windows Command Prompt. Thankyou - I now have a .osm file that loads into JOSM and looks right.</p>
</div>
<div id="comment-9134-info" class="comment-info">
<span class="comment-age">(20 Nov '11, 00:40)</span> <span class="comment-user userinfo">srbrook</span>
</div>
</div>
<span id="9137"></span>
<div id="comment-9137" class="comment">
<div id="post-9137-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Please be aware that if you plan to import anything from an external source into OSM, you must discuss your plans with the local community and/or on the "imports" mailing list. Imports are not universally welcomed in OSM and your data might be deleted if it is considered to be a "rogue import".</p>
</div>
<div id="comment-9137-info" class="comment-info">
<span class="comment-age">(20 Nov '11, 16:49)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-9123" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9123-form-container" class="comment-form-container">
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

<span id="9130"></span>

<div id="answer-container-9130" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9130-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9130-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-9130-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="srbrook has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Having set up gdal with python bindings on Windows in the past, I can confidently say that it is easier to set up a VM with VirtualBox running ubuntu and install gdal on it.</p>
<p>If you do want to go the Windows route, you need to run it through the OSGeo4W shell which should get the paths right. You may also need to execute a file that I believe is called gdal17.bat to get the correct version loaded.</p>
<p>When I reinstalled Windows I did not reinstall OSGeo4W and I now run all gdal-related stuff on my server.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Nov '11, 21:57</strong></p>
<img src="https://secure.gravatar.com/avatar/5634c46072077e10f5b7c0da9b4bbb62?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pnorman&#39;s gravatar image" />
<p><span>pnorman</span><br />
<span class="score" title="2352 reputation points"><span>2.4k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="21 badges"><span class="silver">●</span><span class="badgecount">21</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pnorman has 9 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-9130" class="comments-container">
&#10;</div>
<div id="comment-tools-9130" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9130-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="9131"></span>

<div id="answer-container-9131" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9131-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9131-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-9131-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You're almost certainly correct that the import error is because Python can't find the python-gdal bindings.</p>
<p>What I would do is download prebuilt GDAL binaries from: <a href="http://www.gisinternals.com/sdk/">http://www.gisinternals.com/sdk/</a></p>
<p>That page offers binaries from a variety of compilers. You should choose the compiler that was used to build your copy of Python. You can see what compiler your Python was built with by opening the Python command line -- it's part of the version info that is spat out at startup.</p>
<p>Once you've got the correct GDAL binaries, you'll need to let Python know where they are. You can do this by adding (or updating) PYTHONPATH in your Windows environment variables. You'll want to set it to &lt;your_gdal_install&gt;\bin\gdal\python</p>
<p>Note that I haven't actually used GDAL from Python before, so take my instructions with a grain of salt.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Nov '11, 22:04</strong></p>
<img src="https://secure.gravatar.com/avatar/343111beef816657beccdf3c601d600b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DanHomerick&#39;s gravatar image" />
<p><span>DanHomerick</span><br />
<span class="score" title="156 reputation points">156</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DanHomerick has one accepted answer">33%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Nov '11, 22:06</strong> </span></p>
</div>
</div>
<div id="comments-container-9131" class="comments-container">
&#10;</div>
<div id="comment-tools-9131" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9131-form-container" class="comment-form-container">
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


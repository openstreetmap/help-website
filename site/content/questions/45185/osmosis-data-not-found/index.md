+++
type = "question"
title = "OSMOSIS data not found"
description = '''Hi all, I am very new to this and just managed to install OSMOSIS. I am trying to test run a small data extract, but it files finding the data osmosis --read-pbf moldova-latest.osm.pbf --bounding-box top=47.0 left=28.0 bottom=46.0 right=29.0 --write-pbf cut.pbf Does this bring the Moldova file from ...'''
date = "2015-09-11T11:45:00Z"
lastmod = "2015-09-14T10:04:00Z"
weight = 45185
keywords = [ "extract", "data", "osmosis" ]
aliases = [ "/questions/45185" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [OSMOSIS data not found](/questions/45185/osmosis-data-not-found)

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
<span id="post-45185-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45185-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-45185-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all,</p>
<p>I am very new to this and just managed to install OSMOSIS. I am trying to test run a small data extract, but it files finding the data</p>
<p>osmosis --read-pbf moldova-latest.osm.pbf --bounding-box top=47.0 left=28.0 bottom=46.0 right=29.0 --write-pbf cut.pbf</p>
<p>Does this bring the Moldova file from the internet or do I need to place the file in a certain folder.</p>
<p>Any help greatly appreciated</p>
<p>Many thanks</p>
<p>Jon</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-extract" rel="tag" title="see questions tagged &#39;extract&#39;">extract</span> <span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Sep '15, 11:45</strong></p>
<img src="https://secure.gravatar.com/avatar/ad7df450e9cbc9f0133014ef50c8bcf0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jon2709&#39;s gravatar image" />
<p><span>Jon2709</span><br />
<span class="score" title="36 reputation points">36</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jon2709 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-45185" class="comments-container">
<span id="45186"></span>
<div id="comment-45186" class="comment">
<div id="post-45186-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Your command line is looking for moldova-latest.osm.pbf in the directory that you are currently in.</p>
</div>
<div id="comment-45186-info" class="comment-info">
<span class="comment-age">(11 Sep '15, 11:46)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="45187"></span>
<div id="comment-45187" class="comment">
<div id="post-45187-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, but now I get another error failed to initialise Osmosis pbf serializer</p>
<p>I think I will try with the planet.pbf</p>
</div>
<div id="comment-45187-info" class="comment-info">
<span class="comment-age">(11 Sep '15, 11:54)</span> <span class="comment-user userinfo">Jon2709</span>
</div>
</div>
<span id="45188"></span>
<div id="comment-45188" class="comment">
<div id="post-45188-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Don't try the planet until a small extract works. You'll need to provide more information (what OS you're using, how did you install osmosis etc.) to get more meaningful help.</p>
</div>
<div id="comment-45188-info" class="comment-info">
<span class="comment-age">(11 Sep '15, 11:56)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="45189"></span>
<div id="comment-45189" class="comment">
<div id="post-45189-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Using windows 7 enterprise</p>
<p>Downloaded the latest OSMOSIS file, and had to change the batch file plexus-classworlds-2.4.jar to plexus-classworlds-2.5.2.jar to get OSMOSIS working on my PC</p>
<p>The point of this task is that I use ESRI software and I have built various models to extract OSM data into ESRI Geeodatabases and to merge the OSM Shapefiles (that contain labels) with the database. I want to play with the .pbf formats to see what other useful info/metadata is available and see on the tags work.</p>
<p>I will most likely stay with the ESRI model that have for extracting .osm data. But I would like to have OSMOSIS working</p>
<p>Thanks for the help!</p>
</div>
<div id="comment-45189-info" class="comment-info">
<span class="comment-age">(11 Sep '15, 12:02)</span> <span class="comment-user userinfo">Jon2709</span>
</div>
</div>
<span id="45192"></span>
<div id="comment-45192" class="comment">
<div id="post-45192-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>It's not just you and it's not just a problem with our wiki page. As currently packaged osmosis doesn't work on Windows. There's the plexus-classworlds change that you spotted, but also clearly something else (and not just that the readme is wrong).</p>
<p>What I've done in the past on Windows is just ignore osmosis' bizarre packaging attempt and set the CLASSPATH manually. That may work, but requires more knowledge of Java than users ought to need.</p>
<p>I'll have a look at it if time permits today - but with a bit of luck somebody somewhere may have a distribution that actually works.</p>
</div>
<div id="comment-45192-info" class="comment-info">
<span class="comment-age">(11 Sep '15, 12:53)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="45195"></span>
<div id="comment-45195" class="comment not_top_scorer">
<div id="post-45195-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Many thanks, looking forward to it. If you do find a solution please email me on jonathan.mccloskey1@btinternet.com</p>
<p>best</p>
<p>jon</p>
</div>
<div id="comment-45195-info" class="comment-info">
<span class="comment-age">(11 Sep '15, 13:03)</span> <span class="comment-user userinfo">Jon2709</span>
</div>
</div>
<span id="45199"></span>
<div id="comment-45199" class="comment not_top_scorer">
<div id="post-45199-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I've tidied up the readme and the batch file to make them more likely to work in most cases. See <a href="https://github.com/SomeoneElseOSM/osmosis/releases/tag/0.44.1.5">https://github.com/SomeoneElseOSM/osmosis/releases/tag/0.44.1.5</a> .</p>
<p>Try the zip file at <a href="https://github.com/SomeoneElseOSM/osmosis/releases/download/0.44.1.5/osmosis-0.44.1-5-gc2a8a69-SNAPSHOT.zip">https://github.com/SomeoneElseOSM/osmosis/releases/download/0.44.1.5/osmosis-0.44.1-5-gc2a8a69-SNAPSHOT.zip</a> . I've added a pbf example to the readme - if it still doesn't work post the full command line here. FWIW it works for me on Windows now when run with a Java version that identifies as "Java(TM) SE Runtime Environment (build 1.8.0_60-b27)".</p>
</div>
<div id="comment-45199-info" class="comment-info">
<span class="comment-age">(11 Sep '15, 16:57)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="45235"></span>
<div id="comment-45235" class="comment not_top_scorer">
<div id="post-45235-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Many thanks!!</p>
</div>
<div id="comment-45235-info" class="comment-info">
<span class="comment-age">(14 Sep '15, 10:04)</span> <span class="comment-user userinfo">Jon2709</span>
</div>
</div>
</div>
<div id="comment-tools-45185" class="comment-tools">
<span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-45185-form-container" class="comment-form-container">
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

<span id="45200"></span>

<div id="answer-container-45200" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-45200-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45200-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-45200-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For this type of operation I would strongly suggest using <a href="http://wiki.openstreetmap.org/wiki/Osmconvert">osmconvert</a>.</p>
<p>Osmosis has had issues with its Windows distribution for at least <a href="http://forum.openstreetmap.org/viewtopic.php?id=4039">6 years</a>. As SomeoneElse shows they can be fixed, but there are other less painful routes.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Sep '15, 17:06</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-45200" class="comments-container">
<span id="45233"></span>
<div id="comment-45233" class="comment">
<div id="post-45233-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, yes came across osmconvert and being using this.</p>
</div>
<div id="comment-45233-info" class="comment-info">
<span class="comment-age">(14 Sep '15, 09:12)</span> <span class="comment-user userinfo">Jon2709</span>
</div>
</div>
</div>
<div id="comment-tools-45200" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45200-form-container" class="comment-form-container">
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


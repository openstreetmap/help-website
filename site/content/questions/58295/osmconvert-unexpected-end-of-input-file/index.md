+++
type = "question"
title = "osmconvert unexpected end of input file"
description = '''Hi, I&#x27;m trying to subset the history and changeset files for Syria to focus on the area around Aleppo. I downloaded the Syria history file and converted it to Syria_history.osm using osm convert and I did the same with the country&#x27;s changeset file, changesets-170417.osm . I also created a poly file ...'''
date = "2017-08-13T23:40:00Z"
lastmod = "2017-08-21T01:33:00Z"
weight = 58295
keywords = [ "changesets", "osmconvert", "history" ]
aliases = [ "/questions/58295" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [osmconvert unexpected end of input file](/questions/58295/osmconvert-unexpected-end-of-input-file)

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
<span id="post-58295-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-58295-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-58295-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I'm trying to subset the history and changeset files for Syria to focus on the area around Aleppo. I downloaded the Syria history file and converted it to Syria_history.osm using osm convert and I did the same with the country's changeset file, changesets-170417.osm . I also created a poly file with the following text in it:</p>
<p>Aleppo_City_Rectangle 1 36.3078 37.0229 36.3078 37.2676 36.1066 37.2676 36.1066 37.0229 END END</p>
<p>I then run the following command using osmconvert 64 bit:</p>
<p>osmconvert changesets-170417.osm -B=Aleppo_City_Rectangle.poly --complex-ways --out-osm -o=changesets-170417_01.osm</p>
<p>I get the error (twice on consecutive lines): osmconvert Warning: unexpected end of input file: changesets-170417.osm</p>
<p>Same happens when I run it on the history file. Has anyone had this error before? Trying to process data for a school project. Appreciate any help!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-changesets" rel="tag" title="see questions tagged &#39;changesets&#39;">changesets</span> <span class="post-tag tag-link-osmconvert" rel="tag" title="see questions tagged &#39;osmconvert&#39;">osmconvert</span> <span class="post-tag tag-link-history" rel="tag" title="see questions tagged &#39;history&#39;">history</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Aug '17, 23:40</strong></p>
<img src="https://secure.gravatar.com/avatar/862ad51c251682f7af001a6cb0e487c3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="walshep&#39;s gravatar image" />
<p><span>walshep</span><br />
<span class="score" title="86 reputation points">86</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="walshep has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-58295" class="comments-container">
&#10;</div>
<div id="comment-tools-58295" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-58295-form-container" class="comment-form-container">
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

<span id="58296"></span>

<div id="answer-container-58296" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-58296-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-58296-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-58296-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I don't think osmconvert can handle history files. Try <a href="http://osmcode.org/osmium-tool/">Osmium</a> which <a href="http://docs.osmcode.org/osmium/latest/osmium-extract.html">can do that</a>. Something like this should work:</p>
<pre><code>osmium extract syria.osh.pbf -o aleppo.osh.pbf -b BBOX --with-history</code></pre>
<p>Note that you have to use the <code>--with-history</code> option and I recommend using <code>.osh</code> as file ending with history files instead of <code>.osm</code>, Osmium will then auto-detect the type (works with <code>.osh.pbf</code>, too for PBF files.)</p>
<p>Osmium currently can't filter changeset files by bbox and I don't know of any command that can.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Aug '17, 07:11</strong></p>
<img src="https://secure.gravatar.com/avatar/2d4dfcdcde73aa5e2ffa4a9b3a7cb51d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jochen%20Topf&#39;s gravatar image" />
<p><span>Jochen Topf</span><br />
<span class="score" title="5244 reputation points"><span>5.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jochen Topf has 32 accepted answers">31%</span></p>
</div>
</div>
<div id="comments-container-58296" class="comments-container">
<span id="58308"></span>
<div id="comment-58308" class="comment">
<div id="post-58308-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi Jochen. Thank you for your reply. I was looking into the osmium tool several months ago and even watched your video from SOTM2013 on youtube. It seemed to be ideal for what I'd like to do which is: get statistics on the number of changesets by language, and user stats for the country of Syria, comparing data from 2011 and present to see what the change is.</p>
<p>Back in April, tried to install Osmium but I'm not sure how to get it build it properly. I'm using windows 10 and have Cygwin and in it's <strong>lib</strong> directory I have the libraries listed on the [GitHub site][1]. I'm not sure what to do from there though. Is the a detailed guide for windows users?</p>
<p>Thanks!</p>
</div>
<div id="comment-58308-info" class="comment-info">
<span class="comment-age">(15 Aug '17, 01:39)</span> <span class="comment-user userinfo">walshep</span>
</div>
</div>
<span id="58309"></span>
<div id="comment-58309" class="comment">
<div id="post-58309-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I also read on the features of Osmosis that it can generate the changesets file from osm files. I have the 2011 Syria data from the planet website but I don't have the changeset. Would I be able to use the Osmosis tool to generate the changeset for it?</p>
<p>Also as a workaround to the above problem (that I can't use a bounding box to extract data from a changeset file) I could just use the bounding box to extract the Aleppo data and then use the Osmosis tool on that extracted data to get a changeset correct?</p>
<p>Thanks!</p>
</div>
<div id="comment-58309-info" class="comment-info">
<span class="comment-age">(15 Aug '17, 01:53)</span> <span class="comment-user userinfo">walshep</span>
</div>
</div>
<span id="58310"></span>
<div id="comment-58310" class="comment">
<div id="post-58310-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>If you are having problems compiling Osmium, open an issue on the github issue tracker for it and describe in more details what you are doing. I don't know anything about Windows builds but there might be others there. You can also look at the <code>build-appveyor.bat</code> and <code>build-local.bat</code> files in the repository to get you started. They are used for the automated build on appveyor.com.</p>
<p>I see there is some confusion regarding "change files" and "changeset files". Read about the differences at <a href="http://osmcode.org/file-formats-manual/#file-types">http://osmcode.org/file-formats-manual/#file-types</a> .</p>
</div>
<div id="comment-58310-info" class="comment-info">
<span class="comment-age">(15 Aug '17, 07:04)</span> <span class="comment-user userinfo">Jochen Topf</span>
</div>
</div>
<span id="58339"></span>
<div id="comment-58339" class="comment">
<div id="post-58339-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks! I was able to download a windows build from:</p>
<p><a href="https://ci.appveyor.com/project/Mapbox/osmium-tool/build/1.0.284/job/m9ye1tolkglwqmas/artifacts">https://ci.appveyor.com/project/Mapbox/osmium-tool/build/1.0.284/job/m9ye1tolkglwqmas/artifacts</a></p>
</div>
<div id="comment-58339-info" class="comment-info">
<span class="comment-age">(16 Aug '17, 23:40)</span> <span class="comment-user userinfo">walshep</span>
</div>
</div>
</div>
<div id="comment-tools-58296" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-58296-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="58416"></span>

<div id="answer-container-58416" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-58416-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-58416-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-58416-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The following would work in osmconvert:</p>
<p>c:\osmconvert\osmconvert.exe c:\data\OSMplanets\history-141229.osm.pbf –b=-79.3,39.9,-78.2,40.7 –o=c:\data\OSMcities\osm_with_relations\region_history.osm</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Aug '17, 01:33</strong></p>
<img src="https://secure.gravatar.com/avatar/862ad51c251682f7af001a6cb0e487c3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="walshep&#39;s gravatar image" />
<p><span>walshep</span><br />
<span class="score" title="86 reputation points">86</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="walshep has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-58416" class="comments-container">
&#10;</div>
<div id="comment-tools-58416" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-58416-form-container" class="comment-form-container">
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


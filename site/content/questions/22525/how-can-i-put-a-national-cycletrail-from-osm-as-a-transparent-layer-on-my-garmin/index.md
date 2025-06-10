+++
type = "question"
title = "How can I put a national cycletrail from OSM as a transparent layer on my Garmin"
description = '''Question asked on IRC. How can I get a national cycle trail (such as this one in Sweden) converted to a transparent overlay for my Garmin?'''
date = "2013-05-17T16:37:00Z"
lastmod = "2013-05-18T04:26:00Z"
weight = 22525
keywords = [ "mkgmap", "garmin", "ncn", "trail" ]
aliases = [ "/questions/22525" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How can I put a national cycletrail from OSM as a transparent layer on my Garmin](/questions/22525/how-can-i-put-a-national-cycletrail-from-osm-as-a-transparent-layer-on-my-garmin)

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
<span id="post-22525-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22525-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-22525-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Question asked on IRC.</p>
<p>How can I get a national cycle trail (such as this <a href="http://www.openstreetmap.org/browse/relation/2195143">one</a> in Sweden) converted to a transparent overlay for my Garmin?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mkgmap" rel="tag" title="see questions tagged &#39;mkgmap&#39;">mkgmap</span> <span class="post-tag tag-link-garmin" rel="tag" title="see questions tagged &#39;garmin&#39;">garmin</span> <span class="post-tag tag-link-ncn" rel="tag" title="see questions tagged &#39;ncn&#39;">ncn</span> <span class="post-tag tag-link-trail" rel="tag" title="see questions tagged &#39;trail&#39;">trail</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 May '13, 16:37</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-22525" class="comments-container">
&#10;</div>
<div id="comment-tools-22525" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22525-form-container" class="comment-form-container">
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

<span id="22532"></span>

<div id="answer-container-22532" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-22532-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22532-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-22532-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Working on the assumption that the trail covers most of the country, you need to do the following things (a lot of this follows <a href="http://wiki.openstreetmap.org/wiki/OSM_Map_On_Garmin/Cycle_map">OSM on Garmin Cycle Map</a>):</p>
<ul>
<li>Download an OSM XML file containing the area of interest. Usually Geofabrik's download site is the best place to start (some alternatives are listed at the end).</li>
<li>Download the java program <a href="http://www.mkgmap.org.uk/download/mkgmap.html">Mkgmap</a> from here.</li>
<li>Place the OSM XML file &amp; mkgmap in the same directory. (I usually have a specific directory for garmin work).</li>
<li>Create a subdirectory of that directory called, say, <code>ncnstyle</code>. This will be used to store the rules for processing the xml to a garmin img file</li>
<li>Download a cycle specific mkgmap style from <a href="http://svn.openstreetmap.org/applications/utils/export/garmincyclemap/network/cyclemap/">http://svn.openstreetmap.org/applications/utils/export/garmincyclemap/network/cyclemap/</a> and place them in the subdirectory. You need all the files from this site (info, lines, options, points, polygons, relations, version). Either save by right clicking in your browser or use svn to get all at once. In windows you may need to open each file with the command line editor and save them to change newlines to windows end of lines.</li>
</ul>
<p>At this point you have everything you need to create a garmin IMG file, but first we want to change things a little so that only the National Cycle Trail data are processed. There are several options for doing this (by filtering out unneeded data from the OSM file), but here I follow a route where we only process NCN data in the mkgmap style.</p>
<p>Once the style has been changed we now need to use it. The way I do this is as follows</p>
<ul>
<li>Create a batch file (.bat on windows, a shell script under unix). I only do this because I forget all the parameters and it's easier to change than remember the parameters. Enter on one line the following text (replace things IN UPPER CASE with your particular file names) and save it.</li>
</ul>
<blockquote>
<p><code>java -jar .\mkgmap.jar -c NCNCYCLE.txt OSMDOWNLOADFILE</code></p>
</blockquote>
<ul>
<li>Now create the file NCNCYCLE.txt (again use whatever name you want instead of NCNCYCLE). Here all the mkgmap parameters can be set. The ones I standardly use are as follows:</li>
</ul>
<blockquote>
<p><code>style-file: ncncycle family-id: 9201 family-name: YOURNAME series-name: YOURNAME tdbfile route lower-case transparent overview-mapname: ncn-test overview-mapnumber: 92010000 mapname: mapname: 92010001 keep-going</code></p>
</blockquote>
<p>The 9201 is used because this is unlikely to clash with any other Garmin maps you have, but it is as well to check beforehand. Further details on these options at mkgmap on the wiki.</p>
<p>Now we edit the style files copied earlier. Because we only want the NCN route and we do not want buildings, POIs, forests etc., replace the two following files with an empty file: points, polygons.</p>
<p>Add the following line to the lines file near the top,</p>
<pre><code>&gt; # ----- Downgrade tracks where bicycles are banned
&gt; #     (ignore motorway/trunk as this&#39;ll look stupid)
&gt; 
&gt; bicycle=no &amp; ( highway!=motorway &amp;
&gt; highway!=trunk ) { set
&gt; highway=footway; } access=private {
&gt; set highway=private; }
&gt; ###==== these are the extra three lines, the aim is to suppress all
&gt; output except ncn ==== ### ncn_ref=*
&gt; {add ncn=yes; } (ncn!=yes &amp; highway=*)
&gt; { set ncn=no; } (ncn=no &amp; highway =*)
&gt; {delete highway; delete lcn; delete
&gt; rcn; delete lcn_ref; delete rcn_ref;}</code></pre>
<p>Now run the batch file. It should create 3 files a .tdb and 2 *.img files.</p>
<p>... this answer is incomplete because I'm going to the pub. It should say something about MapSetToolkit. It could do with being edited too.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 May '13, 20:45</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-22532" class="comments-container">
&#10;</div>
<div id="comment-tools-22532" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22532-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="22536"></span>

<div id="answer-container-22536" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-22536-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22536-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-22536-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you can live with an intransparent overlay, go to <a href="http://cycling.waymarkedtrails.org/">waymarked trails</a>, search for the name of the desired trail, download the GPX file to your Garmin device and set it to show the parts of the track on the map.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 May '13, 04:26</strong></p>
<img src="https://secure.gravatar.com/avatar/a18e2b8eb41515c09bb66159941584bf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="malenki&#39;s gravatar image" />
<p><span>malenki</span><br />
<span class="score" title="4713 reputation points"><span>4.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="46 badges"><span class="silver">●</span><span class="badgecount">46</span></span><span title="83 badges"><span class="bronze">●</span><span class="badgecount">83</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="malenki has 10 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-22536" class="comments-container">
&#10;</div>
<div id="comment-tools-22536" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22536-form-container" class="comment-form-container">
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


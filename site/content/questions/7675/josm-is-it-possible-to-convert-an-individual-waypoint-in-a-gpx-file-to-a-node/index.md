+++
type = "question"
title = "JOSM - Is it possible to convert an individual waypoint in a GPX file to a node?"
description = '''Imagine that I&#x27;ve been to the pub. It&#x27;s not listed on OSM, so I&#x27;ll add a GPX waypoint at the front door, and edit it so that the description contains the pub name and any other useful information. When I get home, I&#x27;ll open the GPX file in JOSM and update the map. Naturally I&#x27;ll want to add the pub ...'''
date = "2011-09-06T12:41:00Z"
lastmod = "2016-07-13T14:42:00Z"
weight = 7675
keywords = [ "josm", "gpx", "waypoints" ]
aliases = [ "/questions/7675" ]
osqa_answers = 5
osqa_accepted = true
+++

<div class="headNormal">

# [JOSM - Is it possible to convert an individual waypoint in a GPX file to a node?](/questions/7675/josm-is-it-possible-to-convert-an-individual-waypoint-in-a-gpx-file-to-a-node)

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
<span id="post-7675-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7675-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-7675-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
3
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Imagine that I've been to the pub. It's not listed on OSM, so I'll add a GPX waypoint at the front door, and edit it so that the description contains the pub name and any other useful information.</p>
<p>When I get home, I'll open the GPX file in JOSM and update the map. Naturally I'll want to add the pub to OSM, and it would be nice to be able to use the text stored in the waypoint description. The problem is that there are lots of other waypoints in the file, and i don't want to merge them all as nodes - just this one. How do I do that?</p>
<p>Similar questions have been previously asked on the forum <a href="http://forum.openstreetmap.org/viewtopic.php?pid=180263">here</a> and <a href="http://forum.openstreetmap.org/viewtopic.php?id=8394">here</a>, and also on the newbies list <a href="http://lists.openstreetmap.org/pipermail/newbies/2009-March/002717.html">here</a>. It appears that there are solutions to "convert all waypoints..." but not "convert one waypoint..."?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-gpx" rel="tag" title="see questions tagged &#39;gpx&#39;">gpx</span> <span class="post-tag tag-link-waypoints" rel="tag" title="see questions tagged &#39;waypoints&#39;">waypoints</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Sep '11, 12:41</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>22 Oct '15, 09:27</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span></p>
</div>
</div>
<div id="comments-container-7675" class="comments-container">
<span id="7772"></span>
<div id="comment-7772" class="comment">
<div id="post-7772-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Actually there's a serious downside to converting .GPX files to .OSM files for use by JOSM - you don't see any useful information in the data layer about them; just the name. To actually see the tags that have been set you have to "inspect" the node, which is extremely clumsy.</p>
</div>
<div id="comment-7772-info" class="comment-info">
<span class="comment-age">(10 Sep '11, 12:43)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-7675" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7675-form-container" class="comment-form-container">
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

5 Answers:

</div>

</div>

<span id="7705"></span>

<div id="answer-container-7705" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7705-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7705-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-7705-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SomeoneElse has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is not currently possible in JOSM. However you may try to make a plugin or script that does this. Mind that if other people use it they may want to enter the details in another format then you want.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Sep '11, 11:09</strong></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gnonthgol has 57 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-7705" class="comments-container">
<span id="7706"></span>
<div id="comment-7706" class="comment">
<div id="post-7706-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Interesting - I'll have a read of <a href="http://josm.openstreetmap.de/wiki/DevelopersGuide/DevelopingPlugins">http://josm.openstreetmap.de/wiki/DevelopersGuide/DevelopingPlugins</a> . Probably won't be today though...</p>
</div>
<div id="comment-7706-info" class="comment-info">
<span class="comment-age">(07 Sep '11, 11:33)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="50889"></span>
<div id="comment-50889" class="comment">
<div id="post-50889-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It is possible, see Vincent de P...’s answer (which should be the accepted answer, I think).</p>
</div>
<div id="comment-50889-info" class="comment-info">
<span class="comment-age">(13 Jul '16, 13:37)</span> <span class="comment-user userinfo">erik</span>
</div>
</div>
<span id="50893"></span>
<div id="comment-50893" class="comment">
<div id="post-50893-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/5517/erik">@erik</a> It's not the accepted answer because it doesn't actually work for me (for the reasons I added as comments below that answer).</p>
</div>
<div id="comment-50893-info" class="comment-info">
<span class="comment-age">(13 Jul '16, 14:42)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-7705" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7705-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="7680"></span>

<div id="answer-container-7680" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7680-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7680-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-7680-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Your first forum link suggests you can use gpsbabel to make the waypoints into a data layer. If that is so (and I've not tried it), open that layer as a separate layer in JOSM and copy and paste individual nodes between the layers.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Sep '11, 13:40</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-7680" class="comments-container">
<span id="7708"></span>
<div id="comment-7708" class="comment">
<div id="post-7708-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sounds promising - I'll definitely have a look at this.</p>
</div>
<div id="comment-7708-info" class="comment-info">
<span class="comment-age">(07 Sep '11, 11:42)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="7763"></span>
<div id="comment-7763" class="comment">
<div id="post-7763-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Converting a .GPX to a .OSM file works - the tricky bit seems to be getting JOSM to work with multiple layers. For example, if I first of all I open up my converted .osm file, create a new layer, and download from OSM, I can't select anything in the converted .osm file.</p>
<p>If I delete and then reopen the converted .osm file I can now select nodes and press ^C - the problem is that I can't select the other layer and paste them in there (what actually happens is that pressing ^V renames "Data Layer 2" and adds a "0" to the end of the name, so I get "Data Layer 20" etc.</p>
</div>
<div id="comment-7763-info" class="comment-info">
<span class="comment-age">(10 Sep '11, 00:59)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="7764"></span>
<div id="comment-7764" class="comment">
<div id="post-7764-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Interestingly what does work is to press ^C on the node from the converted .OSM file, delete the layer containing the converted .OSM file, and then press ^V, but it's not practical to close and reopen a file every time that you want to add a node.</p>
</div>
<div id="comment-7764-info" class="comment-info">
<span class="comment-age">(10 Sep '11, 01:01)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="7771"></span>
<div id="comment-7771" class="comment">
<div id="post-7771-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>If you have the .osm layer open as one layer and download data to a second, I switch between layers by having the layers dialog open on the right, highlighting the one I want to use, then clicking the third button in (with the green tick on) to make it the active layer. I have used this method to cut and paste missing ways from OS OpenData BoundaryLine shapefiles converted to .osm files using OGR2OSM when fixing GB boundary relations. It is only individual nodes I haven't tried cutting and pasting between layers, but assumed it would work similarly.</p>
</div>
<div id="comment-7771-info" class="comment-info">
<span class="comment-age">(10 Sep '11, 11:46)</span> <span class="comment-user userinfo">EdLoach ♦</span>
</div>
</div>
<span id="7779"></span>
<div id="comment-7779" class="comment">
<div id="post-7779-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That works - the full sequence is as follows:</p>
<p>gpsbabel -w -i gpx -f c:Temposmtr1724a_post.gpx -o osm -F C:/Temp/osm/tr1724a.osm</p>
<p>Open tr1724a.osm in JOSM File / New layer Download from OSM</p>
<p>At this point "Data Layer 1" is active. "Upload Data" says there's nothing to upload.</p>
<p>At this point what I'd expect to be is in each layer - I can hide each and see what I'd expect.</p>
<p>Zoom in on a point that I'm interested in. I can't read the name, the font is too small and the grey on black font is illegible. Activate the other layer and click on the point...</p>
</div>
<div id="comment-7779-info" class="comment-info">
<span class="comment-age">(11 Sep '11, 13:21)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="7780"></span>
<div id="comment-7780" class="comment not_top_scorer">
<div id="post-7780-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>... Right click / inspect shows:</p>
<p>Node id=-8 lat=53.1675882 lon=-1.1494951 (projected: x=-127961.20920136309, y=7014057.564866551); Data set: 1385846; User: [&lt;new object=""&gt;]; ChangeSet id: 0; Timestamp: &lt;new object=""&gt;; Version: 0 tags: "created_by"="GPSBabel-1.4.2" "amenity"="pharmacy" "description"="Pharmacy 09-SEP-11 18:27:19" "name"="DOA049653"</p>
<p>Edit / Copy</p>
<p>Activate Data Layer 1 Edit / Paste</p>
<p>Command Stack says "Added 1 object" Edit the tags on the node (because I've used "pharmacy" to indicate something else).</p>
<p>Upload Data the changeset shows 1 node...</p>
</div>
<div id="comment-7780-info" class="comment-info">
<span class="comment-age">(11 Sep '11, 13:23)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="7781"></span>
<div id="comment-7781" class="comment not_top_scorer">
<div id="post-7781-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The problem is that it's not really a realistic workflow for individual waypoints - way too many button presses.</p>
</div>
<div id="comment-7781-info" class="comment-info">
<span class="comment-age">(11 Sep '11, 13:25)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-7680" class="comment-tools">
<span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-7680-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="47188"></span>

<div id="answer-container-47188" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47188-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47188-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-47188-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<ol>
<li>Open the gpx file</li>
<li>Right-click on the gpx layer, select "convert to data layer"</li>
<li>Switch to editing this layer instead of the osm data layer</li>
<li>Select waypoint(s), Copy</li>
<li>Switch back to editing osm data layer</li>
<li>Paste</li>
</ol>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Dec '15, 17:13</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-47188" class="comments-container">
<span id="47189"></span>
<div id="comment-47189" class="comment">
<div id="post-47189-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>When I try and open a GPX file (I used <a href="http://www.openstreetmap.org/user/SomeoneElse/traces/2079394">http://www.openstreetmap.org/user/SomeoneElse/traces/2079394</a> ) two layers are created, "TR3891b.GPX" and "Markers from TR3891b.GPX". If I select the latter, and "convert to data layer" I get a warning "Upload of unprocessed GPS data as map data is considered harmful" (which is fair enough - I have no intention of uploading unprocessed GPS data).</p>
<p>I selected a waypoint (DOA157315) and copied it to a new OSM layer. If I save (to the dev server, for testing) I get <a href="http://api06.dev.openstreetmap.org/node/4301145583">http://api06.dev.openstreetmap.org/node/4301145583</a> . This isn't much use. What I actually want to do is to be able to see the full set of tags on the waypoint:</p>
<p>&lt;wpt lat="53.0097842" lon="-1.4806223"&gt; &lt;name&gt;DOA157315&lt;/name&gt; &lt;sym&gt;Boat Ramp&lt;/sym&gt; &lt;/wpt&gt;</p>
<p>and process them. In this case "Boat Ramp" means "this footway is marked as a public footpath".</p>
<p>For completeness no non-name tags seem to be coming through. For example cmt and/or desc would be useful here to indicate whether a road has a sidewalk or not:</p>
<p>&lt;wpt lat="53.0004501" lon="-1.4820385"&gt; &lt;name&gt;DOA157415&lt;/name&gt; &lt;cmt&gt;0&lt;/cmt&gt; &lt;desc&gt;0&lt;/desc&gt; &lt;sym&gt;Swimming Area&lt;/sym&gt; &lt;/wpt&gt;</p>
<p>(same file)</p>
</div>
<div id="comment-47189-info" class="comment-info">
<span class="comment-age">(16 Dec '15, 19:04)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="47191"></span>
<div id="comment-47191" class="comment">
<div id="post-47191-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Also, if I convert the "TR3891b.GPX" layer to a data layer I just get an untagged way (I've not uploaded that).</p>
</div>
<div id="comment-47191-info" class="comment-info">
<span class="comment-age">(16 Dec '15, 19:12)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="47192"></span>
<div id="comment-47192" class="comment">
<div id="post-47192-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Just for comparison, here's the equivalent workflow in P2:</p>
<pre><code>1) Edit the GPS trace directly (no need to hunt for the original file)
2) Background / Vector File / TR3891b.GPX / tick
3) Click on an orange waypoint
4) Look at the waypoint&#39;s symbol and comment fields
5) Make changes to map based on what is there
6) Repeat from (3).</code></pre>
<p>There's no need to convert anything, copy between layers, or worry about adding things like <a href="http://api06.dev.openstreetmap.org/node/4301145583">http://api06.dev.openstreetmap.org/node/4301145583</a> by mistake. Most importantly, waypoint information other than the name is visible.</p>
</div>
<div id="comment-47192-info" class="comment-info">
<span class="comment-age">(16 Dec '15, 19:37)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-47188" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47188-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="7704"></span>

<div id="answer-container-7704" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7704-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7704-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-7704-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You could (carefully!) edit the GPX file using your favourite text-editor; it's plain-text XML. Make a backup copy of the file, open the file in your editor, find the waypoint of interest, delete the others, save the file, close the editor, then open the file in JOSM.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Sep '11, 10:52</strong></p>
<img src="https://secure.gravatar.com/avatar/a8992ad9a83eacdd6388ed265d3f6921?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tongro&#39;s gravatar image" />
<p><span>tongro</span><br />
<span class="score" title="701 reputation points">701</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tongro has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-7704" class="comments-container">
<span id="7707"></span>
<div id="comment-7707" class="comment">
<div id="post-7707-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That'd work, but I'd need to know which POIs to create the second data layer from before starting JOSM (or go round the loop several times), and I'd need to write something or use GPSBabel to convert "wpt" entries in the GPX to "node" in a pseudo-OSM file.</p>
</div>
<div id="comment-7707-info" class="comment-info">
<span class="comment-age">(07 Sep '11, 11:42)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-7704" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7704-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="46025"></span>

<div id="answer-container-46025" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-46025-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46025-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-46025-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This question is already answered imho. Convert your gpx file to osm file (possible via web service but also directly in josm via right click on the gpx layer) and then copy the wanted nodes from that layer into your main data layer.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Oct '15, 14:31</strong></p>
<img src="https://secure.gravatar.com/avatar/b904d75b8ea950f64710d2a8303cead7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Klumbumbus&#39;s gravatar image" />
<p><span>Klumbumbus</span><br />
<span class="score" title="543 reputation points">543</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Klumbumbus has one accepted answer">8%</span></p>
</div>
</div>
<div id="comments-container-46025" class="comments-container">
<span id="47190"></span>
<div id="comment-47190" class="comment">
<div id="post-47190-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It's not answered - see the comment on <a href="https://help.openstreetmap.org/answer_link/47188/">https://help.openstreetmap.org/answer_link/47188/</a> .</p>
</div>
<div id="comment-47190-info" class="comment-info">
<span class="comment-age">(16 Dec '15, 19:05)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-46025" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46025-form-container" class="comment-form-container">
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


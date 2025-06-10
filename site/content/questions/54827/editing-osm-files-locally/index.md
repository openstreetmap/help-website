+++
type = "question"
title = "Editing osm files locally"
description = '''Hi all, Use case: I use OpenTripPlanner in combination with OSM and GTFS data in order to calculate catchment areas (&quot;How far do I get within 10 minutes by car?&quot;). This works fine! Now I would like to do scenarios like &quot;How does the catchment area change if we build a new street somewhere or if we i...'''
date = "2017-02-28T11:10:00Z"
lastmod = "2017-03-01T11:06:00Z"
weight = 54827
keywords = [ "editing", "local", "pbf" ]
aliases = [ "/questions/54827" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Editing osm files locally](/questions/54827/editing-osm-files-locally)

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
<span id="post-54827-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54827-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-54827-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all,</p>
<p><strong>Use case</strong>:</p>
<p>I use <a href="http://www.opentripplanner.org/">OpenTripPlanner</a> in combination with OSM and <a href="https://developers.google.com/transit/gtfs/">GTFS</a> data in order to calculate catchment areas ("<em>How far do I get within 10 minutes by car?</em>"). This works fine!</p>
<p>Now I would like to do scenarios like "<em>How does the catchment area change if we build a new street somewhere or if we increase the tempo limit for a certain street etc.?</em>".</p>
<p><strong>Question</strong>:</p>
<p>Therefore, I'm looking for a way to edit my local OSM data (which is the extract of <a href="http://download.geofabrik.de/europe/denmark.html">Denmark from Geofabrik</a>) without uploading the changes to OSM. Thus, the work flow will look as simple as:</p>
<ol>
<li>Import osm.pbf of Denmark</li>
<li>Modify OSM data</li>
<li>Export osm.pbf of Denmark</li>
</ol>
<p>I'm interested in suggestions how to implement this work flow by using existing open source tools, editors etc.. I work with Ubuntu 14.04.</p>
<p>Many thanks for your input.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-editing" rel="tag" title="see questions tagged &#39;editing&#39;">editing</span> <span class="post-tag tag-link-local" rel="tag" title="see questions tagged &#39;local&#39;">local</span> <span class="post-tag tag-link-pbf" rel="tag" title="see questions tagged &#39;pbf&#39;">pbf</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Feb '17, 11:10</strong></p>
<img src="https://secure.gravatar.com/avatar/b33683c10ecf24a95f6c7e368edb258f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PeBerlin&#39;s gravatar image" />
<p><span>PeBerlin</span><br />
<span class="score" title="46 reputation points">46</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PeBerlin has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Mar '17, 02:39</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-54827" class="comments-container">
&#10;</div>
<div id="comment-tools-54827" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54827-form-container" class="comment-form-container">
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

<span id="54848"></span>

<div id="answer-container-54848" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-54848-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54848-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-54848-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="PeBerlin has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Just to add to <a href="https://help.openstreetmap.org/users/3577/hjart">@Hjart</a>'s answer:</p>
<ul>
<li>Cut out the area of interest using either Osmosis or osmconvert</li>
<li>Open &amp; edit it in JOSM. (In order to avoid accidental uploading the data you can add upload=false in a JOSM file in XML format).</li>
<li>Save the edited data to a file (PBF or XML). I would recommend that you mark your changes in some way, perhaps using a scenario=xxx tag.</li>
<li>You can use osmosis or osmconvert to change your edited file into an OSM change format (.osc) if you can compare it with the original file. OSC is probably the best format for storing any given scenario as it will only contain the actual modifications.</li>
</ul>
<p>To apply your scenario merge either the OSC file or the JOSM file with all of Denmark. Push this through your OTP model.</p>
<p>You may also remove data which is not needed, such as building outlines etc, from the Denmark file before proceeding. Use osmfilter for this.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Mar '17, 10:32</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-54848" class="comments-container">
<span id="54849"></span>
<div id="comment-54849" class="comment">
<div id="post-54849-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Great, many thanks! That sounds like a reasonable work flow. I will go through these steps and see if I can manage it.</p>
</div>
<div id="comment-54849-info" class="comment-info">
<span class="comment-age">(01 Mar '17, 11:06)</span> <span class="comment-user userinfo">PeBerlin</span>
</div>
</div>
</div>
<div id="comment-tools-54848" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54848-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="54829"></span>

<div id="answer-container-54829" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-54829-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54829-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-54829-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="https://wiki.openstreetmap.org/wiki/JOSM">JOSM</a> with the <a href="https://wiki.openstreetmap.org/wiki/JOSM/Plugins/PBF">PBF</a> plugin can do what you want. All of Denmark is a considerable amount of data though, so you'll probably want to split up the pbf</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Feb '17, 12:18</strong></p>
<img src="https://secure.gravatar.com/avatar/6edf3a421a450237beae62ba93582637?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hjart&#39;s gravatar image" />
<p><span>Hjart</span><br />
<span class="score" title="2961 reputation points"><span>3.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hjart has 14 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-54829" class="comments-container">
<span id="54835"></span>
<div id="comment-54835" class="comment">
<div id="post-54835-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Many thanks for your answer! I will give JOSM a try. Do you have any specific advices which tools to use to first split and then merge the .osm files?</p>
</div>
<div id="comment-54835-info" class="comment-info">
<span class="comment-age">(28 Feb '17, 15:36)</span> <span class="comment-user userinfo">PeBerlin</span>
</div>
</div>
<span id="54842"></span>
<div id="comment-54842" class="comment">
<div id="post-54842-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Either osmosis or osmconvert. I'd try with latter &amp; stick with it if it works.</p>
</div>
<div id="comment-54842-info" class="comment-info">
<span class="comment-age">(28 Feb '17, 21:43)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-54829" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54829-form-container" class="comment-form-container">
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


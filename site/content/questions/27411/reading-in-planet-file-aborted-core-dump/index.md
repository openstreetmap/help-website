+++
type = "question"
title = "Reading in Planet File - Aborted Core Dump"
description = '''Am trying to import a planet file (have done this many times before) however my last 4 attempts (with different planet files) result in the following error. Reading in file: planet-latest.osm.pbf Processing: Node(2041920k 189.9k/s) Way(199297k 3.39k/s) Relation(47930 14.42/s)osm2pgsql: PolygonBuilde...'''
date = "2013-10-22T17:05:00Z"
lastmod = "2013-12-12T07:57:00Z"
weight = 27411
keywords = [ "osm2pgsql" ]
aliases = [ "/questions/27411" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Reading in Planet File - Aborted Core Dump](/questions/27411/reading-in-planet-file-aborted-core-dump)

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
<span id="post-27411-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27411-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-27411-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Am trying to import a planet file (have done this many times before) however my last 4 attempts (with different planet files) result in the following error.</p>
<pre><code>Reading in file: planet-latest.osm.pbf
Processing: Node(2041920k 189.9k/s) Way(199297k 3.39k/s) Relation(47930 14.42/s)osm2pgsql: PolygonBuilder.cpp:261: geos::geomgraph::EdgeRing* geos::operation::overlay::PolygonBuilder::findShell(std::vector&lt;geos::operation::overlay::MinimalEdgeRing*&gt;*): Assertion `shellCount &lt;= 1&#39; failed</code></pre>
<p>Any help would be much appreciated</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Oct '13, 17:05</strong></p>
<img src="https://secure.gravatar.com/avatar/69ac40fbb114bc39ef46a1abafb25059?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="daveyp1234&#39;s gravatar image" />
<p><span>daveyp1234</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="daveyp1234 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Oct '13, 17:43</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-27411" class="comments-container">
<span id="27562"></span>
<div id="comment-27562" class="comment">
<div id="post-27562-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Were you able to resolve this issue? I am having similar trouble.</p>
<p>processing way (1213k) at 0.25k/s (done 0 of 1)osm2pgsql: PolygonBuilder.cpp:261: geos::geomgraph::EdgeRing <em>geos::operation::overlay::PolygonBuilder::findShell(std::vector&lt;geos::operation::overlay::minimaledgering*&gt;</em>): Assertion `shellCount &lt;= 1' failed. Aborted (core dumped)</p>
<p>I am able to import small ammounts of data (Great Britian) but when I attempt to import other data such as europe or the planet I get the above error.</p>
<p>I have checked the version of geos that i am using, it is 3.4.2.</p>
<p>Any help would be appreciated.</p>
</div>
<div id="comment-27562-info" class="comment-info">
<span class="comment-age">(28 Oct '13, 11:26)</span> <span class="comment-user userinfo">George1372</span>
</div>
</div>
</div>
<div id="comment-tools-27411" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27411-form-container" class="comment-form-container">
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

<span id="27433"></span>

<div id="answer-container-27433" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-27433-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27433-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-27433-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The planet-131017.osm.pbf (available as planet-latest.osm.pbf for awhile) was incomplete. Please try another release.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Oct '13, 09:39</strong></p>
<img src="https://secure.gravatar.com/avatar/e79628d44a15e95c607f8c5007d0ccd2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Firefishy&#39;s gravatar image" />
<p><span>Firefishy ♦♦</span><br />
<span class="score" title="1296 reputation points"><span>1.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="36 badges"><span class="silver">●</span><span class="badgecount">36</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Firefishy has 14 accepted answers">29%</span></p>
</div>
</div>
<div id="comments-container-27433" class="comments-container">
<span id="27444"></span>
<div id="comment-27444" class="comment">
<div id="post-27444-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks, am already in the process of reading a file from 130814....I think the last 3 or 4 planet files (up to 131017) must have been incomplete as have tried a couple of those but got the same error.</p>
</div>
<div id="comment-27444-info" class="comment-info">
<span class="comment-age">(23 Oct '13, 15:50)</span> <span class="comment-user userinfo">daveyp1234</span>
</div>
</div>
<span id="27485"></span>
<div id="comment-27485" class="comment">
<div id="post-27485-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Have now tried with planet file 130814 and three others. Same result same error.</p>
</div>
<div id="comment-27485-info" class="comment-info">
<span class="comment-age">(25 Oct '13, 08:20)</span> <span class="comment-user userinfo">daveyp1234</span>
</div>
</div>
<span id="27487"></span>
<div id="comment-27487" class="comment">
<div id="post-27487-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Importing planet dumps are extremely taxing on any system, you may want to do a prime95 burnin-test to check the machine for hardware faults. Download mprime here: <a href="http://www.mersenne.org/freesoft/">http://www.mersenne.org/freesoft/</a> and follow the test described here: <a href="https://wiki.archlinux.org/index.php/Stress_Test#Mprime_.28Prime95_for_Windows_and_MacOS.29">https://wiki.archlinux.org/index.php/Stress_Test#Mprime_.28Prime95_for_Windows_and_MacOS.29</a></p>
</div>
<div id="comment-27487-info" class="comment-info">
<span class="comment-age">(25 Oct '13, 10:22)</span> <span class="comment-user userinfo">Firefishy ♦♦</span>
</div>
</div>
</div>
<div id="comment-tools-27433" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27433-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="29000"></span>

<div id="answer-container-29000" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29000-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29000-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-29000-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>After several attempts over even more weeks finally managed to resolve the issue by using osm2pgsql 0.81 (version on github is 0.85). Have tried the this twice to confirm the resolution.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Dec '13, 07:57</strong></p>
<img src="https://secure.gravatar.com/avatar/69ac40fbb114bc39ef46a1abafb25059?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="daveyp1234&#39;s gravatar image" />
<p><span>daveyp1234</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="daveyp1234 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-29000" class="comments-container">
&#10;</div>
<div id="comment-tools-29000" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29000-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="27503"></span>

<div id="answer-container-27503" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-27503-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27503-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-27503-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Assuming your hardware checks out, you may want to check your geos version as that's where the error message is arising from. <code>geos-config --version</code> will tell you what version. 3.3 has fixed some bugs present in 3.2</p>
<p>You can also open a ticket on the issue tracker at <a href="https://github.com/openstreetmap/osm2pgsql/issues">https://github.com/openstreetmap/osm2pgsql/issues</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Oct '13, 04:37</strong></p>
<img src="https://secure.gravatar.com/avatar/5634c46072077e10f5b7c0da9b4bbb62?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pnorman&#39;s gravatar image" />
<p><span>pnorman</span><br />
<span class="score" title="2352 reputation points"><span>2.4k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="21 badges"><span class="silver">●</span><span class="badgecount">21</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pnorman has 9 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-27503" class="comments-container">
&#10;</div>
<div id="comment-tools-27503" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27503-form-container" class="comment-form-container">
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


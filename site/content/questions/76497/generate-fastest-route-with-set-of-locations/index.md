+++
type = "question"
title = "Generate fastest route with set of locations"
description = '''I have a set of locations, the workers need to visit this locations (view below image with points) i need to find the best possible route along this set of points no matter where does it start. I tried with the &quot;trip/&quot; API but it creates new points that do not exist in the original points, and this ...'''
date = "2020-09-07T19:06:00Z"
lastmod = "2020-09-08T21:40:00Z"
weight = 76497
keywords = [ "osrm", "trip" ]
aliases = [ "/questions/76497" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Generate fastest route with set of locations](/questions/76497/generate-fastest-route-with-set-of-locations)

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
<span id="post-76497-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76497-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-76497-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a set of locations, the workers need to visit this locations (view below image with points) i need to find the best possible route along this set of points no matter where does it start.</p>
<p>I tried with the "trip/" API but it creates new points that do not exist in the original points, and this creates a terrible route.</p>
<p>Am i missing something in parameters?</p>
<pre><code>http://router.project-osrm.org/trip/v1/driving/-90.499807,38.82392;-90.497916,38.822408;-90.498461,38.822241;-90.496597,38.82351;-90.496352,38.823821;-90.49809,38.825024;-90.495743,38.823304;-90.497415,38.824089;-90.498851,38.823079;-90.49957,38.822156;-90.500771,38.823087;-90.49861,38.82196;-90.496589,38.82255;-90.497906,38.82286;-90.49696,38.822816;-90.49897,38.822577;-90.499736,38.823182;-90.498388,38.823185;-90.498142,38.822603;-90.496481,38.823885;-90.497778,38.824796;-90.497826,38.82337;-90.498705,38.822402;-90.500444,38.822877;-90.497618,38.822596;-90.49804,38.823532;-90.49696,38.822301;-90.499445,38.823499;-90.499071,38.823257;-90.497862,38.823564;-90.496668,38.823013;-90.49884,38.823535;-90.497157,38.822219;-90.49719,38.824389;-90.497107,38.822891;-90.497237,38.822968;-90.499633,38.823079;-90.497061,38.823837;-90.498126,38.823626;-90.497969,38.823923;-90.497473,38.823134;-90.498297,38.825059;-90.499794,38.822598;-90.497592,38.823214;-90.497783,38.82433;-90.498189,38.824087;-90.500557,38.822791;-90.498589,38.82233;-90.498388,38.822737;-90.500666,38.823171;-90.498729,38.823003;-90.497878,38.8249;-90.497381,38.823502;-90.49828,38.8231;-90.497951,38.823454;-90.498483,38.825039;-90.498259,38.822677;-90.499498,38.824195;-90.49817,38.821799;-90.497142,38.823337;-90.498742,38.823433;-90.499237,38.823305;-90.497186,38.823919;-90.499503,38.822995;-90.50002,38.822828;-90.49881,38.822496;-90.500109,38.822332;-90.496935,38.823773;-90.498629,38.822908;-90.500189,38.823052;-90.497524,38.823586;-90.498032,38.822502;-90.499083,38.822658;-90.498594,38.82339;-90.497649,38.824736;-90.49619,38.823234;-90.498351,38.822154;-90.498219,38.822085;-90.499487,38.822238;-90.497439,38.824546;-90.500558,38.823266;-90.498143,38.824573;-90.499182,38.82447;-90.500382,38.822984;-90.496852,38.822382;-90.498783,38.824051;-90.498525,38.823872;-90.496953,38.824221;-90.499716,38.824013;-90.497348,38.822449;-90.499709,38.823049;-90.498075,38.823999;-90.499417,38.822915;-90.500137,38.82364;-90.499989,38.823707;-90.500451,38.823362;-90.499698,38.822076;-90.499604,38.82411;-90.496008,38.823548?steps=true&amp;overview=full</code></pre>
<p>This is the original set of locations <img src="https://help.openstreetmap.org/upfiles/Screen_Shot_2020-09-07_at_12.27.02_PM.png" alt="alt text" /></p>
<p>And this is what returns from OSRM, clearly there are additional points, and its wrong <img src="https://help.openstreetmap.org/upfiles/Screen_Shot_2020-09-07_at_12.30.35_PM_m0Cbxxx.png" alt="alt text" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osrm" rel="tag" title="see questions tagged &#39;osrm&#39;">osrm</span> <span class="post-tag tag-link-trip" rel="tag" title="see questions tagged &#39;trip&#39;">trip</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Sep '20, 19:06</strong></p>
<img src="https://secure.gravatar.com/avatar/5e105c0e54583da7b1bc5de4a026ace6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RonEskinder&#39;s gravatar image" />
<p><span>RonEskinder</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RonEskinder has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Sep '20, 19:54</strong> </span></p>
</div>
</div>
<div id="comments-container-76497" class="comments-container">
<span id="76505"></span>
<div id="comment-76505" class="comment">
<div id="post-76505-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What are you actually plotting to produce the second view? I swapped the geometry output to geojson and the linestring it produces only shows a path along the expected streets.</p>
</div>
<div id="comment-76505-info" class="comment-info">
<span class="comment-age">(08 Sep '20, 07:14)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
<span id="76516"></span>
<div id="comment-76516" class="comment">
<div id="post-76516-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>"geometry": "ww}kFvujgPGGj@{@<a href="https://help.openstreetmap.org/users/148/osmnoase"><code>@o</code></a><code>@FMFIHKNUFKNWHMDGb</code><a href="https://help.openstreetmap.org/users/148/osmnoase"><code>@o</code></a><code>@Y</code>@iDlFIKSUQSu@_AIIoA{AKQCYDYNUJMDIHKDIXc@FK<a href="https://help.openstreetmap.org/users/29/mishok13"><code>@m</code></a><code>@HMVa@FKPYLSXc@NUHMh@}@PUHCDAL?LFPVv@zA[f@EDQXOV[d@EHOTILSXCDOVCBINOTMROTOVEFe@r@~GsKJR^t@LVP\\@DNVm@~@EFQVQXOTJMzAaCzAxCDJM@KJGJQVABMRQVOTQXt@fALPPVuAqBQXOTq@dAU\\GLCBJQ^f@FFr@~@{AoBFKGJYd@W</code>@GJCTBTHHNR@@LPPTMQm@u@IKu@_AQUe@k@",</p>
</div>
<div id="comment-76516-info" class="comment-info">
<span class="comment-age">(08 Sep '20, 15:18)</span> <span class="comment-user userinfo">RonEskinder</span>
</div>
</div>
</div>
<div id="comment-tools-76497" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76497-form-container" class="comment-form-container">
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

<span id="76519"></span>

<div id="answer-container-76519" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76519-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76519-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-76519-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="RonEskinder has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The decoder on <a href="https://developers.google.com/maps/documentation/utilities/polylineutility">this page</a> seems to work if you replace the <code>\\</code>'s with <code>\</code>. i.e. using: <code>ww}kFvujgPGGj@{@`</code><a href="https://help.openstreetmap.org/users/148/osmnoase"><code>@o</code></a><code>@FMFIHKNUFKNWHMDGb</code><a href="https://help.openstreetmap.org/users/148/osmnoase"><code>@o</code></a><code>@Y`@iDlFIKSUQSu@_AIIoA{AKQCYDYNUJMDIHKDIXc@FK`</code><a href="https://help.openstreetmap.org/users/29/mishok13"><code>@m</code></a><code>@HMVa@FKPYLSXc@NUHMh@}@PUHCDAL?LFPVv@zA[f@EDQXOV[d@EHOTILSXCDOVCBINOTMROTOVEFe@r@~GsKJR^t@LVP\@DNVm@~@EFQVQXOTJMzAaCzAxCDJM@KJGJQVABMRQVOTQXt@fALPPVuAqBQXOTq@dAU\GLCBJQ^f@FFr@~@{AoBFKGJYd@W`@GJCTBTHHNR@@LPPTMQm@u@IKu@_AQUe@k@</code></p>
<p>My guess is that although the <a href="https://developers.google.com/maps/documentation/utilities/polylinealgorithm">documentation page</a> says:</p>
<blockquote>
<p>Note that the backslash is interpreted as an escape character within string literals. Any output of this utility should convert backslash characters to double-backslashes within string literals.</p>
</blockquote>
<p>The interactive encoder does not seem to (un)do this. Reversing just the first <code>\\</code> appears to follow the path for longer before the sudden onset of brownian motion.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Sep '20, 21:40</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</img>
</div>
</div>
<div id="comments-container-76519" class="comments-container">
&#10;</div>
<div id="comment-tools-76519" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76519-form-container" class="comment-form-container">
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


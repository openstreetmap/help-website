+++
type = "question"
title = "Putting a place at a point in iD"
description = '''I have this field note,  24.1798149, 120.8687728 1 meter diameter 1.5 meter tall metal water tank, 1 meter north of here.  that I want to enter into the map using the iD editor. I don&#x27;t want to use JOSM, I don&#x27;t want to use level0. How do I get that tank to that point? (Here are some screenshots fro...'''
date = "2021-09-22T00:13:00Z"
lastmod = "2021-10-19T16:45:00Z"
weight = 81849
keywords = [ "ideditor" ]
aliases = [ "/questions/81849" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [Putting a place at a point in iD](/questions/81849/putting-a-place-at-a-point-in-id)

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
<span id="post-81849-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81849-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81849-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have this field note,</p>
<blockquote>
<p>24.1798149, 120.8687728 1 meter diameter 1.5 meter tall metal water tank, 1 meter north of here.</p>
</blockquote>
<p>that I want to enter into the map using the iD editor.</p>
<p>I don't want to use JOSM, I don't want to use level0.</p>
<p>How do I get that tank to that point?</p>
<p>(Here are some screenshots from when I finally solved the problem later:)</p>
<p><img src="https://help.openstreetmap.org/upfiles/20211010T203100.jpg" alt="alt text" /> <img src="https://help.openstreetmap.org/upfiles/20211010T203433.jpg" alt="alt text" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ideditor" rel="tag" title="see questions tagged &#39;ideditor&#39;">ideditor</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Sep '21, 00:13</strong></p>
<img src="https://secure.gravatar.com/avatar/47edd1ee4d973c50bbe7991bb063d09d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jidanni&#39;s gravatar image" />
<p><span>jidanni</span><br />
<span class="score" title="339 reputation points">339</span><span title="32 badges"><span class="badge1">●</span><span class="badgecount">32</span></span><span title="36 badges"><span class="silver">●</span><span class="badgecount">36</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jidanni has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Oct '21, 13:38</strong> </span></p>
</div>
</div>
<div id="comments-container-81849" class="comments-container">
<span id="81873"></span>
<div id="comment-81873" class="comment">
<div id="post-81873-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>It's worth spending a bit of time think about the accuracy of the data that you're using above. See <a href="https://wiki.gis.com/wiki/index.php/Decimal_degrees">here</a> for a discussion of the implied accuracy of various numbers of decimal places (and do the maths to allow for your latitude - the higher your latitude, the shorter is the distance corresponding to one degree of longitude).</p>
<p>You've quoted 7 decimal places, but as you're using a handheld GPS or phone the best you can expect to get is a few meters either way (if you're in tree cover up a hill in Taiwan, probably less).</p>
<p>When transferring this to OSM you'll need to compare several difference sources - both your recorded position, and also what imagery is available, and other people's GPS traces too if possible. You'll want to add the feature to OSM using as many sources as possible, not just your one lat/long value.</p>
</div>
<div id="comment-81873-info" class="comment-info">
<span class="comment-age">(22 Sep '21, 22:03)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="81880"></span>
<div id="comment-81880" class="comment">
<div id="post-81880-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<ol>
<li><p>Aerial photography won't help: in forests, one meter high water tanks just look like forest, as the canopy covers them.</p></li>
<li><p>Water tanks might be lifesavers.</p></li>
<li><p>Places might be off the beaten path: no traces available.</p></li>
<li><p>Fine. Shave off some digits. But iD can't place a point at a given longitude, latitude, even if we are talking about just 24.000,121.000 .</p></li>
<li><p>Also, let's say everybody just owns cheap cellphones. Well, iD doesn't allow people to put points where cheap cellphones probably mean. One is only allowed to make traces, which are in fact just points from those cheap cellphones in the first place.</p></li>
</ol>
<p>So to enter our one point, one needs to upload a trace.</p>
</div>
<div id="comment-81880-info" class="comment-info">
<span class="comment-age">(23 Sep '21, 07:01)</span> <span class="comment-user userinfo">jidanni</span>
</div>
</div>
</div>
<div id="comment-tools-81849" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81849-form-container" class="comment-form-container">
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

4 Answers:

</div>

</div>

<span id="81850"></span>

<div id="answer-container-81850" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81850-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81850-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-81850-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi, you can do it with the 'Measurement Tool' in the iD editor.</p>
<p>Search for your coords on the OSM frontpage:- <a href="https://tinyurl.com/6jny6xvh">https://tinyurl.com/6jny6xvh</a></p>
<p>Open the iD editor.</p>
<p>Place a point in roughly the correct position.</p>
<p>Highlight the point.</p>
<p>Open the 'Map Data' panel from the menu on the right of the screen.</p>
<p>Click/open the 'Show Measurement Panel'</p>
<p>Zoom in as far as you can onto your point.</p>
<p>Move your point slowly to the exact coords, you can see the coords change in the measurement panel.</p>
<p>You have to have a very steady mouse movement.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Sep '21, 08:16</strong></p>
<img src="https://secure.gravatar.com/avatar/e3283a6b5f83e16214ec39a1478f64f0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BCNorwich&#39;s gravatar image" />
<p><span>BCNorwich</span><br />
<span class="score" title="6299 reputation points"><span>6.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="44 badges"><span class="silver">●</span><span class="badgecount">44</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BCNorwich has 44 accepted answers">20%</span></p>
</img>
</div>
</div>
<div id="comments-container-81850" class="comments-container">
<span id="81852"></span>
<div id="comment-81852" class="comment">
<div id="post-81852-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Leaving the part with "1 meter north of here".</p>
<p>Starting from the point placed on the coordinates you can create a line. It's length is also shown in the measurement panel. Place the 2nd line node so that you get a line of 1m length. Delete the first node.</p>
</div>
<div id="comment-81852-info" class="comment-info">
<span class="comment-age">(22 Sep '21, 08:31)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="81864"></span>
<div id="comment-81864" class="comment">
<div id="post-81864-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I think it is terrible of iD to force users to "Move your point slowly to the exact coords, you can see the coords change in the measurement panel.</p>
<p>You have to have a very steady mouse movement."</p>
<p>OK, I will learn Level0, to allow me to place a point at the exact point.</p>
<p>Then I will create the tank nearby, and move it over that point.</p>
<p>Then I will delete the point.</p>
<p>Sorry about wasting a node in the process.</p>
<p>Oh, yeah. Then I'll move the tank north like you said.</p>
</div>
<div id="comment-81864-info" class="comment-info">
<span class="comment-age">(22 Sep '21, 20:58)</span> <span class="comment-user userinfo">jidanni</span>
</div>
</div>
<span id="81867"></span>
<div id="comment-81867" class="comment">
<div id="post-81867-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Well, I guess for the average user of iD it is much harder to obtain such precise coordinates with available GPS devices than placing a node based on aerial imagery.</p>
<p>I also wonder if not even in your case the error by mouse jitter is much smaller than the GPS precision error.</p>
</div>
<div id="comment-81867-info" class="comment-info">
<span class="comment-age">(22 Sep '21, 21:16)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="81870"></span>
<div id="comment-81870" class="comment">
<div id="post-81870-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Odd that iD lacks such a basic feature.</p>
</div>
<div id="comment-81870-info" class="comment-info">
<span class="comment-age">(22 Sep '21, 21:41)</span> <span class="comment-user userinfo">jidanni</span>
</div>
</div>
<span id="81934"></span>
<div id="comment-81934" class="comment not_top_scorer">
<div id="post-81934-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Even if I had the coordinates handed to me on a piece of paper by the granddaddy of GPS himself, I can't avoid mouse jitter because there is no way to simply type them in in iD.</p>
</div>
<div id="comment-81934-info" class="comment-info">
<span class="comment-age">(24 Sep '21, 14:57)</span> <span class="comment-user userinfo">jidanni</span>
</div>
</div>
<span id="81935"></span>
<div id="comment-81935" class="comment not_top_scorer">
<div id="post-81935-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<blockquote>
<p>I can't avoid mouse jitter because there is no way to simply type them in in iD.</p>
</blockquote>
<p>It doesn't matter - all GPS co-ordinates that relate to objects in the real world are inaccurate.</p>
</div>
<div id="comment-81935-info" class="comment-info">
<span class="comment-age">(24 Sep '21, 15:33)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="81936"></span>
<div id="comment-81936" class="comment not_top_scorer">
<div id="post-81936-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I couldn't even enter the coordinates to map the Greenwich Observatory.</p>
</div>
<div id="comment-81936-info" class="comment-info">
<span class="comment-age">(24 Sep '21, 15:45)</span> <span class="comment-user userinfo">jidanni</span>
</div>
</div>
<span id="81937"></span>
<div id="comment-81937" class="comment">
<div id="post-81937-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Funny you mention that - you might get a surprise:</p>
<p><a href="https://www.openstreetmap.org/user/PlaneMad/diary/39398">https://www.openstreetmap.org/user/PlaneMad/diary/39398</a></p>
</div>
<div id="comment-81937-info" class="comment-info">
<span class="comment-age">(24 Sep '21, 16:02)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="82108"></span>
<div id="comment-82108" class="comment not_top_scorer">
<div id="post-82108-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Indeed, above I added photos of how I used the Measurement tool. Though it is hard with the mouse to get an exact 1 meter long line, and 1 meter diameter circle (via drawing a triangle and then using the circle tool,) I'm happy with the close call. The main point is indeed I finally got the starting point at an exact X,Y via level0 ! (Though alas after his temporary role in life was over I had to delete him.) Anyway, there's my baby!: <a href="https://www.openstreetmap.org/way/991670713">https://www.openstreetmap.org/way/991670713</a> . I'm the proud father. No cigars. (Man you would never expect there was a water tank there in the dense forest unless you almost bumped into it. Yes, 25 years ago there was traces of a house too, but I didn't see any now. Anyway, as the tank is made of some non-corrodable metal it will surely be there long after yours truly...)</p>
</div>
<div id="comment-82108-info" class="comment-info">
<span class="comment-age">(10 Oct '21, 13:43)</span> <span class="comment-user userinfo">jidanni</span>
</div>
</div>
</div>
<div id="comment-tools-81850" class="comment-tools">
<span class="comments-showing"> showing 5 of 9 </span> <a href="#" class="show-all-comments-link">show 4 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-81850-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="81949"></span>

<div id="answer-container-81949" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81949-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81949-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-81949-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Saying</p>
<pre><code>I don&#39;t want to use JOSM, I don&#39;t want to use level0.</code></pre>
<p>is being unnecessarily restrictive. Logically, it makes sense to pick the best tool for the job - and that varies. If I want to put a small plant in a pot I'd use a trowel, but if I'm digging a big hole in the garden for a tree I'd use a spade. It would be silly to try and use either tool for the other job. Looking at the <a href="https://hdyc.neis-one.org/?SomeoneElse">OSM editors I've used</a> there are 4 or 5 that I've used over 100 times - the best tool for that particular job in each case.</p>
<p>There are some people that say that "everyone should use JOSM for everything". I wholeheartedly disagree with that approach, although JOSM has more functionality than any other OSM editor it isn't best at everything - iD is great at what it sets out to do, so is Potlatch3, so is level0, and Vespucci, and Go Map!!... However in your case you have a specific requirement, and "an editor that is not iD" is the best answer to that requirement.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Sep '21, 11:15</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-81949" class="comments-container">
<span id="81950"></span>
<div id="comment-81950" class="comment">
<div id="post-81950-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>OK, I will use another editor to put one vanilla node on the map, and then switch back to iD (the official OSM editor, as it is bound to the Edit button) to complete the task.</p>
<p>I cannot touch JOSM: one cannot rebind the mouse, so any use of its backwards bindings ruins muscle memory of all other mapping systems for months.</p>
<p>It is a shame that the iD maintainers really do insist that allowing users to place a point at exactly X,Y should never be allowed.</p>
</div>
<div id="comment-81950-info" class="comment-info">
<span class="comment-age">(25 Sep '21, 14:21)</span> <span class="comment-user userinfo">jidanni</span>
</div>
</div>
<span id="82101"></span>
<div id="comment-82101" class="comment">
<div id="post-82101-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The saga continues at <a href="https://help.openstreetmap.org/questions/82091/putting-a-place-at-a-point-in-level0">https://help.openstreetmap.org/questions/82091/putting-a-place-at-a-point-in-level0</a> .</p>
</div>
<div id="comment-82101-info" class="comment-info">
<span class="comment-age">(09 Oct '21, 10:06)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="82107"></span>
<div id="comment-82107" class="comment">
<div id="post-82107-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Indeed, it took a few days to figure out but now I finally made a node at an exact X,Y via level0, and can complete the rest of the task with iD!</p>
</div>
<div id="comment-82107-info" class="comment-info">
<span class="comment-age">(10 Oct '21, 13:22)</span> <span class="comment-user userinfo">jidanni</span>
</div>
</div>
</div>
<div id="comment-tools-81949" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81949-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="81938"></span>

<div id="answer-container-81938" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81938-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81938-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-81938-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I would agree with others opinions regarding GPS accuracy. You could create a short trace from a walk by the local road to then around the tank. Another solution if you are determined to use your co-ords is to substitute them into this link. <a href="https://www.openstreetmap.org/?mlat=52.3211&amp;mlon=-0.1864#map=15/52.3211/-0.1864">https://www.openstreetmap.org/?mlat=52.3211&amp;mlon=-0.1864#map=15/52.3211/-0.1864</a> then click on the + to magnify and zoom right in. Then open the iD editor. Your point should be in the centre of the display, or at least close enough to put a location for the tank. I just put your co-ords into the OSM map page search box and got this. just zoom in maybe.</p>
<p><img src="https://help.openstreetmap.org/upfiles/co_ords.JPG" alt="alt text" /></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Sep '21, 16:16</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Sep '21, 16:23</strong> </span></p>
</div>
</div>
<div id="comments-container-81938" class="comments-container">
<span id="81945"></span>
<div id="comment-81945" class="comment">
<div id="post-81945-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sure, near the center of display, just zoom in etc... But it is so frustrating that no crosshairs, no thumbtack, no upsidedown teardrop marker will ever be provided, to show just where near the center of the screen. Sure, on OSM.ORG one can get a marker. But alas iD will never give the user such a clue to know where a given X,Y is.</p>
</div>
<div id="comment-81945-info" class="comment-info">
<span class="comment-age">(25 Sep '21, 07:28)</span> <span class="comment-user userinfo">jidanni</span>
</div>
</div>
<span id="81947"></span>
<div id="comment-81947" class="comment">
<div id="post-81947-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Potlatch does have co-ord read out you could try it.</p>
</div>
<div id="comment-81947-info" class="comment-info">
<span class="comment-age">(25 Sep '21, 08:29)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="82089"></span>
<div id="comment-82089" class="comment">
<div id="post-82089-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>"Running Potlatch on Linux is not yet established" https://github.com/systemed/potlatch3</p>
</div>
<div id="comment-82089-info" class="comment-info">
<span class="comment-age">(09 Oct '21, 02:35)</span> <span class="comment-user userinfo">jidanni</span>
</div>
</div>
<span id="82098"></span>
<div id="comment-82098" class="comment">
<div id="post-82098-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, useful info. I have installed linux mint on an old pc. I may try these instructions. <a href="https://www.openstreetmap.org/user/SomeoneElse/diary/395603">https://www.openstreetmap.org/user/SomeoneElse/diary/395603</a></p>
</div>
<div id="comment-82098-info" class="comment-info">
<span class="comment-age">(09 Oct '21, 08:33)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="82100"></span>
<div id="comment-82100" class="comment">
<div id="post-82100-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>For the avoidance of doubt, the complete sentence referred to above ^^ is "Running Potlatch on Linux is not yet established (other than via the Wine emulation environment)."</p>
<p>Potlatch3 on Linux under Wine does work, and works well enough for me to use it there; there are some issues with loading background imagery at the same time as scrolling, but as your requirement here is "an editor that is not iD" rather than "I need to do something only supported in Potlatch2" I'd choose one of the many other options.</p>
</div>
<div id="comment-82100-info" class="comment-info">
<span class="comment-age">(09 Oct '21, 10:05)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-81938" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81938-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="82182"></span>

<div id="answer-container-82182" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82182-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82182-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-82182-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>A trace is much more useful and checkable. For example walk along the road for say 50 metres detour to the tank walk slowly around it a couple of times and return to the road and walk along the road again for a 50 metres. You can now check that trace against the mapped road and the other traces. If the trace follows the road ok the detour around the tank should be ok also and the tank is then easy to position. Sometimes big distinctive trees are identifiable on Bing or other sources and may assist location, If you can pick some out during the survey. Counting paces to and from the road may help. A trace will enable you to map the paths to and from the tank.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Oct '21, 11:46</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</div>
</div>
<div id="comments-container-82182" class="comments-container">
<span id="82252"></span>
<div id="comment-82252" class="comment">
<div id="post-82252-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>OK but: we often can't walk "around" things without falling off cliffs or getting mired in thickets or quicksand. We are lucky enough to be able to walk back the way we came in. This is no day in the park.</p>
<p>Bing etc. just show monotonous forest with no special different trees. Nor can paths be seen under the trees. Nor has anybody else mapped a network of trails that we can build on top of.</p>
<p>Sure traces made with pro surveyor equipment may be great, but cellphone traces walking in straight lines look like "v~^~v~" waving all over the place. Anyway, even if the coordinates of an object were engraved in stone by the daddy of GPS him/herself, iD can't use them.</p>
</div>
<div id="comment-82252-info" class="comment-info">
<span class="comment-age">(19 Oct '21, 16:45)</span> <span class="comment-user userinfo">jidanni</span>
</div>
</div>
</div>
<div id="comment-tools-82182" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82182-form-container" class="comment-form-container">
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


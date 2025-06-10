+++
type = "question"
title = "How to get building heights for mapping?"
description = '''I&#x27;m wondering what are acceptable sources for building heights, and especially how approximate we can be. Some places have freely licensed data for building heights, derived from Lidar, or other sources. That&#x27;s great, but when this is not available, what can we do? I&#x27;ve just started to do some 3d ma...'''
date = "2018-07-04T18:29:00Z"
lastmod = "2018-07-08T08:06:00Z"
weight = 64533
keywords = [ "building", "3d" ]
aliases = [ "/questions/64533" ]
osqa_answers = 5
osqa_accepted = false
+++

<div class="headNormal">

# [How to get building heights for mapping?](/questions/64533/how-to-get-building-heights-for-mapping)

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
<span id="post-64533-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64533-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-64533-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm wondering what are acceptable sources for building heights, and especially how approximate we can be.</p>
<p>Some places have freely licensed data for building heights, derived from Lidar, or other sources. That's great, but when this is not available, what can we do?</p>
<p>I've just started to do some 3d mapping. To get height values, I've been estimating the ratio of height to width, using the measure tool in Josm to determine the width, and calculating a value for the height from these two. It's not a very accurate system.</p>
<p>Is it an acceptable approach, when lacking better quality data? Are there better systems?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-building" rel="tag" title="see questions tagged &#39;building&#39;">building</span> <span class="post-tag tag-link-3d" rel="tag" title="see questions tagged &#39;3d&#39;">3d</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Jul '18, 18:29</strong></p>
<img src="https://secure.gravatar.com/avatar/f88a467aa884aeb760041004f62448ee?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="keithonearth&#39;s gravatar image" />
<p><span>keithonearth</span><br />
<span class="score" title="2939 reputation points"><span>2.9k</span></span><span title="56 badges"><span class="badge1">●</span><span class="badgecount">56</span></span><span title="76 badges"><span class="silver">●</span><span class="badgecount">76</span></span><span title="108 badges"><span class="bronze">●</span><span class="badgecount">108</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="keithonearth has 3 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-64533" class="comments-container">
&#10;</div>
<div id="comment-tools-64533" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64533-form-container" class="comment-form-container">
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

<span id="64559"></span>

<div id="answer-container-64559" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64559-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64559-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-64559-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I usually take pictures of the stuff I map, so I have used some guesstimates to determine heights.</p>
<p>I.e. I have a picture of a building im trying to map:</p>
<ol>
<li>It has a door, I assume the door is 2.2m high.</li>
<li>Measure the height of the door in cm/pixels,</li>
<li>Calculate how many real life meters a cm/pixel on the picture is.</li>
<li>Measure the height of the building and muliply it by your value.</li>
</ol>
<p>Now you have an estimate of the building height.</p>
<p>If you area has lidar-imagery available (and open) there is normally a point cloud where you can pan and zoom and rotate and look at objects in 3D and measure.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Jul '18, 09:22</strong></p>
<img src="https://secure.gravatar.com/avatar/f882e7865ffe23339fbaa71c9f576065?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="FredrikLindseth&#39;s gravatar image" />
<p><span>FredrikLindseth</span><br />
<span class="score" title="815 reputation points">815</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="35 badges"><span class="bronze">●</span><span class="badgecount">35</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="FredrikLindseth has 2 accepted answers">13%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Jul '18, 09:24</strong> </span></p>
</div>
</div>
<div id="comments-container-64559" class="comments-container">
&#10;</div>
<div id="comment-tools-64559" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64559-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="64537"></span>

<div id="answer-container-64537" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64537-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64537-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-64537-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Personally, if I believe I can estimate it to the closest meter (which means it's pretty short or it's next to an object of known, similar height) I'll go ahead and add the integer height -- always with no decimal point, to indicate the lack of precision.</p>
<p>Failing that, I'll just add a <code>building:levels=*</code> tag. Whether that's any use to 3D mapping, I dunno, certainly the renderers could use it as a rough height estimate if they were so inclined. But if you're doing complex things like roof shapes, it's probably no help.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Jul '18, 21:59</strong></p>
<img src="https://secure.gravatar.com/avatar/977d95e2184a885d9a01fb3297225872?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jmapb&#39;s gravatar image" />
<p><span>jmapb</span><br />
<span class="score" title="3387 reputation points"><span>3.4k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="61 badges"><span class="bronze">●</span><span class="badgecount">61</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jmapb has 22 accepted answers">22%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Jul '18, 22:09</strong> </span></p>
</div>
</div>
<div id="comments-container-64537" class="comments-container">
<span id="64552"></span>
<div id="comment-64552" class="comment">
<div id="post-64552-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Mapping <code>building:levels</code> is very useful for 3D rendering, and it's indeed used by rendering software to estimate building heights. In areas where there are no legal sources for building heights, it's quite common to use <code>building:levels</code> almost everywhere and add heights only for the couple "special" buildings (towers, churches etc.) where that approach falls short. Of course, having heights for all buildings would be ideal, but counting levels is often a lot easier and therefore a good first step.</p>
</div>
<div id="comment-64552-info" class="comment-info">
<span class="comment-age">(05 Jul '18, 17:23)</span> <span class="comment-user userinfo">Tordanik</span>
</div>
</div>
<span id="64553"></span>
<div id="comment-64553" class="comment">
<div id="post-64553-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Good to know!</p>
</div>
<div id="comment-64553-info" class="comment-info">
<span class="comment-age">(05 Jul '18, 19:02)</span> <span class="comment-user userinfo">jmapb</span>
</div>
</div>
</div>
<div id="comment-tools-64537" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64537-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="64561"></span>

<div id="answer-container-64561" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64561-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64561-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-64561-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are free apps for phones measure the heights of buildings too. This is an example... <a href="https://itunes.apple.com/au/app/height-and-distance/id722926841?mt=8">https://itunes.apple.com/au/app/height-and-distance/id722926841?mt=8</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Jul '18, 14:57</strong></p>
<img src="https://secure.gravatar.com/avatar/e5674dd96938593e0af5130dfffe0f90?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nevw&#39;s gravatar image" />
<p><span>nevw</span><br />
<span class="score" title="9843 reputation points"><span>9.8k</span></span><span title="26 badges"><span class="badge1">●</span><span class="badgecount">26</span></span><span title="90 badges"><span class="silver">●</span><span class="badgecount">90</span></span><span title="178 badges"><span class="bronze">●</span><span class="badgecount">178</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nevw has 32 accepted answers">9%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Jul '18, 15:15</strong> </span></p>
</div>
</div>
<div id="comments-container-64561" class="comments-container">
<span id="64563"></span>
<div id="comment-64563" class="comment">
<div id="post-64563-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yeah I've tried that one, and a couple others. Comparing the results to tall buildings of known height, they are always wildly inaccurate. It's too bad because this is exactly the sort of magic that smartphones were hyped to be capable of. If there's an app out there that can do better, I'd love to try it. (I'm on iOS.)</p>
</div>
<div id="comment-64563-info" class="comment-info">
<span class="comment-age">(06 Jul '18, 16:53)</span> <span class="comment-user userinfo">jmapb</span>
</div>
</div>
</div>
<div id="comment-tools-64561" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64561-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="64564"></span>

<div id="answer-container-64564" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64564-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64564-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-64564-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you can't get an accurate measurement from an iPhone why not use old-school trignomentry? You can measure the distance to the base of the building (either physically, or <a href="https://duckduckgo.com/html?q=convert%20latitude%20and%20longitude%20to%20distance">calculate</a> based on lat and long, and can <a href="http://www.mathwords.com/s/sohcahtoa.htm">calculate</a> the height based on the measured distance and angle.</p>
<p>If you can get 5 degree accuracy with a cheap plastic protractor then you'll get the height of a 100m building at 100m away to within 20m, which is way more accurate than if you were sat on the roof with a regular GPS :)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Jul '18, 18:04</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-64564" class="comments-container">
<span id="64565"></span>
<div id="comment-64565" class="comment">
<div id="post-64565-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yeah you can make a pretty good 3D model this way, if you have the patience. I would still doubt that you'd get sub-meter accuracy, so I'd advise to round to the nearest integer to avoid giving the impression that a height is an official or exact number.</p>
<p>Maybe consider tagging with <code>source:height=calculated estimate</code>, <code>source:height=city building records</code>, <code>source:height=lidar</code>, etc.</p>
<p>I've never had a GPS give me decent enough elevation that I'd trust it for building height. If I could get to the roof, I'd just drop a cannonball off the top and time how long it takes to hit the ground ;)</p>
</div>
<div id="comment-64565-info" class="comment-info">
<span class="comment-age">(06 Jul '18, 18:21)</span> <span class="comment-user userinfo">jmapb</span>
</div>
</div>
<span id="64566"></span>
<div id="comment-64566" class="comment">
<div id="post-64566-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I hadn't thought of using a plastic protractor, but I was imagining using a sextant to do this, and came to the conclusion that I really wasn't willing to go that far. It seems like there should be a way to get the angle from a photo, based on the focal length, and number of pixels from base to top of the building.</p>
</div>
<div id="comment-64566-info" class="comment-info">
<span class="comment-age">(06 Jul '18, 18:57)</span> <span class="comment-user userinfo">keithonearth</span>
</div>
</div>
<span id="64572"></span>
<div id="comment-64572" class="comment">
<div id="post-64572-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Using a walking pole say 1.2 metres measure poles shadow length then measure buildings shadow should give a very accurate estimation. If you have measured your pace length you can pace it out.</p>
</div>
<div id="comment-64572-info" class="comment-info">
<span class="comment-age">(07 Jul '18, 15:23)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="64573"></span>
<div id="comment-64573" class="comment">
<div id="post-64573-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Building shadows on Bing can be used to estimate heights if an object of know height is in the same image.</p>
</div>
<div id="comment-64573-info" class="comment-info">
<span class="comment-age">(07 Jul '18, 15:26)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="64575"></span>
<div id="comment-64575" class="comment">
<div id="post-64575-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This app as an angle read out that can be used with trigonmetry to get heights <a href="https://play.google.com/store/apps/details?id=com.digital_and_dreams.android.android_army_knife&amp;hl=en_GB">https://play.google.com/store/apps/details?id=com.digital_and_dreams.android.android_army_knife&amp;hl=en_GB</a></p>
</div>
<div id="comment-64575-info" class="comment-info">
<span class="comment-age">(07 Jul '18, 15:39)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
</div>
<div id="comment-tools-64564" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64564-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="64569"></span>

<div id="answer-container-64569" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64569-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64569-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-64569-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi Keithonearth, why don’t you use the oldest method of measuring an object ? The pencil ? Look at the building alongside the pencil, mark the height and turn the pencil 90 degrees to the surface and mark the distance of the height and walk along it or measure it as well. The other method is a technical one, use a distance measurementtool with the option to calculate the height of an object using the method SomeoneElse mentioned (much cheaper). If so, choose an infra red one a simple one wont work that well during daylight or in the sun.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Jul '18, 09:30</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-64569" class="comments-container">
<span id="64574"></span>
<div id="comment-64574" class="comment">
<div id="post-64574-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I estimated a tree height by measuring a nearby wall on a survey (level with third shirt button, for example). On bing the shadows of both can then be measured to calculate the tree height after seeing how high the button is.</p>
</div>
<div id="comment-64574-info" class="comment-info">
<span class="comment-age">(07 Jul '18, 15:33)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="64577"></span>
<div id="comment-64577" class="comment">
<div id="post-64577-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi Andy, its the same method perfect &amp; simple, but consider to take a spring rule with you its even usable as a large pencil.</p>
</div>
<div id="comment-64577-info" class="comment-info">
<span class="comment-age">(07 Jul '18, 22:23)</span> <span class="comment-user userinfo">Hendrikklaas</span>
</div>
</div>
<span id="64582"></span>
<div id="comment-64582" class="comment">
<div id="post-64582-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have used a 3 metre tape but a 50 metre tape for tree shadows could cause some suspicion. I usually carry a backpack with GPS, camera, water, food, more clothes so i carry too much stuff already. But i agree old surveying and estimation methods are useful.</p>
</div>
<div id="comment-64582-info" class="comment-info">
<span class="comment-age">(08 Jul '18, 08:06)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
</div>
<div id="comment-tools-64569" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64569-form-container" class="comment-form-container">
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


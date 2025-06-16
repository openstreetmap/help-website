+++
type = "question"
title = "Best desktop machine configuration for JOSM"
description = '''Not being sure if this question belongs in here, but anyway. I am a quite long time user of JOSM, and for the last two years, all of the common desktop machines I&#x27;ve used all are able to offer a somewhat decent level of performance running JOSM. By &quot;decent&quot; I mean, scrolling/zooming is not too laggy...'''
date = "2016-01-04T15:09:00Z"
lastmod = "2021-03-12T06:55:00Z"
weight = 47368
keywords = [ "josm", "desktop", "cpu", "performance" ]
aliases = [ "/questions/47368" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Best desktop machine configuration for JOSM](/questions/47368/best-desktop-machine-configuration-for-josm)

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
<span id="post-47368-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47368-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-47368-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Not being sure if this question belongs in here, but anyway. I am a quite long time user of JOSM, and for the last two years, all of the common desktop machines I've used all are able to offer a somewhat decent level of performance running JOSM.</p>
<p>By "decent" I mean, scrolling/zooming is not too laggy, search operations are quick, high command (via mouse and keyboard) responsiveness, validation is quick, able to work with a few hundred GPX files open at the same time, etc.</p>
<p>However, I just acquired a new 4k display, and now JOSM's performance is abysmal. That is expected, since the previous display setup was just a pair of common HD (1080) ones. Another machine I've used for some time had a 2k display, and it ran JOSM just OK (but not anything near "greatly").</p>
<p>My question is about what should be my next upgrade (or upgrades). Should I invest in a high end video card? (current is an very ancient AMD) Higher end CPU? (current one is i7-3770) More memory? (currently with 32GB, but nowhere near full use running JOSM) Anything else?</p>
<p>Rephrasing it, what would be a good desktop configuration for running JOSM @4k resolutions?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-desktop" rel="tag" title="see questions tagged &#39;desktop&#39;">desktop</span> <span class="post-tag tag-link-cpu" rel="tag" title="see questions tagged &#39;cpu&#39;">cpu</span> <span class="post-tag tag-link-performance" rel="tag" title="see questions tagged &#39;performance&#39;">performance</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Jan '16, 15:09</strong></p>
<img src="https://secure.gravatar.com/avatar/94b019f273c04cd88bc1c8dd0a8f2161?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MCPicoli&#39;s gravatar image" />
<p><span>MCPicoli</span><br />
<span class="score" title="2172 reputation points"><span>2.2k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MCPicoli has 10 accepted answers">24%</span></p>
</div>
</div>
<div id="comments-container-47368" class="comments-container">
<span id="47372"></span>
<div id="comment-47372" class="comment">
<div id="post-47372-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Remember that to make use of more of your system's memory you need to start JOSM with a <a href="https://josm.openstreetmap.de/wiki/Help/CommandLineOptions">-Xmx...m argument</a>. Experiment with a heavy session to see how high a setting is worthwile for you.</p>
</div>
<div id="comment-47372-info" class="comment-info">
<span class="comment-age">(04 Jan '16, 22:09)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
<span id="47373"></span>
<div id="comment-47373" class="comment">
<div id="post-47373-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/867/vincent-de-phily"></a><a href="https://help.openstreetmap.org/users/867/vincent-de-phily">@Vincent de Phily</a>: Indeed - took me a while to understand why it's only using a little bit of memory. Assigning more of the available RAM helps a lot.</p>
</div>
<div id="comment-47373-info" class="comment-info">
<span class="comment-age">(05 Jan '16, 06:30)</span> <span class="comment-user userinfo">Piskvor</span>
</div>
</div>
<span id="47376"></span>
<div id="comment-47376" class="comment">
<div id="post-47376-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Increasing memory (tried giving JOSM 2GB using the 32-bit JVM and up to 20GB using the 64-bit JVM with "-d64" just in case) caused little perceivable improvement.</p>
</div>
<div id="comment-47376-info" class="comment-info">
<span class="comment-age">(05 Jan '16, 11:36)</span> <span class="comment-user userinfo">MCPicoli</span>
</div>
</div>
<span id="79219"></span>
<div id="comment-79219" class="comment">
<div id="post-79219-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Did you find anything that helped (or was holding you back)? I'm considering a new machine and 4k monitor and wondering how important the graphics card is.</p>
</div>
<div id="comment-79219-info" class="comment-info">
<span class="comment-age">(11 Mar '21, 18:58)</span> <span class="comment-user userinfo">TrekClimbing</span>
</div>
</div>
</div>
<div id="comment-tools-47368" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47368-form-container" class="comment-form-container">
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

<span id="47385"></span>

<div id="answer-container-47385" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47385-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47385-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-47385-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>look at CPU usage graphs (separated by core, although for me JOSM is nicely multithreading), if a single cpu core is clearly over 75% (assuming some kind of averaging), then it may be slowing down the whole. You need to search for the weakest link in your config. It may be your CPU, your buses, you memory speed, your graphics card, your graphics drivers/system, or even another OS ... Likely it is not your storage - but again: look at its usage when JOSM is slow. And in any case: having a SSD is a really paying-off thing for program starts.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Jan '16, 22:47</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-47385" class="comments-container">
&#10;</div>
<div id="comment-tools-47385" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47385-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="79225"></span>

<div id="answer-container-79225" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-79225-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79225-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-79225-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It would be a annoying to set the screen to a lower resolution for JOSM but if it works it might be less annoying than slow updates. My WIN10 view.</p>
<p><img src="/upfiles/right_click_on_background.JPG" alt="alt text" /></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Mar '21, 23:32</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</img>
</div>
</div>
<div id="comments-container-79225" class="comments-container">
<span id="79226"></span>
<div id="comment-79226" class="comment">
<div id="post-79226-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I agree that's a workaround if you can't fix the hardware, but it would be a shame to buy a 4k monitor and then not be able to use it well for osm editing.</p>
</div>
<div id="comment-79226-info" class="comment-info">
<span class="comment-age">(11 Mar '21, 23:42)</span> <span class="comment-user userinfo">TrekClimbing</span>
</div>
</div>
<span id="79228"></span>
<div id="comment-79228" class="comment">
<div id="post-79228-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Agreed, I wonder what JOSMs true maximum resolution is, 1K stretched to 4K may look nicer but is it of use? or have i got this wrong?</p>
</div>
<div id="comment-79228-info" class="comment-info">
<span class="comment-age">(12 Mar '21, 06:55)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
</div>
<div id="comment-tools-79225" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79225-form-container" class="comment-form-container">
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


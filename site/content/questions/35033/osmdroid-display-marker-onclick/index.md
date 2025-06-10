+++
type = "question"
title = "OSMDroid Display marker onClick"
description = '''Hi , I am working on a project to implement maps in android. I have used OSMDroid and successfully displayed it. I want to add markers on my map so I can form a path. Now I can add markers if I enter the GPS coordinates manually. But I want to add the markers automatically if i click on the map.  Is...'''
date = "2014-07-21T07:12:00Z"
lastmod = "2015-04-09T12:43:00Z"
weight = 35033
keywords = [ "marker", "development", "osmdroid", "click" ]
aliases = [ "/questions/35033" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [OSMDroid Display marker onClick](/questions/35033/osmdroid-display-marker-onclick)

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
<span id="post-35033-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35033-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-35033-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi ,</p>
<p>I am working on a project to implement maps in android. I have used OSMDroid and successfully displayed it.</p>
<p>I want to add markers on my map so I can form a path. Now I can add markers if I enter the GPS coordinates manually. But I want to add the markers automatically if i click on the map.</p>
<p>Is there any way to get this data? Please help.</p>
<p>PS : This is an offline map. I checked by giving GPS coordinates and having data off, the marker was added. So , I know that it can be done but I dont know how.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-marker" rel="tag" title="see questions tagged &#39;marker&#39;">marker</span> <span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-osmdroid" rel="tag" title="see questions tagged &#39;osmdroid&#39;">osmdroid</span> <span class="post-tag tag-link-click" rel="tag" title="see questions tagged &#39;click&#39;">click</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Jul '14, 07:12</strong></p>
<img src="https://secure.gravatar.com/avatar/6f442e9fe69b991ea9dd987947a492bc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="anshumank&#39;s gravatar image" />
<p><span>anshumank</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="anshumank has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Apr '15, 12:44</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-35033" class="comments-container">
&#10;</div>
<div id="comment-tools-35033" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35033-form-container" class="comment-form-container">
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

<span id="42229"></span>

<div id="answer-container-42229" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-42229-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42229-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-42229-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Have a look at MapEventsReceiver from the <a href="https://github.com/MKergall/osmbonuspack/blob/master/OSMBonusPack/src/org/osmdroid/bonuspack/overlays/MapEventsReceiver.java">osmbonuspack</a> and this <a href="https://groups.google.com/forum/#!topic/osmdroid/qf0XvmAPgYQ">groups</a> thread.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Apr '15, 10:37</strong></p>
<img src="https://secure.gravatar.com/avatar/942cb7c3dfb906396eed454ad4e0fa3a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bmla&#39;s gravatar image" />
<p><span>bmla</span><br />
<span class="score" title="16 reputation points">16</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bmla has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Apr '15, 12:44</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-42229" class="comments-container">
<span id="42235"></span>
<div id="comment-42235" class="comment">
<div id="post-42235-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>yes, "single tap" and "long press" sounds like what the question is, in my opinion. I have replaced your URL with the new one (according to the project's home page) since google code will vanish next year.</p>
</div>
<div id="comment-42235-info" class="comment-info">
<span class="comment-age">(09 Apr '15, 12:43)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-42229" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42229-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="35037"></span>

<div id="answer-container-35037" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-35037-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35037-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-35037-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Osmdroid is some software that happens to use OSM data, rather than "part of OSM". There's a <a href="https://groups.google.com/forum/#!forum/osmdroid">Google Group</a> for it; people there will be more familiar with it than here.</p>
<p>However, it sounds like you're just asking "<a href="http://stackoverflow.com/questions/1513485/how-do-i-get-the-current-gps-location-programmatically-in-android">how do I get the current location on Android</a>"? That stackoverflow questions links to examples and covers the issues, including whether you want to use Google Play Services or not.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Jul '14, 09:35</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Jul '14, 09:37</strong> </span></p>
</div>
</div>
<div id="comments-container-35037" class="comments-container">
<span id="42234"></span>
<div id="comment-42234" class="comment">
<div id="post-42234-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>"I want to add the markers automatically if i click on the map" does <em>not</em> sound like getting the current (gps) location is the question (I have removed the "gps" tag therefore). "GPS coordinates" should likely just mean "coordinates".</p>
</div>
<div id="comment-42234-info" class="comment-info">
<span class="comment-age">(09 Apr '15, 12:37)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-35037" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35037-form-container" class="comment-form-container">
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


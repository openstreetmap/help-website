+++
type = "question"
title = "Can I Customize A Map with Auto-Routable Tracks?"
description = '''I have the need to access many private roads that I have tracked. I&#x27;m wondering if there is a way for me to make these auto routable with OSM on my GPS.'''
date = "2014-05-30T17:24:00Z"
lastmod = "2014-06-04T21:38:00Z"
weight = 33563
keywords = [ "garmin", "customization" ]
aliases = [ "/questions/33563" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Can I Customize A Map with Auto-Routable Tracks?](/questions/33563/can-i-customize-a-map-with-auto-routable-tracks)

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
<span id="post-33563-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33563-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-33563-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have the need to access many private roads that I have tracked. I'm wondering if there is a way for me to make these auto routable with OSM on my GPS.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-garmin" rel="tag" title="see questions tagged &#39;garmin&#39;">garmin</span> <span class="post-tag tag-link-customization" rel="tag" title="see questions tagged &#39;customization&#39;">customization</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 May '14, 17:24</strong></p>
<img src="https://secure.gravatar.com/avatar/3756fe154d7e36e3028f3f6d1239bcd6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SlimJim44&#39;s gravatar image" />
<p><span>SlimJim44</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SlimJim44 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Jun '14, 21:46</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-33563" class="comments-container">
&#10;</div>
<div id="comment-tools-33563" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33563-form-container" class="comment-form-container">
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

<span id="33565"></span>

<div id="answer-container-33565" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-33565-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33565-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-33565-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes, but it's probably going to involve you doing something with the data before you feed it into your GPS. How you do this will depend on what sort of GPS it is that you're using.</p>
<p>If it's a Garmin GPS, then you may be able to use <a href="https://wiki.openstreetmap.org/wiki/Mkgmap">mkgmap</a> and edit the style files that it uses to achieve your desired result (a <a href="https://www.google.co.uk/search?hl=en-GB&amp;source=hp&amp;q=mkgmap+route+private&amp;btnG=Google+Search&amp;gbv=1">quick web search</a> provides several suggestions). Even if you can't do exactly what you want using mkgmap you do have the option to write something that modifies the data (perhaps to remove e.g. "access=private" from the data) before feeding it to mkgmap - but that involves you writing some code, of course.</p>
<p>It's worth noting that the web links above are mostly about trying to <em>avoid</em> routing on private tracks rather than to allow it, so it might help if you could provide an example of a track that your GPS doesn't route down because it's private (and also say what sort of GPS you're using, of course).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 May '14, 18:02</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-33565" class="comments-container">
<span id="33686"></span>
<div id="comment-33686" class="comment">
<div id="post-33686-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have a Garmin Montana 600. I'm generally using minimally used farm roads, so they aren't recognized as roads at all. I have City Navigator (CN) and the birds eye ariel imaging currently installed. CN has no problems sending me down private roads behind locked gates, my issue is that I'm needing to use dirt paths basically. With CN, if my waypoint is not located near a recognized road, it routes me to the closest recognized road and then sends me directly to the waypoint (through fields, rivers, etc). Typically the entrance to the dirt path is not the nearest point on a recognized road.</p>
</div>
<div id="comment-33686-info" class="comment-info">
<span class="comment-age">(04 Jun '14, 20:50)</span> <span class="comment-user userinfo">SlimJim44</span>
</div>
</div>
<span id="33691"></span>
<div id="comment-33691" class="comment">
<div id="post-33691-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>City Navigator's a Garmin product and unrelated to OSM data; I guess what you're asking is whether you could use OSM data to route to places that CN won't recognise a route to by using OSM data. The answer's yes, but will probably need a bit of experimentation on your part.</p>
</div>
<div id="comment-33691-info" class="comment-info">
<span class="comment-age">(04 Jun '14, 21:38)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-33565" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33565-form-container" class="comment-form-container">
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


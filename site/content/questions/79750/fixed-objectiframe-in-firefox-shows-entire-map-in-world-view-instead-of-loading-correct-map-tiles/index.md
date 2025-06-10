+++
type = "question"
title = "[fixed] object/iframe in firefox shows entire map in world view instead of loading correct map tiles"
description = '''Hi! On a website I built, I&#x27;m running into a weird issue using several iframes from OSM. I only see the world view, not the actual coordinates. It works in Chrome. And it used to work on Firefoy. It happens in Firefox, 78.9.0 esr on Debian, but also confirmed on Windows. Using the following code:  o...'''
date = "2021-04-19T20:45:00Z"
lastmod = "2021-04-20T11:44:00Z"
weight = 79750
keywords = [ "firefox", "worldview" ]
aliases = [ "/questions/79750" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [\[fixed\] object/iframe in firefox shows entire map in world view instead of loading correct map tiles](/questions/79750/fixed-objectiframe-in-firefox-shows-entire-map-in-world-view-instead-of-loading-correct-map-tiles)

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
<span id="post-79750-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79750-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-79750-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi!</p>
<p>On a website I built, I'm running into a weird issue using several iframes from OSM. I only see the world view, not the actual coordinates. It works in Chrome. And it used to work on Firefoy. It happens in Firefox, 78.9.0 esr on Debian, but also confirmed on Windows.</p>
<p>Using the following code:</p>
<pre><code> object loading=&quot;lazy&quot; width=&quot;450&quot; height=&quot;250&quot; frameborder=&quot;0&quot; scrolling=&quot;no&quot; marginheight=&quot;0&quot; marginwidth=&quot;0&quot; data=&quot;https://www.openstreetmap.org/export/embed.html?bbox=9.50119972229004,51.325060678316106,9.513173103332521,51.32918373770352&amp;amp;layer=mapnik&amp;amp;marker=51.327118902266484,9.50718641281128&quot;&gt;&lt;/object&gt;</code></pre>
<p>or the following code:</p>
<pre><code>iframe loading=&quot;lazy&quot; width=&quot;450&quot; height=&quot;250&quot; frameborder=&quot;0&quot; scrolling=&quot;no&quot; marginheight=&quot;0&quot; marginwidth=&quot;0&quot; src=&quot;https://www.openstreetmap.org/export/embed.html?bbox=9.50119972229004,51.325060678316106,9.513173103332521,51.32918373770352&amp;amp;layer=mapnik&amp;amp;marker=51.327118902266484,9.50718641281128&quot;&gt;&lt;/iframe&gt;</code></pre>
<p>(Note that I removed the first "&lt;" from the code above only because the code editor here didn't like it. It's not a typo that I have in my code.)</p>
<p>It actually happens to all the maps that I included in the page, regardless if I show them on the actual web server or if I run the website locally and regardless of the inclusion method.</p>
<p>Now, what's even weirder, extremely weird, is that when I throttle the speed using Firefox' developer tab to something smaller or equal to "regular 3G", the correct map tiles get loaded and shown.</p>
<p>But, on my mobile phone I also use Firefox, and there I have the same issue, I see only the world view, not the correct map tiles. Regardless if I use my home WiFi or a 3G connection.</p>
<p>I saw that the tiles get loaded from fastly CDN, and I wonder if that might have something to do with my issue. Maybe.. Firefox has a weird DNS cache and caches my request in a strange way?</p>
<p>In the past I saw this behavior:</p>
<ul>
<li>on Chrome/Chromium using iframe instead of object</li>
<li>on Chromium/FF making mistakes in the coordinates</li>
</ul>
<p>But in this case, it seems like it works on Chromium, and there is no mistake in the coordinates. This happens to all the maps I included on the page, 7 small maps.</p>
<p><strong>UPDATE</strong> see my last answer for analysis of the issue and workaround. The issue is not with OSM, but it seems to be a FF bug.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-firefox" rel="tag" title="see questions tagged &#39;firefox&#39;">firefox</span> <span class="post-tag tag-link-worldview" rel="tag" title="see questions tagged &#39;worldview&#39;">worldview</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Apr '21, 20:45</strong></p>
<img src="https://secure.gravatar.com/avatar/8c43417385b2b0325c06f0f70b6868b9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ulrikeu&#39;s gravatar image" />
<p><span>ulrikeu</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ulrikeu has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Apr '21, 11:56</strong> </span></p>
</div>
</div>
<div id="comments-container-79750" class="comments-container">
<span id="79761"></span>
<div id="comment-79761" class="comment">
<div id="post-79761-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ok, I'm investigating this a bit further. My maps are hidden in the DOM by default. When I copy the same code to another file then it seems to work just fine. So I'm currently suspecting something related to the hidden item.</p>
</div>
<div id="comment-79761-info" class="comment-info">
<span class="comment-age">(20 Apr '21, 11:13)</span> <span class="comment-user userinfo">ulrikeu</span>
</div>
</div>
</div>
<div id="comment-tools-79750" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79750-form-container" class="comment-form-container">
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

<span id="79765"></span>

<div id="answer-container-79765" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-79765-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79765-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-79765-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In the setup I have, people click on some link and then they see a detailed map, which is by default set to "display:none" via CSS. Because of this, Firefox can apparently not correctly load the tiles. This is some sort of bug that I have no power to investigate better. But I found a workaround for my issue. Instead of using "display:none" in CSS or "hide()" with jQuery, I now use two classes which "transform:translateX(some-value-outside-viewport)" the map detail, so that it's not visible on the screen. And now the maps get loaded correctly, either using "object" or "iframe". I use "object", because otherwise we run into exactly the same bug on Chrome.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Apr '21, 11:44</strong></p>
<img src="https://secure.gravatar.com/avatar/8c43417385b2b0325c06f0f70b6868b9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ulrikeu&#39;s gravatar image" />
<p><span>ulrikeu</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ulrikeu has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Apr '21, 11:56</strong> </span></p>
</div>
</div>
<div id="comments-container-79765" class="comments-container">
&#10;</div>
<div id="comment-tools-79765" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79765-form-container" class="comment-form-container">
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


+++
type = "question"
title = "javascript bookmarklet fails to load Mapillary website"
description = '''Hi This is only semi related to OSM, but I&#x27;m hoping someone here with expert knowledge can help me. I&#x27;m using this bookmarklet to scrape the co-ordinates from OSM&#x27;s URL &amp;amp; transferring them to a URL to loaded the equivalent location in Mapillary. javascript:(function(){var%20a=/map=(&#92;d+)&#92;/(-?&#92;d+(...'''
date = "2018-07-10T13:09:00Z"
lastmod = "2018-07-13T22:10:00Z"
weight = 64643
keywords = [ "javascript", "bookmarklet" ]
aliases = [ "/questions/64643" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [javascript bookmarklet fails to load Mapillary website](/questions/64643/javascript-bookmarklet-fails-to-load-mapillary-website)

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
<span id="post-64643-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64643-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-64643-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi This is only semi related to OSM, but I'm hoping someone here with expert knowledge can help me.</p>
<p>I'm using this bookmarklet to scrape the co-ordinates from OSM's URL &amp; transferring them to a URL to loaded the equivalent location in Mapillary.</p>
<pre><code>javascript:(function(){var%20a=/map=(\d+)\/(-?\d+(.\d*)?)\/(-?\d+(.\d*)?)/.exec(window.location.hash);window.open(&quot;https://www.mapillary.com/app/?lat=&quot;+a[2]+&quot;&amp;lng=&quot;+a[4]+&quot;&amp;z=&quot;+a[1])}())</code></pre>
<p>For some reason it stopped working on the main OSM page. I'm using Firefox &amp; sure there wasn't an update when the failure occurred. I've also failed on a old version of Firefox (43) but works in an old copy of IE.</p>
<p>It still works in the edit screen of Potlatch, but not iD.</p>
<p>I check site permissions but P2 &amp; iD use the same <a href="https://www.openstreetmap.org"><code>https://www.openstreetmap.org</code></a></p>
<p>What has changed?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-javascript" rel="tag" title="see questions tagged &#39;javascript&#39;">javascript</span> <span class="post-tag tag-link-bookmarklet" rel="tag" title="see questions tagged &#39;bookmarklet&#39;">bookmarklet</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Jul '18, 13:09</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-64643" class="comments-container">
&#10;</div>
<div id="comment-tools-64643" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64643-form-container" class="comment-form-container">
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

<span id="64715"></span>

<div id="answer-container-64715" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64715-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64715-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-64715-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>What has changed? openstreetmap.org has a strict CSP since a day in May 2018.</p>
<p>See <a href="https://wiki.openstreetmap.org/wiki/Bookmarklet">https://wiki.openstreetmap.org/wiki/Bookmarklet</a> : "use a browser which supports bookmarklets on pages with a strict CSP (openstreetmap.org has one since May 2018). Firefox does not work; Chromium works."</p>
<p>I do not understand why it works on a P2 edit page.</p>
<p>Workaround (for many cases but not for your case): For osm object IDs I use Firefox' special bookmark placeholder %s in my bookmarks - see <a href="https://forum.openstreetmap.org/viewtopic.php?pid=675076#p675076">https://forum.openstreetmap.org/viewtopic.php?pid=675076#p675076</a> . In your case I see no simple workaround. Try to use Chromium/Chrome instead of Firefox of you want to avoid IE.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Jul '18, 22:10</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Jul '18, 22:12</strong> </span></p>
</div>
</div>
<div id="comments-container-64715" class="comments-container">
&#10;</div>
<div id="comment-tools-64715" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64715-form-container" class="comment-form-container">
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


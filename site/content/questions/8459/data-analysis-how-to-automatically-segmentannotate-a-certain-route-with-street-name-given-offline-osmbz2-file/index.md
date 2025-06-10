+++
type = "question"
title = "[Data Analysis] How to automatically segment/annotate a certain route with street name given offline .osm.bz2 file"
description = '''Hi: I want to write a script to automatically segment/annotate of a route (.gpx file) with street names given the .osm.bz2 offline.  Just wondering if similar work has been done. I&#x27;m planning to build a quadtree Data Structure of the &quot;ways&quot; to facilitate the search: instead of keeping all the nodes,...'''
date = "2011-10-14T21:15:00Z"
lastmod = "2011-10-20T14:28:00Z"
weight = 8459
keywords = [ "development", "annotate", "gpx", "streetnames", "script" ]
aliases = [ "/questions/8459" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [\[Data Analysis\] How to automatically segment/annotate a certain route with street name given offline .osm.bz2 file](/questions/8459/data-analysis-how-to-automatically-segmentannotate-a-certain-route-with-street-name-given-offline-osmbz2-file)

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
<span id="post-8459-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8459-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-8459-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi:</p>
<p>I want to write a script to automatically segment/annotate of a route (.gpx file) with street names given the .osm.bz2 offline.</p>
<ol>
<li>Just wondering if similar work has been done.</li>
<li>I'm planning to build a quadtree Data Structure of the "ways" to facilitate the search:</li>
<li>instead of keeping all the nodes, I'll just have a coarse AABB bounding box for each way</li>
<li>In the beginning, we find the "way" of the first gps pt belonged to in the quadtree.</li>
<li>Then for the next gps pt, locally search over the "way"s connected to the "way" that the previous pt is in.</li>
</ol>
<p>Thanks for your advice</p>
<p>E.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-annotate" rel="tag" title="see questions tagged &#39;annotate&#39;">annotate</span> <span class="post-tag tag-link-gpx" rel="tag" title="see questions tagged &#39;gpx&#39;">gpx</span> <span class="post-tag tag-link-streetnames" rel="tag" title="see questions tagged &#39;streetnames&#39;">streetnames</span> <span class="post-tag tag-link-script" rel="tag" title="see questions tagged &#39;script&#39;">script</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Oct '11, 21:15</strong></p>
<img src="https://secure.gravatar.com/avatar/a24fb83b1a0f9b1915be072d2c42762d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="eminemya&#39;s gravatar image" />
<p><span>eminemya</span><br />
<span class="score" title="1 reputation points">1</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="eminemya has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Jan '15, 19:25</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-8459" class="comments-container">
&#10;</div>
<div id="comment-tools-8459" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8459-form-container" class="comment-form-container">
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

<span id="8523"></span>

<div id="answer-container-8523" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8523-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8523-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-8523-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you won't get any useful hints at this FAQ site you can try to ask again at one of the appropriate OSM mailing lists ... there is a least one about developers and one about routing.</p>
<p>To access these mailing lists, go to <a href="http://wiki.osm.org">wiki.osm.org</a> and serach for "mailing lists".</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Oct '11, 09:28</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-8523" class="comments-container">
<span id="8532"></span>
<div id="comment-8532" class="comment">
<div id="post-8532-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>thanks for the suggestion:)</p>
</div>
<div id="comment-8532-info" class="comment-info">
<span class="comment-age">(20 Oct '11, 14:28)</span> <span class="comment-user userinfo">eminemya</span>
</div>
</div>
</div>
<div id="comment-tools-8523" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8523-form-container" class="comment-form-container">
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


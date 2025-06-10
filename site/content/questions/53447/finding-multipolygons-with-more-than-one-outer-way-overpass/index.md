+++
type = "question"
title = "Finding multipolygons with more than one &#x27;outer&#x27; way. Overpass?"
description = '''I&#x27;d like to find multipolygons that have more than one member with the role &#x27;outer&#x27;. Is there a way to do that with the Overpass API, or would I have to wait for https://github.com/drolbr/Overpass-API/issues/197 to get written? Would there be any other way to do this?'''
date = "2016-12-10T01:16:00Z"
lastmod = "2021-05-09T21:44:00Z"
weight = 53447
keywords = [ "overpass", "relations", "multipolygon" ]
aliases = [ "/questions/53447" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Finding multipolygons with more than one 'outer' way. Overpass?](/questions/53447/finding-multipolygons-with-more-than-one-outer-way-overpass)

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
<span id="post-53447-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53447-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-53447-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'd like to find multipolygons that have more than one member with the role 'outer'.</p>
<p>Is there a way to do that with the Overpass API, or would I have to wait for <a href="https://github.com/drolbr/Overpass-API/issues/197">https://github.com/drolbr/Overpass-API/issues/197</a> to get written?</p>
<p>Would there be any other way to do this?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span> <span class="post-tag tag-link-multipolygon" rel="tag" title="see questions tagged &#39;multipolygon&#39;">multipolygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Dec '16, 01:16</strong></p>
<img src="https://secure.gravatar.com/avatar/aace33beb0d1a608b0763ac8a2404049?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Stereo&#39;s gravatar image" />
<p><span>Stereo</span><br />
<span class="score" title="356 reputation points">356</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Stereo has one accepted answer">11%</span></p>
</div>
</div>
<div id="comments-container-53447" class="comments-container">
&#10;</div>
<div id="comment-tools-53447" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53447-form-container" class="comment-form-container">
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

<span id="53453"></span>

<div id="answer-container-53453" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53453-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53453-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-53453-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Stereo has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you are willing to put up with a beta quality program I am working on, you can use <a href="https://github.com/osmcode/osmium-filter">osmium-filter</a>. It can do a query like that: osmium-filter-simple <code>INPUTFILE -e '@relation and (@members[@role=="outer"] &gt; 1)' -o OUTPUTFILE</code>. It doesn't support giving you all the ways and nodes needed for these relations yet, if you need that, you can use the <a href="http://osmcode.org/osmium-tool/">Osmium tool</a> (to be more exact, <a href="http://docs.osmcode.org/osmium/latest/osmium-getid.html"><code>osmium getid</code></a>). Other options include writing your own program using libosmium, PyOsmium, or node-osmium (see <a href="http://osmcode.org/).">http://osmcode.org/).</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Dec '16, 09:30</strong></p>
<img src="https://secure.gravatar.com/avatar/2d4dfcdcde73aa5e2ffa4a9b3a7cb51d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jochen%20Topf&#39;s gravatar image" />
<p><span>Jochen Topf</span><br />
<span class="score" title="5244 reputation points"><span>5.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jochen Topf has 32 accepted answers">31%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Dec '16, 09:34</strong> </span></p>
</div>
</div>
<div id="comments-container-53453" class="comments-container">
<span id="53456"></span>
<div id="comment-53456" class="comment">
<div id="post-53456-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you Jochen, I'll give that a go!</p>
<p>Would you also happen to have a way of <a href="https://www.openstreetmap.org/user/Stereo/diary/40037">finding old-style multipolygons</a> with it?</p>
</div>
<div id="comment-53456-info" class="comment-info">
<span class="comment-age">(10 Dec '16, 12:56)</span> <span class="comment-user userinfo">Stereo</span>
</div>
</div>
<span id="53462"></span>
<div id="comment-53462" class="comment">
<div id="post-53462-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Have a look at <a href="https://github.com/osmcode/osm-area-tools">https://github.com/osmcode/osm-area-tools</a> . There are tools that can find old-style multipolygons. I use that to create the overlay on <a href="http://area.jochentopf.com/map/index.html">http://area.jochentopf.com/map/index.html</a> for instance. But you can also just download the old-style mps from <a href="http://area.jochentopf.com/">http://area.jochentopf.com/</a> updated daily.</p>
</div>
<div id="comment-53462-info" class="comment-info">
<span class="comment-age">(10 Dec '16, 14:36)</span> <span class="comment-user userinfo">Jochen Topf</span>
</div>
</div>
<span id="53463"></span>
<div id="comment-53463" class="comment">
<div id="post-53463-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Wow, osmium-filter is impressively fast! It's an exciting tool, and I hope that you'll find time to document it :).</p>
<p>'@relation and "type"="multipolygon" and (@members[@role=="outer"] &gt; 1)' did the trick.</p>
</div>
<div id="comment-53463-info" class="comment-info">
<span class="comment-age">(10 Dec '16, 14:38)</span> <span class="comment-user userinfo">Stereo</span>
</div>
</div>
</div>
<div id="comment-tools-53453" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53453-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="80090"></span>

<div id="answer-container-80090" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80090-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80090-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-80090-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I ended up doing it in overpass:</p>
<pre><code>[out:xml][timeout:25];
{{geocodeArea:Luxembourg}}-&gt;.searchArea;
// gather results
(
  relation[&quot;type&quot;=&quot;multipolygon&quot;](if: count_by_role(&quot;outer&quot;) &gt; 1 )(area.searchArea);
  relation[&quot;type&quot;=&quot;multipolygon&quot;](if: count_members() == 1 )(area.searchArea);
&#10;);
// print results
out meta;
&gt;;
out meta qt;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 May '21, 21:44</strong></p>
<img src="https://secure.gravatar.com/avatar/aace33beb0d1a608b0763ac8a2404049?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Stereo&#39;s gravatar image" />
<p><span>Stereo</span><br />
<span class="score" title="356 reputation points">356</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Stereo has one accepted answer">11%</span></p>
</div>
</div>
<div id="comments-container-80090" class="comments-container">
&#10;</div>
<div id="comment-tools-80090" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80090-form-container" class="comment-form-container">
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


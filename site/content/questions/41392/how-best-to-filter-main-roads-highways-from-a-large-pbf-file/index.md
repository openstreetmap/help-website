+++
type = "question"
title = "How best to filter &#x27;main&#x27; roads (highways) from a large PBF file"
description = '''I&#x27;m looking for some guidance on the best way to filter the Europe-latest.osm.pbf file which I&#x27;ve downloaded from Geofabrik. I want to reduce the file to keep all of the &#x27;main&#x27; roads; i.e. keeping those tagged: highway=motorway highway=motorway link  highway=trunk highway=trunk_link highway=primary ...'''
date = "2015-02-26T16:31:00Z"
lastmod = "2015-02-27T11:42:00Z"
weight = 41392
keywords = [ "filter", "pbf", "osmfilter", "highway", "osmosis" ]
aliases = [ "/questions/41392" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How best to filter 'main' roads (highways) from a large PBF file](/questions/41392/how-best-to-filter-main-roads-highways-from-a-large-pbf-file)

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
<span id="post-41392-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41392-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-41392-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm looking for some guidance on the best way to filter the Europe-latest.osm.pbf file which I've downloaded from Geofabrik. I want to reduce the file to keep all of the 'main' roads; i.e. keeping those tagged:</p>
<pre><code>highway=motorway
highway=motorway link 
highway=trunk
highway=trunk_link
highway=primary
highway=primary_link</code></pre>
<p>I want to keep the related data; so keep all nodes and ways for these roads. I'm looking at osmosis and osmfilter and can run some tests, but I thought it worth asking for some guidance here to help focus my efforts. What is the best approach to filtering such a large set of data? I wonder if I need to concern myself with the machine's available memory? (I'm assuming so) How much might I need and how long might it take?</p>
<p>Thanks for any guidance.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-pbf" rel="tag" title="see questions tagged &#39;pbf&#39;">pbf</span> <span class="post-tag tag-link-osmfilter" rel="tag" title="see questions tagged &#39;osmfilter&#39;">osmfilter</span> <span class="post-tag tag-link-highway" rel="tag" title="see questions tagged &#39;highway&#39;">highway</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Feb '15, 16:31</strong></p>
<img src="https://secure.gravatar.com/avatar/ca7b309ba49a51403baaf2499f9fa431?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Barryn&#39;s gravatar image" />
<p><span>Barryn</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Barryn has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-41392" class="comments-container">
&#10;</div>
<div id="comment-tools-41392" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41392-form-container" class="comment-form-container">
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

<span id="41396"></span>

<div id="answer-container-41396" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-41396-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41396-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-41396-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I recommend <strong>osmfilter</strong> over osmosis for doing such a task.</p>
<p>Assuming that you have read documentation about osmfilter and osmconvert in the OSM wiki, I would start do test filtering strategies on a smaller country extract, like Luxembourg or similar.</p>
<p>When you are ok with the filtering parameters and the result file, just start that processing with europe-latest.pbf</p>
<p>Maybe it is godg to have the windows taskmanager or similar program in Linux in the background, to see whether your PC is still working. And check free HD space before.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Feb '15, 20:01</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-41396" class="comments-container">
<span id="41409"></span>
<div id="comment-41409" class="comment">
<div id="post-41409-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Agreed: osmfilter is well suited to this task and fast.</p>
</div>
<div id="comment-41409-info" class="comment-info">
<span class="comment-age">(27 Feb '15, 11:42)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
</div>
<div id="comment-tools-41396" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41396-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="41401"></span>

<div id="answer-container-41401" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-41401-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41401-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-41401-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Osmosis can do the job with the <a href="https://wiki.openstreetmap.org/wiki/Osmosis/Detailed_Usage#--tag-filter_.28--tf.29"><code>--tag-filter</code> option</a>. You may need a lot of memory to store all the nodes (since you'll have to use the <a href="https://wiki.openstreetmap.org/wiki/Osmosis/Detailed_Usage#--used-node_.28--un.29"><code>--used-node</code> option</a>). How much memory do you have? The amount of harddisk space you'll need will be less than the europe-latest.osm.pbf file, so as long as you have at least 15GB you should be fine. If I were you, I'd just run it, and if it runs out of memory, it runs out of memory. You'll know in a few hours.</p>
<p>If want to do this in a memory effecient manner, you'd have to write your own programme, e.g. using the <a href="http://osmcode.org/libosmium/">Osmium library</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Feb '15, 09:09</strong></p>
<img src="https://secure.gravatar.com/avatar/16e12e337f6edc3750681492656097ed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rorym&#39;s gravatar image" />
<p><span>rorym</span><br />
<span class="score" title="5358 reputation points"><span>5.4k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="49 badges"><span class="silver">●</span><span class="badgecount">49</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rorym has 18 accepted answers">11%</span></p>
</div>
</div>
<div id="comments-container-41401" class="comments-container">
&#10;</div>
<div id="comment-tools-41401" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41401-form-container" class="comment-form-container">
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


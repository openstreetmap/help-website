+++
type = "question"
title = "Maperitive - is it possible to reduce duplication of code in definitions?"
description = '''At this moment AND NOT @isOneOf(highway, trunk, trunk_link, primary, primary_link, secondary, tertiary, pedestrian, residential, living_street, unclassified)  is used three times in my feature definition code, and I really want to replace it by reusable definition/variable/function. Is it possible?'''
date = "2013-09-23T12:29:00Z"
lastmod = "2013-09-23T18:00:00Z"
weight = 26640
keywords = [ "maperitive" ]
aliases = [ "/questions/26640" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Maperitive - is it possible to reduce duplication of code in definitions?](/questions/26640/maperitive-is-it-possible-to-reduce-duplication-of-code-in-definitions)

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
<span id="post-26640-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26640-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-26640-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>At this moment</p>
<pre><code>AND NOT @isOneOf(highway, trunk, trunk_link, primary, primary_link, secondary, tertiary, pedestrian, residential, living_street, unclassified)</code></pre>
<p>is used three times in my feature definition code, and I really want to replace it by reusable definition/variable/function. Is it possible?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-maperitive" rel="tag" title="see questions tagged &#39;maperitive&#39;">maperitive</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Sep '13, 12:29</strong></p>
<img src="https://secure.gravatar.com/avatar/fd2f7303e92334ed1eef75268aed7611?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bulwersator&#39;s gravatar image" />
<p><span>Bulwersator</span><br />
<span class="score" title="468 reputation points">468</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bulwersator has one accepted answer">14%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Sep '13, 12:33</strong> </span></p>
</div>
</div>
<div id="comments-container-26640" class="comments-container">
&#10;</div>
<div id="comment-tools-26640" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26640-form-container" class="comment-form-container">
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

<span id="26649"></span>

<div id="answer-container-26649" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-26649-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26649-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-26649-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For now I use C preprocessor - I have a separate file called expand.c. I run <code>gcc -E expand.c &gt; test.txt</code>, add two tabs at start of every line and copy it to file with rules.</p>
<p>My expand.c file looks like this:</p>
<pre><code>/*
use
gcc -E expand.c &gt; test.txt
to expand macros. Run regexp &quot;^&quot; to add tabs, than replace part of Biking.mrules
this hack is hilarious ugly, but better than editing expanded form of this stuff
*/
&#10;#define __cycleable (highway=cycleway OR cycleway=lane OR bicycle = yes OR bicycle = designated OR cycleway=opposite_lane)
#define __typical_road @isOneOf(highway, trunk, trunk_link, primary, primary_link, secondary, tertiary, pedestrian, residential, living_street, unclassified)
#define __no_surface_for_lane ((cycleway=lane OR segregated = yes) AND NOT cycleway:right = surface* AND NOT cycleway:left = surface*)
#define __paved_surface_for_lane ((cycleway=lane OR segregated = yes) AND (cycleway:right = &quot;surface=paved&quot; OR cycleway:left = &quot;surface=paved&quot;))
#define __separate_cycleway (highway=cycleway AND NOT segregated = no AND NOT foot = yes AND NOT foot = designated)
#define __segregated_cycleway ((highway=cycleway AND segregated = yes) OR (bicycle=designated AND segregated = yes) OR (cycleway = lane))
#define __proper_surface (surface = asphalt OR smoothness = excellent OR cycleway:right = &quot;surface=asphalt&quot; OR cycleway:left = &quot;surface=asphalt&quot;)
#define __cycleway __separate_cycleway OR __segregated_cycleway
&#10;no_and_yes_bug : __cycleable AND bicycle=no
crossing_as_way_rather_than_node_bug : highway = crossing
no oneway for bicycle instead of opposite_lane : &quot;oneway:bicycle&quot; = &quot;no&quot; AND NOT cycleway=opposite_lane
no_surface_info : __cycleable AND (__no_surface_for_lane OR __paved_surface_for_lane OR (surface=paved OR (NOT (surface) AND NOT (tracktype)))) AND (NOT bicycle = yes OR NOT __typical_road)
&#10;proper cycleway : __cycleway AND __proper_surface
proper cycleway maybe with a bad surface : __cycleway
lame cycleway : ((bicycle=designated OR (highway=cycleway AND bicycle = yes)) AND NOT segregated = yes)
contraflow : cycleway=opposite_lane
bicycle allowed : (bicycle=yes) AND NOT __typical_road
dismount from bicycle : bicycle=dismount
unexpected cycling ban : bicycle=no //AND __typical_road</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Sep '13, 15:23</strong></p>
<img src="https://secure.gravatar.com/avatar/fd2f7303e92334ed1eef75268aed7611?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bulwersator&#39;s gravatar image" />
<p><span>Bulwersator</span><br />
<span class="score" title="468 reputation points">468</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bulwersator has one accepted answer">14%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Sep '13, 15:31</strong> </span></p>
</div>
</div>
<div id="comments-container-26649" class="comments-container">
<span id="26653"></span>
<div id="comment-26653" class="comment">
<div id="post-26653-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Alternatively you could use <code>filepp</code> which works as a pre-processor for regular text files.</p>
</div>
<div id="comment-26653-info" class="comment-info">
<span class="comment-age">(23 Sep '13, 18:00)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-26649" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26649-form-container" class="comment-form-container">
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


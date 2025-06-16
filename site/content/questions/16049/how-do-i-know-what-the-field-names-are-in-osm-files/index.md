+++
type = "question"
title = "How do I know what the field names are in .osm files."
description = '''I want to use osmconvert to convert an osm file to a csv file with just the street, city, state, latitude/longitude fields. But I don&#x27;t know what the actual field names are in the osm file. How do I open it to see or is there a list somewhere? The .osm file is rather large, so if there was a cmd lin...'''
date = "2012-09-13T22:08:00Z"
lastmod = "2012-09-15T14:35:00Z"
weight = 16049
keywords = [ "fields", "osmconvert", "csv" ]
aliases = [ "/questions/16049" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How do I know what the field names are in .osm files.](/questions/16049/how-do-i-know-what-the-field-names-are-in-osm-files)

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
<span id="post-16049-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16049-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-16049-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to use osmconvert to convert an osm file to a csv file with just the street, city, state, latitude/longitude fields. But I don't know what the actual field names are in the osm file. How do I open it to see or is there a list somewhere? The .osm file is rather large, so if there was a cmd line to view fields, that would be easier. Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-fields" rel="tag" title="see questions tagged &#39;fields&#39;">fields</span> <span class="post-tag tag-link-osmconvert" rel="tag" title="see questions tagged &#39;osmconvert&#39;">osmconvert</span> <span class="post-tag tag-link-csv" rel="tag" title="see questions tagged &#39;csv&#39;">csv</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Sep '12, 22:08</strong></p>
<img src="https://secure.gravatar.com/avatar/a45de846d76d68849c0e70b6fd21f256?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JMB5&#39;s gravatar image" />
<p><span>JMB5</span><br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JMB5 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Sep '12, 22:09</strong> </span></p>
</div>
</div>
<div id="comments-container-16049" class="comments-container">
&#10;</div>
<div id="comment-tools-16049" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16049-form-container" class="comment-form-container">
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

<span id="16051"></span>

<div id="answer-container-16051" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-16051-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16051-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-16051-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you want to see what the most commonly used keys are worldwide, have a look at <a href="http://taginfo.openstreetmap.org/">Taginfo</a>. You can use standard GNU/Unix utilities to look at what's in the ".osm" file, if it's too big for a text editor. If you're on Windows and don't have things like "grep" available, have a look at <a href="http://unxutils.sourceforge.net/">Unxutils</a>, which is a native build of most of the common GNU utilities for Windows, or <a href="http://www.cygwin.com/">Cygwin</a>, which is a slightly different approach to solving the same problem.</p>
<p>For example, looking at a small .osm file that I happen to have lying around:</p>
<pre><code>c:\Temp\osm\new&gt;grep &#39;k=&quot;highway&quot;&#39; local_101017_01.osm | wc
    3182     9546   109056</code></pre>
<p>I can see that there are 3182 "highway" items (roads, paths, bus stops etc.)</p>
<p>To see what sort of highway items there are I can do:</p>
<pre><code>c:\Temp\osm\new&gt;grep &#39;k=&quot;highway&quot;&#39; local_101017_01.osm | \utils\sort -u | more
&#10;  tag k=&quot;highway&quot; v=&quot;bridleway&quot;
  tag k=&quot;highway&quot; v=&quot;bus_stop&quot;
  tag k=&quot;highway&quot; v=&quot;cycleway&quot;
  tag k=&quot;highway&quot; v=&quot;footway&quot;
  tag k=&quot;highway&quot; v=&quot;ford&quot;</code></pre>
<p>(rest of output truncated and chevrons removed)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Sep '12, 23:36</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-16051" class="comments-container">
&#10;</div>
<div id="comment-tools-16051" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16051-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="16116"></span>

<div id="answer-container-16116" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-16116-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16116-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-16116-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Have a look at the similar program osmfilter.</p>
<p>It has features to produce a listing for all used keys in an osm file, see <a href="https://wiki.openstreetmap.org/wiki/Osmfilter#Getting_Tag_Statistics">Osmfilter#Getting_Tag_Statistics</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Sep '12, 14:35</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-16116" class="comments-container">
&#10;</div>
<div id="comment-tools-16116" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16116-form-container" class="comment-form-container">
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


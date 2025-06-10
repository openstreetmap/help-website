+++
type = "question"
title = "How to convert nodes of a way from OSM to excell in a correct order?"
description = '''I have read some posts on this subject but none of them solved my problem.  I have a file Olszon.osm which opens well in JOSM, has one long way of about 7000 nodes. It starts with  &amp;lt;osm version=&quot;0.6&quot; generator=&quot;osmfilter 1.2S&quot;&amp;gt;  &amp;lt;node id=&quot;137350351&quot; lat=&quot;53.0048676&quot; lon=&quot;106.9679891&quot; versio...'''
date = "2014-05-30T21:26:00Z"
lastmod = "2014-05-30T22:10:00Z"
weight = 33566
keywords = [ "convert" ]
aliases = [ "/questions/33566" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to convert nodes of a way from OSM to excell in a correct order?](/questions/33566/how-to-convert-nodes-of-a-way-from-osm-to-excell-in-a-correct-order)

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
<span id="post-33566-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33566-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-33566-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have read some posts on this subject but none of them solved my problem.</p>
<p>I have a file Olszon.osm which opens well in JOSM, has one long way of about 7000 nodes. It starts with</p>
&lt;osm version="0.6" generator="osmfilter 1.2S"&gt; &lt;node id="137350351" lat="53.0048676" lon="106.9679891" version="8" timestamp="2013-01-23T00:04:12Z" changeset="14752406" uid="214969" user="AndrewBuck"/&gt; &lt;node id="137350353" lat="53.0111087" lon="106.9858454" version="8" timestamp="2013-01-23T00:04:12Z" changeset="14752406" uid="214969" user="AndrewBuck"/&gt; ....
<p>then in the middle start references:</p>
<p>&lt;nd ref="2125463617"/&gt; &lt;nd ref="2125463613"/&gt; &lt;nd ref="2125463612"/&gt; &lt;nd ref="2125463611"/&gt; ...</p>
<p>I tried to convert it to .csv file by typing:</p>
<p>osmconvert Olszon.osm --all-to-nodes --csv="<span>@id</span> <span>@lat</span> <span>@lon</span>" --csv=headline &gt; Olszon.csv</p>
<p>but wat I get is Olszon.csv file that contains nodes but they are not in good order. The first node in .csv file has id = 137350351 but the first node on the way should have id = 2125463613.</p>
<p>How to solve the problem? Writing a script in VBA?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-convert" rel="tag" title="see questions tagged &#39;convert&#39;">convert</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 May '14, 21:26</strong></p>
<img src="https://secure.gravatar.com/avatar/9b18be372f895390b2f63a41066498a5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="miko679&#39;s gravatar image" />
<p><span>miko679</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="miko679 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-33566" class="comments-container">
&#10;</div>
<div id="comment-tools-33566" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33566-form-container" class="comment-form-container">
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

<span id="33569"></span>

<div id="answer-container-33569" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-33569-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33569-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-33569-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Converting an OSM file to CSV is a task that can be done in different ways; however, since OSM files can normally contain multiple ways that sometimes share the same nodes, it is not generally possible to convert OSM to CSV so that "nodes are in the right order" - there might be any number of "right orders", even though in your specific case there's only one.</p>
<p>Writing a small program that does the conversion you want will probably be the easiest way - on Unix with Perl installed, this could be as simple as</p>
<pre><code>perl -n -e &#39;if (/&lt;node id=.(\d+).*lat=.([-0-9.]+).*lon=.([-0-9.]+)/) { $p{$1}=[$2,$3]; } elsif (/nd ref=.(\d+)/) { printf &quot;%f,%f\n&quot;, $p{$1}[0],$p{$1}[1] }&#39; &lt; Olszon.osm</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 May '14, 22:10</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-33569" class="comments-container">
&#10;</div>
<div id="comment-tools-33569" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33569-form-container" class="comment-form-container">
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


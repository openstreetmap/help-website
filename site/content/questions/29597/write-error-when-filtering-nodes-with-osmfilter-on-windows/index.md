+++
type = "question"
title = "Write error when filtering nodes with osmfilter on Windows"
description = '''Hi, I&#x27;m using the windows version of osmfilter to try and extract city and town names with lat and long. The idea being to build a gazeteer for use in memory map. The command i use is osmfilter spain.o5m --keep-tags=&quot;city&quot; --keep-tags=&quot;town&quot;-o=mycity.osm The program runs, seems to be working but the...'''
date = "2014-01-05T12:45:00Z"
lastmod = "2014-01-07T19:58:00Z"
weight = 29597
keywords = [ "filter", "nodes", "osmfilter", "error" ]
aliases = [ "/questions/29597" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Write error when filtering nodes with osmfilter on Windows](/questions/29597/write-error-when-filtering-nodes-with-osmfilter-on-windows)

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
<span id="post-29597-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29597-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-29597-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I'm using the windows version of osmfilter to try and extract city and town names with lat and long. The idea being to build a gazeteer for use in memory map. The command i use is</p>
<p>osmfilter spain.o5m --keep-tags="city" --keep-tags="town"-o=mycity.osm</p>
<p>The program runs, seems to be working but then keeps returning osmfilter error : write error</p>
<p>I've searched using google and one other person has asked about this error but no answer was given.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-osmfilter" rel="tag" title="see questions tagged &#39;osmfilter&#39;">osmfilter</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Jan '14, 12:45</strong></p>
<img src="https://secure.gravatar.com/avatar/fa76fbaffb3f0cf67f7bf8f94308e50e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="daveasbury&#39;s gravatar image" />
<p><span>daveasbury</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="daveasbury has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Jan '14, 13:29</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span></p>
</div>
</div>
<div id="comments-container-29597" class="comments-container">
&#10;</div>
<div id="comment-tools-29597" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29597-form-container" class="comment-form-container">
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

<span id="29598"></span>

<div id="answer-container-29598" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29598-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29598-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-29598-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You have misunderstood the <code>--keep-tags</code> option. It does not actually filter the objects - it just decides which <em>tags</em> to copy over to the output. This means that your command will include all input objects in the output (instead of just cities and towns).</p>
<p>The write error is likely a consequence of this misunderstanding; your command results in a file of about 9 GB and it is possible that you are either out of disk space, or even using a file system that cannot handle files that large.</p>
<p>What you want is:</p>
<pre><code>osmfilter spain.o5m --keep-nodes=&quot;place=city =town&quot; --keep-ways= --keep-relations= -o=mycity.osm</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Jan '14, 13:28</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-29598" class="comments-container">
<span id="29599"></span>
<div id="comment-29599" class="comment">
<div id="post-29599-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the reply. I've sorted the write error. You are correct about the filtering. So is it possible to filter in the form - copy one town and cities?</p>
<p>I've tried various examples but none seem to do what i'm after</p>
</div>
<div id="comment-29599-info" class="comment-info">
<span class="comment-age">(05 Jan '14, 14:37)</span> <span class="comment-user userinfo">daveasbury</span>
</div>
</div>
<span id="29617"></span>
<div id="comment-29617" class="comment">
<div id="post-29617-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>so you want to limit your result to a smaller area?</p>
<p>If yes, can you define that area via a boundingbox or a boundary relation from the OSM data? like <a href="http://www.openstreetmap.org/relation/2417889">http://www.openstreetmap.org/relation/2417889</a> ?</p>
</div>
<div id="comment-29617-info" class="comment-info">
<span class="comment-age">(06 Jan '14, 16:26)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
<span id="29618"></span>
<div id="comment-29618" class="comment">
<div id="post-29618-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Nope.</p>
<p>What I am attempting is to take the file spain-latest.osm.pbf which i obtained, and extract all the towns and cities contained within it as well as their lat and long. This data would be ouput to a csv file in the form</p>
<h1 id="example">Example</h1>
<p>Barcelona 28.00023 3.34568</p>
<p>benidorm 28.00034 3.90987</p>
<p>this I would hope to import into the program memory map navigator to create a town look up gazeteer.</p>
</div>
<div id="comment-29618-info" class="comment-info">
<span class="comment-age">(06 Jan '14, 19:52)</span> <span class="comment-user userinfo">daveasbury</span>
</div>
</div>
<span id="29626"></span>
<div id="comment-29626" class="comment not_top_scorer">
<div id="post-29626-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The command in the grey box at the end of my original reply does just that (it doesn't give you a CSV but an OSM file with only towns and cities).</p>
</div>
<div id="comment-29626-info" class="comment-info">
<span class="comment-age">(07 Jan '14, 09:48)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="29637"></span>
<div id="comment-29637" class="comment">
<div id="post-29637-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>... and then use <a href="http://wiki.openstreetmap.org/wiki/Osmconvert">http://wiki.openstreetmap.org/wiki/Osmconvert</a> to convert your OSM file to a CSV file where you determine yourself what elements should be in the output file.</p>
<p>Read that documentation in the OSM wiki and try several tags.</p>
</div>
<div id="comment-29637-info" class="comment-info">
<span class="comment-age">(07 Jan '14, 16:51)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
<span id="29639"></span>
<div id="comment-29639" class="comment">
<div id="post-29639-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Thanks folks! finally sorted thanks to your replies using osmfilter spain.o5m --keep-nodes="place=city =town =village =hamlet =suburb =province" --keep-ways= --keep-relations= &gt;mycity.osm</p>
<p>and</p>
<p>osmconvert mycity.osm --csv="name place province <span>@lat</span> <span>@lon</span>" -o=somefilename.csv</p>
<p>this i imported into memorymap to work with my Mobac maps and it works!</p>
</div>
<div id="comment-29639-info" class="comment-info">
<span class="comment-age">(07 Jan '14, 19:58)</span> <span class="comment-user userinfo">daveasbury</span>
</div>
</div>
</div>
<div id="comment-tools-29598" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-29598-form-container" class="comment-form-container">
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


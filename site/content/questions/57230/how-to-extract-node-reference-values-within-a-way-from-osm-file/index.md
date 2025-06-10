+++
type = "question"
title = "How to extract node reference values within a way from osm file"
description = '''Hello, I need to have order of nodes within a way. For instance: &amp;lt;way id=&quot;10053349&quot;&amp;gt; &amp;lt;nd ref=&quot;4534884733&quot;/&amp;gt; &amp;lt;nd ref=&quot;4534884725&quot;/&amp;gt; &amp;lt;nd ref=&quot;4534884748&quot;/&amp;gt; &amp;lt;nd ref=&quot;82608659&quot;/&amp;gt; &amp;lt;nd ref=&quot;82608658&quot;/&amp;gt; &amp;lt;nd ref=&quot;639108039&quot;/&amp;gt; &amp;lt;nd ref=&quot;3451083060&quot;/&amp;gt; &amp;lt;nd ref=...'''
date = "2017-07-22T00:51:00Z"
lastmod = "2017-07-22T11:22:00Z"
weight = 57230
keywords = [ "osmfilter", "osmconvert", "osm" ]
aliases = [ "/questions/57230" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to extract node reference values within a way from osm file](/questions/57230/how-to-extract-node-reference-values-within-a-way-from-osm-file)

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
<span id="post-57230-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57230-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-57230-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I need to have order of nodes within a way. For instance:</p>
<pre><code>&lt;way id=&quot;10053349&quot;&gt;
&lt;nd ref=&quot;4534884733&quot;/&gt;
&lt;nd ref=&quot;4534884725&quot;/&gt;
&lt;nd ref=&quot;4534884748&quot;/&gt;
&lt;nd ref=&quot;82608659&quot;/&gt;
&lt;nd ref=&quot;82608658&quot;/&gt;
&lt;nd ref=&quot;639108039&quot;/&gt;
&lt;nd ref=&quot;3451083060&quot;/&gt;
&lt;nd ref=&quot;345553449&quot;/&gt;
&lt;nd ref=&quot;345553447&quot;/&gt;
&lt;nd ref=&quot;345553431&quot;/&gt;
&lt;nd ref=&quot;3451083057&quot;/&gt;
&lt;nd ref=&quot;345553432&quot;/&gt;
&lt;nd ref=&quot;345553433&quot;/&gt;
&lt;nd ref=&quot;345553434&quot;/&gt;
&lt;nd ref=&quot;345553435&quot;/&gt;
&lt;nd ref=&quot;3451083068&quot;/&gt;
&lt;nd ref=&quot;345553436&quot;/&gt;
&lt;nd ref=&quot;29564147&quot;/&gt;
&lt;nd ref=&quot;345553437&quot;/&gt;
&lt;nd ref=&quot;345553438&quot;/&gt;
&lt;nd ref=&quot;3451083079&quot;/&gt;
&lt;nd ref=&quot;345553439&quot;/&gt;
&lt;nd ref=&quot;3451083082&quot;/&gt;
&lt;nd ref=&quot;345553440&quot;/&gt;
&lt;nd ref=&quot;1326631485&quot;/&gt;
&lt;nd ref=&quot;82608663&quot;/&gt;
&lt;nd ref=&quot;82608662&quot;/&gt;
&lt;nd ref=&quot;4534884733&quot;/&gt;
&lt;tag k=&quot;addr:housenumber&quot; v=&quot;21&quot;/&gt;
&lt;tag k=&quot;addr:street&quot; v=&quot;Arcisstraße&quot;/&gt;
&lt;tag k=&quot;amenity&quot; v=&quot;university&quot;/&gt;
&lt;tag k=&quot;building&quot; v=&quot;yes&quot;/&gt;
&lt;tag k=&quot;name&quot; v=&quot;1&quot;/&gt;
&lt;tag k=&quot;wheelchair&quot; v=&quot;yes&quot;/&gt;</code></pre>
<p>&lt;/way&gt;</p>
<p>I need to retrieve only a list like following from above code:</p>
<p>4534884733 4534884725 4534884748 82608659 82608658 639108039 ...</p>
<p>I tried to use osmfilter and osmconvert, but could not find any command. Any suggestions? I need this for an application where the order of latitudes and longitudes is important.</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmfilter" rel="tag" title="see questions tagged &#39;osmfilter&#39;">osmfilter</span> <span class="post-tag tag-link-osmconvert" rel="tag" title="see questions tagged &#39;osmconvert&#39;">osmconvert</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Jul '17, 00:51</strong></p>
<img src="https://secure.gravatar.com/avatar/4b277923b00d40760b68fd056f14c76d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="omidrad&#39;s gravatar image" />
<p><span>omidrad</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="omidrad has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-57230" class="comments-container">
&#10;</div>
<div id="comment-tools-57230" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57230-form-container" class="comment-form-container">
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

<span id="57231"></span>

<div id="answer-container-57231" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-57231-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57231-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-57231-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Your question does not make a lot of sense for the following reasons:</p>
<ul>
<li>The order of nodes is significant for everyone who processes a way, not just for your application.</li>
<li>You can trivially convert the list of node IDs into a textual form with a few lines of code in a scripting language of your choice (Perl: <code>cat myfile | perl -ne 'END { print join(" ", </code><a href="https://help.openstreetmap.org/users/4517/nidi"></a><a href="https://help.openstreetmap.org/users/4517/nidi"><code>@nid</code></a></a><code>)."\n"; } push(</code><a href="https://help.openstreetmap.org/users/4517/nidi"></a><a href="https://help.openstreetmap.org/users/4517/nidi"><code>@nid</code></a></a><code>,$1) if (/&lt;nd ref="(\d+)"/);'</code> or shell: <code>cat myfile | grep "&lt;nd ref"|cut -d\" -f2|xargs echo</code>) but is that really your question? The list of Node IDs is <em>not</em> a list of latitudes and longitudes.</li>
</ul>
<p>If you are hoping to extract a sequence of latitudes and longitudes for all nodes in a way, then the easiest way is to run your OSM XML file (which of course has to have the matching node data referenced by your ways) through the <code>osmium</code> command line tool, writing out an XML file with the osmium specific <code>locations_on_ways</code> option.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Jul '17, 10:16</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-57231" class="comments-container">
<span id="57232"></span>
<div id="comment-57232" class="comment">
<div id="post-57232-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks a lot for the reply.</p>
<p>Actually I have a csv file containing 3 columns : ID, lat and lon of a building footprint which I obtained using osmconvert. I have loaded this csv file into a list in my Java code.</p>
<p>However, the order of the lats and lons are not sorted to form a correct polygon of the footprint. I wanted to have the correct sequence using the ref values of the way to sort the list in my Java code.</p>
</div>
<div id="comment-57232-info" class="comment-info">
<span class="comment-age">(22 Jul '17, 11:22)</span> <span class="comment-user userinfo">omidrad</span>
</div>
</div>
</div>
<div id="comment-tools-57231" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57231-form-container" class="comment-form-container">
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


+++
type = "question"
title = "How to convert an OSM file to OBF, via command-line"
description = '''I have a remote server tasked with regularly generating .osm files from Wikivoyage listings. I would like that server to also convert from .osm to .obf While this conversion is easy with the GUI of OsmAndMapCreator (screenshot below), I am not sure how to proceed by command-line (bash). '''
date = "2013-12-18T09:12:00Z"
lastmod = "2023-10-27T22:56:00Z"
weight = 29155
keywords = [ "obf", "osmand" ]
aliases = [ "/questions/29155" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to convert an OSM file to OBF, via command-line](/questions/29155/how-to-convert-an-osm-file-to-obf-via-command-line)

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
<span id="post-29155-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29155-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-29155-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a remote server tasked with regularly generating .osm files from <a href="http://en.wikivoyage.org">Wikivoyage</a> listings.</p>
<p>I would like that server to also convert from <a href="https://sourceforge.net/projects/wikivoyage/files/Listings-as-OSM/">.osm</a> to <a href="https://sourceforge.net/projects/wikivoyage/files/Listings-as-OBF/">.obf</a><br />
While this conversion is easy with the GUI of OsmAndMapCreator (screenshot below), I am not sure how to proceed by command-line (bash).</p>
<p><img src="http://img5.imageshack.us/img5/2305/mf7q.png" alt="OsmAnd Map Creator - Create .obf from osm file..." /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-obf" rel="tag" title="see questions tagged &#39;obf&#39;">obf</span> <span class="post-tag tag-link-osmand" rel="tag" title="see questions tagged &#39;osmand&#39;">osmand</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Dec '13, 09:12</strong></p>
<img src="https://secure.gravatar.com/avatar/c3af87f6b1d4d247d01ce3b73d918fc7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nicolas%20Raoul&#39;s gravatar image" />
<p><span>Nicolas Raoul</span><br />
<span class="score" title="645 reputation points">645</span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="25 badges"><span class="silver">●</span><span class="badgecount">25</span></span><span title="33 badges"><span class="bronze">●</span><span class="badgecount">33</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nicolas Raoul has one accepted answer">20%</span> </br></p>
</img>
</div>
</div>
<div id="comments-container-29155" class="comments-container">
&#10;</div>
<div id="comment-tools-29155" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29155-form-container" class="comment-form-container">
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

<span id="29156"></span>

<div id="answer-container-29156" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29156-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29156-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-29156-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>1) Create 2 folders, for instance <code>/home/nico/osm2obf/input</code> and <code>/home/nico/osm2obf/output</code></p>
<p>2) Put your OSM file(s) in <code>/home/nico/osm2obf/input</code>.</p>
<p>3) Create this file in the folder where OsmAndMapCreator is installed:</p>
<pre><code>&lt;?xml version=&quot;1.0&quot; encoding=&quot;utf-8&quot;?&gt;
&lt;batch_process&gt;
    &lt;process_attributes
        mapZooms=&quot;&quot;
        renderingTypesFile=&quot;&quot;
        zoomWaySmoothness=&quot;&quot; 
        osmDbDialect=&quot;sqlite&quot;
        mapDbDialect=&quot;sqlite&quot;/&gt;
    &lt;process
        directory_for_osm_files=&quot;/home/nico/osm2obf/input&quot;
        directory_for_index_files=&quot;/home/nico/osm2obf/output&quot;
        directory_for_generation=&quot;/home/nico/osm2obf/output&quot;
        skipExistingIndexesAt=&quot;&quot;
        indexPOI=&quot;true&quot;
        indexRouting=&quot;false&quot;
        indexMap=&quot;false&quot;
        indexTransport=&quot;false&quot;
        indexAddress=&quot;false&quot;&gt;
    &lt;/process&gt;
&lt;/batch_process&gt;</code></pre>
<p>4) Run this command:</p>
<pre><code>java -Djava.util.logging.config.file=logging.properties -Xms256M -Xmx2560M -cp &quot;./OsmAndMapCreator.jar:./lib/OsmAnd-core.jar:./lib/*.jar&quot; net.osmand.data.index.IndexBatchCreator osm2obf.xml</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Dec '13, 09:36</strong></p>
<img src="https://secure.gravatar.com/avatar/c3af87f6b1d4d247d01ce3b73d918fc7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nicolas%20Raoul&#39;s gravatar image" />
<p><span>Nicolas Raoul</span><br />
<span class="score" title="645 reputation points">645</span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="25 badges"><span class="silver">●</span><span class="badgecount">25</span></span><span title="33 badges"><span class="bronze">●</span><span class="badgecount">33</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nicolas Raoul has one accepted answer">20%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Dec '13, 09:38</strong> </span></p>
</div>
</div>
<div id="comments-container-29156" class="comments-container">
&#10;</div>
<div id="comment-tools-29156" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29156-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="87952"></span>

<div id="answer-container-87952" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87952-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87952-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87952-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I have two more questions about this topic :</p>
<p>1) Could you update this answer : It seems net.osmand.data.index.IndexBatchCreator no more exists in 2023 versions 2) I noticed that the software increased from 2014 to 2023 from a size of 24MB to 189MB. What are the reasons for such great growth when the software of 2014 made it possible to do everything that the software of 2023?</p>
<p>thanks a lot for any answer</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Oct '23, 22:56</strong></p>
<img src="https://secure.gravatar.com/avatar/c189c06690bd74e121219ad54ddab475?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chris38&#39;s gravatar image" />
<p><span>chris38</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chris38 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-87952" class="comments-container">
&#10;</div>
<div id="comment-tools-87952" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87952-form-container" class="comment-form-container">
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


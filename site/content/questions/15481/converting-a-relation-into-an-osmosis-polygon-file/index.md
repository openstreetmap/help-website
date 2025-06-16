+++
type = "question"
title = "Converting a relation into an Osmosis polygon file"
description = '''I&#x27;m trying to use the boundary of London as a bounding polygon for an osmembrane pipeline. How do I convert https://www.openstreetmap.org/browse/relation/175342 into something more like https://wiki.openstreetmap.org/wiki/Osmosis/Polygon_Filter_File_Format so I can use it as the boundary polygon?'''
date = "2012-08-24T14:49:00Z"
lastmod = "2018-12-06T09:05:00Z"
weight = 15481
keywords = [ "london", "bounding-polygon", "osmosis" ]
aliases = [ "/questions/15481" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Converting a relation into an Osmosis polygon file](/questions/15481/converting-a-relation-into-an-osmosis-polygon-file)

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
<span id="post-15481-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15481-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-15481-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to use the boundary of London as a bounding polygon for an osmembrane pipeline. How do I convert <a href="https://www.openstreetmap.org/browse/relation/175342">https://www.openstreetmap.org/browse/relation/175342</a> into something more like <a href="https://wiki.openstreetmap.org/wiki/Osmosis/Polygon_Filter_File_Format">https://wiki.openstreetmap.org/wiki/Osmosis/Polygon_Filter_File_Format</a> so I can use it as the boundary polygon?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-london" rel="tag" title="see questions tagged &#39;london&#39;">london</span> <span class="post-tag tag-link-bounding-polygon" rel="tag" title="see questions tagged &#39;bounding-polygon&#39;">bounding-polygon</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Aug '12, 14:49</strong></p>
<img src="https://secure.gravatar.com/avatar/e4f9f47a8c9be862c0e6f344151013e6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PeterGribble&#39;s gravatar image" />
<p><span>PeterGribble</span><br />
<span class="score" title="66 reputation points">66</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PeterGribble has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-15481" class="comments-container">
&#10;</div>
<div id="comment-tools-15481" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15481-form-container" class="comment-form-container">
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

<span id="15483"></span>

<div id="answer-container-15483" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-15483-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15483-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-15483-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="PeterGribble has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I don't know if there is an easier way, but that is how I was doing:</p>
<p>With JOSM</p>
<ol>
<li>File-&gt;Download an object, choose the type "relation" and give the id, uncheck "Download referents" and check "Download members"</li>
<li>select all objects (Ctrl+A) and unselect the admin_centre (London in your example)</li>
<li>copy the data (Ctr+C), create a new Layer (Ctrl+N) and paste your data (Ctrl+V)</li>
<li>remove all the tags</li>
<li>save the layer created in a .osm file (Ctrl+S)</li>
<li>Use <a href="http://svn.openstreetmap.org/applications/utils/osm-extract/polygons/osm2poly.pl">osm2poly.pl</a> script for generate the poly file : perl osm2poly.pl data.osm &gt; data.poly</li>
</ol>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Aug '12, 15:22</strong></p>
<img src="https://secure.gravatar.com/avatar/a2839f25c5f2da24f6ffd25de1641684?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NicolasDumoulin&#39;s gravatar image" />
<p><span>NicolasDumoulin</span><br />
<span class="score" title="3327 reputation points"><span>3.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NicolasDumoulin has 15 accepted answers">13%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Sep '12, 16:36</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0e92f2d89853fd4e04c4b40a921e519b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pieren&#39;s gravatar image" />
<p><span>Pieren</span><br />
<span class="score" title="9847 reputation points"><span>9.8k</span></span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="157 badges"><span class="bronze">●</span><span class="badgecount">157</span></span></p>
</div>
</div>
<div id="comments-container-15483" class="comments-container">
<span id="15486"></span>
<div id="comment-15486" class="comment">
<div id="post-15486-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, that seems to have worked. It's cooking away now, so I'll have to see how it comes out!</p>
</div>
<div id="comment-15486-info" class="comment-info">
<span class="comment-age">(24 Aug '12, 16:33)</span> <span class="comment-user userinfo">PeterGribble</span>
</div>
</div>
<span id="15569"></span>
<div id="comment-15569" class="comment">
<div id="post-15569-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It seems to have come out in 60 different polygons, and when I ran my query it only found two results, whereas with a box covering the same rough area I got over 6000... Is that because the relation is made of 60 different ways? I've combined them in JOSM, and I'm about to try it again.</p>
</div>
<div id="comment-15569-info" class="comment-info">
<span class="comment-age">(28 Aug '12, 09:39)</span> <span class="comment-user userinfo">PeterGribble</span>
</div>
</div>
<span id="15570"></span>
<div id="comment-15570" class="comment">
<div id="post-15570-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I don't understand which query you're talking. Ensure that you're merging all the ways in JOSM, and remove all the tags. Then, you can check the resulting .poly file by opening it in a text editor. You should have only one polygon section in the file.</p>
</div>
<div id="comment-15570-info" class="comment-info">
<span class="comment-age">(28 Aug '12, 10:11)</span> <span class="comment-user userinfo">NicolasDumoulin</span>
</div>
</div>
<span id="15571"></span>
<div id="comment-15571" class="comment">
<div id="post-15571-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Have you seen the text at the top of osm2poly.pl? The bit about the "must have" tags is missing from Nicolas' description:</p>
<pre><code># script to convert an OSM file to a polygon file.
# the OSM file must follow certain conventions, namely
# each way must have a polygon_file and polygon_id tag,
# may have a note tag and must not have others.</code></pre>
</div>
<div id="comment-15571-info" class="comment-info">
<span class="comment-age">(28 Aug '12, 10:19)</span> <span class="comment-user userinfo">cartinus</span>
</div>
</div>
<span id="15574"></span>
<div id="comment-15574" class="comment not_top_scorer">
<div id="post-15574-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>you're right cartinus, but I've never done that in my previous usage of this script … so I don't know, but you may try ;)</p>
</div>
<div id="comment-15574-info" class="comment-info">
<span class="comment-age">(28 Aug '12, 10:48)</span> <span class="comment-user userinfo">NicolasDumoulin</span>
</div>
</div>
<span id="15795"></span>
<div id="comment-15795" class="comment">
<div id="post-15795-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Yeah, it seems the original data were split into different ways, and combining them in JOSM before converting has fixed the problem. It's all working fine! Thanks Nicolas :)</p>
</div>
<div id="comment-15795-info" class="comment-info">
<span class="comment-age">(04 Sep '12, 14:41)</span> <span class="comment-user userinfo">PeterGribble</span>
</div>
</div>
<span id="15796"></span>
<div id="comment-15796" class="comment not_top_scorer">
<div id="post-15796-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It seems that a JOSM plugin can be installed (name 'poly') and you can export the poly file directly from JOSM (<a href="http://josm.openstreetmap.de/wiki/Plugins)">http://josm.openstreetmap.de/wiki/Plugins)</a></p>
</div>
<div id="comment-15796-info" class="comment-info">
<span class="comment-age">(04 Sep '12, 16:40)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
</div>
<div id="comment-tools-15483" class="comment-tools">
<span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-15483-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="67081"></span>

<div id="answer-container-67081" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67081-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67081-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-67081-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can use: <a href="http://polygons.openstreetmap.fr/">http://polygons.openstreetmap.fr/</a></p>
<p>It will convert your relation ID to a poly file and it has an API :</p>
<blockquote>
<p><a href="http://polygons.openstreetmap.fr/get_poly.py?id=376823&amp;params=0">http://polygons.openstreetmap.fr/get_poly.py?id=376823&amp;params=0</a></p>
</blockquote>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Dec '18, 09:05</strong></p>
<img src="https://secure.gravatar.com/avatar/6863bef08c5e0bc17bee1e10c2b56b83?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Potdeyaourt&#39;s gravatar image" />
<p><span>Potdeyaourt</span><br />
<span class="score" title="61 reputation points">61</span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Potdeyaourt has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-67081" class="comments-container">
&#10;</div>
<div id="comment-tools-67081" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67081-form-container" class="comment-form-container">
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


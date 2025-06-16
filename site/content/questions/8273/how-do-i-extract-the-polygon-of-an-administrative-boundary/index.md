+++
type = "question"
title = "How do I extract the polygon of an administrative boundary?"
description = '''How do I extract the polygon of an administrative boundary from an OSM file?'''
date = "2011-10-04T09:32:00Z"
lastmod = "2022-01-06T12:33:00Z"
weight = 8273
keywords = [ "boundary", "extract", "polygon", ".osm" ]
aliases = [ "/questions/8273" ]
osqa_answers = 7
osqa_accepted = false
+++

<div class="headNormal">

# [How do I extract the polygon of an administrative boundary?](/questions/8273/how-do-i-extract-the-polygon-of-an-administrative-boundary)

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
<span id="post-8273-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8273-score" class="post-score" title="current number of votes">
8
</div>
<span id="post-8273-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
3
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How do I extract the polygon of an administrative boundary from an OSM file?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-boundary" rel="tag" title="see questions tagged &#39;boundary&#39;">boundary</span> <span class="post-tag tag-link-extract" rel="tag" title="see questions tagged &#39;extract&#39;">extract</span> <span class="post-tag tag-link-polygon" rel="tag" title="see questions tagged &#39;polygon&#39;">polygon</span> <span class="post-tag tag-link-.osm" rel="tag" title="see questions tagged &#39;.osm&#39;">.osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Oct '11, 09:32</strong></p>
<img src="https://secure.gravatar.com/avatar/315eacb418fe8b2a721db7ffe266df6a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fhedberg&#39;s gravatar image" />
<p><span>fhedberg</span><br />
<span class="score" title="121 reputation points">121</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fhedberg has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Nov '13, 14:49</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-8273" class="comments-container">
&#10;</div>
<div id="comment-tools-8273" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8273-form-container" class="comment-form-container">
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

7 Answers:

</div>

</div>

<span id="17511"></span>

<div id="answer-container-17511" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17511-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17511-score" class="post-score" title="current number of votes">
9
</div>
<span id="post-17511-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Here is an online tool to do that : <a href="http://polygons.openstreetmap.fr/index.py">http://polygons.openstreetmap.fr/index.py</a></p>
<p>Give it the id of the administrative relation (or whatever polygon relation), it outputs result in .poly, WKT (Gis format) and a nice image to view it ;-)</p>
<p>It also offers geometry simplification and extended buffer. It supports pyramidal relation</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Nov '12, 00:35</strong></p>
<img src="https://secure.gravatar.com/avatar/0137f3597f9ca0efbda5c3b1e2678aa7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sly&#39;s gravatar image" />
<p><span>sly</span><br />
<span class="score" title="290 reputation points">290</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sly has one accepted answer">25%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Jul '14, 23:55</strong> </span></p>
</div>
</div>
<div id="comments-container-17511" class="comments-container">
<span id="31112"></span>
<div id="comment-31112" class="comment">
<div id="post-31112-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>THANK YOU! It is a great tool!</p>
</div>
<div id="comment-31112-info" class="comment-info">
<span class="comment-age">(28 Feb '14, 09:13)</span> <span class="comment-user userinfo">exec</span>
</div>
</div>
</div>
<div id="comment-tools-17511" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17511-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="17368"></span>

<div id="answer-container-17368" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17368-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17368-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-17368-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>One more addition:</p>
<p><a href="http://overpass-api.de/api/interpreter?data=(rel(8638);%3E;);out;">http://overpass-api.de/api/interpreter?data=(rel(8638);&gt;;);out;</a></p>
<p>is even faster than the api/.../full call and preferable, because then api/full call causes significant load on the main api.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Nov '12, 19:02</strong></p>
<img src="https://secure.gravatar.com/avatar/fcfdb0825826fd13d2ff0d83d58819c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland%20Olbricht&#39;s gravatar image" />
<p><span>Roland Olbricht</span><br />
<span class="score" title="6666 reputation points"><span>6.7k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland Olbricht has 40 accepted answers">36%</span></p>
</div>
</div>
<div id="comments-container-17368" class="comments-container">
<span id="17464"></span>
<div id="comment-17464" class="comment">
<div id="post-17464-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>... and see <a href="https://wiki.openstreetmap.org/wiki/Overpass_API">https://wiki.openstreetmap.org/wiki/Overpass_API</a> about more documentation for overpassAPI</p>
</div>
<div id="comment-17464-info" class="comment-info">
<span class="comment-age">(04 Nov '12, 17:38)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
</div>
<div id="comment-tools-17368" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17368-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="8274"></span>

<div id="answer-container-8274" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8274-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8274-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-8274-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You could use this Perl script:</p>
<p><a href="http://svn.openstreetmap.org/applications/utils/osm-extract/polygons/rel2poly.pl">http://svn.openstreetmap.org/applications/utils/osm-extract/polygons/rel2poly.pl</a></p>
<p>It requires a "full" extract of the administrative boundary relation on input and has some limitations (see comments at the top of the file).</p>
<p>There's also a much more complex script that extracts all boundaries from a given OSM extract and can optionally write polygons:</p>
<p><a href="http://svn.openstreetmap.org/applications/utils/gary68/boundaries.pl">http://svn.openstreetmap.org/applications/utils/gary68/boundaries.pl</a></p>
<p>If you intend to use the polygon for making extracts, it may be wise to simplify it before use as extracting may take very long if the polygon is too big. Simplifying the polygon might, however, clip off bits, and you might want to look for a simplification algorithm that guarantees that the simplified polygon contains the original polygon.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Oct '11, 09:40</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Oct '11, 09:40</strong> </span></p>
</div>
</div>
<div id="comments-container-8274" class="comments-container">
<span id="8275"></span>
<div id="comment-8275" class="comment">
<div id="post-8275-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>In addition to Frederick's suggestions above, I used <a href="http://osm2mp.googlecode.com/svn/trunk/getbound/getbound.pl">http://osm2mp.googlecode.com/svn/trunk/getbound/getbound.pl</a> to create a boundary polygon for my local district. I didn't simplify it though, and the speed comparisons mentioned at <a href="https://wiki.openstreetmap.org/wiki/Tendring(Essex_District)#Data_Extracts">https://wiki.openstreetmap.org/wiki/Tendring(Essex_District)#Data_Extracts</a> suggest polygon vs bbox is over 20 times slower in my case.</p>
</div>
<div id="comment-8275-info" class="comment-info">
<span class="comment-age">(04 Oct '11, 09:47)</span> <span class="comment-user userinfo">EdLoach ♦</span>
</div>
</div>
</div>
<div id="comment-tools-8274" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8274-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="8276"></span>

<div id="answer-container-8276" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8276-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8276-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-8276-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>How I've done it:</p>
<ol>
<li>Download the data: <code>wget -O auvergneRel.osm </code><a href="http://api.openstreetmap.org/api/0.6/relation/8638/full"><code>http://api.openstreetmap.org/api/0.6/relation/8638/full</code></a></li>
<li>open the data in JOSM</li>
<li>delete all tags contained in the data</li>
<li>merge the ways</li>
<li>save your data, and run <a href="http://svn.openstreetmap.org/applications/utils/osm-extract/polygons/osm2poly.pl">osm2poly.pl</a>: <code>perl </code><a href="http://osm2poly.pl"><code>osm2poly.pl</code></a><code> auvergneRel.osm &gt; auvergne.poly</code></li>
</ol>
<p>I have never tested <a href="http://rel2poly.pl">rel2poly.pl</a> script. I haven't found a scripted way for merging the ways (deleting the tags is possible with osmosis by using a tagtransform filter).</p>
<p>I've used successfully this method several times. Hope that helps…</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Oct '11, 09:55</strong></p>
<img src="https://secure.gravatar.com/avatar/a2839f25c5f2da24f6ffd25de1641684?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NicolasDumoulin&#39;s gravatar image" />
<p><span>NicolasDumoulin</span><br />
<span class="score" title="3327 reputation points"><span>3.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NicolasDumoulin has 15 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-8276" class="comments-container">
<span id="64875"></span>
<div id="comment-64875" class="comment">
<div id="post-64875-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>There is a "poly" plugin for JOSM that lets you save your data directly as a .poly file.</p>
</div>
<div id="comment-64875-info" class="comment-info">
<span class="comment-age">(23 Jul '18, 15:23)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-8276" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8276-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="20361"></span>

<div id="answer-container-20361" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-20361-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20361-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-20361-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It depends, of course, of the format you want. Convert as written above.</p>
<ul>
<li>Display any part of the map in JOSM.</li>
<li>File&gt;new layer</li>
<li>Select what you want</li>
<li>Edit&gt;Merge Selection -&gt; new layer</li>
</ul>
<p>Repeat Select+Merge as many times as needed<br />
With new layer active,</p>
<ul>
<li>File&gt;Save As... -&gt; layer -&gt; xxx.osm file</li>
<li>same to save xx.gpx, xxx.json or compressed OSM files.</li>
</ul>
<p>A new layer is useful to display only the data you want to edit or save. Example with your boundary:</p>
<ul>
<li>display it in the main layer.</li>
<li>in Relations window, right-click your boundary&gt;Select relation</li>
<li>Edit&gt;Merge Selection -&gt; new layer</li>
</ul>
<p>With new layer active,</p>
<ul>
<li>right-click your boundary&gt;Download incomplete members</li>
<li>-&gt; your boundary to be a polygon</li>
</ul>
<p>If your admin_level relations contain admin_level+x relations as subareas (a very good idea), you can download whole chunks of boundaries going from one to the parent or child.<br />
You may save your work to an osm.file. But if you reload that file later, do:</p>
<ul>
<li>Edit&gt;Select all File&gt;Update selection</li>
<li>to keep your data in sync, else you may get nasty conflicts to solve.</li>
</ul>
<p>BEWARE BEWARE</p>
<p>If you delete something aesthetically in a layer, DO NOT File&gt;Update data in that layer, JOSM would actually delete that something from the real data. It is especially important to SAY NO to update suggestions when you close (Delete) a layer, or File&gt;Exit JOSM, or reload a saved file where such condition exists. You might carelessly delete huge amounts of data that way.</p>
<p>!!! Always carefully check what JOSM says it's going to do when updating the server.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Feb '13, 22:19</strong></p>
<img src="https://secure.gravatar.com/avatar/22d0547d929d81aa90014a6f0aef484a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GentilPapou&#39;s gravatar image" />
<p><span>GentilPapou</span><br />
<span class="score" title="160 reputation points">160</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GentilPapou has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-20361" class="comments-container">
&#10;</div>
<div id="comment-tools-20361" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20361-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="64871"></span>

<div id="answer-container-64871" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64871-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64871-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-64871-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Tried to use <a href="http://polygons.openstreetmap.fr/index.py">http://polygons.openstreetmap.fr/index.py</a> but it doesnt seems working properly with inner rings. Eg. try to look at relation 62657, you will see that it generates WKT with 2 polygons, where both are outer. It can be easily checked here: <a href="https://clydedacruz.github.io/openstreetmap-wkt-playground/">https://clydedacruz.github.io/openstreetmap-wkt-playground/</a>.</p>
<p>So there is <a href="https://www.diggernaut.com">web scraping service</a> with geo functionality, which has free tier so can be freely used for conversion. If you need to convert more than 5000 relations, you can compile scraper to run on your local computer / server without limitations. Below is a code for the scraper that do conversion job:</p>
<pre><code>---
config:
    debug: 2
    agent: Chrome
iterator:
- type: csv
  name: relation
  value: &quot;62657,62554,62378&quot;
do:
- geo:
    do:
    - wkt:
        relation: &lt;%relation%&gt;
        do:
        - find:
            path: wkt
            do:
            - object_new: item
            - parse
            - object_field_set:
                object: item
                field: wkt
            - argument_get: relation
            - object_field_set:
                object: item
                field: relation
            - object_save:
                name: item</code></pre>
<p>There is nore geo functionality available, you can read <a href="https://www.diggernaut.com/dev/meta-language-methods-geospatial-data-working-with-geospatial-data.html">documentation</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Jul '18, 12:49</strong></p>
<img src="https://secure.gravatar.com/avatar/a8fcc4bcfb1e16d234d5834b31ea585c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jako2008&#39;s gravatar image" />
<p><span>Jako2008</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jako2008 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Jul '18, 12:50</strong> </span></p>
</div>
</div>
<div id="comments-container-64871" class="comments-container">
<span id="64874"></span>
<div id="comment-64874" class="comment">
<div id="post-64874-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>OpenStreetMap's data is primarily released as raw data, and only secondarily in the form of web pages. Why anyone would want to scrape web sites using a third party tool instead of just using the data that is readily published, is beyond me.</p>
</div>
<div id="comment-64874-info" class="comment-info">
<span class="comment-age">(23 Jul '18, 15:22)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-64871" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64871-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="82972"></span>

<div id="answer-container-82972" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82972-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82972-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82972-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I tried to implement on the maps on the website <a href="https://www.przymorzu.pl">www.przymorzu.pl</a> administrative outlines for individual towns, but without success :(</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Jan '22, 12:33</strong></p>
<img src="https://secure.gravatar.com/avatar/c990aea3adcf52344c35a2fdb6c7e5f2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Przymorzu&#39;s gravatar image" />
<p><span>Przymorzu</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Przymorzu has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Jan '22, 12:37</strong> </span></p>
</div>
</div>
<div id="comments-container-82972" class="comments-container">
&#10;</div>
<div id="comment-tools-82972" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82972-form-container" class="comment-form-container">
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


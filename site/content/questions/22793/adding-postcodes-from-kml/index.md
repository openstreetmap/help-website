+++
type = "question"
title = "Adding postcodes from KML"
description = '''Hi, im trying to add all postal codes of spain from a KML file. Every postcode is a placemark with name, coordinates and a postcode, there is an example of an addres.  &amp;lt; Placemark&amp;gt;  &amp;lt; styleUrl&amp;gt;#default&amp;lt; /styleUrl&amp;gt;  &amp;lt; name&amp;gt;&amp;lt; ![CDATA[PostCode]]&amp;gt;&amp;lt; /name&amp;gt;  &amp;lt; Point&amp;...'''
date = "2013-05-27T12:24:00Z"
lastmod = "2013-05-27T13:12:00Z"
weight = 22793
keywords = [ "postalcode", "zip-code", "kml", "postcode", "address" ]
aliases = [ "/questions/22793" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Adding postcodes from KML](/questions/22793/adding-postcodes-from-kml)

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
<span id="post-22793-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22793-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-22793-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>im trying to add all postal codes of spain from a KML file. Every postcode is a placemark with name, coordinates and a postcode, there is an example of an addres.</p>
<pre><code>&lt; Placemark&gt;
   &lt; styleUrl&gt;#default&lt; /styleUrl&gt;
   &lt; name&gt;&lt; ![CDATA[PostCode]]&gt;&lt; /name&gt;
   &lt; Point&gt;
      &lt; coordinates&gt;-3.6666,40.4291&lt; /coordinates&gt;
   &lt; /Point&gt;
&lt; /Placemark&gt;</code></pre>
<p>(apologize about extra space at the beginning of each tag, is just for showing it)</p>
<p>My problem is that i cant find the tag for postcode or address, i made some test with &lt; address&gt;, &lt; postcode&gt; or &lt; addr:postcode&gt;(this tag is the same used in Potlatch 2) but never appear when i load the file with Potlatch.</p>
<p>what tag should i use to add this field?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-postalcode" rel="tag" title="see questions tagged &#39;postalcode&#39;">postalcode</span> <span class="post-tag tag-link-zip-code" rel="tag" title="see questions tagged &#39;zip-code&#39;">zip-code</span> <span class="post-tag tag-link-kml" rel="tag" title="see questions tagged &#39;kml&#39;">kml</span> <span class="post-tag tag-link-postcode" rel="tag" title="see questions tagged &#39;postcode&#39;">postcode</span> <span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 May '13, 12:24</strong></p>
<img src="https://secure.gravatar.com/avatar/8d14d8bb6bbba9c87b27580820bf6b75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dremel&#39;s gravatar image" />
<p><span>dremel</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dremel has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-22793" class="comments-container">
&#10;</div>
<div id="comment-tools-22793" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22793-form-container" class="comment-form-container">
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

<span id="22795"></span>

<div id="answer-container-22795" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-22795-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22795-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-22795-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Firstly you don't state the source of your data. It is important that external data loaded into OSM is both compatible with the OdBL licence (sorry for tautology) <strong>and</strong> that the import itself is carried out according to the <a href="https://wiki.openstreetmap.org/wiki/Import/Guidelines">established guidelines</a>.</p>
<p>Secondly, centroids for postal areas are not a useful object to map in OSM. They are not capable of being verified on the ground, and are much more useful when attached to other objects. For instance in Britain it is usually necessary to attach postal codes to individual buildings because of the granularity of the data. (In some cases all buildings on a road share a postcode so the street can also be tagged with addr:postcode). In many european countries most postcodes will be closely associated with communes, and thus can be added to a place=* tag. Making the centroids available outside OSM will meet 99.9999% of use cases which might be envisaged for holding this data in OSM.</p>
<p>Lastly, Potlatch is designed to discourage uploading of data. Things like KML and GPS traces are incorporated to assist a manual editing process, and as such no tag or other information is directly available in the editor.</p>
<p>It is possible to import this kind of data into OSM, but first it is important to check that you have fully covered my first two points. Importing data also requires a good degree of familiarity with OSM tools: the first requirement of performing an import is that the importer is capable of reverting it without damaging other contributions.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 May '13, 13:12</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-22795" class="comments-container">
&#10;</div>
<div id="comment-tools-22795" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22795-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="22794"></span>

<div id="answer-container-22794" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-22794-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22794-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-22794-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Please explain what you want to do. Do you want to add postal codes to OpenStreetMap? In that case, please be aware that such data imports have to abide by certain rules - most importantly, you have to make sure that the data is legally usable for OSM, and you have to discuss your plans beforehand. Type "import" in the search box above and read some of the answers.</p>
<p>Also, the data you seem to have is point coordinates, whereas OSM usually records post code areas (i.e. polygons).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 May '13, 13:09</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-22794" class="comments-container">
&#10;</div>
<div id="comment-tools-22794" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22794-form-container" class="comment-form-container">
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


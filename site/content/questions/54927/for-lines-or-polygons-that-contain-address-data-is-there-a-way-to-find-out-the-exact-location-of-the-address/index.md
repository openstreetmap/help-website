+++
type = "question"
title = "For lines or polygons that contain address data, is there a way to find out the exact location of the address?"
description = '''I&#x27;m new to OSM and I&#x27;m particularly interested in address point data. I found that many ways and relations contain address data, for example: &amp;lt;way id=&quot;4712941&quot; version=&quot;6&quot; timestamp=&quot;2015-03-16T03:16:49Z&quot; uid=&quot;2601744&quot; user=&quot;sctrojan79&quot; changeset=&quot;29509013&quot;&amp;gt;  &amp;lt;nd ref=&quot;30004021&quot;/&amp;gt;  &amp;lt;nd...'''
date = "2017-03-05T19:06:00Z"
lastmod = "2017-03-06T05:01:00Z"
weight = 54927
keywords = [ "point", "address" ]
aliases = [ "/questions/54927" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [For lines or polygons that contain address data, is there a way to find out the exact location of the address?](/questions/54927/for-lines-or-polygons-that-contain-address-data-is-there-a-way-to-find-out-the-exact-location-of-the-address)

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
<span id="post-54927-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54927-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-54927-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm new to OSM and I'm particularly interested in address point data. I found that many ways and relations contain address data, for example:</p>
<p>&lt;way id="4712941" version="6" timestamp="2015-03-16T03:16:49Z" uid="2601744" user="sctrojan79" changeset="29509013"&gt; &lt;nd ref="30004021"/&gt; &lt;nd ref="30004018"/&gt; &lt;nd ref="3401208140"/&gt; &lt;nd ref="2049285169"/&gt; &lt;nd ref="30004020"/&gt; &lt;nd ref="30004021"/&gt; &lt;tag k="name" v="Fire Station 30"/&gt; &lt;tag k="amenity" v="fire_station"/&gt; &lt;tag k="building" v="yes"/&gt; &lt;tag k="addr:city" v="Seattle"/&gt; &lt;tag k="addr:street" v="South Mount Baker Boulevard"/&gt; &lt;tag k="addr:postcode" v="98144"/&gt; &lt;tag k="addr:housenumber" v="2801"/&gt; &lt;/way&gt;</p>
<p>&lt;relation id="233742" version="4" timestamp="2015-02-27T20:27:27Z" uid="2601744" user="sctrojan79" changeset="29143782"&gt; &lt;member type="way" ref="40416110" role="outer"/&gt; &lt;member type="way" ref="40416111" role="inner"/&gt; &lt;member type="way" ref="40416112" role="inner"/&gt; &lt;tag k="name" v="Northwest Fisheries Science Center, NOAA"/&gt; &lt;tag k="type" v="multipolygon"/&gt; &lt;tag k="office" v="government"/&gt; &lt;tag k="source" v="yahoo_wms"/&gt; &lt;tag k="building" v="office"/&gt; &lt;tag k="addr:city" v="Seattle"/&gt; &lt;tag k="wheelchair" v="yes"/&gt; &lt;tag k="addr:street" v="Montlake Blvd E,"/&gt; &lt;tag k="addr:postcode" v="98112"/&gt; &lt;tag k="building:levels" v="3"/&gt; &lt;tag k="addr:housenumber" v="2725"/&gt; &lt;/relation&gt;</p>
<p>Is there a way to find out where exactly on a linear segment (or polygon) an address point exists? Or should I interpret it as "this entire linear segment (or polygon) represents an address"?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-point" rel="tag" title="see questions tagged &#39;point&#39;">point</span> <span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Mar '17, 19:06</strong></p>
<img src="https://secure.gravatar.com/avatar/113f3247b68d1f21a2c594b2b87519c3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zlzhao1104&#39;s gravatar image" />
<p><span>zlzhao1104</span><br />
<span class="score" title="61 reputation points">61</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zlzhao1104 has one accepted answer">100%</span></p>
</div>
</div>
<div id="comments-container-54927" class="comments-container">
&#10;</div>
<div id="comment-tools-54927" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54927-form-container" class="comment-form-container">
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

<span id="54928"></span>

<div id="answer-container-54928" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-54928-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54928-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-54928-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The latter. It should usually not be a linear segment but a polygon, and will usually represent a building or area that has the given address.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Mar '17, 19:18</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-54928" class="comments-container">
<span id="54937"></span>
<div id="comment-54937" class="comment">
<div id="post-54937-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you! That makes sense!</p>
</div>
<div id="comment-54937-info" class="comment-info">
<span class="comment-age">(06 Mar '17, 05:01)</span> <span class="comment-user userinfo">zlzhao1104</span>
</div>
</div>
</div>
<div id="comment-tools-54928" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54928-form-container" class="comment-form-container">
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


+++
type = "question"
title = "how to tag block of apartments with units?"
description = '''Hello, I would like to tag a group of apartment blocks, which share the same postal address, and which have several units (German: Stiegen). Each unit has a number and is the entrance to the apartments above. The units are numbered 1 to 8 in this case. The address is usually written like &quot;Hermann Br...'''
date = "2015-01-02T09:55:00Z"
lastmod = "2015-01-02T11:34:00Z"
weight = 39962
keywords = [ "unit", "mapnik", "apartmentblock" ]
aliases = [ "/questions/39962" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [how to tag block of apartments with units?](/questions/39962/how-to-tag-block-of-apartments-with-units)

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
<span id="post-39962-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-39962-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-39962-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, I would like to tag a group of apartment blocks, which share the same postal address, and which have several units (German: Stiegen). Each unit has a number and is the entrance to the apartments above.</p>
<p>The units are numbered 1 to 8 in this case. The address is usually written like "Hermann Broch-Gasse 1/4".</p>
<p>This is the apartment complex in question:</p>
<ul>
<li>Address: Hermann Broch-Gasse 1, Wien / Vienna, Austria</li>
<li>Way link: <a href="https://www.openstreetmap.org/way/90032986">https://www.openstreetmap.org/way/90032986</a></li>
<li>Geo coordinates link: <a href="https://www.openstreetmap.org/#map=19/48.16516/16.30273">https://www.openstreetmap.org/#map=19/48.16516/16.30273</a></li>
</ul>
<p>What I have done so far:</p>
<ol>
<li>tagged the units with separate "addr:housenumber" and "addr:unit". House number is the same and unit is numbered according to the surveyed units there.</li>
</ol>
<p>Expected result:</p>
<ol>
<li>A label in Mapnik with something like "1/1" "1/2" "1/3" etc.</li>
</ol>
<p>Unexpected result:</p>
<ol>
<li>A label in Mapnik with 8 times the label "1" for "housenumber 1".</li>
</ol>
<p>Ugly work-around:</p>
<ol>
<li>Tag with addr:housenumber="1/1" "1/2 "1/3" etc. and remove the addr:unit, but this is ugly, because in applications like OsmAnd, this shows up as a separate house number, even if it's just a unit. Also, it goes against the purpose of fine-grain tagging.</li>
<li>Tag with addr:housenumber="1/1" "1/2" "1/3" etc. and keep addr:unit, but this will create confusion sometime in the future: Maybe Mapnik would later label it with housenumber+unit, which would be "1/1/1", which is clearly wrong.</li>
</ol>
<p>Proposed solution:</p>
<ol>
<li>Enhance Mapnik with labeling of units, like "1/2", "1/3" or another, country-dependet form.</li>
<li>Please also give proposed recommendation for tagging so that I can finish tagging this apartment complex.</li>
</ol>
<p>Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-unit" rel="tag" title="see questions tagged &#39;unit&#39;">unit</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-apartmentblock" rel="tag" title="see questions tagged &#39;apartmentblock&#39;">apartmentblock</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Jan '15, 09:55</strong></p>
<img src="https://secure.gravatar.com/avatar/bf862c4ef89804882a62a35be60f3ebf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ErnstlAT&#39;s gravatar image" />
<p><span>ErnstlAT</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ErnstlAT has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Jan '15, 09:58</strong> </span></p>
</div>
</div>
<div id="comments-container-39962" class="comments-container">
<span id="39964"></span>
<div id="comment-39964" class="comment">
<div id="post-39964-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>This is an interesting example; it might be worth adding to the wiki page <a href="https://wiki.openstreetmap.org/wiki/Tag:building%3Dapartments">https://wiki.openstreetmap.org/wiki/Tag:building%3Dapartments</a></p>
</div>
<div id="comment-39964-info" class="comment-info">
<span class="comment-age">(02 Jan '15, 11:34)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-39962" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-39962-form-container" class="comment-form-container">
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

<span id="39963"></span>

<div id="answer-container-39963" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-39963-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-39963-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-39963-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ErnstlAT has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You are already doing the right thing.</p>
<p>Anything else would be classic "tagging for the renderer" which is a nono. The point of OSM is to collect as high quality and consistent geo-data as possible within the contraints of the project, not to make labels appear on one specific map rendering.</p>
<p>There is an existing issue for the "Mapnik" style discussing the rendering of addr:flat and addr:unit here <a href="https://github.com/gravitystorm/openstreetmap-carto/issues/264">https://github.com/gravitystorm/openstreetmap-carto/issues/264</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Jan '15, 10:47</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Jan '15, 10:57</strong> </span></p>
</div>
</div>
<div id="comments-container-39963" class="comments-container">
&#10;</div>
<div id="comment-tools-39963" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-39963-form-container" class="comment-form-container">
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


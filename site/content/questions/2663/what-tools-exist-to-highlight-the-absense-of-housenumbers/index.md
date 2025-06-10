+++
type = "question"
title = "What tools exist to highlight the absense of housenumbers ?"
description = '''There are a number of tools that highlight roads without names, encouraging users to survey them. What similar tools exist to highlight locations that needs to be surveyed for housenumbers ? Possible conditions the tools should look for:  A road starts or ends and there is no &#x27;addr&#x27; tagged node near...'''
date = "2011-02-01T20:58:00Z"
lastmod = "2011-12-18T16:26:00Z"
weight = 2663
keywords = [ "housenumbers" ]
aliases = [ "/questions/2663" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [What tools exist to highlight the absense of housenumbers ?](/questions/2663/what-tools-exist-to-highlight-the-absense-of-housenumbers)

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
<span id="post-2663-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2663-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-2663-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>There are a number of tools that highlight roads without names, encouraging users to survey them.</p>
<p>What similar tools exist to highlight locations that needs to be surveyed for housenumbers ?</p>
<p>Possible conditions the tools should look for:</p>
<ol>
<li>A road starts or ends and there is no 'addr' tagged node nearby.</li>
<li>An 'addr:interpolation' way does not have an addr tagged node on each end.</li>
</ol>
<p>Possible presentations of the data include:</p>
<ol>
<li>A slippy map, so that users can add a web routing user interface on it, e.g. YOURS.</li>
<li>The nodes where the errors occur in a file format supported by gpsbabel.</li>
</ol>
<p>(Please give only one tool per answer)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-housenumbers" rel="tag" title="see questions tagged &#39;housenumbers&#39;">housenumbers</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Feb '11, 20:58</strong></p>
<img src="https://secure.gravatar.com/avatar/d25927545eb18b4d577280081df5ce6b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nic%20Roets&#39;s gravatar image" />
<p><span>Nic Roets</span><br />
<span class="score" title="583 reputation points">583</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nic Roets has one accepted answer">6%</span></p>
</div>
</div>
<div id="comments-container-2663" class="comments-container">
&#10;</div>
<div id="comment-tools-2663" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2663-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="2700"></span>

<div id="answer-container-2700" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-2700-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2700-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-2700-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The address tool component of Geofabrik's <a href="http://tools.geofabrik.de/osmi/?view=addresses&amp;lon=8.40160&amp;lat=49.02311&amp;zoom=11&amp;opacity=0.43&amp;overlays=buildings,buildings_with_addresses,postal_code,nodes_with_addresses_defined,nodes_with_addresses_interpolated,no_addr_street,street_not_found,interpolation,interpolation_errors,connection_lines,nearest_points,nearest_roads">OSM Inspector</a> is able to explicitly identify examples of your second condition. It uses a slippy map, and offers direct links to browse and edit the data.</p>
<p>Indirectly OSM Inspector can be used to find the first condition, but expects buildings to be mapped first. This seems logical as there must be many roads with no buildings and therefore no addresses.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Feb '11, 00:00</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-2700" class="comments-container">
&#10;</div>
<div id="comment-tools-2700" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2700-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="9570"></span>

<div id="answer-container-9570" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9570-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9570-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-9570-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you use Merkaartor then you can create a custom style with the style editor. You can hide or highlight certain features you're interested in. Before I go surveying some area I change the colors of ways/houses with missing information to dark red and print the map, for example.</p>
<p>Here's my <a href="http://osm.kodafritt.se/files/Mapnik-SLB.mas">style file</a>. It colors buildings without addr:street/housenumber and residential roads without names. This version colors them in light blue/light red, but you can of course change that.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Dec '11, 14:20</strong></p>
<img src="https://secure.gravatar.com/avatar/31a583013e9eba8c178f5b54fad29098?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SamuelLB&#39;s gravatar image" />
<p><span>SamuelLB</span><br />
<span class="score" title="76 reputation points">76</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SamuelLB has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-9570" class="comments-container">
&#10;</div>
<div id="comment-tools-9570" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9570-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="9573"></span>

<div id="answer-container-9573" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9573-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9573-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-9573-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="http://www.itoworld.com/product/data/ito_map/main">ITO Map</a> has a layer for buildings and addresses. This highlights ways tagged as <code>building</code>, and whether or not they are tagged with address details. If they are tagged with <code>addr:housenumber</code> they are coloured green, if tagged with <code>addr:housename</code> or <code>name</code> they are blue, if no address they are red.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Dec '11, 16:26</strong></p>
<img src="https://secure.gravatar.com/avatar/aa505c046b1c010e997a7849c6f3dbbe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vclaw&#39;s gravatar image" />
<p><span>Vclaw</span><br />
<span class="score" title="9217 reputation points"><span>9.2k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="95 badges"><span class="silver">●</span><span class="badgecount">95</span></span><span title="141 badges"><span class="bronze">●</span><span class="badgecount">141</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vclaw has 41 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-9573" class="comments-container">
&#10;</div>
<div id="comment-tools-9573" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9573-form-container" class="comment-form-container">
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


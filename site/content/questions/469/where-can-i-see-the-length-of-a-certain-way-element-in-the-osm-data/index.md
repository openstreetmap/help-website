+++
type = "question"
title = "Where can I see the length of a certain way element in the OSM data?"
description = '''When I am looking at the pure data in a certain area (like in the data layer or in any editor), where can I see the length of one way element in meters?'''
date = "2010-07-24T11:26:00Z"
lastmod = "2019-11-18T11:39:00Z"
weight = 469
keywords = [ "data", "editor" ]
aliases = [ "/questions/469" ]
osqa_answers = 5
osqa_accepted = false
+++

<div class="headNormal">

# [Where can I see the length of a certain way element in the OSM data?](/questions/469/where-can-i-see-the-length-of-a-certain-way-element-in-the-osm-data)

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
<span id="post-469-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-469-score" class="post-score" title="current number of votes">
8
</div>
<span id="post-469-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>When I am looking at the pure data in a certain area (like in the data layer or in any editor), where can I see the length of one way element in meters?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span> <span class="post-tag tag-link-editor" rel="tag" title="see questions tagged &#39;editor&#39;">editor</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Jul '10, 11:26</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Jul '10, 14:50</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/2d4dfcdcde73aa5e2ffa4a9b3a7cb51d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jochen%20Topf&#39;s gravatar image" />
<p><span>Jochen Topf</span><br />
<span class="score" title="5244 reputation points"><span>5.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span></p>
</div>
</div>
<div id="comments-container-469" class="comments-container">
&#10;</div>
<div id="comment-tools-469" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-469-form-container" class="comment-form-container">
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

5 Answers:

</div>

</div>

<span id="471"></span>

<div id="answer-container-471" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-471-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-471-score" class="post-score" title="current number of votes">
8
</div>
<span id="post-471-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Pure OSM data only indirectly contains length information: The lengths themselves aren't stored anywhere but can be calculated from the nodes' coordinates. Therefore, you need a tool that calculates and displays this information.</p>
<p>OSM editing applications typically offer this feature:</p>
<ul>
<li>In JOSM, you can see the length of the selected way in the <a href="https://josm.openstreetmap.de/wiki/Help/StatusBar">status bar</a> at the bottom of the editor window (next to the <img src="https://josm.openstreetmap.de/export/15530/josm/trunk/images/statusline/dist.svg" alt="ruler" /> icon)</li>
<li>In iD, press Ctrl+Shift+M to toggle the measurement panel (alternatively click on "map data" in the right hand menu and tick "show measurements" field). Now click on the way that you want to know the length of.</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Jul '10, 12:45</strong></p>
<img src="https://secure.gravatar.com/avatar/0626be5f46f32fce501353e8a5ec399c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tordanik&#39;s gravatar image" />
<p><span>Tordanik</span><br />
<span class="score" title="11998 reputation points"><span>12.0k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="106 badges"><span class="silver">●</span><span class="badgecount">106</span></span><span title="147 badges"><span class="bronze">●</span><span class="badgecount">147</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tordanik has 58 accepted answers">35%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Dec '22, 06:39</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/a6e2839b04b99e35e45d64fe66b9a500?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rene78&#39;s gravatar image" />
<p><span>rene78</span><br />
<span class="score" title="700 reputation points">700</span><span title="29 badges"><span class="badge1">●</span><span class="badgecount">29</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span></p>
</div>
</div>
<div id="comments-container-471" class="comments-container">
&#10;</div>
<div id="comment-tools-471" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-471-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="487"></span>

<div id="answer-container-487" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-487-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-487-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-487-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Found one more on my own:</p>
<p>Maybe the <em>most simple</em> way to see the length of an OSM way element in a kind of data layer is to load the area (or just the way) in the editor Merkaartor <a href="http://wiki.openstreetmap.org/wiki/Merkaartor"></a><a href="http://wiki.openstreetmap.org/wiki/Merkaartor"></a><a href="http://wiki.openstreetmap.org/wiki/Merkaartor">http://wiki.openstreetmap.org/wiki/Merkaartor</a>.</p>
<p>You only need to hover over the way with the mouse, or select it. The length is displayed in the information panel on the right of the screen.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Jul '10, 15:51</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-487" class="comments-container">
&#10;</div>
<div id="comment-tools-487" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-487-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="484"></span>

<div id="answer-container-484" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-484-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-484-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-484-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Maperitive can show you lengths of ways:</p>
<ol>
<li>Load the OSM data from a file using the "<code>load-source mydata.osm</code>" command</li>
<li>Find a way using some kind of search criteria, for example "<code>find way[highway=footway]</code>". This will find all footways.</li>
<li>List the results using the "<code>list-results</code>" command. It will show a list of all matching ways, their IDs and lengths in meters.</li>
<li>You view each individual search result using the F3 (<code>find-next</code>) and SHIFT+F3 (<code>find-prev</code>) keys.</li>
</ol>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Jul '10, 13:59</strong></p>
<img src="https://secure.gravatar.com/avatar/591340f954c00c8208d5ffe668f50a05?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Breki&#39;s gravatar image" />
<p><span>Breki</span><br />
<span class="score" title="2040 reputation points"><span>2.0k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="18 badges"><span class="silver">●</span><span class="badgecount">18</span></span><span title="43 badges"><span class="bronze">●</span><span class="badgecount">43</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Breki has 5 accepted answers">10%</span></p>
</div>
</div>
<div id="comments-container-484" class="comments-container">
<span id="61069"></span>
<div id="comment-61069" class="comment">
<div id="post-61069-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Wow! Great tip!</p>
</div>
<div id="comment-61069-info" class="comment-info">
<span class="comment-age">(07 Dec '17, 19:28)</span> <span class="comment-user userinfo">Linhares</span>
</div>
</div>
</div>
<div id="comment-tools-484" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-484-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="71694"></span>

<div id="answer-container-71694" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71694-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71694-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-71694-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<ol>
<li>Visit <a href="https://openstreetmap.org/edit">https://openstreetmap.org/edit</a> and pan to location of interest.</li>
<li>Ctrl+Shift+M (Toggle measurement panel.)</li>
<li>Click on the <em>way</em> that you want length of.</li>
</ol>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Nov '19, 11:39</strong></p>
<img src="https://secure.gravatar.com/avatar/47edd1ee4d973c50bbe7991bb063d09d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jidanni&#39;s gravatar image" />
<p><span>jidanni</span><br />
<span class="score" title="339 reputation points">339</span><span title="32 badges"><span class="badge1">●</span><span class="badgecount">32</span></span><span title="36 badges"><span class="silver">●</span><span class="badgecount">36</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jidanni has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-71694" class="comments-container">
&#10;</div>
<div id="comment-tools-71694" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71694-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="483"></span>

<div id="answer-container-483" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-483-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-483-score" class="post-score" title="current number of votes">
-3
</div>
<span id="post-483-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OSM data contains only the geometries stored as nodes, ways and relations. If you want to obtain the some statistics on an element, you will need to work with tools like Postgis or specialized program.</p>
<p>Postgis 1.5 has a new geography type which can be used to return numbers like length, area in meters. You would need to use osm2pgsql to import your data and then create a geography column based on the geometry column created by osm2psql.</p>
<p>This method is quite complicated and should mostly be used for more advanced users.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Jul '10, 12:51</strong></p>
<img src="https://secure.gravatar.com/avatar/fc34340b0f5b16ceb2802f2c485801d6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Melaskia&#39;s gravatar image" />
<p><span>Melaskia</span><br />
<span class="score" title="149 reputation points">149</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Melaskia has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-483" class="comments-container">
&#10;</div>
<div id="comment-tools-483" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-483-form-container" class="comment-form-container">
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


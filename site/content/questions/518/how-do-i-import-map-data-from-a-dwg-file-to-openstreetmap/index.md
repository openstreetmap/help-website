+++
type = "question"
title = "How do I import map data from a .dwg file to OpenStreetMap?"
description = '''What are the tools and methods to sucessfully import map data from a .dwg file to OpenStreetMap?'''
date = "2010-07-30T17:28:00Z"
lastmod = "2018-05-20T20:30:00Z"
weight = 518
keywords = [ "import", "conversion", "tools", "dwg", "government" ]
aliases = [ "/questions/518" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How do I import map data from a .dwg file to OpenStreetMap?](/questions/518/how-do-i-import-map-data-from-a-dwg-file-to-openstreetmap)

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
<span id="post-518-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-518-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-518-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>What are the <strong>tools</strong> and <strong>methods</strong> to sucessfully import map data from a .dwg file to OpenStreetMap?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-conversion" rel="tag" title="see questions tagged &#39;conversion&#39;">conversion</span> <span class="post-tag tag-link-tools" rel="tag" title="see questions tagged &#39;tools&#39;">tools</span> <span class="post-tag tag-link-dwg" rel="tag" title="see questions tagged &#39;dwg&#39;">dwg</span> <span class="post-tag tag-link-government" rel="tag" title="see questions tagged &#39;government&#39;">government</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Jul '10, 17:28</strong></p>
<img src="https://secure.gravatar.com/avatar/77ac2d599553a2b1a968b473d4bf670b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vgeorge&#39;s gravatar image" />
<p><span>vgeorge</span><br />
<span class="score" title="201 reputation points">201</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vgeorge has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-518" class="comments-container">
&#10;</div>
<div id="comment-tools-518" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-518-form-container" class="comment-form-container">
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

<span id="519"></span>

<div id="answer-container-519" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-519-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-519-score" class="post-score" title="current number of votes">
12
</div>
<span id="post-519-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="vgeorge has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The first rule of imports is:</p>
<p><strong>If you have to ask - don't do it.</strong></p>
<p>Seriously, imports are difficult for a number of reasons. Firstly, not every import makes sense; for example, if it is third-party data which is well and actively maintained then importing the data into OSM will create a reduced-quality clone (because the data will not be updated when the original source updates). Or if the data is of a kind that cannot be sensibly improved by the community, like official boundaries or airspaces or building floor plans - that's also something that has very little reason to be in OSM. It is important to remember that OSM is a community mapping platform; data not meant for editing should not be in OSM.</p>
<p>Secondly, even if the data is good and suitable, imports can discourage people from getting engaged (because the map looks complete). This is a problem we're seeing in some areas where imports have boosted the data but not the community. Andy Allan has an excellent parable about imports, <a href="http://www.gravitystorm.co.uk/shine/archives/2009/11/10/the-pottery-club/">The Pottery Club</a>, and Matt Amos has run an interesting <a href="http://www.asklater.com/matt/wordpress/2009/09/imports-and-the-community/">simulation</a> that aims to illustrate the effect of imports on community growth.</p>
<p>Thirdly, doing imports properly requires a lot of knowledge. You have to select the right tagging, you have to make sure your data does not collide with anything that is already there, you have to make sure that adjacent polygons don't unnecessarily duplicate nodes, and so on. Some of these challenges can be solved by good importing software, some cannot.</p>
<p>The second rule of imports is:</p>
<p>Even if you find a program that seemingly does what you want, never try to run an import if you don't know exactly what the program does, and if you don't know exactly how to undo your import if something should go wrong.</p>
<p>Any import needs to be well planned, needs to be discussed with the community, and professionally executed. The usual credo of "something is better than nothing", which we often use when surveying, does not apply to imports. There is a high risk of imports actually damaging the project rather than being of use.</p>
<p>There is a piece of software that seems to read dxf files and create osm files, but it is seldom used and I have no idea whether or not this would work for your data set:</p>
<p><a href="http://github.com/h4ck3rm1k3/TwoNickels"></a><a href="http://github.com/h4ck3rm1k3/TwoNickels"></a><a href="http://github.com/h4ck3rm1k3/TwoNickels">http://github.com/h4ck3rm1k3/TwoNickels</a></p>
<p>Be sure to discuss your plans on the <a href="http://lists.openstreetmap.org/listinfo/imports">"imports" mailing list</a> before you do anything.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Jul '10, 23:55</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Dec '10, 12:59</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/9e04333be840d50c6aa66fb112aad77c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Harry%20Wood&#39;s gravatar image" />
<p><span>Harry Wood</span><br />
<span class="score" title="9489 reputation points"><span>9.5k</span></span><span title="25 badges"><span class="badge1">●</span><span class="badgecount">25</span></span><span title="88 badges"><span class="silver">●</span><span class="badgecount">88</span></span><span title="128 badges"><span class="bronze">●</span><span class="badgecount">128</span></span></p>
</div>
</div>
<div id="comments-container-519" class="comments-container">
<span id="545"></span>
<div id="comment-545" class="comment">
<div id="post-545-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Closed source CAD software might be necessary to convert DWG (Drawing) to DFX (Drawing File Exchange) formats, depending on the version of CAD used to generate the original file.</p>
</div>
<div id="comment-545-info" class="comment-info">
<span class="comment-age">(03 Aug '10, 07:59)</span> <span class="comment-user userinfo">Skippern</span>
</div>
</div>
</div>
<div id="comment-tools-519" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-519-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="63583"></span>

<div id="answer-container-63583" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63583-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63583-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63583-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Ad "Closed source CAD software": You can use GNU LibreDWG to read or write DWG or DXF files. I'm the maintainer of it, and I'm interested to create an automatic filter to ease the conversion from DWG (i.e. closed commercial GIS systems) to OpenStreetMap.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 May '18, 20:30</strong></p>
<img src="https://secure.gravatar.com/avatar/5c2888084ed6ac4c1c6e71cbd6bd23a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rurban&#39;s gravatar image" />
<p><span>rurban</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rurban has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-63583" class="comments-container">
&#10;</div>
<div id="comment-tools-63583" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63583-form-container" class="comment-form-container">
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


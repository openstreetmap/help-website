+++
type = "question"
title = "Can 3D building shapes be previewed?"
description = '''When constructing a model for a building (for example a church with steeple etc) using primitive shapes. Is there any way to preview what it will look like in 3d without having to wait the 24 hours for it to appear in F4-group map?'''
date = "2013-08-06T23:32:00Z"
lastmod = "2017-12-22T20:40:00Z"
weight = 25011
keywords = [ "building", "preview", "buildingtools", "3d" ]
aliases = [ "/questions/25011" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Can 3D building shapes be previewed?](/questions/25011/can-3d-building-shapes-be-previewed)

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
<span id="post-25011-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25011-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-25011-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>When constructing a model for a building (for example a church with steeple etc) using primitive shapes. Is there any way to preview what it will look like in 3d without having to wait the 24 hours for it to appear in F4-group map?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-building" rel="tag" title="see questions tagged &#39;building&#39;">building</span> <span class="post-tag tag-link-preview" rel="tag" title="see questions tagged &#39;preview&#39;">preview</span> <span class="post-tag tag-link-buildingtools" rel="tag" title="see questions tagged &#39;buildingtools&#39;">buildingtools</span> <span class="post-tag tag-link-3d" rel="tag" title="see questions tagged &#39;3d&#39;">3d</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Aug '13, 23:32</strong></p>
<img src="https://secure.gravatar.com/avatar/395602bfa099efbdc09dd6385ead265d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="CDP1&#39;s gravatar image" />
<p><span>CDP1</span><br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="CDP1 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-25011" class="comments-container">
&#10;</div>
<div id="comment-tools-25011" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25011-form-container" class="comment-form-container">
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

<span id="25031"></span>

<div id="answer-container-25031" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-25031-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25031-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-25031-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are different options for you to preview 3D renderings:</p>
<hr />
<p>The <strong><a href="http://wiki.openstreetmap.org/wiki/JOSM/Plugins/Kendzi3D">Kendzi 3D</a></strong> plugin for JOSM is probably the best choice for your purpose. It allows you to instantly view your editor contents in 3D and can easily be installed from within JOSM.</p>
<p><img src="http://wiki.openstreetmap.org/w/images/thumb/5/57/Kendzi3d_real_world_example.png/300px-Kendzi3d_real_world_example.png" alt="Kendzi3D Screenshot 1" /> <img src="http://wiki.openstreetmap.org/w/images/thumb/5/59/Kendzi3d_custom_models.png/300px-Kendzi3d_custom_models.png" alt="Kendzi3D Screenshot 2" /></p>
<hr />
<p>Alternatively, <strong><a href="http://osm2world.org/">OSM2World</a></strong> (<a href="http://wiki.openstreetmap.org/wiki/OSM2World">Wiki</a>) can also be used offline. It's a stand-alone program and a little bit harder to set up:</p>
<ul>
<li>Download and unzip "latest build" and "example texture selection" from the <a href="http://osm2world.org/download/">download page</a></li>
<li>Call the appropriate script for your operating system (.bat or .sh) in the OSM2World directory from the command line, and add the parameters <code>--config texture_config.properties --gui</code>, with "texture_config.properties" pointing to the file of that name from the "example texture selection" archive you have downloaded previously</li>
<li>From the program window, you can now open the .osm file you want to view (it also accepts saved files from JOSM) and reload it after edits</li>
</ul>
<p><img src="http://wiki.openstreetmap.org/w/images/thumb/7/75/OSM2World_building-levels-building-color.png/300px-OSM2World_building-levels-building-color.png" alt="OSM2World Screenshot 1" /> <img src="http://wiki.openstreetmap.org/w/images/thumb/0/08/OSM2World_amenity-waste_basket.png/300px-OSM2World_amenity-waste_basket.png" alt="OSM2World Screenshot 2" /></p>
<hr />
<p>It should be noted that both programs support some features not (yet?) present in F4 map - after all, they have been around for a few years already -, and interpret some things differently. For you, that means that there is no guarantee that F4 will render buildings in exactly the same way, but I still think it is very helpful to have the instant verification of your 3D mapping efforts.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Aug '13, 10:09</strong></p>
<img src="https://secure.gravatar.com/avatar/0626be5f46f32fce501353e8a5ec399c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tordanik&#39;s gravatar image" />
<p><span>Tordanik</span><br />
<span class="score" title="11998 reputation points"><span>12.0k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="106 badges"><span class="silver">●</span><span class="badgecount">106</span></span><span title="147 badges"><span class="bronze">●</span><span class="badgecount">147</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tordanik has 58 accepted answers">35%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Aug '13, 10:28</strong> </span></p>
</div>
</div>
<div id="comments-container-25031" class="comments-container">
<span id="25055"></span>
<div id="comment-25055" class="comment">
<div id="post-25055-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks Tordanik, I'll haven't used JOSM. So I will see if I can download and install, Java, JOSM &amp; the Kendz 3D plugin. Had a quick look at the download site looks like there may be issues with 64 bit windows. I'm using Windows 7 64 bit &amp; Chrome Browser Version 23.0.1271.64 m</p>
</div>
<div id="comment-25055-info" class="comment-info">
<span class="comment-age">(07 Aug '13, 23:11)</span> <span class="comment-user userinfo">CDP1</span>
</div>
</div>
<span id="61328"></span>
<div id="comment-61328" class="comment">
<div id="post-61328-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I've spent hours of researching and looking things up and I have yet to get Kendz 3D plugin. I'm using Java 8 update (151?) on MacOS and I can never get the plugin to run on any version of JOSM.</p>
</div>
<div id="comment-61328-info" class="comment-info">
<span class="comment-age">(22 Dec '17, 20:40)</span> <span class="comment-user userinfo">Mxdanger</span>
</div>
</div>
</div>
<div id="comment-tools-25031" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25031-form-container" class="comment-form-container">
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


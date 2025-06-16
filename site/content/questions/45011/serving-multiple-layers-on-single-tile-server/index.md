+++
type = "question"
title = "serving multiple layers on single tile server"
description = '''Hi, I followed the instructions on switch2osm setting up my own osm tile server and managed to render a small area of the osm map data. Now next I want to add another layer of the same area into the server so that the client is able to have different views of the area just like on the main osm web w...'''
date = "2015-09-01T11:01:00Z"
lastmod = "2015-09-08T10:56:00Z"
weight = 45011
keywords = [ "layers", "rendering", "renderd", "multiple", "server" ]
aliases = [ "/questions/45011" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [serving multiple layers on single tile server](/questions/45011/serving-multiple-layers-on-single-tile-server)

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
<span id="post-45011-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45011-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-45011-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I followed the instructions on switch2osm setting up my own osm tile server and managed to render a small area of the osm map data. Now next I want to add another layer of the same area into the server so that the client is able to have different views of the area just like on the main osm web where I can switch to Circle Map view or Transport Map view in addition to the standard view.</p>
<p>I could not be able to find much information about how to do this? Any advice on this would be appreciated. Now my configuration is Ubuntu14.04 64bt + Apache + Mod_tile(renderd) + mapnik + osmbright + Postgresql(PostGIS).</p>
<p>Thanks guys.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-layers" rel="tag" title="see questions tagged &#39;layers&#39;">layers</span> <span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-multiple" rel="tag" title="see questions tagged &#39;multiple&#39;">multiple</span> <span class="post-tag tag-link-server" rel="tag" title="see questions tagged &#39;server&#39;">server</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Sep '15, 11:01</strong></p>
<img src="https://secure.gravatar.com/avatar/0cd6d6bd835d840ee1df1f5a3310d099?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dalishi&#39;s gravatar image" />
<p><span>dalishi</span><br />
<span class="score" title="126 reputation points">126</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dalishi has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Jan '16, 14:48</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-45011" class="comments-container">
&#10;</div>
<div id="comment-tools-45011" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45011-form-container" class="comment-form-container">
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

<span id="45018"></span>

<div id="answer-container-45018" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-45018-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45018-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-45018-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="dalishi has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is easy. You need to add the additional layers to your renderd,conf and naturally you need the added style files, for example</p>
<pre><code>....
[noname]
URI=/noname/
XML=/usr/local/etc/mapnik/noname.xml
&#10;[noaddress]
URI=/noaddress/
XML=/usr/local/etc/mapnik/noaddress.xml
&#10;[has_address]
URI=/has_address/
XML=/usr/local/etc/mapnik/has_address.xml
....</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Sep '15, 18:33</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Sep '15, 18:34</strong> </span></p>
</div>
</div>
<div id="comments-container-45018" class="comments-container">
<span id="45019"></span>
<div id="comment-45019" class="comment">
<div id="post-45019-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Hi SimonPoole, thanks for your reply. I am sorry if I did not describe my case clearly. My two layers are from different data sources, e.g. maplayer1.pbf and maplayer2.pbf, both of exactly the same area. How do I set maplayer2.pbf to the postgresql database and how then configure to link the layers in the renderd probably I guess? Thanks.</p>
</div>
<div id="comment-45019-info" class="comment-info">
<span class="comment-age">(02 Sep '15, 03:32)</span> <span class="comment-user userinfo">dalishi</span>
</div>
</div>
<span id="45020"></span>
<div id="comment-45020" class="comment">
<div id="post-45020-score" class="comment-score">
2
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/11425/dalishi"></a><a href="https://help.openstreetmap.org/users/11425/dalishi">@dalishi</a> the datasource specifications are in the style file. If for whatever reason the data is different for the two extracts you have, you simply need to import them in to seperate database instances and adapt the datasource specs. I've never actually done that myself, but I don't see any reason why that shouldn't work.</p>
</div>
<div id="comment-45020-info" class="comment-info">
<span class="comment-age">(02 Sep '15, 06:58)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="45076"></span>
<div id="comment-45076" class="comment">
<div id="post-45076-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>One slight caveat to SimonPoole's original answer - it appears that the layers can't be called "[default]" (which they may be if someone's come via the switch2osm instructions). Maybe this has been fixed recently (I'm using fairly old versions). However, there's no need to change the URI for the resulting tiles - just the name of the section in /usr/local/etc/renderd.conf and the name of the directory below /usr/local/etc/renderd.conf change.</p>
</div>
<div id="comment-45076-info" class="comment-info">
<span class="comment-age">(05 Sep '15, 14:17)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="45115"></span>
<div id="comment-45115" class="comment">
<div id="post-45115-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Hi <a href="https://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a> thanks for the comments. I have tried and I can keep the [default] and add other sections below with their style xml respectively. For the URI I don't quite understand why you said no need to change. I assign each section with a URI, e.g URI=/osm_tiles/ for [dafault] and URI=/my_tiles/ for [myosm] which is my own section. I keep the TILEDIR=/var/lib/mod_tile the same though.</p>
</div>
<div id="comment-45115-info" class="comment-info">
<span class="comment-age">(08 Sep '15, 10:56)</span> <span class="comment-user userinfo">dalishi</span>
</div>
</div>
</div>
<div id="comment-tools-45018" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45018-form-container" class="comment-form-container">
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


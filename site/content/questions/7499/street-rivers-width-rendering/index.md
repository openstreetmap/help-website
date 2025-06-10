+++
type = "question"
title = "Street (rivers...) width rendering"
description = '''After reading Pieren&#x27;s comment to this Gnonthgol&#x27;s answer and after having no response (not even negative one) to this enhancement ticket for Mapnik I started to wonder:  What is the big obstacle that prevents rendering of real width for higher zoom levels?  I do not believe it is technically imposs...'''
date = "2011-09-01T13:22:00Z"
lastmod = "2012-05-28T22:48:00Z"
weight = 7499
keywords = [ "rendering", "river", "mapnik", "highway", "width" ]
aliases = [ "/questions/7499" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Street (rivers...) width rendering](/questions/7499/street-rivers-width-rendering)

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
<span id="post-7499-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7499-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-7499-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>After reading <a href="http://help.openstreetmap.org/users/87/pieren">Pieren</a>'s comment to <a href="http://help.openstreetmap.org/questions/7486/narrow-streets-in-old-cities/7487">this</a> <a href="http://help.openstreetmap.org/users/131/gnonthgol">Gnonthgol</a>'s answer and after having no response (not even negative one) to <a href="http://trac.openstreetmap.org/ticket/3984">this</a> enhancement ticket for Mapnik I started to wonder:<br />
</p>
<p><strong>What is the big obstacle that prevents rendering of real width for higher zoom levels?</strong><br />
</p>
<p>I do not believe it is technically impossible, since different types of roads get rendered in different widths.<br />
Somewhere someone mentioned that road importance is the key for rendered width. This is a good option for lower zoom levels and for roads where the information is not present. Still more important roads (motorways) tend to be much wider and have more lanes than minor roads, so the relation of more important road being rendered more prominently is still there.<br />
</p>
<p>Even more so for waterways. Unlike for roads there are only two types based on size (river + stream). What else makes a river more important than its size/width? And having a uniform width tag for all linear objects is certainly much more consistent than developing tag array like small stream/stram/big stream/small river/river/big river/huge river (that partially happened for roads.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-river" rel="tag" title="see questions tagged &#39;river&#39;">river</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-highway" rel="tag" title="see questions tagged &#39;highway&#39;">highway</span> <span class="post-tag tag-link-width" rel="tag" title="see questions tagged &#39;width&#39;">width</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Sep '11, 13:22</strong></p>
<img src="https://secure.gravatar.com/avatar/15c1efc9ebb466f69907a3e85693e739?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LM_1&#39;s gravatar image" />
<p><span>LM_1</span><br />
<span class="score" title="3287 reputation points"><span>3.3k</span></span><span title="33 badges"><span class="badge1">●</span><span class="badgecount">33</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LM_1 has 7 accepted answers">10%</span> </br></br></p>
</div>
</div>
<div id="comments-container-7499" class="comments-container">
<span id="7516"></span>
<div id="comment-7516" class="comment">
<div id="post-7516-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>Seriously, if you want to discuss this then take it to the mailing lists. But in short, it's a map, not fake-aerial-imagery, so it's to be expected that things aren't always drawn to accurate scale.</p>
</div>
<div id="comment-7516-info" class="comment-info">
<span class="comment-age">(01 Sep '11, 18:31)</span> <span class="comment-user userinfo">Andy Allan</span>
</div>
</div>
<span id="7522"></span>
<div id="comment-7522" class="comment">
<div id="post-7522-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>And I always thought that reality depicted as objects in an accurate positinon and scale are a map.</p>
</div>
<div id="comment-7522-info" class="comment-info">
<span class="comment-age">(01 Sep '11, 22:36)</span> <span class="comment-user userinfo">LM_1</span>
</div>
</div>
</div>
<div id="comment-tools-7499" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7499-form-container" class="comment-form-container">
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

<span id="7504"></span>

<div id="answer-container-7504" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7504-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7504-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-7504-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The best solution for rivers is to draw the riverbank and tag it with <a href="http://wiki.openstreetmap.org/wiki/Tag:waterway%3Driverbank">waterway=riverbank</a>. As I said in another question, the "width" tag solution works only if you put the tag everywhere along your feature (a road or a river). When the tag is not present, you can only estimate a default width which is very difficult because it is very cultural and country specific (the default width for a residential road is different between USA and Europe. Same for a default river width between Sudan and Switzerland). About rendering, the result might not be what you are expecting. Perhaps the segments with the tag "width" will be correct but the vast majority of the other segments will be incorrect. The resulting maps might be worst than not supporting the tag.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Sep '11, 13:36</strong></p>
<img src="https://secure.gravatar.com/avatar/0e92f2d89853fd4e04c4b40a921e519b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pieren&#39;s gravatar image" />
<p><span>Pieren</span><br />
<span class="score" title="9847 reputation points"><span>9.8k</span></span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="157 badges"><span class="bronze">●</span><span class="badgecount">157</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pieren has 34 accepted answers">15%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Sep '11, 13:39</strong> </span></p>
</div>
</div>
<div id="comments-container-7504" class="comments-container">
<span id="7507"></span>
<div id="comment-7507" class="comment">
<div id="post-7507-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Riverbanks on uniformly wide rivers seem to me like a lot of duplicate data (in result three almost identical, slightly shifted parallel ways).<br />
Within towns/cities there are good reasons to draw rivers with riverbanks because they are more often artificial and have more complicated shapes.<br />
I believe that after renderer's support the width data would quickly be added.<br />
</p>
<p>For roads there is (despite some proposals) no way of tagging it. And the situation would be similar to rivers' - it is imaginable to create some "streetbanks" within towns, but otherwise width makes more sense.</p>
</div>
<div id="comment-7507-info" class="comment-info">
<span class="comment-age">(01 Sep '11, 13:47)</span> <span class="comment-user userinfo">LM_1</span>
</div>
</div>
<span id="12992"></span>
<div id="comment-12992" class="comment">
<div id="post-12992-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You're wrong within town/cities ! Riverbanks within cities are much more regular than in rural areas where these rivers vary considerably (mostly because they have lateral areas left that can be flooded). Look at a really natural river, even if it has been channelized, and you'll see large variations and irregularities of their banks, depending on the natural fields, type of soils, altitude. Rivers in cities are channelized so their banks are more regular, even if there are details such as harbour equipments &amp; local adjustments around bridges, to help stabilize them on their feet.</p>
</div>
<div id="comment-12992-info" class="comment-info">
<span class="comment-age">(28 May '12, 07:12)</span> <span class="comment-user userinfo">Verdy_p</span>
</div>
</div>
<span id="13041"></span>
<div id="comment-13041" class="comment">
<div id="post-13041-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sure that natural rivers are not regular, but generally in urbanized areas the map is much more detailed and smaller width differences are important. Even so it is better to know that a river is generally 20 m wide (and maybe wider in some areas) than not having any visual representation of its width. It would be perfect if everything could be mapped as area, but it is not - some things are simplified...</p>
</div>
<div id="comment-13041-info" class="comment-info">
<span class="comment-age">(28 May '12, 22:48)</span> <span class="comment-user userinfo">LM_1</span>
</div>
</div>
</div>
<div id="comment-tools-7504" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7504-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="7537"></span>

<div id="answer-container-7537" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7537-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7537-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-7537-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It is generally admitted that a map is not an imagery, so that all widths are not proportional. But this is highly related to the current zoom level:</p>
<ul>
<li>if we know the effective width of a path, and this width is already larger than the minimum display width to render it on the map, this width would override the default disaply width, so that it could be traced more exactly.</li>
<li>if there's no width specified, use a width assigned by default by the renderer for the type of path.</li>
<li>if the renderer minimum display width is larger than the specified width (or the default width for the type of path), then ignore the specified width or default width, just use the minimum display width to render the path (this will hide tiny details along the path, but it will create a usable map, where paths are consistantly visible all along).</li>
</ul>
<p>This logic can be applied to roads, railways, rivers, and even to boundary limits (that don't have a specified width, but only a default width according to the boundary type, or may be according to the boundary effective surface (in square meters).</p>
<p>But for relaly large ways, whose width is not consistant along their way (notably rivers whose width are growing in a nearly monotonic way), specifying only widths would create inconsistant results. Gernally roads and railways have a very standard metric (which only varies when parallel lanes are added/removed along the way), but this is not the case of rivers that have much more variations (this would mean splitting the river into many more sections, each one with its own local width, plus a linear interpolation between points for this width).</p>
<p>For this reason it just seems simpler, for large enough rivers, to draw rivers not just with a single central path, but with its limiting banks, that are easier to geolocalize exactly on the map. In this case, choosing a representation of rivers by their boundaries (banks) is more consistant than using widths, at least for large rivers. A mapper can then autodetect these cases, and compute the widths itself, to determine if details of banks are accurate to represent the river, substituting the bounding banks by an auto-computed "skeleton" path that will be rendered by a minimum display width (larger than the effective width represented by the banks.</p>
<p>For now, such approach is not supported by renderers, so rivers have to be drawn twice, when their banks are detailed: you draw the bounding banks, as well as a virtual central path, which should be tagged correctly with a consistant width (or whose default width will be derived from the type of path). Which one of these two specifications of the same object should be chosen by the renderer, but I think that their task will be easier if both representations are grouped in a relation representing the whole river as a single object.</p>
<p>Note: nothing forbids using the same approach for streets, especially narrow streets in old cities, but these streets (generally not open to automotive traffic, but I won't bet it's always the case, there are certainly lots of exceptions, and such condition is then not determinant) could be assigned distinct types, without requiring to specify their effective widths (when they are consistantly narrower than the default widths of other streets of the same type). This is in fact the same kind of distinction between normal gauge railways, and narrow gauge railways.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Sep '11, 02:49</strong></p>
<img src="https://secure.gravatar.com/avatar/b0ac3d0a15ce4f96f0d6b29172fca72a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Verdy_p&#39;s gravatar image" />
<p><span>Verdy_p</span><br />
<span class="score" title="141 reputation points">141</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Verdy_p has no accepted answers">0%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Sep '11, 02:54</strong> </span></p>
</div>
</div>
<div id="comments-container-7537" class="comments-container">
&#10;</div>
<div id="comment-tools-7537" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7537-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="7518"></span>

<div id="answer-container-7518" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7518-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7518-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-7518-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you want a map showing the width of rivers or roads (or other types of ways), I suggest you try rendering one yourself.</p>
<p>This will demonstrate what it look like, and show that it is technically possible. And you could share the stylesheets, which would make it easier for anyone else to make such a map.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Sep '11, 20:05</strong></p>
<img src="https://secure.gravatar.com/avatar/aa505c046b1c010e997a7849c6f3dbbe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vclaw&#39;s gravatar image" />
<p><span>Vclaw</span><br />
<span class="score" title="9217 reputation points"><span>9.2k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="95 badges"><span class="silver">●</span><span class="badgecount">95</span></span><span title="141 badges"><span class="bronze">●</span><span class="badgecount">141</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vclaw has 41 accepted answers">22%</span> </br></p>
</div>
</div>
<div id="comments-container-7518" class="comments-container">
<span id="7519"></span>
<div id="comment-7519" class="comment">
<div id="post-7519-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>That is certainly possible. For someone like me (never attempted any rendering) it could be more than a job for one afternoon, but not impossible.<br />
</p>
<p>This question however is here to find out why it is not in place already.<br />
Technical difficulties?<br />
Processing power required?<br />
Uniform width rivers are considered better?<br />
Something else entirely?</p>
</div>
<div id="comment-7519-info" class="comment-info">
<span class="comment-age">(01 Sep '11, 21:51)</span> <span class="comment-user userinfo">LM_1</span>
</div>
</div>
</div>
<div id="comment-tools-7518" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7518-form-container" class="comment-form-container">
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


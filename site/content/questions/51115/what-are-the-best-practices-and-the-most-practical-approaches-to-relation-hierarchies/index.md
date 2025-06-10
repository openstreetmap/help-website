+++
type = "question"
title = "What are the best practices and the most practical approaches to relation hierarchies?"
description = '''I&#x27;m wanting to know about the best practices and the most practical approaches to relation hierarchies. And importantly if the ideal approach is different from the practical approach. Specifically, I&#x27;ve recently added a relation for the Haida Gwaii island group (edit). It is a major island group and...'''
date = "2016-07-26T20:44:00Z"
lastmod = "2017-12-27T19:48:00Z"
weight = 51115
keywords = [ "hierarchy", "islands", "relations", "super-relations", "bestpractice" ]
aliases = [ "/questions/51115" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [What are the best practices and the most practical approaches to relation hierarchies?](/questions/51115/what-are-the-best-practices-and-the-most-practical-approaches-to-relation-hierarchies)

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
<span id="post-51115-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51115-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-51115-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm wanting to know about the best practices and the most practical approaches to relation hierarchies. And importantly if the ideal approach is different from the practical approach.</p>
<p>Specifically, I've recently added a relation for the <a href="https://en.wikipedia.org/wiki/Haida_Gwaii">Haida Gwaii</a> island group (<a href="http://www.openstreetmap.org/changeset/41045130">edit</a>). It is a major island group and had not been labelled correctly. As many of the islands were already mapped as multipolygons, I added these mulitpolygons to the relation. Now when I look at <a href="http://www.openstreetmap.org/relation/6439518#map=7/53.199/-131.320">the relation</a> it only shows the islands mapped as a single way.</p>
<p>I'm not sure if this is a problem. Perhaps it's suboptimal, but at present the best solution.</p>
<p>My main goal in mapping this group of islands was to have it mapped in a meaningful way in the database, but it'd be nice if it would display in a meaningful way when searched for, and if a label was rendered.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-hierarchy" rel="tag" title="see questions tagged &#39;hierarchy&#39;">hierarchy</span> <span class="post-tag tag-link-islands" rel="tag" title="see questions tagged &#39;islands&#39;">islands</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span> <span class="post-tag tag-link-super-relations" rel="tag" title="see questions tagged &#39;super-relations&#39;">super-relations</span> <span class="post-tag tag-link-bestpractice" rel="tag" title="see questions tagged &#39;bestpractice&#39;">bestpractice</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Jul '16, 20:44</strong></p>
<img src="https://secure.gravatar.com/avatar/f88a467aa884aeb760041004f62448ee?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="keithonearth&#39;s gravatar image" />
<p><span>keithonearth</span><br />
<span class="score" title="2939 reputation points"><span>2.9k</span></span><span title="56 badges"><span class="badge1">●</span><span class="badgecount">56</span></span><span title="76 badges"><span class="silver">●</span><span class="badgecount">76</span></span><span title="108 badges"><span class="bronze">●</span><span class="badgecount">108</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="keithonearth has 3 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-51115" class="comments-container">
&#10;</div>
<div id="comment-tools-51115" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51115-form-container" class="comment-form-container">
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

<span id="51237"></span>

<div id="answer-container-51237" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-51237-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51237-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-51237-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Relations of <strong>type=multipolygon</strong> don't accept other relations as members, but <strong>only ways</strong> (closed or not), with roles outer and inner. Multipolygon relations don't accept nodes either. So including multipolygon relations as members of the Haida Gwaii archipelago is the reason for your problem.</p>
<p>There is actually an alternave to the type=multipolygon, that is the <strong>type=cluster</strong>, that would accept as members a) single ways (for simple islands), 2) multipolygon relations for complex islands, like Graham island, and even c) islands mapped as nodes. No roles for any of them. But <strong>type=cluster is only a draft!</strong>.</p>
<p>To map the whole Haida Gwaii archipelago as type=multipolygon relation, you have to download all the natural=coastline ways of the archipelago (3,843 ways), download the relation and open it, delete all members, then select all those 3,843 ways, add them to the relation as outer and upload.</p>
<p><strong>Procedure with JOSM</strong>:</p>
<p>To download all the coastline ways, you better use <strong>overpass with JOSM (Shift + Alt + UpArrow)</strong>:</p>
<p><img src="http://help.openstreetmap.org/upfiles/overpass_YCDQ4mq.png" alt="downloading coastlines with overpass" /></p>
<p>Next, you <strong>download the relation</strong>. For that, you first <strong>get its id</strong>:</p>
<p><img src="http://help.openstreetmap.org/upfiles/idRelation.png" alt="relation id" /></p>
<p>We see that it is <em>6439518</em>. Now we download the relation with <strong>Download object... (Ctrl + Shift + O)</strong> (we only download the relation members and not in a separate layer):</p>
<p><img src="http://help.openstreetmap.org/upfiles/downloadRelation_oBfBexG.png" alt="download relation" /></p>
<p>Now, we open the relation, <strong>select all its current members</strong> and we <strong>delete them</strong>:</p>
<p><img src="http://help.openstreetmap.org/upfiles/deleteAllCurrentMembers_owPl6W0.png" alt="delete all current relation members" /></p>
<p>Now, we set two filters, <strong>natural="coastline"</strong> and <strong>type:node</strong> as follows:</p>
<p><img src="http://help.openstreetmap.org/upfiles/filtersActive.png" alt="filters" /></p>
<p>And <strong>select all coastline ways</strong>:</p>
<p><img src="http://help.openstreetmap.org/upfiles/selectAllCoastlineWays.png" alt="select all coastline ways" /></p>
<p>You <strong>add them to the Haida Gwaii</strong> archipelago multipolygon relation, with role <strong>outer</strong>:</p>
<p><img src="http://help.openstreetmap.org/upfiles/addCoastlineWaysToRelation.png" alt="add all coastlines to relation as outer" /></p>
<p>And now you are ready to <strong>upload the modified relation to OSM</strong>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Aug '16, 00:51</strong></p>
<img src="https://secure.gravatar.com/avatar/d45c161edd4b471fd947a7ec574274ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="edvac&#39;s gravatar image" />
<p><span>edvac</span><br />
<span class="score" title="665 reputation points">665</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="edvac has 4 accepted answers">15%</span></p>
</img>
</div>
</div>
<div id="comments-container-51237" class="comments-container">
<span id="51252"></span>
<div id="comment-51252" class="comment">
<div id="post-51252-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thank you edvac, for your amazingly thorough answer. I've followed your suggestion, and updated the relation for Haida Gwaii. More than just teaching me an efficient way to do this one task your post has taught me lots of good JOSM tricks. (I'd never used the filter before, for example. Thanks!</p>
</div>
<div id="comment-51252-info" class="comment-info">
<span class="comment-age">(05 Aug '16, 03:24)</span> <span class="comment-user userinfo">keithonearth</span>
</div>
</div>
<span id="61388"></span>
<div id="comment-61388" class="comment">
<div id="post-61388-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You are welcome :)</p>
</div>
<div id="comment-61388-info" class="comment-info">
<span class="comment-age">(27 Dec '17, 19:48)</span> <span class="comment-user userinfo">edvac</span>
</div>
</div>
</div>
<div id="comment-tools-51237" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51237-form-container" class="comment-form-container">
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


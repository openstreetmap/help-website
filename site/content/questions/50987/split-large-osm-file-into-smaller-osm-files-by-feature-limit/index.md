+++
type = "question"
title = "Split large OSM file into smaller OSM files by feature limit"
description = '''I have a very large 2GB osm file that I need to split up into &amp;lt;=50K feature chunks.  I have attempted to use splitter, which is a great tool. you can set the # of nodes within each split file. Splitter then creates x amount of polygons to ensure there are no more then the requested # of nodes wit...'''
date = "2016-07-19T16:50:00Z"
lastmod = "2016-07-20T21:24:00Z"
weight = 50987
keywords = [ "changesets", "osm", "split" ]
aliases = [ "/questions/50987" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Split large OSM file into smaller OSM files by feature limit](/questions/50987/split-large-osm-file-into-smaller-osm-files-by-feature-limit)

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
<span id="post-50987-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50987-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-50987-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a very large 2GB osm file that I need to split up into &lt;=50K feature chunks.</p>
<p>I have attempted to use <a href="http://www.mkgmap.org.uk/doc/splitter.html">splitter</a>, which is a great tool. you can set the # of nodes within each split file. Splitter then creates x amount of polygons to ensure there are no more then the requested # of nodes within each split file. The problem is splitter duplicates ways across overlapping changesets so that it does not cut them at intersection points. I am trying to find a solution that simply splits the osm file up without worrying about location of features.</p>
<p>Is there a tool to simply split an osm file based on # of features that ignores the location of features.</p>
<p>Any insight is welcome.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-changesets" rel="tag" title="see questions tagged &#39;changesets&#39;">changesets</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-split" rel="tag" title="see questions tagged &#39;split&#39;">split</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Jul '16, 16:50</strong></p>
<img src="https://secure.gravatar.com/avatar/943c484e8c04680902357de8f080dcc0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Cellington&#39;s gravatar image" />
<p><span>Cellington</span><br />
<span class="score" title="216 reputation points">216</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Cellington has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Jul '16, 18:20</strong> </span></p>
</div>
</div>
<div id="comments-container-50987" class="comments-container">
<span id="50989"></span>
<div id="comment-50989" class="comment">
<div id="post-50989-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I've linked to mkgmap's tile splitter - I presume that's what you meant.</p>
<p>Unfortunately I don't know an answer (and have no idea what you'd do with relations).</p>
</div>
<div id="comment-50989-info" class="comment-info">
<span class="comment-age">(19 Jul '16, 17:57)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="50990"></span>
<div id="comment-50990" class="comment">
<div id="post-50990-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, I was talking about mkgmap's splitter.jar tool. I hadn't thought of relations.</p>
</div>
<div id="comment-50990-info" class="comment-info">
<span class="comment-age">(19 Jul '16, 18:26)</span> <span class="comment-user userinfo">Cellington</span>
</div>
</div>
</div>
<div id="comment-tools-50987" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50987-form-container" class="comment-form-container">
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

<span id="50994"></span>

<div id="answer-container-50994" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-50994-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50994-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-50994-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Generally it doesn't make much sense to split up OSM files into chunks without taking geometry into account, because you would end up with lots of ways and relations without the nodes and members they are referring to. About the only thing I can think of where this would make sense is when you are trying to transport the data over some "link" that doesn't support large files, but you will re-assemble the file on the other end before using it as a whole again. For instance if you only have a small USB stick or so. But then you can just use any normal file splitting program that can work with binary data, on Linux you can use 'split' for this.</p>
<p>Using splitter seems to be the right approach here, maybe you can cut the ways after using splitter somehow? Osmosis can cut ways, but you'd have to figure out the bounding box of each splitter output file in some way. Maybe it would be easier to write a small script that calls osmosis with different parameters splitting into a reglar grid? The same could be accomplished using the <a href="https://github.com/joto/osm-history-splitter">OSM history splitter</a>. Maybe you can tell us <strong>why</strong> you want to do the splitting in the way you describe and we have a better way to help you.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Jul '16, 07:13</strong></p>
<img src="https://secure.gravatar.com/avatar/2d4dfcdcde73aa5e2ffa4a9b3a7cb51d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jochen%20Topf&#39;s gravatar image" />
<p><span>Jochen Topf</span><br />
<span class="score" title="5244 reputation points"><span>5.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jochen Topf has 32 accepted answers">31%</span></p>
</div>
</div>
<div id="comments-container-50994" class="comments-container">
<span id="51002"></span>
<div id="comment-51002" class="comment">
<div id="post-51002-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>So my ultimate goal is to get a 2gb osm file into my personal API db. This file contains nearly 7 million total features (nodes, ways, relations). The proper way to get this into my OSM server is through the use of Osmosis using the upload change command (I also use osmosis to convert this file into a create changeset)</p>
<p>I use negative ids in my osm file so that when running the upload command, the data gets pushed into my database with the correct ids.</p>
<p>The osmosis upload command is limited to 50K features per changeset. This is why I am trying to split apart my file into many smaller files.</p>
<p>Ideally I would like to create a script that would parse through the large xml file and write multiple small xmls up to a max feature count while retaining the proper relationships between nodes, ways and relations.</p>
</div>
<div id="comment-51002-info" class="comment-info">
<span class="comment-age">(20 Jul '16, 19:09)</span> <span class="comment-user userinfo">Cellington</span>
</div>
</div>
<span id="51004"></span>
<div id="comment-51004" class="comment">
<div id="post-51004-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Have a look at <a href="https://wiki.openstreetmap.org/wiki/Import/Software">https://wiki.openstreetmap.org/wiki/Import/Software</a> . There are multiple programs there that might help you.</p>
</div>
<div id="comment-51004-info" class="comment-info">
<span class="comment-age">(20 Jul '16, 21:24)</span> <span class="comment-user userinfo">Jochen Topf</span>
</div>
</div>
</div>
<div id="comment-tools-50994" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50994-form-container" class="comment-form-container">
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


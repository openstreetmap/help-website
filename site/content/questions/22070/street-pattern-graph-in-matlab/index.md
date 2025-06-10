+++
type = "question"
title = "Street pattern graph in Matlab"
description = '''Dear all, I am looking for the following. I need to have a graph based representation of a city in Matlab. Preferably I would like to decide myself where exactly in the world. Therefore, I would imagine I would need the following: long. and latitude of nodes (points) that have a street in between (s...'''
date = "2013-05-03T10:04:00Z"
lastmod = "2013-05-03T14:33:00Z"
weight = 22070
keywords = [ "graph", "streets", "matlab", "city" ]
aliases = [ "/questions/22070" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Street pattern graph in Matlab](/questions/22070/street-pattern-graph-in-matlab)

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
<span id="post-22070-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22070-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-22070-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Dear all,</p>
<p>I am looking for the following. I need to have a graph based representation of a city in Matlab. Preferably I would like to decide myself where exactly in the world. Therefore, I would imagine I would need the following: long. and latitude of nodes (points) that have a street in between (so where there is an edge present). In this way I can create a graph. Preferably I would also like to know the type of the street for each edge (main street, small street, etc.), but this is not strictly necessary. If I get it into a text file, I will be able to load it into Matlab. But I have no idea how to obtain this data from this website.</p>
<p>I am completely new to this kind of street data and all the associated file types. Can someone help me with this? If something is is not clear about what I need please let me know.</p>
<p>Kind regards.</p>
<p>Roland</p>
<p>I would really appreciate your help!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-graph" rel="tag" title="see questions tagged &#39;graph&#39;">graph</span> <span class="post-tag tag-link-streets" rel="tag" title="see questions tagged &#39;streets&#39;">streets</span> <span class="post-tag tag-link-matlab" rel="tag" title="see questions tagged &#39;matlab&#39;">matlab</span> <span class="post-tag tag-link-city" rel="tag" title="see questions tagged &#39;city&#39;">city</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 May '13, 10:04</strong></p>
<img src="https://secure.gravatar.com/avatar/9676e0d862b1ee6391d0afb9fad17f00?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland_d&#39;s gravatar image" />
<p><span>Roland_d</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland_d has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-22070" class="comments-container">
<span id="22072"></span>
<div id="comment-22072" class="comment">
<div id="post-22072-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>People have tried turning OSM data into a (mathematical) graph before - <a href="https://help.openstreetmap.org/search/?q=graph&amp;Submit=Search&amp;t=question">search this help site for "graph"</a> and you'll get some helpful answers. Also, if you've not already read it, have a read of <a href="http://wiki.openstreetmap.org/wiki/Beginners_Guide_1.3">this page of the "Beginners' Guide"</a> that explains what sort of data (in the sense of "what's in the XML file that you download")</p>
</div>
<div id="comment-22072-info" class="comment-info">
<span class="comment-age">(03 May '13, 12:08)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="22078"></span>
<div id="comment-22078" class="comment">
<div id="post-22078-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That guide that you refer to seems to be only about editing the map. Where can i find how to choose which data to export and what not?</p>
</div>
<div id="comment-22078-info" class="comment-info">
<span class="comment-age">(03 May '13, 14:23)</span> <span class="comment-user userinfo">Roland_d</span>
</div>
</div>
<span id="22079"></span>
<div id="comment-22079" class="comment">
<div id="post-22079-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>There are multiple possibilities. You can use <a href="http://wiki.openstreetmap.org/wiki/Osmfilter">osmfilter</a> after you obtained the data or you can use some API that supports filtering like the <a href="http://wiki.openstreetmap.org/wiki/Overpass_API">Overpass API</a> (also take a look at <a href="http://overpass-turbo.eu/">Overpass Turbo</a>). Or you skip the uninteresting parts while parsing a data export.</p>
</div>
<div id="comment-22079-info" class="comment-info">
<span class="comment-age">(03 May '13, 14:32)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="22080"></span>
<div id="comment-22080" class="comment">
<div id="post-22080-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>osmfilter, osmconvert, overpass, XAPI, Geofabrik downloads, osmosis, imposm ..... Search the wiki.</p>
</div>
<div id="comment-22080-info" class="comment-info">
<span class="comment-age">(03 May '13, 14:33)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-22070" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22070-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>


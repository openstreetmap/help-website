+++
type = "question"
title = "what exactly street id is??"
description = '''hello, i am kumar completely new to open street map database, i am working with data bases as of my first task is i need to create a node table which includes node id, lat and long values , so i did this step.... and now i want create a new table with information of street id and node id. here my qu...'''
date = "2015-10-01T14:33:00Z"
lastmod = "2015-10-01T20:59:00Z"
weight = 45683
keywords = [ "nodes", "street", "postgresql", "id", "postgis" ]
aliases = [ "/questions/45683" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [what exactly street id is??](/questions/45683/what-exactly-street-id-is)

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
<span id="post-45683-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45683-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-45683-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>hello, i am kumar completely new to open street map database, i am working with data bases as of my first task is i need to create a node table which includes node id, lat and long values , so i did this step.... and now i want create a new table with information of street id and node id.</p>
<p>here my question is what is street id?? can any one help me please</p>
<p>best regards</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-street" rel="tag" title="see questions tagged &#39;street&#39;">street</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-id" rel="tag" title="see questions tagged &#39;id&#39;">id</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Oct '15, 14:33</strong></p>
<img src="https://secure.gravatar.com/avatar/b51f82218d5511a6cb08225ee3015f57?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kumar45&#39;s gravatar image" />
<p><span>kumar45</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kumar45 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Oct '15, 18:35</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-45683" class="comments-container">
&#10;</div>
<div id="comment-tools-45683" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45683-form-container" class="comment-form-container">
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

<span id="45684"></span>

<div id="answer-container-45684" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-45684-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45684-score" class="post-score" title="current number of votes">
8
</div>
<span id="post-45684-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>We do not have street IDs, we have way IDs. A way can represent a part of a street, a whole street, or another linear or polygonal feature, and consists of a sequence of nodes that describe the geometry as well of a set of tags that describe its properties.</p>
<p>Even though OSM data can be represented in many formats, the Wiki page on <a href="https://wiki.openstreetmap.org/wiki/OSM_XML">OSM XML</a> should give you a good idea of how data is organised in OSM.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Oct '15, 15:00</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-45684" class="comments-container">
&#10;</div>
<div id="comment-tools-45684" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45684-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="45689"></span>

<div id="answer-container-45689" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-45689-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45689-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-45689-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The other answer is perfect.</p>
<p>On a topic I mistook it for when first read the title. At least few {so far} streets carry a NPLG:USRN tags which are street referance numbers used in the UK based on the National Property and Land Gazetter system. Although not common to the public they are used with streetworks applications and permits like digging to lay pipes and cables. Some sites realsed details of these to the public so some were annotated to streets on OSM were applicable. Similar things are happening for UPRN in addressing at a few places too. UPRN being for properties from flats to factory sites can somtiemes been seen on labels like on bins when your surveying. UARN's I don't think have been added to OSM yet [Universal Address Referance Number]. Some OSM data users compile address lists so these come in useful.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Oct '15, 20:59</strong></p>
<img src="https://secure.gravatar.com/avatar/30d90feb3a40fa6255767f95a8cd7943?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Govanus&#39;s gravatar image" />
<p><span>Govanus</span><br />
<span class="score" title="154 reputation points">154</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Govanus has one accepted answer">3%</span></p>
</div>
</div>
<div id="comments-container-45689" class="comments-container">
&#10;</div>
<div id="comment-tools-45689" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45689-form-container" class="comment-form-container">
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


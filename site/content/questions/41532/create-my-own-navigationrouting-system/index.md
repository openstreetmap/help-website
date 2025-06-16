+++
type = "question"
title = "Create my own navigation/routing system"
description = '''I&#x27;m studding AI course and I need to create a routing or navigation program. I live in Barcelona and first at all I need Barcelona&#x27;s street network data. I have found it here https://mapzen.com/metro-extracts/ (but I don&#x27;t know it this data is good enough to use it in a navigation system). Here, htt...'''
date = "2015-03-06T08:16:00Z"
lastmod = "2015-03-06T11:34:00Z"
weight = 41532
keywords = [ "navigation", "routing" ]
aliases = [ "/questions/41532" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Create my own navigation/routing system](/questions/41532/create-my-own-navigationrouting-system)

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
<span id="post-41532-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41532-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-41532-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm studding AI course and I need to create a routing or navigation program.</p>
<p>I live in Barcelona and first at all I need Barcelona's street network data. I have found it here <a href="https://mapzen.com/metro-extracts/">https://mapzen.com/metro-extracts/</a> (but I don't know it this data is good enough to use it in a navigation system).</p>
<p>Here, <a href="https://wiki.openstreetmap.org/wiki/Routing">https://wiki.openstreetmap.org/wiki/Routing</a>, I have found more information about routing but I'm terrible lost.</p>
<p>Where do you recommend me to start with this?</p>
<p>I have to implement my own version of A* algorithm. I only need data, but reading the previous page I see that Openstreet data has information about speed, highway type, etc.</p>
<p>I'm sorry, but I'm lost and I don't know where to start with.</p>
<p>Any advice?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-navigation" rel="tag" title="see questions tagged &#39;navigation&#39;">navigation</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Mar '15, 08:16</strong></p>
<img src="https://secure.gravatar.com/avatar/d2bbca1934066bc468617d36b14ccf92?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="VansFannel&#39;s gravatar image" />
<p><span>VansFannel</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="VansFannel has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Mar '15, 08:52</strong> </span></p>
</div>
</div>
<div id="comments-container-41532" class="comments-container">
<span id="41535"></span>
<div id="comment-41535" class="comment">
<div id="post-41535-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>There have already been various similar questions, for example <a href="/questions/19213/how-can-i-convert-an-osm-xml-file-into-a-graph-representation">How can I convert an OSM XML file into a graph representation?</a>.</p>
</div>
<div id="comment-41535-info" class="comment-info">
<span class="comment-age">(06 Mar '15, 10:26)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-41532" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41532-form-container" class="comment-form-container">
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

<span id="41538"></span>

<div id="answer-container-41538" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-41538-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41538-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-41538-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes, it looks like you're onto the right idea. You can use an extract like that to route. It should have good information for you to route on (roads, footpaths, etc.). Read up about the <a href="https://wiki.openstreetmap.org/wiki/Elements">OpenStreetMap data model</a> and learn how ways are made up of nodes. When 2 roads join (e.g. at a junction), they should share a node. You will need the PBF or XML file from Mapzen. The XML format might be easier for you to work with (read up about the <a href="https://wiki.openstreetmap.org/wiki/OSM_XML">XML Schema</a>). You can parse XML in any language. I <a href="https://github.com/rory/openstreetmap-publess-walk">wrote a programme to route across Dublin without passing a pub</a>, it parses the XML directly and does simple routing on that. It's open source.</p>
<p>re: speed limits. They are optional for your routing algorithm. You can use them or not use them. It depends on what you want your router to be aware of.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Mar '15, 11:34</strong></p>
<img src="https://secure.gravatar.com/avatar/16e12e337f6edc3750681492656097ed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rorym&#39;s gravatar image" />
<p><span>rorym</span><br />
<span class="score" title="5358 reputation points"><span>5.4k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="49 badges"><span class="silver">●</span><span class="badgecount">49</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rorym has 18 accepted answers">11%</span></p>
</div>
</div>
<div id="comments-container-41538" class="comments-container">
&#10;</div>
<div id="comment-tools-41538" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41538-form-container" class="comment-form-container">
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


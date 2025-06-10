+++
type = "question"
title = "How do I create polygons from OSM data?"
description = '''Hi, I just discovered OSM files, and I think it awesome ! I am a cg artist. I use a software called Houdini, in which I would like to import osm data.  I have a python script doing excatly that. I read osm datas fine. But the problem is : I can&#x27;t really make sens of all the different nodes in the fi...'''
date = "2013-06-24T23:38:00Z"
lastmod = "2016-01-04T06:23:00Z"
weight = 23650
keywords = [ "xml", "polygon", ".osm" ]
aliases = [ "/questions/23650" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How do I create polygons from OSM data?](/questions/23650/how-do-i-create-polygons-from-osm-data)

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
<span id="post-23650-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23650-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-23650-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I just discovered OSM files, and I think it awesome ! I am a cg artist. I use a software called Houdini, in which I would like to import osm data.</p>
<p>I have a python script doing excatly that. I read osm datas fine. But the problem is : I can't really make sens of all the different nodes in the file. The only paramters that make sense to me are the one containing some coordinates. I have been able to loop through them, creating a point each time. And I can se a result. All the points start to draw the shape of some streets.</p>
<p>So I am getting the data, no problem about that I think.</p>
<p>My question is : How are these points related to each other ? How can I make sense of them enough to be able to connect them ? My final goal is just to able to connect these points to represent streets and roads,but not necesserally in a very realistic way. I mean, all I really need is an order in which to connect points, and some infos about which point belongs to which way or road.</p>
<p>I hope I am being clear ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-xml" rel="tag" title="see questions tagged &#39;xml&#39;">xml</span> <span class="post-tag tag-link-polygon" rel="tag" title="see questions tagged &#39;polygon&#39;">polygon</span> <span class="post-tag tag-link-.osm" rel="tag" title="see questions tagged &#39;.osm&#39;">.osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Jun '13, 23:38</strong></p>
<img src="https://secure.gravatar.com/avatar/3970741e438713c730ec8e33fadb3199?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gui2one&#39;s gravatar image" />
<p><span>gui2one</span><br />
<span class="score" title="56 reputation points">56</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gui2one has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Jun '13, 00:56</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-23650" class="comments-container">
&#10;</div>
<div id="comment-tools-23650" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23650-form-container" class="comment-form-container">
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

<span id="23651"></span>

<div id="answer-container-23651" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-23651-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23651-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-23651-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think I've got it, I didn't seen the &lt;way/&gt; nodes with &lt;nd ref="something ..."/&gt; "ref" attribute corresponding to the id of the points I managed to loop through ... I must not be far from my goal ^^</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Jun '13, 00:40</strong></p>
<img src="https://secure.gravatar.com/avatar/3970741e438713c730ec8e33fadb3199?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gui2one&#39;s gravatar image" />
<p><span>gui2one</span><br />
<span class="score" title="56 reputation points">56</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gui2one has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-23651" class="comments-container">
&#10;</div>
<div id="comment-tools-23651" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23651-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="23652"></span>

<div id="answer-container-23652" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-23652-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23652-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-23652-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><span>Docu for .osm files</span> might help you. <a href="/questions/11693/osm-xml-polygon-code-example/11698">Frederik's answer over there</a> too.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Jun '13, 00:54</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-23652" class="comments-container">
<span id="23653"></span>
<div id="comment-23653" class="comment">
<div id="post-23653-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you, I get that part now ^^ . The rest of the job is python and me I guess. I have to write some nice lines of code to process this data. And there's potentialy A LOT of data ^^</p>
<p>I'll try to comment on my progress ^^ thanks for your help</p>
<p>G</p>
</div>
<div id="comment-23653-info" class="comment-info">
<span class="comment-age">(25 Jun '13, 02:26)</span> <span class="comment-user userinfo">gui2one</span>
</div>
</div>
<span id="23655"></span>
<div id="comment-23655" class="comment">
<div id="post-23655-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Okay, fine! I think you could write an entry about your progress with OSM-derived artwork in <a href="http://www.openstreetmap.org/user/gui2one/diary">your user blog</a> if you want to. At least I would be interested.</p>
<p>By the way: <a href="http://www.openstreetmap.org/copyright">Please</a> don't forget to attribute OSM and mention the OSM license if you publish your works, so others know where you got that great, open, free geo data from. :-)</p>
</div>
<div id="comment-23655-info" class="comment-info">
<span class="comment-age">(25 Jun '13, 03:14)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="23657"></span>
<div id="comment-23657" class="comment">
<div id="post-23657-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>hello, well I tried to post an entry in my blog. But the formatting is awfull. I posted my ptyhon code, and it's just unreadable. There seems to some formatting "commands". I am not familiar with that.</p>
</div>
<div id="comment-23657-info" class="comment-info">
<span class="comment-age">(25 Jun '13, 04:15)</span> <span class="comment-user userinfo">gui2one</span>
</div>
</div>
<span id="23660"></span>
<div id="comment-23660" class="comment">
<div id="post-23660-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>It's <a href="http://daringfireball.net/projects/markdown/syntax">Markdown</a>. It does take a bit of getting used to...</p>
</div>
<div id="comment-23660-info" class="comment-info">
<span class="comment-age">(25 Jun '13, 07:39)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-23652" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23652-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="47363"></span>

<div id="answer-container-47363" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47363-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47363-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-47363-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you r using osmosis to bring the data into a data base its quite easy coz osmosis create the line strings for the ways then u can simply use</p>
<blockquote>
<p>insert into polygons (select id,ST_MakePolygon(linestring) from ways where nodes[1]=nodes[array_upper(nodes,1)]);</p>
</blockquote>
<p>command to create polygons from them</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Jan '16, 06:23</strong></p>
<img src="https://secure.gravatar.com/avatar/e3a32bf261f93de288be2d64b6fef9e4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ballaji%20R&#39;s gravatar image" />
<p><span>Ballaji R</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ballaji R has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-47363" class="comments-container">
&#10;</div>
<div id="comment-tools-47363" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47363-form-container" class="comment-form-container">
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


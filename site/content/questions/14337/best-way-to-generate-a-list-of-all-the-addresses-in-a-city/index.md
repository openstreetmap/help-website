+++
type = "question"
title = "Best way to generate a list of all the addresses in a city?!"
description = '''I finally managed to import the data from an OSM file to a PostgreSQL database :). The problem is that, I think, I don&#x27;t really understand the database structure. Can someone, please, help me with a method to generate a list that will contain these informations:  1. Street name;  2. House number;  3...'''
date = "2012-07-17T12:18:00Z"
lastmod = "2012-07-18T17:15:00Z"
weight = 14337
keywords = [ "streetnames", "postgresql" ]
aliases = [ "/questions/14337" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Best way to generate a list of all the addresses in a city?!](/questions/14337/best-way-to-generate-a-list-of-all-the-addresses-in-a-city)

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
<span id="post-14337-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14337-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-14337-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I finally managed to import the data from an OSM file to a PostgreSQL database :).<br />
The problem is that, I think, I don't really understand the database structure.<br />
Can someone, please, help me with a method to generate a list that will contain these informations:<br />
1. Street name;<br />
2. House number;<br />
3. Lat;<br />
4. Long;<br />
Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-streetnames" rel="tag" title="see questions tagged &#39;streetnames&#39;">streetnames</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Jul '12, 12:18</strong></p>
<img src="https://secure.gravatar.com/avatar/aeb7b59188c6d4ab1846362547839eb3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alexandru&#39;s gravatar image" />
<p><span>Alexandru</span><br />
<span class="score" title="15 reputation points">15</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alexandru has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-14337" class="comments-container">
<span id="14338"></span>
<div id="comment-14338" class="comment">
<div id="post-14338-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What tool did you use to produce the PostgreSQL database?</p>
</div>
<div id="comment-14338-info" class="comment-info">
<span class="comment-age">(17 Jul '12, 12:22)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="14339"></span>
<div id="comment-14339" class="comment">
<div id="post-14339-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I used osm2pgsql</p>
</div>
<div id="comment-14339-info" class="comment-info">
<span class="comment-age">(17 Jul '12, 12:51)</span> <span class="comment-user userinfo">Alexandru</span>
</div>
</div>
<span id="14341"></span>
<div id="comment-14341" class="comment">
<div id="post-14341-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Alexandru: How do you define that all your OSM objects in your database really belong to the city you want?</p>
<p>Do you have a boundary polygon that you used to do a clipping with osmosis or similar?</p>
<p>Or is it enough to describe the elements you want to process via a boundingbox?</p>
</div>
<div id="comment-14341-info" class="comment-info">
<span class="comment-age">(17 Jul '12, 16:40)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
<span id="14342"></span>
<div id="comment-14342" class="comment">
<div id="post-14342-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I downloaded the OSM file only for a city from here: <a href="http://downloads.cloudmade.com/.">http://downloads.cloudmade.com/.</a> My question was about generating a list with some details, so please, let's focus on my question and stop answering me with other qwestions :)</p>
</div>
<div id="comment-14342-info" class="comment-info">
<span class="comment-age">(17 Jul '12, 18:36)</span> <span class="comment-user userinfo">Alexandru</span>
</div>
</div>
<span id="14355"></span>
<div id="comment-14355" class="comment">
<div id="post-14355-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>stephan75 asked the right question as currently you would get addresses not only for your city but also for surrounding area.</p>
</div>
<div id="comment-14355-info" class="comment-info">
<span class="comment-age">(18 Jul '12, 05:47)</span> <span class="comment-user userinfo">RM87</span>
</div>
</div>
<span id="14356"></span>
<div id="comment-14356" class="comment not_top_scorer">
<div id="post-14356-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ok, that would not be a problem :). So, anyone cand help me? :D</p>
</div>
<div id="comment-14356-info" class="comment-info">
<span class="comment-age">(18 Jul '12, 05:59)</span> <span class="comment-user userinfo">Alexandru</span>
</div>
</div>
</div>
<div id="comment-tools-14337" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-14337-form-container" class="comment-form-container">
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

<span id="14371"></span>

<div id="answer-container-14371" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-14371-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14371-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-14371-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Take the data as raw <em>.osm file or</em> .pbf file and try <a href="https://wiki.openstreetmap.org/wiki/Osmconvert">Osmconvert</a>.</p>
<p>There is recentry introduced option to export all elements with tag colums that you can define how you need it as CSV file (comma separated value.</p>
<p>try osmconvert --help on a command line and read more instructions in detail.</p>
<p>At least you should add columns for the tags "highway" and "name".</p>
<p>If you got your csv file like you need, you can load it in any spreadsheet program like libreoffice calc or similar. Sort the whole table for the column "name" and delete all doublettes.</p>
<p>Thus you get all road names of your area.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Jul '12, 17:15</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span> </br></br></p>
</div>
</div>
<div id="comments-container-14371" class="comments-container">
&#10;</div>
<div id="comment-tools-14371" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14371-form-container" class="comment-form-container">
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


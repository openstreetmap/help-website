+++
type = "question"
title = "How to exclude tables during importing full OSM into PostgreSQL"
description = '''Hi, I am using osm2pgsql to import full OSM into PostgreSQL and is there any way to exclude some tables during the importing? I just want to import the planet_osm_polygon table only and exclude the planet_osm_line , planet_osm_point and planet_osm_roads tables. Really appreciate any help.'''
date = "2017-08-28T04:20:00Z"
lastmod = "2017-08-28T09:51:00Z"
weight = 58841
keywords = [ "import", "osm", "postgresql" ]
aliases = [ "/questions/58841" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to exclude tables during importing full OSM into PostgreSQL](/questions/58841/how-to-exclude-tables-during-importing-full-osm-into-postgresql)

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
<span id="post-58841-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-58841-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-58841-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I am using osm2pgsql to import full OSM into PostgreSQL and is there any way to exclude some tables during the importing?</p>
<p>I just want to import the planet_osm_polygon table only and exclude the planet_osm_line , planet_osm_point and planet_osm_roads tables.</p>
<p>Really appreciate any help.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Aug '17, 04:20</strong></p>
<img src="https://secure.gravatar.com/avatar/95d580c60b9b016849766d2781c46af9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="xiaoweishen&#39;s gravatar image" />
<p><span>xiaoweishen</span><br />
<span class="score" title="66 reputation points">66</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="xiaoweishen has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-58841" class="comments-container">
&#10;</div>
<div id="comment-tools-58841" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-58841-form-container" class="comment-form-container">
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

<span id="58842"></span>

<div id="answer-container-58842" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-58842-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-58842-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-58842-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The _ways and _node tables are only used for "-slim" imports, if your machine has enough memory or you are only importing a small extract you can try the import without the -slim option.</p>
<p>Note a further way to save space is to use a normal file for node storage instead of the database table.</p>
<p><em>the above notes are not directly relevant for the specific question</em></p>
<p>Outside of the above you can simply edit the default.style file to control what gets imported and what not. There is no exact one to one relationship between OSM elements and tables in the osm2pgsql schema so asking to "exclude" tables doesn't make much sense. You can naturally simply drop any tables you don't want post import (assuming this is a one-off import)</p>
<p>See <a href="https://wiki.openstreetmap.org/wiki/Osm2pgsql">https://wiki.openstreetmap.org/wiki/Osm2pgsql</a> and <a href="https://github.com/openstreetmap/osm2pgsql/blob/master/README.md">https://github.com/openstreetmap/osm2pgsql/blob/master/README.md</a> for more information.</p>
<p>It should be noted that this help site is not intended as a way to find people that can google for you, but far more for questions with non-obvious answers that cannot be easily found simply by reading the documentation.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Aug '17, 08:55</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Aug '17, 10:33</strong> </span></p>
</div>
</div>
<div id="comments-container-58842" class="comments-container">
<span id="58843"></span>
<div id="comment-58843" class="comment">
<div id="post-58843-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi Simon, Thanks for your reply firstly. What you given are obvious notes for osm2pgsql and I certainly have read lot of this. What I want is just to try to find out how to exclude tables during importing, something like the options exclude... of Oracle import. BTW, you said the _line and _point are only used for "-slim" mode, I suggest you mean _nodes and _ways.</p>
<p>Anyway, there are four tables basicly will be imported by osm2pgsql, including planet_osm_line, planet_osm_point, planet_osm_polygon and planet_osm_roads, no matter what you are using "-slim" mode or not. I just want to import planet_osm_polygon only. You have no answers about my question.</p>
<p>Thanks.</p>
</div>
<div id="comment-58843-info" class="comment-info">
<span class="comment-age">(28 Aug '17, 09:09)</span> <span class="comment-user userinfo">xiaoweishen</span>
</div>
</div>
<span id="58844"></span>
<div id="comment-58844" class="comment">
<div id="post-58844-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I do not care aboud the disk and RAM size. Just want to import the specified table and ignore the others.</p>
</div>
<div id="comment-58844-info" class="comment-info">
<span class="comment-age">(28 Aug '17, 09:13)</span> <span class="comment-user userinfo">xiaoweishen</span>
</div>
</div>
<span id="58845"></span>
<div id="comment-58845" class="comment">
<div id="post-58845-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Edit the default.style to only include the objects you want (you won't be able to completely get rid of the other tables likely due to how some of the polygon building works).</p>
</div>
<div id="comment-58845-info" class="comment-info">
<span class="comment-age">(28 Aug '17, 09:51)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-58842" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-58842-form-container" class="comment-form-container">
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


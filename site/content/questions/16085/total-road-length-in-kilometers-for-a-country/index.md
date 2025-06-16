+++
type = "question"
title = "Total road length in Kilometers for a country"
description = '''Or in miles. How can you calculate the total road length for a country. Or a continent, or a city, etc etc I installed Qgis and learned to play a little with it.  There i can select to have all roads except track. Or a lot of nice stuff you can do, but one thing that i cannot figure it out in Qgis i...'''
date = "2012-09-14T14:33:00Z"
lastmod = "2022-05-23T21:29:00Z"
weight = 16085
keywords = [ "ways", "length", "statistics" ]
aliases = [ "/questions/16085" ]
osqa_answers = 6
osqa_accepted = false
+++

<div class="headNormal">

# [Total road length in Kilometers for a country](/questions/16085/total-road-length-in-kilometers-for-a-country)

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
<span id="post-16085-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16085-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-16085-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
2
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Or in miles. How can you calculate the total road length for a country. Or a continent, or a city, etc etc</p>
<p>I installed Qgis and learned to play a little with it.</p>
<p>There i can select to have all roads except track. Or a lot of nice stuff you can do, but one thing that i cannot figure it out in Qgis is to calculate the length of a road. Or calculate the lenght of all the roads.</p>
<p>So i can download once per week and do a query, so i can tell to people that this week we have added 200 km more or roads.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span> <span class="post-tag tag-link-length" rel="tag" title="see questions tagged &#39;length&#39;">length</span> <span class="post-tag tag-link-statistics" rel="tag" title="see questions tagged &#39;statistics&#39;">statistics</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Sep '12, 14:33</strong></p>
<img src="https://secure.gravatar.com/avatar/92a51d3af99ee124bb9e06dd35249910?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Badita%20Florin&#39;s gravatar image" />
<p><span>Badita Florin</span><br />
<span class="score" title="112 reputation points">112</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Badita Florin has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Sep '12, 14:57</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span></p>
</div>
</div>
<div id="comments-container-16085" class="comments-container">
&#10;</div>
<div id="comment-tools-16085" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16085-form-container" class="comment-form-container">
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

6 Answers:

</div>

</div>

<span id="16111"></span>

<div id="answer-container-16111" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-16111-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16111-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-16111-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>One option is to use this Perl script, which will calculate the length of roads in an OSM file: <a href="http://svn.openstreetmap.org/applications/utils/filter/osm-length/osm-length-2.pl">osm-length-2.pl</a> For more details, see this post by Frederik Ramm on the talk mailing list: <a href="http://lists.openstreetmap.org/pipermail/talk/2011-November/060656.html">[OSM-talk] Statistics on road network length?</a></p>
<p>Some of the other posts in that mailing list thread may be helpful.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Sep '12, 19:26</strong></p>
<img src="https://secure.gravatar.com/avatar/aa505c046b1c010e997a7849c6f3dbbe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vclaw&#39;s gravatar image" />
<p><span>Vclaw</span><br />
<span class="score" title="9217 reputation points"><span>9.2k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="95 badges"><span class="silver">●</span><span class="badgecount">95</span></span><span title="141 badges"><span class="bronze">●</span><span class="badgecount">141</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vclaw has 41 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-16111" class="comments-container">
<span id="16150"></span>
<div id="comment-16150" class="comment">
<div id="post-16150-score" class="comment-score">
-1
</div>
<div class="comment-text">
<p>osm-length-2.pl i cannot make it work and the other alternative, that i forgot right now what it was, the link it`s no more.</p>
</div>
<div id="comment-16150-info" class="comment-info">
<span class="comment-age">(16 Sep '12, 20:07)</span> <span class="comment-user userinfo">Badita Florin</span>
</div>
</div>
</div>
<div id="comment-tools-16111" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16111-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="38204"></span>

<div id="answer-container-38204" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-38204-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38204-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-38204-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Perhaps <a href="/questions/38203/if-i-want-to-calculate-total-way-length-is-this-query-a-good-way-to-do-it">this</a> question helps. I am currently waiting for someone to confirm that this is a good approach :)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Oct '14, 23:23</strong></p>
<img src="https://secure.gravatar.com/avatar/acea3c9fd5908d7ff09596d16b8724d8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mvexel&#39;s gravatar image" />
<p><span>mvexel</span><br />
<span class="score" title="762 reputation points">762</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mvexel has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-38204" class="comments-container">
&#10;</div>
<div id="comment-tools-38204" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38204-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="43630"></span>

<div id="answer-container-43630" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43630-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43630-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-43630-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For regular updates, Vclaw's answer is probably best. But I don't think what you were trying to do is difficult in qgis. Here's a <a href="http://www.qgistutorials.com/de/docs/calculating_line_lengths.html">tutorial</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Jun '15, 21:56</strong></p>
<img src="https://secure.gravatar.com/avatar/1df835d513b1282e0edd7405d29cd8d9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joost%20schouppe&#39;s gravatar image" />
<p><span>joost schouppe</span><br />
<span class="score" title="3427 reputation points"><span>3.4k</span></span><span title="24 badges"><span class="badge1">●</span><span class="badgecount">24</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="87 badges"><span class="bronze">●</span><span class="badgecount">87</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joost schouppe has 9 accepted answers">12%</span></p>
</div>
</div>
<div id="comments-container-43630" class="comments-container">
&#10;</div>
<div id="comment-tools-43630" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43630-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="74520"></span>

<div id="answer-container-74520" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74520-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74520-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74520-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is a python package that does exactly that.</p>
<p>It is basically a wrapper on top of Overpass that handles the calls.</p>
<p>It supports country-size regions :)</p>
<p><a href="https://github.com/JoaoCarabetta/osm-road-length">https://github.com/JoaoCarabetta/osm-road-length</a></p>
<p>It is super easy to use,</p>
<p>Install it: pip install osm-road-length</p>
<p>And run:</p>
<p>import osm_road_length from shapely import wkt</p>
<p>geometry = wkt.loads('POLYGON((-43.2958811591311 -22.853167273541693,-43.30961406928735 -23.035275736044728,-43.115980036084224 -23.02010939749927,-43.157178766552974 -22.832917893834313,-43.2958811591311 -22.853167273541693))')</p>
<p>length = osm_road_length.get(geometry)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Apr '20, 22:30</strong></p>
<img src="https://secure.gravatar.com/avatar/233392fffdef27e8db3a844cf613d74d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JOAO%20LUIZ&#39;s gravatar image" />
<p><span>JOAO LUIZ</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JOAO LUIZ has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-74520" class="comments-container">
&#10;</div>
<div id="comment-tools-74520" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74520-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="78369"></span>

<div id="answer-container-78369" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78369-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78369-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78369-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can use the free CartoType tool <a href="https://www.cartotype.com/developers/documentation/510-search-analyse-map">ctm1_info</a> on a CartoType map. Both ctm1_info and the <a href="https://www.cartotype.com/developers/documentation/50-how-to-create-map-files-for-cartotype-ctm1-files">makemap</a> tool to create CartoType maps are free for non-commercial use. For example, to get the total road length for Sweden:</p>
<pre><code>ctm1_info sweden.ctm1 -n -aroad/
ctm1_info built using CartoType 6.3.9557
&#10;Layer &#39;road/&#39; has 941,643 objects:
    line objects: 939,897; length = 482121.61 km
    polygon objects: 1746; area = 3.79 sq km</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Jan '21, 14:33</strong></p>
<img src="https://secure.gravatar.com/avatar/be8a91153ef95952a91929575d7ec8ef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Graham&#39;s gravatar image" />
<p><span>Graham</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Graham has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Jan '21, 14:34</strong> </span></p>
</div>
</div>
<div id="comments-container-78369" class="comments-container">
&#10;</div>
<div id="comment-tools-78369" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78369-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="84572"></span>

<div id="answer-container-84572" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-84572-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84572-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84572-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>With <a href="https://ohsome.org/apps/dashboard/">https://ohsome.org/apps/dashboard/</a> you can select your country, and then select highway=*, select ways, select length and click on results.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 May '22, 21:29</strong></p>
<img src="https://secure.gravatar.com/avatar/df332e015a6d935f12396ae1323b4327?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="CharliePlett&#39;s gravatar image" />
<p><span>CharliePlett</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="CharliePlett has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Sep '23, 04:22</strong> </span></p>
</div>
</div>
<div id="comments-container-84572" class="comments-container">
&#10;</div>
<div id="comment-tools-84572" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84572-form-container" class="comment-form-container">
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


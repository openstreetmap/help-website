+++
type = "question"
title = "PBF file parsing"
description = '''Hi, How can I parse(read) a binary *.pbf extract of a country ? Do I need some additional software or I can do it with standard functions of any programming language ? Thanks'''
date = "2012-02-07T14:00:00Z"
lastmod = "2016-12-07T17:28:00Z"
weight = 10468
keywords = [ "parser", "extract" ]
aliases = [ "/questions/10468" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [PBF file parsing](/questions/10468/pbf-file-parsing)

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
<span id="post-10468-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10468-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-10468-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>How can I parse(read) a binary *.pbf extract of a country ? Do I need some additional software or I can do it with standard functions of any programming language ?</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-parser" rel="tag" title="see questions tagged &#39;parser&#39;">parser</span> <span class="post-tag tag-link-extract" rel="tag" title="see questions tagged &#39;extract&#39;">extract</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Feb '12, 14:00</strong></p>
<img src="https://secure.gravatar.com/avatar/e8343c2fdfd08fea47ea8a0dc5210607?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MrX1&#39;s gravatar image" />
<p><span>MrX1</span><br />
<span class="score" title="46 reputation points">46</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MrX1 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-10468" class="comments-container">
&#10;</div>
<div id="comment-tools-10468" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10468-form-container" class="comment-form-container">
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

<span id="10469"></span>

<div id="answer-container-10469" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-10469-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10469-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-10469-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Well in theory you can use any programming language to parse the data without the help of any libraries. Here's a C program that does exactly that: <a href="http://m.m.i24.cc/osmconvert.c">http://m.m.i24.cc/osmconvert.c</a> - the more usual way, however, is to use a Google Protocol Buffer library to parse the data. Ready-made OSM reading modules exist for Java, Python, and for C++ <a href="http://wiki.openstreetmap.org/wiki/Osmium">("Osmium")</a> among others.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Feb '12, 14:04</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Feb '12, 07:23</strong> </span></p>
</div>
</div>
<div id="comments-container-10469" class="comments-container">
<span id="10471"></span>
<div id="comment-10471" class="comment">
<div id="post-10471-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Frederik it's amazing how quickly you create useful answer for any question. Well done. Thank you</p>
</div>
<div id="comment-10471-info" class="comment-info">
<span class="comment-age">(07 Feb '12, 14:38)</span> <span class="comment-user userinfo">MrX1</span>
</div>
</div>
<span id="14030"></span>
<div id="comment-14030" class="comment">
<div id="post-14030-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The <a href="http://wiki.openstreetmap.org/wiki/Osmconvert">wiki</a> page for osmconvert is also worth a read - it has links to various binary versions too.</p>
</div>
<div id="comment-14030-info" class="comment-info">
<span class="comment-age">(06 Jul '12, 11:56)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-10469" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10469-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="53306"></span>

<div id="answer-container-53306" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53306-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53306-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-53306-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Here's an example of parsing a .pbf file natively in Ruby: <a href="https://github.com/systemed/ruby_osmpbf">https://github.com/systemed/ruby_osmpbf</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Dec '16, 17:28</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-53306" class="comments-container">
&#10;</div>
<div id="comment-tools-53306" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53306-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="10474"></span>

<div id="answer-container-10474" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-10474-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10474-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-10474-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can download Osmosis.</p>
<p>In the bin directory</p>
<p>drop your pbf file<br />
</p>
<p>Create a run.bat file in notepad with following commands all on one line :</p>
<p>osmosis --read-pbf my_map.osm.pbf --write-xml my_map.osm</p>
<p>save bat file in the same folder and dble click on it</p>
<p>this will create your new osm file</p>
<p>Read instructions for more more detailed commands</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Feb '12, 17:17</strong></p>
<img src="https://secure.gravatar.com/avatar/8ba2c58c05833657151b21837517bea1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wilpin&#39;s gravatar image" />
<p><span>wilpin</span><br />
<span class="score" title="37 reputation points">37</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wilpin has no accepted answers">0%</span> </br></p>
</div>
</div>
<div id="comments-container-10474" class="comments-container">
<span id="10491"></span>
<div id="comment-10491" class="comment">
<div id="post-10491-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The question of MrX1 was about parsing a PBF file for own purposes, maybe with an own program.</p>
<p>Your way would be correct if you just wanna convert a PBF into an OSM file. This can also be done with <a href="http://wiki.openstreetmap.org/wiki/Osmconvert">http://wiki.openstreetmap.org/wiki/Osmconvert</a> ... maybe even in a more simple way.</p>
</div>
<div id="comment-10491-info" class="comment-info">
<span class="comment-age">(08 Feb '12, 16:35)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
<span id="10534"></span>
<div id="comment-10534" class="comment">
<div id="post-10534-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>When the user reads the instructions as recommended, he'll see that with Osmosis he can also manipulate the data. Additionally, maybe Osmembrane should be mentioned, a GUI for osmosis.</p>
<p>Plus, <a href="http://wiki.openstreetmap.org/wiki/Osmfilter">http://wiki.openstreetmap.org/wiki/Osmfilter</a> should be worth a look.</p>
</div>
<div id="comment-10534-info" class="comment-info">
<span class="comment-age">(11 Feb '12, 09:46)</span> <span class="comment-user userinfo">malenki</span>
</div>
</div>
</div>
<div id="comment-tools-10474" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10474-form-container" class="comment-form-container">
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


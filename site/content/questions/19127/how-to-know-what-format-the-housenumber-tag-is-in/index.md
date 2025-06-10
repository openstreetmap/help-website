+++
type = "question"
title = "How to know what format the housenumber tag is in"
description = '''All, Looking at OSM data, I see housenumber tag being entered in multiple ways such as  12345 12A 12a,12b 12-15 etc... There are probably more formats. I am trying to parse this data and need to know what format this data is. Is there something in the OSM data that could help me here? I suppose I co...'''
date = "2013-01-15T20:39:00Z"
lastmod = "2015-01-06T12:02:00Z"
weight = 19127
keywords = [ "housenumbers", "housenumber", "osg", "housenumbering" ]
aliases = [ "/questions/19127" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [How to know what format the housenumber tag is in](/questions/19127/how-to-know-what-format-the-housenumber-tag-is-in)

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
<span id="post-19127-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19127-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-19127-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>All, Looking at OSM data, I see housenumber tag being entered in multiple ways such as 12345 12A 12a,12b 12-15 etc... There are probably more formats.</p>
<p>I am trying to parse this data and need to know what format this data is. Is there something in the OSM data that could help me here? I suppose I could parse and test all housenumbers against all possible formats and determine what format it is in. Am I missing something that could help me to determine the format the housenumber tag is in while I read the OSM data?</p>
<p>Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-housenumbers" rel="tag" title="see questions tagged &#39;housenumbers&#39;">housenumbers</span> <span class="post-tag tag-link-housenumber" rel="tag" title="see questions tagged &#39;housenumber&#39;">housenumber</span> <span class="post-tag tag-link-osg" rel="tag" title="see questions tagged &#39;osg&#39;">osg</span> <span class="post-tag tag-link-housenumbering" rel="tag" title="see questions tagged &#39;housenumbering&#39;">housenumbering</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Jan '13, 20:39</strong></p>
<img src="https://secure.gravatar.com/avatar/343237842fce1f7a82f69ebf7a92f6b6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kcjailbirds&#39;s gravatar image" />
<p><span>kcjailbirds</span><br />
<span class="score" title="141 reputation points">141</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kcjailbirds has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-19127" class="comments-container">
&#10;</div>
<div id="comment-tools-19127" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19127-form-container" class="comment-form-container">
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

<span id="19153"></span>

<div id="answer-container-19153" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-19153-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19153-score" class="post-score" title="current number of votes">
8
</div>
<span id="post-19153-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="kcjailbirds has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This probably depends from country to country. For instance, in Austria three official variants are used:</p>
<ul>
<li>numbers (most commonly): 12</li>
<li>numbers plus letter(s) attached (letter not case sensitive): 12a</li>
<li>from - to numbers: 12-14</li>
</ul>
<p>And housenumbers are - often, but not always - ordered and odd on the left and even on the right side of the street. Sometimes they are randomly scattered around the whole village.</p>
<p>And BTW: there is nothing to parse here. Use them as they are entered. And if you implement a search, be "forgivable". A search for "12" should find "12", "12a", "12-14" and "10-14".</p>
<p>/al</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Jan '13, 08:30</strong></p>
<img src="https://secure.gravatar.com/avatar/5501080a7333d6383d6c545f076eaeba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="_al&#39;s gravatar image" />
<p><span>_al</span><br />
<span class="score" title="860 reputation points">860</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="_al has one accepted answer">4%</span></p>
</div>
</div>
<div id="comments-container-19153" class="comments-container">
<span id="19163"></span>
<div id="comment-19163" class="comment">
<div id="post-19163-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thank you. You are correct. Instead of parsing, we need to adjust the search engine.</p>
</div>
<div id="comment-19163-info" class="comment-info">
<span class="comment-age">(17 Jan '13, 14:32)</span> <span class="comment-user userinfo">kcjailbirds</span>
</div>
</div>
<span id="19209"></span>
<div id="comment-19209" class="comment">
<div id="post-19209-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I even had to use non-official formats once, to get around governmental mistakes: <a href="http://osm.org/go/0EgfbRBHI--">http://osm.org/go/0EgfbRBHI--</a></p>
<p>If you look at the official data, those streets are highlighted that they have mistakes, but the mistakes can only be solved by renumbering the street (something I can't do). So until now, the housenumbers start with a letter.</p>
</div>
<div id="comment-19209-info" class="comment-info">
<span class="comment-age">(19 Jan '13, 13:42)</span> <span class="comment-user userinfo">Sanderd17</span>
</div>
</div>
</div>
<div id="comment-tools-19153" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19153-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="19129"></span>

<div id="answer-container-19129" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-19129-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19129-score" class="post-score" title="current number of votes">
10
</div>
<span id="post-19129-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are as many formats as exist in the real life + all the possible insertion mistakes. Take a look at the <a href="http://taginfo.openstreetmap.org/keys/addr:housenumber#values">taginfo page</a> for different values. There are more than 20 thousand different values that use at least 100 different formats.</p>
<p>You can find out from the <a href="http://wiki.openstreetmap.org/wiki/Addresses">wiki</a> why some of these formats are used.</p>
<p>Depending on your needs you may concider treating housenumbers as text.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Jan '13, 21:41</strong></p>
<img src="https://secure.gravatar.com/avatar/f7f8127223bd00c9e8f569ce2e9ddf22?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RM87&#39;s gravatar image" />
<p><span>RM87</span><br />
<span class="score" title="3346 reputation points"><span>3.3k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="37 badges"><span class="silver">●</span><span class="badgecount">37</span></span><span title="53 badges"><span class="bronze">●</span><span class="badgecount">53</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RM87 has 20 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-19129" class="comments-container">
<span id="19130"></span>
<div id="comment-19130" class="comment">
<div id="post-19130-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for your coment. I realize that there are many many different formats of housenumber out there plus mistakes. I also found some that say something like "FIXME". I am extracting housenumber as text and storing in sql database. I was hoping there was a way to know what format they are actually in but it does not look like it.</p>
</div>
<div id="comment-19130-info" class="comment-info">
<span class="comment-age">(15 Jan '13, 21:55)</span> <span class="comment-user userinfo">kcjailbirds</span>
</div>
</div>
<span id="40040"></span>
<div id="comment-40040" class="comment">
<div id="post-40040-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>"you may concider treating housenumbers as text." Actually that's probably the <em>only</em> option - there are too many formats to parse house numbers reliably, unless you limit yourself to a specific country or part of a country.</p>
</div>
<div id="comment-40040-info" class="comment-info">
<span class="comment-age">(05 Jan '15, 16:29)</span> <span class="comment-user userinfo">sleske</span>
</div>
</div>
</div>
<div id="comment-tools-19129" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19129-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="40054"></span>

<div id="answer-container-40054" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-40054-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40054-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-40054-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>See: <a href="https://dl.dropboxusercontent.com/u/29846412/Mapping/DR%20AS%20NZS%204819%20Rural%20and%20urban%20addressing.pdf">AS NZ Rural and Urban Addressing Standards Draft</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Jan '15, 12:02</strong></p>
<img src="https://secure.gravatar.com/avatar/44c55dd2284bac32e4abdd4d65d00b27?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aaronsta&#39;s gravatar image" />
<p><span>aaronsta</span><br />
<span class="score" title="25 reputation points">25</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aaronsta has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Jan '15, 05:06</strong> </span></p>
</div>
</div>
<div id="comments-container-40054" class="comments-container">
&#10;</div>
<div id="comment-tools-40054" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40054-form-container" class="comment-form-container">
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


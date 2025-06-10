+++
type = "question"
title = "How to download the OSM data together with the information about the contributors?"
description = '''Hi, as I am new to OSM in many ways my question may look strange or easy to be done, so sorry for that in advance. I want to download a certain part of OSM data into my local computer. I know I can probably use Overpass API for that (I know about this tool - http://overpass-turbo.eu/). But together ...'''
date = "2016-02-13T12:49:00Z"
lastmod = "2016-02-13T22:23:00Z"
weight = 48099
keywords = [ "overpass-turbo", "user" ]
aliases = [ "/questions/48099" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to download the OSM data together with the information about the contributors?](/questions/48099/how-to-download-the-osm-data-together-with-the-information-about-the-contributors)

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
<span id="post-48099-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48099-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-48099-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, as I am new to OSM in many ways my question may look strange or easy to be done, so sorry for that in advance.</p>
<p>I want to download a certain part of OSM data into my local computer. I know I can probably use Overpass API for that (I know about this tool - <a href="http://overpass-turbo.eu/).">http://overpass-turbo.eu/).</a> But together with the geographic location of the data, I would like to retrieve the information about users themselves as well. I checked how the OSM database looks like and there is a table which contains the information about users called User.</p>
<p>Anyone knows how to use that? I should just probably use some SQL join query going joining multiple tables, is that?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-user" rel="tag" title="see questions tagged &#39;user&#39;">user</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Feb '16, 12:49</strong></p>
<img src="https://secure.gravatar.com/avatar/6519da24f1dd200123ae19bca273523b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bodnarm89&#39;s gravatar image" />
<p><span>bodnarm89</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bodnarm89 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-48099" class="comments-container">
<span id="48107"></span>
<div id="comment-48107" class="comment">
<div id="post-48107-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>crosspost: <a href="https://stackoverflow.com/questions/35380506/how-to-download-the-osm-data-together-with-the-information-about-the-contributor">https://stackoverflow.com/questions/35380506/how-to-download-the-osm-data-together-with-the-information-about-the-contributor</a></p>
</div>
<div id="comment-48107-info" class="comment-info">
<span class="comment-age">(13 Feb '16, 22:23)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-48099" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48099-form-container" class="comment-form-container">
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

<span id="48100"></span>

<div id="answer-container-48100" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48100-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48100-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-48100-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="bodnarm89 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Overpass API will return extended information about objects if you use the print statement <code>out meta</code>. It only returns information about the last user to change an object. A deeper analysis than that would require tracking the history somehow (the history dumps or changesets or...).</p>
<p>If you want information <em>about</em> the users, the OSM API could then be used to access public profile information:</p>
<p><a href="http://wiki.openstreetmap.org/wiki/API_v0.6#Methods_for_user_data">http://wiki.openstreetmap.org/wiki/API_v0.6#Methods_for_user_data</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Feb '16, 14:09</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-48100" class="comments-container">
&#10;</div>
<div id="comment-tools-48100" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48100-form-container" class="comment-form-container">
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


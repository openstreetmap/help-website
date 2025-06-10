+++
type = "question"
title = "Find most recent imagery for a given place"
description = '''Hi all Here is the problem statement: very often when doing mapping for HOT or mapping place I know I would like to make sure I use the latest imagery. I sometimes check manually by opening several imageries in JOSM e.g. Bing, DG, Mapbox, but it&#x27;s a bit tedious, and it&#x27;s not comprehensive, for exemp...'''
date = "2018-02-17T03:42:00Z"
lastmod = "2018-02-18T23:23:00Z"
weight = 62168
keywords = [ "imagery" ]
aliases = [ "/questions/62168" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Find most recent imagery for a given place](/questions/62168/find-most-recent-imagery-for-a-given-place)

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
<span id="post-62168-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62168-score" class="post-score" title="current number of votes">
7
</div>
<span id="post-62168-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all</p>
<p>Here is the problem statement: very often when doing mapping for HOT or mapping place I know I would like to make sure I use the latest imagery. I sometimes check manually by opening several imageries in JOSM e.g. Bing, DG, Mapbox, but it's a bit tedious, and it's not comprehensive, for exemple I don't go to OpenAerialMap, Mapillary or equivalent.</p>
<p>So my question is: is there a way to find which is the most recent imagery for a given place, or that will list all resources available for a given place?</p>
<p>Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-imagery" rel="tag" title="see questions tagged &#39;imagery&#39;">imagery</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Feb '18, 03:42</strong></p>
<img src="https://secure.gravatar.com/avatar/c6e5197a13718a370dcc25a9e3dff86e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="David%20V&#39;s gravatar image" />
<p><span>David V</span><br />
<span class="score" title="116 reputation points">116</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="David V has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Feb '18, 03:42</strong> </span></p>
</div>
</div>
<div id="comments-container-62168" class="comments-container">
&#10;</div>
<div id="comment-tools-62168" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62168-form-container" class="comment-form-container">
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

<span id="62169"></span>

<div id="answer-container-62169" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-62169-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62169-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-62169-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For most imagery layers it seems not possible to know the capture date. For Bing in JOSM you can just right-click and check <strong>Show tile info</strong>: in <em>Metadata Capture Date</em> you will see the date the images were captured. But even in that case, you get sometimes a segment of time that spans 2 years...</p>
<p>In order to know (or guess) what is the most recent imagery, what I do is comparing the imagery providers for the area, looking for objects that are in construction. For example, you will notice some buildings present in one imagery and not in other. There can be surely buildings that existed in 2014 but were already destroyed in 2016, but the majority of buildings are constructed, not destroyed. Another object that helps are bridges, but there are many others. Just use your common sense, and you will surely find out which imagery is the newest of all.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Feb '18, 12:09</strong></p>
<img src="https://secure.gravatar.com/avatar/d45c161edd4b471fd947a7ec574274ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="edvac&#39;s gravatar image" />
<p><span>edvac</span><br />
<span class="score" title="665 reputation points">665</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="edvac has 4 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-62169" class="comments-container">
<span id="62170"></span>
<div id="comment-62170" class="comment">
<div id="post-62170-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>… Often comparing is good anyway - to see different times of day, times of year and viewing angles. Though, <em>knowing</em> the most recent one would be a good starting point, indeed.</p>
</div>
<div id="comment-62170-info" class="comment-info">
<span class="comment-age">(17 Feb '18, 12:26)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="62176"></span>
<div id="comment-62176" class="comment">
<div id="post-62176-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Thanks a lot for the tips Edvac. That doesn't really answer my question though. Those checks are what I already do, I was wondering if there is a sort of search engine of imagery, where you could type coordinates and find which imagery is available for that location (ideally with their date).</p>
</div>
<div id="comment-62176-info" class="comment-info">
<span class="comment-age">(17 Feb '18, 13:49)</span> <span class="comment-user userinfo">David V</span>
</div>
</div>
<span id="62182"></span>
<div id="comment-62182" class="comment">
<div id="post-62182-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ok, I see. I don't really know if such search engine actually exists. In any case, your question is interesting. If only all the imagery had a standardized Metadata Capture Date field, it would make the job easier.</p>
</div>
<div id="comment-62182-info" class="comment-info">
<span class="comment-age">(18 Feb '18, 17:02)</span> <span class="comment-user userinfo">edvac</span>
</div>
</div>
</div>
<div id="comment-tools-62169" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62169-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="62187"></span>

<div id="answer-container-62187" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-62187-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62187-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62187-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Well, you can always try to compare imagery that you can legally use with one that's available in Google Earth and has capture date specified. It has a clock icon which lets you load older images. I think you will be fine if you don't use information from Google Earth in mapping, only just to narrow down the age of whatever imagery we can use.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Feb '18, 20:12</strong></p>
<img src="https://secure.gravatar.com/avatar/b68bcf9f1c4a7921aeee1bb35b0e2784?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RicoElectrico&#39;s gravatar image" />
<p><span>RicoElectrico</span><br />
<span class="score" title="371 reputation points">371</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RicoElectrico has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-62187" class="comments-container">
&#10;</div>
<div id="comment-tools-62187" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62187-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="62191"></span>

<div id="answer-container-62191" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-62191-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62191-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62191-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Both iD and vespucci will order imagery selection lists in sensible way taking the age of the imagery in to account together with other properties.</p>
<p>More detailed information where available can be found directly in the <a href="https://github.com/osmlab/editor-layer-index">editor imagery index</a> and for JOSM on <a href="https://josm.openstreetmap.de/wiki/Maps">JOSM background layers wiki</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Feb '18, 23:23</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-62191" class="comments-container">
&#10;</div>
<div id="comment-tools-62191" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62191-form-container" class="comment-form-container">
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


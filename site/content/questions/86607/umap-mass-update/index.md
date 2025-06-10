+++
type = "question"
title = "umap mass update"
description = '''Hi, What is the process to mass update a .umap file? I would expect a tool to convert it to .csv for further manipulation. Thank you, Martin'''
date = "2023-02-01T16:52:00Z"
lastmod = "2023-02-19T12:48:00Z"
weight = 86607
keywords = [ "umap" ]
aliases = [ "/questions/86607" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [umap mass update](/questions/86607/umap-mass-update)

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
<span id="post-86607-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86607-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86607-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, What is the process to mass update a .umap file? I would expect a tool to convert it to .csv for further manipulation.</p>
<p>Thank you, Martin</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-umap" rel="tag" title="see questions tagged &#39;umap&#39;">umap</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Feb '23, 16:52</strong></p>
<img src="https://secure.gravatar.com/avatar/310e67303461fe66418a76cc89000402?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="martingwb&#39;s gravatar image" />
<p><span>martingwb</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="martingwb has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-86607" class="comments-container">
&#10;</div>
<div id="comment-tools-86607" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86607-form-container" class="comment-form-container">
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

<span id="86676"></span>

<div id="answer-container-86676" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86676-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86676-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-86676-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi.</p>
<p>a umap file is basically json, so you can use json-oriented tools to process the data.</p>
<p>Or you can download the data of your umap as GPX, and use one the various converter to get CSV from GPX.</p>
<p>Regards.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Feb '23, 11:26</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-86676" class="comments-container">
<span id="86711"></span>
<div id="comment-86711" class="comment">
<div id="post-86711-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for your reply. Actually I have tried a few web based json converters but did not succeed. Can you name one which does work? Thanks, Martin</p>
</div>
<div id="comment-86711-info" class="comment-info">
<span class="comment-age">(16 Feb '23, 17:33)</span> <span class="comment-user userinfo">martingwb</span>
</div>
</div>
<span id="86739"></span>
<div id="comment-86739" class="comment">
<div id="post-86739-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Bear in mind that that "umap" file is a special format, based on json, that usually won't be understood by third-party tools.</p>
<p>If you want to try to extract specific data from your umap file, general-purpose json editor (like this <a href="https://jsoneditoronline.org/">one</a>) might help you.</p>
<p>On the other hand, if you're mostly interested in geographical data, I've tried to download the (visible) map data (from the umap interface, '<a href="https://wiki.openstreetmap.org/wiki/UMap/Guide/Export_data_of_my_uMap#Download_data">Advanced actions</a>') as GPX and converted it with the <a href="https://mygeodata.cloud/converter/gpx-to-csv">first result</a> of a search engine. Also tried with geojson and this <a href="geojson.io/">one</a> with some success.</p>
<p>The results will depend on the complexity of the data, and some converters have options to select either the points, or the lines and so on...</p>
<p>Regards</p>
</div>
<div id="comment-86739-info" class="comment-info">
<span class="comment-age">(19 Feb '23, 12:48)</span> <span class="comment-user userinfo">H_mlet</span>
</div>
</div>
</div>
<div id="comment-tools-86676" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86676-form-container" class="comment-form-container">
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


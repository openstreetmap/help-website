+++
type = "question"
title = "How to add Mapnik osmdroid zip files to sd card from code"
description = '''Hi guys, I am facing a problem here about using offline openstreetmap. I am using Mobile atlas creator to create osmdroid zip files used as offline map resources. I searched several articles about how to use this zip file. They all mentioned that we need to add this zip file (or unzipped one) to sd ...'''
date = "2012-05-14T12:01:00Z"
lastmod = "2012-05-18T01:58:00Z"
weight = 12718
keywords = [ "openstreetmap", "map", "offline", "sdcard", "mapnik" ]
aliases = [ "/questions/12718" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to add Mapnik osmdroid zip files to sd card from code](/questions/12718/how-to-add-mapnik-osmdroid-zip-files-to-sd-card-from-code)

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
<span id="post-12718-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12718-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-12718-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi guys, I am facing a problem here about using offline openstreetmap. I am using Mobile atlas creator to create osmdroid zip files used as offline map resources. I searched several articles about how to use this zip file. They all mentioned that we need to add this zip file (or unzipped one) to sd card manually.</p>
<p>Well, I was wandering if I can do this from my code; let's say putting this zip file in assets folder or anywhere; and add it to user's handphone sd card later? Or just reference it from the code? So the users don't need to add it manually..They might be lazy to do so....Please kindly leave any suggestions you may have.....Thank you very much!!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span> <span class="post-tag tag-link-offline" rel="tag" title="see questions tagged &#39;offline&#39;">offline</span> <span class="post-tag tag-link-sdcard" rel="tag" title="see questions tagged &#39;sdcard&#39;">sdcard</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 May '12, 12:01</strong></p>
<img src="https://secure.gravatar.com/avatar/94236a92b0de27ec317a147de30e9780?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kelsie&#39;s gravatar image" />
<p><span>Kelsie</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kelsie has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-12718" class="comments-container">
&#10;</div>
<div id="comment-tools-12718" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12718-form-container" class="comment-form-container">
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

<span id="12781"></span>

<div id="answer-container-12781" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-12781-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12781-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-12781-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Well guys, I found a way to do it. Put the zip file in assets folder in the program. When app starts, check if "osmdroid" directory exists under Environment.getExternalStorageDirectory().getPath(). If not, create the directory and copy the zip file to that folder! But you should seek users permission for doing so.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 May '12, 01:58</strong></p>
<img src="https://secure.gravatar.com/avatar/94236a92b0de27ec317a147de30e9780?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kelsie&#39;s gravatar image" />
<p><span>Kelsie</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kelsie has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-12781" class="comments-container">
&#10;</div>
<div id="comment-tools-12781" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12781-form-container" class="comment-form-container">
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


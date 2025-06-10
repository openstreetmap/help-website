+++
type = "question"
title = "Upload Addresses with GPS coordinates to OSM"
description = '''Hello, I have a list of Addresses and gps coordinates and I was wondering if this list can be sent to you to vet and upload to OSM. After this batch is done, is there a was to use a python script to add new nodes as they are identified after the batch file is uploaded above? Please let me know if th...'''
date = "2014-08-28T14:03:00Z"
lastmod = "2014-09-02T13:01:00Z"
weight = 36331
keywords = [ "import" ]
aliases = [ "/questions/36331" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Upload Addresses with GPS coordinates to OSM](/questions/36331/upload-addresses-with-gps-coordinates-to-osm)

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
<span id="post-36331-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36331-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-36331-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I have a list of Addresses and gps coordinates and I was wondering if this list can be sent to you to vet and upload to OSM.</p>
<p>After this batch is done, is there a was to use a python script to add new nodes as they are identified after the batch file is uploaded above?</p>
<p>Please let me know if this can be done, and what format should I send the data.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Aug '14, 14:03</strong></p>
<img src="https://secure.gravatar.com/avatar/ee63b7c26c26508dfefd8231620f464d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="loc_id&#39;s gravatar image" />
<p><span>loc_id</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="loc_id has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Sep '14, 12:39</strong> </span></p>
</div>
</div>
<div id="comments-container-36331" class="comments-container">
&#10;</div>
<div id="comment-tools-36331" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-36331-form-container" class="comment-form-container">
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

<span id="36503"></span>

<div id="answer-container-36503" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-36503-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36503-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-36503-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi loc_id, Read this first, there a lot of lookalike questions in this database, <a href="https://help.openstreetmap.org/search/?csrfmiddlewaretoken=iJOi8cXg8Kpav7sJUCWwVHuOchDiXwwD&amp;q=how+to+upload+GPS&amp;t=question">https://help.openstreetmap.org/search/?csrfmiddlewaretoken=iJOi8cXg8Kpav7sJUCWwVHuOchDiXwwD&amp;q=how+to+upload+GPS&amp;t=question</a> For instance there are a couple of questions that you should answer, before thinking about the technical aspects of the import: Am I allowed to use the data and publish it under CC-BY-SA as well as under ODbL? Is the data set accurate and useful? Does the local community want the import Do I have the technical abilities to cleanly conduct the import? Does the data set conflict with existing data in OpenStreetMap? The first four question determine if you should import the data at all and the fifth one has a large influence on the way to do it. About the import itself there are many way, some of which I'll give here, roughly ordered by amount of manual work: Tracing from custom images uses as background Creating XML and manually copying from one layer to another in JOSM Creating XML and automatically merge with exisiting data, check with JOSM and upload Custom upload script Please get clear answers to the questions listed above, especially #1 and #3 before proceeding with any import to OpenStreetMap. OpenStreetMap is not a dataset dumping ground nor an aerial tracing project but an outdoor activity. And more Questions and Answers can be found behind the link.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Sep '14, 13:01</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-36503" class="comments-container">
&#10;</div>
<div id="comment-tools-36503" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-36503-form-container" class="comment-form-container">
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


+++
type = "question"
title = "problem installing uMap locally and problem saving POIs (probably connected)"
description = '''So I managed to set up both an osm tile server (which runs like a charm thanks to an exceptionally good tutorial on how to set it up) and uMAP locally and it mostly works (completely without internet access, just like it wanted it), but I experience two issues (which may or may not be connected - as...'''
date = "2018-03-05T18:31:00Z"
lastmod = "2018-08-27T17:47:00Z"
weight = 62517
keywords = [ "umap", "installation", "linux" ]
aliases = [ "/questions/62517" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [problem installing uMap locally and problem saving POIs (probably connected)](/questions/62517/problem-installing-umap-locally-and-problem-saving-pois-probably-connected)

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
<span id="post-62517-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62517-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62517-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>So I managed to set up both an osm tile server (which runs like a charm thanks to an exceptionally good tutorial on how to set it up) and uMAP locally and it mostly works (completely without internet access, just like it wanted it), but I experience two issues (which may or may not be connected - as I understand really VERY little of how Linux and all of this works behind the scenes). I can get things running with the help of a good tutorial, but I'm totally lost when something goes wrong.</p>
<p>Problem is: My tiles load in the background, I can access the uMAP-GUI, create a new map, even create POIs and everything - but I can't save my POIs.</p>
<p>However, I already had an issue during installation (I followed this guide: <a href="https://umap-project.readthedocs.io/en/latest/install/):">https://umap-project.readthedocs.io/en/latest/install/):</a></p>
<p>"umap collectstatic" doesn't work and gives me this error OSError: [Errno 2] No such file or directory: '/home/ybon/Code/js/Leaflet.Storage</p>
<p>I don't know how important this is (and what collectstatic actually does...)- I was able to continue with my installation normally and still able to start my server. I tried so many things that I'm not sure if this was the first error message or not (I think there was something else about a directory missing before that and I created one by hand but not sure)</p>
<p>No idea where the file/directory is supposed to be coming from and why it is not there /where and when it should have been created and what else I can do. I was supposed to configure a couple of paths in a local.py - file but this one was not among them. I was supposed to change these paths (and created the folders respectively)</p>
<h1 id="for-static-deployment">For static deployment</h1>
<p>STATIC_ROOT = '/home/fayyy/umap/var/static'</p>
<h1 id="for-users-statics-geojson-mainly">For users' statics (geojson mainly)</h1>
<p>MEDIA_ROOT = '/home/fayyy/umap/var/data'</p>
<p>That was during installation.</p>
<p>Now, when I try to save a POI I get "Problem in the response" and this error</p>
<p>OSError: [Errno 13] Permission denied: '/home/ybon/.virtualenvs/umap/var/uploads</p>
<p>Problem is, that this folder (probably?) doesn't even exist and I don't know WHERE I even should put it (or look for it to change its permissions)(since this is in a virtual environment as suggested in the installation guide). There is no folder "ybon" anywhere anyway. I could create one but I guess that's not the way.</p>
<p>Can somebody please help me ? I've been trying to find a solution for hours. For someone experienced with Linux and all these shell commands this is probably crystal clear and super easy, but I absolutely have no clue what's going on...</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-umap" rel="tag" title="see questions tagged &#39;umap&#39;">umap</span> <span class="post-tag tag-link-installation" rel="tag" title="see questions tagged &#39;installation&#39;">installation</span> <span class="post-tag tag-link-linux" rel="tag" title="see questions tagged &#39;linux&#39;">linux</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Mar '18, 18:31</strong></p>
<img src="https://secure.gravatar.com/avatar/4a2043cccc6b63fd0449319af86e560e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fayyyyyy&#39;s gravatar image" />
<p><span>fayyyyyy</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fayyyyyy has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-62517" class="comments-container">
&#10;</div>
<div id="comment-tools-62517" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62517-form-container" class="comment-form-container">
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

<span id="65583"></span>

<div id="answer-container-65583" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65583-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65583-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65583-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Geolocation error: position unavailable. I live in San Juan PR</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Aug '18, 17:47</strong></p>
<img src="https://secure.gravatar.com/avatar/f4f9e29920b41b112fecf3c42321fbd3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jrvelezb&#39;s gravatar image" />
<p><span>jrvelezb</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jrvelezb has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-65583" class="comments-container">
&#10;</div>
<div id="comment-tools-65583" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65583-form-container" class="comment-form-container">
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


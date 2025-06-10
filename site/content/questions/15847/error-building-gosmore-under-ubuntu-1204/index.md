+++
type = "question"
title = "Error building Gosmore under ubuntu 12.04"
description = '''I am trying to build Gosmore under Ubuntu 12.04. I am following the instrucions on http://wiki.openstreetmap.org/wiki/Gosmore#Downloading_and_running: sudo apt-get install libxml2-dev libgtk2.0-dev g++ make subversion libcurl4-gnutls-dev libgps-dev svn co http://svn.openstreetmap.org/applications/re...'''
date = "2012-09-06T15:40:00Z"
lastmod = "2013-03-31T16:52:00Z"
weight = 15847
keywords = [ "gosmore", "ubuntu" ]
aliases = [ "/questions/15847" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Error building Gosmore under ubuntu 12.04](/questions/15847/error-building-gosmore-under-ubuntu-1204)

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
<span id="post-15847-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15847-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-15847-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to build Gosmore under Ubuntu 12.04. I am following the instrucions on <a href="http://wiki.openstreetmap.org/wiki/Gosmore#Downloading_and_running:">http://wiki.openstreetmap.org/wiki/Gosmore#Downloading_and_running:</a></p>
<pre><code>sudo apt-get install libxml2-dev libgtk2.0-dev g++ make subversion libcurl4-gnutls-dev libgps-dev
svn co http://svn.openstreetmap.org/applications/rendering/gosmore/
cd gosmore
./configure
make</code></pre>
<p>when I run make I get the following errors:</p>
<p>jni/gosmore.cpp:3649:39: error: gps_set_raw_hook was not declared in this scope</p>
<p>jni/gosmore.cpp:3656:26: error: gps_poll was not declared in this scope</p>
<p>jni/gosmore.cpp:3647:54: error: too few arguments to function int gps_open(const char<em>, const char</em>, gps_data_t*)</p>
<p>Is this a bug? How can I fix it?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-gosmore" rel="tag" title="see questions tagged &#39;gosmore&#39;">gosmore</span> <span class="post-tag tag-link-ubuntu" rel="tag" title="see questions tagged &#39;ubuntu&#39;">ubuntu</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Sep '12, 15:40</strong></p>
<img src="https://secure.gravatar.com/avatar/d718afe8f5d202ce2646d8d9edf24157?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tvasb&#39;s gravatar image" />
<p><span>Tvasb</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tvasb has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-15847" class="comments-container">
&#10;</div>
<div id="comment-tools-15847" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15847-form-container" class="comment-form-container">
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

<span id="21110"></span>

<div id="answer-container-21110" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-21110-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21110-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-21110-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>see possible solution at <a href="http://wiki.openstreetmap.org/wiki/Talk:Gosmore">http://wiki.openstreetmap.org/wiki/Talk:Gosmore</a></p>
<p>Use at your own risk</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Mar '13, 16:52</strong></p>
<img src="https://secure.gravatar.com/avatar/966824d666ae94e2d24612c4eb480a50?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dmgroom&#39;s gravatar image" />
<p><span>dmgroom</span><br />
<span class="score" title="42 reputation points">42</span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dmgroom has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-21110" class="comments-container">
&#10;</div>
<div id="comment-tools-21110" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21110-form-container" class="comment-form-container">
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


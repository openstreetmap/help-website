+++
type = "question"
title = "changed virtual host"
description = '''this is ubuntu 12.04 lts updated. The sequence of commands that I&#x27;ve executed was from  http://switch2osm.org/serving-tiles/building-a-tile-server-from-packages/ I have several virtual hosts defined and enabled - xx1.com, xx2.com, xx3.com,... One of them (xx1.com) was accessible from outside through...'''
date = "2013-06-27T05:12:00Z"
lastmod = "2013-06-27T07:37:00Z"
weight = 23741
keywords = [ "recover", "installation", "localhost" ]
aliases = [ "/questions/23741" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [changed virtual host](/questions/23741/changed-virtual-host)

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
<span id="post-23741-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23741-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-23741-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>this is ubuntu 12.04 lts updated. The sequence of commands that I've executed was from <a href="http://switch2osm.org/serving-tiles/building-a-tile-server-from-packages/">http://switch2osm.org/serving-tiles/building-a-tile-server-from-packages/</a> I have several virtual hosts defined and enabled - xx1.com, xx2.com, xx3.com,... One of them (xx1.com) was accessible from outside through xxx.no-ip.org through an alias in configuration file in sites-available/ One of the side-effects of the install is that external access through xxx.no-ip.org now gets me to my local xx3.com Any ideas how I can change it back? Or, as a 2nd best alternative, point me to the source of the installation script?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-recover" rel="tag" title="see questions tagged &#39;recover&#39;">recover</span> <span class="post-tag tag-link-installation" rel="tag" title="see questions tagged &#39;installation&#39;">installation</span> <span class="post-tag tag-link-localhost" rel="tag" title="see questions tagged &#39;localhost&#39;">localhost</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Jun '13, 05:12</strong></p>
<img src="https://secure.gravatar.com/avatar/a8b33bde0d225a0588ab618bd62f2515?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gene292&#39;s gravatar image" />
<p><span>gene292</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gene292 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Jun '13, 16:23</strong> </span></p>
</div>
</div>
<div id="comments-container-23741" class="comments-container">
&#10;</div>
<div id="comment-tools-23741" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23741-form-container" class="comment-form-container">
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

<span id="23742"></span>

<div id="answer-container-23742" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-23742-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23742-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-23742-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is not an OpenStreetMap question, but a web server (likely Apache) configuration question, and as such it is off-topic here. If Apache, then the problem is likely that you were not using ServerName/NameVirtualHosts correctly and therefore the host that comes first in the alphabet gets all the hits. Read the virtual hosts documentation appropriate for your web server.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Jun '13, 07:37</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-23742" class="comments-container">
&#10;</div>
<div id="comment-tools-23742" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23742-form-container" class="comment-form-container">
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


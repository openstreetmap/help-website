+++
type = "question"
title = "Instructions for building a tile server on Redhat"
description = '''My company only allows Redhat Linux (Version: Red Hat Enterprise Linux Server 5.9). Has anyone tried building a tile servers using the instructions here? http://switch2osm.org/serving-tiles/manually-building-a-tile-server/ If yes, can you share the challenges/problems (if any). Also, what should I b...'''
date = "2014-06-27T16:07:00Z"
lastmod = "2018-05-15T08:16:00Z"
weight = 34380
keywords = [ "centos", "ubuntu", "fedora", "redhat", "rhel" ]
aliases = [ "/questions/34380" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Instructions for building a tile server on Redhat](/questions/34380/instructions-for-building-a-tile-server-on-redhat)

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
<span id="post-34380-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34380-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-34380-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>My company only allows Redhat Linux (Version: Red Hat Enterprise Linux Server 5.9). Has anyone tried building a tile servers using the instructions here? <a href="http://switch2osm.org/serving-tiles/manually-building-a-tile-server/">http://switch2osm.org/serving-tiles/manually-building-a-tile-server/</a></p>
<p>If yes, can you share the challenges/problems (if any). Also, what should I be on the look out for? Any details on the which (version) packages to get? I also did read about users having problems with configuring mod_tile on redhat. Any workaround/info on that? Any help would be very appreciated.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-centos" rel="tag" title="see questions tagged &#39;centos&#39;">centos</span> <span class="post-tag tag-link-ubuntu" rel="tag" title="see questions tagged &#39;ubuntu&#39;">ubuntu</span> <span class="post-tag tag-link-fedora" rel="tag" title="see questions tagged &#39;fedora&#39;">fedora</span> <span class="post-tag tag-link-redhat" rel="tag" title="see questions tagged &#39;redhat&#39;">redhat</span> <span class="post-tag tag-link-rhel" rel="tag" title="see questions tagged &#39;rhel&#39;">rhel</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Jun '14, 16:07</strong></p>
<img src="https://secure.gravatar.com/avatar/82f60906a8f391b1cdd0d4d8ea0db158?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dk2005&#39;s gravatar image" />
<p><span>dk2005</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dk2005 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Jun '14, 17:22</strong> </span></p>
</div>
</div>
<div id="comments-container-34380" class="comments-container">
<span id="34381"></span>
<div id="comment-34381" class="comment">
<div id="post-34381-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>What Redhat (or CentOS) version in particular? Knowing that would enable people to compare the available packages in that with an existing set of Ubuntu instructions.</p>
</div>
<div id="comment-34381-info" class="comment-info">
<span class="comment-age">(27 Jun '14, 16:09)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="34383"></span>
<div id="comment-34383" class="comment">
<div id="post-34383-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Distributor ID: RedHatEnterpriseServer Description: Red Hat Enterprise Linux Server release 5.9 (Tikanga) Release: 5.9</p>
</div>
<div id="comment-34383-info" class="comment-info">
<span class="comment-age">(27 Jun '14, 17:21)</span> <span class="comment-user userinfo">dk2005</span>
</div>
</div>
<span id="63469"></span>
<div id="comment-63469" class="comment">
<div id="post-63469-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Wondering why there is no any good document on the Internet regarding Setup openstreetmap on RedHat Linux Enterprise Server, really interesting</p>
</div>
<div id="comment-63469-info" class="comment-info">
<span class="comment-age">(14 May '18, 15:43)</span> <span class="comment-user userinfo">ArashArteman</span>
</div>
</div>
<span id="63473"></span>
<div id="comment-63473" class="comment">
<div id="post-63473-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Did you try a docker image?</p>
</div>
<div id="comment-63473-info" class="comment-info">
<span class="comment-age">(14 May '18, 16:37)</span> <span class="comment-user userinfo">gfitz</span>
</div>
</div>
<span id="63482"></span>
<div id="comment-63482" class="comment">
<div id="post-63482-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I'm working with a Logistics Network Design Team and in our Company we have some restrications which prevents us to have another Distribution or some Kind of docker Images or VM, just Redhat Linux Enterprise one.</p>
</div>
<div id="comment-63482-info" class="comment-info">
<span class="comment-age">(15 May '18, 07:45)</span> <span class="comment-user userinfo">ArashArteman</span>
</div>
</div>
<span id="63483"></span>
<div id="comment-63483" class="comment not_top_scorer">
<div id="post-63483-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Docker sucks, so it's good if you don't use it.</p>
</div>
<div id="comment-63483-info" class="comment-info">
<span class="comment-age">(15 May '18, 08:16)</span> <span class="comment-user userinfo">Druzhba</span>
</div>
</div>
</div>
<div id="comment-tools-34380" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-34380-form-container" class="comment-form-container">
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

<span id="47723"></span>

<div id="answer-container-47723" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47723-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47723-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-47723-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I found the link which may help you</p>
<p><a href="http://duemafoss.blogspot.in/2014/02/installation-of-openstreetmap-server-on.html">http://duemafoss.blogspot.in/2014/02/installation-of-openstreetmap-server-on.html</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Jan '16, 07:31</strong></p>
<img src="https://secure.gravatar.com/avatar/99c1048662796ecabe2ec5e2252ce555?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Naren970&#39;s gravatar image" />
<p><span>Naren970</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Naren970 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-47723" class="comments-container">
&#10;</div>
<div id="comment-tools-47723" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47723-form-container" class="comment-form-container">
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


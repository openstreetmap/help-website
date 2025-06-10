+++
type = "question"
title = "Disable renderd debug messages"
description = '''I have a OSM server set up and it is writing a lot of debug messages to syslog, access.log, and journal logs. How do I disable the excessive logging?  I believe I have the access.log disabled via commenting out the CustomLog line in /etc/apache2/sites-available/000-default.conf Not sure what to do w...'''
date = "2021-10-11T21:27:00Z"
lastmod = "2022-01-25T18:28:00Z"
weight = 82132
keywords = [ "renderd", "osm", "mod_tile" ]
aliases = [ "/questions/82132" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Disable renderd debug messages](/questions/82132/disable-renderd-debug-messages)

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
<span id="post-82132-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82132-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82132-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a OSM server set up and it is writing a lot of debug messages to syslog, access.log, and journal logs. How do I disable the excessive logging?</p>
<p>I believe I have the access.log disabled via commenting out the CustomLog line in /etc/apache2/sites-available/000-default.conf</p>
<p>Not sure what to do with the others (syslog was 60GB before it filled my root partition...)</p>
<p>EDIT: Also, I saw an older message from Feb 2020 and nobody replied; I tried to find a solution but haven't found anything.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-mod_tile" rel="tag" title="see questions tagged &#39;mod_tile&#39;">mod_tile</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Oct '21, 21:27</strong></p>
<img src="https://secure.gravatar.com/avatar/ed49ee0853cfb44df8f2c26bc4b2c133?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sanosuke001&#39;s gravatar image" />
<p><span>sanosuke001</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sanosuke001 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Oct '21, 21:28</strong> </span></p>
</div>
</div>
<div id="comments-container-82132" class="comments-container">
&#10;</div>
<div id="comment-tools-82132" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82132-form-container" class="comment-form-container">
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

<span id="83193"></span>

<div id="answer-container-83193" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83193-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83193-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-83193-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>With regard to messages from renderd, there have been some issues raised about it such as <a href="https://github.com/openstreetmap/mod_tile/issues/170">https://github.com/openstreetmap/mod_tile/issues/170</a>. <a href="https://github.com/openstreetmap/mod_tile/issues/13">https://github.com/openstreetmap/mod_tile/issues/13</a> suggests that later versions may have less of an issue with this.</p>
<p>It looks like Ubuntu 22.04 <a href="https://packages.ubuntu.com/search?keywords=libapache2-mod-tile+&amp;searchon=sourcenames">will have</a> that later version in. Current released versions of <a href="https://packages.ubuntu.com/source/impish/libapache2-mod-tile">Ubuntu</a> and <a href="https://packages.debian.org/uk/bullseye/libapache2-mod-tile">Debian</a> do not yet.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Jan '22, 18:28</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-83193" class="comments-container">
&#10;</div>
<div id="comment-tools-83193" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83193-form-container" class="comment-form-container">
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


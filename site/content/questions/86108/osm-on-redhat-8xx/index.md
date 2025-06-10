+++
type = "question"
title = "OSM on Redhat 8.x.x"
description = '''Installing OS Map Tile server on a Redhat 8.x.x. I keep running into dependency-related issues. Also, I can&#x27;t seem to find many guides on this.  Is this possible? If so, does anyone have a guide or work arounds?'''
date = "2022-11-08T01:45:00Z"
lastmod = "2022-11-08T02:09:00Z"
weight = 86108
keywords = [ "osm", "linux" ]
aliases = [ "/questions/86108" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [OSM on Redhat 8.x.x](/questions/86108/osm-on-redhat-8xx)

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
<span id="post-86108-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86108-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86108-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Installing OS Map Tile server on a Redhat 8.x.x. I keep running into dependency-related issues. Also, I can't seem to find many guides on this.</p>
<p>Is this possible? If so, does anyone have a guide or work arounds?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-linux" rel="tag" title="see questions tagged &#39;linux&#39;">linux</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Nov '22, 01:45</strong></p>
<img src="https://secure.gravatar.com/avatar/f9fa8bc174e5bfdf6d96989df7f544a5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Soulless_Solo&#39;s gravatar image" />
<p><span>Soulless_Solo</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Soulless_Solo has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-86108" class="comments-container">
&#10;</div>
<div id="comment-tools-86108" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86108-form-container" class="comment-form-container">
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

<span id="86109"></span>

<div id="answer-container-86109" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86109-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86109-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-86109-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Presumably you don't mean <a href="https://www.redhat.com/en/about/press-releases/press-redhatlinux80">Redhat 8</a> from 2002 but actually <a href="https://developers.redhat.com/rhel8">RHEL 8</a> from 2022?</p>
<p>If so, <a href="https://en.wikipedia.org/wiki/Red_Hat_Enterprise_Linux#RHEL_8">this</a> says it's based on <a href="https://en.wikipedia.org/wiki/Fedora_Linux_release_history#Fedora_Linux_28">Fedora 28</a> which isn't listed <a href="https://github.com/openstreetmap/mod_tile/blob/master/.github/workflows/build-and-test.yml">here</a> although Fedora 33 and 34 are.</p>
<p>You have a few options:</p>
<ul>
<li>Choose a more mainstream distribution for this sort of thing (recent Ubuntu or Debian)</li>
<li>Use something like Docker</li>
<li>Try and build as per <a href="https://github.com/openstreetmap/mod_tile/blob/master/docs/build/building_on_centos_7.md">Centos 7</a></li>
<li>Try and build as per <a href="https://github.com/openstreetmap/mod_tile/blob/master/docs/build/building_on_fedora_34.md">Fedora 34</a></li>
</ul>
<p>You haven't said what you have tried and what hasn't worked - presumably you're following either the Centos 7 instructions above or the Fedora 34 ones. Whichever you're following that doesn't work, try the other one.</p>
<p>However, you will be able to save yourself an awful lot of pain if you start from Debian 11 or Ubuntu 22.04 LTS, as described <a href="https://github.com/openstreetmap/mod_tile/blob/master/README.rst">here</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Nov '22, 02:05</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-86109" class="comments-container">
<span id="86110"></span>
<div id="comment-86110" class="comment">
<div id="post-86110-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks. I have tried Ubuntu 22 and that works fine without a hitch. But the environment I am in will only allow a RHEL 8 or a Windows instance.</p>
</div>
<div id="comment-86110-info" class="comment-info">
<span class="comment-age">(08 Nov '22, 02:09)</span> <span class="comment-user userinfo">Soulless_Solo</span>
</div>
</div>
</div>
<div id="comment-tools-86109" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86109-form-container" class="comment-form-container">
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


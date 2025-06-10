+++
type = "question"
title = "SSL certificate for https://osm.org does not match the host name"
description = '''I have an issue with SSL certificate for osm.org domain. If you try to open url https://osm.org in browser you will get an error because SSL certificate does not match the host name. SSL certificate from openstreetmap.org domain is used at osm.org domain. Could you fix this?'''
date = "2014-06-03T08:46:00Z"
lastmod = "2014-06-03T13:22:00Z"
weight = 33639
keywords = [ "osm.org", "ssl" ]
aliases = [ "/questions/33639" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [SSL certificate for https://osm.org does not match the host name](/questions/33639/ssl-certificate-for-httpsosmorg-does-not-match-the-host-name)

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
<span id="post-33639-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33639-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-33639-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have an issue with SSL certificate for <code>osm.org</code> domain. If you try to open url <a href="https://osm.org"><code>https://osm.org</code></a> in browser you will get an error because SSL certificate does not match the host name. SSL certificate from <code>openstreetmap.org</code> domain is used at <code>osm.org</code> domain. Could you fix this?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm.org" rel="tag" title="see questions tagged &#39;osm.org&#39;">osm.org</span> <span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Jun '14, 08:46</strong></p>
<img src="https://secure.gravatar.com/avatar/0ef2ab19a5aaf4ee0cace45ef5aa6cda?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="knockpenny&#39;s gravatar image" />
<p><span>knockpenny</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="knockpenny has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Jun '14, 13:23</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-33639" class="comments-container">
&#10;</div>
<div id="comment-tools-33639" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33639-form-container" class="comment-form-container">
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

<span id="33640"></span>

<div id="answer-container-33640" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-33640-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33640-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-33640-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Don't use the osm.org domain, it is not officially supported. Our certificates are for openstreetmap.org, and the certificates will work perfectly there.</p>
<p>OSMF have tried to grab a couple of "lookalike" domains like osm.org, openstreetmaps.org, and others, just to avoid someone doing something silly with them. But we can't afford to buy proper certificates for each and every one of them.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Jun '14, 09:46</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-33640" class="comments-container">
<span id="33644"></span>
<div id="comment-33644" class="comment">
<div id="post-33644-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span></span><span>@knockpenny</span>: … and as a simple workaround (if you like to use osm.org) just check that you get the same certificate (hashes) as for openstreetmap.org and add a permanent exception to your browser.</p>
</div>
<div id="comment-33644-info" class="comment-info">
<span class="comment-age">(03 Jun '14, 13:22)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-33640" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33640-form-container" class="comment-form-container">
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


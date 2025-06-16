+++
type = "question"
title = "website search.php is not displayed"
description = '''Hi, I am having trouble viewing the nominations directory, I have the settings at https://nominatim.org/release-docs/latest/appendix/Install-on-Ubuntu-18/ contained in / srv / nominatim / build / settings local.php @define (&#x27;CONST_Website_BaseUrl&#x27;, &#x27;http: // localhost / nominatim /&#x27;); contained in /...'''
date = "2020-05-14T20:51:00Z"
lastmod = "2020-05-14T22:29:00Z"
weight = 74815
keywords = [ "nominatim", "apache2" ]
aliases = [ "/questions/74815" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [website search.php is not displayed](/questions/74815/website-searchphp-is-not-displayed)

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
<span id="post-74815-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74815-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74815-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I am having trouble viewing the nominations directory, I have the settings at <a href="https://nominatim.org/release-docs/latest/appendix/Install-on-Ubuntu-18/">https://nominatim.org/release-docs/latest/appendix/Install-on-Ubuntu-18/</a></p>
<p>contained in / srv / nominatim / build / settings local.php</p>
<p>@define ('CONST_Website_BaseUrl', 'http: // localhost / nominatim /');</p>
<p>contained in / etc / apache2 / conf-available</p>
<p>&lt;directory "="" srv="" nominatim="" build="" website"=""&gt; FollowSymLinks MultiViews options AddType text / html .php Require all awarded</p>
<p>Alias ​​/ nominatim / srv / nominatim / build / website</p>
<p>contained in 000-default.conf ServerAdmin webmaster @ localhost DocumentRoot / srv / nominatim</p>
<p>&lt;directory "="" srv="" nominatim="" build="" website"=""&gt; Options FollowSymLinks MultiViews AddType text / html .php DirectoryIndex search.php Require all granted</p>
<p>Alias ​​/ nominatim / srv / nominatim / build / website is not displayed in the browser http: //localhost/nominatim/search.php as if not entering nominatim</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-apache2" rel="tag" title="see questions tagged &#39;apache2&#39;">apache2</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 May '20, 20:51</strong></p>
<img src="https://secure.gravatar.com/avatar/224322734ba5aec7f8c1b96e32946ca1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="edderantonio&#39;s gravatar image" />
<p><span>edderantonio</span><br />
<span class="score" title="11 reputation points">11</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="edderantonio has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-74815" class="comments-container">
<span id="74817"></span>
<div id="comment-74817" class="comment">
<div id="post-74817-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The question is unreadable. Apache2 has no configuration setting "Require all awarded" (<a href="https://httpd.apache.org/docs/2.4/howto/access.html).">https://httpd.apache.org/docs/2.4/howto/access.html).</a></p>
</div>
<div id="comment-74817-info" class="comment-info">
<span class="comment-age">(14 May '20, 21:09)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
</div>
<div id="comment-tools-74815" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74815-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="74818"></span>

<div id="answer-container-74818" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74818-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74818-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74818-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I publish it again because I add characters that should not go I am having trouble viewing the nominations directory, I have the settings at <a href="https://nominatim.org/release-docs/latest/appendix/Install-on-Ubuntu-18/">https://nominatim.org/release-docs/latest/appendix/Install-on-Ubuntu-18/</a></p>
<p>contained in / srv / nominatim / build / settings local.php</p>
<p>@define ('CONST_Website_BaseUrl', 'http: // localhost / nominatim /');</p>
<p>contained in / etc / apache2 / conf-available</p>
<p>&lt;directory "="" srv="" nominatim="" build="" website"=""&gt; FollowSymLinks MultiViews options AddType text / html .php Require all awarded</p>
<p>Alias ​​/ nominatim / srv / nominatim / build / website</p>
<p>contained in 000-default.conf ServerAdmin webmaster @ localhost DocumentRoot / srv / nominatim</p>
<p>&lt;directory "="" srv="" nominatim="" build="" website"=""&gt; Options FollowSymLinks MultiViews AddType text / html .php DirectoryIndex search.php Require all granted</p>
<p>Alias ​​/ nominatim / srv / nominatim / build / website is not displayed in the browser http: //localhost/nominatim/search.php as if not entering nominatim</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 May '20, 21:46</strong></p>
<img src="https://secure.gravatar.com/avatar/224322734ba5aec7f8c1b96e32946ca1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="edderantonio&#39;s gravatar image" />
<p><span>edderantonio</span><br />
<span class="score" title="11 reputation points">11</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="edderantonio has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-74818" class="comments-container">
&#10;</div>
<div id="comment-tools-74818" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74818-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="74820"></span>

<div id="answer-container-74820" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74820-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74820-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74820-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>here is correct</p>
<p><img src="/upfiles/4.png" alt="alt text" /></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 May '20, 22:25</strong></p>
<img src="https://secure.gravatar.com/avatar/224322734ba5aec7f8c1b96e32946ca1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="edderantonio&#39;s gravatar image" />
<p><span>edderantonio</span><br />
<span class="score" title="11 reputation points">11</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="edderantonio has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-74820" class="comments-container">
<span id="74821"></span>
<div id="comment-74821" class="comment">
<div id="post-74821-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Read the website <a href="https://nominatim.org/release-docs/latest/appendix/Install-on-Ubuntu-18/">https://nominatim.org/release-docs/latest/appendix/Install-on-Ubuntu-18/</a> carefully. There are no spaces around ' / ', there is no 'Require all awarded', there is no '000-default'.</p>
</div>
<div id="comment-74821-info" class="comment-info">
<span class="comment-age">(14 May '20, 22:29)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
</div>
<div id="comment-tools-74820" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74820-form-container" class="comment-form-container">
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


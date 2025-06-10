+++
type = "question"
title = "mod_tile not rendering second style"
description = '''Hi everybody,  I have a mod_tile instance working and already serving a style. I have now added another style (it works properly if I try to render an image with nik4) but I&#x27;m not able to get the images from mod_tile. On the browser I get 404 (Not Found) answer and in the renderd windows (since I la...'''
date = "2021-10-17T22:39:00Z"
lastmod = "2021-10-17T23:31:00Z"
weight = 82214
keywords = [ "mod_tile" ]
aliases = [ "/questions/82214" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [mod_tile not rendering second style](/questions/82214/mod_tile-not-rendering-second-style)

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
<span id="post-82214-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82214-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82214-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi everybody,</p>
<p>I have a <code>mod_tile</code> instance working and already serving a style. I have now added another style (it works properly if I try to render an image with nik4) but I'm not able to get the images from <code>mod_tile</code>.</p>
<p>On the browser I get 404 (Not Found) answer and in the renderd windows (since I launched it with -f flags to see the output) I get "Received request for map layer 'wikihiking' which failed to load"</p>
<p>Is there a way to have more debug info?</p>
<p>In the case I can share my configuration files</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mod_tile" rel="tag" title="see questions tagged &#39;mod_tile&#39;">mod_tile</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Oct '21, 22:39</strong></p>
<img src="https://secure.gravatar.com/avatar/5c1da2c4e653e42553126d1ef1714fcd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lucadelu&#39;s gravatar image" />
<p><span>lucadelu</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lucadelu has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-82214" class="comments-container">
<span id="82215"></span>
<div id="comment-82215" class="comment">
<div id="post-82215-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<blockquote>
<p>In the case I can share my configuration files</p>
</blockquote>
<p>Please do.</p>
<blockquote>
<p>I get "Received request for map layer 'wikihiking' which failed to load"</p>
</blockquote>
<p>Somewhat higher up the logfile you should be able to see why it failed to load.</p>
</div>
<div id="comment-82215-info" class="comment-info">
<span class="comment-age">(17 Oct '21, 22:48)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="82216"></span>
<div id="comment-82216" class="comment">
<div id="post-82216-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>If you haven't misconfigured something, then the "works with nik4 but not in renderd" situation might point to a permisssion issue - maybe your style tries to access a file that is available to you but not to the user renderd runs under, or the style is set to connect to the database with the current unix user and there's no database user for the user renderd runs under.</p>
</div>
<div id="comment-82216-info" class="comment-info">
<span class="comment-age">(17 Oct '21, 23:04)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="82218"></span>
<div id="comment-82218" class="comment">
<div id="post-82218-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Changing user it works properly, thanks Frederik</p>
</div>
<div id="comment-82218-info" class="comment-info">
<span class="comment-age">(17 Oct '21, 23:31)</span> <span class="comment-user userinfo">lucadelu</span>
</div>
</div>
</div>
<div id="comment-tools-82214" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82214-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>


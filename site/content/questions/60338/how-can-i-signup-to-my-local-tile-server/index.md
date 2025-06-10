+++
type = "question"
title = "How can I signup to my local tile server?"
description = '''I use Rails to point my local server. I can see my local map in web browser when i type localhost:3000.But When I try to sign up, The error occours: Parameters: {&quot;utf8&quot;=&amp;gt;&quot;✓&quot;, &quot;authenticity_token&quot;=&amp;gt;&quot;+DRjYos1zxLzd5iDC9AZyUX5UqN3lhiUUcLmHmU5FAy2r6TRQoarVoC2ci/Fe4w9p/u9JA4x05BwRlhAJCPatA==&quot;, &quot;user...'''
date = "2017-10-28T14:11:00Z"
lastmod = "2017-11-24T14:11:00Z"
weight = 60338
keywords = [ "signup", "error" ]
aliases = [ "/questions/60338" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How can I signup to my local tile server?](/questions/60338/how-can-i-signup-to-my-local-tile-server)

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
<span id="post-60338-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60338-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-60338-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I use Rails to point my local server. I can see my local map in web browser when i type localhost:3000.But When I try to sign up, The error occours: Parameters: {"utf8"=&gt;"✓", "authenticity_token"=&gt;"+DRjYos1zxLzd5iDC9AZyUX5UqN3lhiUUcLmHmU5FAy2r6TRQoarVoC2ci/Fe4w9p/u9JA4x05BwRlhAJCPatA==", "user"=&gt;{"email"=&gt;"yuanyahui11@gmail.com", "email_confirmation"=&gt;"yuanyahui11@gmail.com", "display_name"=&gt;"yeager", "auth_provider"=&gt;"", "pass_crypt"=&gt;"[FILTERED]", "pass_crypt_confirmation"=&gt;"[FILTERED]"}, "commit"=&gt;"Sign Up"} Can't verify CSRF token authenticity. How can I sovle this,Hope I can get help .Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-signup" rel="tag" title="see questions tagged &#39;signup&#39;">signup</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Oct '17, 14:11</strong></p>
<img src="https://secure.gravatar.com/avatar/66e4305afae2faf808a2b600525c4cc9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gleide&#39;s gravatar image" />
<p><span>gleide</span><br />
<span class="score" title="79 reputation points">79</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gleide has one accepted answer">50%</span></p>
</div>
</div>
<div id="comments-container-60338" class="comments-container">
<span id="60353"></span>
<div id="comment-60353" class="comment">
<div id="post-60353-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Please be a bit clearer. Are you running your own instance of the rails port? If yes <a href="https://github.com/openstreetmap/openstreetmap-website/blob/master/CONFIGURE.md">https://github.com/openstreetmap/openstreetmap-website/blob/master/CONFIGURE.md</a> has configuration information.</p>
</div>
<div id="comment-60353-info" class="comment-info">
<span class="comment-age">(29 Oct '17, 19:52)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="60355"></span>
<div id="comment-60355" class="comment">
<div id="post-60355-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>In addition, would it be possible to take a step back and explain what problem you are trying to solve - what is your goal?</p>
</div>
<div id="comment-60355-info" class="comment-info">
<span class="comment-age">(29 Oct '17, 20:05)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="60361"></span>
<div id="comment-60361" class="comment">
<div id="post-60361-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I did run my own instance of the rails port. I first build a local tile server following the guide: <a href="https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/.Then">https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/.Then</a> I want to edit my local title server without changing openstreetmap server's data.So I used Rails port to point my local server.I want to use JOSM to edit my data and upload to my http//localhost:3000/api.Then I need to Authentication.So I want to sign up my local server.But I failed.I am sorry my English is poor.Thanks for your help!</p>
</div>
<div id="comment-60361-info" class="comment-info">
<span class="comment-age">(30 Oct '17, 15:55)</span> <span class="comment-user userinfo">gleide</span>
</div>
</div>
<span id="60362"></span>
<div id="comment-60362" class="comment">
<div id="post-60362-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>After I run rails server.In web browser,I type <a href="http://localhost:3000">http://localhost:3000</a>,I saw my local map.The page are very similar to openstreetmap.org's.The only differences is is showed my own tile.So I click Signup,But cannot success.It shows the error above.</p>
<p>Sincerely hope to get your help.Thanks!!!</p>
</div>
<div id="comment-60362-info" class="comment-info">
<span class="comment-age">(30 Oct '17, 16:09)</span> <span class="comment-user userinfo">gleide</span>
</div>
</div>
<span id="60764"></span>
<div id="comment-60764" class="comment">
<div id="post-60764-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>For info for anyone looking to answer there's a bit more info on a related question from the same person <a href="https://help.openstreetmap.org/questions/60716/how-can-edit-my-local-tile-server-without-uploading-changes-to-openstreetmap-server">https://help.openstreetmap.org/questions/60716/how-can-edit-my-local-tile-server-without-uploading-changes-to-openstreetmap-server</a> that adds a bit of context here.</p>
</div>
<div id="comment-60764-info" class="comment-info">
<span class="comment-age">(24 Nov '17, 11:21)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-60338" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60338-form-container" class="comment-form-container">
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

<span id="60765"></span>

<div id="answer-container-60765" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60765-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60765-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-60765-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Finally I solved this problem by creating a blank file at tmp/cache-dev.txt. This will turn on a local in-memory cache store, which will be used to store your user session data. Hope this can help those who met the same problem.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Nov '17, 14:11</strong></p>
<img src="https://secure.gravatar.com/avatar/66e4305afae2faf808a2b600525c4cc9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gleide&#39;s gravatar image" />
<p><span>gleide</span><br />
<span class="score" title="79 reputation points">79</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gleide has one accepted answer">50%</span></p>
</div>
</div>
<div id="comments-container-60765" class="comments-container">
&#10;</div>
<div id="comment-tools-60765" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60765-form-container" class="comment-form-container">
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

